# Batch 10 — Master Projects (03 Master Projects)
Scope: master, "master 5", "master 6", master1, master2, master3, master4, master555, master7, mastercal, masterdidy, masterdub, masterfinisc, masterflag, masterform, masterhop, masteridur, masterindicoPYJS, masterlink, mastermatter, mastermayan  |  Candidate dirs inspected: 21  |  Meaningful projects: 19  |  Tiny/empty/boilerplate: 2

Note on method: every clone directory (masterXXX/<clone>) is `git init`-ed with **zero commits** (`git log` → "does not have any commits yet"), so dates below use file mtimes, not commit history. This is read-only evidence only — no build/install/test was run anywhere in this batch.

## Quick table

| Project | Path | Type | Origin | Stack | Complexity | Docs | Disp |
|---|---|---|---|---|---|---|---|
| Master Life Plan | master | web app | ORIGINAL/COURSE | Next.js 16 / React 19 / Prisma 6 | Junior+ | EXCELLENT (astraupskill/) | B |
| Master6 LMS (v1) | "master 6" | monorepo(3 apps) | ORIGINAL/COURSE | Node/Express-ish API+web+worker, Prisma | Mid | EXCELLENT (astraupskill/ + dfableandopus/) | B |
| GlobalWork EOR Platform | master1 | monorepo(8 pkgs) | ORIGINAL/COURSE | NestJS/Next.js/Prisma/BullMQ/Testcontainers | Mid+ | EXCELLENT (astraupskill/, 47 feature docs, 20 walkthroughs) | A |
| Enterprise Billing Platform | master2 | monorepo(5 pkgs) | ORIGINAL/COURSE | Express/React/Prisma/BullMQ | Mid | EXCELLENT (astraupskill/ + dfableandopus/) | B |
| Support Desk CRM | master3 | monorepo(5 pkgs) | ORIGINAL/COURSE | Express/React/Prisma/Vite/Vitest | Junior+ | EXCELLENT (astraupskill/ + dfableandopus/) | C |
| Atlas Fulfillment | master4 | web app (client+server in one repo) | ORIGINAL/COURSE | Express 5/React 19/Prisma/Vite/worker | Junior+ | EXCELLENT (astraupskill/ + dfableandopus/) | C |
| Master7 LMS (v2) | master7 | monorepo(8 pkgs) | ORIGINAL/COURSE | same @lms/* stack as master6 | Mid | EXCELLENT (astraupskill/, remediation journal) | B |
| (empty) master 5 | "master 5" | — | — | — | Tiny | none | G |
| (empty) master555 | master555 | — | — | — | Tiny | none | G |
| Cal.com clone | mastercal\cal.diy | monorepo | OPEN-SOURCE CLONE | Next.js/tRPC/Prisma | Production-like | STRONG (fabledocs/upskill, 53 files) | D |
| Dify clone | masterdidy\dify | monorepo | OPEN-SOURCE CLONE | Next.js + Python backend | Production-like | STRONG ("fable docs"/upskill, 53 files) | D |
| Dub clone | masterdub\dub | monorepo | OPEN-SOURCE CLONE | Next.js/Turborepo/Prisma | Production-like | STRONG ("fable docs"/upskill, 53 files) | D |
| Infisical clone | masterfinisc\infisical | monorepo | OPEN-SOURCE CLONE | Fastify/Knex/Postgres + React/Vite | Production-like | EXCELLENT (fable-docs/, 60 files, newest template) | C |
| Flagsmith clone | masterflag\flagsmith | monorepo | OPEN-SOURCE CLONE | Django/DRF + React 19 | Production-like | EXCELLENT ("fable docs"/, newest template, upgraded) | C |
| Formbricks clone | masterform\formbricks | monorepo | OPEN-SOURCE CLONE | Next.js/Prisma/Redis | Production-like | STRONG (fabledocs/upskill, 53 files) | D |
| Hoppscotch clone | masterhop\hoppscotch | monorepo | OPEN-SOURCE CLONE | Nuxt/Vue + Node | Production-like | STRONG (fabledocs/upskill, 53 files) | D |
| IDURAR ERP/CRM clone | masteridur\idurar-erp-crm | monorepo(2 apps) | OPEN-SOURCE CLONE | MERN (Express/React/Mongo) | Mid | EXCELLENT (fable docs/, newest template, upgraded) | C |
| Indico clone | masterindicoPYJS\indico | monolith | OPEN-SOURCE CLONE | Python/Flask + React/Webpack | Production-like | NONE (no curriculum found) | G |
| Linkwarden clone | masterlink\linkwarden | monorepo | OPEN-SOURCE CLONE | Next.js/Prisma | Production-like | STRONG (fabledocs/upskill, 53 files) | D |
| Mattermost clone | mastermatter\mattermost | monorepo | OPEN-SOURCE CLONE | Go server + React webapp | Production-like | USEFUL (sibling astraupskill/, 12 files, Go-specific) | C |
| Mayan EDMS clone | mastermayan\Mayan-EDMS | monolith | OPEN-SOURCE CLONE | Django/Celery | Production-like | STRONG (fabledocs/upskill, 53 files) | D |

---

## Master Life Plan

- Path: master
- Origin: ORIGINAL/COURSE — Type: web app
- State: working-looking — Size: 143 files (excl. node_modules) — Last modified: Feb 21 2026 (mtime; git repo has 0 commits — `git -C master log` errors "does not have any commits yet")
- Purpose: Personal life-planning app (Areas→Goals→Projects→Tasks), daily checklist workflow with timers, locked schedule blocks, offline mutation queue. Evidence: `master/README.md`.
- Stack: Next.js 16.1.6 / React 19.2.3 (`package.json`), Prisma 6.16.3, SQLite (`dev.db` present at 0 bytes, unseeded), no visible auth beyond a "local default user" (README: "App no longer requires login")
- Architecture: single Next.js app, `src/app/api/*` route handlers, `middleware.ts`, `prisma/`
- Complexity: Junior+
- Educational material: EXCELLENT — `master/astraupskill/` (01-CODEBASE-MAP.md … 07-TRACE-LAB.md + README.md + VERIFICATION.md + evidence/ + snapshots/, 12 items). Read in full: `astraupskill/README.md` and `VERIFICATION.md` — both are tightly project-specific (exact file paths `src/app/api/tasks/route.ts`, `src/app/api/tasks/[id]/route.ts`), explain a real ownership-guard bug (task↔project relationship not re-validated on reassignment), and VERIFICATION.md is unusually honest about what a mocked-Prisma regression test does and doesn't prove ("It is not evidence that real Zod validation ran... does not establish cookie or session correctness"). This is the "Astra" curriculum-fix-pass lineage referenced in the user's own memory (fablereview-astra-audit). Preserve as-is.
- Quality observations:
  - `docs/intern/ARCHITECTURE.md` + `docs/intern/walkthroughs/` exist for onboarding
  - `tests/` has `task-project-isolation.test.mjs` and `timer.test.ts` plus a custom TS loader helper — real but thin (2 test files)
  - `.env` / `.env.example` present, `.gitignore` covers `.env`
  - `dev.db` is 0 bytes — DB not seeded/exercised in this snapshot
  - README describes a deliberately odd UX ("red demonic splash screen", 5s countdown) — an intentional idiosyncrasy, not a defect
- Old-AI-generated smells: none seen beyond the thin (2-file) native test suite; the astraupskill material actively counters typical "mock-as-complete" smells by calling them out explicitly
- Skill tags: fe-next, fe-react, be-rest-design, orm, db-sqlite, authz-rbac, test-unit, legacy-codebase-reading, code-review
- Duplicate/overlap: sibling of master1/master2/master3/master4/master6/master7 — same "generate a fictional SaaS + Astra CRUD-repair lesson" pipeline, different domain (personal productivity vs. B2B SaaS)
- Learning value: High — smallest/simplest of the cluster, good entry point, curriculum quality is excellent
- Transformation opportunity: Could anchor a short "read the ownership-guard bug, fix it yourself" onboarding exercise reusing astraupskill's existing snapshots/evidence scaffolding.
- Interview stories it could support: "found and fixed an authorization gap where a foreign-key relationship wasn't re-validated on update" (tenant/ownership-guard pattern, transferable to any FK-reassignment endpoint)
- Proposed disposition: B HIGH-VALUE — solid small teaching artifact with an unusually rigorous, honest verification doc; keep for the ownership-guard lesson specifically.

## Master6 LMS (v1)

- Path: "master 6"
- Origin: ORIGINAL/COURSE — Type: monorepo (apps: api, web, worker; packages: domain)
- State: working-looking (planned features exceed built features) — Size: 130 files — Last modified: Sep 18 2026 (dfableandopus/, most recent); apps/docs mostly May 4 2026
- Purpose: Enterprise LMS / certification platform — courses, cohorts, enrollments, completion tracking. Workspace name is `@lms/api` / `@lms/web` (`apps/api/package.json`, `apps/web/package.json`) — **same lineage as master7**, an earlier/parallel snapshot of the identical LMS codebase.
- Stack: Node monorepo (workspaces `api/web/worker/domain`), Prisma-based per `docker-compose.yml`, no test/framework deps visible in root `package.json` (they live per-app)
- Architecture: modular monolith, apps/api + apps/web + apps/worker + packages/domain, docker-compose for infra
- Complexity: Mid
- Educational material: EXCELLENT and unusually double-layered —
  - `astraupskill/` (12 files: 01-CODEBASE-MAP.md…07-TRACE-LAB.md, README, VERIFICATION.md, evidence/, snapshots/). Read `astraupskill/README.md` in full: "Master 6: learner enrollment, completion, and durable side effects" — teaches that a learner action is valid only when authenticated user + org header + enrollment's course version all agree; exact file citations (Express router + Prisma + domain completion predicates).
  - `dfableandopus/` (7 files: 01-INTERVIEW-QUESTIONS.md, 02-STORIES-AND-RESUME.md, 03-CODE-READING-DRILL.md, 04-TAKE-HOME.md, 05-SYSTEM-DESIGN-FOLLOWUPS.md, 06-FLASHCARDS.md, README.md) — a career-prep layer (interview Qs, resume-story framing, take-home exercise, flashcards) built on top of the same codebase, most recently touched (Sep 18 2026).
  - `docs/features/01..21-*.md` — 21 planned feature slices (course versioning, SCORM packages, video processing, certificate verification, etc.) — this is a *backlog*, not all implemented; treat as design docs, not proof of built features.
- Quality observations:
  - `docs/architecture/{architecture-journal,final-system-design,initial-architecture-plan}.md` present
  - Native test files found: 3 (`*.test.ts`/`*.spec.ts` outside node_modules) — thin relative to the 21-feature backlog, i.e. docs describe more than what's demonstrably tested here
  - `docker-compose.yml` for local infra
- Old-AI-generated smells: docs/features backlog is aspirational and could be mistaken for "done" — flag when reusing (don't cite as evidence of a working SCORM/video pipeline)
- Skill tags: be-node-express, orm, db-postgres, authz-rbac, multitenancy, docker, design-docs-adrs, legacy-codebase-reading
- Duplicate/overlap: **direct duplicate/iteration of master7** (identical `@lms/api`/`@lms/web` package names, same domain). master7 is further along (verify script, remediation journal, feature 01-07 implemented) while master6 has a longer backlog (21 planned features) and the extra `dfableandopus/` career-prep layer.
- Learning value: Medium — value is mostly in the unique `dfableandopus/` interview-prep layer; the base LMS itself is superseded by master7 for architecture study
- Proposed disposition: B HIGH-VALUE — keep specifically for `dfableandopus/` (interview/flashcard layer is not duplicated elsewhere in this batch); otherwise consolidate architecture study time into master7.

## GlobalWork EOR Platform

- Path: master1
- Origin: ORIGINAL/COURSE — Type: monorepo (apps: api, web, worker; packages: config, contracts, database, domain, test-utils)
- State: working-looking, most feature-rich in the cluster — Size: 281 files — Last modified: May 4 2026 (mtime; astraupskill present, no dfableandopus)
- Purpose: Fictional Employer-of-Record (EOR) SaaS — worker onboarding, payroll, invoicing, compliance, tenant isolation. Evidence: `master1/README.md` ("living software project for practicing real-world engineering: domain modeling, tenant isolation, workflow state, auditability, background jobs").
- Stack: NestJS API, Next.js web, Postgres+Prisma, Redis+BullMQ worker, Docker Compose, Playwright/Vitest-or-Jest/Testcontainers (all per README)
- Architecture: modular monolith, 8-package workspace (api/web/worker/config/contracts/database/domain/test-utils), OpenTelemetry-ready
- Complexity: Mid+ — the deepest/most mature of the master1-7 cluster
- Educational material: EXCELLENT and by far the largest documentation set of the batch —
  - `astraupskill/` (12 files, same 7-chapter format as the rest of the cluster)
  - `docs/code-walkthroughs/` — **20 numbered walkthrough files** (01-prisma-schema.md … 20-testcontainers-helper.md) covering schema, seed, domain states/country-profile/money, every NestJS service, web API client, dashboard, worker process, shared config, and the Testcontainers test helper
  - `docs/features/` — **47 numbered feature docs** (01-auth-rbac through 47-sla-task-queue-system), covering RBAC, tenant isolation tests, file upload (MinIO/S3), time-off/expense workflows, notification queues, OpenAPI codegen, payroll locking/adjustments, invoice PDF generation, outbox pattern, feature flags, observability, CSV import/export, admin impersonation, SLA task queue
  - Plus `docs/ARCHITECTURE_JOURNAL.md`, `docs/CODEBASE_STRUCTURE_AND_SYSTEM_DESIGN.md`, `docs/DATABASE_MIGRATION_GUIDE.md`, `docs/SYSTEM_DESIGN_FORWARD_PLAN.md`
- Quality observations:
  - 12 native test files found outside node_modules — more than siblings but still modest relative to the 47-feature doc set (docs likely outpace fully-verified test coverage; treat feature docs as design/build journal, cross-check specific claims before reuse)
  - Outbox pattern, worker retry policies, and domain-event abstraction are explicitly named topics (`docs/features/16-worker-outbox-pattern.md`, `43-background-job-retry-policies.md`, `44-domain-event-abstraction.md`) — advanced, senior-oriented content for this batch
  - `.env.example` + Docker Compose present
- Old-AI-generated smells: none directly observed; the sheer feature-doc count (47) relative to 12 test files is worth spot-checking before treating every documented feature as fully implemented and tested
- Skill tags: be-nest, fe-next, db-postgres, orm, db-migrations, queues, be-async-jobs, outbox, authz-rbac, multitenancy, observability-logs, test-integration, design-docs-adrs
- Duplicate/overlap: same pipeline as master/master2/master3/master4/master6/master7 but this is the flagship/most-developed instance
- Learning value: Very High — richest single learning artifact in this batch (47 feature slices + 20 code walkthroughs + astraupskill CRUD lesson + Testcontainers integration testing)
- Transformation opportunity: Strong candidate to promote as the flagship "how a modular-monolith SaaS actually grows" reference — the feature/walkthrough docs read like a real build journal and could anchor a multi-week self-study track or interview system-design prep.
- Interview stories it could support: tenant isolation design and its integration tests; outbox pattern for worker reliability; payroll locking/adjustment workflow (concurrency-sensitive business rule); OpenAPI-generated client discipline.
- Proposed disposition: A FLAGSHIP — largest, most mature, most senior-oriented educational artifact found in Batch 10.

## Enterprise Billing Platform

- Path: master2
- Origin: ORIGINAL/COURSE — Type: monorepo (apps: api, web, worker; packages: db, domain)
- State: working-looking — Size: 110 files — Last modified: Sep 12 2026 (README), astraupskill present, dfableandopus present
- Purpose: Multi-tenant SaaS billing/subscription platform. Evidence: `master2/README.md` ("learning-oriented multi-tenant SaaS billing and subscription platform").
- Stack: Express API, React admin/customer portal, Prisma+Postgres db package, BullMQ worker, Vitest 3.1.2 (`package.json`)
- Architecture: modular monolith (api/web/worker/db/domain), Docker Compose for infra
- Complexity: Mid
- Educational material: EXCELLENT — `astraupskill/` (same 7-chapter/README/VERIFICATION format) plus `dfableandopus/` (interview questions, stories/resume, code-reading drill, take-home, system-design follow-ups, flashcards — same 6-file structure as master6's).
- Quality observations:
  - `docs/` has 8 top-level entries (architecture/feature docs, lighter than master1/master4 but present)
  - 4 native test files found — thin
  - `.env.example` + `docker-compose.yml` present
- Old-AI-generated smells: none seen beyond thin test coverage relative to doc scope
- Skill tags: be-node-express, fe-react, db-postgres, orm, be-async-jobs, multitenancy, authz-rbac, design-docs-adrs
- Duplicate/overlap: same master*-cluster pipeline; billing domain is unique among the 7 (no other billing-focused instance in this batch)
- Learning value: Medium-High — combination of astraupskill (CRUD-repair) + dfableandopus (interview prep) makes it a compact two-layer study unit
- Interview stories it could support: multi-tenant billing/subscription domain modeling, background job (BullMQ) reliability
- Proposed disposition: B HIGH-VALUE — solid, complete two-layer teaching unit; keep.

## Support Desk CRM

- Path: master3
- Origin: ORIGINAL/COURSE — Type: monorepo (apps: api, web, worker; packages: domain, shared)
- State: working-looking — Size: 68 files (smallest of the cluster) — Last modified: Sep 12 2026 (README)
- Purpose: Support/CRM ticketing tool. Evidence: `master3/README.md` ("modular-monolith learning project modeled after internal support and CRM tools").
- Stack: Express, React, Prisma 5.22, Vite 6, Vitest 2.1.8 (`package.json`)
- Architecture: modular monolith (api/web/worker/domain/shared)
- Complexity: Junior+
- Educational material: EXCELLENT — `astraupskill/` covers "tenant scope, operational ticket authorization, role-aware comment visibility, Prisma transactions" (per `README.md` "Learning Path" section) plus `dfableandopus/` interview-prep set (same 6-file structure).
- Quality observations:
  - `docs/architecture/architecture-plan.md`, `architecture-journal.md`, `docs/walkthrough/important-files.md` referenced by README's explicit "Learning Path"
  - Only 3 native test files — thinnest test footprint in the cluster
  - `.env` + `.env.example` present
- Old-AI-generated smells: none seen; smallest/simplest instance, proportionate to its size
- Skill tags: be-node-express, fe-react, orm, db-transactions, authz-rbac, multitenancy, design-docs-adrs
- Duplicate/overlap: same cluster pipeline; smallest/simplest instance — good "first" entry point alongside master
- Learning value: Medium — good compact entry point but redundant with master/master2 for someone who already has one of those
- Proposed disposition: C SPECIALIZED — keep as the lightest-weight entry point in the cluster for onboarding a new learner quickly; otherwise redundant with master.

## Atlas Fulfillment

- Path: master4
- Origin: ORIGINAL/COURSE — Type: web app (client+server co-located, plus a worker)
- State: working-looking — Size: 79 files — Last modified: Sep 12 2026 (README)
- Purpose: Warehouse/ecommerce inventory, orders, fulfillment operations tool. Evidence: `master4/README.md`.
- Stack: Express 5, React 19, Prisma 6.19, Vite 8, Vitest 4.1.5 (`package.json`); NOT the apps/packages layout — single `src/` tree with `src/client`, `src/server`, `src/shared`, `src/worker` subfolders (`src/App.tsx`, `src/server/app.ts`, `src/server/db.ts`, `src/worker/reconciliation.worker.ts`)
- Architecture: single-repo modular monolith (client/server/shared/worker folders inside one `src/`), a `reconciliation.worker.ts` background job for inventory reconciliation
- Complexity: Junior+
- Educational material: EXCELLENT — `astraupskill/` (standard 7-chapter format) plus `dfableandopus/` (README only — thinner than master2/3/6's full 6-file interview-prep set; likely a partial/earlier drop)
- Quality observations:
  - `docs/architecture/{architecture-journal,final-system-design,initial-architecture-plan}.md`, `docs/features/000-backlog.md` + 3 numbered feature docs (001-auth-rbac-shell, 002-audit-log-viewer, 003-csv-export), `docs/walkthroughs/important-files.md`
  - 3 native test files
  - Distinct architecture from siblings — this is the one instance NOT using an apps/packages monorepo layout, worth noting for anyone comparing "how do you structure a modular monolith" across the cluster
- Old-AI-generated smells: `dfableandopus/README.md`-only (no interview-questions/flashcards/etc. files) suggests this pass was left incomplete relative to its siblings
- Skill tags: be-node-express, fe-react, orm, be-async-jobs, db-transactions, design-docs-adrs
- Duplicate/overlap: same cluster pipeline; unique domain (inventory/fulfillment) and unique architecture (non-apps/packages layout)
- Learning value: Medium — useful as a *contrast* case for "modular monolith without a monorepo tool" architecture discussion
- Proposed disposition: C SPECIALIZED — keep for the architectural contrast; dfableandopus/ layer is incomplete here versus siblings.

## Master7 LMS (v2)

- Path: master7
- Origin: ORIGINAL/COURSE — Type: monorepo (apps: api, web, worker; packages: config, contracts, database, domain, test-utils)
- State: working-looking, most mature LMS snapshot — Size: 95 files — Last modified: Sep 17 2026 (README)
- Purpose: Enterprise LMS/certification platform — same `@lms/api`/`@lms/web` codebase lineage as "master 6" (confirmed via `apps/api/package.json` and `apps/web/package.json` names being identical), but a later, more-implemented snapshot: README states "current feature trail is complete through feature 07" with a `docs/HIGH_REASONING_REMEDIATION_JOURNAL.md` and an `npm run verify` script running "Prisma schema validation, TypeScript build mode, Vitest tests, and production builds."
- Stack: same as master6 (Node workspaces, Prisma-based per docker-compose, Vite web client) plus explicit `npm run verify` CI-like gate
- Architecture: modular monolith, 8-package workspace matching master1/master7's naming convention
- Complexity: Mid
- Educational material: EXCELLENT — `astraupskill/README.md` ("Master7: protect audit data in every response") is a genuinely sharp, specific lesson: an org admin dashboard leaked a *second*, unscoped read path of audit records even though the dedicated audit endpoint was already correctly scoped — the course explicitly clarifies the app currently runs on an in-memory store, not the Prisma DB, for these particular tests ("Keeping that distinction clear is part of learning to assess a codebase accurately" — a notably senior-level honesty point). `docs/features/01-07*.md`, `docs/CODEBASE_STRUCTURE_AND_SYSTEM_DESIGN.md`, `docs/code-walkthroughs/`.
- Quality observations:
  - `npm run verify` gate described in README (schema validation + typecheck + tests + build) — most CI-like of the cluster
  - 4 native test files found
  - `review` file present at root (16KB) — likely a prior review artifact, not deep-read (out of scope per brief)
- Old-AI-generated smells: none seen; the astraupskill lesson is a good example of catching a "second read path bypasses the authorization fix" class of bug
- Skill tags: be-node-express, authz-rbac, multitenancy, observability-logs, ci-cd, test-unit, security-owasp
- Duplicate/overlap: **direct duplicate/iteration of "master 6"** — same LMS codebase, master7 is the more-implemented/more-verified snapshot; treat the pair as one project with two curriculum snapshots rather than two separate projects
- Learning value: High — the "second read path leaks data despite the primary endpoint being fixed" lesson is a strong, realistic authorization-review teaching point (maps well to a real code-review interview scenario)
- Interview stories it could support: "caught a data-leak where a dashboard aggregation endpoint bypassed an already-fixed authorization check on a sibling endpoint" — a strong, concrete code-review story.
- Proposed disposition: B HIGH-VALUE — keep as the canonical/most-mature LMS snapshot; if consolidating with master6, master7 is the one to retain for the base codebase (master6 retained only for its extra dfableandopus/ layer).

## (empty) master 5 / master555

- Path: "master 5", master555 — Origin: n/a — Type: empty directories (confirmed via `ls -la`, zero entries beyond `.`/`..`)
- One-line record: both are completely empty placeholder folders; no files, no git repo. Proposed disposition: G ARCHIVE (delete-candidate, nothing to preserve).

---

## Cal.com clone

- Path: mastercal\cal.diy
- Origin: OPEN-SOURCE CLONE (Cal.com scheduling platform, cloned as "cal.diy") — Type: monorepo
- State: complete (real production OSS codebase) — Size: large (22 top-level dirs incl. `.changeset`, `.claude`, `.cursor`) — Last modified: curriculum mtime 2026-07-09 (per memory: mastercal-upskill-curriculum.md)
- Purpose: Cal.com/cal.diy — scheduling/booking SaaS. Real cloned app, not audited beyond top-level identity check per brief (do-not-deep-read rule for huge OSS clones).
- Stack: Next.js/tRPC/Prisma monorepo (per prior memory notes; Yarn/Turbo)
- Educational material: STRONG — `mastercal/cal.diy/fabledocs/upskill/` (53 files). Per user memory (already-verified project-specific quality): PBAC stub-returns-true, slot-reservation TOCTOU, and post-commit-effects outbox gap flagged as top teaching seams.
- Skill tags: fe-next, be-rest-design or be-graphql-trpc, db-postgres, orm, authz-rbac, db-concurrency, outbox
- Duplicate/overlap: none within this batch
- Learning value: High (per memory) — concurrency/authorization teaching seams in a real production codebase
- Proposed disposition: D REFERENCE — large real OSS codebase with an established, previously-verified curriculum; not re-deep-read this pass, no changes found since last review.

## Dify clone

- Path: masterdidy\dify
- Origin: OPEN-SOURCE CLONE (Dify LLM app platform) — Type: monorepo
- State: complete — Size: large (21 top-level dirs)
- Purpose: LLM application-building platform (per memory: masterdidy-upskill-curriculum.md — "no git commits" note holds true here too — confirmed zero commits).
- Stack: Next.js frontend + Python backend (per memory notes); `masterdidy/dify/fable docs/upskill/` (53 files) + `user-stories.md` at curriculum root.
- Educational material: STRONG — per memory, "graphon engine is external dep" flagged as a scoping note.
- Skill tags: fe-next, be-python, ai-llm-integration, db-postgres, orm
- Duplicate/overlap: none within this batch
- Learning value: Medium-High (per memory)
- Proposed disposition: D REFERENCE.

## Dub clone

- Path: masterdub\dub
- Origin: OPEN-SOURCE CLONE (Dub link-shortener/analytics) — Type: monorepo
- State: complete — Size: large but flat at top level (5 dirs — `apps/` monorepo layout)
- Purpose: Link shortener + click analytics SaaS.
- Stack: Next.js/Turborepo/Prisma (per memory: masterdub-upskill-curriculum.md)
- Educational material: STRONG — `masterdub/dub/fable docs/upskill/` (53 files), previously reviewed by user's own Astra fix-pass project (per memory, this project is explicitly named in the fablereview-astra-audit history — i.e. this curriculum may already have gone through a quality fix pass).
- Skill tags: fe-next, be-rest-design, db-postgres, orm, caching, db-indexes-perf
- Duplicate/overlap: none within this batch
- Learning value: High
- Proposed disposition: D REFERENCE.

## Infisical clone

- Path: masterfinisc\infisical
- Origin: OPEN-SOURCE CLONE (Infisical secrets management) — Type: monorepo
- State: complete — Size: large (18 top-level dirs)
- Purpose: Secrets/credentials management platform — projects/environments/folders, machine-fetched secrets at runtime. Evidence: `masterfinisc/infisical/fable-docs/README.md`.
- Stack: Fastify 4 API (`backend/`), PostgreSQL via Knex, BullMQ/Redis job queues, React 18 SPA (`frontend/`) with Vite/TanStack Router/React Query/Tailwind v4, CASL-based ABAC authorization — all cited with exact file paths in the curriculum
- Educational material: EXCELLENT, largest/most sophisticated curriculum template seen in this batch — `fable-docs/` (60 files across 9 numbered modules: codebase-cartography, stack-and-language-mastery, architecture-and-patterns, code-reading-gym, quality-engineering, contribution-practice, career-and-collaboration, interview-prep, reference — plus a `25-user-stories.md`). Read in full: `fable-docs/README.md` and `fable-docs/03-architecture-and-patterns/06-architecture-critique.md`. The critique doc is genuinely excellent: names concrete confirmed risks with exact file/line citations (3,606-line `routes/index.ts` "wiring god-file", check-then-insert race in `secret-v2-bridge-service.ts:316-323`, no transactional outbox on job enqueue, error-contract-by-message-string, dual secrets engines coexisting, deprecated auth modes still live), separates "confirmed observations" from labeled "hypotheses," proposes prioritized fixes each with a test strategy and migration path, and ends with a "defend the opposite position" drill plus a self-grading rubric. This is publication-quality senior-engineer teaching content, not generic boilerplate.
- Skill tags: be-node-express, be-rest-design, db-postgres, db-concurrency, db-migrations, orm, authz-rbac, queues, outbox, security-owasp, code-review, design-docs-adrs
- Duplicate/overlap: none within this batch; not previously in the user's own memory index (new finding this audit)
- Learning value: Very High — best single curriculum artifact found in the open-source-clone half of this batch; concrete race-condition and reliability-gap teaching seams
- Transformation opportunity: The `06-architecture-critique.md` + `08-interview-prep/` pairing is strong enough to lift as a template for retrofitting curricula onto the other, older-template clones (mastercal/masterdub/masterform/masterhop/masterlink/mastermayan/masterdidy all use the thinner 53-file `upskill/` format).
- Interview stories it could support: system-design critique of a real secrets-manager (race conditions, outbox pattern, auth-contract fragility), "what would you fix in your first 3 months owning this."
- Proposed disposition: C SPECIALIZED — treat as the reference template for what a top-tier curriculum in this style should look like; strong enough to consider A/B-tier promotion if the audit criteria weight curriculum quality heavily.

## Flagsmith clone

- Path: masterflag\flagsmith
- Origin: OPEN-SOURCE CLONE (Flagsmith feature-flag platform) — Type: monorepo
- State: complete — Size: large (13 top-level dirs)
- Purpose: Feature-flag/remote-config/A-B-testing platform.
- Stack: Django/DRF API (`api/`), React 19 + TypeScript dashboard (`frontend/`), Docusaurus docs site. Evidence: `masterflag/flagsmith/fable docs/README.md`.
- Educational material: EXCELLENT — this curriculum has been **upgraded to the same newer 9-module template as Infisical's** (`00-fast-track.md` + `01-codebase-cartography/` … `09-reference/`), not the older flat 53-file `upskill/` format the memory index describes for most other clones in this batch. Explicitly frames the Python/Django backend as a *feature* for a Node-background learner ("Mid-level fullstack interviews test whether you understand API design, data modelling, authorization, and async reliability — concepts that live above the language"). Per prior memory (masterflag-upskill-curriculum.md), the older version of this curriculum flagged advisory-lock sequencing/split-authz/CSRF-off issues — this newer template supersedes that note; content should be treated as refreshed, not the same artifact previously reviewed.
- Skill tags: be-python (Django), fe-react, authz-rbac, caching, realtime-ws (SSE flag streams), multitenancy
- Duplicate/overlap: none within this batch
- Learning value: High — one of only two clones (with masteridur) upgraded to the newer, richer curriculum template
- Proposed disposition: C SPECIALIZED — flag for consistency review: this project was rebuilt with the newer template after its original memory entry, worth confirming which version is canonical before further edits.

## Formbricks clone

- Path: masterform\formbricks
- Origin: OPEN-SOURCE CLONE (Formbricks survey/forms platform) — Type: monorepo
- State: complete — Size: large (18 top-level dirs)
- Purpose: Open-source survey/form platform.
- Stack: Next.js/Prisma/Redis, Preact widget SDK (per memory: masterform-upskill-curriculum.md)
- Educational material: STRONG — `masterform/formbricks/fabledocs/upskill/` (53 files, older template). Per memory: fire-and-forget pipeline (no outbox), quota-count race, fail-open rate limiting flagged as top seams.
- Skill tags: fe-next, be-rest-design, db-postgres, orm, caching, db-concurrency, outbox
- Duplicate/overlap: none within this batch
- Learning value: High (per memory)
- Proposed disposition: D REFERENCE.

## Hoppscotch clone

- Path: masterhop\hoppscotch
- Origin: OPEN-SOURCE CLONE (Hoppscotch API client) — Type: monorepo
- State: complete — Size: large but flat at top level (7 dirs)
- Purpose: Open-source API testing/client tool (Postman alternative).
- Stack: per memory notes (masterhop-upskill-curriculum.md) — docs-only curriculum, commands inferred, TOCTOU + in-memory pubsub flagged as top teaching seams
- Educational material: STRONG — `masterhop/hoppscotch/fabledocs/upskill/` (53 files, older template)
- Skill tags: fe-react-or-vue, realtime-ws, be-rest-design, arch-event-driven
- Duplicate/overlap: none within this batch
- Learning value: Medium-High (per memory)
- Proposed disposition: D REFERENCE.

## IDURAR ERP/CRM clone

- Path: masteridur\idurar-erp-crm
- Origin: OPEN-SOURCE CLONE (IDURAR open-source ERP/CRM) — Type: monorepo (backend + frontend, MERN)
- State: complete — Size: 8 top-level dirs (`backend/`, `frontend/`, etc.)
- Purpose: Invoicing/ERP/CRM system.
- Stack: MERN (Express/React/MongoDB), per memory (masteridur-upskill-curriculum.md): no tests, several confirmed defects used as teaching seams
- Educational material: EXCELLENT — like Flagsmith, this curriculum has been **upgraded to the newer 9-module `00-fast-track.md`+numbered-module template** (12 top-level entries in `masteridur/idurar-erp-crm/fable docs/`, matching Infisical's structure), superseding the older flat-53-file version described in memory.
- Skill tags: be-node-express, fe-react, db-mongo, orm (mongoose), be-error-handling
- Duplicate/overlap: none within this batch
- Learning value: High — MERN + Mongo stack is otherwise underrepresented in this batch (everything else leans Postgres/Prisma or Django), and the confirmed-defect teaching seams make it good debugging practice material
- Proposed disposition: C SPECIALIZED — flag for the same template-upgrade consistency review as Flagsmith; also the only Mongo-based clone in this batch, worth keeping for stack diversity.

## Indico clone

- Path: masterindicoPYJS\indico
- Origin: OPEN-SOURCE CLONE (Indico conference/event management) — Type: monolith
- State: complete OSS codebase, but **NO curriculum present** — Size: large (9 top-level dirs, real `requirements.txt`/`pyproject.toml`/`webpack.config.mjs`/`jest.config.js`)
- Purpose: Conference/event management platform.
- Stack: Python/Flask-style backend (`pyproject.toml`, `requirements.txt`, `.coveragerc`, `conftest.py`) + React/webpack JS frontend (`package.json`, `jest.config.js`, `tsconfig.json`)
- Educational material: **NONE** — exhaustive search (`find masterindicoPYJS -maxdepth 2 -iname "*fable*"` and directory listing) found no `fabledocs/`, `fable docs/`, or `upskill/` directory anywhere in this project, unlike every other clone in this batch. This is an anomaly relative to the batch pattern.
- Quality observations: real project with `pytest.ini`, `conftest.py`, `.coveragerc` (native test infra exists in the clone itself, just no generated curriculum layered on top)
- Skill tags: be-python, fe-react, test-unit
- Duplicate/overlap: none within this batch
- Learning value: Low as-is (no curriculum layer) — Medium if a curriculum were generated for it, since it's currently the only clone without one
- Transformation opportunity: Candidate to run the same fabledocs-generation pipeline used on its 11 siblings, ideally using the newer Infisical/Flagsmith-style 9-module template rather than the older 53-file one.
- Proposed disposition: G ARCHIVE (as-is) — no differentiated content beyond the raw clone; either generate a curriculum for it or drop it, since an un-curated open-source clone with no other modification adds little to the portfolio.

## Linkwarden clone

- Path: masterlink\linkwarden
- Origin: OPEN-SOURCE CLONE (Linkwarden bookmark manager) — Type: monorepo
- State: complete — Size: 10 top-level dirs
- Purpose: Self-hosted bookmark/link archiving manager.
- Stack: Next.js/Prisma (per memory: masterlink-upskill-curriculum.md)
- Educational material: STRONG — `masterlink/linkwarden/fabledocs/upskill/` (53 files, older template)
- Skill tags: fe-next, be-rest-design, db-postgres, orm
- Duplicate/overlap: none within this batch
- Learning value: Medium-High (per memory)
- Proposed disposition: D REFERENCE.

## Mattermost clone

- Path: mastermatter\mattermost
- Origin: OPEN-SOURCE CLONE (Mattermost team chat, Go + React) — Type: monorepo
- State: complete — Size: large (11 top-level dirs incl. `server/`, `webapp/`, `api/`, `e2e-tests/`)
- Purpose: Self-hosted Slack-alternative team chat platform.
- Stack: Go server (`server/`), React webapp (`webapp/`), sizeable `e2e-tests/`. Note: this project has an `AGENTS.md`, `.agents/`, `.cursor/`, `skills-lock.json`, `enable-claude-docs.sh` at its root — the original Mattermost repo itself ships AI-tooling config; not something added by this audit's pipeline.
- Educational material: USEFUL, **not in the standard fabledocs/upskill format** — curriculum lives in a **sibling directory** `mastermatter/astraupskill/` (12 files: same 7-chapter CRUD-repair format as the master1-7 cluster, i.e. this is an Astra-style lesson, not a fabledocs-style broad curriculum). Read in full: `astraupskill/README.md` — "Channel update row counts: a CRUD boundary lesson." Excellent, Go-specific, and precise: traces `SqlChannelStore.Update` in `server/channels/store/sqlstore/channel_store.go`, explains a real defect (SQL `UPDATE` affecting zero rows was treated as success, letting a nonexistent-channel update fall through into downstream `PublicChannels` propagation instead of returning not-found), cites the exact snapshot (`snapshots/channel_store.go.original.txt`) and the focused regression test file, and is explicit about scope ("It is not a claim that all Mattermost channel writes are covered... The native Go test remains a separate follow-up").
- Skill tags: be-error-handling, db-sql-raw, db-transactions, legacy-codebase-reading, code-review
- Duplicate/overlap: unique — only Go-based codebase in this entire batch, and the only clone using the Astra CRUD-lesson format instead of the broad fabledocs format
- Learning value: High — rare Go-specific SQL-transaction/error-boundary lesson, good contrast to the batch's otherwise TS/Python-heavy content
- Interview stories it could support: "SQL UPDATE affecting zero rows silently treated as success — caught before it corrupted a public-channel propagation step"
- Proposed disposition: C SPECIALIZED — keep for Go/transactional-correctness teaching value and stack diversity; note it structurally differs from its siblings (astraupskill only, no fabledocs).

## Mayan EDMS clone

- Path: mastermayan\Mayan-EDMS
- Origin: OPEN-SOURCE CLONE (Mayan EDMS document management) — Type: monolith
- State: complete — Size: 12 top-level dirs
- Purpose: Document management/workflow system.
- Stack: Django + Celery, 57 apps (per memory: mastermayan-upskill-curriculum.md), not locally runnable in that prior review (commands inferred)
- Educational material: STRONG — `mastermayan/Mayan-EDMS/fabledocs/upskill/` (53 files, older template). Per memory: `pages_append_all` FieldError, `ignore_results` typo, change-type authz asymmetry, workflow-transition race flagged as top seams.
- Skill tags: be-python (Django), be-async-jobs, authz-rbac, db-concurrency
- Duplicate/overlap: none within this batch
- Learning value: Medium-High (per memory)
- Proposed disposition: D REFERENCE.

---

## Batch observations

- **Two distinct sub-portfolios in one batch.** The numbered `master`/`master1-7` directories are NOT open-source clones (despite the batch context suggesting that pattern) — they are ORIGINAL/COURSE fictional-SaaS codebases generated by the same pipeline that produced the user's own "Astra" curriculum-fix-pass project (named directly in the user's memory: fablereview-astra-audit.md). Every one of them ships a matching `astraupskill/` folder (7-chapter CRUD-repair lesson + README + VERIFICATION.md + evidence/ + snapshots/), and several also ship a `dfableandopus/` career-prep layer (interview questions, resume stories, flashcards, take-home, system-design follow-ups). This is a clear, repeated pipeline output, not organic project growth.
- **master6/master7 are the same codebase, twice.** Both are `@lms/api`/`@lms/web` (confirmed via `apps/*/package.json` name fields) — an Enterprise LMS/certification platform. master7 is the more-developed snapshot (verify script, remediation journal, 7 features built); master6 has a longer feature backlog (21 planned) but only the extra `dfableandopus/` layer distinguishes it. Recommend treating as one project with two curriculum artifacts rather than two independent portfolio pieces.
- **master1 (GlobalWork EOR) is a clear standout** — 47 numbered feature docs, 20 code-walkthrough docs, Testcontainers-based integration testing, and topics (outbox pattern, worker retry policies, payroll locking under concurrency) that are meaningfully more senior than its five siblings. Recommend as this batch's flagship.
- **Curriculum template has visibly evolved.** Most open-source-clone curricula use an older flat `fabledocs/upskill/` (or `"fable docs"/upskill/`) format with exactly 53 files. Two clones — masterflag (Flagsmith) and masteridur (IDURAR) — have been rebuilt with a materially richer 9-module template (`00-fast-track.md` → `09-reference/`, with an explicit "architecture critique" doc, self-grading rubrics, "defend the opposite position" drills). masterfinisc (Infisical) — not previously tracked in the user's memory at all — uses this same newer template and is, on direct reading, the single best curriculum artifact in the batch. This suggests an active, still-in-progress upgrade pass across the clone curricula; the other 8 older-template clones (cal.diy, dify, dub, formbricks, hoppscotch, linkwarden, Mayan-EDMS, and — differently — mattermost) have not yet received it.
- **Two real gaps found.** `masterindicoPYJS/indico` has a real, substantial OSS clone but genuinely no curriculum anywhere in the directory tree — the only clone in the batch missing one entirely. `mastermatter/mattermost` (Go) has curriculum but in the different, narrower Astra-lesson format rather than the broad fabledocs format its siblings use, and it's the only Go-language project in the batch.
- **No project in this batch has real git history.** Every clone and every master*-cluster repo is `git init`-ed with zero commits; all dating in this report relies on file mtimes, which is a weaker signal than commit history (noted per-project above where relevant).
- **Stack diversity note:** the 12 open-source clones together cover Next.js/Prisma (cal.diy, dub, formbricks, linkwarden — 4 of 12, the dominant pattern), Django/Python (dify partial, flagsmith, Mayan-EDMS, indico — 4 of 12), MERN/Mongo (idurar — the only Mongo instance), Fastify/Knex (infisical), and Go (mattermost — the only Go instance). The master1-7 cluster is uniformly Node/TS (NestJS or Express) + Prisma + Postgres, so Mongo (idurar) and Go (mattermost) are this batch's only genuine stack outliers and worth preserving for that diversity alone.
