# 07 — Zero-downtime schema changes (expand / contract)

**Problem.** During a rolling deploy, old and new app versions run **at the same time** against **one** database. A migration that renames or drops
a column breaks whichever version doesn't expect it. The result is a burst of 5xx errors, or silent data loss when the old code writes a column the new code no longer reads.

**The sequence** (each step is its own deploy)
1. **Expand:** add the new column/table as nullable or defaulted. The old code ignores it.
2. **Dual-write:** the new code writes both old and new; reads stay on the old.
3. **Backfill** in batches from a job (not inside the migration transaction): throttled, resumable, idempotent.
4. **Switch reads** to the new column, behind a flag if possible.
5. **Stop writing the old column**, and wait one full release so rollback stays safe (N-1 compatibility).
6. **Contract:** drop the old column.

**Hazards that ORMs hide**
- Prisma/EF generate `DROP + ADD` for a rename. Always read the generated SQL (`prisma migrate diff`, `dotnet ef migrations script`).
- Index builds lock writes unless you run `CREATE INDEX CONCURRENTLY` (Postgres) or `ONLINE = ON` (SQL Server). These can't run inside a transaction.
- `NOT NULL` on a big table needs a default or a validated `CHECK` first.
- The migration runner must run **before** new pods start, and must be safe to re-run.

**Worked examples in your repos**
- gitjira-app:
  - `training/incidents/003-deploy-story-points`: 4 minutes of 5xx, then data gone. The committed SQL was verified to be DROP + ADD via `prisma migrate diff`.
  - `training/ladder/S2`: expand/contract of labels on 2M rows.
- netdrop: `training/ladder/S2-zero-downtime-migration.md`.
- atlas:
  - `training/incidents/004-canary-rollback`: the old revision fails after the migration.
  - `training/ladder/M1`: online covering index.
- netintercom: curriculum need "adopting EF migrations on an `EnsureCreated` database".

Interview framing: "every migration must be compatible with the currently running version *and* the one you might roll back to."
