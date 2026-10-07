# 13 — Release safety: health checks, reproducible artifacts, rollback

**Where these repos live now (checked 2026-10-06):** astraspacegameweb → `elirc/astraspacegameweb` (`main` @ `736b75f`; all five `training/incidents/*` branches **are** on GitHub) · gitjira-app → `elirc/gitjira` (`main` @ `42abd2c`; incident branches not on GitHub) · atlas → `elirc/gitvg`, folder `atlas/training/` (`main` @ `af91bab`; the standalone `elirc/atlas` repo has no `training/`, and the `004-canary-rollback` branch is not on GitHub).

**Health endpoints do three different jobs. Don't merge them.**
| Endpoint | Question | Failure consequence | Should check |
|---|---|---|---|
| **liveness** | "Is this process wedged?" | the orchestrator **restarts** it | only in-process state (event loop responsive), never dependencies |
| **readiness** | "Can this instance take traffic now?" | it is **removed from the load balancer** | the dependencies this instance needs *right now* (DB pool, migrations applied) |
| **status/deps** | "How healthy is the system?" | dashboards and humans | everything, with detail. Not used for routing. |

If a dependency blip is wired into liveness, every instance restarts at once, and a 40-second Redis restart becomes a full outage. Wiring it into a readiness check that *every* instance shares does the same thing: every instance leaves the load balancer at once.

**Reproducible, rollback-able releases**
- Deploy **immutable, tagged images** (by digest). `build: .` on the production host means there is nothing to roll back *to*.
- Normalize line endings (a `.gitattributes`) and anything hashed at build or migrate time. A CRLF checkout can change checksums.
- Migrations must be compatible with version N-1 ([07](07-zero-downtime-migrations.md)), or rollback breaks the DB contract.
- Rehearse rollback: time it, and record the exact command in the runbook *before* you need it.
- Canary: compare error rates old vs new, and make sure the *old* revision still works against the new schema.

**Worked examples in your repos**
- **astraspacegameweb:**
  - `training/incidents/004-deploy-crashloop`: every role restarts in a loop after a release.
  - `training/incidents/005-redis-blip-outage`: a 40 s Redis restart causes 502s everywhere. The Redis-outage test (`tools/sim/redis-outage.ts`, run as `pnpm test:redis-outage`) fails on the branch and passes on `main`. *(Corrected 2026-10-06: an earlier version of this page called it "the existing chaos test". `tools/sim/chaos.ts` is a different drill, and it passed on `main` in B03.)*
  - `ladder/S1`: deploy with a rehearsed rollback.
  - Real findings, still true at `736b75f`: there's no `.gitattributes`, and the migration checksum over the file text breaks across CRLF/LF checkouts; `compose.production.yaml:3` is `build: .` with no image tag; `/api/health` is both Caddy's routing check and checks only the DB.
- **gitjira-app:** `training/ladder/J1-readiness-probe.md` (readiness vs liveness) and `S1-aws-production.md` (Fly → AWS). The deploy workflow ships only the API and doesn't wait for CI (re-verified at `42abd2c`: `.github/workflows/deploy.yml` runs on every push to `main` or a `v*` tag, has no `needs:` or `workflow_run` dependency on CI, and only runs `flyctl deploy` for the API apps).
- **atlas:** `elirc/gitvg: atlas/training/incidents/004-canary-rollback.md` (the old revision 500s) and `atlas/training/ladder/S1-azure-container-apps-azure-sql.md` (Azure Container Apps).

---

## Worked trace: who calls `/api/health` in astraspacegameweb (`main` @ `736b75f`)

1. **The handler.** `apps/server/src/transport/app.ts:94` routes `GET /api/health` to `gameUseCases.get_api_health`. That use case is `apps/server/src/application/game.ts:62-65`: one `SELECT 1` against Postgres, then `{ ok: true, server_now }`. So "healthy" means "this process can reach the DB".
2. **Caller 1: the load balancer.** `infra/Caddyfile:5-9` reverse-proxies to `api:3001` with `health_uri /api/health` every 10 s. A failing check removes the upstream from rotation. If every upstream fails, Caddy logs `no upstreams available` and returns 502 (INC-005's log).
3. **Caller 2: Docker.** `compose.production.yaml:25-35` defines a `healthcheck` on the shared `x-app` anchor that fetches the same URL every 15 s with 4 retries. The anchor is merged into all four roles (api, resolver, relay, sidejobs).
4. **Caller 3: test tools.** `tools/sim/load.ts:90` and `tools/sim/redis-outage.ts:39` poll it to decide when the server is up.

One URL is doing a readiness job (Caddy), a liveness-ish job (Docker), and a "started" job (the sims). Any change to what it checks changes all three at once.

## Failure mode, step by step: INC-004 (the crash-loop)

1. **Every role migrates at boot.** `apps/server/src/index.ts:16` runs `await initialize()` before it even reads `ROLE` (`:17`). So api, resolver, relay and sidejobs all execute the migration runner.
2. **The runner hashes the file text.** `packages/db/index.ts:143-144` reads each `.sql` file as UTF-8 and takes its SHA-256. `:147-148` throws `Applied migration was modified: <name>` if an already-applied file's checksum differs.
3. **The release edits an applied migration.** The brief's diff adds two comment lines to `013_npc_players.sql`, which was already applied in production. The SQL is the same, but the bytes are not.
4. **Every role exits with code 1.** Compose `restart: unless-stopped` (`compose.production.yaml:4`) restarts them, and they fail again. The old containers are already gone, because compose recreated them in place.
5. **There is nothing to roll back to.** With `build: .` there is no previous image tag. You must check out the old commit and rebuild on the host, during the outage.
6. **No alert fires.** The brief notes that `up == 0` had no rule and there was no Alertmanager (B03 findings).

**The same crash without anyone editing a migration:** git converts line endings on Windows checkouts. On this machine on 2026-10-06, `git ls-files --eol packages/db/migrations` printed `i/lf w/crlf attr/` for every file: the files are stored with LF, checked out with CRLF, and no attribute pins them. A Windows-built image would hash different bytes than a Linux-built one. B03 reproduced this (`Applied migration was modified: 001_initial.sql`). The fix is a `.gitattributes` with `*.sql text eol=lf`, *and* a checksum that normalizes line endings before hashing, because you can't re-hash rows already in `schema_migrations` without a plan.

## Goal + **Check** ladder

1. **Goal (junior):** classify each health caller. **Check:** grep `api/health` across the repo (excluding `training/`). You should find six hits: the five in the trace, plus `app.ts:79`, which exempts the URL from authentication. Label each caller as liveness, readiness or "started".
2. **Goal (junior):** do gitjira-app J1 on paper. **Check:** `elirc/gitjira: apps/api/src/services/health.service.js:10-16` returns only `status`, `version` and `uptimeSeconds`, with no dependency touched. `fly.toml:37-40` points Fly's HTTP check at that URL (15 s interval, 2 s timeout). Your design adds `/api/health/ready` with a bounded DB probe and leaves `/api/health` unchanged (J1's constraints).
3. **Goal (junior → mid):** prove the CRLF hazard yourself. **Check:** run `git ls-files --eol packages/db/migrations` in a Windows clone of `elirc/astraspacegameweb`. If you see `w/crlf` with an empty `attr/`, the hazard is live on your machine.
4. **Goal (mid):** reproduce INC-005. **Check (run locally):** `git switch training/incidents/005-redis-blip-outage`, then `docker compose up -d postgres` and `pnpm test:redis-outage`. Expected, from the brief: it fails with `Server did not start without Redis` on the branch and passes on `main` (B03 also saw one cold failure on `main` before a pass).
5. **Goal (mid → senior):** write S1's release state machine. **Check:** your design answers each pressure point in `training/ladder/S1-deploy-with-rollback.md`: an image per SHA, migrate once as a gate, overlap during the API swap, automatic rollback from SLO signals, and no schema rollback.

## Verified senior findings

- **gitjira-app migrates in the right place, but it deploys without CI.** `fly.toml:25` runs migrations once as a `release_command`, so a failed migration aborts the deploy and the old version keeps serving. That is the opposite of astraspacegameweb's per-role `initialize()`. But `deploy.yml` deploys staging on every push to `main` without waiting for the CI workflow, and production on a tag after a human approval. Neither ships the web app.
- **atlas INC-004 inverts the usual canary story.** The brief's ingress table shows the *old* revision (r42) with 611 5xx out of 8,120 requests and the new one (r43) with 0 out of 897. The migration renamed a column (`column p0.Label does not exist`). "Rollback" moved all traffic onto the revision that couldn't read the new schema, and the 5xx rate went above 40%. A canary only protects you if N-1 can run against N's schema.

## Debugging scenario: "all instances went unhealthy at the same moment"

Simultaneous failure means a shared cause. (1) List what the health endpoint touches (here: `game.ts:62-65`). (2) Check whether that dependency had an event at the same time (INC-005: Redis maintenance at 03:10). (3) Check *who* acted on the failing check: the LB pulling upstreams (502s, `no upstreams available`) or the orchestrator restarting containers (`Restarting (1)` in `docker compose ps`). (4) Fix the model, not the timeout. Keep the shared soft dependency out of readiness, and expose it in a status endpoint for humans.

**Honesty cap:** the INC-004/005 outcomes and the CRLF crash were run-verified in B03 (2026-09-24) on the original clone. On 2026-10-06 I re-read the code paths and the EOL state only. I didn't run anything. The S1 answers for astraspacegameweb are marked "reasoned, not rehearsed" in the B03 report.
