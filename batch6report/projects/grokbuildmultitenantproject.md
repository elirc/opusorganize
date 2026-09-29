# B06: grokbuildmultitenantproject (DRILL)

Repo: `C:\Users\Owner\Desktop\grokbuildmultitenantproject` (own `.git`, remote not touched, never pushed)

## Base branch: it contains the user's uncommitted work
`main` HEAD `41a9785` is the original Grok starter. The working tree holds a large **uncommitted** hardening rewrite:
28 modified tracked files plus untracked `app.ts`, `auth.ts`, `errors.ts`, `validation.ts`, migrations, `scripts/` and more
(92 files, +12.3k lines against HEAD). Per the brief, incidents are built on **`training/base/working-tree-snapshot` (`06d0205`)**.
That branch was made in a scratch worktree from a read-only copy of the main tree's tracked plus untracked, non-ignored files.
**That branch therefore contains the user's uncommitted work.** In the main tree, nothing was staged, stashed, reset or
checked out, apart from the single pathspec commit `cb03e05 training: add B06 apprenticeship materials -- training`.
Afterwards the user's 48 dirty/untracked entries are still in place. Both worktrees have been removed. `git worktree list` shows only main.

## Created (`training/`, commit `cb03e05`)
- `README.md`: index, order, about 7 h.
- `review/EXERCISE.md`, `review/COMPARE.md`, `_answers/review.md`: a blind review of the hardened tree. The model review has 4 High, 9 Medium and 6 Low findings plus "done well", with AI smells flagged.
- `review/LEGACY_DIFF_REVIEW.md` and `_answers/legacy-diff-review.md`: an extra legacy-rescue drill, starter (`main`) vs the uncommitted rewrite. It covers what was fixed (16 items, each with mechanism and proof), claims vs reality, and what was missed. The key trap: `git diff` hides the untracked auth, errors and migrations files.
- `incidents/001-task-assignee.md` and `_answers/001-task-assignee.md`
- `incidents/002-status-report.md` and `_answers/002-status-report.md` (includes the RLS backstop design)
- `interview/PROJECT_STORIES.md` (4 STAR skeletons), `interview/TECHNICAL_QUESTIONS.md` (10 questions) and `_answers/technical-questions.md`

## Incident branches (based on `training/base/working-tree-snapshot`)
| Branch | Commit | Symptom (not the cause) |
|---|---|---|
| `training/incidents/001-task-assignee` | `d2e350b` | SEV-2: a customer sees a stranger's name and email as the assignee on their task. CI was green |
| `training/incidents/002-status-report` | `b68c247` | SEV-1: a contractor removed from one org could read another tenant's project names on a new dashboard endpoint |

## Verification (all on native PostgreSQL 18, a throwaway cluster via the repo's `scripts/test-database.mjs`, no Docker)
- Base (`06d0205`): backend and frontend suites, seed and seed-repeat all **PASS**.
- INC-001 bug plus the sealed regression test: **42 pass / 2 fail**, and they are exactly the intended ones (API cross-tenant assign → 201 instead of 400; a raw-SQL insert bypassing the repo is accepted by the DB).
- INC-001 fix plus INC-002 bug plus both regression tests: 44/2. INC-001's regressions all pass and INC-002's regression fails (200 instead of 403), as intended. This run also caught that the INC-001 fix **breaks the PR's own test** (404→400, and the assignee shape becomes nested). The sealed answer now discusses that contract change explicitly.
- Both fixes applied (PR test updated): **46/46 pass**, including the migrate, seed and seed-repeat steps.
- RLS probe (`psql` on PG18 against the migrated schema): the superuser bypasses RLS even with FORCE. With no tenant set, the app role sees 0 rows. A transaction-local `set_config` scopes correctly. WITH CHECK rejects a cross-tenant insert. The setting is gone after the transaction. A session-level `SET` leaks, and a `DELETE` on the leaked connection removed the other tenant's row. A fresh connection's reset deletes 0 rows. All confirmed. (While writing this up I found that the earlier probe script misreported its final step. It has been fixed and re-run, and the answer text was updated.)
- The frontend was not re-run for the incidents (they are backend-only). The Playwright browser tests were not run.

## Issues found in the project
- **Presented as working but isn't (on `main`, the Grok starter):** README and UI copy say "strictly isolated", but the tenant was whatever `x-org-id` said, with a silent `'demo-org'` default. There was no authentication at all, even though `jsonwebtoken` was a dependency. The frontend sent `?orgId=` while the server read a header, so every request fell back to the default tenant. The frontend test rendered `useQuery` without a provider and had no runner. The backend tests were tautological mocks.
- **Hardened rewrite (uncommitted):** isolation is app-level only. `docker-compose.yml` and `backend/.env.example` make the runtime role the `POSTGRES_USER` superuser, so any future RLS would be bypassed. Only `Task→Project` is tenant-safe in the DB. The login limiter is keyed on `req.ip` with no `trust proxy`. P2003 is mapped to a misleading 409. Security-relevant 403s aren't logged. There is deep OFFSET plus `count(*)`. `tenantContext.test.ts` has tests that can't fail. `astraupskill/VERIFICATION.md` cites run folders that don't exist.
- **Secrets:** none committed. `backend/.env` is gitignored, and `backend/.env.example` has placeholders only. The starter's `docker-compose.yml` on `main` uses default DB credentials on `0.0.0.0:5432` (location only).

## Skill links (for COMPETENCY_GRAPH)
- authn/authz/multi-tenancy, **DB-enforced isolation**: `_answers/review.md` H1–H3; INC-001 (compound FK to `OrganizationMember`, a bypass-the-repo test); INC-002 (RLS backstop: non-superuser role, `set_config(...,true)`, FORCE, fail-closed); TECHNICAL_QUESTIONS 1–7
- data modeling/migrations: INC-001 repair-then-constrain migration, `NOT VALID`/`VALIDATE`, Prisma compound-FK `SetNull` limitation; Q1–Q3
- code review / legacy rescue / reviewing AI output: `review/LEGACY_DIFF_REVIEW.md`, `review/EXERCISE.md` (tautological tests, docs-vs-code)
- performance / noisy neighbours: review M5–M7; Q10
- security (OWASP): limiter/`trust proxy` (H4, Q9); error-message oracles (Q8)
- observability: review M1–M2; INC-002's 403→200 log correlation and its follow-up alert
- testing: bypass-the-repository regression tests; tests that can't fail (L1)

## Curriculum needs (one central page each, not written)
- **Postgres RLS as defense in depth:** owner vs runtime role, why superusers and BYPASSRLS skip policies, FORCE, `current_setting(...,true)` fail-closed, transaction-local `set_config` with pooled connections (Prisma/PgBouncer), what breaks (migrations, seeds, test resets), and the cost. B06's thin skill has no page yet.
- **Tenant-safe relations:** compound FKs `(child_id, org_id) → parent(id, org_id)`, the needed `UNIQUE(id, org_id)`, and a schema lint for relations missing `organizationId`. This could be a section of the RLS page.

## Existing learning-doc trees
- `astraupskill/` (7 docs plus evidence, Astra-generated walkthrough of the rewrite): **KEEP**, linked as context. Caveat: `VERIFICATION.md` cites evidence folders that aren't present (review L4). It is also untracked.
- `dfableandopus/` (interview questions, stories, code-reading drill, take-home, system design, flashcards): **KEEP**. The new `PROJECT_STORIES.md` deliberately avoids its "trusted header → membership" story. Parts of its code-reading drill could be converted to exercises later.

## Caveats
- The scratchpad still holds a copy of the repo used for the verification runs (`scratchpad/grokmt/verify`, including `node_modules`, installed with npm workspaces) and an 40 MB throwaway PG cluster (`scratchpad/grokmt/rlspg`, stopped). Both are outside any repo. Per the no-recursive-delete rule I didn't delete them. The orchestrator can remove them with the junction-safe script if space is needed.
- The first INC-001 verification attempt died when the disk filled. It was re-run after the space was freed.
- The DRILL tier was delivered with one extra exercise (the legacy diff review), because the starter-vs-rewrite gap is the repo's most distinctive lesson.
