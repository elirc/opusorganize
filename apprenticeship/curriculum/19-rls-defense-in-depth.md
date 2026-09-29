# 19 — Database-enforced isolation: RLS and tenant-safe keys as defense in depth

**Why.** App-level "scope every query by tenant" (saturated in this curriculum) fails the day someone writes a raw query, a new endpoint,
or a background job that forgets the filter. Defense in depth makes the **database** refuse cross-tenant access even when the app is wrong.

**Layer 1: tenant-safe keys.** Use compound foreign keys `(tenant_id, id)`. A row can only reference rows in the same tenant, so the DB rejects cross-tenant writes even if the service layer is bypassed.

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

**Worked examples in your repos**
- grokbuildmultitenantproject:
  - INC-001 (cross-tenant assignee) and INC-002 (a reporting endpoint bypasses the Prisma tenant extension).
  - The PG18 probe was run for real: the superuser bypasses RLS even with FORCE; no context gives 0 rows; `WITH CHECK` blocks a cross-tenant insert; a transaction-local `set_config` doesn't leak, but a session-level `SET` does, and a DELETE on the leaked connection removed another tenant's row.
- HNJOBTRACK:
  - `training/lab/rls/rls_lab.py` probes P1–P11.
  - Real findings on main: `hn_threads` and `job_listings` have **no RLS**, so the anon key can UPDATE listings (rewrite `apply_url`) and INSERT threads. `user_preferences` has no DELETE policy. All user data is read through the service role.
  - The reference migration blocks P7/P8 (42501).
  - INC-004: a user-scoped client shared across requests leaked other users' saved jobs in 20/40 concurrent requests.
- **aaa1** (the main RLS lab):
  - Base branch `training/base/rls-foundation` is "phase 1 of an RLS rollout": a least-privilege app role, one policy per tenant table, and a `withTenant()` wrapper that pins role and tenant inside one transaction. It also includes a two-tenant seed, a canary over every tenant table, and probes.
  - Incidents:
    - 001: a "perf" fast path leaves pooled connections on the restricted role with a stale tenant, so 89/240 lead lists come back empty.
    - 002: the worker connects as the restricted role, so imports sit in QUEUED forever while ticks look healthy.
    - 003: a new table ships without a policy, and confidential notes leak across tenants (the canary catches it).
    - 004: two individually harmless commits combine so a retention purge deletes another tenant's deals, including one under legal hold.
    - 005: a noisy neighbour, where one tenant's big import pushes others' p50 from 352 to 1,820 ms ([14](14-load-backpressure-timeouts.md)).
