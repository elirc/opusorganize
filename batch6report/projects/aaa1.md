# aaa1: B06 report (LAB)

Project: `C:\Users\Owner\Desktop\_Organized Desktop\12 Other Projects\aaa1`, a multi-tenant CRM (Next.js 15.5 / React 19 / Prisma 6.19 /
PostgreSQL + a polling worker `src/worker.ts`). Tier: **LAB** (Phases 2-5). Batch focus: database-enforced tenant isolation.

## Git state (the repo had no `.git`)
- `git init -b main` + baseline **`0a99ba0` "chore: baseline snapshot before training"** (244 files, respecting `.gitignore`, no node_modules).
  Repo-local identity set (`user.name elirc`, `core.autocrlf false`). No remote configured, nothing pushed.
- Training materials: **`ca1986f` "training: add B06 apprenticeship materials"** on `main` (pathspec commit of `training/` only).
- Lab base branch **`training/base/rls-foundation` @ `4ca048e`**, "phase 1 of an RLS rollout" on top of main:
  `prisma/rls/001_roles_and_grants.sql`, `prisma/rls/010_tenant_policies.sql`, `src/lib/db/tenantDb.ts` (`withTenant()`), lead list/create +
  import worker + retention purge moved onto `withTenant`, 3 unit test files updated for the new wrapper, and `training/lab/rls/` (setup for Docker **or**
  native Postgres, seed with 2 tenants, canary, 5 probes). All incidents branch from it. This is new code I wrote, not user code.

## Incident branches (symptom only)
| Branch | Commit | Symptom |
|---|---|---|
| `training/incidents/001-tenant-read-fastpath` | `28f3ca3` | Lead lists intermittently come back empty after a "perf" deploy. No errors, p95 improved. |
| `training/incidents/002-worker-least-privilege` | `ef6fb88` | After a security hardening release, imports sit in QUEUED and workflow rules stop firing. The worker reports fast, error-free ticks. |
| `training/incidents/003-company-enrichment` | `be0c07d` | A new "company panel" shows one tenant's confidential account notes to another tenant. |
| `training/incidents/004-retention-batch` | `53a983e`, `80fdc93` | One tenant's retention purge deleted another tenant's archived deals, including one under legal hold. CI green. |
| `training/incidents/005-parallel-import` | `e816c00` | During a big tenant's CSV onboarding, every other tenant's requests slow down about 5x, and the onboarding import itself ends FAILED part-way with inconsistent counts. |

## Verification (what actually ran)
Docker was wedged during the run (see the disk-full incident). Every DB verification ran on a **private native PostgreSQL 18 cluster**
(`initdb` in the scratchpad, port 55471), a fresh database per run. The lab supports this via `LAB_PSQL` (documented in `training/lab/rls/README.md`).
- `tsc --noEmit`: 0 errors on the base and on incidents 001, 002, 004, 005. Incident 003: 0 errors, after `prisma generate` for its schema.
- Base unit tests touched by the base branch: `import.worker`, `retention.service`, `transaction-boundaries` → 3 files / 4 tests passing.
- Full `npm test` on main: **33 files / 62 tests passing** (vitest 2.1.9, run after all the incident work, with the client regenerated from main).
- Base branch, all probes PASS: canary `checked=35 alerts=0`; `probe-concurrency` 240/240 ok with idle connections `role=crm tenant=""`;
  the worker processes a Globex import to COMPLETED; retention PASS (deletes only Acme's 2 deals); noisy probe PASS (Globex p50 352 ms, max 1085 ms, 0 errors while Acme's 400-row import ran; the tick took 181 s on this loaded laptop).
- Incident reproductions on the live DB:
  - 001: `ok 150 / empty_list 89 / pool_wait 1`, idle connections left as `role=crm_app` with stale `app.tenant_id` → FAIL.
  - 002: `worker connected as crm_app`, 3 ticks with imports=0 / outbox=0, the job stays QUEUED → reproduced.
  - 003: `probe-enrichment`: Globex receives Acme's row, including `accountNotes` → FAIL. Canary: `ALERT rls_canary table=CompanyEnrichment rls_disabled no_policy visible_foreign_rows=1`, `checked=36 alerts=1`.
  - 004: `deletedDeals: 4`, Globex's deals gone, including the held one → FAIL. **Commit 1 alone (`53a983e`) → PASS**, verified in a detached worktree. Only the combination breaks.
  - 005: at chunk size 100: Globex p50 1820 ms / max 2726 ms (base 352 / 1085), and Acme's import FAILED at 100/400 rows with
    "Unable to start a transaction in the given time" (rows IMPORTED 24 / FAILED 15 / PENDING 361, successRows 36, so 12 leads were created without their row being marked) → FAIL.
    **Calibration note:** my first version used chunks of 25 and did NOT reproduce on this laptop (PASS: p50 401 ms, max 1643 ms, import completed, 10x faster).
    I amended the branch to 100 (`e816c00`) and documented the 25-row result in the answer. tsc was verified at 25. The amend changed only the constant, a comment and the commit message.
- Prisma refused `db push --force-reset` because it detected an AI agent. I did not bypass it. The lab setup was changed to never wipe:
  it creates a fresh `LAB_DB` and refuses a non-empty one.

## Issues found in the project (details: `training/_answers/review.md`, 24 findings)
- **Credential shipped to the browser:** `src/hooks/apiClient.ts:12-15` hard-codes a bearer token + tenant header matching a session created by `prisma/seed.ts:76-96` (demo credentials, OWNER role). Location only.
- `.env.example` has placeholder DB credentials and `APP_SESSION_SECRET`, which **nothing in `src/` reads** (config that does nothing). No `.env` present.
- Presented as working but isn't / unverified: `build-final.log` stops at "Linting and checking validity of types…", so the build result is UNKNOWN.
  `docs/roadmap/phase-1-reliability-hardening.md` describes defects that the current code has already fixed (e.g. lead + audit + outbox now share one transaction), so the roadmap is stale.
  `docs/learning/phase-2..5*.md` contain ~108 links to the old path `C:/Users/Owner/Desktop/aaa1/...` (the project moved), and they're broken.
- Top production risks on main: tenancy enforced only by app `where` clauses; import jobs stuck RUNNING on crash with duplicate leads on re-run;
  no webhook fetch timeout (one tenant's endpoint stalls all deliveries); FAILED outbox events never auto-retried; exports silently truncated at 1,000 rows; CSV formula injection;
  webhook secrets in plaintext; no migration history (`db push` only); tests are 100% mock-based.

## Skill links (competency graph)
- **DB-enforced tenancy / RLS** → base branch `training/lab/rls/*`; ladder J3, M1; incidents 001, 002, 003, 004; interview Q1-6; agentic M1; flashcards 1-11.
- **Tenant-aware background jobs** → incident 002; ladder M2 (dispatcher vs processing); interview Q7-9; S3 (scoring worker).
- **Noisy neighbours / per-tenant limits** → incident 005; ladder M2, M3; SYSTEM_DESIGN pressure points 2-4; interview Q9-10.
- **Data lifecycle (offboarding/DSR/retention)** → incident 004; ladder S2.
- **Tenancy models (pooled/silo/hybrid)** → ladder S1; SYSTEM_DESIGN.
- **AI features** → ladder S3 (tenant-isolated embeddings, injection bounded by output schema, per-tenant budget).
- **Accessibility** → ladder J2 (LeadTable/DealBoard names, live region, focus after move).
- **Frontend performance** → ladder M4 (debounce, abort, keepPreviousData).
- **API design** → ladder J1 (paginated failed rows, back-compat of the old field, 404 vs 403); navigation CHANGE_REQUEST.
- **Code review** → `training/review/` (24 findings, 8 flagged AI smells).
- **Unfamiliar codebase** → `training/navigation/*`.
- **Agentic engineering** → `training/agentic/WORKFLOW.md` + rubric.
- Deliberately *not* added (saturated): plain IDOR/authz, concurrency races, idempotency/outbox (referenced only).

## Curriculum needs (not written)
1. **"Database-enforced multi-tenancy (Postgres RLS)"**: roles vs owner vs superuser/BYPASSRLS, FORCE, `set_config`/`SET LOCAL` with pooled
   clients and PgBouncer transaction mode, fail-closed policies, SECURITY DEFINER exceptions, the canary, RLS with Prisma. Referenced by every incident here.
2. **"Noisy neighbours and per-tenant fairness"**: shared pools and bulkheads, fair dispatch in SQL (`row_number() OVER (PARTITION BY tenant)` + `SKIP LOCKED`),
   per-tenant quotas with atomic counters. Could extend page 14 instead of a new page.
3. **"Tenant data lifecycle"**: export, batched resumable delete, legal holds, DSR, what can't be deleted (backups/webhooks), deletion certificates.

## Existing learning-doc trees
| Tree | Verdict | Why |
|---|---|---|
| `docs/architecture/` (5 files) | **KEEP** | Accurate, cites real files. Link from the graph as this repo's architecture reference. It has no RLS content, which is fine. |
| `docs/learning/build-journal.md`, `flow-traces.md`, `guided-reading-path.md`, `load-bearing-files.md`, `testing-rationale.md`, `complexity-slice-implementation-process.md` | **KEEP** | Project-specific decision log and reading paths. `build-journal.md:143-146` is the RLS deferral that this pack builds on. |
| `docs/learning/concepts-demonstrated.md` | **IGNORE** | A glossary of generic patterns with pointers. Duplicates the central curriculum. |
| `docs/learning/phase-2..5*.md` | **KEEP (fix links)** | Useful change narratives, but ~108 links point to the old `C:/Users/Owner/Desktop/aaa1` path. The user should approve a mechanical link fix. |
| `docs/roadmap/*` (5 files) | **CONVERT TO EXERCISE** | Partly stale (lists defects already fixed). A good "verify every roadmap claim against the code" drill for the navigation pack. Not written yet. |

## Honest caveats
- Timings come from a heavily loaded laptop (7 agents, 6-8 GB free disk). Absolute latencies are inflated. Compare base vs branch only.
- The lab owner is a superuser. The base branch simulates the least-privilege app via `SET LOCAL ROLE`, which is a lab shortcut, not a production role design (M1 covers the real one).
- Incident 003 changes the Prisma schema. The shared `node_modules/.prisma/client` was regenerated for it and then regenerated back from `main`'s schema (verified: the generated schema has 37 models and no `CompanyEnrichment`).
- Incidents are based on my base branch, not on user code. `main` itself contains only the user's original code + `training/`.
- `vitest.config.ts.timestamp-*.mjs` left untracked in the main tree by an interrupted vitest run (ENOSPC during the disk-full event): deleted (a single untracked file I created). `git status` on main is clean.
- Incident 003's brief shows the canary alert (`rls_disabled no_policy`), which makes "which table" easy. That's intentional (it's what on-call would see).
  The exercise is *why* the policy is missing (a hand-maintained table list) and the grant-timing question.
- The earlier session's context was lost to the disk-full crash. I rebuilt it from the filesystem and my prior transcript. One defect from before the crash
  (a duplicated `processedImports += 1` in my base-branch edit) was found and fixed before the base commit.

## Cleanup / machine state
- All 7 worktrees removed (`git worktree list` = main only). Branches kept: `training/base/rls-foundation` + 5 incident branches. Nothing pushed.
- `node_modules` in the repo was installed with `npm install` during the first session (package-lock present; left installed, gitignored). No Docker containers or images created by me (Docker was wedged).
- The private PG18 cluster was stopped. `pgdata` (152 MB) in my scratch folder was deleted after unlinking the scratch `node_modules` junction first
  (non-recursive `rmdir` on the junction; the repo's node_modules was verified intact with 156 entries).
- Time for the user to work through the pack: ~45-55 h (breakdown in `training/README.md`).
