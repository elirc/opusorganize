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

**Worked examples in your repos** (all share the "p95 180 ms → 3.7 s" shape, so drill them back to back)
- atlas:
  - `training/ladder/M1`: employment-cost report at 1.3M payslips, Postgres and SQL Server plans.
  - `training/incidents/001-payslip-history-latency`, `003-run-list-memory`.
- netdrop: `training/incidents/004-slow-folder-listing` (N+1 plus overfetch; statements/s ×27) and `ladder/M2` (search at 2M files).
- netintercom: `training/incidents/005-inbox-list-latency` and `ladder/M1`.
- gitjira-app: `training/incidents/001-board-cpu-storm` and `ladder/J2` (the table stops at 50).
- astra1: `training/review/EXPLAIN-JOURNAL.md` (3 heaviest queries), `training/incidents/001-invoice-history-pagination` (OFFSET on an unindexed table), and an audit query whose OR branch defeats the index.
- pulse: `training/incidents/002-rollup-eligibility-array-identity` (the fast path is silently disabled).
