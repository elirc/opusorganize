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
