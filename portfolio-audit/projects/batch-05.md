# Batch 05 — Desktop apps B
Scope: C:\Users\Owner\Desktop\{campusops, devdeck, finance-dashboard, formforge, globehire, meterforge, missioncontrol, masternocu, masteroutline, spacegame, spacegamev2, astraspacegameweb, skillforgejs, union-alpha-playground, unionboot, AlanAndEliSoccer, resume}  |  Candidate dirs inspected: 17  |  Meaningful projects: 14  |  Tiny/empty/boilerplate: 3

| Project | Path | Type | Origin | Stack | Complexity | Docs | Disp |
|---|---|---|---|---|---|---|---|
| CampusOps | campusops | monolith API + SPA (C#/.NET) | COURSE/GENERATED | .NET 10, React/TS, SQLite | Mid | STRONG (astraupskill, 8 files) | B |
| FormForge | formforge | monorepo(2: Fastify API + React) | COURSE/GENERATED | React/TS, Vite, Fastify, pnpm/turbo | Mid | STRONG (astraupskill, 8 files) | B |
| GlobeHire | globehire | modular monolith API (C#/.NET) | COURSE/GENERATED | .NET 10, in-memory persistence | Mid+ | STRONG (astraupskill, 8 files) | B |
| MeterForge | meterforge | modular monolith API (C#/.NET) | COURSE/GENERATED | .NET 10, PostgreSQL, Docker | Mid+ | STRONG (astraupskill, 7 files) | B |
| MissionControl (Fleet Command .NET) | missioncontrol | modular monolith API (C#/.NET) | OPEN-SOURCE CLONE (recreation of builderz-labs/mission-control) | .NET 10, EF Core, SQLite, SSE | Mid+ | STRONG (astraupskill, 8 files) | B |
| DevDeck | devdeck | web app (PWA) | ORIGINAL + COURSE overlay | React/TS, Vite, IndexedDB(Dexie-like) | Junior+ | STRONG (astraupskill, 9 files) | C |
| Finance Dashboard | finance-dashboard | web app (single-page, vanilla) | ORIGINAL + COURSE overlay | vanilla JS, HTML, CSS, localStorage | Junior | USEFUL (astraupskill, 9 files) | C |
| Skillforge | skillforgejs | web app (learning platform) | ORIGINAL + COURSE overlay | Next.js, Prisma, SQLite, C# runner | Mid | STRONG (astraupskill, evidence+snapshots) | C |
| NocoBase (masternocu) | masternocu/nocobase | monorepo (no-code platform, real OSS) | OPEN-SOURCE CLONE (actual fork) | Node/TS, React, multiple DBs, plugins | Senior-oriented (as-is OSS) | STRONG (fabledocs, 10 sections) | D |
| Outline (masteroutline) | masteroutline/outline | monorepo (wiki/knowledge base, real OSS) | OPEN-SOURCE CLONE (actual fork) | Koa, Sequelize, React, Yjs/Hocuspocus | Senior-oriented (as-is OSS) | EXCELLENT (fabledocs 1-4, 80 files: onboarding+ADRs+practice pack) | A |
| Warband (spacegame v1) | spacegame | monorepo(2: Expo mobile + Fastify server) | ORIGINAL | Expo/RN, Fastify, Postgres/Prisma, BullMQ, Redis, Socket.io | Mid+ | NONE seen in this dir | F |
| Warband v2 (spacegamev2) | spacegamev2/spacegamev2 | monorepo(2: Expo mobile + server) | ORIGINAL (rebuild of v1) | Expo/RN, Node/TS, turbo | Mid+ | STRONG (fabledocs 1-4: postmortem, spec, product docs, session reports) | C |
| Warband — The Crownlands (astraspacegameweb) | astraspacegameweb | monorepo(2: web + server) | ORIGINAL (browser rewrite of v1/v2) | React web, Node/TS server, Postgres, Redis, Docker, Caddy, Prometheus/Grafana/Tempo | Mid+/Senior-oriented (ops tooling) | USEFUL (docs/, ADRs, runbooks) | B |
| Union Alpha playground | union-alpha-playground | CLI scripts | ORIGINAL | Node (no deps), OpenRouter API | Tiny | NONE | G |
| Unionboot | unionboot | exercise pack | COURSE/GENERATED | JS/TS/React/C#/ASP.NET/SQL | Junior→Mid (graduated) | EXCELLENT (fabledocs spec+plan, ~24k exercise files, verified) | A |
| AlanAndEliSoccer (soccer-laws-app) | AlanAndEliSoccer/soccer-laws-app | web app (Next.js) | ORIGINAL | Next.js, TS, Tailwind | Junior+ | MINIMAL (docs/FEATURE_EXPANSION.md) | C |
| Resume materials | resume | docs-only | ORIGINAL | Markdown | Tiny | N/A (content itself is the artifact, not curriculum) | G |

## CampusOps
- Path: campusops   - Origin: COURSE/GENERATED (fictional university facilities platform teaching repo)
- Type: monolith API (C#/.NET) + React/TS console, monorepo(2)
- State: complete-looking (15-sprint course claims completion)   - Size: 167 files   - Last modified: 2026-07-15 (32 commits)
- Purpose: Teaches CRUD/business-logic ownership through a fictional university facilities/work-order platform (locations, assets, requests, work orders, technicians, procurement).
- Stack: FE React/TS console (web/CampusOps.Web) | BE .NET 10 (Api/Core/Infrastructure/Worker/Contracts) | DB in-memory + SQLite | Test xUnit-style (3 test projects) | Infra none seen
- Architecture: modular monolith (module boundaries without network calls), scheduled worker for maintenance/delivery
- Complexity: Mid
- Educational material: STRONG — campusops/astraupskill/ (00-07 numbered guide: codebase map, concepts, worked change, testing/debugging, practice, solutions, trace lab) + snapshots/ (before/after source diffs) + VERIFICATION.md; project-specific, not generic
- Quality observations:
  - Explicit layered architecture documented in README with dependency direction stated
  - astraupskill/snapshots gives concrete before/after code for a worked repair (ConcurrentReservationTests, PartEndpoints, Program) — evidence of a deliberately planted-and-fixed concurrency bug
  - Separate test projects per layer (Api/Core/Infrastructure) suggest layer-appropriate testing
  - `dotnet restore --locked-mode` implies pinned/locked dependency graph
- Old-AI-generated smells: none seen beyond typical course scaffolding
- Skill tags: be-dotnet, db-sqlite, arch-modular-monolith, test-unit, test-integration, db-concurrency, be-async-jobs, fe-react, ts-types, design-docs-adrs
- Duplicate/overlap: sibling of formforge/globehire/meterforge/missioncontrol/devdeck/finance-dashboard/skillforgejs — all share the identical `astraupskill/` 8-file curriculum scaffold (00-07 + README + VERIFICATION), evidently a repeatable Astra course template applied to different domains
- Learning value: High — concurrency bug (worked repair) is a strong interview story, plus clean modular-monolith example
- Interview stories it could support: "found and fixed a race condition in a reservation flow using a worked before/after diff", "designed module boundaries in a monolith without premature microservices"
- Proposed disposition: B HIGH-VALUE — solid mid-level teaching repo with a genuinely worked concurrency fix; keep as reference/portfolio piece, curriculum reusable

## FormForge
- Path: formforge   - Origin: COURSE/GENERATED (mid-level CRUD/forms course)
- Type: monorepo(2: React/TS form-builder SPA + Fastify API), pnpm/turbo workspace
- State: working-looking, explicitly notes an unfinished boundary (browser not yet wired to persisted API — "guided integration capstone" left as exercise)   - Size: 178 files   - Last modified: 2026-07-14 (17 commits)
- Purpose: Schema-driven form builder + response analytics teaching workspace (7 field types, validation, conditional logic, branching, autosave, publishing, CSV export, analytics, diffs, accessibility checks).
- Stack: FE React/TS + Vite | BE Fastify (separately implemented/tested) | DB none (fixture data) | Test present (pnpm scripts reference an "evidence gate") | Infra pnpm/turbo monorepo
- Architecture: SPA + separate API, deliberately incomplete integration as a teaching seam
- Complexity: Mid
- Educational material: STRONG — formforge/astraupskill/ (00-PREREQS through 07-TRACE-LAB, labs/publication-trace.ts, VERIFICATION.md); explicitly calls out the fixture/API boundary as the course's teaching point
- Quality observations:
  - README is unusually candid about limitations ("browser is not yet a persisted end-to-end API client") — rare honesty vs. typical "everything works" AI-generated claims
  - `pnpm seed` prints a "deterministic fingerprint" — a verification-first pattern
  - Includes an executable trace lab (labs/publication-trace.ts) rather than just prose
- Old-AI-generated smells: none seen; the explicit incompleteness disclosure is the opposite of a typical AI-smell
- Skill tags: fe-react, fe-forms-validation, ts-types, be-node-express, be-validation, test-unit, fe-a11y
- Duplicate/overlap: same astraupskill template family as campusops/globehire/meterforge/missioncontrol/devdeck/finance-dashboard/skillforgejs
- Learning value: High — the deliberate FE/BE integration gap is a strong "identify the seam" exercise
- Interview stories: "built a schema-driven form builder with conditional branching and autosave", "designed an integration capstone connecting a fixture-backed SPA to a real API"
- Proposed disposition: B HIGH-VALUE — good forms/validation showcase with an unusually honest scope boundary

## GlobeHire
- Path: globehire   - Origin: COURSE/GENERATED (fictional employer-of-record platform, explicitly disclaims being a Pebl/Velocity Global copy)
- Type: modular monolith API (C#/.NET), no persisted DB yet (in-memory adapters)
- State: complete-looking (15 sprints)   - Size: 169 files   - Last modified: 2026-07-15 (76 commits — highest commit count in batch)   
- Purpose: Global workforce/EOR platform teaching repo: money/date/policy modeling, versioned API contracts, tenant-bound ports, idempotency, optimistic concurrency, outbox/webhook identities.
- Stack: BE .NET 10 (Api/Application/Contracts/Domain/Infrastructure) | DB in-memory teaching adapters | Test 4 test projects incl. GlobeHire.Architecture.Tests (NetArchTest-style) | Infra none
- Architecture: clean/hexagonal-leaning layered architecture, domain-centric with ports for persistence/time/identity/events
- Complexity: Mid+
- Educational material: STRONG — globehire/astraupskill/ (00-07 + evidence/ test run artifacts + snapshots/); FLAW-LEDGER.local.md documents 4+ deliberately planted bugs (fractional-cent money allocation drift, inclusive/exclusive date boundary bug, tenant-unscoped IDOR, concurrent-approval race) with sprint-numbered plant/harvest points
- Quality observations:
  - GlobeHire.Architecture.Tests project enforces layering rules in code, not just docs
  - FLAW-LEDGER.local.md is a strong artifact: explicit security (IDOR) and correctness (money rounding, date-boundary, concurrency) bugs planted and later harvested with tests — genuine security-minded teaching design
  - 76 commits (vs ~17-32 for siblings) suggests the most iteratively built/reviewed of the .NET course repos
  - evidence/ directory holds actual test run logs, not just claims
- Old-AI-generated smells: none seen — the flaw ledger is the opposite pattern (deliberately-planted, tracked bugs rather than accidental hallucinated ones)
- Skill tags: be-dotnet, arch-clean-hex, authz-rbac, multitenancy, idempotency, db-concurrency, security-owasp, outbox, backcompat-versioning, test-unit, test-integration
- Duplicate/overlap: astraupskill template family (see CampusOps); domain-wise adjacent to missioncontrol/meterforge (all SaaS/ops platforms)
- Learning value: Very High — IDOR + money-rounding + concurrency bugs are excellent, concrete interview stories with test evidence
- Transformation opportunity: Extract the FLAW-LEDGER pattern (plant-then-harvest bugs with tests) as a standalone "bug-hunting" interview-prep exercise set, reusable across other repos
- Interview stories: "found and fixed a cross-tenant IDOR via a resource lookup missing tenant scope", "fixed a fractional-cent money-allocation drift bug", "resolved a concurrent-approval race with optimistic concurrency"
- Proposed disposition: A FLAGSHIP — most security/concurrency-rich of the .NET course repos, strong interview material, highest commit iteration count

## MeterForge
- Path: meterforge   - Origin: COURSE/GENERATED (fictional multi-tenant usage-based billing platform, explicitly disclaims being Stripe/a real payment processor)
- Type: modular monolith API (C#/.NET) with PostgreSQL
- State: complete-looking (15 sprints)   - Size: 137 files   - Last modified: 2026-07-15 (68 commits)
- Purpose: Usage-based subscription billing teaching repo: money/subscriptions/invoices/credits/refunds/entitlements, PostgreSQL persistence, external provider integration ports.
- Stack: BE .NET 10 (Api/Application/Contracts/Domain/Infrastructure) | DB PostgreSQL (docker-compose.yml present) | Test 4 test projects incl. Architecture.Tests | Infra Docker
- Architecture: clean/hexagonal layering, outbox/webhook delivery pattern, idempotency-key + If-Match headers
- Complexity: Mid+
- Educational material: STRONG — meterforge/astraupskill/ (00-07 style, no snapshots dir but full set); FLAW-LEDGER.local.md lists 5 planted bugs (tenant-missing dedup key, tier-boundary double-counting, mutable finalized invoice lines, non-atomic version check+mutation, retry generating new idempotency key) all harvested in "Sprint 14"
- Quality observations:
  - Real PostgreSQL via docker-compose (not just in-memory), a step up in realism from GlobeHire
  - Idempotency-Key / If-Match / Problem Details are named explicitly in the README — real REST API design vocabulary, not generic CRUD
  - FLAW-LEDGER's 5 bugs are all classic billing-system failure modes (double counting, non-atomic optimistic concurrency, idempotency-key reuse under retry) — genuinely instructive
- Old-AI-generated smells: none seen
- Skill tags: be-dotnet, db-postgres, idempotency, outbox, db-concurrency, be-validation, backcompat-versioning, docker, security-owasp
- Duplicate/overlap: astraupskill template family; domain-adjacent to GlobeHire (both money/billing-flavored) and MissionControl/CampusOps
- Learning value: Very High — idempotency-under-retry and tier-boundary bugs are excellent senior-leaning interview stories
- Interview stories: "diagnosed a billing double-charge caused by a retry generating a fresh idempotency key", "fixed a non-atomic optimistic-concurrency check causing lost subscription updates"
- Proposed disposition: A FLAGSHIP — real Postgres + idempotency/outbox patterns + a strong planted-bug ledger make this one of the most production-realistic .NET teaching repos in the batch

## MissionControl (Fleet Command .NET)
- Path: missioncontrol   - Origin: OPEN-SOURCE CLONE — explicit C#/.NET recreation of `builderz-labs/mission-control` per a written technical spec (not disclaimed as fictional; it's a real ported product)
- Type: single-process modular monolith API (ASP.NET Core) — "self-hosted control plane for fleets of AI agents"
- State: partial (README states "Phases 1-4 of 8 implemented")   - Size: 115 files   - Last modified: 2026-07-17 (only 2 commits — least-iterated repo in the C#/.NET group)
- Purpose: Recreates an AI-agent fleet orchestration control plane (task dispatch, quality gates, scheduling, webhooks, SSE events) in C#/.NET instead of the original stack.
- Stack: BE .NET 10, EF Core + SQLite (WAL pragmas, snake_case, migrations) | Auth session cookies (PBKDF2 600k) + API keys + RBAC (Viewer/Operator/Admin) | Realtime SSE via Channels event bus | Test 2 test projects (ApiTests, UnitTests) | Infra none
- Architecture: single-process monolith with an internal event bus, orchestration state machine, and a background scheduler (6 jobs)
- Complexity: Mid+
- Educational material: STRONG — missioncontrol/astraupskill/ (00-07 style + evidence/ with .trx test run files + source-hash verification JSON + snapshots/); this is the most "evidence-heavy" astraupskill folder in the batch (actual .trx test result files, not just logs)
- Quality observations:
  - PBKDF2 600k-iteration password hashing and CSRF origin checks called out explicitly — above-average auth hygiene for a teaching repo
  - Only 2 commits vs. siblings' 17-76 — likely the newest/least-refined of the group, or a single large import commit; worth flagging as needing a closer look
  - Declares itself only 4/8 phases complete — an honest partial-completion disclosure
  - evidence/ has real .trx (VSTest) result files with machine/timestamp names — genuine test execution evidence, not fabricated
- Old-AI-generated smells: none confirmed, but the low commit count (2) relative to siblings (17-76) suggests it may be a single bulk-generated drop rather than iteratively built/reviewed — flag for closer inspection
- Skill tags: be-dotnet, db-sqlite, authn, authz-rbac, realtime-ws, observability-logs, arch-event-driven, queues, agentic-engineering
- Duplicate/overlap: astraupskill template family; conceptually distinct (agent-orchestration domain, not business CRUD) from the other five .NET repos
- Learning value: High — SSE event bus + auth pipeline (PBKDF2, API keys, RBAC) + scheduler design are strong mid/senior interview material, but incomplete-phase status and low commit count warrant verification before relying on it
- Interview stories: "implemented a multi-tier API-key + session-cookie auth pipeline with RBAC", "built an SSE event bus with backpressure (drop-oldest 10k)"
- Proposed disposition: B HIGH-VALUE — strong auth/eventing design, but flagged NEEDS DEEPER INSPECTION on completeness given the 2-commit history and stated 4/8-phase status

## DevDeck
- Path: devdeck   - Origin: ORIGINAL product with a COURSE (astraupskill) overlay
- Type: web app (PWA, single app)
- State: working-looking (README claims full feature set; tests exist alongside source)   - Size: 146 files   - Last modified: 2026-07-18 (1 commit)
- Purpose: Spaced-repetition (SM-2, Anki-style) flashcard PWA for learning software-dev concepts (265 starter cards across 11 decks: JS, TS, React, Git, DSA, security, CSS).
- Stack: FE React/TS + Vite | State likely Zustand/local (store.ts) | DB IndexedDB (db.ts) | Test Vitest (scheduler.test.ts, queue.test.ts, app.integration.test.ts, importValidation.test.ts) | Infra none, offline-first PWA
- Architecture: client-only SPA, no backend; JSON import/export for backup
- Complexity: Junior+
- Educational material: STRONG — devdeck/astraupskill/ (01-07 + README + VERIFICATION.md, no 00-PREREQS or snapshots/evidence dirs); the app's *content* (265 flashcards) is itself educational material about JS/TS/React/DSA/security, distinct from the astraupskill meta-course about the app's own code
- Quality observations:
  - Real SM-2 spaced-repetition scheduling algorithm implemented and unit-tested (scheduler.test.ts) — non-trivial algorithm, not boilerplate CRUD
  - importValidation.ts + its test file suggest defensive handling of user-supplied JSON import (a common security/robustness teaching point)
  - Single commit despite substantial file count — likely imported/squashed rather than built incrementally in this repo
  - Offline-first PWA with local persistence only (no server, no auth) keeps scope appropriately small
- Old-AI-generated smells: single-commit history for a fairly complete app is a mild smell (no visible incremental history to inspect), but code structure (separate scheduler/queue/store/content modules) looks intentional, not boilerplate
- Skill tags: fe-react, ts-types, fe-state, test-unit, be-validation, desktop-electron-tauri (PWA, not exactly), fe-perf
- Duplicate/overlap: astraupskill template family (see CampusOps); content-wise overlaps with unionboot (both teach JS/TS/React/DSA fundamentals, different delivery format — flashcards vs. exercises)
- Learning value: Medium — good self-contained algorithm example (SM-2) for interview talk-tracks; less structurally complex than the .NET course repos
- Interview stories: "implemented Anki-style SM-2 spaced repetition scheduling with unit tests", "built an offline-first PWA with IndexedDB persistence and JSON import/export validation"
- Proposed disposition: C SPECIALIZED — good scheduler-algorithm and PWA-offline exercise source, but a smaller/less architecturally rich project than the .NET course group

## Finance Dashboard
- Path: finance-dashboard   - Origin: ORIGINAL product ("Eli & Elyn Finance Dashboard" — personal/family app) with a COURSE (astraupskill) overlay
- Type: web app (single static page, no build step)
- State: working-looking   - Size: 54 files   - Last modified: 2026-07-18 (1 commit)
- Purpose: Self-contained household finance dashboard (expenses, bills, savings goals, investments) for personal use, built as a teaching example of "form modes, stable identities and derived totals."
- Stack: FE vanilla JS + HTML + CSS (app.js, index.html, styles.css, no framework) | Charts inline | DB browser localStorage | Test test/browser.cjs, test/expense-edit.test.cjs | Infra none — "open index.html in a browser"
- Architecture: single-file client-only app, no build tooling, no backend
- Complexity: Junior
- Educational material: USEFUL — finance-dashboard/astraupskill/ (01-07 + README + VERIFICATION.md); README explicitly frames the course around "form modes, stable identities and derived totals" as the core teaching concepts
- Quality observations:
  - No framework/build step at all — deliberately minimal, good for "vanilla JS fundamentals" teaching rather than framework literacy
  - Has an actual reset-to-defaults button and localStorage persistence pattern — practical state-management example without a framework
  - Only 2 test files for a fairly feature-rich app (KPIs, budgets, bill calendar, goals, investments, charts, add-entry modal) — test coverage likely shallow relative to feature surface
  - dashboard-preview.png / dashboard-tall-preview.png suggest this was polished for presentation/portfolio use
- Old-AI-generated smells: single monolithic app.js (not split into modules) is typical of small vanilla-JS AI output; worth a closer read to confirm it isn't one giant file — NEEDS DEEPER INSPECTION on app.js size/structure
- Skill tags: fe-forms-validation, fe-state, test-unit, crud-basic
- Duplicate/overlap: astraupskill template family; domain-unique in this batch (personal finance)
- Learning value: Medium — good "no-framework state management" interview talking point, but simpler/smaller in scope than the .NET repos
- Interview stories: "built a client-only finance dashboard with derived/aggregated totals and stable list identities without a framework"
- Proposed disposition: C SPECIALIZED — decent vanilla-JS fundamentals example and personal-use artifact, smaller learning surface than the flagship repos

## Skillforge
- Path: skillforgejs   - Origin: ORIGINAL product (a boot.dev-style CRUD/C#/SQL learning trainer) with a COURSE (astraupskill) overlay
- Type: web app (Next.js)
- State: working-looking (has db:setup/seed/reset scripts, real Prisma+SQLite)   - Size: 5,570 files (includes node_modules-adjacent generated content — likely inflated by prisma/content generation; re-check with node_modules excluded if precise count matters)   - Last modified: 2026-09-11 (7 commits)
- Purpose: Local-only, single-learner gamified coding trainer (XP, streaks, quests, achievements) for CRUD web apps in C#/.NET/SQL, with a C# exercise runner.
- Stack: FE Next.js/React | BE Next.js server routes (src/server) | DB SQLite via Prisma | Runner separate .NET SDK-based C# exercise runner | Test tests/unit + tests/e2e (Playwright config present) | Infra none, fully local
- Architecture: modular Next.js app (app/components/features/lib/server/store separation), local SQLite persistence, external process invocation for C# exercise grading
- Complexity: Mid
- Educational material: STRONG — skillforgejs/astraupskill/ (01-07 + README + VERIFICATION.md + evidence/ + snapshots/), most recently modified of the astraupskill group (2026-09-11 vs. mid-July for the rest) — likely the most refined iteration of the template
- Quality observations:
  - Combines a real DB (Prisma/SQLite), a background-process C# runner, and e2e tests (Playwright) — the most technically diverse of the "original product + course" trio (with DevDeck, Finance Dashboard)
  - Content is data-driven (content/ directory feeds db:seed) rather than hardcoded — a reasonable content-authoring pattern
  - Has both tests/unit and tests/e2e directories, plus astraupskill/evidence — stronger test-discipline signal than Finance Dashboard
- Old-AI-generated smells: none strongly indicated; would need a read of src/server for API validation patterns to confirm
- Skill tags: fe-next, ts-types, be-node-express, db-sqlite, orm, test-unit, test-e2e, gamification (not in vocab — using crud-basic, fe-state)
- Duplicate/overlap: astraupskill template family; thematically overlaps with unionboot and devdeck (all are "learn to code" tools), but Skillforge is itself a learning *platform* rather than an exercise set
- Learning value: High — a real full-stack app (DB, seeding, background process invocation, e2e tests) built by the user's own tooling as a meta-example of the CRUD skills it teaches
- Interview stories: "built a gamified learning platform with Prisma/SQLite, spaced content seeding, and a sandboxed C# exercise runner invoked from Next.js API routes"
- Proposed disposition: C SPECIALIZED — solid full-stack Next.js/Prisma example and the most recently touched project in the batch; good portfolio candidate on its own merits, separate from its astraupskill content

## NocoBase (masternocu)
- Path: masternocu/nocobase   - Origin: OPEN-SOURCE CLONE — this is an actual clone/fork of the real NocoBase no-code platform (README.md, CHANGELOG, LICENSE-APACHE all present, multi-language READMEs), not a from-scratch recreation
- Type: monorepo (no-code app-building platform: server + multiple frontend packages + plugins)
- State: complete (it's the real upstream OSS project)   - Size: not counted in detail (large OSS monorepo with `packages/`, `plugins/`, `examples/`)   - Last modified: 2026-07-18 (1 commit in this local repo — i.e., a single import/vendoring commit, not original development history)
- Purpose: Real open-source no-code/low-code database & app builder (NocoBase). Not authored by the user; the user's contribution here is the fabledocs/ curriculum layered on top of the vendored codebase.
- Stack: FE React | BE Node/TS | DB multi-DB support (per upstream NocoBase) | Test upstream test suite (not run here) | Infra Docker, Lerna monorepo, Yarn
- Architecture: plugin-based modular monolith (per NocoBase's own architecture)
- Complexity: Senior-oriented as a codebase to read (large real-world OSS), though the curriculum targets junior/mid learning-to-read-legacy-code skills
- Educational material: STRONG — masternocu/nocobase/fabledocs/ (00-fast-track.md + 01-09 numbered directories + README) — a full "learn to read this codebase" curriculum (cartography, stack mastery, architecture/patterns, code-reading gym, quality engineering, contribution practice, career/collaboration, interview prep, reference) — this is a *reading/legacy-codebase* curriculum, distinct from the astraupskill "worked-change" format used elsewhere in the batch
- Quality observations:
  - This is real, production open-source code — not AI-generated — so "quality observations" in the AI-smell sense don't apply; the codebase's own maturity (Apache-licensed, i18n, plugin system, CI configs, AGENTS.md/CLAUDE.md already present upstream) is a given
  - Single local commit means no local development history to audit — it's a drop-in of the upstream source plus fabledocs
  - fabledocs/09-reference and 08-interview-prep folders (need directory listing to confirm depth) suggest interview-prep content specifically keyed to reading a real large codebase, which is valuable and different from writing new code
- Old-AI-generated smells: N/A — real human-authored OSS
- Skill tags: legacy-codebase-reading, code-review, fe-react, arch-modular-monolith, db-postgres, db-mongo, design-docs-adrs
- Duplicate/overlap: same fabledocs-cartography pattern as masteroutline (Outline clone) — both are "read a real OSS codebase" curricula; masteroutline's is more developed (4 fabledocs waves vs. 1 here)
- Learning value: High — legacy-codebase-reading skill is underrepresented elsewhere in the batch and highly relevant for mid/senior roles
- Interview stories: "navigated and explained the architecture of a real production no-code platform (NocoBase) using a self-authored codebase cartography"
- Proposed disposition: D REFERENCE — valuable as a legacy-code-reading exercise source, but it's vendored third-party code (not portfolio-worthy as "built by me"); keep fabledocs/, don't feature the vendored app itself as original work

## Outline (masteroutline)
- Path: masteroutline/outline   - Origin: OPEN-SOURCE CLONE — actual fork of the real Outline wiki/knowledge-base app (matches memory: prior review already covered this project in depth)
- Type: monorepo (Koa server + React app + CRDT collaboration server)
- State: complete (real upstream OSS)   - Size: large OSS monorepo (app/, server/, shared/, plugins/)   - Last modified: 2026-07-18
- Purpose: Real open-source team wiki/knowledge-base app (Outline). User's original contribution is the four-wave fabledocs curriculum layered on top.
- Stack: FE React + Vite | BE Koa + Sequelize | Realtime Yjs/Hocuspocus (CRDT collaboration) | DB Postgres (per upstream) | Infra Docker, Redis (per ADRs)
- Architecture: modular monolith with a CRDT-based realtime collaboration subsystem and Redis-backed horizontal scaling
- Complexity: Senior-oriented codebase; curriculum spans junior-to-senior
- Educational material: EXCELLENT — four full waves totaling ~80 files: fabledocs/ (53 files: fast-track + 9 numbered sections + README — cartography/stack/architecture/code-reading-gym/quality/contribution/career/interview-prep/reference), fabledocs2/ (7 files: architecture, API design, data access, testing, error handling, observability), fabledocs3/ (12 files: 10 numbered ADRs — modular-monolith service flags, 3-runtime layering, RPC-over-POST, policy authorization, Sequelize explicit transactions, event spine, CRDT triple-representation, Redis horizontal scale, error philosophy, integration-first testing — plus interview-translation.md), fabledocs4/ (8 files: fire drills, outbox-relay capstone, collab-harness capstone, SQL concurrency lab, frontend MobX lab, flashcards, four-week plan)
- Quality observations:
  - This is the deepest/most complete educational layering seen in the batch — matches the user's own memory note describing it as reverse-engineered ADRs + practice pack
  - ADR set (fabledocs3) documents real architectural decisions with interview-translation, a genuinely rare and valuable artifact for interview prep
  - fabledocs4 capstones (outbox-relay, collab-harness, SQL concurrency lab) are hands-on exercises built specifically against this real codebase's concurrency/collaboration seams
  - Codebase itself is real production OSS (not AI-generated), so architecture quality is inherently strong
- Old-AI-generated smells: N/A for the vendored app; the fabledocs curriculum content quality is user-verified per memory (2026-07-16 authored)
- Skill tags: legacy-codebase-reading, realtime-ws, db-postgres, db-transactions, arch-event-driven, outbox, db-concurrency, design-docs-adrs, code-review, fe-state
- Duplicate/overlap: same pattern as masternocu (both are "curriculum layered on a real OSS clone"), but this one is far more developed (80 files across 4 waves vs. 10 in masternocu)
- Learning value: Very High — richest interview-prep material in the entire batch (ADRs + interview-translation + capstones + fire drills + flashcards)
- Transformation opportunity: This fabledocs 1-4 pattern (cartography → ADRs/interview-translation → practice pack) is a template worth reusing on other real OSS clones in the archive (starting with masternocu, which only has wave 1)
- Interview stories: "reverse-engineered and defended 10 architectural decisions (CRDT triple-representation, Sequelize explicit transactions, Redis horizontal scale) in a real production wiki app", "built and debugged an outbox-relay capstone against a real event-spine implementation"
- Proposed disposition: A FLAGSHIP — the single strongest educational artifact in this batch; keep and treat as a template for future OSS-clone curricula

## Warband (spacegame v1)
- Path: spacegame   - Origin: ORIGINAL
- Type: monorepo(2: Expo/React Native mobile + Fastify server), packages/shared
- State: working-looking (has integration tests)   - Size: 372 files   - Last modified: 2026-07-18 (6 commits)
- Purpose: Server-authoritative Tribal Wars-style multiplayer strategy game — building/unit management, combat, community features — v1 of a game later rebuilt twice (see spacegamev2, astraspacegameweb).
- Stack: FE Expo/React Native (Expo Router, Zustand, TanStack Query, socket.io-client) | BE Node 22 + Fastify | DB PostgreSQL via Prisma | Queue BullMQ + Redis (every game timer) | Realtime Socket.io | Shared package (config/formulas/Zod schemas) | Test vitest (community.integration.test.ts, conquest.test.ts, integration.test.ts)
- Architecture: monorepo with a shared domain package imported by both client and server; static game config intentionally kept out of the DB (config-as-code pattern, explicitly documented)
- Complexity: Mid+
- Educational material: NONE seen in this directory (no astraupskill/fabledocs here — the curriculum for this game lineage lives in spacegamev2's fabledocs, which includes a "v1-postmortem" reviewing this very codebase)
- Quality observations:
  - "Static game config lives only in packages/shared/src/config — never in the DB" is a deliberate, documented architectural rule (config vs. data separation)
  - BullMQ + Redis used for every game timer — a real async-jobs/queue pattern, not trivial CRUD
  - Only 3 test files for a "5 design docs, single source of truth" scope — test coverage is thin relative to stated ambition
  - This version is explicitly superseded: spacegamev2/fabledocs2/01-v1-postmortem.md exists specifically to critique this codebase
- Old-AI-generated smells: superseded-and-rebuilt-twice pattern itself suggests v1 hit real limits (see postmortem in v2) — worth reading fabledocs2/01-v1-postmortem.md for specifics if pursuing this lineage further
- Skill tags: mobile-rn, be-node-express, db-postgres, orm, queues, realtime-ws, arch-modular-monolith
- Duplicate/overlap: DIRECT VERSION CHAIN with spacegamev2 (rebuild) and astraspacegameweb (browser rewrite) — all three are the same "Warband" Tribal-Wars-style game at different stages; v1 (this) → v2 (mobile rebuild, has a written postmortem of v1) → astraspacegameweb (browser-based "Crownlands" version, most operationally mature with Docker/Prometheus/Grafana/Tempo)
- Learning value: Medium standalone (superseded by v2/v3) but High in context as the "before" half of a documented rebuild story
- Interview stories: "shipped v1 of a server-authoritative game, then wrote a postmortem and rebuilt the timing/rules engine" (story spans this + spacegamev2)
- Proposed disposition: F CONSOLIDATE — do not treat as a standalone flagship; its value is almost entirely as the "v1" reference point for the postmortem in spacegamev2/fabledocs2; keep alongside v2/v3, not separately

## Warband v2 (spacegamev2)
- Path: spacegamev2/spacegamev2 (note: nested folder — spacegamev2/ contains a single subfolder spacegamev2/ with the actual repo)   - Origin: ORIGINAL (rebuild of spacegame v1)
- Type: monorepo(2: Expo mobile + server), packages/shared
- State: working-looking, with an explicit post-hoc review/upgrade cycle documented   - Size: 827 files   - Last modified: 2026-09-04 (11 commits)
- Purpose: Rebuild of the Warband Tribal-Wars-style game addressing v1's postmortem findings — rules engine, protocol/contracts, timing engine, realtime, world map, alliances, market/economy, security/anticheat.
- Stack: FE Expo/React Native | BE Node/TS server | packages/shared | Test vitest (army.test.ts, client.test.ts, session-races.test.ts, session.test.ts, socket.test.ts) | Infra turbo monorepo
- Architecture: same shared-package monorepo pattern as v1, expanded with explicit anticheat and session-race handling
- Complexity: Mid+
- Educational material: STRONG — fabledocs/ (2 files: anticheat, readme) + fabledocs2/ (18 files: 00-START-HERE through 18-build-order-and-curriculum — a full product+architecture spec: v1-postmortem, product spec, architecture, monorepo/tooling, rules engine, protocol/contracts, data model, timing engine, API/command pipeline, realtime/notifications, mobile client, world map, alliances/social, market/events/economy, security/anticheat, testing strategy, observability/operations, build-order curriculum) + fabledocs3/ (5 files: feature-ideas-research, live-ops-calendar, naming-review, pm-onboarding, roadmap-proposals — PM/product-flavored docs) + fabledocs4/ (5 files: session reports, project state, fix waves, open decisions, upgrade/ops)
- Quality observations:
  - reports/review-2026-09-04/ contains genuine verification evidence: live-smoke.ts + results JSON, server-probes.ts, redis-probe.ts, auth-outage-probe.ts, APP-REVIEW.md, and a large UPGRADE-REPORT.md with per-stage logs (typecheck, lint, export iOS/Android, regressions) — this is a real audited upgrade cycle, not just claims
  - session-races.test.ts specifically targets race conditions in game sessions — a deliberate concurrency-testing focus, consistent with a "learned from v1" rebuild
  - fabledocs2/15-security-and-anticheat.md + a dedicated anticheat.md in fabledocs/ show security was treated as a first-class design concern, not bolted on
  - fabledocs3 (PM-flavored: roadmap proposals, live-ops calendar, naming review) is a different register from the rest of the batch's curricula — product-thinking material, not just engineering
- Old-AI-generated smells: none seen; the review/upgrade evidence trail is unusually rigorous for this batch
- Skill tags: mobile-rn, realtime-ws, db-concurrency, security-owasp, arch-event-driven, queues, test-integration, ci-cd, observability-logs, design-docs-adrs
- Duplicate/overlap: version chain with spacegame (v1) and astraspacegameweb (browser rewrite); fabledocs2/01-v1-postmortem.md is the authoritative comparison document
- Learning value: Very High — the postmortem-driven rebuild, session-race testing, and audited upgrade cycle together form a strong "iterative hardening" narrative
- Transformation opportunity: The fabledocs2 18-file product+architecture spec is detailed enough to stand alone as a "how to spec a real-time multiplayer game" reference document, independent of this specific codebase
- Interview stories: "wrote a postmortem of a v1 game server, then redesigned the timing/rules engine and added anticheat + session-race tests in a v2 rebuild", "ran and documented a full upgrade verification cycle (typecheck/lint/export/smoke tests) with an audit report"
- Proposed disposition: B HIGH-VALUE — strong rebuild narrative and product+architecture spec; slightly overshadowed by astraspacegameweb as the most mature/operational version of this game lineage

## Warband — The Crownlands (astraspacegameweb)
- Path: astraspacegameweb   - Origin: ORIGINAL (browser-based rewrite/continuation of the spacegame lineage — game name changed to "The Crownlands")
- Type: monorepo(2: web SPA + server), full production-style infra
- State: complete/working-looking, most operationally mature of the three Warband versions   - Size: 2,673 files (largest in this batch)   - Last modified: 2026-09-08 (2 commits)
- Purpose: Persistent browser strategy game (construction, recruitment, scouting, battles, conquest, resource caravans, tribes, diplomacy, forums, PMs, rankings) — the browser-based successor to the Expo mobile versions.
- Stack: FE React web app (apps/web) | BE Node/TS server (apps/server) | DB Postgres | Cache/Queue Redis | Mail Mailpit (dev) | Auth JWT (access 15min, refresh 30-day rotating families, reuse-revokes-family) | Infra Docker Compose, Caddy (reverse proxy), Prometheus/Grafana/Tempo (full observability stack), chaos/ testing dir, benchmark.Dockerfile
- Architecture: production-style deployment topology (reverse proxy + metrics/tracing/dashboards + chaos testing), not just a dev-mode app
- Complexity: Mid+/Senior-oriented for the ops/infra layer specifically
- Educational material: USEFUL — docs/ (architecture.md, ADRs, npcs.md, spawning.md, production-work.md, final-improvements docs, verification.md, runbooks/) — operational/architecture documentation rather than a numbered learner curriculum like the other astraupskill/fabledocs sets
- Quality observations:
  - Refresh-token rotation with family-reuse-revocation is a real, correctly-described security pattern (detects token theft via reuse detection) — above the security sophistication seen in most of this batch
  - infra/chaos/ directory suggests deliberate chaos-testing practice — rare in this archive
  - Full observability stack (Prometheus + Grafana + Tempo + alerts.yaml) configured, not just mentioned — genuine attempt at production-grade operability
  - Only 2 commits for 2,673 files is a strong signal this was bulk-imported/squashed rather than built incrementally in this specific git history — NEEDS DEEPER INSPECTION if commit-by-commit history matters for portfolio narrative
  - docs/runbooks/ presence suggests on-call/incident-response thinking was included
- Old-AI-generated smells: the low commit count (2) for the largest file count in the batch is the main flag — can't verify iterative development from git history alone here; content itself (refresh-token rotation, chaos dir, full observability stack) reads as deliberately engineered rather than shallow
- Skill tags: authn, security-owasp, docker, observability-metrics-tracing, observability-logs, deploy, ci-cd, realtime-ws, db-postgres, caching, queues, incident-debugging
- Duplicate/overlap: final version in the version chain spacegame → spacegamev2 → astraspacegameweb; most production-realistic of the three
- Learning value: Very High — refresh-token rotation/reuse-detection and a real Prometheus/Grafana/Tempo/chaos-testing stack are senior-leaning, production-operations material rarely seen elsewhere in this archive
- Transformation opportunity: The auth (rotating refresh families + reuse detection) and observability stack (Prometheus/Grafana/Tempo/alerts + runbooks) are strong enough to extract as standalone reference implementations independent of the game domain
- Interview stories: "implemented refresh-token rotation with reuse detection to revoke a stolen token family", "stood up a full observability stack (metrics/tracing/dashboards/alerts) plus chaos-testing infra for a real-time multiplayer backend"
- Proposed disposition: B HIGH-VALUE — the most production/ops-mature version of the Warband lineage; verify the 2-commit history doesn't hide missing iteration story, but content quality is strong

## Union Alpha playground
- Path: union-alpha-playground   - Origin: ORIGINAL
- Type: CLI scripts (tiny)
- State: working-looking, trivially small   - Size: 5 files (chat.mjs, key.mjs, once.mjs, package.json, README.md)   - Last modified: not captured (1 commit, git log not separately queried — treat as ~mid-2026)
- Purpose: Dependency-free Node scripts for chatting with a free OpenRouter model (`stealth/union-alpha`) from VS Code tasks/launch configs.
- Stack: Node (no deps) | AI integration via OpenRouter API, key from env var
- Architecture: script-only, no framework
- Complexity: Tiny
- Educational material: NONE
- Quality observations: minimal by design — a personal utility script, not a teaching or portfolio artifact
- Old-AI-generated smells: none seen; appropriately small for its purpose
- Skill tags: ai-llm-integration
- Duplicate/overlap: none in this batch
- Learning value: Low — trivial utility
- Proposed disposition: G ARCHIVE — personal tool, not portfolio-relevant; keep for reference only

## Unionboot
- Path: unionboot   - Origin: COURSE/GENERATED (large, actively-expanding verified exercise pack — matches memory note "unionboot exercise pack")
- Type: exercise pack (not a runnable app)
- State: complete-and-growing (verification-report.json + multiple verify-*.cjs scripts, "expansion wave to ~5,400 in flight" per memory)   - Size: many thousands of files across categories (js-more 1,290; ts-next 6,027; react-next 2,897; dotnet-web-300 1,258; dotnet-web-more 1,264; sql-200 1,030; sql-more 954; react-300 1,215; mixed-data 673; ts-final 997; ts-more 2,527; js-rest 264; react-more 820; mixed-react 198; react-junior 156; js-capstones 24; js 84; ts 704; react 303)   - Last modified: 2026-09-22 (7 commits, most recent activity in the whole batch)
- Purpose: Massive graduated exercise library spanning JS, TypeScript, React, C#/ASP.NET Core, and SQL — "3,384 exercises" per START-HERE.txt at minimum-inventory count, with several additional expansion directories (js-more, ts-more, ts-next, react-next, etc.) beyond that baseline not yet folded into the official verification run.
- Stack: JS/TS/React exercises, standalone C# exercise files (E001-E1166), ASP.NET Core web exercises (W001-W300), SQL/database exercises (Q001-Q200)
- Architecture: N/A (flat exercise-file organization by category/difficulty tier)
- Complexity: Junior→Mid, graduated by directory (junior/more/next/300-tier naming suggests explicit difficulty progression)
- Educational material: EXCELLENT — unionboot/fabledocs/ (EXPLANATIONS-PLAN.md, EXPLANATIONS-SPEC.md) defines the meta-process for authoring/verifying exercises; SOLUTIONS.md + solutions/ directory; verification-report.json + 7+ verify-*.cjs scripts provide automated correctness checking across the whole pack, not just spot-checks
- Quality observations:
  - START-HERE.txt is explicit and precise about scope, ID ranges, and what is/isn't yet included in the official verification run — an honest, well-maintained index rather than an inflated claim
  - Multiple verify-*.cjs scripts (verify-23, verify-39-50, verify-all, verify-csharp, verify-csharp-more, verify-missing, verify-original, verify-round2-remaining) show iterative, incremental verification waves rather than a single unchecked bulk drop
  - "Families are revisited with policy changes" (per START-HERE.txt) — i.e., the larger directories are deliberate scenario variants of core patterns, not padding with unrelated one-offs
  - Most recently touched project in the entire batch (2026-09-22, today minus 1 day) — actively maintained
- Old-AI-generated smells: the sheer file count (tens of thousands across categories) makes uniform quality hard to verify without deeper sampling; the project's own verification tooling is the mitigating factor — NEEDS DEEPER INSPECTION only if auditing exercise-level quality specifically, not structurally
- Skill tags: ts-types, fe-react, be-node-express, be-dotnet, db-sql-raw, test-unit, crud-basic, db-postgres/db-sqlserver (SQL exercises, DB unspecified)
- Duplicate/overlap: thematically overlaps with devdeck (flashcards) and skillforgejs (learning platform) as "learn to code" material, but is far larger in scope and is the only one with automated per-exercise verification tooling
- Learning value: Very High — largest and most rigorously self-verified exercise corpus in the archive per memory and evidence here
- Transformation opportunity: could be curated into themed practice sets (e.g., a "SQL concurrency" or "React state" 20-exercise subset) for focused interview prep, given the verification tooling already exists to confirm correctness
- Interview stories: "authored and verified thousands of graduated coding exercises across 5 languages/stacks with automated correctness checking"
- Proposed disposition: A FLAGSHIP — largest, most actively maintained, most rigorously verified educational asset in this batch; core exercise-source project

## AlanAndEliSoccer (soccer-laws-app)
- Path: AlanAndEliSoccer/soccer-laws-app (note: AlanAndEliSoccer/ also has a standalone base.js utility script — a timeout/retry helper — separate from the Next.js app)   - Origin: ORIGINAL (family project, per name)
- Type: web app (Next.js)
- State: working-looking (dev-server.log/prod-server.log present, suggesting it was actually run)   - Size: not separately counted (subset of the ~dozens of files under soccer-laws-app; base.js is a single ~small utility)   - Last modified: 2026-07-18 (1 commit)
- Purpose: Educational Next.js app teaching the 17 Laws of Soccer plus World Cup tools (host explorer, group calculator, knockout planner) and match utilities (formation board, penalty tracker, referee notebook) — appears to be a personal/family (kids') learning project, not a professional portfolio piece by design.
- Stack: FE Next.js + TypeScript + Tailwind | No DB/backend indicated | Docs docs/FEATURE_EXPANSION.md
- Architecture: client-side Next.js app with route-per-feature (/, /laws/[lawNumber], /world-cup, /tools)
- Complexity: Junior+
- Educational material: MINIMAL — docs/FEATURE_EXPANSION.md described as containing "implementation notes, feature inventory, design choices, and junior-to-mid-senior engineering guidance" (single file; not verified in depth here)
- Quality observations:
  - Dynamic route `/laws/[lawNumber]` for 17 structured lesson pages is a reasonable, idiomatic Next.js pattern
  - README explicitly frames docs/FEATURE_EXPANSION.md as containing engineering guidance aimed at a junior-to-senior audience, suggesting the app doubles as a case study, not just a kids' app
  - dev-server.err.log / prod-server.log present at repo root (should arguably be gitignored) — minor hygiene issue
- Old-AI-generated smells: none strongly indicated from directory structure alone; the presence of committed log files is a minor smell (uncurated repo state)
- Skill tags: fe-next, ts-types, fe-a11y (formation/planner tools likely need it), crud-basic
- Duplicate/overlap: none in this batch
- Learning value: Medium — reasonable Next.js routing/composition example, personal-project scope
- Interview stories: "built a Next.js educational app with dynamic per-law lesson routes and several interactive calculator/planner tools"
- Proposed disposition: C SPECIALIZED — fine as a personal/family project and a light Next.js portfolio piece; not deep enough to be a flagship

## Resume materials
- Path: resume   - Origin: ORIGINAL (personal career documents, not software)
- Type: docs-only
- State: complete (content-focused, not code)   - Size: 33 top-level files (plus subfolders not enumerated)   - Last modified: 2026-07-18
- Purpose: Resume review notes and role-tailored resume/cover-letter variants (AI engineer, business analyst, cloud engineer, customer success engineer, data analyst/engineer, DevOps, implementation engineer, QA automation, SRE, solutions engineer, systems analyst, technical PM/writer, etc.) plus multiple reviewed resume versions (consulting-support, agentic-fullstack, dotnet-senior, IT support, Java/TypeScript, legacy-dev, IGT-dev).
- Stack: Markdown only
- Architecture: N/A
- Complexity: Tiny (not a software project)
- Educational material: N/A — this content is itself the deliverable (career material), not curriculum
- Quality observations: out of scope for engineering quality review; noted only for completeness per brief's "list all candidates" instruction
- Old-AI-generated smells: N/A
- Skill tags: (none — not a code artifact)
- Duplicate/overlap: none
- Learning value: Low (for engineering-skill purposes; separately high-value as career material, outside this audit's scope)
- Proposed disposition: G ARCHIVE — not a software project; out of scope for portfolio/skill audit, retain as personal career documents

## Batch observations
- **Astra course template cluster (7 projects):** campusops, formforge, globehire, meterforge, missioncontrol, devdeck, finance-dashboard, and skillforgejs all carry an identical `astraupskill/` scaffold (numbered 00/01-07 files + README + VERIFICATION.md, sometimes with `evidence/` and `snapshots/`). This confirms the "Astra" curriculum-generation pattern already noted in memory (fablereview-astra-audit.md) extends well beyond the 153 projects reviewed there — this batch alone has 7 more instances, plus a variant `fabledocs/` template (masternocu, masteroutline) for real-OSS-clone codebase-reading curricula.
- **Two distinct curriculum families:** (1) astraupskill = "worked-change" format for original/course-generated apps (codebase map → concepts → worked change → testing/debugging → practice → solutions → trace lab), consistently 7-9 files; (2) fabledocs = "codebase cartography" format for real open-source clones (cartography → stack mastery → architecture/patterns → code-reading gym → quality → contribution → career → interview-prep → reference), with masteroutline extending this into 4 full waves (fabledocs/2/3/4) including ADRs and capstones — by far the deepest single educational artifact in the batch.
- **Planted-bug ledgers as a strong, reusable pattern:** globehire and meterforge both ship `FLAW-LEDGER.local.md` files documenting deliberately planted-then-harvested bugs (IDOR, money-rounding drift, date-boundary bugs, non-atomic concurrency, idempotency-key regeneration under retry) tied to specific sprint numbers. This is a concrete, high-value interview-story generator and should be checked for in other Astra-family projects across the archive.
- **Warband version chain (3 projects, escalating maturity):** spacegame (v1, Expo/Fastify) → spacegamev2 (rebuild with a written v1-postmortem and audited upgrade cycle) → astraspacegameweb ("The Crownlands," browser-based, with Docker/Caddy/Prometheus/Grafana/Tempo/chaos-testing — the most production-realistic project in this entire batch). Should be presented together as a single "iterative rebuild" portfolio narrative rather than three separate entries; astraspacegameweb's refresh-token rotation and observability stack are standout, reusable reference implementations.
- **Real-OSS-clone-plus-curriculum pattern (2 projects):** masternocu (NocoBase) and masteroutline (Outline) both take an actual open-source codebase and layer a reading/onboarding curriculum on top rather than generating new code. masteroutline is far more developed (4 waves, ~80 files including 10 ADRs with interview-translation) than masternocu (1 wave, 10 files) — masternocu is a strong candidate to receive the same fabledocs2/3/4 treatment.
- **Low commit counts on large/complex repos are a recurring flag:** missioncontrol (115 files, 2 commits, explicitly only 4/8 phases done) and astraspacegameweb (2,673 files, 2 commits) both show minimal git history relative to their size/complexity, suggesting bulk import or squashed history rather than fully visible iterative development — worth a closer look if development-history narrative matters for interview prep.
- **Unionboot is the batch's (and possibly the archive's) largest single asset:** tens of thousands of files across JS/TS/React/C#/ASP.NET/SQL, with real automated verification tooling (multiple `verify-*.cjs` scripts + `verification-report.json`) and the most recent activity of any project in this batch (2026-09-22). It anchors the "E EXERCISE SOURCE"-adjacent flagship tier.
- **Gap:** no clear GraphQL, no message-queue-based event-driven microservices example distinct from monolith-plus-outbox patterns, and only shallow multi-tenancy coverage outside GlobeHire/MeterForge — the .NET course cluster otherwise covers SaaS-platform fundamentals (auth, RBAC, idempotency, outbox, optimistic concurrency) unusually well for a single batch.
