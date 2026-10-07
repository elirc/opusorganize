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
    *Dated:* lab-proven at B05 (2026-09-24). At elirc/relay HEAD `27a74af` (2026-10-02) the literal is still there (`apps/api/src/queue.ts:16`, `apps/engine/src/worker.ts:25`) and the lockfile still pins `bullmq@5.79.3`, so the bug should still reproduce. Not re-run on 2026-10-06; the 151-test count is from B05.
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

**Where these repos live now (checked 2026-10-06).**
relay → code at `elirc/relay` (main only, `27a74af`); its `training/` tree is at `elirc/gitvg: relay/training/` (`af91bab`), **not** on elirc/relay main. The branches `training/base/engine-boots` and `training/incidents/001..005` are **not on GitHub** (`git ls-remote` shows only `main` on elirc/relay and no `training/*` heads on elirc/gitvg).
atlas → `elirc/gitvg: atlas/training/` (elirc/atlas main `19e8c2d` has no `training/`).
buildermentor → `elirc/buildermentor` (main `8fcdb9d`; `training/incidents/005-genjob-expiry` is pushed, `c14f85d`).
buildevent → `elirc/build-event` (main `b941e78`).

---

## Worked trace: one versioned run through relay's engine

All lines below were opened at elirc/relay `27a74af`.

1. **Truth first, then work.** A webhook writes the Run row, then enqueues a pointer to it: `prisma.run.create` at `elirc/relay: apps/api/src/routes/hooks.ts:20`, then `enqueueRun(run.id)` at `:27`. The job carries only `{ runId }` (`apps/api/src/queue.ts:30`). Postgres is the source of truth; Redis just holds "go execute run X".
2. **No retry budget on the message.** `queue.ts:30` passes `{ removeOnComplete: 1000, removeOnFail: 5000 }` and **no `attempts`**, so BullMQ's default of one attempt applies. Keep that in mind for step 7.
3. **Pinned version.** The worker loads the run *with its own version* (`apps/engine/src/worker.ts:235`, `include: { version: true, relay: true }`) and parses `run.version.definition` (`:248`). This is contract 1, and the schema comment says so: "A Run pins the version it started on" (`packages/db/prisma/schema.prisma:147`, field `versionId` at `:167`).
4. **The checkpoint read.** Before executing anything, `worker.ts:162` loads every `StepRun` with `status: "succeeded"` for this run, and `:165-167` turns matching step ids into a `completed` set. This is contract 2: it runs on **every** delivery, not just "retries".
5. **Skip or execute.** `apps/engine/src/executor.ts:96-100`: a completed step's output is rehydrated with `loadPersistedOutput` and **not** re-executed. Otherwise the config is rendered (`:103`), the action runs with in-process retries (`:106`, `runWithRetry` at `:61-74`), and only then is the checkpoint written (`:107`).
6. **The idempotency key.** Inside `runAction`, `deriveIdempotencyKey(action.idempotency, runId, step.id, parsed)` (`worker.ts:115`; implementation `apps/engine/src/idempotency.ts:14-33`) returns `${runId}:${stepId}` for `vendorKey` and `dedupeWindow`, or a content key for `naturalKey`. MailPost and CalendarLite declare `vendorKey` (`packages/connectors/src/mailpost.ts:25`, `calendarlite.ts:26`); ChatBox declares `dedupeWindow` (`chatbox.ts:24`), for which `idempotencyHeader` sends **no** header (`idempotency.ts:36-39`).
7. **Failure.** `worker.ts:255-257` marks the run `failed` and rethrows with the comment "a retried delivery resumes from the last persisted step". Because of step 2, there is no retried delivery: a thrown run stays failed. (B05 review finding #3, still true at `27a74af`.)

### The failure mode, step by step: the crash window

The executor documents its own gap (`executor.ts:79-86`, and the inline comment at `:107`):

1. Step `s1` (ChatBox post) is rendered and sent. ChatBox accepts it and posts the message.
2. Before `persistStep` (`executor.ts:107`) commits, the pod is SIGKILLed.
3. BullMQ's stalled-job check notices the lost lock and moves the job back to `wait`.
4. A new worker picks it up. The checkpoint read (`worker.ts:162`) finds `s0` but not `s1`, so `s1` runs again.
5. Had `s1` been a MailPost step, the repeat would carry the same `${runId}:s1` key in a header and MailPost would dedupe it. ChatBox gets no key, and nothing enforces the 60 s window (`grep -rn dedupeWindow apps packages` finds only the declaration, the key derivation and comments). **Second chat post.**

A checkpoint narrows the window to one in-flight step; only a key that travels **with** the side effect closes it (`idempotency.ts:9-12` says exactly this).

## Goal + **Check** ladder

**Goal:** you can point at the line in a real engine where each durability contract is kept or broken, and predict what a crash does at that line.

1. **(junior) Find the boot bug.** Search for the queue name across `apps/`.
   **Check:** `grep -rn '"relay:runs"' apps` in elirc/relay returns exactly two hits, `apps/api/src/queue.ts:16` and `apps/engine/src/worker.ts:25`. You can say why two literals for one shared name is itself a defect (J1 asks for one shared constant).
2. **(junior) Locate the crash window.** Read `executor.ts:94-111` without the comments.
   **Check:** you name `:106` (side effect) and `:107` (checkpoint) as the gap, and you can say which of MailPost/ChatBox/CalendarLite would duplicate if a crash hit there, citing the `idempotency:` line in each connector.
3. **(mid) Explain why version pinning is load-bearing.** Read the builder's "add step" code.
   **Check:** you find `id: \`s${s.length}\`` at `apps/web/src/app/builder/page.tsx:79` and explain, before opening the sealed answer, why resuming a v1 run on a v2 that inserted a step at the front skips one side effect and repeats another (incident 001's mechanism, `elirc/gitvg: relay/training/_answers/incident-001.md`).
4. **(mid) Separate delivery metadata from durable state.** Read `queue.ts:30` and the incident 003 brief.
   **Check:** you can explain why `job.attemptsMade` cannot tell a first delivery from a stalled redelivery here (no `attempts` set; a killed worker increments the stalled counter, not `attemptsMade`) and propose deriving "is this a resume?" from Postgres (`run.startedAt`, set at `worker.ts:239`).
5. **(mid → senior) Design a durable timer.** Today waits are in-process: `sleep: (ms) => new Promise((r) => setTimeout(r, ms))` at `worker.ts:157`, used by the retry loop at `executor.ts:70`.
   **Check:** your written design (ladder M4, `elirc/gitvg: relay/training/ladder/M4-durable-timers-and-schedule-drift.md`) names the table, the sweeper query and what happens when two sweepers race, and says what today's code does with a `Retry-After` wait if the worker dies mid-sleep (the wait is lost; only stall redelivery restarts the run from its checkpoint).

## Verified senior findings (at elirc/relay `27a74af`)

- **The event log can drop events silently.** `worker.ts:85` sets `seq = await prisma.runEvent.count(...)`, and `emit` (`:86-91`) does a fire-and-forget `create` with `.catch(() => {})`. Two processes resuming the same run (or a resume racing a straggler) compute the same `seq`; the unique-constraint error is swallowed. B05 hit this as a real P2002 while building incident 002 (relay report, 2026-09-24). History you can't trust makes every other diagnosis harder.
- **A durable checkpoint points at non-durable storage.** Large outputs are offloaded to `new MemoryObjectStore()` (`worker.ts:29`, write at `:133-135`), and only the ref is saved in Postgres. On resume in a *different* process, `loadPersistedOutput` finds the ref, gets nothing back and returns `{}` (`:150-152`). Later steps then render templates against an empty object. The comment at `:27-28` says production uses S3/GCS "behind the same interface"; nothing in the repo wires that.

## Debugging scenario: "duplicate chat posts, emails fine" (relay incident 003)

Brief: `elirc/gitvg: relay/training/incidents/003-checkpoint-read-skipped.md`. After a node rotation that SIGKILLed pods, 57 runs each posted to #signups twice but sent one email. Every run ended `succeeded`. Run events show a second `run.started` followed by `step.started s0` again.

How to work it:
1. **Read the events, not the status.** A second `run.started` that re-executes `s0` means resume did not skip completed steps. StepRun rows for `s0`/`s1` exist, so the checkpoints were *written*; suspect the *read*.
2. **Use the mixed evidence.** Email did not duplicate and chat did. That points at the idempotency strategy, not the engine: MailPost dedupes on its header key; ChatBox has none (trace step 6).
3. **Check the queue metadata.** The B05 lab showed `stc=1 ats=2` in the job hash: stalled once, started twice. It was not a retry.
4. **Diff the resume path.** The suspect PR #93 gates the checkpoint lookup on `job.attemptsMade > 0`. With no `attempts` configured and a stall instead of a failure, that counter is 0 on every delivery.
5. **Fix and regression test.** Always read checkpoints (it's a primary-key lookup); if you must branch, branch on Postgres state. Test: crash after `s1`, redeliver with `attemptsMade: 0`, assert only `s2` runs. Separately, enforce or honestly label ChatBox's `dedupeWindow`.

Lab result recorded at B05: `emails=1 chat=2 calendar=1` on the incident branch vs `chat=1` on base.

## The other examples, verified

- **buildermentor INC-005.** `apps/api/src/jobs/boss.ts:31` sets `retryLimit: 3, retryDelay: 30, retryBackoff: true`; the suspect branch adds `expireInSeconds: 90`. The sealed answer (`elirc/buildermentor: training/_answers/incident-005.md`) ran the real pg-boss 10.4.2 scaled down and got `runs=4 inserts=4 maxConcurrentForOneJob=2`: expiry marks the job failed and retries while the original handler keeps running. A queue timeout is a visibility timeout, not a kill switch. The script is `training/_answers/inc005-pgboss-expiry.mjs`.
- **atlas S2.** `elirc/gitvg: atlas/training/ladder/S2-payroll-as-a-background-job.md` is a design rung: 250k workers per org, a vendor capped at 50 req/s, "one run per `(cycle, period)`", a pinned vendor, and resumable partial failure. It is design-only (no code to trace).
- **buildevent.** At elirc/build-event `b941e78`, `apps/api/src/jobs/expire-pending-orders.ts` and `release-seat-holds.ts` exist, but no file under `apps/` imports them (grep for `expire-pending-orders`, `release-seat-holds` or `jobs/` in `apps/**/*.ts|json` returns nothing). The module also schedules its repeatable job as a top-level side effect (`expire-pending-orders.ts:12`) and processes only `take: 100` per minute (`:17-20`). Ladder: `training/ladder/M2-expiry-workers-and-backpressure.md`.

## Honesty caps

- The relay incident **branches** (and the suspect PRs #88/#91/#93/#95/#97 they contain) are not on GitHub, so the incident diffs cannot be opened from a fresh clone. The mechanisms above come from the sealed answers in `elirc/gitvg: relay/training/_answers/` plus main's code, which was opened line by line. Until those branches are pushed, incidents 001–005 are read-the-answer exercises, not reproducible ones.
- The numbers (151 tests, 3.4 s / 10 MB at 50k events, `stc=1 ats=2`, `chat=2`, +3M rows) were measured or written at B05 on 2026-09-24 and were **not** re-run on 2026-10-06. Some incident-brief figures (57 customers, dashboard percentiles) are illustrative, and the B05 report says so.
- The BullMQ behaviours cited (default single attempt, stalled-counter vs `attemptsMade`) are taken from the B05 lab answer, not re-checked against BullMQ source here.
