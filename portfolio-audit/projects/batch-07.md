# Batch 07 — Grok domain builds + JS curricula
Scope: grokbuildecommerceproject, grokbuildhrproject, grokbuildmultitenantproject, grokbuildorderproject, grokbuildppmproject, grokbuildsupportproject, grokbuildteamproject, grokjs, groktuts, JS1, jsharness, JSProjectLearn, JSTut (Base: C:\Users\Owner\Desktop\) | Candidate dirs inspected: 13 | Meaningful projects: 11 | Tiny/empty/boilerplate: 2 (grokbuildsupportproject, jsharness/VTCode)

## Batch-wide note on the "grokbuild*" cluster and origin story

All seven `grokbuild*` directories (ecommerce, hr, multitenant, order, ppm, support, team) share one skeleton and one history:
- Each is a **single git commit** dated `2026-07-18 09:55:xx`, message `"Initial commit: <name> snapshot"` — i.e. a snapshot import of an originally Grok-generated starter app, not organic commit history.
- Every project (except `support`) has **uncommitted working-tree changes** on top of that commit: `backend/`, `frontend/`, `README.md`, `JOURNAL.md`, `PHASE_PLANS.md` etc. carry file mtimes of **2026-09-09** (an app-code fix/rebuild pass), and `astraupskill/` + `dfableandopus/` carry mtimes of **2026-09-18** (or 2026-09-21 for multitenant) — a documentation/review pass added after the code fix. None of this is committed to git; `git status --short` on `grokbuildecommerceproject` shows dozens of modified/untracked paths. This lines up with the user's own memory note about a 2026-09-16→18 "Fable review + fix pass of Astra improvements" across ~153 projects — these are very likely part of that pass.
- READMEs are self-aware about this lineage. Example, `grokbuildmultitenantproject/README.md`: *"The original starter's trusted tenant header and placeholder pages have been replaced with verified membership, project and task CRUD, role checks, version conflicts, and transactional audit history."* `grokbuildecommerceproject/README.md`: *"JOURNAL and PHASE_PLANS remain historical starter notes; this README and the course describe the implemented application."* So what's on disk today is a **repaired/hardened rewrite of an intentionally-flawed Grok starter**, not raw Grok output — treat these as junior→mid CRUD teaching apps with deliberately-seeded-then-fixed defects, not as "old AI slop."
- Standard skeleton per project: `backend/` (Express + TypeScript + Prisma + Postgres + Zod + JWT, layered routes→services→repositories), `frontend/` (React + Vite + Tailwind), `docker-compose.yml`, root `README.md`/`JOURNAL.md`/`PHASE_PLANS.md`, `astraupskill/` (8-file course: codebase map, concepts, worked change, break-it, testing/debugging, practice, solutions, trace lab, + VERIFICATION.md), `dfableandopus/` (6-file interview pack: interview questions, stories/resume, code-reading drill, take-home, system-design follow-ups, flashcards).
- `package.json` descriptions were copy-pasted sloppily: ecommerce, hr, and team backends all say `"description": "Educational HR Platform backend"` verbatim — a real (harmless) old-AI/copy-paste smell, evidence it started from one shared scaffold.
- Depth varies: `ppm` and `support` are noticeably behind the other five (fewer astraupskill/dfableandopus files, `support` has no app code at all).

## Candidates table

| Project | Path | Type | Origin | Stack | Complexity | Docs | Disp |
|---|---|---|---|---|---|---|---|
| grokbuildecommerceproject | Desktop\grokbuildecommerceproject | web app (monorepo: BE+FE) | COURSE/GENERATED (Grok starter, hardened by later fix+review pass) | React/Vite+Express/TS+Prisma+Postgres+Zod+JWT | Junior+/Mid | STRONG (astraupskill 8f + dfableandopus 6f) | B HIGH-VALUE |
| grokbuildhrproject | Desktop\grokbuildhrproject | web app (monorepo: BE+FE) | COURSE/GENERATED | React/Vite+Express/TS+Prisma+Postgres+Zod+JWT | Junior+/Mid | STRONG | B HIGH-VALUE |
| grokbuildmultitenantproject | Desktop\grokbuildmultitenantproject | web app (monorepo: BE+FE) | COURSE/GENERATED | React/Vite+Express/TS+Prisma+Postgres+Zod+JWT | Mid | STRONG | A FLAGSHIP |
| grokbuildorderproject | Desktop\grokbuildorderproject | web app (monorepo: BE+FE) | COURSE/GENERATED | React/Vite+Express/TS+Prisma+Postgres+Zod+JWT | Junior+/Mid | STRONG | B HIGH-VALUE |
| grokbuildppmproject | Desktop\grokbuildppmproject | web app (monorepo: BE+FE) | COURSE/GENERATED | React/Vite+Express/TS+Prisma+Postgres+Zod+JWT | Mid | USEFUL (partial: astraupskill full, dfableandopus only 2 files) | C SPECIALIZED |
| grokbuildsupportproject | Desktop\grokbuildsupportproject | docs-only / skeleton | COURSE/GENERATED (never built) | planned: React+Express+Prisma+Postgres | Tiny | NONE | G ARCHIVE |
| grokbuildteamproject | Desktop\grokbuildteamproject | web app (monorepo: BE+FE) | COURSE/GENERATED | React/Vite+Express/TS+Prisma+Postgres+Zod+JWT | Junior+/Mid | USEFUL (astraupskill only, no dfableandopus) | B HIGH-VALUE |
| grokjs | Desktop\grokjs | curriculum (multi-lang, monorepo of labs) | COURSE/GENERATED | JS/TS/React/Python/C#/.NET | Tutorial→Junior | EXCELLENT (~2,700+ files across 8 sub-labs) | A FLAGSHIP |
| groktuts | Desktop\groktuts | curriculum (4 upskilling labs) | COURSE/GENERATED | JS/TS/React, Python, C#/.NET, SQL/Postgres | Tutorial→Junior/Mid | STRONG (1,047 files, real pytest/xUnit/vitest-graded practice) | B HIGH-VALUE |
| JS1 | Desktop\JS1 | monorepo(~97 exercise apps) | COURSE/GENERATED | mixed: TS/React/Express/Postgres AND C#/.NET console/repository apps | Junior | USEFUL (astraupskill in ~48/97 subprojects) | E EXERCISE SOURCE |
| jsharness/ctvodejs | Desktop\jsharness\ctvodejs | CLI / agent framework (pnpm monorepo) | ORIGINAL (user's own TS port project) | TypeScript, pnpm workspaces, LLM/MCP tooling | Mid/Mid+ | MINIMAL (docs/migration-roadmap.md only) | C SPECIALIZED |
| jsharness/VTCode | Desktop\jsharness\VTCode | CLI coding agent | OPEN-SOURCE CLONE (third-party, not user's work) | Rust | Production-like | N/A (not user's) | G ARCHIVE |
| JSProjectLearn | Desktop\JSProjectLearn | web app / curriculum platform ("SkillForge Quest") | ORIGINAL app wrapping COURSE/GENERATED content | React 19+TS+Vite, vitest, playwright | Mid | EXCELLENT (334 missions / 329 playable + 5 reference, gamified spaced-repetition) | A FLAGSHIP |
| JSTut | Desktop\JSTut | curriculum (39 markdown files, flat) | COURSE/GENERATED | JS/TS/React/C#/.NET/SQL fundamentals→advanced→interview prep | Tutorial→Mid | EXCELLENT (15,650 lines, genuinely differentiated, non-templated) | B HIGH-VALUE |

---

## grokbuildecommerceproject
- Path: `Desktop\grokbuildecommerceproject`            - Origin: COURSE/GENERATED (Grok-built starter, subsequently hardened)
- Type: web app, monolith monorepo (backend + frontend)
- State: working-looking (code + real transactional logic present; not verified to run)      - Size: ~89 files   - Last modified: app code 2026-09-09, docs 2026-09-18 (git commit frozen at 2026-07-18)
- Purpose: "Small Goods commerce workspace" — product CRUD, cart, checkout that server-prices items, reserves stock, snapshots order lines, and stores a durable retry key, all in one DB transaction (`README.md`).
- Stack: FE React/Vite; BE Express+TypeScript, Prisma 6.19.2, Postgres, Zod validation, JWT (bcryptjs hashing); Test: Jest + Supertest (unit + integration); Infra: docker-compose (Postgres)
- Architecture: layered modular monolith — `routes → controllers → services → repositories`, plus `lib/domain.ts`, `lib/errors.ts`
- Complexity: Junior+ / Mid — optimistic-locking `version` fields on `Product`, `AuditEvent` model, idempotency via `requestId`, transactional stock reservation
- Educational material: STRONG — `astraupskill/` (01-07 + VERIFICATION.md, 376 lines) is a full codebase-map→concepts→worked-change→practice→solutions→trace-lab course; `dfableandopus/` (570 lines) is a matching interview-prep pack (questions, resume stories, code-reading drill, take-home, system-design follow-ups, flashcards). Project-specific, not generic — preserve as-is.
- Quality observations:
  - `backend/src/__tests__/workflow.integration.test.ts` exercises a real failure path: it dynamically creates a Postgres trigger that raises an exception to test that internal DB errors aren't leaked to the client (`auditFailure()` helper) — this is senior-flavored defensive testing, not shallow happy-path-only coverage.
  - `prisma/schema.prisma` models `Order`/`Product` with `Decimal` money types, `@@index([active,createdAt,id])`, `version Int @default(1)` for optimistic concurrency.
  - `.env.example` uses placeholder secrets (`replace-with-a-generated-secret-of-at-least-32-bytes`) — no real secrets committed.
  - `package.json` description field literally says `"Educational HR Platform backend"` — copy-paste leftover from the shared scaffold (harmless but sloppy).
  - No committed git history beyond the single snapshot commit — all fix/review work is uncommitted on disk.
- Old-AI-generated smells: copy-pasted `package.json` description (see above); otherwise none seen — the transaction handling, optimistic locking, and negative-path test are above typical old-AI-generated quality, consistent with this being the *post-fix* state.
- Skill tags: fe-react, be-node-express, be-validation, be-error-handling, db-postgres, db-transactions, db-concurrency, orm, test-integration, test-unit, docker, authn, crud-basic
- Duplicate/overlap: part of the grokbuild* cluster (shared skeleton + astraupskill + dfableandopus pattern); domain (commerce) is unique in this batch.
- Learning value: High — real transactional/idempotency patterns plus a matched course + interview pack.
- Transformation opportunity: Package as a "junior→mid CRUD with transactions" portfolio sample; the audit-log/idempotent-checkout pattern is a strong take-home/interview demo as-is.
- Interview stories: "How I designed idempotent checkout with a durable retry key and DB-transaction stock reservation"; "How I hid internal DB errors from API responses while preserving audit trail."
- Proposed disposition: B HIGH-VALUE — solid mid-level CRUD+transactions sample with a matched course/interview pack; not flagship because domain (basic commerce CRUD) is common and it's one of several siblings.

## grokbuildhrproject
- Path: `Desktop\grokbuildhrproject`            - Origin: COURSE/GENERATED
- Type: web app, monolith monorepo (backend + frontend)
- State: working-looking      - Size: ~93 files   - Last modified: app code 2026-09-09, docs ~2026-09-18
- Purpose: "People & Leave Workspace" — employee CRUD plus a leave-request workflow with role/scope checks, overlap prevention, and reporting-line protection (`README.md`).
- Stack: FE React/Vite; BE Express+TS, Prisma 6.19.2, Postgres, Zod, JWT/bcryptjs; Test: Jest+Supertest; docker-compose
- Architecture: layered monolith — `repositories/{departmentRepository,employeeRepository,leaveRepository,scope}.ts`, `services/{employeeService,leaveService}.ts`
- Complexity: Junior+/Mid — `repositories/scope.ts` implies row-level access scoping (manager can only see their reports), a common real-world authz pattern.
- Educational material: STRONG — astraupskill (300 lines across 8 files) + dfableandopus (561 lines, 6 files), same structure as ecommerce, project-specific.
- Quality observations:
  - Dedicated `scope.ts` repository suggests deliberate row-level authorization design rather than blanket admin/user checks.
  - `__tests__/leaveService.test.ts` + `workflow.integration.test.ts` present (not deep-read line by line, but naming indicates behavior coverage of the leave workflow specifically, matching the README's "overlapping active requests" and "protects reporting relationships" claims).
  - Same copy-pasted `"description": "Educational HR Platform backend"` (this is the project it was presumably copied *from*).
  - README explicitly frames this as "the repaired application" — confirms fix-pass lineage.
- Old-AI-generated smells: none beyond the shared copy-paste description.
- Skill tags: authz-rbac, be-node-express, be-validation, db-postgres, orm, test-integration, crud-basic
- Duplicate/overlap: grokbuild* cluster; likely the "source" scaffold for the copy-pasted package description in ecommerce/team.
- Learning value: High — the manager-scoped access pattern + leave-overlap business rule are good interview material.
- Interview stories: "Scoping employee/leave visibility to a manager's own reports"; "preventing overlapping leave requests under concurrent writes."
- Proposed disposition: B HIGH-VALUE — same reasoning as ecommerce.

## grokbuildmultitenantproject
- Path: `Desktop\grokbuildmultitenantproject`            - Origin: COURSE/GENERATED
- Type: web app, monolith monorepo (backend + frontend)
- State: working-looking      - Size: ~93 files   - Last modified: app code 2026-09-09, docs 2026-09-21 (most recently touched project in the batch)
- Purpose: "Tenant Workspace" — multi-tenant SaaS CRUD (organizations/projects/tasks) where the README says the original starter's *"trusted tenant header"* (a classic IDOR/spoofable-tenant vuln) was replaced with verified membership checks, role checks, version conflicts, and transactional audit history.
- Stack: FE React/Vite; BE Express+TS, Prisma 6.19.2, Postgres, Zod, JWT; Test: Vitest+Supertest; docker-compose
- Architecture: layered monolith with an explicit `middleware/tenantContext.ts` — the multi-tenancy boundary is centralized rather than scattered per-route.
- Complexity: Mid — this is the only project in the cluster centered on a security defect (trust-the-header tenant isolation) that was found and fixed; `__tests__/tenantContext.test.ts` exists specifically to cover that boundary.
- Educational material: STRONG — astraupskill (286 lines) + dfableandopus (570 lines), 8+6 files.
- Quality observations:
  - `middleware/tenantContext.ts` + a dedicated `tenantContext.test.ts` — deliberate coverage of the tenant-isolation boundary, the highest-stakes bug class for multi-tenant apps.
  - README explicitly narrates the vulnerability that was fixed ("trusted tenant header and placeholder pages have been replaced with verified membership"), which is itself excellent case-study material for an authz-rbac / multitenancy interview story.
  - `__tests__/projectRepository.test.ts` and `projectService.test.ts` split repository-level vs service-level tests — decent separation of concerns in the test suite.
- Old-AI-generated smells: none seen in the current (fixed) state; the *original* starter's trust-the-header design is itself a textbook old-AI/naive-AI security smell, now documented as a fixed defect rather than a live one.
- Skill tags: multitenancy, authz-rbac, security-owasp, be-node-express, db-postgres, db-concurrency, orm, test-unit, test-integration, docker
- Duplicate/overlap: grokbuild* cluster; unique among siblings for centering on a named security vulnerability + fix.
- Learning value: Very High — a concrete, narratable "I found and fixed a broken tenant-isolation vuln" story plus working code and tests to back it.
- Transformation opportunity: This is the strongest interview-story material in the whole grokbuild* cluster — worth a short standalone write-up (before/after diff of the trust-the-header bug) as a portfolio artifact.
- Interview stories: "I audited a multi-tenant app and found tenant isolation relied on a client-supplied header — here's how I replaced it with verified membership and centralized tenant context, plus the regression test I added."
- Proposed disposition: A FLAGSHIP — most recently maintained (2026-09-21), and the only project in the batch with a concrete, well-documented security-vulnerability-fixed narrative backed by real code and a dedicated regression test.

## grokbuildorderproject
- Path: `Desktop\grokbuildorderproject`            - Origin: COURSE/GENERATED
- Type: web app, monolith monorepo (backend + frontend)
- State: working-looking      - Size: ~80 files   - Last modified: app code / docs ~2026-09-18
- Purpose: "Order and inventory learning lab" — product CRUD, paged listings, server-priced order creation, transactional stock reservation, one-time-restore cancellation, fulfillment (`README.md`).
- Stack: FE React/Vite; BE Express+TS, Prisma **^5.15.0** (older major than siblings' 6.19.2 — inconsistent dependency pinning across the cluster), Postgres, Zod, JWT; Test: Jest+Supertest, plus a Playwright `e2e/orders.spec.ts`; docker-compose
- Architecture: layered monolith, slightly flatter than siblings (`db.ts`, `http.ts`, `errors.ts`, `validation.ts` at `src/` root rather than under `lib/`)
- Complexity: Junior+/Mid
- Educational material: STRONG — astraupskill (463 lines) + dfableandopus (565 lines).
- Quality observations:
  - README is unusually candid about scope limits: *"`userId` is a caller-provided customer reference, not authenticated identity... Supplier and PurchaseOrder models are future exercises with no implemented routes. There is no payment processing, request idempotency or deployment hardening."* — honest, well-scoped documentation rather than overclaiming.
  - Has an actual Playwright e2e spec (`e2e/orders.spec.ts`), the only sibling with a real e2e test file at the project root (others use `browser-tests/*.spec.mjs`, naming inconsistency across the cluster).
  - Prisma version drift (5.x here vs 6.19.2 in ecommerce/hr/multitenant/team) suggests this and ppm were built/fixed in an earlier pass than the others.
- Old-AI-generated smells: none seen; the explicit "not implemented" callouts in the README are the opposite of the old-AI smell of claiming fake completeness.
- Skill tags: be-node-express, db-postgres, db-transactions, orm, test-e2e, test-integration, crud-basic
- Duplicate/overlap: grokbuild* cluster.
- Learning value: High — honest scoping + real e2e coverage.
- Interview stories: "Building server-priced order creation with transactional stock reservation and cancellation restore."
- Proposed disposition: B HIGH-VALUE.

## grokbuildppmproject
- Path: `Desktop\grokbuildppmproject`            - Origin: COURSE/GENERATED
- Type: web app, monolith monorepo (backend + frontend)
- State: working-looking, but visibly less finished than its siblings      - Size: ~76 files   - Last modified: ~2026-09-18
- Purpose: Project Portfolio Management — Portfolio → Program → Project → Task hierarchy, described in its README as deliberately "medium-large" to force complex domain modeling, RBAC, audit logs, pagination/filtering (`README.md`).
- Stack: FE React/Vite (has its own `vite.config.ts`/`vitest.config.ts`, slightly divergent tooling from siblings); BE Express+TS, Prisma **^5.15.0**, Postgres, Zod, JWT; Test: Vitest (backend `test` script is `vitest run`, only one `__tests__/taskService.test.ts` found)
- Architecture: layered monolith — `controllers/taskController.ts` + `routes/{auth,portfolio,project,task}Routes.ts` + `services/{auth,portfolio,project,task}Service.ts`; note there's a `controllers/` dir but only one controller file (`taskController.ts`) — other routes appear to call services directly, an inconsistent layering compared to siblings.
- Complexity: Mid (by design/ambition) but shallower in realized test coverage than ecommerce/hr/multitenant/team.
- Educational material: USEFUL, not STRONG — `astraupskill/` has the full 8-file+VERIFICATION set (454 lines), but `dfableandopus/` only has 3 files (`01-INTERVIEW-QUESTIONS.md`, `02-STORIES-AND-RESUME.md`, `README.md`, 185 lines) — missing the code-reading-drill/take-home/system-design/flashcards files every other sibling has. This looks like the review pass was interrupted partway through for this project.
- Quality observations:
  - Root README leads with an explicit pedagogical rationale ("mirrors what engineers build at small-to-mid size companies for internal tools or SaaS products") rather than describing implemented behavior — reads more like a project *brief* than a completion report, unlike ecommerce/hr/multitenant which describe what was actually fixed.
  - Root also has `JOURNAL.md` and `PHASE_PLANS.md` (like team/support), suggesting this was built via the same phased-build process as `grokbuildsupportproject`, which never got past the planning stage — ppm apparently did get built, but the docs pass didn't fully catch up.
  - Only one test file found under backend (`taskService.test.ts`) versus 2-3 in most siblings — thinner test coverage.
- Old-AI-generated smells: none seen in the code itself; the incomplete dfableandopus pack and single test file are gaps rather than fabrication.
- Skill tags: be-node-express, db-postgres, orm, test-unit, db-modeling, crud-basic
- Duplicate/overlap: grokbuild* cluster; overlaps conceptually with grokbuildteamproject (both are project/task management domains) — worth comparing directly if consolidating.
- Learning value: Medium — real code and a full astraupskill course, but thinner tests and an incomplete interview pack versus its siblings.
- Proposed disposition: C SPECIALIZED — useful as a hierarchical-domain-modeling example (Portfolio→Program→Project→Task) distinct from the flatter siblings, but needs its dfableandopus pack finished before it's on par with the rest of the cluster.

## grokbuildsupportproject
- Path: `Desktop\grokbuildsupportproject`            - Origin: COURSE/GENERATED (planned, never built)
- Type: docs-only / skeleton
- State: skeleton — **only 4 files total**: `README.md`, `JOURNAL.md`, `PHASE_PLANS.md`, and `.git`. No `backend/`, `frontend/`, `astraupskill/`, or `dfableandopus/` exist.      - Size: ~4 files / ~0 app LOC   - Last modified: single commit 2026-07-18
- Purpose: Planned "Customer Support Ticketing + Knowledge Base Platform" (tickets, KB articles, RBAC, workflows) per README, but never implemented — README describes an ambition, not a delivered app.
- Stack: planned only — Node/TS/Express/Prisma/Postgres, React/Vite/TanStack Query/Tailwind (per README's aspirational "Tech Stack" section).
- Architecture: N/A — no code exists.
- Complexity: Tiny
- Educational material: NONE
- Quality observations: README/JOURNAL/PHASE_PLANS read like a project brief and build plan that was never executed — compare directly against grokbuildppmproject and grokbuildteamproject, which have the same JOURNAL/PHASE_PLANS front-matter but *did* get built.
- Old-AI-generated smells: none applicable (no code).
- Skill tags: none
- Duplicate/overlap: domain (support ticketing) is unique in this batch, but the project itself is just an unrealized plan.
- Learning value: Low — the planning docs alone aren't worth much without the build.
- Proposed disposition: G ARCHIVE — nothing to preserve beyond noting the domain idea was abandoned; could be revived later as a genuinely-missing domain in the grokbuild* set if someone wants an 8th CRUD variant, but as-is there is no artifact.

## grokbuildteamproject
- Path: `Desktop\grokbuildteamproject`            - Origin: COURSE/GENERATED
- Type: web app, monolith monorepo (backend + frontend)
- State: working-looking      - Size: ~75 files (+package-lock, playwright.config.mjs, JOURNAL.md, PHASE_PLANS.md at root)   - Last modified: ~2026-09-18
- Purpose: "Team workspace" — project/task/comment CRUD for a team, with team registration and membership (`README.md`).
- Stack: FE React/Vite; BE Express+TS, Prisma 6.19.2, Postgres, Zod, JWT; Test: Jest + Playwright (`playwright.config.mjs` at root, `browser-tests/workspace.spec.mjs`); docker-compose
- Architecture: layered monolith with `middleware/tenantContext.ts` again present (team-as-tenant boundary, like multitenantproject) plus `commentRepository.ts`/`commentService.ts` for the discussion feature.
- Complexity: Junior+/Mid
- Educational material: USEFUL, not STRONG — has the full astraupskill 8-file course (340 lines) but **no `dfableandopus/` directory exists at all** (confirmed via directory listing) — the interview-prep pass never reached this project, unlike ppm which at least got a partial one.
- Quality observations:
  - Reuses the `tenantContext.ts` pattern from multitenantproject for team-scoped access — good sign of a consistent access-boundary pattern being reused across the cluster rather than reinvented per project.
  - `__tests__/authService.test.ts` + `__tests__/taskRoutes.integration.test.ts` present.
  - README explicitly notes an unverified path: `docker compose up -d postgres   # unverified path: prefer npm run setup:local (see astraupskill/VERIFICATION.md)` — honest about what was and wasn't actually run/verified.
  - Same copy-pasted `"description": "Educational HR Platform backend"` in `package.json`.
- Old-AI-generated smells: copy-pasted description field; otherwise none.
- Skill tags: multitenancy, authz-rbac, be-node-express, db-postgres, orm, test-e2e, test-integration, crud-basic
- Duplicate/overlap: grokbuild* cluster; domain overlaps with grokbuildppmproject (both project/task management) — team is the simpler, flatter sibling.
- Learning value: High — real code + full astraupskill course, missing only the interview pack.
- Proposed disposition: B HIGH-VALUE — would be worth generating the missing dfableandopus pack to bring it to parity with ecommerce/hr/order/multitenant.

## grokjs
- Path: `Desktop\grokjs`            - Origin: COURSE/GENERATED
- Type: curriculum, multi-language monorepo-of-labs
- State: complete (per its own README, "Ready")      - Size: very large — `csharp-learning-lab` 242 files, `dotnet-learning-lab` 214, `javascript-learning-lab` **999 files**, `python-learning-lab` 277, plus `grokbuildjs`/`grokbuildpython`/`grokbuildc#` (~120-140 files each) and a small `Fable Learning Lab` (5 files) — several thousand files total   - Last modified: single commit 2026-07-18
- Purpose: Self-study, beginner-to-junior educational coding material across JS/TS/React, Python, C#, and .NET, plus three "grokbuild*" mini full-stack starter projects (JS/Python/C#) to apply fundamentals.
- Stack: JavaScript, TypeScript, React basics, Python, C#, .NET (DI/EF/middleware topics)
- Architecture: N/A (curriculum, not an app) — each "lab" is a flat/light directory of self-contained lesson files.
- Complexity: Tutorial → Junior
- Educational material: EXCELLENT. The dir's own `README.md` documents its own structure and evolution candidly: an original "standard style" (BEGINNER GOAL / REAL WORLD USE CASE / CONCEPTS COVERED header, numbered STEPS, dense inline comments, LINE-BY-LINE BREAKDOWN / NOOB TRANSLATION / COMMON MISTAKES / TRY CHANGING THIS / MINI CHALLENGE footer), then a "2026 Expansion" that added three more pedagogical variants per topic (Think-Predict, Bug-Hunt, Narrative) and expanded `examples/` folders "to a literal ~20x the original count (now over 1,500 example files total)". Verified directly: `csharp-learning-lab/09-classes-and-objects.cs` matches this exact header/step/footer pattern and reads as genuine, specific teaching content, not filler.
- Quality observations:
  - Self-documenting README explicitly names its own teaching philosophy and revision history — unusually good meta-documentation for a curriculum dump.
  - `javascript-learning-lab` (999 files) is disproportionately large vs siblings — likely the "flagship" lab per its own README, worth spot-checking further if reusing content, since file count that high risks templated repetition despite the README's claims.
  - Three "grokbuild*" sub-projects (js/python/c#) are separate, smaller full-stack starter attempts distinct from the batch's main `grokbuild*project` cluster (different naming, same idea: apply fundamentals in a "build a real app" context) — worth not confusing the two when cross-referencing other batches.
- Old-AI-generated smells: the explicit "-2.0", "-bug-hunt", "-narrative", "-think-predict" file-per-topic multiplication is a mild breadth-over-depth smell (volume goal stated outright: "the amount of *new* teaching material is roughly on the same scale as the material that previously existed") — likely to contain redundant/overlapping explanations across the 4 variants per topic; worth deduping before reuse rather than preserving all variants verbatim.
- Skill tags: ts-types, fe-react, be-node-express, be-python, be-dotnet, crud-basic, design-docs-adrs
- Duplicate/overlap: heavy topical overlap with `groktuts` (also JS/Python/C#/.NET fundamentals) and `JSTut` (also JS/TS/React/C#/.NET) — this batch has three largely-parallel from-scratch curricula covering nearly the same fundamentals ground from different angles/formats. Also overlaps with `JS1`'s csharp console apps at the exercise level.
- Learning value: High — mostly for raw exercise/example material to mine, less as a coherent single artifact given the volume and internal redundancy.
- Transformation opportunity: Curate/dedupe into a smaller canonical set (pick best variant per topic) rather than keep 4x redundant files per topic.
- Proposed disposition: A FLAGSHIP for its scale and self-documentation quality as a source pack, but recommend a follow-up consolidation pass given the 3-4x per-topic redundancy it admits to itself.

## groktuts
- Path: `Desktop\groktuts`            - Origin: COURSE/GENERATED
- Type: curriculum, 4 upskilling labs
- State: complete ("Ready" status for all 4 labs per root README)      - Size: 1,047 files total (dotnet-upskilling-lab 45, python-upskilling-lab 62, sql-upskilling-lab 44, web-dev-upskilling-lab 248; remaining files are node_modules-adjacent config/lockfiles at web-dev-upskilling-lab root)   - Last modified: single commit 2026-07-18
- Purpose: Structured, graded upskilling curricula for JS/TS/React, Python, C#/.NET, and SQL/Postgres, targeting beginner→junior/mid.
- Stack: JavaScript/TypeScript/React (`web-dev-upskilling-lab`), Python (`python-upskilling-lab`), C#/.NET (`dotnet-upskilling-lab`), SQL/Postgres/SQLite (`sql-upskilling-lab`)
- Architecture: N/A (curriculum) — each lab has `practice/` (real graded exercises with test files), `projects/`, and a `README.md`.
- Complexity: Tutorial → Junior/Mid (`web-dev-upskilling-lab` includes `system-design-deep-dives.md` and `interview-questions.md`, pushing toward mid-level prep)
- Educational material: STRONG-to-EXCELLENT — unlike a lot of curriculum content, this one is **actually runnable and graded**: `python-upskilling-lab/practice/python/{async,basics,data-structures,functions-oop,testing,web}/test_*.py` are real pytest files; `dotnet-upskilling-lab` has `Practice.Tests.csproj` at its root; `sql-upskilling-lab` has `pytest.ini` + `schema.sql` for practice against real schemas ("support tickets, finance, habits, events" per its README).
- Quality observations:
  - Every lab README states a clear target audience and study order rather than generic "learn X" boilerplate.
  - Real pytest test files confirmed present and organized by topic (`test_async.py`, `test_basics.py`, `test_data_structures.py`), not just prose lessons — this is graded, checkable practice, a step above pure-reading curricula.
  - `web-dev-upskilling-lab` is by far the largest (248 files) and has its own `package.json`/`vitest.config.js`/`tsconfig.json` — it's runnable as a small project, not just markdown.
- Old-AI-generated smells: none seen — the presence of real test suites per topic argues against shallow/copy-paste content.
- Skill tags: test-unit, be-python, be-dotnet, db-postgres, db-sql-raw, ts-types, fe-react, crud-basic
- Duplicate/overlap: significant topical overlap with `grokjs` (same 4 language areas) and `JSTut` (JS/TS/React/C#/.NET); groktuts differentiates itself by being **test-graded** rather than read-only, which is its main value-add over the other two.
- Learning value: High — the graded/runnable practice sets are the most "provably useful" curriculum content in this batch.
- Proposed disposition: B HIGH-VALUE — keep as the "do the exercises and see them pass/fail" complement to grokjs (read) and JSTut (reference).

## JS1
- Path: `Desktop\JS1`            - Origin: COURSE/GENERATED
- Type: monorepo(~97 small exercise apps)
- State: working-looking (mixed depth)      - Size: 97 subdirectories (`.claude`/`.git` excluded); representative subproject sizes 4-10 top-level entries each   - Last modified: single commit ("Initial commit: JS1 snapshot"), no later date confirmed beyond snapshot
- Purpose: A large pack of small, domain-varied CRUD exercise apps (asset checkout, board resolutions, budget tracker, clinic referrals, donation management, fleet maintenance, insurance claims, kanban flow, legal case tracker, patient intake, procurement portal, etc.) — clearly generated as an exercise-repetition pack across many business domains, each implemented twice: once as a TypeScript/React/Node/Postgres app (e.g. `asset-checkout`) and once as a **generic C# console/repository app** (e.g. `asset-depreciation-dotnet`, `board-resolutions-dotnet`), with a third naming convention `X-csharp` for a further C# variant.
- Stack: TS/React/Express/Postgres pattern for the non-`-dotnet`/non-`-csharp` names (e.g. `asset-checkout`: `client/`, `server/`, `shared/types.ts`, real `test/workflow.test.ts`); plain C#/.NET single-project console+repository pattern for `*-dotnet` names (`Models.cs`, `Program.cs`, `Repositories/`, `.csproj`); `*-csharp` names appear to be a third, smaller variant.
- Architecture: many independent small monoliths, no shared runtime between subprojects.
- Complexity: Junior — each subproject is intentionally small/scoped (a single CRUD domain).
- Educational material: USEFUL — 48 of the 97 subprojects have their own `astraupskill/` course (confirmed via `find . -maxdepth 2 -iname astraupskill | wc -l` = 48), each with `CODEBASE_GUIDE.md` and `USER_STORIES.md` at minimum. The `-dotnet` variants generally lack astraupskill.
- Quality observations:
  - **Confirmed template reuse smell**: `asset-depreciation-dotnet/Models.cs` and `board-resolutions-dotnet/Models.cs` are byte-identical except for the `namespace` line — both define an identical generic `WorkItem` record (`Id, Title, Owner, Category, Status, Amount, Priority, DueDate, Notes, CreatedAt, UpdatedAt`) regardless of business domain. This means the 20 `*-dotnet` projects are very likely the *same generic ticket/work-item model reskinned by name only*, not domain-specific data models — a genuine old-AI/templated-boilerplate smell. Worth spot-checking a few more `*-dotnet` pairs before relying on any one of them as a "distinct" exercise.
  - By contrast, `asset-checkout` (the TS/React variant) has a real domain-specific `shared/types.ts`, a dedicated `test/workflow.test.ts` + `test/database.ts`, and a `CODEBASE_GUIDE.md` — meaningfully more effort went into the TS variants than the `-dotnet` variants.
  - 97 subprojects is a large surface area; only ~8-10 were sampled directly, so per-subproject quality claims beyond the ones cited here are UNKNOWN / NEEDS DEEPER INSPECTION.
- Old-AI-generated smells: confirmed template-reuse across `*-dotnet` projects (identical generic `WorkItem` model renamed by namespace only, not truly domain-modeled); breadth-over-depth pattern (near-100 tiny apps, many likely shallow).
- Skill tags: crud-basic, be-node-express, be-dotnet, db-postgres, orm, ts-types, test-integration
- Duplicate/overlap: same "many small domain CRUD apps" idea as the `grokbuild*project` cluster but at much smaller individual scope; the `*-dotnet` template-reuse pattern is JS1-specific and not seen in the grokbuild* cluster's backend code.
- Learning value: Medium — good as a large *source* of varied domain names/user-stories to mine (especially the TS/React halves), but the `*-dotnet` half needs real differentiation before it's worth much as-is.
- Proposed disposition: E EXERCISE SOURCE — useful as a breadth pool of CRUD domain ideas and user stories, but not a flagship; recommend spot-checking more `*-dotnet` pairs before trusting any single one, and prioritize the TS/React + astraupskill-bearing subset over the templated `*-dotnet` set.

## jsharness/ctvodejs
- Path: `Desktop\jsharness\ctvodejs`            - Origin: ORIGINAL (the user's own project — git remote is `elirc/ctvodejs`)
- Type: CLI / agent framework, pnpm monorepo (`apps/`, `packages/`)
- State: partial / early — its own README states: *"This is an early port, not yet a feature-complete replacement. Follow the migration roadmap for current scope and parity."*      - Size: UNKNOWN precise file count (not separately measured; directory contains `apps/`, `packages/`, `docs/`, biome.json, pnpm-workspace.yaml)   - Last modified: git history present with real incremental commits (`feat(cli): demo approved skill script execution`, `feat(tools): propose activated skill scripts`, etc.) — a genuine multi-commit history, unlike the grokbuild* single-snapshot commits.
- Purpose: A TypeScript port of the open-source Rust coding-agent **VTCode** (see below), built "as a sequence of reviewable vertical slices" — i.e. an agentic-engineering learning/build exercise reimplementing a real coding-agent's architecture (event demo, config-check, LLM demo, MCP demo, MCP-stdio demo per its Quick Start).
- Stack: TypeScript, pnpm workspaces, biome for linting, MCP (Model Context Protocol) integration, LLM provider abstraction
- Architecture: modular monorepo mirroring VTCode's own crate structure, ported incrementally ("vertical slices")
- Complexity: Mid/Mid+ — porting a real agentic coding-tool's architecture (skill-script approval flow, MCP demos, config parsing) is meaningfully harder than the CRUD apps elsewhere in this batch.
- Educational material: MINIMAL — `docs/migration-roadmap.md` referenced but not deeply inspected; no astraupskill/dfableandopus-style course bundle here.
- Quality observations:
  - Real, incremental git history (not a single snapshot commit) with descriptive commit messages tracking a genuine porting effort (`test(core): execute an approved skill script`, `feat(tools): revalidate commands after approval`) — evidence of deliberate, reviewed engineering work rather than one-shot generation.
  - Explicitly scoped as a **port**, with honest "not yet feature-complete" framing.
  - This is the only agentic-engineering / LLM-tooling project in this batch — stands out from the CRUD/curriculum content around it.
- Old-AI-generated smells: none seen; this looks like the user's own deliberate, incremental agentic-engineering project.
- Skill tags: agentic-engineering, ai-llm-integration, ts-types, design-docs-adrs, legacy-codebase-reading
- Duplicate/overlap: none in this batch; conceptually related to other agent-building work referenced in the user's memory (Hermes CLI agent, Pulse orchestrator) but distinct project.
- Learning value: High — real incremental engineering on a genuinely hard problem (porting an agent framework), plus a live comparison target (the original Rust VTCode is sitting right next to it).
- Transformation opportunity: Given real git history and an ambitious, differentiated scope, this is a strong candidate for a dedicated write-up/case study ("porting an agentic coding tool from Rust to TypeScript, one vertical slice at a time") distinct from the CRUD-cluster narrative dominating this batch.
- Interview stories: "How I ported [an agentic coding CLI]'s skill-approval and MCP integration from Rust to TypeScript incrementally, verifying each vertical slice."
- Proposed disposition: C SPECIALIZED — genuinely differentiated agentic-engineering work, worth keeping and potentially promoting, but its "early/partial" self-assessment and lack of a course/docs bundle keep it out of A FLAGSHIP for now without a deeper look at `apps/`/`packages/` contents (NEEDS DEEPER INSPECTION for full completeness assessment).

## jsharness/VTCode
- Path: `Desktop\jsharness\VTCode`            - Origin: OPEN-SOURCE CLONE (third-party — **not the user's own work**)
- Type: CLI coding agent (Rust)
- State: complete, production-like — real releases, changelog, homebrew formula
- Purpose: "VT Code is a Rust coding agent built for long-running autonomous workflows, with OS-native sandboxing, multi-provider LLM support, open protocols, and extensible Skills" (its own README).
- Evidence this is vendored, not authored: `Cargo.toml` lists `authors = ["Vinh Nguyen <vinhnguyen2308@gmail.com>"]` and `repository = "https://github.com/vinhnx/vtcode"`; `git remote -v` shows `origin https://github.com/vinhnx/VTCode.git` (not an `elirc/*` fork); `git log --oneline` shows an active third-party commit history (`chore: update homebrew formula to 0.136.4`, etc.) with no user attribution.
- Stack: Rust
- Educational material: N/A — not the user's material to claim credit for, though it is clearly the reference implementation `ctvodejs` (above) is porting from, so it has *reference value* for that project.
- Skill tags: (not applicable — third-party code)
- Duplicate/overlap: this is the source project `jsharness/ctvodejs` is porting; keep the two side by side for comparison purposes but do not present VTCode itself as portfolio work.
- Learning value: N/A as a portfolio artifact, but High as reference material for evaluating `ctvodejs`'s porting fidelity/progress.
- Proposed disposition: G ARCHIVE — clearly identified third-party open-source software (vinhnx/VTCode), not the user's original work; retain only as a reference copy for `ctvodejs`, not as a standalone portfolio entry.

## JSProjectLearn ("SkillForge Quest")
- Path: `Desktop\JSProjectLearn`            - Origin: ORIGINAL app (React platform) wrapping COURSE/GENERATED underlying curriculum content
- Type: web app — a gamified learning platform, PWA (`public/manifest.webmanifest`, `public/sw.js`)
- State: complete/working-looking, actively evolving      - Size: `public/content/` alone is 13 MB / 334 catalog entries; `src/App.tsx` is 1,183 lines (per its own `handoff/01-repo-state.md`)   - Last modified: 2026-09-21 (most recently touched project in this batch alongside grokbuildmultitenantproject)
- Purpose: Per `README.md`: "turns the original software-engineering curriculum into an active, persistent campaign" — each of 329 playable "missions" (+5 reference docs) requires a **recall checkpoint**, a **prediction checkpoint**, and a **build-and-prove checkpoint** before unlocking the next node, with XP, streaks, badges, and spaced-repetition review scheduled at 2/7/30/90/180/365 days.
- Stack: React 19.2, TypeScript 7, Vite 8, Vitest 5 (`src/game/engine.test.ts` — 7 tests per handoff doc), Playwright (`scripts/browser-smoke.mjs`, `playwright.config.ts`), `react-markdown`; content stored as JSON (`public/content/missions/*.json`, `catalog.json`); Node ≥22.
- Architecture: SPA with a small dedicated "game engine" module (`src/game/engine.ts`, 156 lines — XP/unlocks/streaks/spaced repetition) separate from the UI (`App.tsx`), plus a content-integrity toolchain: `scripts/verify-content.mjs` (an `npm run verify:content` script enforcing a "content contract"), `scripts/refresh-catalog-metadata.mjs` (idempotent metadata regeneration that never rewrites archived source hashes), and SHA-256 verification of all 1,839 archived source files per `MIGRATION_REPORT.md`.
- Complexity: Mid — this is a genuine small product (gamification engine, spaced-repetition scheduling, offline-installable PWA, content-integrity verification pipeline), not just a content dump.
- Educational material: EXCELLENT, and unusually well-engineered as *delivery infrastructure* for education, not just content: 334 catalog entries (329 missions + 5 reference docs) covering — per `MIGRATION_REPORT.md` — "10 curriculum worlds spanning JavaScript, TypeScript, React, algorithms, production engineering, and an optional C# track", derived from "1,839 archived source and lesson files" (~10.17 MB), each mission auto-summarized with concepts/estimated-minutes/XP/difficulty from the original "Field Manual" lesson file via `refresh-catalog-metadata.mjs`. `handoff/` (7 files: repo-state, content-system, expansion-spec, authoring-style, execution-plan, verification-and-risks, POLISH-PLAN) documents the build process itself in detail. `astraupskill/` (8 files) also present, per the batch's standard course-doc pattern.
- Quality observations:
  - Content lineage is verifiable and auditable: `public/content/migration-report.json` records "Full source paths, language metadata, byte counts, and SHA-256 hashes" for every archived file — this is a genuinely careful data-migration/preservation design, not a casual copy.
  - Real automated verification: `npm run verify:content` enforces a content contract (schema/consistency checks presumably), and `test:browser` runs a Playwright smoke test — this app is actually checked, not just built-and-hoped.
  - Sample mission JSON (`apps-14-todo-app.json`) shows a well-structured schema: `id`, `sourceKey`, `worldId`, `concepts[]`, `estimatedMinutes`, `xp`, `difficulty`, `fileCount`, `bytes`, and three `challenges` (reconstruct/predict/prove) each with `kind`, `xp`, `minLength`, `prompt`, `hint` — this is a deliberately-designed instructional-design data model, not a flat text dump.
  - `MIGRATION_REPORT.md` "Product changes" section shows real commit-by-commit iteration (`Rebuild the mission page and dashboard for short phone sessions`, `Make the app installable and mission content readable offline`, `Refresh mission metadata and mark reference documents`, `Migrate lesson directories into SkillForge Quest app`, `Expand repo to 263 projects across 5 tracks with full learning layers`) — a genuine product-development history, not a single generation pass.
  - State is stored in `localStorage` only (per README: "Progress is stored in this browser") — no backend/sync, a deliberate and reasonable scope limit for a local self-study tool, but worth noting if evaluating for multi-device use.
- Old-AI-generated smells: none seen — this is one of the more carefully engineered artifacts in the whole batch (content-integrity hashing, idempotent metadata refresh, real verification scripts).
- Skill tags: fe-react, ts-types, test-unit, test-e2e, fe-state, design-docs-adrs, crud-basic (content model), legacy-codebase-reading (the migration itself is a legacy-code-preservation exercise)
- Duplicate/overlap: absorbs/wraps the prior "JSProjectLearn 165-project curriculum" described in the user's memory notes (now expanded to 329 playable missions across 10 worlds, including "an optional C# track" — meaning this now also overlaps thematically with grokjs/groktuts/JSTut/JS1's C# content, though delivered as gamified missions rather than raw files).
- Learning value: Very High — both as a study tool to actually use, and as a portfolio artifact: it demonstrates product thinking (retention design, spaced repetition), data-migration discipline (hash-verified content preservation), and full-stack-adjacent engineering (PWA, offline support, automated content verification) well beyond the CRUD-cluster norm in this batch.
- Transformation opportunity: This is arguably the single most "shippable as a real product" artifact in this batch — could be polished into a standalone public self-study tool/portfolio centerpiece (the gamification + spaced-repetition engine is reusable for any curriculum, not just this one).
- Interview stories: "I migrated a 1,800-file curriculum into a gamified learning app with hash-verified content integrity and idempotent metadata regeneration"; "Building a spaced-repetition scheduling engine and a three-gate (recall/predict/prove) mastery model."
- Proposed disposition: A FLAGSHIP — the strongest single artifact in this batch by engineering depth, product completeness, and self-documentation.

## JSTut
- Path: `Desktop\JSTut`            - Origin: COURSE/GENERATED
- Type: curriculum (39 flat markdown files)
- State: complete      - Size: 39 files, 15,650 total lines (`wc -l *.md`)   - Last modified: single commit 2026-07-18
- Purpose: A single progressive JS/TS/React/C#/.NET/SQL reference-and-drill curriculum: fundamentals (Parts 1-9) → advanced (10-18) → "other angles" retellings via story/analogy/flashcards (19-28, note: files 19-23 are actually C#/.NET fundamentals/advanced/netplus, and 24-28 are the "other angles" retellings for JS/TS/React/C#/.NET) → drills/workbooks (29-38) → a targeted job-description-specific interview-prep file (39).
- Stack: JavaScript, TypeScript, React, C#, .NET, SQL — covered end-to-end fundamentals through advanced through interview application.
- Complexity: Tutorial → Mid (file 39 is explicitly mid/senior interview-prep for a named job description archetype: ".NET Core/C# + React fullstack, Azure cloud-native serverless/event-driven")
- Educational material: EXCELLENT — read 5 files in full/substantial excerpt across the spread (01-core-language, 10-advanced-core-language, 24-javascript-other-angles, 29-javascript-drills, 39-interview-prep) and found each genuinely differentiated rather than templated:
  - `01-core-language.md`: standard definition→use-cases→explanation teaching format with real, specific code (`const`/`let` mutation vs rebinding example).
  - `10-advanced-core-language.md`: real advanced content (Map/Set/WeakMap, explained via a concrete DOM-element-as-key example a plain object can't handle).
  - `24-javascript-other-angles.md`: a genuinely well-written extended analogy ("JavaScript is a single worker in a kitchen...") that maps closures, `this`, the event loop, microtask/macrotask queues, and prototypes onto one consistent kitchen metaphor — this is unusually well-crafted explanatory writing, not generic filler.
  - `29-javascript-drills.md`: real predict-the-output drills with explained answers (`const x = {count:1}; x.count = 2;` → explains binding vs mutation).
  - `39-interview-prep-dotnet-react-azure.md`: maps a literal job-description's bullet points to specific interview topics and cross-references back to the earlier Parts (e.g., "Azure Functions... the main gap, study hardest") — this is targeted, not generic, prep.
- Quality observations:
  - No filler/repetition detected across the 5 sampled files despite covering 39 files/15,650 lines — genuinely differentiated content per file, unlike the more volume-driven grokjs pattern.
  - The "other angles" section (24-28) is a deliberate second-pass pedagogical device (story/analogy retelling) layered on top of the fundamentals/advanced sections, similar in spirit to grokjs's multi-variant approach but executed as one polished file per topic rather than 4x file multiplication.
  - File 39 demonstrates real job-targeting — maps a specific JD to specific gaps ("the main gap, study hardest") rather than generic interview advice.
- Old-AI-generated smells: none seen in the sampled content — writing quality and specificity are consistently high across widely-spaced sample points (file 1, file 10, file 24, file 29, file 39).
- Skill tags: ts-types, fe-react, be-node-express, be-dotnet, db-sql-raw, design-docs-adrs, cloud-azure
- Duplicate/overlap: covers much of the same fundamentals ground as grokjs (JS/C#/.NET) and groktuts (JS/TS/React/C#/.NET/SQL), but JSTut's "other angles" + targeted interview-prep format is distinct and arguably the most immediately reusable of the three for interview prep specifically.
- Learning value: Very High — the job-description-mapped interview-prep file (39) is unusually actionable and specific; the "other angles" retellings are genuinely well-written, not padding.
- Proposed disposition: B HIGH-VALUE — could be A FLAGSHIP on quality alone, but held to B because it's one of three largely-overlapping JS/TS/C#/.NET fundamentals curricula in this same batch (grokjs, groktuts, JSTut) and a consolidation decision across all three should happen before crowning one flagship.

## Batch observations

- **The `grokbuild*` cluster is one system, not seven unrelated apps.** All seven share the exact same scaffold (Express/TS/Prisma/Postgres backend, React/Vite frontend, docker-compose, astraupskill course, dfableandopus interview pack), the exact same single-snapshot-commit git pattern (frozen 2026-07-18, all later work uncommitted), and the exact same "hardened-Grok-starter" narrative in their READMEs. Treat them as one project family when deciding what to keep: `grokbuildmultitenantproject` (A, security-fix narrative) and `grokbuildecommerceproject`/`grokbuildhrproject`/`grokbuildorderproject`/`grokbuildteamproject` (B) are the complete/strong members; `grokbuildppmproject` (C) and `grokbuildsupportproject` (G) are the incomplete ones that didn't finish the review/build pass.
- **None of the grokbuild* work is committed to git.** Every project with real code has a single frozen "snapshot" commit and then uncommitted local modifications for both the app-code fix pass (~2026-09-09) and the docs/review pass (~2026-09-18/21). If any of this is meant to be preserved long-term, it should be committed before anything else touches these directories.
- **Old-AI smells were mild and specific, not systemic.** The clearest confirmed smells in this batch are: (1) copy-pasted `package.json` descriptions across ecommerce/hr/team (`"Educational HR Platform backend"` verbatim in a non-HR project); (2) JS1's `*-dotnet` subprojects reusing an identical generic `WorkItem` model renamed only by namespace across at least 2 confirmed domains (asset-depreciation, board-resolutions) — likely across all 20 `*-dotnet` projects. Everywhere else — the grokbuild* backend transaction/locking logic, groktuts's graded pytest suites, JSTut's writing, JSProjectLearn's content-integrity pipeline — quality was notably *above* typical old-AI-generated baseline, consistent with these being post-review/fixed artifacts rather than raw first-pass output.
- **Three largely-redundant JS/TS/C#/.NET fundamentals curricula exist side by side: grokjs, groktuts, JSTut.** All three cover materially the same core-language/advanced/OOP/async ground for JS, TS, React, C#, and .NET. They differentiate on format (grokjs: multi-variant lesson files + huge example count; groktuts: graded pytest/xUnit/vitest practice; JSTut: polished single-file-per-topic reference + story retellings + job-specific interview prep). A consolidation/dedup decision across these three is the single highest-leverage cleanup opportunity in this batch — likely keep groktuts's graded exercises + JSTut's reference/interview material, and mine grokjs mainly for its larger raw example pool rather than preserving all 4 pedagogical variants per topic.
- **`JSProjectLearn` has quietly grown into the strongest single artifact in the batch.** What the user's memory index still describes as "165-project curriculum, summarize structure, don't record each" is now (per its own migration report, dated as recently as 2026-09-21) a 334-mission gamified spaced-repetition platform ("SkillForge Quest") with hash-verified content migration and automated verification — the memory note is stale and should probably be updated to reflect the rebuild.
- **`jsharness` is a mixed bag by design**: one subdirectory (`VTCode`) is straightforwardly third-party open-source software with no user authorship (confirmed via git remote + Cargo.toml authorship) and should not be presented as portfolio work; the other (`ctvodejs`) is a genuine, differentiated, incrementally-committed original project (a TypeScript port of VTCode) — the only agentic-engineering/LLM-tooling work in this batch, and worth a closer, dedicated look beyond this survey pass (`apps/`/`packages/` contents were not deeply inspected).
- **`grokbuildsupportproject` is the one clear "never happened" item** in this batch — a planning stub with no code, directly comparable to (and less complete than) its sibling `grokbuildppmproject`/`grokbuildteamproject`, which share the same JOURNAL/PHASE_PLANS front-matter but did get built.
