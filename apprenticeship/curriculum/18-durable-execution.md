# 18 — Durable execution: checkpoints, determinism, leases, timers

**Problem.** A workflow runs for minutes to days across many steps and external calls. Processes crash, deploys happen, and queues redeliver.
You need "every step runs to completion effectively-once, and the workflow resumes where it left off."

**Two resume models**
- **Checkpoint & skip:** persist each step's result; on resume, skip the steps that have results. This is simple, but step identity must be **stable**: positional step ids collide when a definition changes.
- **Event-history replay** (Temporal-style): re-run workflow code against the recorded history. The code must be **deterministic** (no `Date.now()`, random or I/O outside activities).

**The contracts that make it work**
1. **Pin the definition version per run.** In-flight runs resume on the version they started with; new runs use the latest. Resuming on "latest" duplicates or skips side effects.
2. **Read the checkpoint before every side effect.** Skipping that read means duplicate emails or posts after a worker rotation.
3. **Activities are idempotent**, keyed by something stable across replay. A key derived from a *new* run id breaks "safe replay" ([02](02-idempotency.md)).
4. **Leases + fencing, not just queue locks.** A worker holds a lease it renews by heartbeat, and its writes carry a fencing token so a zombie worker's late writes are rejected.
5. **Durable timers live in the DB**, not in `setTimeout` or queue delays alone, and a sweeper wakes due runs. Otherwise parked runs never wake.
6. **Bounded retries with a terminal state.** "Retriable failed" must not loop forever; add DLQ/parking and an alert.
7. **History growth is a performance problem.** Heartbeat events and large outputs bloat the run table: offload, compact, and page.

**Worked examples in your repos**
- **relay** (the main lab; its runnable `training/lab/` has Postgres, Redis, a fake vendor farm and the real worker):
  - `main` can't boot: BullMQ rejects the queue name `relay:runs`, while 151 tests stay green. That's ticket J1 and [05](05-verify-before-trust.md).
  - Incidents:
    - 001 resume on the latest version: duplicate emails
    - 002 parked runs never wake
    - 003 checkpoint read skipped: 2 chat posts instead of 1
    - 004 retriable-failed loop: +3M history rows
    - 005 heartbeat events: the run page takes 3.4 s at 50k events
  - Ladder M1–M4 (determinism, leases/fencing, versioning, timers), S1 (multi-day onboarding with compensation, see [16](16-sagas-vs-2pc-vs-outbox.md)), S2 (migrating in-flight state).
- **buildermentor:** `training/incidents/005-genjob-expiry` (a pg-boss expiry is not a kill switch: 4 handler runs).
- **atlas:** `training/ladder/S2` (payroll preparation as a durable job).
- **buildevent:** expiry jobs that are never imported (review finding).
