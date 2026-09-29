# gitjira-app (GitJira): B02 report

**Tier:** LAB (Phases 2, 3, 4 and 5)
**Repo:** `C:\Users\Owner\Desktop\gitjira-app` (own `.git`, remote `github.com/elirc/gitjira`, **not pushed**)
**Base:** `main` @ `0c1a640`
**Training commits on `main`:**
- `a0b506c` "docs(training): add B02 apprenticeship materials" (53 files, `training/` only).
- `b778462` "docs(training): fix mangled inline code in ladder J1 answer".

Both were pathspec commits. The owner's 14 uncommitted changes are untouched. I checked this before and after each commit: `git status --porcelain` and the full `git diff` are byte-identical to a backup taken first (the backup is in the scratchpad `gitjira-backup/`).

**Deviation from the brief:** the commit message isn't the brief's `training: add B02…`. The repo's husky `commit-msg` hook runs commitlint (config-conventional), which rejects the type `training`. I used `docs(training): …` rather than `--no-verify`. The `pre-commit` hook (lint-staged) ran prettier on the training markdown, so the committed files are prettier-formatted. With a pathspec commit, lint-staged left the real index holding the pre-prettier copies. I ran `git reset -q -- training` (training paths only) to re-sync it.

## What I created (`gitjira-app\training\`)
- `README.md`: index, spoiler list, suggested order (about 55 h), a one-weekend subset, and run notes.
- `ladder/`: README plus 10 tickets, each with "Explain before touching":
  - **J1** readiness vs liveness.
  - **J2** issue table stops at 50 (`useInfiniteQuery`).
  - **J3** queue metrics that exist.
  - **M1** board at 2,000 issues (React Profiler, memo, invalidation scope, truncation).
  - **M2** SLOs + route labels + burn-rate alerts.
  - **M3** Redis as a soft dependency (the agentic ticket).
  - **M4** live board across 2 machines (adapter, stickiness, emit-after-commit, rejoin).
  - **S1** GitJira on AWS (ECS Fargate/RDS/ElastiCache/S3/ALB, OIDC `deploy.yml` rewrite, migration task, circuit-breaker rollback).
  - **S2** labels normalization with expand/contract on 2M rows under Prisma (locks table, `CONCURRENTLY` in Prisma, backfill, JQL switch).
  - **S3** "assigned → bell ≤ 10 s p99" end-to-end SLO.
- `review/`: `EXERCISE.md` (60-min blind review of `0c1a640` in a worktree) and `COMPARE.md`.
- `incidents/`: README (worktree instructions) plus 5 briefs.
- `navigation/`: `ARCHITECTURE.md` (evidence-cited, 3 flows, 10 migrations, test strategy, deploy), `FIRST_CHANGE.md`, `TRADEOFFS.md` (4 "Why?" drills: hint+invalidate realtime, fractional string positions, release-phase migrations, Postgres FTS), `CHANGE_REQUEST.md` (CR-21, live bell across tabs and instances).
- `agentic/`: `EXERCISE.md` (spec → implementer → adversarial reviewer → revision → verify with Redis down → graded explanation, on M3) and `VERIFY_CHECKLIST.md` (GitJira-specific).
- `interview/`: `PROJECT_STORIES.md` (5 STAR), `TECHNICAL_QUESTIONS.md` (20, with Q16–20 spoiler-fenced), `SYSTEM_DESIGN.md` (50× / multi-region / enterprise), `MOCK_DEFENSE.md` (buzzword-refusing script, /18 rubric), `FLASHCARDS.md` (24, with cards 20–24 spoiler-fenced).
- `_answers/` (sealed, 22 files): `review.md` (29 ranked findings), `incident-001..005`, `ladder-J1..S3` (10), `navigation-architecture`, `navigation-tradeoffs`, `navigation-change-request`, `agentic-rubric`, `interview-technical`, `interview-system-design`.

Navigation, agentic and interview were drafted by two parallel forks against my plan. I reviewed them for spoilers and tightened two `VERIFY_CHECKLIST.md` items that gave away the causes of INC-001 and INC-003.

## Incident branches (each is HEAD `0c1a640` plus one "suspect PR" commit; worktrees removed)
| Branch | Commit | Symptom (not the cause) |
|---|---|---|
| `training/incidents/001-board-cpu-storm` | `da66e59` | After a web-only release, Postgres CPU goes from 14 % to 91 % and API event-loop lag from 4 ms to 380 ms whenever a big team opens its board; laptops spin; some live cards only appear after refresh |
| `training/incidents/002-missing-notifications` | `5267476` | Repeat assignments and later mentions on the same issue silently produce no notification; notifications/day down 38 %, zero errors |
| `training/incidents/003-deploy-story-points` | `65a3d1c` | 4 minutes of 5xx during a prod deploy, then every sprint report shows 0 points, and edits from some users "don't save" |
| `training/incidents/004-dashboards-flatline` | `d7bbbdb` | All RED dashboards go "No data" on a Saturday night; API RSS climbs about 6 MB/h, with p99 spikes every 15 s; no alert fired |
| `training/incidents/005-live-board-goes-stale` | `48f6a4c` | The live board stops updating about 15 minutes after the page loads; presence shows people who left and misses people who are there |

Each incident commit has a realistic Conventional-Commit PR message that states a genuine bug the PR was trying to fix. All passed the repo's lint-staged and commitlint hooks.

## Verification
- I ran `npm ci` **once, in the main tree** (873 packages, about 10 min; `node_modules` is gitignored and left installed). Incident worktrees used temporary junctions to it, which I removed before `git worktree remove`. The main `node_modules` is intact.
- **INC-001: VERIFIED by execution.** A scratch vitest (not committed) mounted HEAD's hook and the branch's hook against a fake socket that echoes presence after 1 ms. In 300 ms, HEAD emitted `join-project` once (2 renders), and the branch emitted it 25 times (25 renders), from a single client. On the branch, the web suite passed 13/13 tests, and 1 vitest worker-pool startup timed out. That's the environment (a slow machine), not a test failure.
- **INC-003: VERIFIED.** `prisma migrate diff --from-schema-datamodel <HEAD> --to-schema-datamodel <branch> --script` prints exactly `ALTER TABLE "Issue" DROP COLUMN "storyPoints", ADD COLUMN "estimate" INTEGER;`, which is the committed migration. `prisma validate` passes, and eslint is clean.
- **INC-004: VERIFIED by execution.** A scratch script drove the branch's `metricsMiddleware`. About 42k distinct paths produced 504,000 series, a 55 MB `/metrics` body and a 5.6 s `registry.metrics()`, against 36 series, 10 KB and 23 ms for HEAD on the same traffic.
- **INC-002: partially verified.** `notificationJobId` was executed. BullMQ 5.79.3 source confirms that a duplicate `jobId` returns the existing id and emits `duplicated` (`commands/includes/handleDuplicatedJob.lua`) and that `:` is rejected in custom ids (hence the `|` separator). The end-to-end drop was not run (no Redis). The new API test file needs Postgres (setup truncates), so it wasn't run.
- **INC-005:** the web suite on the branch passed 6/6 files and 16/16 tests. Eslint is clean. Loss of rooms on reconnect is Socket.IO protocol behavior, **UNVERIFIED by execution** (no running API).
- **Not run anywhere:** the API integration suites (no Postgres started; the brief says no long-running servers), Playwright e2e, and the Docker builds. Ladder answers are reference analyses, not implemented solutions. AWS cost figures in S1 are order-of-magnitude.

## Issues found in the project (full list in `training/_answers/review.md`)
- **Presented as working, but not:**
  - (R1) `deploy.yml` + `fly.toml` deploy **only the API**. The worker and web have no deploy path, and deploys don't wait for CI.
  - (R4) Only `issue.created` and `comment.added` are ever broadcast. Moves and edits never reach other viewers. The e2e realtime test only covers creation.
  - (R6) The RUNBOOK and postmortem claim the API "degrades gracefully" with Redis down. In fact the member-map cache in the authz path and the awaited after-commit enqueue make Redis a hard dependency.
  - (R7) The board and backlog silently show only the newest 50 issues. `docs/performance.md` benchmarked "issue list (50)" without noticing.
  - (R10/R25) The queue-depth gauge, `queue_consumed_total`, the "~90 s rollback drill" and "the socket makes the bell instant" don't exist. The repo's own `docs/process/AUDIT-2026-07.md` admits that the postmortem and drill were narrated.
  - (R16) `reconnectSocket` is dead code.
- **Top runtime risks:**
  - (R2) Attachments live on local ephemeral disk across 2 machines, and a missing file crashes the process (a stream with no `error` listener).
  - (R3) Socket.IO has no adapter or stickiness on 2 machines.
  - (R5) The socket hint is emitted before commit.
  - (R8) The watch endpoint has no authz.
  - (R9) There's no graceful shutdown.
  - (R12) The login limiter Map grows without bound.
  - (R18) Two historical migrations would be write outages at scale (type change, non-concurrent index).
  - (R28) Board order can differ between JS sort and SQL collation.
- **Secrets (locations only):**
  - `apps/api/.env` exists locally and is gitignored, not committed.
  - `apps/api/.env.example` holds placeholders.
  - Test-only values in `.github/workflows/ci.yml` (Postgres password, `JWT_SECRET`) and `e2e.yml`.
  - A default Postgres password fallback in `docker-compose.prod.yml` (`${POSTGRES_PASSWORD:-…}`).
  - A seed user password in `apps/api/prisma/seed.js:9` and `README.md`.
  - `FLY_API_TOKEN` is correctly referenced as a GitHub secret. Nothing live was found.
- **Brief vs reality:** the orchestrator described deployment as "to AWS via its existing deploy.yml". It deploys to **Fly.io**, not AWS. S1 is therefore framed as "take this Fly-only pipeline to AWS," which is honest and a harder, better exercise.

## Skill links (for COMPETENCY_GRAPH)
- **deployment/cloud/config/secrets:** `ladder/S1-aws-production.md`, INC-003, `ladder/J1-readiness-probe.md`, review R1/R2/R9/R26/R29, interview Q13–14, `interview/SYSTEM_DESIGN.md`
- **data/migrations (zero-downtime, Prisma):** `ladder/S2-labels-expand-contract.md`, INC-003, review R18, Q3–4, `navigation/TRADEOFFS.md` drill 3
- **observability/SLOs:** `ladder/M2-slos-and-route-labels.md`, `ladder/J3-queue-metrics.md`, INC-004, `ladder/S3-notification-latency-slo.md`, review R10/R11, Q15
- **web/TS/React (rendering, perf):** INC-001, `ladder/M1-board-at-2000-issues.md`, `ladder/J2-issue-table-load-more.md`, review R7/R15/R17, Q6–8
- **async jobs/queues (BullMQ failure modes):** INC-002, `ladder/M3-redis-soft-dependency.md`, `ladder/J3`, `ladder/S3`, review R6/R13
- **realtime/WebSockets (scaling):** `ladder/M4-live-board-across-instances.md`, INC-005, INC-001 (server amplification), review R3/R4/R5/R16/R20, `navigation/CHANGE_REQUEST.md` (CR-21)
- **performance:** INC-001, INC-004, M1, review R14/R22/R23
- **caching:** M3 (cache as a soft dependency; stale authz on failed invalidation), review R15 (client cache invalidation scope)
- **reliability/incidents:** all 5 incidents, each with a sealed postmortem
- **testing:** review R24 (the harness can't see commit ordering or Redis), `agentic/VERIFY_CHECKLIST.md`, the regression tests in each incident answer, the M2 cardinality test
- **backward compatibility:** INC-003 (N−1 schema, cached SPA bundles + Zod strip), J2 (additive field), S2
- **design docs/ADRs:** `navigation/TRADEOFFS.md` (4), S1–S3 design deliverables
- **code review:** `review/EXERCISE.md` + `COMPARE.md` + `_answers/review.md` (29 findings); every incident answer has a "why review missed it" section
- **unfamiliar-codebase navigation:** `navigation/ARCHITECTURE.md`, `FIRST_CHANGE.md`, CR-21
- **agentic engineering:** `agentic/EXERCISE.md`, `VERIFY_CHECKLIST.md`, `_answers/agentic-rubric.md`
- **authz/idempotency/outbox/concurrency:** intentionally **not** exercised again. They're linked to curriculum 01/02/03 from M3, M4, S3, INC-002 and R21.

## Curriculum needs (one central page each; not written)
1. **Liveness vs readiness vs startup probes.** What each signal triggers on Fly, ECS/ALB and k8s; why dependency checks in liveness cause restart storms.
2. **Zero-downtime migrations on Postgres (lock levels + expand/contract).** The lock table, `lock_timeout`, `CONCURRENTLY`, `NOT VALID`/`VALIDATE`, N−1 compatibility, and ORM quirks (Prisma rename = DROP+ADD, multi-statement files and `CONCURRENTLY`). Netdrop S2 already needed this, so this is now the second project.
3. **SLIs, SLOs and burn-rate alerting.** Ratio SLIs from histograms, multi-window burn rates, "monitor the monitor" (`up` and `absent`), and bounded label cardinality.
4. **Realtime fan-out at more than one instance.** Pub/sub adapters, sticky vs WebSocket-only transports, rooms as per-connection state, rejoin on reconnect, emit after commit. netintercom (SignalR) is the other example, so this is due now.
5. **Queue client failure modes (BullMQ/ioredis).** Offline queue, `maxRetriesPerRequest`, `enableOfflineQueue: false` on producers, `noeviction`, job-id semantics (event vs entity identity), retention of completed and failed jobs.
6. **React effect dependencies with side effects.** Referential stability, the latest-callback ref pattern, act() queuing in tests, and render-count tests.
7. **Graceful shutdown for Node HTTP + WebSocket servers.** Signal handling, drain ordering vs LB deregistration delay, and platform kill timeouts.

## Existing learning-doc trees in the repo
- `docs/adr/` (31 ADRs + README): **KEEP**. High quality. Link it from the graph as design-docs reference. Caveat: ADR 0031 isn't followed by the migration history (S2 uses that gap).
- `docs/concepts/` (5 pages: idempotency, incremental migration, parsing, state machines, websockets): **MERGE (candidate)**. `idempotency.md` overlaps `curriculum/02`, and `websockets.md` could seed curriculum need #4. Move only with approval.
- `docs/RUNBOOK.md`, `docs/postmortems/2026-07-10-redis-outage.md`: **CONVERT TO EXERCISE**, already done. They're used as "claims to verify" in the review, M3 and J3. The postmortem is narrated fiction (AUDIT item 4).
- `docs/performance.md`, `docs/TESTING.md`, `docs/SECURITY.md`, `docs/security-audit.md`, `docs/threat-model.md`: **KEEP** as background. `performance.md` missed the 50-cap (R7).
- `docs/sprints/` (sprint 01–11 exercises) and `docs/state/`: **KEEP** as the course's own path, but they're **spoilers** for its planted bugs. None is reused here.
- `docs/process/` (AUDIT, SKILLS-LEDGER, WORKFLOW-IMPROVEMENTS): **KEEP**. The honest self-audit is itself good "verify AI output" material, but it's a spoiler for review R25.
- `docs/GLOSSARY.md`, `docs/RETRO.md`, `docs/DEMO.md`, `claudecodedoc.md`, `workflowoutcome.md`: **IGNORE** for the graph (generic, retrospective, or tool-usage).
- `astraupskill/` (untracked, the owner's WIP course on sprint assignment/completion races, matching the uncommitted diffs): **KEEP, don't touch**. It overlaps review R19 and is referenced in the README spoiler list.
- No planted-flaw ledger file (`FLAW-LEDGER.local.md` or `docs/sprints/flaw-ledger.md`) exists in this repo. The course's planted bugs live in the sprint docs and PR threads, which are flagged as spoilers. All 5 incidents are new designs.

## Honest caveats
- Metric numbers and log lines in the incident briefs are synthetic, but consistent with the code paths. Only INC-001 and INC-004's core mechanisms, and INC-003's migration SQL, were reproduced by execution.
- The API integration tests were never run in this session (no Postgres). Line references were taken from `git show HEAD:<path>`, because the working tree differs in 11 source files.
- `node_modules` is now installed in the main tree (gitignored). This is the one `npm ci` the brief allowed. It isn't committed, but it is a large local folder the owner didn't have before.
- Some ladder tickets describe the correct fix for a problem whose incident shows a wrong fix (M2 vs INC-004, M4 vs INC-005, S2 vs INC-003). The README orders the incidents first for that reason.
- The forks' `interview-technical.md` answers are compact (one paragraph per question). They're adequate as a key, not as teaching text.
