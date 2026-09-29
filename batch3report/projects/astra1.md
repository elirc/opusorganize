# astra1 — Helios Interplanetary (B03 report)

**Tier:** DRILL (Phase 3 + small Phase 5 interview kit, per B03_AGENT_BRIEF)
**Batch focus:** raw-SQL performance diagnosis + telemetry correctness (curriculum pages 09/10). Authz/
concurrency explicitly out of scope (saturated per brief).

## What was created

- `training/README.md` — index, suggested order (~3–4 hrs), verification-status summary.
- `training/review/EXERCISE.md` — 60-min blind review of tenant-scoped read paths (`queries.ts`, `hub.ts`,
  `agent-tools.ts`, all 6 migration files, `metrics/route.ts`, `observability.ts`).
- `training/review/COMPARE.md` — my-findings-vs-model template.
- `training/review/EXPLAIN-JOURNAL.md` — the requested **extra exercise**: an `EXPLAIN (ANALYZE, BUFFERS)`
  journal for the 3 heaviest queries (ledger view join+aggregate `hub.ts:151`, task fan-out join `hub.ts:43`,
  incident audit-trail OR query `queries.ts:28`).
- `training/incidents/001-invoice-history-pagination.md` + branch
  `training/incidents/001-invoice-history-pagination` (commit `c2b2688`) — **planted** bug: a new
  `GET /api/billing` invoice-history endpoint using `LIMIT/OFFSET` against `invoices`, which has no supporting
  composite index. Symptom only in the brief (latency grows with page depth); no cause given.
- `training/incidents/002-metrics-blind-spot.md` + branch `training/incidents/002-metrics-blind-spot`
  (== `main` HEAD `3a9bc1e`, no new commit — the bug is already shipped) — **real, pre-existing** bug: the
  OTel exporter (`src/server/observability.ts:7-9`) only forwards spans that have `helios.organization_id`
  set, and that attribute is only set *after* `verifySession` succeeds (`src/server/identity.ts:117`), so
  every `401 UNAUTHENTICATED` (and any `assertLocalRequest` rejection) never reaches `request_spans`, and
  `/api/metrics` silently undercounts. Real diff cited is the actual historical commit `75c4d82` that
  introduced the whole pipeline.
- `training/interview/PROJECT_STORIES.md` (5 STAR prompts) and `training/interview/TECHNICAL_QUESTIONS.md`
  (10 questions), both specific to this codebase.
- `training/_answers/review.md`, `training/_answers/explain-journal.md`,
  `training/_answers/incidents/001-invoice-history-pagination.md`,
  `training/_answers/incidents/002-metrics-blind-spot.md` — all sealed.

Committed to `main` via pathspec commit `9d64e5a` (`training: add B03 apprenticeship materials
(raw-SQL performance + telemetry)`), touching only `training/`. The repo's 7 pre-existing uncommitted files
(`README.md`, `docs/project/current-state.md`, `tests/integration/repair.test.ts` modified;
`astraupskill/`, `docs/exec-plans/003-repair-rollback-regression.md`, `scripts/test-owned-postgres.py`,
`upskilling/repair-rollback/` untracked) were left completely untouched — verified by `git status --short`
before and after.

## Verification

**Static/schema, high confidence (verified by reading, not by running):**
- Missing composite index on `invoices` (also `support_tickets`, `payment_attempts`, `provider_charges`):
  confirmed against `db/migrations/005-finance-support-security.sql` — none of these four tables has an index
  ending in their hot-path sort column, while five sibling tables in the same schema
  (`audit_tenant_time`, `work_orders_tenant_status`, `request_spans_tenant_time`, `energy_history`,
  `readings_asset_time`) do.
- OR-defeats-index bug: confirmed against `db/migrations/001-core.sql`'s `audit_resource` index definition
  and the exact query text at `src/server/queries.ts:28` and its duplicate at `src/server/agent-tools.ts:61`.
- Telemetry blind spot: confirmed by tracing `src/server/http.ts:35-50` →
  `src/server/identity.ts:81-119` → `src/server/observability.ts:5-35` line by line; the control flow is
  synchronous and unconditional, so static tracing is sufficient (no live server needed).

**UNVERIFIED:**
- `EXPLAIN (ANALYZE, BUFFERS)` output for the 3 heaviest queries. Attempted `docker compose up -d --wait`;
  it failed immediately (not a hang) with `failed to connect to the docker API at
  npipe:////./pipe/dockerDesktopLinuxEngine ... The system cannot find the file specified` — the Docker
  Desktop daemon was not running. Did not attempt to start Docker Desktop itself (out of scope / open-ended
  time cost for a background app). All plan-shape reasoning in `_answers/explain-journal.md` is derived from
  the schema + standard Postgres planner behavior and is clearly marked as reasoned, not measured, with
  instructions to re-run for real numbers. Also noted: this repo's seed fixtures are demo-scale, so even a
  live run against seeded data would not reproduce the "3 years live" scale plans discussed — this is stated
  explicitly in the sealed answer.
- The planted INC-001 commit's TypeScript was not compiled (`BUILD: UNVERIFIED` per brief's escape hatch) —
  `node_modules` were not installed in this session (judged not worth the time cost for a ~30-line diff that
  closely mirrors an existing, working pattern in the same files). Hand-checked against
  `src/server/billing.ts`'s existing `Pool`/`Principal` imports and `queries.ts`'s `pool.query<{...}>`
  generic-row style.

## Issues found in the project (beyond what became exercises)

- No secrets found in the repo (checked `.env` is present but not read/quoted; `.env.example` looks like
  placeholder demo values only — `compose.yaml` ships a hardcoded demo DB password
  `helios_local_only`, which is fine for a local-only Postgres port bound to `127.0.0.1:5438`, not a real
  secret).
- Nothing presented as working that isn't — the README's "local test runs ≠ CI" disclaimer (noted in the prior
  audit, `batch-06.md:42`) is honest and the codebase backs it up.
- The 7 uncommitted files are unrelated to this batch (repair-rollback exec plan / a Python DB-ownership test
  script / `astraupskill` regenerated content) and were not inspected beyond confirming their paths for the
  "never touch" rule.

## Skill links for the competency graph

- **SQL: query plans, indexes, N+1** → `astra1/training/review/EXPLAIN-JOURNAL.md` +
  `astra1/training/_answers/explain-journal.md` (3 queries) · `astra1/training/incidents/001-invoice-history-pagination`
  (missing index + OFFSET trap) · `astra1/training/review/EXERCISE.md` findings 1–4.
- **Observability / SLOs** → `astra1/training/incidents/002-metrics-blind-spot` (span-attribute-after-throw
  drop bug) · `astra1/training/review/EXERCISE.md` finding 5 · `astra1/training/_answers/review.md`
  telemetry-correctness section.
- **Interview kit (mini, DRILL tier)** → `astra1/training/interview/PROJECT_STORIES.md` (5 stories) ·
  `astra1/training/interview/TECHNICAL_QUESTIONS.md` (10 questions).

## Curriculum needs (concepts referenced, not written centrally)

- None new — this batch drilled entirely against the two existing central pages
  (`curriculum/09-telemetry-correctness.md`, `curriculum/10-query-plans-and-indexes.md`) without needing a new
  concept page. One addition worth considering for `curriculum/10-...`: the "`LIMIT` after `GROUP BY` doesn't
  bound the pre-aggregation work" trap surfaced by the ledger query (Q1 in the EXPLAIN journal) — it's a
  slightly different failure mode from plain missing-index or OR-defeats-index, and didn't have a clean home
  in the existing page's bullet list. Title: **"Aggregate-then-limit: why LIMIT after GROUP BY doesn't cap
  join/aggregation cost"** (2-line scope: when a query joins, aggregates, then sorts+limits, the LIMIT cannot
  be pushed below the aggregation, so the full join+aggregate cost is paid regardless of how few rows are
  returned; fix by bounding the join's input set before aggregating, not just indexing the sort).

## Existing learning-doc trees — KEEP / MERGE / CONVERT / IGNORE

- **`astraupskill/`** (9 files, generic 8-chapter template + evidence/snapshots) — **KEEP**. Matches prior
  audit's description exactly; covers a "worked change" narrative, codebase map, testing/debugging, a trace
  lab. No overlap with this batch's performance/telemetry focus.
- **`upskilling/`** (31 bespoke files: case-studies, labs, lessons, repair-rollback, retrospective, solutions,
  templates) — **KEEP**, unmodified. Confirmed by directory listing: covers request-to-row architecture,
  agent-loop supervision, long-run recovery, and a full "how this app was actually built" retrospective — none
  of it addresses raw-SQL performance diagnosis or telemetry correctness, so this batch adds net-new coverage
  rather than duplicating. Prior audit calls this "the standout artifact" of the astra family; nothing found
  here changes that assessment.
- No **MERGE** or **CONVERT** candidates identified — neither tree contains generic tutorial content that
  belongs in the central `curriculum/` folder, and neither overlaps enough with the new `training/` material
  to warrant conversion.

## Honest caveats

- Two incidents only (DRILL-tier minimum), both scoped tightly to the batch focus; a LAB-tier pass on this
  repo could easily support 4–6 incidents (this app has ~9 unindexed-or-partially-indexed tenant tables, a
  richer OTel surface via `src/instrumentation.ts`, and an outbox/worker system not touched here at all).
- No live Postgres was reachable in this session (Docker daemon down, not hung — did not attempt to bring
  Docker Desktop up). All performance-diagnosis reasoning is schema-and-planner-model based, not measured;
  this is flagged inline in every file where it matters, not just here.
- The planted incident (001) was not compiled. If this matters before someone works through it, run
  `npm ci && npx tsc --noEmit` (or open the worktree and `npm run dev`) before relying on it as a "does this
  even build" check — I did not have budget to install a full Next.js `node_modules` tree in this session.
