# astraspacegameweb (Warband: The Crownlands): B03 report

**Tier:** LAB (Phases 2, 3, 4, 5) · **Focus:** operate a live stack · **Repo:** `C:\Users\Owner\Desktop\astraspacegameweb` (own `.git`, remote elirc/astraspacegameweb, **not pushed**)
**Working tree before:** clean (0 uncommitted changes). **After:** only `training/` added and committed.

## What was created

Training commit on `main`: **`2fca582`** `training: add B03 apprenticeship materials` (61 files, pathspec commit of `training/` only).

| Area | Paths (under `training/`) |
|---|---|
| Index | `README.md` (order, ~38–48 h estimate, branch table) |
| Ops lab kit (new, the core of this lab) | `ops/LAB0-BRING-UP.md`, `ops/compose.observe.yaml` (Prometheus/Grafana/Tempo reusing `infra/` config, host-port scrape, `WARBAND_INFRA` override for incident branches), `ops/prometheus.local.yaml`, `ops/slo-rules.yaml` (stub for M1), `ops/inject.ts` (arrival injector, tsc-clean), `ops/two-tabs.mjs` (WS repro), `ops/evidence/baseline-150rps-3resolvers.jsonl` |
| Ladder | `ladder/J1-side-effect-backlog.md`, `J2-websocket-metrics.md`, `J3-resolver-tick-span.md`, `M1-slos-and-burn-rate-alerts.md`, `M2-capacity-curve.md`, `M3-scrape-safe-gauges.md`, `M4-connection-budget.md`, `S1-deploy-with-rollback.md`, `S2-thousand-arrivals-per-second.md`, `S3-backlog-catch-up.md` |
| Review | `review/EXERCISE.md`, `review/COMPARE.md`, sealed `_answers/review.md` (24 findings, 9 marked [RUN], 5 marked [AI-smell]) |
| Incidents | `incidents/001…005-*.md` (symptoms only) + sealed `_answers/incidents/*.md` |
| Navigation | `navigation/ARCHITECTURE.md` (3 flows traced file by file), `FIRST_CHANGE.md`, `TRADEOFFS.md` (5 "Why?" drills), `CHANGE_REQUEST.md` + sealed answers |
| Agentic | `agentic/WORKFLOW.md` (M1 via implementer + adversarial reviewer) + sealed `_answers/agentic.md` |
| Interview | `interview/PROJECT_STORIES.md` (5), `TECHNICAL_QUESTIONS.md` (20), `SYSTEM_DESIGN.md`, `MOCK_DEFENSE.md`, `FLASHCARDS.md` (24) + `_answers/interview-technical.md` |
| Sealed answers | `_answers/` one file per exercise, plus `ladder/M1-slo-rules.yaml` + `M1-slo-tests.yaml` (promtool-verified), `lab0.md`, `evidence/runs-2026-09-24.md` + 2 JSONL sample files |

## Incident branches (based on HEAD `3ef7432`)

| Branch | Commit | Symptom (not the cause) |
|---|---|---|
| `training/incidents/001-resolver-oldest-first` | `b551c76` | The world falls behind at a load it handled last week. No errors, no lock retries on the dashboard. |
| `training/incidents/002-lag-panel-flat` | `1ac90fb` | Players report 1–2 min late battles. The lag panel is flat and no alert fires. |
| `training/incidents/003-second-tab-silent` | `a294b8b` | Multi-tab and multi-device players stop getting live updates in one tab. The "connected" dot stays green. |
| `training/incidents/004-deploy-crashloop` | `027c8a8` | After a release, every role restarts in a loop. Full outage, and no alert. |
| `training/incidents/005-redis-blip-outage` | `65dc592` | A 40 s Redis restart makes every HTTP request return 502. |

## Verification (what actually ran on this laptop, 2026-09-24)

Docker Desktop was not running. I started it (it took ~10 min to become responsive) and pulled postgres:16-alpine, redis:7-alpine, prometheus v3.5.0,
grafana 12.1.1 and tempo 2.8.2. `pnpm install --frozen-lockfile` ran once in the main tree (7 min). Every container I started was stopped, and my DB `warband_ops_test` was dropped.
**Docker Desktop was left running** (other B03 agents may use it).

- **Observability stack brought up for real:** Prometheus scraping 5 live roles (api, 3× resolver, relay) from git worktrees, the Grafana dashboard
  "Warband world health" provisioned from `infra/grafana`, and Tempo receiving OTLP from all roles. Live PromQL sampled every 10 s under 150 arrivals/s.
  - Baseline (`main`): ~110–120 events/s capacity. **EventLagHigh fired** (value 60). The lag p99/p50 **clipped at 60.0** and resolver p99 at 30.0 (a real finding on main).
  - Tempo: resolver telemetry is ≥ 1,000 one-span traces per 2 min (a real finding). `/metrics` scrapes are 125 of 200 sampled api traces.
- **INC-001 RUN-VERIFIED:** a 6,000-arrival drain with 3 resolvers took 91–115 s on main vs 151–154 s on the branch. `pg_stat_database` rollbacks went from 163–179 to 568–649.
  One resolver shows no regression (in-process profile 78.4 s vs 78.7 s; one noisy bench outlier of 252 s is reported honestly in the brief).
- **INC-002 RUN-VERIFIED:** branch roles + branch `infra/alerts.yaml` → lag p99 = p50 = 2.0 for the whole run, oldest event 137 s, zero alerts. Bucket dump: 26,998/27,000 in +Inf.
- **INC-003 RUN-VERIFIED:** `two-tabs.mjs` → main: both tabs 5/5 hints, gauge 2. Branch: tab B 0/5 hints, gauge 1 with 2 sockets open.
- **INC-004 RUN-VERIFIED:** branch roles against a main-migrated DB exit with `Applied migration was modified: 013_npc_players.sql`.
- **INC-005 RUN-VERIFIED:** `tools/sim/redis-outage.ts` fails on the branch and passes on main (27 s). `/api/health` 500 with `ClientOfflineError`.
- **Existing chaos tests run:** `tools/sim/chaos.ts` **PASSED** (built the pgBackRest drill image; 8 workers, 2 killed, backend terminated, PG restart,
  Redis flush → identical). `redis-outage.ts` passed on main after **one cold failure**.
- **M1 reference SLO rules:** `promtool check rules` 13 rules OK. `promtool test rules` 4 cases pass. Live drill (with an earlier draft of the rules): the burn-rate page was firing 27 s after injection started. That draft still had the `clamp_min` idle bug, so the timing is indicative only.
- Typecheck (`tsc --noEmit`) passes on main and on incident branches 001/002/003/005. 004 is SQL-only. Non-DB vitest: **63/63 pass** on main.
- **UNVERIFIED:** the DB integration suites (`tests/*.integration.test.ts`) and e2e were not run. `tools/sim/recovery.ts` and `load.ts` were not run.
  Ladder answers M4, S1 and S3 are reasoned, not rehearsed (marked in their files). Lab 0 Q8 (kill one resolver) is expected behaviour, not observed.
  A final "idle for 6 min" live check could not complete because the laptop became CPU-starved by other agents' jobs (roles took minutes to boot).
  That check was replaced by a deterministic promtool idle test.

## Issues found in the project (details: `training/_answers/review.md`)

- **CRLF + raw-byte migration checksum (verified on main):** git here has `core.autocrlf=true` and there's no `.gitattributes`. A worktree/clone checks out CRLF
  `.sql` files, and `initialize()` then refuses a DB migrated from LF files (`Applied migration was modified: 001_initial.sql`), and vice versa. A Windows-built
  image would crash-loop in production. **This is the most serious latent bug.**
- `compose.production.yaml` uses `build: .` with no image tag. The runbook's "immutable digest" rollback is impossible as written.
- There's no Alertmanager or `alerting:` block and no `up == 0` rule. The docs say alerts are "included", but they page no one.
- Resolver contention (`WB_BUSY`) is swallowed and never counted. The lag histogram (60 s) and resolver histogram (30 s) clip.
- `/api/health` is used for Caddy routing and only checks the DB. The ApiErrors SLI is dominated by probe traffic.
- Pools: 7 processes × 16 = 112 > the Postgres default of 100. SMTP/web-push calls happen inside DB transactions. Side-job retries are infinite (`prior.retry()` every 5 s).
- Traces are fragmented (no spans around loops) and scrapes are traced. The runbook's "correlate by trace ID" advice doesn't work for resolvers.
- The sustained 1,000 arrivals/s gate is **not passed**, and `docs/verification.md` says so honestly. Not presented as working.
- **Secrets (locations only):** `.env` (repo root) and `infra/runtime/metrics_token` exist locally. Both are git-ignored and **not tracked** (`git ls-files` shows only `.env.example`).
  `transport/app.ts:47` has a hard-coded non-production JWT fallback secret (guarded only when `NODE_ENV=production`).
- Only 2 commits for the whole codebase (bulk import). Doesn't matter for the lab.

## Skill links (competency graph)

| Skill area | Exercise / incident / question |
|---|---|
| **Observability / SLOs (operate live stack)** | `ops/LAB0-BRING-UP.md`; `ladder/M1` (burn-rate SLOs, promtool, live drill); `ladder/M3`; `ladder/J1`, `J2`, `J3`; `incidents/002`; review #3, #6, #8, #10; interview TQ 15–19 |
| **Telemetry correctness (page 09)** | `incidents/002-lag-panel-flat`; `_answers/agentic.md` (Prom 3 `le="2.0"` normalization, `clamp_min` idle page); review #6, #15, #16 |
| **Deployment / config / rollback** | `incidents/004-deploy-crashloop`; `ladder/S1-deploy-with-rollback`; `ladder/M4`; review #1, #2, #9; navigation W4, W5 |
| **Reliability / incidents** | 5 incident branches, all run-verified; `ladder/S3-backlog-catch-up` |
| **Performance / capacity (measured)** | `incidents/001`; `ladder/M2-capacity-curve` (real profile numbers); `ladder/S2` (1,000 arrivals/s) |
| **Async jobs / queue backlog (game tick)** | `incidents/001`; `ladder/S2`, `S3`; review #11 |
| **Realtime / WebSockets (page 08)** | `incidents/003-second-tab-silent`; `ladder/J2`; `ops/two-tabs.mjs`; interview TQ 7–9 |
| **Health checks / liveness vs readiness** | `incidents/005-redis-blip-outage`; review #7; S1 answer |
| **Testing (drills, alert-rule tests)** | `incidents/005` (flaky chaos-test culture); `ladder/M1` (promtool test rules); interview TQ 10–12 |
| **Agentic engineering** | `agentic/WORKFLOW.md` (M1): two real agent-style bugs caught by live verification |
| **Code review** | `review/EXERCISE.md` + 24-finding model review |
| **Unfamiliar-codebase navigation / design trade-offs** | `navigation/` (3 flows, 5 "Why?" drills, change request) |
| **Interview** | `interview/*` (5 stories, 20 Qs, 50× system design, mock defense, 24 flashcards) |

Not added (per saturation rules): authz/IDOR, concurrency races and idempotency/outbox got no new exercises. INC-001 is framed as throughput/observability,
not as a race.

## Curriculum needs (one central page each; not written)

1. **Health endpoints: liveness vs readiness vs dependency status.** When an instance should leave the load balancer, and shared-dependency correlated failure.
   Worked examples: astraspacegameweb INC-005, gitjira-app J1.
2. **SLOs in PromQL: bucket-ratio SLIs and multi-window burn rates**, including the gotchas: quantile clipping at the top bucket, Prometheus 3 `le` float
   normalization, `clamp_min` at zero traffic, and the "committed-only" blind spot. It could be a section added to page 09 instead of a new page.
3. **Release and rollback on a single host.** Immutable tagged images, a migrate gate, canary/overlap, auto-rollback triggers, expand-only schema.
   Worked examples: astraspacegameweb S1/INC-004, atlas S1, gitjira-app S1.
4. **Measuring capacity honestly.** A/B with ≥ 2 runs, noisy laptops, bottleneck attribution (`pg_stat_statements`, wait events, rollbacks/commit), 1 vs N workers.
5. **Distributing polling-worker work.** Random windows vs shard leases vs `SKIP LOCKED`, and making contention visible. It overlaps queues, but the focus is throughput.

## Existing learning-doc trees in the repo

| Tree | Verdict | Why |
|---|---|---|
| `docs/` (architecture.md, adr/001–003, runbooks/*.md) | **KEEP** (link from the graph) | Accurate, project-specific, cited throughout the exercises. The runbooks are the "claims" the review checks. |
| `docs/verification.md`, `docs/production-work.md` | **KEEP** | Honest evidence ledger, including the failed load gate. Used as S2's baseline. |
| `docs/final-improvements*.md`, `npcs.md`, `spawning.md` | **IGNORE** | Change logs and feature notes, not learning material. |
| `artifacts/` (git-ignored evidence, ~2,400 files) | **IGNORE** for curriculum (keep as the project's evidence) | Raw logs and screenshots. The drills write here, so exercises warn against overwriting it. |

## Honest caveats

- Live numbers come from a laptop shared with other agents' builds. Absolute throughput is noisy (one 252 s outlier), so the briefs show two runs and label the outlier.
- INC-001's mechanism is "contention on a shared head plus wasted planning". The sealed answer explains why one resolver is unaffected, using the profile. The exact
  split of the slowdown between rollback cost and smaller batches isn't isolated.
- Incident 002's brief quotes the current `docs/verification.md` 2 s target as the PR's rationale. That's intentional realism, not a doc change.
- A shared-scratchpad oddity: node_modules junctions inside my worktrees vanished once mid-session (cause unknown, possibly another agent's cleanup). The main
  `node_modules` was unaffected. All junctions were removed with non-recursive deletes before `git worktree remove`.
- Incident branch commits were re-created with `git commit-tree` to add the Co-Authored-By trailer. The trees are identical to the originals.
