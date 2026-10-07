# 16 — Sagas vs 2PC vs outbox: keeping multi-step work consistent

**Where these repos live now (checked 2026-10-06):** astra5 (Stockade) → `elirc/stockade` (`main` @ `ad27b1c`; branch `training/incidents/001-payment-status-drift` **is** on GitHub. No repo is named "astra5": `gh repo list elirc -L 1000` has none, and `batch5report/projects/astra5.md` is titled "astra5 — Stockade") · relay → `elirc/gitvg`, folder `relay/training/` (`main` @ `af91bab`; the standalone `elirc/relay` has no `training/`) · eShop → `elirc/netopen1` (`eShop/training/`, `main` @ `4bb1118`) · modular-monolith-with-ddd → `elirc/netarchitectureproject` (`modular-monolith-with-ddd/training/`, `main` @ `bf7fa14`) · atlas → `elirc/gitvg`, folder `atlas/training/`.

**Problem.** A business action spans several services or resources: reserve stock, capture the payment, ship.
There is no single database transaction around all of them. What do you do when step 3 fails after steps 1–2 committed?

| Approach | How | Use when | Costs |
|---|---|---|---|
| **2PC / distributed transaction** | a coordinator locks all participants, then commits all | the participants support it and hold times are tiny | blocking, a coordinator SPOF, and it's unsupported by most modern stores and APIs (Stripe can't take part) |
| **Outbox** ([01](01-transactional-outbox.md)) | one local transaction writes the state plus an event, then relays it | *one* service must reliably tell others about its own change | it's a building block, not a multi-step workflow |
| **Saga (orchestrated)** | a coordinator runs steps and, on failure, runs **compensations** in reverse | multi-step business processes across services and external APIs | compensations must be idempotent; a workflow state machine is required |
| **Saga (choreographed)** | services react to each other's events | a few loosely coupled steps | the flow is invisible, and hard to debug and change |

**Rules that make sagas actually work**
1. **Every step and every compensation is idempotent** ([02](02-idempotency.md)); both will be retried.
2. **Persist saga state *with* the step's effect** in one local transaction. If they're split across two commits, a crash leaves a step done but unrecorded.
3. **Compensation is a business action, not a rollback.** A refund is not "un-capture", and some steps (sending an email) can't be undone.
4. **Every non-terminal state needs a timeout and a recovery scan,** plus an alert on "stuck for more than X". A saga that can hang forever will.
5. **Contracts between steps are versioned.** A renamed enum value can silently route an order into a state nothing handles.

**Worked examples in your repos**
- **astra5 (Stockade, Next.js + .NET):**
  - `training/incidents/001-payment-status-drift`: a Stripe `requires_action` mapping drift means 3-D Secure orders fall out of reconciliation forever.
  - Real finding: the `void_pending` branch of `services/Fulfil/Services/Worker.cs` (lines 69-75 at `ad27b1c`; the B05 report cited 70-78) splits capture-then-compensate across two committed transactions, so a crash leaves a captured order invisible to recovery *and* to the `stuckSagas` metric.
  - The interview set covers sagas vs 2PC vs outbox (`training/interview/TECHNICAL_QUESTIONS.md`).
- **relay:** `elirc/gitvg: relay/training/ladder/S1-onboarding-approval-workflow.md`, a multi-day onboarding workflow with human approval, with one compensation per forward step, run in reverse. The "what has been done" list comes from the StepRun checkpoints, and a compensation that itself fails goes to a human queue ("never infinite"). Engine mechanics are covered in [18](18-durable-execution.md).
- **eShop:** choreographed order flow via integration events (`elirc/netopen1: eShop/training/navigation/01-checkout-outbox-correctness.md`).
- **modular-monolith-with-ddd:** cross-module integration events plus an internal-command queue (`training/navigation/03-integration-event-flow-meeting-attendee-added.md`; the internal-command queue is in `04-outbox-inbox-processing.md` §"Internal commands").
- **atlas:** outbox plus webhook delivery; ticket `atlas/training/ladder/S2-payroll-as-a-background-job.md` turns payroll preparation into a durable job.

---

## Worked trace: Stockade's orchestrated payment saga (`elirc/stockade` @ `ad27b1c`)

The orchestrator is a polling `BackgroundService`, `services/Fulfil/Services/Worker.cs`.

1. **Recovery scan, every 1.5 s.** `:24` selects up to 20 orders whose `PaymentState` is one of `pending, authorizing, authorized, capturing, unknown, action_required, void_pending`, with `Attempts < 12` and `UpdatedAt` older than 2 s. `:34` sleeps 1,500 ms between ticks. **This list is the saga's state contract.** Any state not on it is treated as terminal.
2. **One runner per order.** `:59` takes a lease, which is a Postgres session advisory lock on `"order:" + id` (`:37-43`). If another worker holds it, this one skips the order.
3. **Record intent before the side effect.** `Stage` (`:124`) runs in a transaction: it sets `PaymentState = "authorizing"` and inserts a `PaymentAttempt` row *before* `payments.Authorize` is called (`:82-83`). A crash after the provider call leaves a recorded attempt that the next scan reconciles.
4. **Record the result with its effect and its event.** `:84-90` writes the provider id, the new states and the attempt row in one `tx.Run`. `Emit` (`:127-128`) adds an `OrderEvent` *and* an `OutboxEvent` to the same `DbContext`, so state, history and the outgoing message commit together. That is rule 2, and it's the outbox inside a saga.
5. **Every transaction is Serializable, with retries.** `services/Fulfil/Data/Transactions.cs:12-22`: `Run` opens a Serializable transaction, and on `40001`/`40P01`/`23505` (`:23`) rolls back and retries up to 16 times with a small jittered delay.
6. **Unknown outcomes back off.** `Unknown` (`:125`) sets `PaymentState = "unknown"`, increments `Attempts`, and pushes `UpdatedAt` forward by `min(120, Attempts × 5)` seconds. That's a durable retry timer.
7. **The "stuck" alert.** `services/Fulfil/Services/ReadApi.cs:70` reports `stuckSagas` as the count of orders with `Attempts >= 12`, and the Next.js health panel shows it as "Stuck payments" (`src/lib/health.ts:11`).

## Failure mode, step by step: the crash window in `void_pending`

1. A customer cancels after authorization, so the order is `void_pending`.
2. The worker asks the provider for the payment's state (`:69`). The provider says it was **captured** (`:70`), so money moved anyway.
3. `:72` calls `CompleteCapture`, which is its own `tx.Run` (`:129-137`). It **commits** `PaymentState = "captured"`, order state `paid`, held stock, and an `order.paid` outbox event.
4. *The process dies here.* (Deploy, OOM, or a node restart.)
5. `:73` would have run the compensation in a second transaction: release stock, reserve a refund for the remainder, transition to `cancelled`, and emit `order.cancelled`. It never runs.
6. On the next tick, `:24` does not select the order, because `captured` isn't on the list. `Attempts` is still below 12, because only `Unknown()` increments it, so `stuckSagas` reads 0. The customer cancelled but is charged and shipped, and nothing alerts.

The fix is rule 2: do the capture bookkeeping *and* the compensation (or a durable "compensation pending" marker) in one transaction, and give that marker a place in the scan list.

## Goal + **Check** ladder

1. **Goal (junior):** write down the saga's states. **Check:** copy the seven states from `Worker.cs:24`. For each one, find the line that moves an order *out* of it (for example `authorizing` → `:86`).
2. **Goal (junior):** show that state and events commit together. **Check:** confirm that `Emit` (`:127-128`) is only ever called inside a `tx.Run` lambda (`grep -n "Emit(" services/Fulfil/Services/Worker.cs`). Explain why that makes the outbox reliable.
3. **Goal (junior → mid):** find every two-commit sequence. **Check:** list the places where one `await tx.Run(...)` or `CompleteCapture` is followed by another without a durable marker in between. `:72-73` is one. Compare your list with `training/_answers/review.md`, which cites `Worker.cs:65-79` and `:129-137`.
4. **Goal (mid):** reproduce INC-001 by reading the diff. **Check:** `git diff main origin/training/incidents/001-payment-status-drift` changes one line in `services/Fulfil/Services/Payments.cs` (line 79 on `main`): `"requires_action" => "action_required"` becomes `"requires_action" => "requires_action"`. Explain why that one string removes 3-D Secure orders from the scan at `:24`.
5. **Goal (mid → senior):** design relay S1's failure-window table. **Check:** for every await in the onboarding flow, your table states the persisted state before and after it, who resumes it, and which compensation runs, and it bounds compensation failure with a human queue.

## Verified senior findings

- **The metric measures the wrong thing.** `stuckSagas` counts `Attempts >= 12` (`ReadApi.cs:70`), which is "retries exhausted", not "non-terminal for too long". An order that leaves the scan list without failing, as in the crash window or INC-001, never increments `Attempts`. A senior metric is "age of the oldest order in a non-terminal state", computed over *every* non-terminal state, not just the scanned ones.
- **The lease is session-wide.** `SessionLease.DisposeAsync` runs `SELECT pg_advisory_unlock_all()` (`Worker.cs:51`) instead of unlocking its own key. The review answer flags it at `Worker.cs:44-55`. It's harmless only while each connection holds exactly one lease.

## Debugging scenario: INC-001, "stuck on 'Confirm your payment with your bank' forever"

Symptoms from the brief: `State: authorized`, an unfamiliar payment state, no `OrderEvent` rows after `reserved`, `Attempts: 0`, and `stuckSagas = 0`. (1) `Attempts: 0` plus no events means the worker **never picked the order up**. It isn't a failing retry. (2) So compare the order's `PaymentState` with the scan list at `Worker.cs:24`. `requires_action` isn't on it, while `action_required` is. (3) Find who writes that value: the provider-status map in `Payments.cs:79`. (4) The fix restores the mapping, and the lesson is rule 5. Contract values between steps need a test that every provider status maps into the scan list or into an explicit terminal state, plus an alert on unknown states.

**Honesty cap:** Stockade's saga was a DRILL in B05: `dotnet build` passed for the incident, but the crash window was found by reading, not by killing a process mid-saga. I re-read the code and diffed the pushed branch on 2026-10-06 and ran nothing. The relay, eShop, modular-monolith and atlas references point to training docs I opened but didn't re-trace line by line, so their file:line claims live in those docs, not here.
