# 10 — Diagnosing slow queries: plans, indexes, N+1

**Method** (use the same one every time)
1. **Find the query.** Postgres: `pg_stat_statements` (total and mean time). SQL Server: Query Store. App side: count queries per request; a sudden rise in statements/s means N+1.
2. **Read the plan.**
   - Postgres: `EXPLAIN (ANALYZE, BUFFERS)`.
   - SQL Server: the actual execution plan with `SET STATISTICS IO ON`.
   - Look for: Seq Scan / Clustered Index Scan on big tables, estimated vs actual row gaps (stale stats), sorts spilling to disk, and Key Lookups.
3. **Fix the shape before the index:** N+1 becomes batched `IN`/join/projection; overfetch becomes a projection of only the needed columns; offset pagination on deep pages becomes keyset.
4. **Index to the predicate + sort:** composite `(tenant_id, status, created_at)` in equality-then-range-then-sort order; covering/`INCLUDE` columns to avoid lookups; partial indexes for hot subsets.
5. **Build it online** (see [07](07-zero-downtime-migrations.md)) and **prove it**: before/after latency and the plan, recorded in the PR.

**Trap: aggregate-then-limit.** `LIMIT` after `GROUP BY` or a join does not cap the cost of the join/aggregation; filter or pre-aggregate first (astra1 EXPLAIN journal, ledger aggregate).

**Where these repos live now** (checked 2026-10-06):

| Name in this page | GitHub repo | HEAD | Incident branches on GitHub? |
|---|---|---|---|
| atlas | code: **elirc/atlas**; `training/`: **elirc/gitvg** `atlas/` | `19e8c2d` / `af91bab` | no |
| netdrop | **elirc/dotnet-drop** | `d7ae725` | no |
| netintercom | **elirc/dotnet-intercom** | `74e0a28` | no |
| gitjira-app | **elirc/gitjira** | `42abd2c` | no |
| astra1 ("Helios") | **elirc/helios-interplanetary** | `4e043bd` | **yes**, 001 and 002 |
| pulse | **elirc/gitvg** `pulse/` | `af91bab` | no |

Where a branch is missing, the brief on `main` carries the suspect diff, so rebuild the branch from it.

**Worked examples in your repos.** At B02 this page said they "all share the 'p95 180 ms → 3.7 s' shape". Checked against the briefs, that holds exactly for netdrop INC-004 and netintercom INC-005. Atlas INC-001 is **140 ms → 3,700 ms**. The rest have different numbers but the same lesson, so still drill them back to back.
- atlas:
  - `training/ladder/M1-cost-report-at-1m-payslips.md`: employment-cost report at 1.3M payslips, Postgres and SQL Server plans.
  - `training/incidents/001-payslip-history-latency`, `003-run-list-memory`.
- netdrop: `training/incidents/004-slow-folder-listing` (N+1 plus overfetch; statements/s 1.4k → 38k, ×27) and `ladder/M2-search-at-scale.md` (search at 2M files).
- netintercom: `training/incidents/005-inbox-list-latency` and `ladder/M1-inbox-query-at-scale.md`.
- gitjira-app: `training/incidents/001-board-cpu-storm` and `ladder/J2-issue-table-load-more.md` (the table stops at 50).
- astra1 (`elirc/helios-interplanetary`):
  - `training/review/EXPLAIN-JOURNAL.md` (3 heaviest queries).
  - `training/incidents/001-invoice-history-pagination` (OFFSET on an unindexed table).
  - An audit query whose OR branch defeats the index, now its own ticket: `training/ladder/M1-audit-or-query.md` (added B08), plus `J1-finance-composite-indexes.md`.
- pulse: `training/incidents/002-rollup-eligibility-array-identity` (the fast path is silently disabled).

## Worked trace: the atlas employment-cost report (ladder M1)

All references are to `elirc/atlas` at `19e8c2d`.

**1. The query.** `ReportQueries.EmploymentCostByCountryMonthAsync` (`src/Atlas.Infrastructure/Persistence/Reporting/ReportQueries.cs:52-96`):
- joins `Payslip → PayrollRun → Worker` (`:63-65`);
- filters `p.OrgId == orgId`, `r.State == Executed` and a half-open `PeriodStart` month range (`:66-69`);
- **projects** six columns instead of loading entities (`:70-76`) and runs `AsNoTracking`. That's step 3 of the method, already done.

**2. The fold.** The sums run **in C#** (`:83-95`). The comment at `:79-82` says why: "SQLite stores decimal as TEXT and cannot SUM it". The same code path runs in production on Postgres, so every payslip row in the month crosses the wire just to be summed.

**3. The indexes.** `PayslipConfiguration` declares only `HasIndex(p => p.RunId)` on `payslips` (`src/Atlas.Infrastructure/Persistence/Configurations/PayrollConfigurations.cs:110`). Nothing supports `OrgId = @org AND PeriodStart in [m, next)`.

### Predicting the plan (do this before you run it)
1. With no `(OrgId, PeriodStart)` index, Postgres has to read `payslips` for the whole tenant (or the whole table) and then filter by month. At M1's 1.3M payslips that's a Seq Scan or a large bitmap scan.
2. Then it hash-joins `payroll_runs` and `workers`.
3. Then it ships every matching row to .NET, where `GroupBy` folds them.
4. The **index to try first**, by the method's equality-then-range rule: `(OrgId, PeriodStart)`. To make it covering, add `INCLUDE (RunId, WorkerId, <amount columns>)`, which M1's hints spell out for both engines (`CONCURRENTLY` / `ONLINE = ON`).
5. The **shape fix** to argue for: push the `SUM … GROUP BY country, currency` into SQL on Postgres and keep the in-memory fold only for SQLite. M1's constraint is "totals must stay exactly equal (decimal, not double)", so prove it with the golden tests (`ReportQueriesTests` / `ReportEndpointsTests`).

## The failure mode, step by step: deep OFFSET (helios INC-001, branch on GitHub)

The suspect PR (in the brief, and on branch `training/incidents/001-invoice-history-pagination`) adds `listInvoiceHistory`. It runs `SELECT … FROM invoices WHERE organization_id=$1 ORDER BY created_at DESC LIMIT $2 OFFSET $3` with 20 rows per page.

1. At `4e043bd`, `invoices` (`db/migrations/005-finance-support-security.sql:15-24`) has indexes only from its PK and two `UNIQUE` constraints: `(organization_id, id)` and `(organization_id, subscription_id, period)`. No index matches `ORDER BY created_at`.
2. So for every page, Postgres collects **all** of the tenant's invoices, sorts them, skips `page × 20` rows and returns 20.
3. Even with a perfect `(organization_id, created_at DESC)` index, `OFFSET` still walks and discards the skipped rows. That explains the brief's log: 38 ms at page 0, 210 ms at page 15, 740 ms at page 30, 2,380 ms at page 45. The cost grows with depth.
4. **Fix both:** add the composite index (J1's pattern), *and* switch to keyset pagination (`WHERE (created_at, id) < ($last_created_at, $last_id) ORDER BY created_at DESC, id DESC LIMIT 20`). Tie-break on `id`, because `created_at` isn't unique.
5. **Regression test** (brief task 4): "returns 200" can't catch it. Assert the plan (no `Sort` node over the whole tenant), or assert a bounded row/buffer count at a deep page against a seeded tenant.

## Two senior findings (verified at HEAD)

**A. The same unindexed sort already ships on the dashboard.** `getHubSnapshot` reads `invoices … ORDER BY created_at DESC LIMIT 40` (`elirc/helios-interplanetary: src/server/hub.ts:139`). The same shape appears for `payment_attempts` (`:145`), `provider_charges` (`:148`, ordered by `charged_at`) and `support_tickets` (`:154`). None of these tables gets an `(organization_id, <sort col> DESC)` index in migrations 001–006, which is the gap ladder J1 lists. This is why INC-001's task 3 asks about the *other* reads. The incident just made the cost visible with depth; page 0 already pays a top-N sort over the whole tenant.

**B. The OR is a write-amplified read.**
- The incident timeline query (`src/server/queries.ts:28`, duplicated with a different `ORDER BY`/`LIMIT` at `src/server/agent-tools.ts:61`) filters `resource_id=$2 OR details->>'incidentId'=$2`.
- `audit_resource (organization_id, resource_id, occurred_at)` (`db/migrations/001-core.sql:76`) can serve only the first branch, so the OR forces a scan of the tenant's audit rows via `audit_tenant_time` (`:75`) or the heap.
- **Every** telemetry reading writes a `TelemetryRecorded` audit row whose details include `incidentId` (`src/server/telemetry.ts:140-148`). The scanned set therefore grows with sensor traffic, not with incidents.
- Fixes: a `UNION` of two index-friendly branches (dedupe on `id`), or an expression index on `(organization_id, (details->>'incidentId'), occurred_at)`. M1 makes you pick one and keep both callers' outputs byte-identical.

**Also (atlas, connects to [09](09-telemetry-correctness.md)):** INC-001's own app log line is `metric http.server.request.duration=3912.4ms {"method":"GET","status":"200"}`. It has no route tag, so the metric can't tell you *which* GET is slow. On-call finds the query only through the EF `Executed DbCommand (3,871ms)` warning and `pg_stat_statements`. That's step 1 of the method, done the hard way.

## Goal + Check ladder

**Goal:** given a slow endpoint, produce a before/after plan, a query count and a latency number, and explain each change in terms of the predicate, the sort and the rows touched.

1. **Junior: inventory indexes.** For `payslips` (atlas) and `invoices` (helios), list every index from the configuration or migration files. **Check:** atlas shows `RunId` only, at `PayrollConfigurations.cs:110`. Helios `invoices` shows only the PK and the two `UNIQUE`s at `005-…sql:16,21`.
2. **Junior: count queries.** Read `tests/Atlas.Api.Tests/Reporting/QueryCountingInterceptor.cs` and its user `ComplianceRosterQueryCountTests.cs`. **Check:** you can explain how the interceptor turns "N+1" into an assertable number, and write the same assertion for netdrop INC-004's listing (*run locally*: expect the count to drop from per-item to a constant).
3. **Mid: predict, then EXPLAIN.** Fill in an `EXPLAIN-JOURNAL.md` entry for helios Q1 (the ledger aggregate at `hub.ts:150-151`: `GROUP BY e.id ORDER BY e.created_at DESC LIMIT 40`). **Check:** your prediction names the aggregate-then-limit trap (all of the tenant's journal entries are aggregated before 40 are kept). *Run locally* with `npm run db:up && npm run db:migrate && npm run db:seed`. B03 ran without Docker, so the journal's plans are reasoned, not measured. You'd be the first to measure them.
4. **Mid: keyset.** Rebuild helios INC-001 locally (`git worktree add … training/incidents/001-invoice-history-pagination`), add the index and the keyset version. **Check:** latency at page 45 is about the same as page 0, and the plan has no full-tenant `Sort`.
5. **Senior: two engines (atlas M1).** Ship the `(OrgId, PeriodStart) INCLUDE (…)` index online on Postgres and SQL Server, and decide on the SQL-side sum. **Check:** both plans are recorded in the PR (index seek with no key lookup on SQL Server; no Seq Scan on Postgres), and the golden totals are unchanged.

## Debugging scenario: "p95 tripled, but the query plan looks fine"

pulse INC-002: `/insights/trend` p95 goes from ~410 ms to 1,180 ms after a "readability" refactor, and ClickHouse CPU doubles. There are no errors, and results are correct.

**How to work it:**
1. Compare the **plan you get** with the **plan you think you get**. The brief points you at the routing decision in `apps/api/src/index.ts` (`:74-76` at `af91bab`; the brief says `:73-76`), where `isRollupEligible(spec)` (`packages/insights/src/rollup.ts:14`) picks `compileTrendRollup` (the cheap `events_daily` path) or the raw scan.
2. A refactor that makes eligibility return `false` for the hot shapes doesn't break anything a correctness test sees, because both paths return the same rows. It just routes ~70% of load (per the brief's `docs/perf/query-shape-audit.md`) back to the raw scan.
3. The tell is a **mix shift**, not a slow plan: the raw-path query count goes up and the rollup count goes to zero.
4. The test that catches it asserts *which path* was chosen for each hot shape, not just that results match. The title, "array identity", tells you what kind of comparison to look for in `packages/insights/src/rollup.ts`.

The interview line: "Before I index anything, I check whether the fast path is even being taken."
