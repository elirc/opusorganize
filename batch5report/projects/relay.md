# B05: relay (`C:\Users\Owner\Desktop\gitvg\relay`), LAB tier, durable execution

**Tier:** LAB (Phases 2, 3, 4, 5). 5 incidents. Batch focus: durable execution / workflow engine.
**Repo state:** own `.git` (16 commits, tags v0.5.0/v1.0.0, remote elirc/relay, **not pushed**). The working tree was clean before I started. Only `training/` was committed on main (pathspec commit).

## What I created
Everything is under `C:\Users\Owner\Desktop\gitvg\relay\training\` (commit **`2cc2ec4`** on `main`, "training: add B05 apprenticeship materials (durable execution lab)"):
- `README.md`: index, branches, suggested order (~45 to 55 h), real bugs on main, and the doc-tree verdicts.
- `lab/`: a **runnable durable-execution lab**: `docker-compose.yml` (PG16 :55442, Redis7 :56392, project `relay-training`), `lab.ps1` (up/farm/worker/kill-worker/stop/down),
  `farm.mts` (the repo's vendor farm with chaos knobs), `worker.mts` (the real `apps/engine/src/worker.ts` of any checkout), `seed.mts` (org + real OAuth code-flow connections + published
  relay + runs enqueued like the API does), `inspect.mts` (Postgres truth + what each vendor actually received), `presets.mts` (welcome v1/v2 with positional ids, welcome-sheet),
  `worktree-links.ps1` (junction sharing of node_modules for incident worktrees with a non-recursive remove), `README.md`.
- `ladder/`: J1 engine-boots + smoke/integration test · J2 nested config rendering · J3 per-step retry policy + call timeout (the "add a step/activity with retries" rung) ·
  M1 determinism contract for resume · M2 leases/fencing/heartbeats/timeouts · M3 versioning in-flight runs · M4 durable timers + drift-free schedules ·
  S1 multi-day onboarding with human approval + saga compensation · S2 linear→DAG state migration + history growth · S3 50× scale, workers and partitioning.
- `review/EXERCISE.md` + `COMPARE.md`. `_answers/review.md` has 26 ranked findings, with [AI]/[LAB] tags.
- `incidents/001..005` briefs. `_answers/incident-001..005.md` (root cause, diagnostic path, fix, regression test, postmortem). `_answers/tools/inc005-history-cost.mts` (measurement).
- `navigation/`: ARCHITECTURE (3 flows traced file by file), FIRST_CHANGE, TRADEOFFS (5 "Why?" drills), CHANGE_REQUEST ("Delay step"), plus sealed answers.
- `agentic/WORKFLOW.md`: M2 via spec → implementer → adversarial reviewer → revision → verification checklist → graded explanation.
- `interview/`: PROJECT_STORIES (5), TECHNICAL_QUESTIONS (20), SYSTEM_DESIGN (50×/multi-region/enterprise), MOCK_DEFENSE (mechanism-first interviewer script + rubric), FLASHCARDS (24). `_answers/interview-technical.md`.

## Branches (never pushed)
| Branch | Commit | Symptom (not cause) |
|---|---|---|
| `training/base/engine-boots` | `483c649` | Not an incident: main + the minimal queue-name rename so the worker can run at all (see below). All incident branches sit on it. |
| `training/incidents/001-resume-on-latest-version` | `4923d7c` | Duplicate welcome emails and a missing sales alert, only for signups in flight during a publish + fleet restart |
| `training/incidents/002-parked-runs-never-wake` | `cc20ba8` | Runs stuck "waiting" for 22 h after a vendor rate-limit episode; no errors, empty queue |
| `training/incidents/003-checkpoint-read-skipped` | `db4fd9c` | Duplicate #signups chat posts after a node rotation; emails not duplicated |
| `training/incidents/004-retriable-failed-loop` | `283d8e5` | +3 M run-history rows overnight; three runs that never end |
| `training/incidents/005-step-heartbeat-events` | `806b85d` | Run page takes seconds for long-running relays; RunEvent growing 20× faster |

**Deviation from the brief, on purpose:** incident branches are based on `training/base/engine-boots`, not directly on HEAD, because on HEAD the engine can't boot (the BullMQ queue-name
bug), so no durable-execution incident could be reproduced. The base commit is a 2-file rename only. The README says it's J1's minimal answer and tells the learner to do J1 first.

## Verification
- `pnpm install --frozen-lockfile --store-dir <SCRATCH>/relay/pnpm-store` (private store; 5 min 26 s). The first API test run failed with "@prisma/client did not initialize" until a manual
  `prisma generate` (the postinstall generate didn't take effect the first time). After that: **151 tests green** (engine 52, shared 28, expr 18, vendor-farm 16, connectors 12, api 12,
  connector-sdk 7, secrets 6) and **`turbo typecheck` 11/11**.
- The live stack was actually run (Docker PG + Redis with a unique project and ports, the vendor farm, the real engine worker). **On main the worker crashes at boot**: `Queue name cannot contain :` (BullMQ 5.79.3).
- **All 5 incidents reproduced in the lab** on 2026-09-24:
  - 001: a resumed run showed 2 welcome emails to the same user, 0 sales emails, and StepRuns `s0..s3` under a Run pinned to v1.
  - 002: parked twice, `ZCARD delayed = 0`, the job finished, and the run stayed `waiting` after the vendor recovered.
  - 003: emails=1 / **chat=2** / calendar=1 on the incident branch vs chat=1 on base (control run). Redis job hash `stc=1 ats=2`.
  - 004: 29 "attempt 1 failed" loops / 56 events for one run in ~55 s, never `failed`.
  - 005: 19 events vs 8 for a normal run. The measurement script gave the run-detail query 17 ms @10 → 604 ms @10k → **3.4 s / 10 MB @50k events**.
- Every incident branch passes its own `tsc --noEmit` and engine vitest (52 or 53 tests, so each passes CI, which is realistic). The api tsc was checked on base.
- The J2 real bug (nested config not rendered + naturalKey dedupe) and the `RunEvent.seq` race (P2002, hit while building incident 002) were **lab-proven on real code**.
- Cleanup: the lab processes were stopped, the junctions removed with `.Delete()` (non-recursive), all 6 worktrees removed with plain `git worktree remove` (no --force), `docker compose down -v`
  done, and no containers left. Main's `node_modules` was verified intact afterwards. No recursive deletes anywhere.
- UNVERIFIED: the lab scripts were run by me from bash/PowerShell but not by a learner from a fresh clone. `lab.ps1 up` (the compose + db push combo) was exercised as separate commands, not
  as the single script command. The ladder reference code snippets (J1/J2/J3/M2/M4) are sketches: not compiled. The S-rung answers are designs.

## Issues found in the project (details in `training/_answers/review.md`)
- **Presented as working, and it isn't:**
  1. The engine and API **cannot construct their BullMQ queue** on the locked deps (`apps/api/src/queue.ts:16`, `apps/engine/src/worker.ts:25`, `"relay:runs"`), so no run has ever executed with the lockfile. CI is green because no test touches BullMQ/Postgres. `.github/workflows/ci.yml` claims "DB/queue wiring is verified via typecheck + build".
  2. ADR-0016, the stuck-run runbook and `docs/postmortems/2026-07-09-vendor-hang-pileup.md` describe a breaker, stuck detection, a heartbeat, metrics, a DLQ and "safe bulk replay". **None of it is wired** into `worker.ts`, and live replay would re-send vendorKey side effects (a new runId means new keys).
  3. Failed runs are never retried (`attempts` default 1), despite the `worker.ts:257` comment. There is no pending-run sweeper, despite the hooks comment.
  4. `dedupeWindow` (ChatBox) is never enforced. `UsageRecord` metering is never written. `fairness/`, `fanout.ts`, `triggers/*` and `sandbox/` are tested libraries with no caller.
  5. Nested step config isn't rendered, so SheetLite rows are literal templates and naturalKey dedupes them across runs → **silent data loss with green runs** (lab-proven).
- Correctness: the `RunEvent.seq = count()` + fire-and-forget race silently drops events (lab-proven). Offloaded outputs sit in an in-process `MemoryObjectStore`, so resume rehydrates `{}`. Positional/duplicate step ids. A race on the lazy DEK creation. DAG relays skip trigger bindings (swallowed ZodError) and replay/test-run 500 on them.
- Security (reported once; authz is saturated): `/auth/dev-login` always registered · `/api/runs*` unauthenticated · replay accepts any `versionId` without checking its relay · webhook HMAC over a re-serialized body, and the replay guard is per-process.
- **Secrets (locations only):** a hardcoded dev KEK default in `apps/engine/src/env.ts` (RELAY_MASTER_KEK) and `apps/api/src/env.ts`, the same value in `.env.example`. Dev OAuth client secrets in
  `packages/vendor-farm/src/meta.ts` (fake vendors; intended). No real credentials found.

## Skill links (for COMPETENCY_GRAPH)
- **durable execution / workflows** (thin → now a primary lab) → `ladder/M1`, `M2`, `M3`, `M4`, `S1`, `S2` · incidents 001, 002, 003, 004, 005 · `navigation/TRADEOFFS.md` #2/#5 · `navigation/CHANGE_REQUEST.md` · interview Q8 to Q13, `SYSTEM_DESIGN.md`, `MOCK_DEFENSE.md`
- **sagas and compensation** (thin) → `ladder/S1` (compensation derived from checkpoints; approval signal) · interview SYSTEM_DESIGN pressure point 4
- **async jobs / queues / idempotency** (saturated: linked, not re-taught) → incidents 002/003/004 (BullMQ stalled vs failed, jobId dedupe, retry budget on the message) · review #4/#5/#8/#9
- **operating a live stack** (thin) → `lab/` (real worker + infra + chaos + kill -9 + Redis probes), all 5 incident reproductions, `_answers/tools/inc005-history-cost.mts`
- **observability** → review #2 (docs vs wiring), interview Q20 (three alerts tied to incidents), incident 005 (history vs liveness)
- **data modeling / SQL / migrations** → incident 005 (partitioning, batched purge), `ladder/S2` (expand/contract of workflow state), `ladder/M2` (conditional claim + fencing), `M4` (Timer table, SKIP LOCKED)
- **performance** → incident 005 (measured query/payload scaling), `ladder/S3` (Little's-law capacity math)
- **testing** → `ladder/J1` (why 151 fake-based tests missed a boot crash; gated integration test), incident answers' regression tests
- **backward compatibility / versioning** → incident 001, `ladder/M3`, `ladder/J3` (additive schema + old-version behaviour)
- **code review** → `review/` (26 findings, 5 claim-vs-code)
- **unfamiliar-codebase navigation** → `navigation/ARCHITECTURE.md`, `FIRST_CHANGE.md`
- **agentic engineering** → `agentic/WORKFLOW.md` (M2 lease/fencing)
- **frontend/React** (light) → interview Q16/Q17 (run page polling, id generation)

## Curriculum needs (one central page each; not written)
- **16: Durable execution: checkpoints, determinism, timers, leases.** Scope: checkpoint-and-recompute vs event-sourced replay (Temporal), the determinism contract (pinned versions,
  stable activity ids, recorded inputs), activity keys, leases + fencing vs queue locks, durable timers in the DB. Worked examples: relay incidents 001 to 005 and M1 to M4.
- **17: Sagas and compensation.** Scope: forward steps + compensations derived from the checkpoint log, reverse order, durable compensations, bounded failure paths, non-compensatable
  effects. Worked examples: relay S1 + astra5 (B05 DRILL: sagas across Next + .NET), so it meets the ≥ 2-project rule.
- Backlog candidates (one project so far): "Workflow versioning for long-running executions (pin / drain / migrate / patch markers)" (could fold into 16) · "Event/history tables: taxonomy, retention, partitioning".

## Existing learning-doc trees
- `docs/` (sprints 00-15 playbooks, `docs/curriculum/sprint-01..15.md`, ADR 0000-0016, runbooks, postmortem, threat model, `LEARNER-GUIDE.md`, audit; ~3,000 lines): **KEEP** as the design
  narrative, linked from `training/README.md`. The runbooks, the postmortem and ADR-0016 describe unwired mechanisms. They're used as review material (**CONVERT TO EXERCISE**, done via review #2), not as operating docs.
- `docs/sprints/flaw-ledger.md`: **KEEP** (the course's spoiler list). None of the B05 incidents reuse its flaws (template injection, inline JSONB outputs, per-relay cursor, unsigned webhooks, unbounded sandbox logs).
- `githelp.md`: **IGNORE** (generic git manual).
- No MERGE proposals.

## Honest caveats
- Incident briefs mix lab-measured facts (per-run counts, the heartbeat/query numbers, log lines) with illustrative production-scale numbers (57 customers, 412 runs, 3.1 M rows, dashboard percentiles). The answers say which is which.
- Incident 002's diff originally wrote a `run.parked` event and crashed on the real `seq` race. I amended the incident commit to log instead (the race is kept as review #6), so the branch shows one clean suspect commit.
- The lab shares main's `node_modules` via junctions, so `@relay/*` packages resolve to **main's** `packages/`. Every incident diff lives in `apps/engine/src`, so this is correct for these branches, but a learner's own changes to `packages/*` inside a worktree won't be picked up by the lab. This is documented in `worktree-links.ps1`.
- Redelivery timing in the lab depends on BullMQ defaults (30 s + 30 s). The scenarios wait 75 to 90 s, and a slower machine may need longer.
- I didn't write to COMPETENCY_GRAPH, curriculum/ or PROGRESS.md (per the brief).
- `relay-app` (the .NET rebuild of the same product) wasn't touched. Its durable-execution story would duplicate this lab.
