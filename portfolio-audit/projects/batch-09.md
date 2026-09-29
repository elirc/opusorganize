# Batch 09 — Build Projects (fabledocs/Astra course monorepos)
Scope: C:\Users\Owner\Desktop\_Organized Desktop\02 Build Projects\{aff-wt-be06, buildaffiliate, buildagenthelpdesk, buildagentteachGEM, buildagentteaching, buildanalytics, buildantigVG, buildasana, buildCRMPYJS, buildecom, buildgum, buildjira, buildScedulingPYJS, buildsubbox}  |  Candidate dirs inspected: 14  |  Meaningful projects: 13  |  Tiny/empty/boilerplate: 1

**Batch-wide finding:** 12 of the 14 directories are NOT their own git repositories — `git -C <dir>` in those falls through to a parent/stray home-directory `.git` (remote `elirc/grouphelpdesk.git`, 0 commits on `main`), which is a red herring, not this project's history. Only `buildaffiliate` and `buildagentteaching` have their own `.git` folder in place. Where no local git history exists, "Last modified" below uses filesystem mtimes (dominated by an `astraupskill/` curriculum fix-pass on 2026-09-18/19/21, consistent with the user's memory of a 2026-09-16→21 Astra review+fix pass across 153 projects). Actual app-code authorship dates (from README/fabledocs content and sibling memory files) are noted separately per project where known.

Every project in this batch (except the empty `aff-wt-be06` stub) carries an `astraupskill/` folder — a per-project junior→mid engineering curriculum (README + 04-TESTING-AND-DEBUGGING.md + evidence/snapshots in the fuller ones) — this is the "Astra" curriculum layer referenced in the user's memory, already reviewed/fixed in a prior pass. Several older ones instead (or also) carry a `dfableandopus/` folder (numbered docs: STORIES-AND-RESUME, SYSTEM-DESIGN-FOLLOWUPS, FLASHCARDS, TRACE-LAB) — an earlier-generation Fable+Opus course-doc format.

| Project | Path | Type | Origin | Stack | Complexity | Docs | Disp |
|---|---|---|---|---|---|---|---|
| aff-wt-be06 | aff-wt-be06 | empty stub | N/A | none | Tiny | none | G |
| buildaffiliate | buildaffiliate | monorepo(3 apps) | COURSE/GENERATED | Next.js+Fastify+Prisma+Postgres+Turbo | Mid+ | fabledocs(6)+astraupskill(12) | B |
| buildagenthelpdesk | buildagenthelpdesk | monorepo(1 app+pkgs) | COURSE/GENERATED | Next.js+Prisma+Postgres+deterministic agents | Mid | fabledocs(3)+astraupskill(14) | B |
| buildagentteachGEM | buildagentteachGEM | monolith web app | COURSE/GENERATED | Next.js14+Prisma5+SQLite | Mid | fabledocs(5)+astraupskill(35) | B |
| buildagentteaching | buildagentteaching | monorepo(1 app+pkgs) | COURSE/GENERATED | Next.js+Prisma+Postgres+deterministic agents | Mid | fabledocs(4)+astraupskill(12) | B |
| buildanalytics | buildanalytics | monorepo(FE+BE) | COURSE/GENERATED | React/Vite+Express+Prisma+Postgres+Redis/BullMQ | Mid+ | fabledocs(4)+7 root guide docs+astraupskill(12) | B |
| buildantigVG | buildantigVG | monorepo(2 apps) | COURSE/GENERATED | NestJS+React/Vite+Prisma+Postgres | Junior+ | docs/+dfableandopus(7)+astraupskill(27) | C |
| buildasana | buildasana | monorepo(FE+BE) | COURSE/GENERATED | ASP.NET Core 8 clean arch+React/Vite (in-memory infra) | Junior+ | docs/+dfableandopus(7)+astraupskill(29) | C |
| buildCRMPYJS | buildCRMPYJS | monorepo(FE+BE) | COURSE/GENERATED | React/Vite+Express+TS+Prisma+Postgres (no Python despite name) | Junior+ | docs/+dfableandopus(7)+astraupskill(36) | C |
| buildecom | buildecom | Next.js monolith | COURSE/GENERATED | Next.js App Router+Prisma+Redis+Stripe Connect (scaffold, deps not installed) | Mid | fabledocs?+astraupskill(14) | C |
| buildgum | buildgum | SPA (vanilla workshop) | COURSE/GENERATED | Vite/TS SPA, local-only CRUD | Junior | dfableandopus(7)+astraupskill(15) | D |
| buildjira | buildjira | monorepo(3 apps, migrated) | COURSE/GENERATED | ASP.NET Core 8 (active) + archived Node/Prisma/React (commented) + Vite/React web | Junior+ | docs/+dfableandopus(7)+astraupskill(15) | C |
| buildScedulingPYJS | buildScedulingPYJS | monorepo(FE+BE) | COURSE/GENERATED | React/Vite+Express+TS+Prisma+Postgres+Redis/BullMQ (no Python despite name) | Mid | 7 root guide docs+astraupskill(14) | C |
| buildsubbox | buildsubbox | SPA (vanilla workshop) | COURSE/GENERATED | Vite/TS SPA, local-only CRUD | Junior | astraupskill(17) | D |

## aff-wt-be06
- Path: aff-wt-be06 — Origin: N/A — Type: empty stub
- State: skeleton (empty) — Size: 0 files, 2 empty dirs (`apps/api`, `apps/api` only) — Last modified: UNKNOWN (no files to stamp)
- Purpose: Folder name (`aff-wt-be06`) and its `elirc/grouphelpdesk` git remote suggest it was meant as a worktree/branch checkout related to `buildaffiliate`, but it contains no files at all — just an empty `apps/api` directory tree.
- Stack: N/A (no source present)
- Architecture: N/A
- Complexity: Tiny
- Educational material: NONE
- Quality observations: Completely empty except directory scaffolding; not a functioning worktree (no `.git` file/pointer found inside it either).
- Old-AI-generated smells: none seen (nothing to inspect)
- Skill tags: (none)
- Duplicate/overlap: named/implied relation to buildaffiliate but shares no content with it
- Learning value: Low — nothing here to learn from
- Proposed disposition: **G ARCHIVE** — empty; safe to delete or ignore, contributes nothing.

## buildaffiliate
- Path: buildaffiliate — Origin: COURSE/GENERATED (LLM-built, fabledocs/PR-per-story workflow) — Type: monorepo (3 apps: web, api, redirect)
- State: working-looking — Size: ~451 files (excl. node_modules/dist/.next) — Last modified: git HEAD 2026-07-31 (120 commits, latest "Merge PR #37 consolidate backend stories"); astraupskill fix-pass touched 2026-09-21
- Purpose: Multi-tenant affiliate/referral marketing platform — brand↔affiliate link tracking, click attribution, commission calculation, fraud review, and payouts.
- Stack: FE: Next.js (apps/web, Tailwind); BE: Fastify (apps/api) + a dedicated Fastify redirect service (apps/redirect) for high-volume click redirects; DB: Postgres via Prisma (`apps/api/prisma/schema.prisma`); Test: Vitest (unit + `vitest.integration.config.ts`) plus a root `tests/campaign-slug.test.mjs`; Infra: docker-compose, Turborepo monorepo (turbo.json, tsconfig.base.json)
- Architecture: modular monolith split into 3 deployable apps (web/api/redirect) sharing `packages/`; redirect service separated for perf/scale reasons — a genuinely instructive real-world pattern.
- Complexity: Mid+
- Educational material: USEFUL — fabledocs/ (6 files: app-overview, user-stories, postback-integration, backend-stories, query-performance, README) + astraupskill/ (12 files incl. 04-TESTING-AND-DEBUGGING.md). Project-specific, not generic; postback-integration and query-performance docs are notably concrete. Preserve.
- Quality observations:
  - Real git history (120 commits, PR-per-story merges) — unusually verifiable provenance vs. most of this batch.
  - Dedicated redirect microservice separated from the main API — shows awareness of hot-path scaling concerns.
  - Has both unit and integration Vitest configs — signals intent to test against real Postgres, not just mocks.
  - Own memory record (buildaffiliate-platform.md) flags a Redis-TTL redirect bug and unauthenticated postbacks as known defects — worth treating as teaching seams rather than hiding.
- Old-AI-generated smells: none seen beyond the already-known defects noted above.
- Skill tags: fe-next, be-node-express, db-postgres, orm, db-migrations, test-unit, test-integration, arch-modular-monolith, queues, security-owasp, docker, ci-cd
- Duplicate/overlap: aff-wt-be06 (empty, likely an abandoned worktree attempt for this repo, no actual shared content)
- Learning value: High — real multi-service architecture (redirect service as its own deployable), real bugs already catalogued, real git history to read.
- Transformation opportunity: Could anchor a "why we split out a redirect service" case study or a security-fix exercise (unauthenticated postbacks, TTL race) for an interview-prep pack.
- Interview stories it could support: "designing high-throughput click redirects separate from the main API"; "fixing an unauthenticated webhook/postback endpoint"; "diagnosing a Redis TTL race in production."
- Proposed disposition: **B HIGH-VALUE** — real architecture, real git history, concrete known bugs to reference in interviews.

## buildagenthelpdesk
- Path: buildagenthelpdesk — Origin: COURSE/GENERATED — Type: monorepo (1 Next.js app + packages)
- State: working-looking — Size: ~221 files — Last modified: no own git history (0 commits, borrowed remote); astraupskill fix-pass touched 2026-09-21; README states repo intentionally avoids real LLM APIs/keys
- Purpose: Internal enterprise help-desk + incident-intelligence platform — ticketing, incident monitoring, structured logs, background job monitoring, audit events, and deterministic "mock agents" standing in for AI triage.
- Stack: Next.js App Router + React, TS, Postgres, Prisma (`packages/db/prisma/schema.prisma`), Zod validation, Vitest, internal CSS-variable UI package — explicitly no Tailwind/LangChain/external keys.
- Architecture: TS modular monolith across `packages/` with a single `apps/web`.
- Complexity: Mid
- Educational material: USEFUL — fabledocs/ (3 files) + astraupskill/ (14 files incl. testing guide). Preserve.
- Quality observations:
  - Deterministic mock-agent design (no real LLM calls) is a deliberate, well-documented choice — good teaching pattern for testable "agentic" features without API cost/nondeterminism.
  - Broad Vitest suite: `agent-diff`, `agents`, `analytics`, `api-keys`, `bulk-triage`, `business-hours` test files visible at a glance — real behavioral coverage, not just smoke tests.
  - No git history locally to verify authorship timeline; per user memory this repo had "no commits" as of 2026-07-24 — appears to remain uncommitted.
- Old-AI-generated smells: none seen; deterministic-agent framing specifically avoids the common "fake AI as complete" smell.
- Skill tags: fe-next, be-validation, db-postgres, orm, agentic-engineering, test-unit, observability-logs, be-async-jobs
- Duplicate/overlap: shares its git remote (`elirc/grouphelpdesk`) with buildagentteachGEM, buildanalytics, buildantigVG, buildasana, buildCRMPYJS, buildecom, buildgum, buildjira, buildScedulingPYJS, buildsubbox, and aff-wt-be06 — this is a stray/inherited remote from the parent home-dir repo, not evidence of relation between these projects; do not treat as a duplicate signal.
- Learning value: High — deterministic-agent pattern is directly reusable across other "agentic" projects in the portfolio and is a strong, low-risk way to demo agent-adjacent work without API dependency.
- Transformation opportunity: Extract the deterministic-mock-agent + business-hours/SLA logic as a standalone teaching module on "testable agent workflows."
- Interview stories it could support: "building a testable agent layer without live LLM calls"; "SLA/business-hours-aware ticket triage logic."
- Proposed disposition: **B HIGH-VALUE** — strong test coverage, reusable deterministic-agent pattern; needs committing to git to lock in state.

## buildagentteachGEM
- Path: buildagentteachGEM — Origin: COURSE/GENERATED — Type: single Next.js app (monolith, not a monorepo — no `apps/`)
- State: working-looking (per own memory: COMPLETE, 19 stories, 129/64 commits in the *public* repo — see below) — Size: ~134 files — Last modified: no own local `.git` (0 commits via borrowed remote); astraupskill fix-pass 2026-09-19
- Purpose: "EduOps" school-operations cockpit — students, teachers, courses, sections, enrollments, assignments, grades, attendance, counselling interventions — wrapped with structured logs/audit/job-queue observability and 5 deterministic "analyst" agents that read the DB and persist inspectable reports.
- Stack: Next.js 14 App Router, React 18 Server Components, Prisma 5, SQLite, TypeScript strict; tests via `tests/*.test.ts` (agent-diff, assignments, coursework) + `scripts/test-workflows.mjs`; `astraupskill/evidence/` contains recorded test run logs/JSON.
- Architecture: modular monolith with a distinct 5-agent "analyst" layer.
- Complexity: Mid
- Educational material: USEFUL — fabledocs/ (5 files incl. codebase-gotchas + what-changed) + astraupskill/ (35 files, the richest in this batch, with evidence/ test-run artifacts). Preserve.
- Quality observations:
  - Per user memory (eduops-buildagentteachgem.md), this project was previously COMPLETE with 64 commits/22 PRs/129 tests and is pushed to public `elirc/3buildagentteachgem` — but **this local folder has no `.git` of its own**, meaning the on-disk copy has lost its history relative to the pushed remote. Flagged discrepancy: verify against the GitHub remote before treating local disk state as authoritative.
  - Memory also notes a "committed-dev.db drift" gotcha — i.e., a SQLite dev DB was previously accidentally committed/drifted; worth checking `.gitignore` coverage if this folder is re-linked to git.
  - 5-agent "analyst" design plus fabledocs/04-what-changed.md suggests active iteration tracking, a good practice rarely seen elsewhere in this batch.
- Old-AI-generated smells: none directly observed; the memory-noted dev.db commit drift is the kind of smell worth confirming/fixing if this is revived.
- Skill tags: fe-next, db-sqlite, orm, agentic-engineering, observability-logs, be-async-jobs, test-unit, design-docs-adrs
- Duplicate/overlap: strong conceptual overlap with buildagentteaching (both "Agentic Education Operations/EduOps" platforms with deterministic agents, students/courses/sections/enrollments domain) — likely two separate course generations of the same idea; compare fabledocs/02-user-stories.md in both before consolidating.
- Learning value: Very High — richest astraupskill curriculum in the batch (35 files + evidence/ test-run logs) plus a live public repo; the local/remote git-history mismatch is itself a useful "recover from lost local history" exercise.
- Transformation opportunity: Re-clone from `elirc/3buildagentteachgem` to restore local git history, then use the evidence/ folder as a template for "how to record verifiable test-run evidence" across other projects.
- Interview stories it could support: "5-agent deterministic analyst layer reading a relational DB"; "recovering a local working copy after losing git history."
- Proposed disposition: **A FLAGSHIP** — largest curriculum, deterministic multi-agent architecture, has a real public repo (verify remote state) — best showcase piece in this batch for agentic-engineering skill tag.

## buildagentteaching
- Path: buildagentteaching — Origin: COURSE/GENERATED — Type: monorepo (1 Next.js app under `apps/web` + `packages/`)
- State: working-looking — Size: ~261 files — Last modified: own git HEAD 2026-07-31 (129 commits, latest "Merge PR #32 docs/record-us-11-to-20"); astraupskill fix-pass 2026-09-21
- Purpose: "Agentic Education Operations" — teacher/student/course/section/term/guardian/enrollment/assignment/rubric/submission/gradebook/attendance/intervention/approval/notification/logs/jobs/audit + deterministic mock-agent workflows. No Tailwind, no real LLM APIs.
- Stack: Next.js App Router (apps/web), TS/React/Node, Prisma (`packages/db/prisma/schema.prisma`), Vitest (`vitest.config.ts`, `.env.test`), docker-compose + docker-compose.test.yml, `tests/runtime-bulk-enroll.test.mjs`.
- Architecture: TS modular monolith, monorepo layout (apps/ + packages/), separate test docker-compose for isolated test DB.
- Complexity: Mid
- Educational material: USEFUL — fabledocs/ (4: app-overview, user-stories, progress, README) + astraupskill/ (12). Preserve.
- Quality observations:
  - Real, verifiable git history: 129 commits ending with a PR that explicitly "records US-11 to US-20" — matches user memory (buildagentteaching-edu-ops.md) noting US-01..12 merged earlier and US-13..20 as the remaining work; this local copy appears to include the full 20-story arc now (worth a quick confirm of fabledocs/03-progress.md contents).
  - Separate `docker-compose.test.yml` + `.env.test` shows deliberate test/dev environment isolation — a genuinely production-shaped practice.
  - `runtime-bulk-enroll.test.mjs` at repo root alongside a `tests/` dir under vitest suggests a mix of integration-style runtime tests and unit tests.
- Old-AI-generated smells: none seen.
- Skill tags: fe-next, be-node-express, db-postgres, orm, agentic-engineering, test-integration, test-ci, docker, config-secrets
- Duplicate/overlap: strong domain overlap with buildagentteachGEM (both EduOps/education-ops platforms with deterministic agents) — likely parallel course generations of the same brief; also related to buildagenthelpdesk (shares the "deterministic mock agents, no real LLM APIs, no Tailwind" house style, suggesting a shared prompt template across the batch).
- Learning value: High — real git history with a resolved story backlog (per memory, previously stalled at US-10, now shows the full run in the merge log) makes this a good "watch a project recover from a stall and finish" narrative.
- Transformation opportunity: Pair with buildagentteachGEM as a "two takes on the same brief" comparison exercise (different DB choice — Postgres vs SQLite — and different agent counts).
- Interview stories it could support: "isolating a Postgres test environment via docker-compose.test.yml + .env.test"; "resuming a stalled 20-story backlog to completion."
- Proposed disposition: **B HIGH-VALUE** — real, complete git history and a genuinely production-shaped test-isolation setup.

## buildanalytics
- Path: buildanalytics — Origin: COURSE/GENERATED — Type: monorepo (frontend/ + backend/, not app-router-nested)
- State: working-looking — Size: ~435 files — Last modified: no own git history (0 commits via borrowed remote); README/memory says "all 20 fabledocs stories built + merged 2026-07-25" (public elirc/3buildanalytics) but this local copy has no `.git`; astraupskill fix-pass 2026-09-21
- Purpose: Production-style internal KPI/admin analytics dashboard — KPI tracking, operational analytics, audit visibility, monitoring dashboards, CSV exports, role-aware ops workflows.
- Stack: FE: React+TS+Vite, TanStack Query, Zustand, React Router, RHF, Zod, Tailwind, Recharts; BE: Node/TS/Express, Prisma, Postgres, JWT+RBAC; Async: Redis+BullMQ; Test: Vitest, Supertest, RTL, Playwright; Infra: Docker Compose, GH-Actions-friendly scripts.
- Architecture: modular monolith, FE/BE split at top level (not apps/ workspace-style), async job queue via BullMQ.
- Complexity: Mid+
- Educational material: STRONG — unusually rich root-level doc set beyond fabledocs: ARCHITECTURE.md, CODE_REVIEW_GUIDE.md, DEBUGGING_GUIDE.md, DEPLOYMENT_GUIDE.md, FEATURE_WALKTHROUGHS.md, LEARNING_GUIDE.md, SENIOR_ENGINEERING_DECISIONS.md, TESTING_GUIDE.md — plus fabledocs/ (4) and astraupskill/ (12). This is the most deliberately-documented "senior engineering decisions" style project in the batch. Preserve, high value.
- Quality observations:
  - Full test pyramid claimed by tooling choice (Vitest unit, Supertest API, RTL component, Playwright e2e) — verify actual coverage before trusting the label, but the scaffolding intent is real (`.env.test`, `backend/tests`, `vitest.setup.ts`).
  - "SENIOR_ENGINEERING_DECISIONS.md" is an unusually explicit ADR-style artifact for this batch — worth reading closely as an interview-prep asset.
  - Per user memory, per-project this was already fully built and merged (PRs #1-#22) on the public repo; local copy lacks git history — same "local lost history vs. remote has it" pattern as buildagentteachGEM.
- Old-AI-generated smells: none observed directly; the volume of root-level *_GUIDE.md files mirrors buildScedulingPYJS almost file-for-file (see overlap note) — suggests a templated doc-generation pass rather than fully bespoke writing; spot-check for boilerplate/generic content before relying on them as "deep" docs.
- Skill tags: fe-react, fe-state, be-node-express, authz-rbac, db-postgres, orm, queues, test-e2e, test-integration, design-docs-adrs, docker, ci-cd
- Duplicate/overlap: shares an identical root-level guide-doc filename set (ARCHITECTURE/CODE_REVIEW_GUIDE/DEBUGGING_GUIDE/DEPLOYMENT_GUIDE/FEATURE_WALKTHROUGHS/LEARNING_GUIDE/SENIOR_ENGINEERING_DECISIONS/TESTING_GUIDE) with buildScedulingPYJS — near-certain same doc-template generation pass across both; compare the two doc sets for genuinely project-specific vs. copy-pasted content.
- Learning value: Very High — richest "senior engineering decisions" documentation style in the batch; strong candidate to mine for interview narratives about tradeoffs.
- Transformation opportunity: Use SENIOR_ENGINEERING_DECISIONS.md + ARCHITECTURE.md as the seed for a dedicated "how to write an ADR" exercise pack, reused across projects that lack this doc type.
- Interview stories it could support: "RBAC-protected analytics dashboard with async CSV export via BullMQ"; "explaining a documented senior-level architecture decision."
- Proposed disposition: **B HIGH-VALUE** — best documentation-as-teaching-material candidate in the batch; needs git history restored/verified against the public remote.

## buildantigVG
- Path: buildantigVG — Origin: COURSE/GENERATED — Type: monorepo (apps/api + apps/web)
- State: partial (README explicitly states this) — Size: ~94 files — Last modified: no own git; dfableandopus mtime 2026-09-18
- Purpose: "GlobalWorkforce OS" — tenant-scoped worker directory: sign-in, profile CRUD, version-conflict handling, bounded search/pagination, guarded status transitions, transactional worker audit records. README explicitly states worker self-service and global-admin access are NOT implemented — an honestly-scoped partial build.
- Stack: NestJS API (`apps/api`, Prisma+Postgres), React/Vite web (`apps/web`), e2e tests present (`apps/api/test`, `scripts/test-database.mjs`), docs/06-testing-strategy.md.
- Architecture: modular monolith, NestJS module structure.
- Complexity: Junior+ (explicitly scoped as "a serious scaffold" but incomplete on the RBAC/global-admin axis)
- Educational material: USEFUL — docs/ (has 06-testing-strategy.md) + dfableandopus/ (7 files: 02-STORIES-AND-RESUME etc.) + astraupskill/ (27 files) — no fabledocs/ folder here (uses docs/ + dfableandopus/ instead). Preserve.
- Quality observations:
  - README is unusually honest about scope gaps ("Worker self-service and global administrator access are not implemented") — good example of documenting known limitations rather than overclaiming completeness.
  - Version-conflict handling + transactional audit records called out explicitly — concrete concurrency-control teaching material if verified in code (`apps/api/src`).
  - NestJS choice (vs. the Express used elsewhere in this batch) makes this the one project demonstrating a structured DI/module framework — useful diversity for a be-nest skill tag.
- Old-AI-generated smells: none seen; the explicit "not implemented" scoping is the opposite of the common over-claiming smell.
- Skill tags: be-nest, db-postgres, orm, multitenancy, db-concurrency, authz-rbac, test-e2e
- Duplicate/overlap: none obvious within this batch (only NestJS project); domain (worker directory/HR) doesn't overlap with the education/help-desk cluster.
- Learning value: Medium-High — concurrency (version conflicts) + multitenancy + NestJS are each individually valuable, but partial completeness (no self-service/global-admin) caps immediate showcase value.
- Interview stories it could support: "handling optimistic-concurrency version conflicts on profile updates"; "tenant-scoped RBAC with intentionally limited role coverage."
- Proposed disposition: **C SPECIALIZED** — good NestJS/multitenancy/concurrency reference but incomplete; useful as a targeted exercise source rather than a flagship.

## buildasana
- Path: buildasana — Origin: COURSE/GENERATED — Type: monorepo (backend/ .NET + frontend/ React)
- State: working-looking (in-memory infra, not yet wired to a real DB per README) — Size: ~92 files — Last modified: no own git; dfableandopus mtime 2026-09-18
- Purpose: Asana-inspired work-management system: projects, tasks, capacity, goals, automations, approvals, RBAC, audit events, executive portfolio health — scoped as "a serious scaffold" for learning production-quality C#/.NET + React patterns.
- Stack: BE: ASP.NET Core 8 minimal API, clean architecture (`BuildAsana.Api`/`.Application`/`.Domain`/`.Infrastructure` projects), repository abstraction over an **in-memory** infrastructure adapter (no real DB/Prisma-equivalent found — no `schema.prisma`, no migrations folder seen); FE: React 18 + TS + Vite with a typed API client and a "resilient mock fallback." Tests: `backend/tests/BuildAsana.Application.Tests` (xUnit-style .NET test project).
- Architecture: .NET Clean Architecture (4-project layering) — the clearest classic clean-architecture example in this batch.
- Complexity: Junior+
- Educational material: USEFUL — docs/ + dfableandopus/ (7: incl. 05-SYSTEM-DESIGN-FOLLOWUPS.md) + astraupskill/ (29 files, incl. evidence/backend-test-release-05 + snapshots/WorkManagementServiceTests-before.cs.txt — before/after test snapshots, a genuinely distinctive artifact). Preserve.
- Quality observations:
  - Clean Architecture layering (Api/Application/Domain/Infrastructure) is the textbook .NET pattern — good be-dotnet reference distinct from buildjira's simpler minimal-API approach.
  - astraupskill/snapshots/ contains a literal before/after test file — rare, concrete evidence of an iterative fix being taught rather than just described.
  - In-memory infrastructure adapter (no real DB) means this is explicitly a scaffold, not a runnable production app — don't overstate completeness.
  - Frontend explicitly ships a "resilient mock fallback" for its typed API client — a defensive-FE pattern worth calling out as a teaching point (graceful degradation when backend is unavailable).
- Old-AI-generated smells: none seen; scope is honestly framed as scaffold-not-production.
- Skill tags: be-dotnet, arch-clean-hex, authz-rbac, test-unit, fe-react, ts-types, design-docs-adrs
- Duplicate/overlap: domain overlap with buildjira (both project/task-management "clones") — different stacks (asana=React+.NET clean-arch vs. jira=migrated .NET minimal API + archived Node) make them complementary rather than truly redundant; good side-by-side "clean architecture vs. minimal API" comparison.
- Learning value: High — one of the few true Clean Architecture .NET examples with a captured before/after test snapshot artifact.
- Transformation opportunity: Use the snapshots/ before/after pair as a template for a "watch a real fix happen" teaching format applied to other .NET projects.
- Interview stories it could support: "structuring a .NET service with Clean Architecture (Domain/Application/Infrastructure/Api)"; "designing a resilient frontend API client with mock fallback."
- Proposed disposition: **C SPECIALIZED** — strong .NET clean-architecture reference; capped by in-memory-only backend (not yet production-shaped end to end).

## buildCRMPYJS
- Path: buildCRMPYJS — Origin: COURSE/GENERATED — Type: monorepo (backend/ + frontend/)
- State: partial (README: "Phase-by-phase implementation is in progress... currently includes: monorepo scaffolding, docker-compose services, healthcheck endpoint and config wiring") — Size: ~142 files — Last modified: no own git; dfableandopus mtime 2026-09-18
- Purpose: Lightweight internal CRM / sales-pipeline platform. Name says "PYJS" but there is **no Python anywhere** — backend is TypeScript/Express, confirmed by directory listing (`backend/` has only `.ts`/`package.json`/`prisma`, no `.py` files).
- Stack: FE: React+TS+Vite, TanStack Query, Zustand, React Router; BE: Node+TS+Express, Postgres+Prisma; Auth: JWT+refresh+RBAC; Infra: Docker Compose; Test: `backend/src/app.test.ts`, `frontend/src/App.test.tsx` (minimal, single top-level test files each — not a real suite yet).
- Architecture: modular monolith, FE/BE split.
- Complexity: Junior+ (explicitly early-phase)
- Educational material: USEFUL — docs/ + dfableandopus/ (7) + astraupskill/ (36 files, largest astraupskill folder among the "PYJS-named" trio, incl. evidence/backend-test-01 + frontend-test-01 + snapshots/app-test-before.ts.txt). Preserve.
- Quality observations:
  - README self-reports as in-progress scaffolding, not a finished CRM — treat "Purpose" as intent, not delivered feature set.
  - Only single top-level test files per side (`app.test.ts`, `App.test.tsx`) — thin coverage relative to the elaborate astraupskill curriculum layered on top; the curriculum outpaces the app itself here.
  - Naming ("PYJS") is misleading/stale — likely a leftover from an earlier plan to use Python that was dropped; worth renaming if consolidated.
- Old-AI-generated smells: shallow tests (single file per side) relative to project scope claims in the README's stack list.
- Skill tags: fe-react, be-node-express, authn, authz-rbac, db-postgres, orm, docker
- Duplicate/overlap: near-identical shape/stack to buildScedulingPYJS (both "PYJS"-named, both React/Vite+Express+Prisma+Postgres+RBAC scaffolds at similar phase) — likely generated from the same template/prompt pair; buildScedulingPYJS is further along (has Redis/BullMQ + a runtime test) and should probably be the one preserved if consolidating.
- Learning value: Medium — useful as an early-phase CRUD/auth scaffold example, but thin test coverage and incomplete feature set limit standalone showcase value.
- Interview stories it could support: "JWT access+refresh token flow with RBAC route protection" (if actually implemented — verify in `backend/src`).
- Proposed disposition: **C SPECIALIZED** — early-phase scaffold; keep as a paired reference alongside buildScedulingPYJS rather than standalone.

## buildecom
- Path: buildecom — Origin: COURSE/GENERATED — Type: single Next.js app (monolith, "MarketForge")
- State: skeleton/scaffold (README: "intentionally scaffolded without installing dependencies or running services... Docker, npm install, database provisioning, and third-party credentials are left to the learner") — Size: ~140 files — Last modified: no own git; astraupskill fix-pass 2026-09-21
- Purpose: Production-style multi-vendor marketplace — buyer storefront, seller ops portal, platform-admin console, shared domain rules, typed API routes, Prisma persistence, Redis-backed security primitives, Stripe Connect payment boundaries.
- Stack: Next.js App Router, Prisma (`prisma/schema.prisma`), Redis, Stripe Connect; Test: `tests/integration/checkout.test.ts`, `tests/unit/order-state.test.ts`, `tests/unit/pricing.test.ts`, `tests/runtime-order-status.test.mjs`; Playwright config present.
- Architecture: modular monolith within a single Next.js app, three logical portals (buyer/seller/admin) sharing domain code.
- Complexity: Mid
- Educational material: USEFUL — astraupskill/ (14 files). No separate fabledocs/ folder found here (unusual for this batch — check `docs/` instead, present but not deeply inspected). Preserve.
- Quality observations:
  - README is explicit that this is an unrun scaffold — code was never installed/executed here; treat all "it works" claims as unverified until dependencies are actually installed and tests run.
  - Stripe Connect + Redis-backed security primitives + multi-portal domain rules is an ambitious scope for a never-run scaffold — worth a deeper read of `src/` before trusting completeness.
  - Test files exist across unit/integration/runtime tiers (checkout, order-state, pricing) suggesting the intended shape even if unexecuted.
- Old-AI-generated smells: possible "written as if production but never run" — the README itself flags this risk; needs an actual `npm install && test` pass to confirm the code is real and not merely plausible-looking.
- Skill tags: fe-next, be-rest-design, db-postgres, orm, caching, security-owasp, test-integration, test-unit
- Duplicate/overlap: none strong within this batch (only true e-commerce/marketplace project).
- Learning value: Medium — Stripe Connect + multi-portal marketplace domain is valuable content, but "never installed or run" status means real functional risk is unverified; needs a verification pass before use in interviews as a "working system."
- Transformation opportunity: Run `npm install`/tests to convert this from an unverified scaffold into a demonstrably-working reference; the Stripe Connect boundary logic alone could become a standalone payments-integration teaching module.
- Interview stories it could support (once verified): "designing a marketplace's Stripe Connect payment boundary"; "multi-portal RBAC in a single Next.js app."
- Proposed disposition: **C SPECIALIZED** — high-value domain (marketplace/Stripe Connect) but unverified/never-run; needs a build-and-test pass before promoting further.

## buildgum
- Path: buildgum — Origin: COURSE/GENERATED — Type: single-page vanilla workshop app
- State: working-looking (README gives explicit run instructions and a pinned Node version) — Size: ~93 files — Last modified: no own git; dfableandopus mtime 2026-09-18
- Purpose: "Buildgum" — local creator-commerce CRUD workshop: products, discounts, exact-cent cart math, durable simulated receipts, cancellation, reviewed backup/recovery. Explicitly no real payments or deliveries.
- Stack: Vite + TS SPA (`index.html`, `src/`), local-only persistence, `scripts/test.mjs` + `test/` dir, pinned to Node 22.16.0, npm lockfile pinned.
- Architecture: single-page CRUD app, no backend server (browser-storage-backed per the README's "storage belongs to that origin" note).
- Complexity: Junior
- Educational material: USEFUL — astraupskill/ (15) + dfableandopus/ (7, incl. 06-FLASHCARDS.md). Preserve as an exercise source.
- Quality observations:
  - "Exact-cent cart math" and "durable simulated receipts" called out explicitly in the README — suggests deliberate attention to floating-point/money-precision correctness, a classic junior-dev gotcha worth verifying in `src/`.
  - Pinned Node version + `npm ci --ignore-scripts` instructions show unusually careful reproducibility discipline for a tiny workshop app.
  - No backend/DB — this is a client-only CRUD exercise, appropriately scoped as junior-level.
- Old-AI-generated smells: none seen.
- Skill tags: fe-testing, ts-types, crud-basic, fe-forms-validation
- Duplicate/overlap: buildsubbox is the closest sibling — same "local CRUD workshop, no real payments/carrier ops, pinned Node, ports 5180/5181, dfableandopus+astraupskill" template, different domain (subscription boxes vs. creator commerce) — almost certainly generated from the same prompt pattern as a paired exercise set.
- Learning value: Medium — good self-contained junior exercise (money-precision + CRUD), limited scope caps it below "High."
- Interview stories it could support: "handling exact-cent monetary calculations in JS without floating-point drift."
- Proposed disposition: **D REFERENCE** — solid small exercise, keep as reference/exercise-source material alongside buildsubbox rather than a standalone flagship.

## buildjira
- Path: buildjira — Origin: COURSE/GENERATED, migrated mid-course — Type: monorepo (3 apps: archived Node api, active .NET api, Vite React web)
- State: working-looking (active side); partial/archived (legacy side) — Size: ~126 files — Last modified: no own git; dfableandopus mtime 2026-09-18
- Purpose: Jira-style project-management practice app — portfolio dashboard, project board, issue editing, demo actor context, health checks, audit events, local persistence.
- Stack: **Active**: ASP.NET Core 8 minimal API (`apps/dotnet/BuildJira.Api`), tests in `tests/BuildJira.Api.Tests` (`IssueApiTests.cs`, `UpdateIssueTests.cs`). **Archived**: the original Node/Prisma/React source (`apps/api` with its own `prisma/schema.prisma` and `test/`) is left in place but explicitly commented-out/inert per the README ("old TypeScript/Node/Prisma/React source files are intentionally left in place as commented archival reference material"). Web: Vite+React (`apps/web`).
- Architecture: migrated stack — a rare, explicit "we rewrote this in a different language mid-course and kept the old code as reference" case.
- Complexity: Junior+
- Educational material: USEFUL — docs/ + dfableandopus/ (7) + astraupskill/ (15). Preserve — the migration-with-archived-original pattern is itself educational.
- Quality observations:
  - Deliberate stack migration (Node/Prisma/React → C#/.NET minimal API) with the old code kept commented as reference is an unusually transparent "here's what changed and why" artifact — rare and valuable for teaching technology-migration decision-making.
  - .NET test project (`BuildJira.Api.Tests`) targets issue CRUD/update specifically — concrete, verifiable behavior tests rather than smoke tests.
  - Because the legacy Node/Prisma side is commented-out rather than deleted, file/LOC counts in the "142 files" total include dead code — treat the 126-file count as inflated relative to the truly active surface area.
- Old-AI-generated smells: none seen; archival-not-deleted approach to the old stack is a thoughtful practice, not a smell.
- Skill tags: be-dotnet, be-node-express (archived), fe-react, test-unit, backcompat-versioning, legacy-codebase-reading
- Duplicate/overlap: domain overlap with buildasana (both project/task-management clones); the archived-Node-vs-active-.NET split inside this one project is itself worth comparing to buildasana's from-scratch Clean Architecture .NET approach.
- Learning value: High — the explicit mid-course language migration with archived original code is a genuinely rare and valuable teaching artifact (most projects in this portfolio don't show their "before" state this way).
- Transformation opportunity: Turn the Node→".NET rewrite with rationale" into a dedicated "why and how we migrated a backend" case study/interview story, using the archived code as the literal "before."
- Interview stories it could support: "migrating a Node/Prisma API to ASP.NET Core mid-project and justifying the decision"; "keeping legacy code as commented reference vs. deleting it."
- Proposed disposition: **C SPECIALIZED** — unusual and valuable as a migration case study, but the mixed-stack state means it's not a single coherent flagship app.

## buildScedulingPYJS
- Path: buildScedulingPYJS — Origin: COURSE/GENERATED — Type: monorepo (backend/ + frontend/)
- State: working-looking (further along than its buildCRMPYJS sibling — has a runtime completion test) — Size: ~199 files — Last modified: no own git; astraupskill fix-pass 2026-09-21
- Purpose: Full-stack scheduling/appointment platform — auth (access+refresh), RBAC route protection, user/staff/customer/service management, staff-service assignments, availability windows/blocked time, timezone-safe slot generation. Name says "PYJS" but is **TypeScript/Express, no Python** (confirmed: `backend/` has only `.ts`, `package.json`, `prisma`, `Dockerfile`, no `.py`).
- Stack: React/Vite/TS FE, Node/TS/Express BE, Postgres+Prisma, Redis+BullMQ, JWT+RBAC; Test: `tests/runtime-appointment-complete.test.mjs`, `TESTING_GUIDE.md`.
- Architecture: modular monolith, FE/BE split, async scheduling via BullMQ.
- Complexity: Mid
- Educational material: STRONG — identical root-guide-doc set to buildanalytics (ARCHITECTURE.md, CODE_REVIEW_GUIDE.md, DEBUGGING_GUIDE.md, DEPLOYMENT_GUIDE.md, FEATURE_WALKTHROUGHS.md, LEARNING_GUIDE.md, SENIOR_ENGINEERING_DECISIONS.md, TESTING_GUIDE.md) + astraupskill/ (14). No separate fabledocs/ folder found. Preserve, but cross-check with buildanalytics for duplicated/generic content.
- Quality observations:
  - "Timezone-safe slot generation" called out explicitly — a genuinely hard, interview-relevant scheduling problem if actually implemented correctly; worth a deeper code read of `backend/src` to verify.
  - Has a runtime "appointment-complete" test — an end-to-end-flavored check beyond pure unit tests, unlike its buildCRMPYJS sibling.
  - Shares the exact same guide-doc filenames as buildanalytics — near-certain templated doc generation; spot-check for genuinely scheduling-specific content vs. boilerplate reused verbatim.
- Old-AI-generated smells: potential boilerplate in the shared *_GUIDE.md set (see overlap note) — verify project-specificity before treating as deep documentation.
- Skill tags: fe-react, be-node-express, authn, authz-rbac, db-postgres, orm, queues, test-integration, db-concurrency
- Duplicate/overlap: paired with buildCRMPYJS (same stack/template family, "PYJS" naming); shares its doc-template set with buildanalytics.
- Learning value: Medium-High — timezone-safe scheduling logic + refresh-token auth are solid interview-relevant topics if verified; capped slightly by templated-doc uncertainty.
- Interview stories it could support: "timezone-safe appointment slot generation avoiding DST/off-by-one bugs"; "access+refresh JWT rotation with RBAC."
- Proposed disposition: **C SPECIALIZED** — most complete of the "PYJS" pair; good scheduling-domain reference once doc-content specificity is confirmed.

## buildsubbox
- Path: buildsubbox — Origin: COURSE/GENERATED — Type: single-page vanilla workshop app
- State: working-looking — Size: ~85 files — Last modified: no own git; astraupskill mtime 2026-09-18
- Purpose: "ParcelPilot / Buildsubbox" — subscription-box CRUD workshop: inventory, plans, subscribers, ratings; preference-aware curation; atomic stock reservation; persistent shipment history; reviewed backup recovery. No real billing/email/carrier operations.
- Stack: Vite + JS SPA (no TS config found, unlike buildgum which has `tsconfig.json`/`tsconfig.test.json`), `test/model.test.mjs`, `scripts/test.mjs`, pinned Node 22.12+.
- Architecture: single-page CRUD app, client-only.
- Complexity: Junior
- Educational material: USEFUL — astraupskill/ (17 files, incl. 07-TRACE-LAB.md, an exercise type not seen elsewhere in this batch). No dfableandopus/ here (unlike its buildgum sibling). Preserve.
- Quality observations:
  - "Atomic stock reservation" is an explicit concurrency-adjacent claim worth verifying in `src/` — a good junior→mid bridge topic if implemented with real locking/transaction logic even in a client-only app (likely simulated via an in-memory/localStorage transaction pattern).
  - astraupskill/07-TRACE-LAB.md is a distinct exercise format not seen in the other astraupskill folders sampled — worth checking what "trace lab" content looks like as a potential reusable exercise template.
  - Plain JS (no TypeScript) distinguishes this from buildgum despite otherwise being the same template family — slightly lower rigor.
- Old-AI-generated smells: none seen.
- Skill tags: crud-basic, db-concurrency, fe-testing
- Duplicate/overlap: buildgum (near-identical template: local-only CRUD workshop, pinned Node, ports 5180/5181, astraupskill-only docs) — different domain (subscription boxes vs. creator commerce), buildgum uses TS and this one doesn't.
- Learning value: Medium — same tier as buildgum; the "atomic stock reservation" concept and the unique TRACE-LAB exercise format nudge it slightly toward reuse value.
- Interview stories it could support: "simulating atomic stock reservation in a client-only app."
- Proposed disposition: **D REFERENCE** — pair with buildgum as junior-level CRUD exercise reference material; the TRACE-LAB doc format is worth extracting for reuse regardless of the app's own fate.

## Batch observations
- **Shared git-remote red herring**: 11 of the 14 directories have no `.git` of their own and silently inherit a stray parent repo (`elirc/grouphelpdesk`, 0 commits). This is NOT evidence these projects are related to each other or to "grouphelpdesk" — it's an artifact of running `git` inside a directory tree under the user's home folder without a local `.git`. Only `buildaffiliate` and `buildagentteaching` have their own local git history; several others (buildagentteachGEM, buildanalytics per user memory) are reported COMPLETE with real commit history on their *public* GitHub remotes, meaning the local disk copies here have lost their `.git` folders relative to what's actually pushed. Recommend re-cloning from the public `elirc/3build*` remotes before treating local disk state as authoritative for any consolidation/archival decision.
- **Two documentation-layer generations coexist**: newer projects use `astraupskill/` (README + 04-TESTING-AND-DEBUGGING.md, sometimes with `evidence/` test-run logs and `snapshots/` before-after diffs); older ones additionally/instead use `dfableandopus/` (numbered docs ending in STORIES-AND-RESUME, SYSTEM-DESIGN-FOLLOWUPS, FLASHCARDS, TRACE-LAB). Every non-empty project in this batch has at least one of the two.
- **Templated doc/README generation is visible across sibling pairs**: buildanalytics and buildScedulingPYJS share an identical 7-file root guide-doc set (ARCHITECTURE/CODE_REVIEW_GUIDE/DEBUGGING_GUIDE/DEPLOYMENT_GUIDE/FEATURE_WALKTHROUGHS/LEARNING_GUIDE/SENIOR_ENGINEERING_DECISIONS/TESTING_GUIDE) almost certainly from the same generation pass; buildCRMPYJS and buildScedulingPYJS share stack, phase-language, and the "PYJS" naming despite neither containing any Python; buildgum and buildsubbox share the exact local-CRUD-workshop template (pinned Node version, port 5180/5181 convention, no backend, same doc folder shape) differing only in domain and TS-vs-JS.
- **"PYJS" naming is misleading**: neither buildCRMPYJS nor buildScedulingPYJS contains any Python code — both are TypeScript/Express/Prisma. The name likely reflects an original plan (Python backend + JS frontend) that was changed during generation; worth renaming if these are kept.
- **Deterministic-mock-agent pattern recurs**: buildagenthelpdesk, buildagentteaching, and buildagentteachGEM (an education-ops/help-desk cluster) all explicitly avoid real LLM API calls in favor of deterministic mock agents — a consistent, deliberate, and reusable house style across this generation era, and a good multi-project source for an "agentic-engineering without live model dependency" teaching arc.
- **Completeness is uneven and self-reported honestly in most READMEs**: buildantigVG, buildasana, buildCRMPYJS, and buildecom all explicitly flag partial/scaffold/never-run status in their own README text rather than overclaiming — a positive signal for trustworthiness of the docs, but it means several of these need a build-and-verify pass before being showcased as "working" projects.
- **aff-wt-be06 is essentially garbage**: two empty directories and nothing else; almost certainly an abandoned worktree/checkout attempt tied to buildaffiliate's `elirc/3build-affiliate` repo, but shares no actual content with it.
- **Notable gap**: no project in this batch has CI configuration beyond docker-compose + package scripts visible at this depth (no `.github/workflows` was surfaced by the searches run) — worth a follow-up check if `ci-cd`/`test-ci` claims in fabledocs need verification.
