# 03 — Check-then-act races & optimistic concurrency

**Problem.** Two requests, workers or replicas run `if (!exists) insert` or `if (status==X) update` at the same time, and both pass the check.
In-memory domain guards do **not** help across two `DbContext`s or two pods.

**Fixes, by situation**
- **Uniqueness:** use a DB unique constraint; the DB is the only shared referee.
- **Conditional state change:**
  - Option 1: run `UPDATE … WHERE id=@id AND status=@expected` and check rows-affected.
  - Option 2: use a **concurrency token** (EF `[Timestamp]` / Postgres `xmin`). A conflict raises `DbUpdateConcurrencyException`; return 409 or 412.
- **Counters/balances:** use an atomic `UPDATE x SET n = n - 1 WHERE n > 0`, or `SELECT … FOR UPDATE` inside the transaction.
- **Singleton jobs across replicas:** use a distributed lock or lease, `DisableConcurrentExecution`, or idempotent set-based sweeps.
- **In-process shared objects:** don't share mutable entities between request handlers and background workers. Copy them or lock.

**How to prove it:** write a test that fires N concurrent calls (`Task.WhenAll`) and asserts the *final state* (exactly one invoice, the exact balance), not just status codes.

**Worked examples in your repos**
- netintercom: `training/incidents/003-sla-escalation-storm` (3 replicas) and `ladder/M1–M2`. Note that `docs/architecture-review.md` §2.3 wrongly claims overlapping sweeps throw.
- netstripe: review finding 1, a duplicate-invoice race in `BillingEngine.RunBillingCycle`/`GenerateInvoice`.
- netramp: review finding 4. `Expense` is changed by both HTTP handlers and the background worker with no lock, despite a "thread-safe" comment.

**Where these repos live now.** netintercom → `elirc/dotnet-intercom` · netstripe → `elirc/dotnet-stripe` · netramp → `elirc/dotnet-ramp`. Re-read on 2026-10-06 at dotnet-intercom `74e0a28`, dotnet-stripe `8f40257` and dotnet-ramp `709feb8`. Line numbers are for those commits.

> **Correction to the list above.** dotnet-intercom's ladder M1 is `M1-inbox-query-at-scale.md` (query performance). The concurrency rungs are **J1** (`J1-concurrent-close-409.md`) and **M2** (`M2-idempotent-visitor-send.md`). INC-003's branch is not on GitHub, so work it from the brief (`training/README.md` explains how). The repo has since added a status note at the top of `docs/architecture-review.md` (line 5) confirming that §2.3 is wrong.

---

## Worked trace: dotnet-intercom's SLA sweep on three replicas

The job is registered once per app start: `elirc/dotnet-intercom: src/NetIntercom.Api/Program.cs:190`, `RecurringJob.AddOrUpdate<SlaBreachJob>("sla-breach-check", …, Cron.Minutely)`. `SlaBreachJob.RunAsync` (`src/NetIntercom.Infrastructure/BackgroundJobs/SlaBreachJob.cs:16`) sends `CheckSlaBreachesCommand`. Its handler, `src/NetIntercom.Application/Sla/CheckSlaBreaches.cs`, does four things:

1. **Read.** Lines 34-40 load every `SlaTimer` with `Status == Running && BreachAtUtc <= now` into *this run's* `DbContext`.
2. **Check + act in memory.** Line 44 calls `timer.MarkBreached(now)`. The guard is in `src/NetIntercom.Domain/Entities/Sla.cs:42-50`: `if (Status != SlaTimerStatus.Running) throw new DomainException(...)`, then it sets `Status = Breached`.
3. **Write.** Line 53 calls `SaveChangesAsync`.
4. **Notify.** Lines 54-58 push `SlaBreachedAsync` for each timer.

## The failure window, step by step

Two sweeps, S1 and S2, start in the same minute. They can be on two replicas, or be two schedules (INC-003's PR #240 registered one recurring job id per machine name, so ids piled up across deploys).

| t | S1 | S2 | DB row |
|---|---|---|---|
| 0 | loads timer T (`Running`) | | `Running` |
| 1 | | loads timer T (`Running`), a separate `DbContext` instance | `Running` |
| 2 | `MarkBreached`: guard sees `Running` → OK | | `Running` |
| 3 | | `MarkBreached`: guard sees **its own copy**, still `Running` → OK | `Running` |
| 4 | `UPDATE … SET Status='Breached'` → 1 row | | `Breached` |
| 5 | | `UPDATE … WHERE Id=@id` → 1 row (no token, so no conflict) | `Breached` |
| 6 | notify | notify | two toasts |

Why does step 5 succeed? `SlaTimer`'s EF mapping (`src/NetIntercom.Infrastructure/Persistence/AppDbContext.cs:95-99`) has an index and a relationship but **no concurrency token**. EF's `UPDATE` therefore filters on the primary key alone. Compare `Conversation`, which *does* map `xmin` as a row version (`AppDbContext.cs:78-79`, and `src/NetIntercom.Domain/Entities/Conversation.cs:30-31`). If `SlaTimer` had the same token, S2's update would match zero rows and EF would throw `DbUpdateConcurrencyException`.

This is exactly where `docs/architecture-review.md` §2.3 (line 74) goes wrong: it predicts that "the loser … throws `DomainException`". The domain guard only sees in-memory state, so it can't see the other process. INC-003's brief says it directly: the guard "has never fired".

**Fixes, ranked:**
1. A set-based claim: `UPDATE "SlaTimers" SET "Status"='Breached' … WHERE "Status"='Running' AND "BreachAtUtc" <= @now RETURNING …`. Only the rows *you* flipped get notified.
2. A concurrency token on `SlaTimer`, catching the conflict per timer.
3. `[DisableConcurrentExecution]` on the job. That covers overlapping runs of one recurring id, but not PR #240's many ids.

## Second example: dotnet-stripe's billing cycle

`elirc/dotnet-stripe: src/Billing.Api/Infrastructure/BillingEngine.cs:115-127`. `RunBillingCycle` checks `subscription.CurrentPeriodEnd <= billingDate` (line 120) against a snapshot array (`BillingStore.Subscriptions()` returns `.ToArray()` under a lock, `BillingStore.cs:41`). Then `GenerateInvoice` (line 9) builds the invoice and does three *separately* locked writes: `SaveInvoice` (82), `SaveUsageEvents` (83) and `SaveSubscription` with the advanced period (84-88). Two concurrent `POST /api/simulator/run-cycle` calls (`Program.cs:204-209`) can both read the old `CurrentPeriodEnd` before either reaches line 84, so they produce **two invoices for one period**. Each `BillingStore` method is thread-safe. The read-decide-write sequence across them isn't. Same lesson as above: per-call locking doesn't make a multi-step operation atomic.

## Verified senior findings

- **The lock only protects the dictionary.** `elirc/dotnet-ramp: backend/Storage/DataStore.cs:11-12` says "ConcurrentDictionary makes individual reads/writes thread-safe, which matters because the background worker mutates entities on a separate thread". That's true of the dictionary and false of the `Expense` objects inside it. `ExpenseService.Transition` (`backend/Services/ExpenseService.cs:169-179`) checks at line 171, sets `Status` at 176 and appends to `History` at 178. `History` is a plain `List<ExpenseEvent>` (`backend/Domain/Expense.cs:39`). `BackgroundJobs.ProcessReimbursement` (`backend/Background/BackgroundJobs.cs:40-69`) mutates the same instance at 58-66 on the worker thread.
- **A nuance worth arguing in review.** B01's review finding 4 says two concurrent `POST /reimburse` calls can give a "double payment in the worst case". Reading the current code: `StartReimbursement` (`ExpenseService.cs:150-156`) does let both callers pass the check at 171, and both enqueue a job (line 154). But `QueuedHostedService.cs:28-43` awaits jobs one at a time, and the job re-checks `CanSystemTransition` (`BackgroundJobs.cs:51`). So the second job logs "not in a reimbursable state" and returns. The visible damage *today* is a duplicated `Approved → Reimbursing` history entry, plus an unsynchronized `List.Add`. The double-payment risk becomes real once the worker runs jobs in parallel or the "payment" stops being simulated. (This is inferred from reading the code, not from a run.)

## Goal + Check ladder

**Goal:** spot a check-then-act in review, explain it as an interleaving table, and pick the fix that makes the database the referee.

1. **Junior: find the check and the act.** In `CheckSlaBreaches.cs`, mark the read, the check and the write.
   **Check:** read = 34-40, check = `Sla.cs:44` (inside `MarkBreached`, called at line 44 of the handler), write = 53.
2. **Junior: prove there's no token.** `grep -n "IsRowVersion\|IsConcurrencyToken" src/NetIntercom.Infrastructure/Persistence/AppDbContext.cs`.
   **Check:** exactly one hit, at line 79, and it's on `Conversation`, not `SlaTimer`.
3. **Junior+: dotnet-intercom J1** (`training/ladder/J1-concurrent-close-409.md`). That rung uses the `Conversation` token you just found.
   **Check:** the sealed `_answers/ladder-J1.md` agrees with your status code and with where you catch `DbUpdateConcurrencyException`.
4. **Mid: write the interleaving table** for dotnet-stripe's `RunBillingCycle`, without looking at the section above.
   **Check:** your table has both calls reading a stale `CurrentPeriodEnd` before line 84. Then do item 6 of `training/review/characterization-tests-billingengine.md`, which pins the current behavior.
5. **Mid→senior: INC-003 tasks 1-4.** The branch isn't on GitHub, so recreate PR #240's diff from the brief on a local branch.
   **Check:** your fix notifies only rows your statement flipped. *Run locally* (needs Docker for the integration tests): two concurrent handler invocations against one Postgres should produce one `Breached` transition and one notification.

## Debugging scenario

*"After scaling to 3 replicas, every breached chat toasts 3-4 times. Hangfire shows 0 failures."*

1. Zero failures tells you the duplicates *succeed*, so look for a missing referee, not an exception.
2. Count the schedules: `hangfire.set` where `key = 'recurring-jobs'` (the query is in the INC-003 brief). More than one `sla-breach-check*` row means multiple schedules.
3. Even with one schedule, check whether runs can overlap. Look at the mapping for `SlaTimer` (no token) and at the handler (read, then save).
4. Confirm with logs: the same conversation id is logged by `CheckSlaBreaches.cs:45-48` from different `host` values within the same second.
5. Fix with a set-based claim, clean up the stray recurring ids, and add a concurrent test that asserts *one notification*, not just "no exception".
