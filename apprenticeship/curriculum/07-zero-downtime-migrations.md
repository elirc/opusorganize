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

**Where these repos live now** (checked 2026-10-06):

| Name in this page | GitHub repo | HEAD |
|---|---|---|
| gitjira-app | **elirc/gitjira** (app code + `training/`) | `42abd2c` |
| netdrop | **elirc/dotnet-drop** | `d7ae725` |
| netintercom | **elirc/dotnet-intercom** | `74e0a28` |
| atlas | code at **elirc/atlas** (`19e8c2d`, no `training/`); `training/` and identical code at **elirc/gitvg** `atlas/` | `af91bab` |

None of the `training/incidents/*` **branches** for gitjira or atlas were pushed. The briefs are on GitHub, and the buggy diffs are inside them, so you recreate each branch by hand (see `elirc/gitjira: training/incidents/README.md`).

**Worked examples in your repos**
- gitjira-app (`elirc/gitjira`):
  - `training/incidents/003-deploy-story-points`: 4 minutes of 5xx, then data gone. At B02 (2026-09-23) the agent verified the committed SQL was DROP + ADD via `prisma migrate diff` on the local branch. That branch was never pushed; the diff is reproduced in the brief.
  - `training/ladder/S2-labels-expand-contract.md`: expand/contract of labels on 2M rows (the brief says 2.1M issues).
- netdrop (`elirc/dotnet-drop`): `training/ladder/S2-zero-downtime-migration.md`, which starts by *adopting* EF migrations. The schema still comes only from `EnsureCreatedAsync` (`src/NetDropbox.Infrastructure/Persistence/DbSeeder.cs:14`, called only in Development at `src/NetDropbox.Api/Program.cs:81-86`), and there is no `Migrations/` folder at HEAD.
- atlas (`elirc/gitvg: atlas/`):
  - `training/incidents/004-canary-rollback`: the old revision fails after the migration.
  - `training/ladder/M1-cost-report-at-1m-payslips.md`: online covering index (`CONCURRENTLY` / `ONLINE = ON`, deliverable 2).
- netintercom (`elirc/dotnet-intercom`): curriculum need "adopting EF migrations on an `EnsureCreated` database". At HEAD, `src/NetIntercom.Api/Program.cs:150-157` calls `MigrateAsync` only if the assembly has migrations, otherwise `EnsureCreatedAsync`, and there is no `Migrations/` folder. So the live path is `EnsureCreated`, which never alters an existing database (the repo's own `training/agentic/VERIFY_AI_OUTPUT.md:31` says so).

Interview framing: "every migration must be compatible with the currently running version *and* the one you might roll back to."

## Worked trace: how gitjira deploys a schema change

All references are to `elirc/gitjira` at `42abd2c`.

**1. Where migrations run.**
- `fly.toml:22-25` sets `release_command = "npm run db:deploy -w @gitjira/api"`, and `db:deploy` is `prisma migrate deploy` (`apps/api/package.json:11`).
- The comment at `fly.toml:16-21` gets the *runner* right: migrations run once, on a throwaway machine, before any new instance serves, and a failure aborts the deploy.
- `fly.toml:35` keeps `min_machines_running = 2`, so a rolling update always has at least one **old** machine serving after the migration has already run.

**2. What the old code expects.**
- `Issue.storyPoints Int?` (`apps/api/prisma/schema.prisma:165`) is selected by the services.
- The shared Zod schema accepts `storyPoints` (`packages/shared/src/issue-schemas.js:30`) inside `issueFields` (`:22`). `updateIssueSchema` is `z.object(issueFields).partial()` (`:42-45`).

**3. What the suspect PR does** (from the INC-003 brief): it renames the field to `estimate` everywhere and commits Prisma's generated SQL, `ALTER TABLE "Issue" DROP COLUMN "storyPoints", ADD COLUMN "estimate" INTEGER;`.

### The failure mode, step by step
1. **14:01:31** — `release_command` drops `storyPoints` and its data, then adds an empty `estimate`. The data loss happens *here*, before any new code runs. "Release phase first" made it worse, because it guaranteed old code would meet the new schema.
2. **14:01:40–14:07** — the old v1.2.4 machines still `SELECT "storyPoints"`. Prisma throws "column `Issue.storyPoints` does not exist", which shows up as 5xx on the issue-list and sprint-report routes.
3. **After 14:07**, every machine runs v1.3.0. But browsers still hold the old SPA bundle and keep PATCHing `{ storyPoints: 3 }`. The new `updateIssueSchema` no longer knows that key. A plain `z.object()` **strips** unknown keys by default (no `.strict()` here), so the request returns 200 and saves nothing: "I set points and they didn't save."
4. **Why CI was green:** the API tests build a fresh database with `npx prisma migrate deploy` (`apps/api/test/global-setup.js:25`). A fresh database has no rows to lose and no old code running against it.

**The safe version** (what INC-003 task 5 asks for): keep the column and map the field with Prisma `@map("storyPoints")`. Then no SQL changes at all. Or, if the database name truly must change, add `estimate` → dual-write → backfill → switch reads → stop writing → drop, with each step as its own release.

## Two senior findings (verified at HEAD)

**A. The ADR's worked example is not what the repo did.**
- ADR 0031 (`docs/adr/0031-expand-contract-migrations.md`) uses "renaming `Issue.position`'s type" as its worked example: add `position_v2`, dual-write, backfill, switch, drop.
- The actual migration `apps/api/prisma/migrations/20260709194359_issue_position_fractional/migration.sql` is a single in-place `ALTER COLUMN "position" SET DATA TYPE TEXT`. `Issue.position` was created as `DOUBLE PRECISION` in `20260709191134_issues_and_columns/migration.sql`. On Postgres, a `double precision → text` type change rewrites the table under an `ACCESS EXCLUSIVE` lock.
- It was harmless on an empty early-sprint database. Still, the document and the history disagree, and S2's "Explain before touching" Q4 asks you to notice exactly this.
- The training README says it directly: "ADR 0031 describes expand/contract, but no migration in the history follows it."

**B. The perf indexes would lock writes on a big table.**
- `apps/api/prisma/migrations/20260710000000_perf_indexes/migration.sql:3` is a plain `CREATE INDEX "Issue_projectId_createdAt_id_idx" ON "Issue"(…)`.
- A non-concurrent build blocks `INSERT`/`UPDATE`/`DELETE` on `Issue` for the whole build. S2 caps that at about 1 s, with 400 writes/s at peak.
- The S2 brief also tells you to *verify on a scratch DB* how Prisma runs a multi-statement migration file before you rely on `CONCURRENTLY`. Do that; don't take this page's word for it.

**Atlas, the same bug in EF:**
- `PayslipLineConfiguration` (`elirc/atlas: src/Atlas.Infrastructure/Persistence/Configurations/PayrollConfigurations.cs:136-160`) leaves `Label`/`Kind` PascalCase (`:145-146`) while `amount`/`currency` are snake_case (`:150-153`). The original migration created them that way (`…/Migrations/20260715154019_AddPayroll.cs:82-83`). That inconsistency is exactly what INC-004's "mapping-only" PR "tidies".
- `Atlas.Api migrate` maps to `MigrateAsync` on Npgsql but **`EnsureCreatedAsync` otherwise** (`src/Atlas.Api/Composition/StartupTasks.cs:26-38`).
- The test factory uses `EnsureCreated()` (`tests/Atlas.Api.Tests/Infrastructure/AtlasApiFactory.cs:52`), and `.github/workflows/ci.yml` has no migration step. The 922 tests can never see a migration-vs-old-binary mismatch.

## Goal + Check ladder

**Goal:** for any schema change, produce the compatibility matrix (old binary × new schema, new binary × old schema), and a release plan where every cell is green.

1. **Junior: read the runner.** Open `fly.toml` and `apps/api/package.json`. **Check:** you can say when `prisma migrate deploy` runs relative to the first new machine, and why `min_machines_running = 2` means old code *will* meet the new schema.
2. **Junior: read the SQL, not the diff.** For INC-003, recreate the branch per `training/incidents/README.md`, then *run locally* `npx prisma migrate diff --from-schema-datamodel <old> --to-schema-datamodel <new> --script`. **Expected:** `DROP COLUMN "storyPoints", ADD COLUMN "estimate"` (B02 got exactly this). Then retry with `@map("storyPoints")`. **Expected:** an empty diff.
3. **Mid: the client-side half.** Explain step 3 of the failure using `issue-schemas.js:22-45`. **Check:** you can name the one-word Zod change that would have turned the silent loss into a loud 400 (`.strict()`), and the cost of that change during an N−1 window.
4. **Mid: atlas INC-004 matrix.** Using `PayrollConfigurations.cs:145-146` and the brief's exceptions, fill the 2×2 matrix for r42/r43 × old/new schema. **Check:** your matrix explains all three observations: r42 broke first, the canary had zero errors, and the rollback raised errors to 40%.
5. **Senior: S2 on paper.** Write the release table for labels → `Label`/`IssueLabel`. **Check:** every DDL statement lists its lock level; the index step uses `CONCURRENTLY` (verified against Prisma's runner on a scratch DB); the contract step has a query that proves nothing reads `Issue.labels`; and the plan answers ADR 0031 vs `20260709194359`.

## Debugging scenario: "we added a column and production doesn't have it"

**Setup (netintercom).** A teammate adds `.HasIndex(c => c.LastMessageAtUtc)` plus a new nullable column to the EF model. Locally everything works: they deleted their dev database, and `EnsureCreatedAsync` rebuilt it from the model. After deploy, the API throws `column … does not exist` on the inbox list.

**Diagnosis:**
1. Read `src/NetIntercom.Api/Program.cs:150-157`. `GetMigrations()` is empty (there is no `Migrations/` folder), so production takes the `EnsureCreatedAsync` branch.
2. That call is a no-op when the database already exists. The new column was never created anywhere except on databases built from scratch.
3. Any test that starts from an empty database passes too. Check how this repo's integration tests build their schema before you trust a green run; I did not verify that for this page.

**Fix:**
1. Introduce migrations with a **baseline**: generate an initial migration, then insert its id into `__EFMigrationsHistory` on the existing database instead of running it.
2. Ship the column as an expand step (nullable).
3. Build the index online.

This is the same "Baseline" deliverable as `elirc/dotnet-drop: training/ladder/S2-zero-downtime-migration.md` (item 1), and netintercom's `training/interview/PROJECT_STORIES.md:21` tells it as an interview story.
