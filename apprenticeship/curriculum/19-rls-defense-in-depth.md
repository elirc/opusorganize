# 19 — Database-enforced isolation: RLS and tenant-safe keys as defense in depth

**Why.** App-level "scope every query by tenant" (saturated in this curriculum) fails the day someone writes a raw query, a new endpoint,
or a background job that forgets the filter. Defense in depth makes the **database** refuse cross-tenant access even when the app is wrong.

**Layer 1: tenant-safe keys.** Use compound foreign keys `(tenant_id, id)`. A row can only reference rows in the same tenant, so the DB rejects cross-tenant writes even if the service layer is bypassed.
The parent needs `UNIQUE (id, tenant_id)` for the FK to point at. FKs constrain **writes** only. They do nothing to stop a *read* of another tenant's rows.

**Layer 2: Postgres Row-Level Security.**
- `ALTER TABLE … ENABLE ROW LEVEL SECURITY`, plus **`FORCE`** so the table owner is also subject to it.
  **Superusers still bypass RLS even with FORCE**, so the app must never connect as a superuser.
- Policies use `USING` for reads, updates and deletes, and `WITH CHECK` for inserts and updates. Forgetting `WITH CHECK` allows cross-tenant *inserts*. Forgetting a DELETE policy leaves owners unable to delete their own rows.
- The tenant or user context comes from `current_setting('app.tenant_id', true)` or, in Supabase, `auth.uid()`. With no context set, the app role should see **0 rows** (fail closed).
- **Pooled connections:** set the context **transaction-locally** with `set_config('app.tenant_id', $1, true)` inside the transaction.
  A session-level `SET` survives on the pooled connection, and the *next* request (another tenant) inherits it.
- Migrations and admin jobs use a separate bypass role. Never use that role in request paths.

**Supabase specifics:** the **anon key** reads and writes whatever the RLS policies allow on any table exposed via PostgREST, so a table without RLS is world-writable.
The **service-role key** bypasses RLS entirely. Using it for user-scoped reads throws away the backstop.

**Two sentences to say in an interview.** RLS is a backstop against a **forgotten `WHERE`**, not against **choosing the wrong tenant**:
if the tenant value fed to `set_config` came from an unverified header, RLS faithfully shows the wrong tenant's rows. Keep both walls, because each one hides the other's failures.

**Where these repos live now (checked 2026-10-06).** grokbuildmultitenantproject → `elirc/grok-build-multitenant` (main `e899e20`) ·
HNJOBTRACK → `elirc/hnjobtrack` (main `a9d1080`) · aaa1 → `elirc/aaa1` (main `8c27024`).
In all three, **only `main` is on GitHub**: the lab base branches and every `training/incidents/00N-*` branch named below exist only in the original local workspaces (`git ls-remote` shows `refs/heads/main` alone).
The incident *briefs* and sealed `_answers/` are on main; the runnable bug-seeded code is not. aaa1's own `training/README.md:6-11` says so.

## Worked examples in your repos

- grokbuildmultitenantproject:
  - INC-001 (cross-tenant assignee: the PR added an assignee with a single-column FK, so a stranger from another org could be assigned) and INC-002 (a new `/api/reports` router was mounted **without** the `attachTenantContext` middleware and read the tenant straight from the `x-org-id` header).
    *Correction 2026-10-06:* earlier versions of this page said INC-002 "bypasses the Prisma tenant extension". The sealed answer (`elirc/grok-build-multitenant: training/_answers/002-status-report.md:5-11`) says it is a missing middleware mount that trusts the header; there is no Prisma tenant extension in the code.
  - The PG18 probe was run for real (B06, 2026-09-24, recorded in `batch6report/projects/grokbuildmultitenantproject.md`; the probe script lived in a scratch folder and is **not** in the repo): the superuser bypasses RLS even with FORCE; no context gives 0 rows; `WITH CHECK` blocks a cross-tenant insert; a transaction-local `set_config` doesn't leak, but a session-level `SET` does, and a DELETE on the leaked connection removed another tenant's row.
  - *History:* at B06 (2026-09-24) main was the Grok starter `41a9785` and the hardened rewrite was uncommitted. It was committed to main on 2026-09-30 (`57a8028`, "Sync local changes to GitHub"), so the code traced below is now on main. `training/README.md` still describes the old state.
- HNJOBTRACK:
  - `training/lab/rls/rls_lab.py` probes P1–P11 (`rls_lab.py:37-47`).
  - Real findings on main (still true at `a9d1080`): `hn_threads` and `job_listings` have **no RLS**, so the anon key can UPDATE listings (rewrite `apply_url`) and INSERT threads. `user_preferences` has no DELETE policy. All user data is read through the service role.
  - The reference migration blocks P7/P8 (42501): `training/_answers/ladder/mid-03-lock-down-public-tables.sql`.
  - INC-004: a user-scoped client shared across requests leaked other users' saved jobs in 20/40 concurrent requests.
- **aaa1** (the main RLS lab):
  - Base branch `training/base/rls-foundation` is "phase 1 of an RLS rollout": a least-privilege app role, one policy per tenant table, and a `withTenant()` wrapper that pins role and tenant inside one transaction. It also includes a two-tenant seed, a canary over every tenant table, and probes.
    **Not on GitHub as of 2026-10-06**: on `elirc/aaa1` main there is no `src/lib/db/tenantDb.ts`, no `prisma/rls/`, and no `training/lab/rls/` (only `src/lib/db/prisma.ts`). Every file:line below for aaa1 is therefore from **main** (the app-filter wall) or from the incident briefs on main.
  - Incidents:
    - 001: a "perf" fast path leaves pooled connections on the restricted role with a stale tenant, so 89/240 lead lists come back empty.
    - 002: the worker connects as the restricted role, so imports sit in QUEUED forever while ticks look healthy.
    - 003: a new table ships without a policy, and confidential notes leak across tenants (the canary catches it).
    - 004: two individually harmless commits combine so a retention purge deletes another tenant's deals, including one under legal hold.
    - 005: a noisy neighbour, where one tenant's big import pushes others' p50 from 352 to 1,820 ms ([14](14-load-backpressure-timeouts.md)).

## Worked trace: one request through both walls (grok-build-multitenant, main `e899e20`)

This is the cleanest real example of Layer 1 next to an app-level tenant check, and the place to see why Layer 2 is still missing.

1. **Who is the tenant?** `elirc/grok-build-multitenant: backend/src/app.ts:53` mounts `authenticate(secret)` on `/api`, and `app.ts:60` mounts `attachTenantContext` **only** on `/api/projects`.
   The tenant is chosen per router, by where the middleware is mounted. That is the seam INC-002 fell through.
2. **Is the claimed tenant real?** `backend/src/middleware/tenantContext.ts:19` reads `x-org-id` from the header, and `:25-34` looks up `organizationMember` by `(userId, organizationId)`. No row means 403.
   `requireTenant()` (`:45-49`) is the only approved way for a handler to get the tenant. A handler that reads the header itself skips the membership check.
3. **Layer 1 in the schema.** `backend/prisma/schema.prisma:66`: `Task.project` is `@relation(fields: [projectId, organizationId], references: [id, organizationId])`,
   backed by `@@unique([id, organizationId])` on `Project` (`schema.prisma:54`). The generated SQL is `prisma/migrations/202609090001_tenant_workspace/migration.sql:95` (the unique index) and `:113` (the compound FK).
   A task cannot point at another org's project, even through raw SQL.
4. **Where Layer 1 stops.** `OrganizationMember` and `Project` reference `Organization` with single-column FKs (`migration.sql:104-110`), which is fine because those are the tenant roots.
   But any *new* user reference on a tenant table (INC-001's assignee) must be compound against `OrganizationMember (userId, organizationId)`, or the DB happily accepts a stranger.
5. **Layer 2 is absent.** `grep -n "ROW LEVEL" backend/prisma/migrations/*/migration.sql` finds nothing, and `docker-compose.yml:5` sets `POSTGRES_USER: tenant_dev`.
   In the official Postgres image that user is a **superuser**, so even if someone added policies tomorrow, the app connection would bypass them. The INC-002 sealed answer (`_answers/002-status-report.md:56-59`) makes "create a separate `NOSUPERUSER NOBYPASSRLS` app role" step one for exactly this reason.

## Failure mode, step by step: the session-level `SET` on a pooled client (aaa1 INC-001)

Source: `elirc/aaa1: training/incidents/001-tenant-read-fastpath.md` and `training/_answers/incidents/001.md` (both on main; the branch and probe are not).

1. A perf PR replaces the transactional `withTenant` with `withTenantRead`, which runs `SET ROLE` and then `set_config('app.tenant_id', id, false)` as **two separate statements** on the shared Prisma client (brief `:31-37`). The `false` makes the setting session-level.
2. Outside an interactive transaction, Prisma may send each statement on a **different pooled connection** (`_answers/incidents/001.md:3-6`). The settings stick to whichever connection received them.
3. The list query lands on a connection that is either still the owner (RLS off, the app filter is right: `ok`), restricted with *my* tenant (`ok`), or restricted with the **other** tenant.
4. In that last case the policy admits only the other tenant, and `tenantScope()` in the repository (`src/lib/tenant/scope.ts:15-19`, spread into `listLeads` at `src/repositories/leadRepository.ts:24`) admits only mine. The intersection is empty: **200 with zero items**, no error, p95 actually improves.
5. The probe tally is `ok: 150, empty_list: 89, pool_wait: 1` out of 240 (brief `:72`). On the base branch, idle connections read back `role=crm app.tenant_id=""`; on the bug branch they read `role=crm_app` with a stale tenant.
6. The scary corollary (`_answers/incidents/001.md:11-12`): foreign rows never appeared **only because** the app filter was still there. Remove it "because RLS handles it" (that is incident 004) and the same bug becomes a cross-tenant leak.
7. Fix (`:21-24`): back into one transaction with `is_local=true`, or both `set_config` calls in one round trip inside the transaction. Under PgBouncer transaction mode the rule is absolute.

## Goal + **Check** ladder

**Goal:** you can tell, from reading a repo, which isolation walls exist, which role the app connects as, and how tenant context reaches the database.

1. **Junior: find the app wall.** In `elirc/aaa1`, open `src/lib/tenant/scope.ts` and grep `src/repositories` for `tenantScope(`.
   **Check:** `tenantScope` returns `{ tenantId: context.tenantId }` (`scope.ts:18`), and every repository spreads it. Then open `src/repositories/importRepository.ts:84-89`: `listQueuedImportJobs` has **no** tenant filter. Explain why that is correct for a dispatcher and why it is exactly the query that INC-002 broke under RLS.
2. **Junior: find a missing tenant-safe key.** In `elirc/aaa1: prisma/schema.prisma`, read the `Lead` model.
   **Check:** `owner` is `@relation("LeadOwner", fields: [ownerId], references: [id])` (`schema.prisma:351`), a single-column FK. The only thing stopping a cross-tenant owner is `resolveAssignableOwner` (`src/services/ownershipService.ts:16-33`), an app-layer membership check. Write the compound-FK version and say what `UNIQUE` it needs first.
3. **Mid: Supabase exposure audit.** In `elirc/hnjobtrack: supabase/schema.sql`, list every `create table` and every `enable row level security`.
   **Check:** six tables (`:14, 51, 79, 94, 144, 173`), RLS on four (`:23, 63, 154, 181`). `hn_threads` and `job_listings` have none, so with the public anon key, probes P7/P8 (`training/lab/rls/rls_lab.py:43-44`) succeed. `user_preferences` has select/update/insert policies (`:65-72`) but no delete, which is P5. Compare with the reference fix `_answers/ladder/mid-03-lock-down-public-tables.sql:4-15`.
4. **Mid: role audit.** For each of the three repos, answer "which role does the running app use, and does it bypass RLS?"
   **Check:** grok: `tenant_dev` from `docker-compose.yml:5` and `backend/.env.example:2`, a superuser, so it bypasses. HNJOBTRACK: every API module calls `get_supabase_admin()` (`backend/app/core/supabase.py:4-6`, service-role key; e.g. `backend/app/api/saved.py:18`), so it bypasses, and isolation is the `.eq("user_id", user_id)` at `saved.py:24`. aaa1 main: one Prisma client (`src/lib/db/prisma.ts:18-22`) on whatever `DATABASE_URL` says, with no RLS defined.
5. **Senior: design the rollout.** Read `elirc/aaa1: training/ladder/M1-force-rls.md` (FORCE everywhere, with named exceptions for session lookup, API-token lookup and worker dispatch).
   **Check (run locally, only if you recreate the lab):** after your change, a fresh connection as the app login with no `app.tenant_id` returns 0 rows from every tenant table; the worker still dispatches for both tenants; `pg_class.relforcerowsecurity` is true for every tenant table. Write the exception list before writing SQL.

## Senior findings (verified on main, 2026-10-06)

- **HNJOBTRACK's RLS is decorative for the API.** Policies exist on `saved_jobs` (`supabase/schema.sql:154-166`), but the backend never presents a user identity to Postgres: every route uses the service-role client.
  The only isolation is the app filter. INC-004 (`training/_answers/incidents/004-saved-jobs-user-scoped-rls.md:21-28`) shows the trap in moving to the user-scoped client: a module-level client with a per-request token mutated into it shares identity across requests (20/40 wrong under concurrency), and the PR had also dropped the `.eq("user_id", …)` filters because "RLS enforces ownership now".
  The fix kept both: a per-request client *and* the explicit filters.
- **grok's hardened rewrite has Layer 1 for one relation and no Layer 2.** `Task → Project` is compound (`schema.prisma:66`), but the runtime role is a superuser, the tenant is attached per router (`app.ts:60`), and the header is the input.
  The structural fix in the sealed answer (`_answers/002-status-report.md:45-48`) is to mount `attachTenantContext` once on a tenant sub-router and add a CI grep for `x-org-id` outside `middleware/tenantContext.ts`. Today `grep -rn "x-org-id" backend/src` (excluding tests) hits only that file, so the grep would currently pass.

## Debugging scenario: "the worker is healthy but nothing happens" (aaa1 INC-002)

**Symptom** (`elirc/aaa1: training/incidents/002-worker-least-privilege.md`): after a security release, a 2-row CSV import sits in `QUEUED`. `worker.runs.errors = 0`, and tick p50 dropped from about 4 s to 60 ms. The web app is fine.

1. **Correlate.** The change is in what the worker *sees*, not what it does: fast ticks plus zero counts started at the release.
2. **Read the suspect diff** (brief, the SEC-212 hunk): with `CRM_PROCESS=worker`, Prisma uses `WORKER_DATABASE_URL`, the `crm_app` login.
3. **Compare as two roles.** `SELECT count(*) FROM "ImportJob" WHERE status='QUEUED'` as owner returns 1, and as `crm_app` returns 0 (`_answers/incidents/002.md:12`). That is RLS failing **closed**: the dispatch queries run before any tenant is known, so `"tenantId" = NULL` matches nothing.
4. **Find the blast radius.** Not only imports: exports, the outbox (so workflow rules and webhooks for *every* tenant), webhook retries and reminders all dispatch the same way (`002.md:8-9`).
5. **Fix without reverting least privilege.** Split dispatch from processing: a narrow dispatcher path that may see job ids across tenants, then `withTenant(job.tenantId)` for the work itself (`002.md:14` onward).
6. **Alert you add:** QUEUED age per job type, not error rate. Fail-closed bugs never raise errors.

**Honesty cap.** The aaa1 and grok probe numbers above come from the B06 runs on a native PG18 cluster on 2026-09-24 (`batch6report/`). I did not re-run them on 2026-10-06, and from a fresh GitHub clone you cannot, because the lab and incident branches were never pushed.
The HNJOBTRACK `rls_lab.py` and its reference SQL are on main and runnable locally against a throwaway Postgres; its P5/P7/P8 results here are also from the 2026-09-24 run.
