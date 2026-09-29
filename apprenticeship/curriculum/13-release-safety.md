# 13 — Release safety: health checks, reproducible artifacts, rollback

**Health endpoints do three different jobs. Don't merge them.**
| Endpoint | Question | Failure consequence | Should check |
|---|---|---|---|
| **liveness** | "Is this process wedged?" | the orchestrator **restarts** it | only in-process state (event loop responsive), never dependencies |
| **readiness** | "Can this instance take traffic now?" | it is **removed from the load balancer** | the dependencies this instance needs *right now* (DB pool, migrations applied) |
| **status/deps** | "How healthy is the system?" | dashboards and humans | everything, with detail. Not used for routing. |

If a dependency blip is wired into liveness, every instance restarts at once, and a 40-second Redis restart becomes a full outage.

**Reproducible, rollback-able releases**
- Deploy **immutable, tagged images** (by digest). `build: .` on the production host means there is nothing to roll back *to*.
- Normalize line endings (a `.gitattributes`) and anything hashed at build or migrate time. A CRLF checkout can change checksums.
- Migrations must be compatible with version N-1 ([07](07-zero-downtime-migrations.md)), or rollback breaks the DB contract.
- Rehearse rollback: time it, and record the exact command in the runbook *before* you need it.
- Canary: compare error rates old vs new, and make sure the *old* revision still works against the new schema.

**Worked examples in your repos**
- **astraspacegameweb:**
  - `training/incidents/004-deploy-crashloop`: every role restarts in a loop after a release.
  - `training/incidents/005-redis-blip-outage`: a 40 s Redis restart causes 502s everywhere. The existing chaos test fails on the branch and passes on `main`.
  - `ladder/S1`: deploy with a rehearsed rollback.
  - Real findings: there's no `.gitattributes`, and the migration checksum over raw bytes breaks across CRLF/LF checkouts; `compose.production.yaml` has no image tag; the health check both routes traffic and checks only the DB.
- **gitjira-app:** `training/ladder/J1` (readiness vs liveness) and `S1` (Fly → AWS). The deploy workflow ships only the API and doesn't wait for CI.
- **atlas:** `training/incidents/004-canary-rollback` (the old revision 500s) and `ladder/S1` (Azure Container Apps).
