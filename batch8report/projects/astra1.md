# astra1 (Helios Interplanetary): B08 learn pass

- **Path:** `C:\Users\Owner\Desktop\astra1`, tier DRILL (raw-SQL Postgres perf + telemetry)
- **Branch / commit:** `main` @ **`db055d8`** `docs(training): add learn/ study guide + junior on-ramp (B08)`. The parent is B03's `9d64e5a`.
  It's a pathspec commit (`git add learn training`). The user's 7 uncommitted files were untouched (`git status` identical before and after). Not pushed.

## Files added (9)
- `learn/README.md`: machine-state notes, 6 prerequisites (curriculum 10/09/05/04/07 + `upskilling/lessons/01-request-to-row.md`), a 10-session route with exit criteria, a do-vs-delegate table, done criteria, next repo
- `learn/00-onramp.md` + `learn/_answers/00-onramp.md`: 8 warm-ups (bad-cookie trace, span-drop trace, composite FK schema, index↔query matching table, empty-tenant output, "are these duplicates?", a characterization test of `localSpanExporter`, verifying a sealed answer)
- `learn/01-agentic-practice.md` + `learn/_answers/01-agentic-practice.md`: 4 drills (A J1 indexes, B M1 OR query, C INC-002 fix, D INC-001 keyset) + a verification checklist citing `src/server/migrations.ts:10,22-23`, `observability.ts:7-10`, `006:1-7`, `identity.ts:108-119`, `http.ts:35`, `billing.ts:14`
- **Gap fill** (this pack had 2 incidents and no ladder): `training/ladder/J1-finance-composite-indexes.md`, `training/ladder/M1-audit-or-query.md`,
  sealed `training/_answers/ladder/J1.md`, `M1.md`. They turn the review's two P1 findings into fix tickets.

## New findings surfaced while writing (all reasoned, not run)
1. **Errata in the B03 sealed answer** `training/_answers/explain-journal.md` Q2. It says `work_order_tasks` has no `(organization_id, work_order_id)` index,
   but `PRIMARY KEY(organization_id,work_order_id,task_key)` (`002:42`) covers it, so its proposed index is redundant. It also calls
   `work_orders_tenant_status(organization_id,status,created_at DESC)` usable for an `ORDER BY created_at` with no status filter. In PG17 it serves the filter only.
   Also, `_answers/review.md` lists 4 tables missing the pattern. `incidents` (hub.ts:37), `purchase_requests` (hub.ts:52) and others are missing it too.
   I **didn't edit** the B03 answers (no rewriting of training/). The corrections live in on-ramp exercise 8 + its sealed answer, as a verify-the-answer-key drill.
2. **The `check_journal_balance()` trigger** (`005:68`) runs `SELECT … FROM journal_lines WHERE entry_id=…` per inserted row with no index on `entry_id`,
   so it seq-scans all tenants' journal lines on every journal insert. Documented in J1's sealed answer (bonus question). Not fixed.
3. `queries.ts:28` and `agent-tools.ts:61` are **not** identical (DESC+id/LIMIT 100 vs ASC/LIMIT 80, different projections). A naive agent de-dup
   changes behaviour. Used in on-ramp 6 and M1.
4. The migration runner wraps all files in one transaction (`migrations.ts:10`), so `CREATE INDEX CONCURRENTLY` can't work here. This is the J1 trap.

## Skipped / UNVERIFIED
- Docs-only: nothing installed, built, or run. `node_modules` is **absent**, so `npm ci` is needed before `npm test` and on-ramp 7.
- Docker is down (WSL distro gone). Every `EXPLAIN`, `db:migrate` and `test:integration` step is marked **[Docker] requires Docker, currently down**, and each session has a no-Docker path.
- The on-ramp 7 reference test, the J1/M1 reference SQL, and the partial-index implication claim in M1 were not executed.
- No new incident branches (per brief).

## Study route (3 lines)
1. Read a request end to end (`http.ts` → `identity.ts` → `queries.ts`), then 8 on-ramp warm-ups, including a first unit test of the span exporter (no DB).
2. Blind review → EXPLAIN journal (predict first; catch the errata) → INC-001 (OFFSET + missing index) → INC-002 (spans of 401/403s dropped).
3. Direct an agent through J1/M1/INC-002/INC-001 fixes with a hand-written spec and the checklist, then the interview kit. Next: **atlas** (SQL at EF scale → SQL Server), alt **aaa1** (RLS).
