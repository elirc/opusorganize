# HNJOBTRACK: B06 report (LAB tier)

- **Repo:** `C:\Users\Owner\Desktop\_Organized Desktop\08 App And Product Projects\HNJOBTRACK`
- **What it is:** a FastAPI + Supabase (Postgres/RLS/PostgREST) + Next.js 14 job board with a GPT-4o-mini parsing
  pipeline and email digests.
- **Git:** the repo had **no `.git`**. I ran `git init` and committed the baseline `2bb1f26 chore: baseline snapshot
  before training` (respecting `.gitignore`; no `.venv`/`node_modules`). The training commit is `044efd2 training: add
  B06 apprenticeship materials` (a pathspec commit of `training/` only; 66 files). Nothing pushed; there is no remote.

## What I created (`training/`)

- `README.md`: index, suggested order, about 34 h.
- `lab/`:
  - `fake_supabase.py`: a query-builder fake with enum checks and a real-library `maybe_single` behaviour.
  - `rls/rls_lab.py` + `00_supabase_shim.sql` + `10_seed.sql`: Supabase-shaped roles/grants/`auth.uid()`, and an 11-probe
    table of what anon/authenticated/service can do. Docker **or** native Postgres mode.
  - `fixtures/parse_multirole.json`; `README.md`.
- `ladder/`:
  - J1 first-time-user 500s · J2 404 vs 500 · J3 reset preferences + delete policy
  - M1 For You at scale · M2 search filter injection + FTS · M3 lock down public tables (RLS) · M4 keyboard/screen reader
  - S1 Teams tenancy with DB-enforced isolation + noisy-neighbour/per-tenant budgets · S2 pipeline out of the API process
- `review/EXERCISE.md`, `review/COMPARE.md`; sealed `_answers/review.md` (21 findings).
- `incidents/001–005` briefs (symptom only).
- `navigation/`: ARCHITECTURE (3 flows with evidence), FIRST_CHANGE, TRADEOFFS (5 "Why?" drills), CHANGE_REQUEST.
- `agentic/WORKFLOW.md` (+ `_answers/agentic/RUBRIC.md`).
- `interview/`: PROJECT_STORIES (5), TECHNICAL_QUESTIONS (20), SYSTEM_DESIGN, MOCK_DEFENSE, FLASHCARDS (25).
- `_answers/`:
  - incident answers (written defensively: symptom → diagnosis → root cause with file:line → fix → test → postmortem;
    no exploit steps) and `00N-fix.patch` for all 5
  - ladder answers + `mid-03-lock-down-public-tables.sql`
  - navigation, interview, agentic answers
  - `regression-tests/` (conftest + 6 test files)

## Incident branches (symptom only)

| Branch | Commit | Symptom |
|---|---|---|
| `training/incidents/001-auth-local-jwt-decode` | ca5142a | An external report: another user's saved jobs were returned; 401s dropped sharply after a perf deploy |
| `training/incidents/002-parser-retry-backoff` | da7b07d | The whole API times out for ~30 min after the monthly cron starts, while CPU is idle |
| `training/incidents/003-camelcase-api-models` | 775891c | After a backend-only deploy, salaries vanish, the profile page errors, and excluded companies reappear in digests |
| `training/incidents/004-saved-jobs-user-scoped-rls` | 0cd9732 | Intermittently, at peak times, a user briefly sees someone else's saved jobs |
| `training/incidents/005-multi-role-type-prompt` | 15acb62 | The monthly thread is stuck at 21% parsed; re-runs barely progress |

## Verification (run 2026-09-24)

Each regression test was run against main, the incident branch, and the branch plus the sealed fix patch:

| Test | main | incident branch | + fix patch |
|---|---|---|---|
| inc001 JWT | pass (401s) | **fail** (bad signature and expired token → 200) | 3/3 pass |
| inc002 event loop | loop test passes; 429 test fails (the original flagging bug, intended) | **fail**: loop blocked 6.13 s with 3 listings | 2/2 pass |
| inc003 contract | pass | **fail** (`per_page`, `job_id`, `saved_at`, `display_name`, ... missing) | revert |
| inc004 concurrency | pass | **fail**: 20/40 responses carried the other user's data | pass |
| inc005 LLM boundary | **fail** (latent on main: same 22P02 crash) | **fail** | 2/2 pass |
| junior01 first-time user | **3/3 fail** with `'NoneType' object has no attribute 'data'` | n/a | not written (learner exercise) |

- **RLS lab:** ran on a **native PostgreSQL 18** cluster (the Docker engine was wedged after the disk-full event).
  Main: P7 anon UPDATE on `job_listings` = `UPDATE 1`; P8 anon INSERT on `hn_threads` = `INSERT 0 1`; P5 owner
  delete of preferences = `DELETE 0`. With the reference migration: P7/P8 → `ERROR 42501`, P5 → `DELETE 1`, P11 anon read
  still works. The enum rejection (22P02) was confirmed on real Postgres.
- **UNVERIFIED:**
  - No frontend code was run (no `node_modules` installed; disk tight). The frontend claims (INC-003 UI symptoms,
    ladder M4, review R6/R18/R19) are static reads.
  - No real Supabase/PostgREST; the lab shim reproduces roles/grants/`auth.uid()` only.
  - The `maybe_single()` → `None` finding was verified with the real postgrest-py 0.19.3 client against a simulated
    PostgREST 406/PGRST116 response, not against a live Supabase.
- PyJWT 2.10.1 was installed into `backend/.venv` (needed by incident 001; pinned in that branch's `requirements.txt`).

## Issues found in the project (main)

1. **Critical:** `hn_threads` and `job_listings` have no RLS; with Supabase default grants, the public anon key can
   modify listings (including apply links) and insert threads (verified P7/P8).
2. **High (verified):** 9 `.maybe_single().execute().data` call sites crash when no row exists (postgrest-py 0.19.3
   returns `None`): a job's first save, the first preferences save, For You without preferences, and **the first
   scrape of each new month** (`scraper.py:35`). The repo's own tests hide this with a fake that returns `self`.
3. **High:** all user data goes through the service-role client (BYPASSRLS); isolation rests on per-query filters only.
4. **High:** `/jobs?search=` interpolates user input into the PostgREST filter grammar (`jobs.py:34-36`).
5. **High:** model output is unvalidated into the DB, `href` (`apply_url`) and email HTML (unescaped).
6. **High:** an open redirect in `frontend/src/app/auth/callback/route.ts:8,31`.
7. **Medium:**
   - a manual `/admin/scrape` re-sends instant digests (`admin.py:21`, no dedupe);
   - daily/weekly digests are nearly always empty (`notifications.py:54-60`);
   - the admin key defaults to `"changeme"` (`config.py:14`);
   - the scheduler runs in the web process (duplicates with >1 worker).
8. **Presented as working but not:** the README's "tsvector full-text search" (the `fts` column is unused), "JWT
   verification" (it's a network call to Supabase Auth), and daily/weekly digests (item 7).
9. **Secrets:** none found. Only `.env.example` and `frontend/.env.local.example` (placeholders) exist; no `.env` in the repo.

## Skill links (for COMPETENCY_GRAPH)

- **DB-enforced tenant isolation / RLS (thin → now practised):**
  - `training/lab/rls/rls_lab.py` · `ladder/mid-03` · `ladder/junior-03` · `ladder/senior-01`
    (+ noisy neighbour, per-tenant budgets, tenant-aware jobs)
  - `incidents/004` · `incidents/001` (RLS bypassed by the service role)
  - `interview/TECHNICAL_QUESTIONS` 8–12 · `agentic/WORKFLOW.md`
- **Python/FastAPI async:** `incidents/002` · `incidents/004` (threadpool vs loop) · `ladder/mid-01` · `interview` Q13–14.
- **AI/LLM integration:** `incidents/005` · `incidents/002` (retry policy) · `ladder/senior-02` (cost cap, Batch API) ·
  `interview` Q15–16 · `lab/fixtures/`.
- **API back-compat/contracts:** `incidents/003` · `_answers/regression-tests/test_inc003_api_contract.py` · `interview` Q4, 18.
- **Accessibility / frontend:** `ladder/mid-04` · `navigation/CHANGE_REQUEST.md` (toast, live region, WCAG 2.2.1).
- **Testing:** `ladder/junior-01` (fakes that encode wrong assumptions) · 6 runnable regression tests.
- **SQL/indexes:** `ladder/mid-02` (the FTS index is unused) · `ladder/mid-01`.
- **Async jobs/idempotency** (saturated; only linked): `ladder/senior-02` → curriculum 01/02.
- **Security (OWASP):** review R1, R4, R5, R6 · `incidents/001`.
- **Code review:** `review/`. **Unfamiliar codebase:** `navigation/`. **Agentic:** `agentic/`.

## Curriculum needs (one central page each; not written by me)

- **"Database-enforced isolation: RLS as defense in depth"**
  - Scope: service role vs user-scoped clients; policies per command; grants + RLS; policy performance
    (`(select auth.uid())`); testing with probe tables.
  - The backlog item "Row-level multi-tenancy (EF filters + RLS)" now has a second project (HNJOBTRACK + aaa1/grok per
    B06), so it qualifies.
- **"Python async: blocking the event loop"**
  - Scope: sync I/O and `time.sleep` in `async def`; `def` handlers in the threadpool and the shared-state hazard; loop-lag
    detection; ruff ASYNC rules.
- **"API contracts between backend and frontend"** (maybe fold into 07)
  - Scope: consumer-driven contract tests, alias/serialization changes, and expand/contract for JSON fields.

## Existing learning-doc trees

- `astraupskill/` (8 md files + evidence + snapshots): a worked change on scraper retry/idempotency. Verdict: **KEEP**
  (link it from the graph under idempotency). It is narrow but accurate. I left it untouched and didn't duplicate it.

## Caveats

- One of my responses was stopped by a safety classifier while I was writing incident answers. The answers were then
  rewritten to be strictly defensive (flaw class, detection, prevention; no exploit steps). The regression test for 001
  still builds an invalidly signed token *inside the test* to assert a 401, the usual way to test auth.
- Tests are slow here (1–3 min per file, import cost).
- The incident "production" numbers in the briefs (latencies, counts) are **invented for realism**. Only the numbers in
  the Verification section were measured.
- **Left behind in the scratchpad:** a stopped native PG18 data dir at `scratchpad/HNJOBTRACK/pgdata` (~40 MB), plus
  small message/log files. Not deleted (no recursive deletes). `rls_lab.py native-up` would use `%TEMP%\hnjobtrack-training-pgdata` instead.
- No Docker containers left running.
