# Batch 06 Report: tenant isolation enforced by the database, plus Python/FastAPI

> **Status note (added 2026-10-06):** this report is a frozen record of the batch and was not updated afterwards. Not every `training/incidents/*` branch it describes is on GitHub: only 21 of the 92 from B01–B07 were pushed, and several projects now live under different elirc repo names. Before you try to check out an incident, see the incident-branch availability note at the top of [`apprenticeship/PROGRESS.md`](../apprenticeship/PROGRESS.md).

*2026-09-24 · I ran `apprenticeship/BATCH_PROMPT.md` on 3 projects. App-level tenant scoping was already saturated, so this batch
teaches the **backstop**: Postgres row-level security (RLS) and tenant-safe keys, plus a Python/FastAPI stack.
Per-project detail is in `projects/<name>.md`. Shared outputs: `apprenticeship/curriculum/19–21` (new), `COMPETENCY_GRAPH.md` (updated after B07).*

## ⚠ 1. Read first: this batch ran through a disk-full outage
- Mid-batch, the **C: drive filled to 46 MB free** and every running agent died on API errors. After cleanup, all agents resumed and finished.
- **Cleanup (with your approval):**
  - cleared the npm, NuGet and pnpm caches;
  - removed `node_modules` from 8 *finished* repos, junction-safe, with `git status` verified identical before and after;
  - **wiped Docker's data disk** (7.3 GB; all images, containers and volumes are gone).
- **Free space went from 46 MB to 13.3 GB.** Those 8 repos need `npm ci` / `pnpm install` before running:
  gitjira-app, lucasrouter, astraspacegameweb, buildevent, buildermentor, aiheartbeat, relay, folio.
- **Docker was wedged for this whole batch,** so all database verification ran on **native Postgres 18** clusters the agents started privately. All of them are now stopped.

## 2. Tiers
| Project | What it is | Tier |
|---|---|---|
| **aaa1** | multi-tenant CRM, Next 15 + Prisma 6 + worker | **LAB**: RLS with Prisma, tenant-aware jobs, noisy neighbours |
| **HNJOBTRACK** | HN job board, FastAPI + Supabase (Postgres RLS) + Next + OpenAI | **LAB**: Python/FastAPI and Supabase RLS in practice |
| grokbuildmultitenantproject | Express/TS + Prisma, a hardened rewrite of a flawed Grok starter | DRILL: compound FKs + legacy-diff review |

## 3. What was created
| Project | Commits | Contents | Incidents | Effort |
|---|---|---|---|---|
| aaa1 | baseline `0a99ba0` (new git), training `ca1986f`; lab base `training/base/rls-foundation` `4ca048e` | 10 tickets (RLS, per-tenant fairness, accessibility, frontend perf, AI) · review (24) · navigation · agentic + rubric · full interview kit | 5 | ~45–55 h |
| HNJOBTRACK | baseline `2bb1f26` (new git), training `044efd2` | 9 tickets (J1–J3, M1–M4, S1 DB-enforced tenancy + noisy neighbours, S2) · review (21) · navigation · agentic · full interview kit · fake-Supabase + RLS probe lab · 6 runnable regression tests + 5 fix patches + a reference migration | 5 | ~34 h |
| grokbuildmultitenantproject | training `cb03e05`; incident base `training/base/working-tree-snapshot` `06d0205` | review (19) · **legacy-diff drill** (Grok starter vs hardened rewrite) · mini interview kit | 2 | ~7 h |

**Git notes**
- aaa1 and HNJOBTRACK had **no git**, so each got a baseline commit first.
- grokbuildmultitenantproject's last commit is the old Grok snapshot, and **your 48 uncommitted files are the real rewrite**.
  Its incidents branch from a **snapshot branch that contains your uncommitted work**. Your working tree itself is untouched (checked).
- Every training commit touches only `training/` (checked). Nothing was pushed, and no worktrees are left.

**Incident symptoms** (causes sealed in `_answers/`)

*aaa1*
1. Lead lists intermittently come back empty after a perf deploy.
2. Imports sit in QUEUED while the worker looks healthy.
3. One tenant's confidential notes appear for another tenant.
4. A retention purge deletes another tenant's deals, including one under legal hold. Only the *pair* of commits breaks it.
5. One big tenant's import slows everyone else and then fails partway.

*HNJOBTRACK*
1. A user's saved jobs are returned to someone else, and 401s drop after a perf deploy.
2. The whole API times out during the monthly cron while CPU is idle.
3. After a backend-only deploy, UI fields vanish and exclusions are wiped.
4. Intermittent cross-user saved jobs at peak times.
5. The monthly thread stalls at 21% parsed.

*grokbuildmultitenantproject*
1. A customer sees a stranger's name and email as a task assignee.
2. A contractor reads another tenant's project names through a new dashboard endpoint.

## 4. Verification (all run against real Postgres 18)
| Project | Verified |
|---|---|
| aaa1 | **All 5 reproduced live:**<br>• 001: 89/240 empty lists<br>• 002: imports=0 / outbox=0 every tick<br>• 003: probe fails and the canary alerts<br>• 004: purge deleted 4 deals instead of 2<br>• 005: other tenant's p50 352 → 1,820 ms, import FAILED at 100/400<br>Typecheck is 0 errors everywhere; the main suite passes (62 tests).<br>Incident 005 did not reproduce at 25 rows per batch on this laptop, so the branch now uses 100 rows and the answer records the 25-row result. |
| HNJOBTRACK | Every incident test **fails on its branch and passes with its fix patch**:<br>• 002: event loop blocked 6.13 s<br>• 004: 20/40 responses had the other user's data<br>RLS lab probes P1–P11 ran on PG18. The reference migration turns the anon-write probes into 42501. |
| grokbuildmultitenantproject | The base passes backend, frontend and seed. INC-001: exactly the 2 intended regressions fail (42 pass). INC-002: fails as intended (200 instead of 403). Both fixes together: 46/46. The RLS probe verified all four RLS properties (see §5). |

**HNJOBTRACK note:** a safety filter interrupted the agent while it wrote an auth-bypass answer.
It resumed with instructions to explain defensively (symptom → root cause → fix → test → postmortem, no attack steps), and finished that way.

## 5. Real defects found (documented, NOT fixed)

**HNJOBTRACK**
- **Critical:**
  - `job_listings` and `hn_threads` have **no RLS**, so the public anon key can **rewrite job apply links** and insert threads (probes P7/P8).
  - All user data is read through the service role, which bypasses RLS.
- **Other:**
  - The 9 `maybe_single()` call sites crash when no row exists, including the first scrape of every month (`scraper.py:35`). A user's first save and first preferences save also fail (junior test: 3/3 `NoneType` errors). The repo's own fake tests hide this.
  - No DELETE policy on `user_preferences`.
  - User input is interpolated into search filter strings.
  - LLM output goes unvalidated into the DB, links and email HTML.
  - An open redirect in the auth callback.
  - An admin re-scrape re-sends digests.
  - The README claims full-text search and JWT verification that don't exist.

**aaa1**
- A demo bearer token and tenant header are hard-coded in the browser bundle (`src/hooks/apiClient.ts:12-15`).
- `APP_SESSION_SECRET` is declared but unused.
- There's no migration history (`db push` only) and only mock-based tests.
- `docs/roadmap` describes defects that are already fixed, and `docs/learning/phase-2..5` has about 108 broken links.

**grokbuildmultitenantproject**
- `docker-compose.yml` on main uses default credentials exposed on 0.0.0.0.
- `astraupskill/VERIFICATION.md` cites evidence folders that don't exist.

**RLS lessons proven on real Postgres** (grokbuild probe):
- a **superuser bypasses RLS even with FORCE**;
- with no tenant context the app role sees 0 rows;
- `WITH CHECK` blocks cross-tenant inserts;
- a **session-level `SET` leaks to the next user of a pooled connection, and a DELETE on the leaked connection removed another tenant's row**.

## 6. Existing learning docs: verdicts
| Repo | Verdict |
|---|---|
| aaa1 | `docs/architecture`, most of `docs/learning`: KEEP · `phase-2..5`: KEEP, but they need a link fix (needs your approval) · `concepts-demonstrated.md`: IGNORE · `docs/roadmap`: CONVERT to exercise |
| HNJOBTRACK | `astraupskill/`: KEEP |
| grokbuildmultitenantproject | `astraupskill/`, `dfableandopus/`: KEEP |

## 7. Curriculum
- **New pages:** [19 Database-enforced isolation](../apprenticeship/curriculum/19-rls-defense-in-depth.md) (all three projects),
  [20 Money and time](../apprenticeship/curriculum/20-money-and-time.md), [21 Legacy rescue and ports](../apprenticeship/curriculum/21-legacy-rescue-and-ports.md).
- **Backlog:** "Python async: blocking the event loop" (HNJOBTRACK only so far); "tenant data lifecycle" (aaa1).

## 8. What to do first (about 1.5 weeks part-time)
1. **aaa1 lab:** check out `training/base/rls-foundation`, run the probes and the canary, then do **INC-001** (stale tenant on pooled connections) and **INC-003** (a new table without a policy). Read page 19 alongside.
2. **HNJOBTRACK:** run `training/lab/rls` on main to watch the anon key write listings, then apply the reference migration. Do **INC-004** (shared client leaking users).
3. **HNJOBTRACK INC-002:** find what blocks the async loop. This is the Python async lesson.
4. **grokbuildmultitenantproject legacy-diff drill:** what did the hardening fix, and what did it miss? Remember that `git diff` hides untracked files.
5. **aaa1 INC-004:** two harmless commits that break only together. A strong code-review interview story.
