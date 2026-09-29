# Batch 04 — Desktop apps A
Scope: C:\Users\Owner\Desktop\{ankijs, aral, aral-deploy, tagalog, mobiletagalog, borrowbox, buildbusinesses, buildermentor, buildevent, buildreviewer, buildsmallplates, buildsql, buildwhiteboard, calendar+jobtrack, jobtrack, recipeview, recipeweb}  |  Candidate dirs inspected: 17  |  Meaningful projects: 15  |  Tiny/empty/boilerplate: 1 (aral-deploy is a deploy snapshot, not a project)

Note: `aral`, `tagalog`, `mobiletagalog`, `aral-deploy` are four DIFFERENT-GENERATION artifacts of the same "Aral — learn Tagalog" product idea, not duplicates of one codebase — see Batch observations for the lineage. `jobtrack` and `calendar+jobtrack` are two separate builds of a similar idea (personal calendar + job-search tracker) with real overlap.

| Project | Path | Type | Origin | Stack | Complexity | Docs | Disp |
|---|---|---|---|---|---|---|---|
| Recall (ankijs) | ankijs | web app (PWA) | ORIGINAL + curriculum overlay | React19/Vite8/Tailwind4, IndexedDB (fake-indexeddb for tests), Supabase (optional sync), Playwright+Vitest | Mid | STRONG (astraupskill/) | B |
| Aral v3 local-first | aral | monorepo(3 pkgs) | ORIGINAL + curriculum overlay | React PWA+Capacitor, Hono+tRPC v11+Drizzle/libsql, zod, Vitest | Mid+ | USEFUL (astraupskill/, docs/) | B |
| aral-deploy | aral-deploy | deploy snapshot | N/A | static JSON content bundle only | Tiny | NONE | G |
| Aral — Learn Tagalog | tagalog | monorepo(3 apps) | ORIGINAL + curriculum overlay | Next.js web, Expo mobile, Fastify API, PostgreSQL, pnpm/Turborepo | Mid+ | USEFUL (docs/, handoff/) | A |
| Aral Tagalog (mobile port) | mobiletagalog | mobile app | ORIGINAL (derived from tagalog) + curriculum overlay | Expo/React Native, no backend, bundled content JSON | Junior+ | STRONG (astraupskill/) | C |
| BorrowBox | borrowbox | web API (monolith) | ORIGINAL (COURSE-STRUCTURED) + curriculum overlay | C#/.NET 10, ASP.NET Core minimal-ish, SQLite, xUnit | Junior→Mid (intentional teaching ramp) | EXCELLENT (astraupskill/, dfableandopus/, docs/curriculum) | A |
| LocalOps Ledger | buildbusinesses | web app | ORIGINAL + curriculum overlay | Next.js 16/React19, TS, IndexedDB, Zod, tsx test runner | Junior+ | USEFUL (astraupskill/, dfableandopus/) | B |
| ShipShape | buildermentor | monorepo(2 apps) | ORIGINAL + curriculum overlay | Fastify API, Drizzle+pg, pg-boss, Anthropic SDK (RAG/LLM item-gen), React+TanStack Query/Router web, Vitest, Playwright e2e | Mid+/Senior-leaning | USEFUL (astraupskill/) | A |
| Event Ticketing Platform | buildevent | monorepo(2 apps+2 pkgs) | ORIGINAL + curriculum overlay | Next.js web, Fastify API, Prisma/PostgreSQL, Redis+BullMQ, Stripe, signed QR, Turborepo | Mid+ | USEFUL (astraupskill/, docs/upskill) | B |
| ReviewDeck | buildreviewer | monorepo(2 apps) | ORIGINAL + curriculum overlay | NestJS API, Prisma/SQLite, Octokit (GitHub PR review API), React+Vite web, Jest+Vitest | Mid | USEFUL (astraupskill/) | B |
| Small Plates | buildsmallplates | mobile app | ORIGINAL + curriculum overlay | Expo57/RN0.86, expo-sqlite, React Navigation, Vitest (92 tests) | Junior+ | USEFUL (astraupskill/, dfableandopus/) | C |
| IPSKILL (buildsql) | buildsql | web app (curriculum archive) | ORIGINAL, evolved from a prior "SQL Dojo" pytest course into a 6-track React archive | React19/Vite8, no backend, content-authoring scripts (merge/validate), Vitest+RTL | Junior+ (as an app) / content is broad | STRONG (this whole repo IS a curriculum: 310 lessons/2,155 missions across SQL/TS/Node/React/C#/.NET) | B |
| Collaborative Markdown Editor | buildwhiteboard | monorepo(client+server) | ORIGINAL + curriculum overlay | React19/Vite client, Node+Yjs CRDT+ws server, Playwright e2e, node:test | Mid | USEFUL (astraupskill/) | B |
| Questboard | calendar+jobtrack | web app | ORIGINAL + curriculum overlay | React19/Vite/TS, Tailwind4, Zustand, date-fns, Vitest | Junior+ | USEFUL (astraupskill/) | C |
| Daybook (jobtrack) | jobtrack | web app | ORIGINAL + curriculum overlay | React18/Vite (JS, not TS), Vitest | Junior | USEFUL (fabledocs/, astraupskill/ — two overlapping curriculum trees) | F |
| Recipe Lab | recipeview | web app (client+server) | ORIGINAL + curriculum overlay | React18/Vite, Express+better-sqlite3-style server, node:test | Junior+ | USEFUL (astraupskill/) | C |
| Sarap & Ngon (recipeweb) | recipeweb | web app | ORIGINAL + curriculum overlay | React19/Vite, client-only (no backend), curated static recipe JSON, oxlint | Junior | USEFUL (astraupskill/, docs/, net/) | C |

## Recall (ankijs)
- Path: ankijs                — Origin: ORIGINAL (app) with a large curriculum-content layer added on top
- Type: web app (offline-capable PWA)
- State: complete   - Size: ~4,700 non-vendor files (much of it is generated `artifacts/` from content-authoring runs, not source) - Last modified: 2026-09-12 (git)
- Purpose: Local-first spaced-repetition flashcard app for practical web-dev skills — 2,871 cards / 75 decks / 48 "missions" covering forms, APIs, SQL, auth, validation, testing, CRUD shipping. Explicitly excludes LeetCode/DSA. No account required; optional Supabase sync.
- Stack: FE: React19+Vite8+Tailwind4 | BE: none required (client-only), optional Supabase sync layer | DB: IndexedDB (browser), fake-indexeddb for tests | Test: Vitest + Testing Library + Playwright e2e | Infra: netlify.toml + vercel.json (dual deploy targets)
- Architecture: SPA, local-first with optional cloud sync; content pipeline (`scripts/build-reviewed-content.mjs`, `content:check`) compiles/validates the flashcard corpus separately from the app code
- Complexity: Mid
- Educational material: STRONG — `astraupskill/` (7-file Astra curriculum: codebase map, concepts, worked change, testing/debugging, practice, solutions, trace lab) plus `handoff/`; the app's own *content* (2,871 cards) is itself a teaching corpus, project-specific and deep, not generic
- Quality observations:
  - Extensive artifact/verification trail in `artifacts/` (crud-unit-results.json, final-vitest.json, diff-check logs) suggesting a disciplined content-QA loop, not just a demo
  - Both `content:check` and `content:runtime` scripts exist — content is validated statically and against a real rendered build
  - Uses `@supabase/supabase-js` for optional sync — worth checking token/secret handling in `.env.example` (not read here; flag for deeper inspection if reused)
  - `dist/`, `release/`, `net/` folders present at top level — suggests multiple packaging targets tried (web + possibly a "net" variant) — NEEDS DEEPER INSPECTION to know if `net/` is a second app or just docs
- Old-AI-generated smells: none seen from manifests/README; content volume is large enough that spot-checking a sample of cards for repetition/genericness would be worthwhile before reuse
- Skill tags: fe-react, fe-state, fe-testing, test-unit, test-e2e, db-sqlite (IndexedDB analog), ai-llm-integration (if Supabase-sync path touches any LLM — UNKNOWN, not confirmed), crud-basic
- Duplicate/overlap: none within this batch (unrelated to the Tagalog family despite superficial folder-name proximity)
- Learning value: High — large, well-organized spaced-repetition engine + huge domain-general content library
- Transformation opportunity: Could be repackaged as a stand-alone "flashcard engine" library (SRS scheduling + IndexedDB store) reusable across other content domains
- Interview stories: SRS scheduling algorithm design; offline-first PWA with optional cloud sync; content-pipeline validation/QA discipline
- Proposed disposition: B HIGH-VALUE — complete, well-tested, PWA architecture, huge bespoke content library worth preserving; not a flagship only because the domain (flashcards) is narrower than the monorepo/product-shaped projects in this batch

## Aral v3 local-first
- Path: aral                  — Origin: ORIGINAL (greenfield rebuild of the Tagalog-app concept)
- Type: monorepo (3 packages: shared/server/app)
- State: working-looking (has `docs/BLOCKED.md` and `docs/DECISIONS.md`, suggesting it stalled at some decision point) - Size: 185 files - Last modified: 2026-07-09 (git)
- Purpose: A from-scratch redesign of the Tagalog-learning app around a local-first sync architecture: client-side SQLite is the source of truth, and an append-only event log syncs to a thin server that "derives nothing."
- Stack: FE: React PWA + Capacitor (iOS/Android) | BE: Hono + tRPC v11 + Drizzle ORM over libsql | DB: SQLite (client, via capacitor-sqlite/jeep-sqlite) + libsql (server) | Validation: Zod | Test: Vitest
- Architecture: event-sourcing-flavored sync (append-only progress event log, server "derives nothing" — i.e., pure event replay for state), SM-2-lite spaced-repetition scheduler, content compiled from YAML with hard lints into versioned bundles (`dist/bundle-v{N}.json`)
- Complexity: Mid+ (event-log sync design is a genuinely senior-adjacent pattern)
- Educational material: USEFUL — `astraupskill/` (same 7-file Astra curriculum pattern) plus `docs/DECISIONS.md`/`docs/BLOCKED.md`, which are unusually good raw material for "how do you make and record an architecture decision" interview prep, since they're real, not retrofitted
- Quality observations:
  - `content/` has its own `compile.test.ts` and a documented build step (`build.ts`) with zod schemas for both events and content — schema-first content pipeline
  - `docs/BLOCKED.md` existing at all is a signal this rebuild did not fully complete — treat state claims with caution; NEEDS DEEPER INSPECTION of that file to know what's unresolved
  - Workspace uses plain npm workspaces (not pnpm/turbo like sibling `tagalog`), so this is a distinct toolchain generation
- Old-AI-generated smells: none obviously — the event-log/sync design is not boilerplate-shaped; genuinely a considered architecture
- Skill tags: fe-react, arch-event-driven, db-sqlite, orm, be-validation, mobile-rn (Capacitor is RN-adjacent but not literally RN — tag loosely), realtime-ws (sync, not literally websockets — UNKNOWN transport, not confirmed), design-docs-adrs
- Duplicate/overlap: same product concept as `tagalog` (Next+Expo+Fastify+Postgres) and `mobiletagalog` (RN port of `tagalog`) — this is a THIRD, architecturally distinct attempt at the same idea, not the same codebase
- Learning value: Very High — the event-log local-first sync pattern is a strong, differentiated portfolio piece distinct from typical CRUD
- Transformation opportunity: Extract the event-log sync design + `docs/DECISIONS.md`/`BLOCKED.md` into a standalone case study/ADR writeup demonstrating architectural reasoning, independent of whether the app itself ships
- Interview stories: "derive nothing" server design, offline-first conflict handling via append-only events, SM-2-lite scheduling, schema-first content compilation with lints
- Proposed disposition: B HIGH-VALUE — reason: strongest architectural idea in the whole Tagalog lineage but incomplete (BLOCKED.md); very good source for a design-decisions writeup even if the app itself isn't finished

## aral-deploy
- Path: aral-deploy            — Origin: N/A (build artifact)
- Type: not an app — a deploy snapshot
- State: N/A - Size: 6 files (JSON content bundles + DEPLOY.md) - Last modified: UNKNOWN (no git repo; `DEPLOY.md` states snapshot taken 2026-09-08)
- Purpose: `DEPLOY.md` states this is a snapshot taken from `tagalog` at commit `39f621b` (course v5), documenting two GitHub remotes (`elirc/aral-tagalog`, `elirc/aral-tagalog-v2`) with 5 unpushed commits. It is compiled content output (`content-dist/`), not source.
- Stack: N/A
- Architecture: N/A
- Complexity: Tiny
- Educational material: NONE
- Quality observations: Confirms `tagalog` is the canonical, most-current build of the Aral product (has real remotes queued to push) — useful as a pointer, not as a project in its own right
- Old-AI-generated smells: none applicable
- Skill tags: deploy
- Duplicate/overlap: derivative of `tagalog`
- Learning value: Low — reference-only
- Proposed disposition: G ARCHIVE — reason: not a project; keep only as a note that `tagalog/` has unpushed commits worth checking before any cleanup

## Aral — Learn Tagalog (tagalog)
- Path: tagalog                — Origin: ORIGINAL + curriculum overlay
- Type: monorepo (3 apps: api/web/mobile + shared packages)
- State: complete-looking (per `aral-deploy/DEPLOY.md`, has unpushed commits to two real GitHub remotes) - Size: largest in this batch (file-count tool reported ~10.8k, but this includes framework caches under `.turbo/` and nested app `node_modules` that the exclude filter didn't fully catch — treat as UNKNOWN precise count, genuinely the biggest by source-tree breadth regardless) - Last modified: 2026-09-08 (git)
- Purpose: Free Duolingo-style Tagalog↔English course app. Web (Next.js) and mobile (Expo) share game/lesson logic through a pnpm/Turborepo monorepo; backend is Fastify + PostgreSQL.
- Stack: FE: Next.js (web), Expo/React Native (mobile) | BE: Fastify, `@node-rs/argon2` (password hashing), `jose` (JWT), `@fastify/rate-limit` | DB: PostgreSQL via Drizzle ORM | Validation: Zod | Infra: pnpm workspaces + Turborepo, Docker (`docker-compose.yml`), GitHub Actions (`.github/`)
- Architecture: modular monolith monorepo — `packages/core` (shared game logic), `packages/db`, `packages/config`, `packages/ui`, `packages/content` — consumed identically by both web and mobile clients
- Complexity: Mid+
- Educational material: USEFUL — `docs/adr-reverse-engineered.md`, `docs/AUTHORING.md`, `docs/upskill/`, and a substantial `handoff/` folder (agent-briefs, COMMIT-PLAN.md, NEXT-STEPS.md, REVIEW-METHOD.md, STATE.md) — this is real project-management/handoff documentation, not generic curriculum filler
- Quality observations:
  - Real auth stack (argon2 password hashing + jose JWT + rate limiting) rather than a toy auth shim
  - Docker Compose present for local Postgres — standard, reasonable
  - `handoff/` folder with STATE.md/NEXT-STEPS.md/REVIEW-METHOD.md indicates this was actively managed across multiple work sessions, a good "how I manage a real project" artifact
  - Two GitHub remotes queued (per aral-deploy notes) with unpushed commits — verify push status before treating as "done"
- Old-AI-generated smells: none seen in manifests; shared-logic-across-two-clients architecture is a deliberate, non-boilerplate choice
- Skill tags: fe-react, fe-next, be-node-express (Fastify, closest tag), authn, db-postgres, orm, db-migrations, mobile-rn, arch-modular-monolith, docker, ci-cd, design-docs-adrs
- Duplicate/overlap: canonical/most current version of the "Aral" Tagalog product; `mobiletagalog` is a standalone port of its mobile app; `aral` (v3) is an architecturally distinct earlier/parallel rebuild attempt
- Learning value: Very High — most production-shaped of the Tagalog lineage: real auth, real Postgres, monorepo discipline, cross-client shared logic, active handoff docs
- Transformation opportunity: This is the strongest flagship candidate in the whole family — push the queued commits, and use `handoff/STATE.md`+`REVIEW-METHOD.md` directly as portfolio evidence of process discipline
- Interview stories: cross-platform shared business logic in a monorepo, Fastify auth (argon2+JWT+rate limiting), Postgres+Drizzle schema design, Turborepo build orchestration
- Proposed disposition: A FLAGSHIP — reason: largest, most production-like, real auth/DB, cross-client architecture, and active project-management artifacts; the other three Tagalog-family dirs are earlier/derivative relative to this one

## Aral Tagalog (mobile port) — mobiletagalog
- Path: mobiletagalog          — Origin: ORIGINAL, explicitly a port ("Ported from the `tagalog` monorepo into a single self-contained project") + curriculum overlay
- Type: mobile app (Expo/React Native)
- State: working-looking (README claims it "works with no backend" — content ships bundled) - Size: 64 files - Last modified: 2026-07-17 (git)
- Purpose: Standalone, no-pnpm-workspace, no-backend version of the Tagalog course app: 15 units / 57 lessons / 480 exercises / 230 vocab entries baked into `src/content/bundle.json`, playable fully offline as a guest.
- Stack: FE: Expo ~53 / React Native 0.79 / React 19, expo-router, expo-sqlite (local persistence), expo-speech (TTS), expo-av | BE: none | Test: Vitest (`--pool=forks --maxWorkers=1`, a concurrency workaround worth noting)
- Architecture: single self-contained mobile app, no monorepo tooling, content pre-compiled and bundled at build time
- Complexity: Junior+
- Educational material: STRONG — same `astraupskill/` 7-file Astra pack
- Quality observations:
  - Deliberately de-coupled from the `tagalog` pnpm workspace ("no `@aral/*` packages") — a reasonable simplification for a standalone demo/App-Store-shaped artifact
  - Uses expo-sqlite for local state and expo-speech for pronunciation — reasonable native-feature usage beyond a toy CRUD list
  - Vitest forced to single-worker forks pool — a known workaround for RN/Expo test-runner flakiness, worth citing as a "gotcha" if this pattern recurs elsewhere in the archive
- Old-AI-generated smells: none seen
- Skill tags: mobile-rn, fe-state, db-sqlite, test-unit
- Duplicate/overlap: derivative of `tagalog`'s `apps/mobile` — same product, extracted to stand alone; keep one, not both, as portfolio evidence unless "here's how I extract a monorepo app to standalone" is itself the story being told
- Learning value: Medium — solid mobile build, but functionally redundant with `tagalog/apps/mobile`
- Proposed disposition: C SPECIALIZED — reason: good as a self-contained mobile-only demo (e.g., for an App Store submission or an isolated mobile-skills interview story) even though `tagalog` is the more complete source of truth

## BorrowBox
- Path: borrowbox               — Origin: ORIGINAL, explicitly structured as a 15-sprint teaching repo + curriculum overlay
- Type: web API (monolith, C#/.NET)
- State: complete - Size: ~121 files (3 src projects + 3 test projects, one per layer) - Last modified: 2026-07-15 (git)
- Purpose: Equipment-lending system (laptops, cameras, calculators, lab kits) for a campus/org setting: borrowers, equipment, loans, reservations, inspections, reporting.
- Stack: BE: C#/.NET 10 (ASP.NET Core, `Microsoft.NET.Sdk.Web`), nullable-enabled | DB: SQLite + in-memory storage implementations (Infrastructure layer) | Auth: "authorization concepts" per README (module: `Security/`) | Test: dedicated `.Tests` project per layer (Api/Core/Infrastructure), lockfiles (`packages.lock.json`) present — reproducible restores
- Architecture: clean three-project layering (Api / Core / Infrastructure), explicitly NOT using microservices, MediatR, CQRS, generic repositories, AutoMapper, or a message broker — a deliberate "deliberately small architecture" per README, aimed at a junior-to-mid ramp
- Complexity: Junior→Mid (intentional pedagogical progression: "starts with plain C# and one HTTP slice," adds validation/LINQ/DI/SQLite/background work/authorization/testing/ops)
- Educational material: EXCELLENT — `astraupskill/` (7-file Astra pack), `dfableandopus/` (interview questions, stories-and-resume, code-reading drill, take-home, system-design followups, flashcards — a full interview-prep pack), plus `docs/curriculum`, `docs/security`, `docs/operations`, `docs/quality`, `docs/integrations`, `docs/sprints`, `LEARNER-GUIDE.md`, `TESTREADME.md`, `BUG-LEDGER.local.md`. This is the deepest documentation stack of any project in this batch.
- Quality observations:
  - Per-project `packages.lock.json` in every src/test project — disciplined, reproducible NuGet restores
  - Three-tier test suite (one test project per architectural layer) rather than one flat test project
  - `BUG-LEDGER.local.md` at repo root — a real defect log, valuable as evidence of debugging practice if its contents are genuine (NEEDS DEEPER INSPECTION to confirm it's not just a template)
  - `global.json` present — pins SDK version, good practice for teaching repos
  - Uses `net10.0` target framework — current .NET version, not stale
- Old-AI-generated smells: none seen; the explicit "we deliberately do NOT use X/Y/Z" framing in the README is a strong signal of intentional scope control rather than uncontrolled AI sprawl
- Skill tags: be-dotnet, db-sqlite, authz-rbac (tentative — "authorization concepts," not confirmed as full RBAC), test-unit, test-integration, arch-modular-monolith, legacy-codebase-reading, design-docs-adrs, code-review
- Duplicate/overlap: none in this batch — only C#/.NET project here
- Learning value: Very High — the only .NET project in this batch, deepest docs/interview-prep of the batch, deliberate architectural minimalism as a teaching device
- Transformation opportunity: Use `dfableandopus/` directly as a mock-interview pack; the layered-with-lockfiles-per-project pattern is a good template to replicate in other .NET portfolio pieces
- Interview stories: "why not microservices/CQRS here" architectural-restraint story, layered testing strategy, reproducible builds via per-project lockfiles
- Proposed disposition: A FLAGSHIP — reason: rare .NET entry in an otherwise TS-heavy archive, deepest and most deliberate documentation/interview-prep material of the batch, clean intentional architecture

## LocalOps Ledger (buildbusinesses)
- Path: buildbusinesses          — Origin: ORIGINAL + curriculum overlay
- Type: web app
- State: complete-looking ("learning edition adds strict validation, transactional IndexedDB storage, guarded CRUD, actual payments, stock history and reviewed migration") - Size: 105 files - Last modified: 2026-07-18 (git)
- Purpose: Local business operating-records tool: people, money, stock, assets, daily logs, reminders, budgets — browser-only, no account/backend.
- Stack: FE: Next.js 16 / React 19 / TypeScript | DB: IndexedDB (client-only), with a "transactional" storage layer per README | Validation: Zod | Test: `tsx --test` (Node's built-in test runner via tsx), `fake-indexeddb` for test doubles
- Architecture: SPA-over-Next.js, no server component beyond static hosting; storage layer explicitly built to be "transactional" and "guarded" over IndexedDB — a genuinely non-trivial browser-DB concurrency concern
- Complexity: Junior+
- Educational material: USEFUL — `astraupskill/`, `dfableandopus/` (interview pack, same structure as borrowbox's), plus `docs/original/` (a preserved pre-"learning edition" snapshot of the single-file source, e.g. `LocalOperationsApp.tsx.txt`) and `docs/upskill/`
- Quality observations:
  - `docs/original/` preserving the pre-upskill single-file version is good provenance — lets you see the "before" state directly
  - README explicitly calls out that `localhost` and `127.0.0.1` are different IndexedDB origins — a real, specific gotcha documented rather than glossed over
  - Node engines pinned (`>=22.16 <23`) — precise, reproducible
- Old-AI-generated smells: the original pre-upskill artifact being a single giant `LocalOperationsApp.tsx` file (per `docs/original/`) is a classic "AI dumped it all in one file" smell — but it's explicitly documented as the "before" state that was refactored, so it's a positive teaching artifact rather than a live problem
- Skill tags: fe-react, fe-next, fe-forms-validation, db-transactions (browser-IndexedDB flavor), be-validation, crud-basic, test-unit
- Duplicate/overlap: none in this batch; conceptually adjacent to `recipeview`/`calendar+jobtrack` as another local-first personal data app, but different domain
- Learning value: Medium-High — good concrete example of "single giant file → validated, transactional, guarded CRUD" refactor with before/after evidence preserved
- Transformation opportunity: The before/after pair (`docs/original/` vs current) is directly reusable as a code-review/refactoring exercise for other learners
- Interview stories: browser-storage transactionality and origin gotchas, refactoring a monolithic component into validated guarded CRUD
- Proposed disposition: B HIGH-VALUE — reason: solid, well-documented refactor story with preserved before/after evidence, though the domain (personal records CRUD) is less differentiated than others in this batch

## ShipShape (buildermentor)
- Path: buildermentor            — Origin: ORIGINAL + curriculum overlay
- Type: monorepo (2 apps: api/web + shared package)
- State: complete (per memory record: "all 8 milestones done ... 30 tests green") - Size: 153 files - Last modified: 2026-07-19 (git)
- Purpose: A mastery-tracking study engine for engineers leveling up to mid/senior and prepping for interviews — recognition→recall→production mastery tiers, FSRS-style spaced repetition, LLM-generated item banks grounded via RAG over uploaded sources (PDF/EPUB/DOCX/MD/TXT/URL), an interview-loop simulator, and explicit LLM cost guardrails.
- Stack: FE: React18 + TanStack Query/Router, react-markdown | BE: Fastify, Drizzle ORM over PostgreSQL (+ pgvector per README), `pg-boss` (Postgres-backed job queue), `@anthropic-ai/sdk` (LLM item generation), `@node-rs/argon2` (auth), `epub2`/`mammoth`/`pdf-parse`/`turndown` (multi-format ingestion) | Test: Vitest (api), Playwright e2e | Infra: Docker (Postgres 16 + pgvector), pnpm workspaces
- Architecture: modular monolith with an async job layer (`pg-boss`) for embedding/generation work, RAG pipeline (chunk → embed → map to an 8-track skill taxonomy → ground LLM-generated items with citations)
- Complexity: Mid+/Senior-leaning (RAG + job queue + LLM cost governance is meaningfully more advanced than typical CRUD in this batch)
- Educational material: USEFUL — `astraupskill/` pack; the product itself teaches interview/system-design skills, a nice meta quality
- Quality observations:
  - Explicit LLM cost guardrails (per-day budget, full call audit log, graceful degradation) — a real production concern most toy AI-integration projects skip
  - Multi-format document ingestion (PDF/EPUB/DOCX) rather than "paste text" — meaningfully more engineering than a typical AI-wrapper demo
  - Uses `pg-boss` for async jobs rather than a bespoke queue — reasonable, idiomatic choice
  - "Review citations" (every wrong answer links to the source passage) demonstrates provenance-tracking discipline in the RAG design
- Old-AI-generated smells: none seen in manifests/README; the cost-guardrail and citation-provenance features are specifically the kind of thing that's absent from shallow AI-wrapper demos, a positive signal
- Skill tags: ai-llm-integration, be-async-jobs, queues, db-postgres, orm, authn, arch-modular-monolith, test-e2e, observability-logs (call audit log), config-secrets (cost budget config)
- Duplicate/overlap: none in this batch
- Learning value: Very High — most sophisticated AI-integration architecture in this batch (RAG + citations + cost governance + async jobs)
- Transformation opportunity: Already a flagship-shaped AI product; the cost-guardrail + citation-provenance design is directly reusable as a case study for "how to ship LLM features responsibly"
- Interview stories: RAG grounding + citation provenance design, LLM cost governance/observability, background-job architecture for embedding pipelines, FSRS-based scheduling
- Proposed disposition: A FLAGSHIP — reason: the deepest, most senior-shaped AI-integration architecture in the batch (RAG, async jobs, cost guardrails, multi-format ingestion), directly interview-relevant for "agentic engineering" and "ai-llm-integration" skill areas

## Event Ticketing Platform (buildevent)
- Path: buildevent                — Origin: ORIGINAL + curriculum overlay
- Type: monorepo (2 apps + 2 shared packages)
- State: working-looking (stray `web-dev.log`/`web-dev-3002.log` files at root suggest active local dev sessions, not proof of completeness — NEEDS DEEPER INSPECTION of `docs/upskill` or test results to confirm "complete") - Size: 157 files - Last modified: 2026-07-18 (git)
- Purpose: Event ticketing platform: discovery, event detail, reservations, Stripe checkout, signed QR tickets, seating, waitlist, mobile check-in/scanning.
- Stack: FE: Next.js App Router | BE: Fastify (`@fastify/helmet`, `@fastify/rate-limit`, `@fastify/websocket`, `@fastify/cors`) | DB: PostgreSQL via Prisma | Jobs: `bullmq` (Redis-backed) | Payments: Stripe (`@stripe/stripe-js`, `@stripe/react-stripe-js`) | Auth: `bcryptjs` | Notable: `packages/ticket-renderer` — dedicated signed-QR-payload/image generation package | Infra: npm workspaces + Turborepo
- Architecture: modular monolith monorepo with a distinct queue-backed jobs layer (BullMQ/Redis) separate from the request path — appropriate for ticket issuance/check-in workloads
- Complexity: Mid+
- Educational material: USEFUL — `astraupskill/`, `docs/upskill/`
- Quality observations:
  - Security middleware present by default (helmet, rate-limit, cors) rather than bolted on later — good baseline
  - Dedicated `ticket-renderer` package for signed QR generation is a clean separation of a security-sensitive concern (ticket authenticity) from general app logic
  - Real Stripe integration (client + server SDKs) rather than a fake payment stub
  - `web` app's `test` script is literally `"echo \"No web tests yet\""` — confirmed test-coverage gap on the frontend
- Old-AI-generated smells: web-app test script being a no-op echo is exactly the "tests claimed but not real" pattern to flag — legitimate gap, not fabricated, but worth calling out explicitly
- Skill tags: be-node-express (Fastify), db-postgres, orm, db-migrations, queues, be-async-jobs, security-owasp (helmet/rate-limit), authn, realtime-ws (`@fastify/websocket`), arch-modular-monolith
- Duplicate/overlap: none in this batch
- Learning value: High — signed-ticket security design, queue-backed workflow, real payments integration
- Transformation opportunity: Backfill web e2e tests (currently a stated gap) to make this a stronger flagship; the ticket-renderer signing design is reusable as a standalone case study on authenticity/anti-fraud design
- Interview stories: designing tamper-resistant QR tickets, queue-backed check-in/issuance workflows, Stripe checkout integration, WebSocket usage for scanner/check-in flows
- Proposed disposition: B HIGH-VALUE — reason: strong backend architecture (queues, signed tickets, real payments) held back from flagship status only by the confirmed absent frontend test coverage

## ReviewDeck (buildreviewer)
- Path: buildreviewer             — Origin: ORIGINAL + curriculum overlay
- Type: monorepo (2 apps + shared package)
- State: complete (per memory record: "all 7 milestones committed ... 68 tests green") - Size: 121 files - Last modified: 2026-07-19 (git)
- Purpose: Local-first GitHub PR review-drafting tool: draft comments with a severity taxonomy (BLOCKER/ISSUE/SUGGESTION/NITPICK/PRAISE) offline, then publish as a single batched GitHub PR review; tracks head-SHA drift and flags orphaned comments whose anchors vanished.
- Stack: BE: NestJS, Prisma (SQLite — `data/reviewdeck.db` present, a real local DB file checked into the working tree), `@octokit/rest` (GitHub API), `helmet`, `dotenv` | FE: React18 + Vite + TanStack Query, `highlight.js` | Test: Jest (api, `--runInBand`), Vitest (web)
- Architecture: modular monolith, local-first drafting workspace synced to an external API (GitHub) only at publish time — a deliberate "local draft, single remote commit" pattern
- Complexity: Mid
- Educational material: USEFUL — `astraupskill/`
- Quality observations:
  - Drift-safety design (snapshotting `headSha`, blocking publish on new commits, flagging orphaned anchors) is a genuinely non-trivial correctness concern most PR-tooling toy projects skip
  - Real Octokit integration rather than a mocked GitHub API — actual external-API integration complexity
  - `.env` (not just `.env.example`) present at repo root — flag for secret-hygiene review before any sharing/reuse (do not assume it's safe; NEEDS DEEPER INSPECTION, do not read contents here per read-only/no-secrets handling)
  - SQLite DB file (`reviewdeck.db`) and its `-journal` sidecar committed into the working tree — fine for a local dev DB but worth excluding if this repo is ever pushed publicly
- Old-AI-generated smells: none seen in architecture; the presence of a real `.env` file (vs. only `.env.example`) is the one hygiene flag worth acting on before any wider sharing
- Skill tags: be-nest, db-sqlite, orm, be-rest-design, security-owasp, test-integration, test-unit, config-secrets (flag), idempotency (drift-safe publish is idempotency-adjacent)
- Duplicate/overlap: none in this batch
- Learning value: High — genuine external-API integration complexity (GitHub) plus a real correctness problem (drift safety) beyond typical CRUD
- Transformation opportunity: The drift-safety/anchor-invalidation design is directly reusable as a "designing for eventual consistency against an external system" interview story
- Interview stories: drift detection against an external API's mutable state, severity-taxonomy UX design, batched-publish transaction design against a third-party API
- Proposed disposition: B HIGH-VALUE — reason: real external-API integration with a genuine correctness/drift problem solved deliberately; held to B rather than A mainly because of the `.env`-in-tree hygiene flag needing resolution first

## Small Plates (buildsmallplates)
- Path: buildsmallplates          — Origin: ORIGINAL + curriculum overlay
- Type: mobile app (Expo/React Native)
- State: complete (per memory record: "70 tests green, commit 45445d0") - Size: 92 files - Last modified: 2026-07-19 (git)
- Purpose: Local-first weightlifting log for beginner/intermediate lifters — one-time-purchase model, no servers/tracking, tells the user what to lift next.
- Stack: FE: Expo SDK57 / RN0.86 / TypeScript strict | DB: expo-sqlite (on-device, single DB, synchronous repos) | Nav: React Navigation (bottom tabs + native stack) | Notable libs: react-native-svg (live barbell-plate rendering + sparklines), expo-haptics (centralized `Haptic` service) | Test: Vitest, 92 tests across core calculations/repository seams/orchestration
- Architecture: single mobile app, layered into `core`/`db`/`engine`/`services`/`screens`/`state`, each with its own `__tests__` — a clean per-module test discipline rather than one flat test dir
- Complexity: Junior+
- Educational material: USEFUL — `astraupskill/` (includes an extra `08-WEB-TRANSLATION.md` beyond the standard 7-file pack), `dfableandopus/`
- Quality observations:
  - Per-module `__tests__` folders (content, core, db, engine, services) — good test-organization discipline, not a bolted-on single test file
  - `expo-sqlite` used with "synchronous repos" per README — a specific, intentional data-access design choice worth citing
  - Custom SVG barbell-plate rendering (not a stock chart library) shows genuine UI-engineering effort beyond CRUD forms
- Old-AI-generated smells: none seen
- Skill tags: mobile-rn, db-sqlite, fe-state, test-unit, fe-perf (sparkline rendering)
- Duplicate/overlap: none in this batch
- Learning value: Medium-High — solid mobile domain app with genuine custom-rendering and calculation-engine complexity
- Interview stories: on-device synchronous SQLite repository design, custom SVG data visualization in RN, progressive-overload calculation engine design
- Proposed disposition: C SPECIALIZED — reason: strong, complete mobile app, but the domain (fitness logging) and architecture are less differentiated for a web/Node/.NET-focused portfolio than the monorepo/backend-heavy projects in this batch

## IPSKILL (buildsql)
- Path: buildsql                   — Origin: ORIGINAL; README explicitly states this evolved from an earlier product framed around SQL specifically ("despite the folder name `buildsql`") into a 6-track curriculum archive app + curriculum overlay
- Type: web app that renders/hosts a curriculum archive (not itself "a SQL course" per its own README)
- State: complete-looking - Size: 210 files - Last modified: 2026-08-31 (git, most recent in this batch)
- Purpose: A React/TS learning workspace displaying a large lesson archive — 310 lessons and 2,155 "missions" spanning SQL, TypeScript, Node, React, C#, and .NET — with progress saves, spaced recall scheduling, an archive view, and a CRUD practice-project tracker.
- Stack: FE: React19/Vite8, `react-markdown`+`remark-gfm` for lesson rendering, `lucide-react` | DB: none (browser-local) | Test: Vitest + Testing Library, `verification/verify_authoring.py` (a Python script that exercises the authoring CLIs in synthetic isolated workspaces — cross-language tooling) | Content pipeline: `scripts/merge-content.mjs`, `scripts/validate-content.mjs`, `content-src/` (raw lesson source, e.g. `content-src/vol3/build/*.part{1,2,3}.txt` — chunked lesson authoring files)
- Architecture: static SPA over a large pre-authored content corpus, with a dedicated content-authoring/validation pipeline (including a Python verification harness) separate from the runtime app
- Complexity: Junior+ as an app; the underlying content spans a very wide skill range
- Educational material: STRONG (this entire project IS curriculum) — plus the standard `astraupskill/` pack (with an extra `08-BACKEND-TICKET.md`) and `dfableandopus/`; `docs/original/` preserves pre-refactor single-file snapshots (`src__App.tsx.txt`, `src__game.ts.txt`, etc.), same before/after provenance pattern seen in `buildbusinesses`
- Quality observations:
  - Cross-language authoring verification (Python script driving Node content-build scripts in synthetic workspaces, explicitly never publishing to the real content) — a genuinely careful "don't corrupt the real corpus while testing the tooling" design
  - `docs/original/` before/after snapshots again present — a repeated pattern across this batch worth noting as a portfolio-organization convention (see Batch observations)
  - README is unusually self-aware/corrective about its own naming ("it is not itself a SQL course, despite the folder name") — good sign of accurate self-documentation over marketing-speak
- Old-AI-generated smells: none seen; content volume (2,155 "missions") warrants spot-checking a sample for repetition given the scale, same caveat as `ankijs`
- Skill tags: fe-react, ts-types, test-unit, db-sql-raw (content domain, not the app's own DB), crud-basic (practice-tracker feature), legacy-codebase-reading (docs/original before/after)
- Duplicate/overlap: none in this batch; internally, note the project's own identity drift (started as "SQL Dojo," is now a 6-track general archive) — worth flagging if any other batch's memory notes still describe it as pytest-graded, since that description is stale
- Learning value: High — largest, broadest curriculum corpus in the batch, plus a careful cross-language authoring/verification pipeline
- Transformation opportunity: The Python-driven synthetic-workspace verification pattern is reusable as a template for safely testing content/authoring tooling elsewhere in the archive
- Interview stories: designing a safe verification harness for content-authoring tools, multi-language content pipeline (Node build + Python verification)
- Proposed disposition: B HIGH-VALUE — reason: very large, broad, and carefully verified curriculum archive with a genuinely interesting authoring-verification design, though as an *app* it's a fairly simple SPA

## Collaborative Markdown Editor (buildwhiteboard)
- Path: buildwhiteboard             — Origin: ORIGINAL + curriculum overlay
- Type: monorepo (client + server, not a shared-workspace monorepo — each has its own `package.json`/lockfile)
- State: working-looking (no git repo present — UNKNOWN true completion state / commit history; judged from file contents only) - Size: 48 files - Last modified: UNKNOWN (no `.git`; not assessed via mtime per brief's efficiency guidance)
- Purpose: Real-time collaborative Markdown editor: document metadata CRUD, file persistence, live presence, import/export, formatting, sanitized preview.
- Stack: FE: React19+Vite client, `react-markdown`+`remark-gfm`+`rehype-sanitize` (sanitized preview — a real XSS-prevention step, not skipped), `yjs`+`y-websocket` (CRDT client) | BE: Node server using `yjs`+`y-websocket`+`y-protocols`+`ws`+`lib0` | Test: Playwright e2e (`tests/collaboration.spec.ts`), `node:test` on the server (`server/test/documents.test.js`) | Infra: Dockerfiles for both client and server, docker-compose
- Architecture: CRDT-based real-time collaboration (Yjs) over a WebSocket server — a legitimately advanced realtime pattern, distinct from simple socket broadcast
- Complexity: Mid
- Educational material: USEFUL — `astraupskill/`
- Quality observations:
  - Uses `rehype-sanitize` in the Markdown render pipeline — explicit XSS defense for user-generated Markdown content, a detail many toy editors skip
  - CRDT (Yjs) chosen over naive last-write-wins or OT — appropriate tool for true multi-user concurrent editing
  - Separate Dockerfiles per service (client/server) plus compose — reasonable containerization split
  - No git repository present in this directory — cannot verify commit history/authorship timeline the way other projects in this batch can; treat completeness claims as evidence-from-files-only
- Old-AI-generated smells: none seen in manifests
- Skill tags: realtime-ws, arch-event-driven (CRDT sync), security-owasp (sanitized Markdown), docker, test-e2e, fe-react
- Duplicate/overlap: none in this batch
- Learning value: High — CRDT-based real-time collaboration is a strong, differentiated technical story
- Interview stories: CRDT vs. OT tradeoffs for collaborative editing, sanitizing untrusted Markdown for safe rendering, WebSocket server design for presence+sync
- Proposed disposition: B HIGH-VALUE — reason: technically differentiated (CRDT realtime collab) and reasonably complete; not flagship-tier mainly due to missing git history to confirm provenance/completeness, and smaller overall scope than the monorepo products above

## Questboard (calendar+jobtrack)
- Path: calendar+jobtrack            — Origin: ORIGINAL + curriculum overlay
- Type: web app
- State: complete (per memory record: "90 tests green") - Size: 78 files - Last modified: UNKNOWN (no `.git` in this directory; memory notes this project historically "sits in the stray home-dir repo" rather than its own repo)
- Purpose: Combined personal calendar + gamified job-application tracker, fully local (no account, no server, no network calls).
- Stack: FE: React19/Vite/TS, Tailwind4, Zustand (state), `date-fns`, `react-router-dom`, `lucide-react` | Test: Vitest+RTL+jsdom
- Architecture: feature-folder SPA (`src/features/{calendar,game,jobs,settings,stats}`), with a dedicated `components/charts` for stats visualization — reasonably organized feature-sliced structure rather than a flat component soup
- Complexity: Junior+
- Educational material: USEFUL — `astraupskill/`
- Quality observations:
  - Feature-sliced folder structure (`features/calendar`, `features/jobs`, `features/game`, `features/stats`, `features/settings`) is a deliberate architectural choice, not a flat dump
  - Gamification (`features/game`) layered on top of a practical job-tracking domain is a distinguishing product idea versus a plain tracker
  - No dedicated git repo of its own (per memory) — provenance/history is weaker evidence here than for git-tracked projects in this batch
- Old-AI-generated smells: none seen
- Skill tags: fe-react, fe-state, fe-testing, crud-basic
- Duplicate/overlap: **significant overlap with `jobtrack` (Daybook)** — both are local-first calendar + job-application tracking apps built independently; Questboard is the more feature-rich/gamified of the two (charts, game features, Zustand, Tailwind4, TS-first) — see Batch observations
- Learning value: Medium — solid feature-sliced SPA, but the domain overlaps with `jobtrack`
- Interview stories: feature-sliced React architecture, gamification mechanics layered on a productivity tool, Zustand state design
- Proposed disposition: C SPECIALIZED — reason: well-built and more feature-complete than its sibling `jobtrack`, but the domain overlap means it should be evaluated alongside `jobtrack` for consolidation rather than as an independent flagship

## Daybook (jobtrack)
- Path: jobtrack                     — Origin: ORIGINAL + curriculum overlay (two overlapping curriculum trees present — see below)
- Type: web app
- State: working-looking - Size: 85 files - Last modified: UNKNOWN (no `.git`)
- Purpose: Private local-first planner: day/week/month calendar with events/notes/categories/completion tracking, plus a job-search pipeline (stages, company/role details, full-text search, filters, posting links, dedicated interview-notes view). Original product brief preserved in `SPEC.md`.
- Stack: FE: React18/Vite, plain JS (not TypeScript — `src/*.jsx`/`.js`) | Test: Vitest+RTL
- Architecture: simpler flat structure (`src/App.jsx`, `src/calendar/CalendarHome.jsx`, `src/JobTracker.jsx`, plus utility modules `dates.js`, `jobBackup.js`, `storage.js`, `theme.js`) — noticeably less structurally organized than `calendar+jobtrack`'s feature-sliced approach
- Complexity: Junior
- Educational material: USEFUL, but with a notable duplication of its own: this project has BOTH `astraupskill/` (the 7-file Astra pack) AND a separate, differently-structured `fabledocs/` tree (`00-fast-track.md` through `09-reference`, `08-interview-prep`, etc.) — two independent curriculum overlays covering similar ground, a redundancy worth resolving
- Quality observations:
  - Plain JS rather than TypeScript, unlike its sibling `calendar+jobtrack` — a real capability/type-safety gap between the two similar apps
  - `jobBackup.js` (a dedicated backup/export module) and a full test file for it (`jobBackup.test.js`) — a thoughtful data-durability feature for a local-only app (mitigates the "browser storage can vanish" risk)
  - `test/smoke.test.jsx` present alongside per-module tests — a deliberate smoke-test layer
  - Two full curriculum trees (`astraupskill/` + `fabledocs/`) covering the same project is itself a documentation-debt signal
- Old-AI-generated smells: none in the app code; the duplicate curriculum-tree situation is worth flagging as accumulated-overlay debt rather than a code smell
- Skill tags: fe-react, fe-testing, crud-basic
- Duplicate/overlap: **same domain as `calendar+jobtrack` (Questboard)** — Daybook is the earlier/simpler of the two (plain JS, flatter structure, no gamification, no Zustand/Tailwind); also has internal doc-tree duplication (`astraupskill/` vs `fabledocs/`)
- Learning value: Low-Medium — the backup/export feature and smoke-test layer are genuinely useful details, but the app is functionally subsumed by `calendar+jobtrack`
- Proposed disposition: F CONSOLIDATE — reason: same product idea as `calendar+jobtrack` but less capable (JS vs TS, flatter architecture, no gamification); recommend folding its distinctive `jobBackup.js` export/backup idea into `calendar+jobtrack` and archiving this one, and separately resolving the `astraupskill/`-vs-`fabledocs/` duplication before either curriculum tree is reused elsewhere

## Recipe Lab (recipeview)
- Path: recipeview                    — Origin: ORIGINAL + curriculum overlay
- Type: web app (client + server)
- State: complete (per memory record) - Size: 46 files - Last modified: 2026-07-17 (git)
- Purpose: Local-first cooking journal built around a deliberate three-level hierarchy — Dish → Recipe → Cook Log — where cook logs are kept distinct from "reviews" (each log captures its own deltas, taste notes, and process notes rather than collapsing to a star rating).
- Stack: FE: React18/Vite, plain CSS | BE: Express (`server/index.ts`, `server/queries.ts`), `multer` (photo upload) | DB: SQLite (`data/recipe-lab.db`, WAL mode — `.db-wal`/`.db-shm` files present, confirming WAL is actually enabled, not just configured) | Shared: `shared/types.ts`, `shared/quantity.ts` (a dedicated unit/quantity-conversion module) | Test: `node:test` (`tsx --test`)
- Architecture: classic client+server monolith with a raw-SQL query layer (`server/queries.ts`, `server/schema.sql`) rather than an ORM — a deliberate raw-SQL choice
- Complexity: Junior+
- Educational material: USEFUL — `astraupskill/`
- Quality observations:
  - Explicit domain modeling decision (cook logs ≠ reviews) documented and defended in the README rather than an accidental design — shows product-thinking, not just CRUD
  - Raw SQL schema + queries (no ORM) — good for demonstrating direct SQL competency
  - WAL-mode SQLite artifacts present on disk, confirming the concurrency-friendly journal mode is actually active, not just mentioned
  - Dedicated `shared/quantity.ts` for ingredient-quantity handling — a real unit-conversion/parsing problem, non-trivial domain logic
  - Photo upload via `multer` — real file-handling, not just text CRUD
- Old-AI-generated smells: none seen
- Skill tags: be-node-express, db-sqlite, db-sql-raw, db-concurrency (WAL), be-rest-design, crud-basic
- Duplicate/overlap: shares a cooking/recipe domain with `recipeweb`, but the two are functionally distinct (see `recipeweb` record and Batch observations) — not true duplicates
- Learning value: Medium-High — strong raw-SQL/domain-modeling example with a real file-upload feature
- Interview stories: deliberate raw-SQL-over-ORM tradeoff reasoning, WAL-mode SQLite concurrency, domain modeling for "logs vs. reviews," ingredient-quantity parsing/normalization
- Proposed disposition: C SPECIALIZED — reason: solid raw-SQL/domain-modeling example, valuable as a targeted SQL/data-modeling interview story, but smaller in scope than the monorepo/backend-heavy B-tier projects above

## Sarap & Ngon (recipeweb)
- Path: recipeweb                      — Origin: ORIGINAL + curriculum overlay
- Type: web app (client-only)
- State: complete-looking - Size: 60 files - Last modified: 2026-07-18 (git)
- Purpose: A Filipino/Vietnamese/Thai/Spanish cookbook companion: browse/search 74 curated recipes (linking out to original source authors for full credit/traffic), with combined shopping-list generation and check-off progress across multiple selected recipes.
- Stack: FE: React19/Vite, `react-router-dom` | BE: none (fully static/client-only) | Content: curated per-cuisine JSON files generated via `scripts/generate-recipes.mjs` (`filipino.json`, `vietnamese.json`, `thai.json`, `spanish.json`) | Lint: `oxlint` (a Rust-based fast linter, a less-common but modern choice) | Test: `tsx --test` (`test/shopping-state.test.ts`) | Infra: `vercel.json` present — actually deployed/deployable to Vercel
- Architecture: static SPA, client-side shopping-list state management, no backend or database at all
- Complexity: Junior
- Educational material: USEFUL — `astraupskill/`, `docs/` (00-START-HERE through 06-GROWTH, plus `PLAN-thai-spanish.md`), and an unusual extra `net/` folder containing a full **parallel C# rewrite plan** (`00-README.md` through `06-TESTING-AND-QUALITY.md`, including `05-CSHARP-FOR-REACT-DEVS.md`) — this is a distinctive, deliberately-designed "port this React app to .NET" learning track, not generic filler
- Quality observations:
  - Ethically considerate design: links to original recipe authors rather than scraping/republishing full instructions — a real product-ethics decision worth noting
  - The `net/` folder's C#-for-React-developers translation guide is a genuinely useful and unusual artifact — a structured bridge document from a React codebase to an equivalent .NET design
  - Uses `oxlint` (Rust-based) instead of ESLint — a modern tooling choice worth flagging as evidence of staying current
  - Fully static, no backend — appropriate for the domain (no user data to persist beyond local shopping-list state)
- Old-AI-generated smells: none seen
- Skill tags: fe-react, crud-basic (shopping-list state), db-sql-raw (not applicable — no DB; omit), legacy-codebase-reading (net/ translation guide), design-docs-adrs
- Duplicate/overlap: shares the cooking/recipe subject matter with `recipeview`, but functionally distinct — this is a curated public recipe browser + shopping list with no backend/journal features, while `recipeview` is a personal cook-log app with a real server and DB; not a true duplicate
- Learning value: Medium-High — the `net/` C#-porting-guide artifact is unusually good, distinct value-add beyond the app itself
- Transformation opportunity: The `net/` folder's plan could be executed to produce an actual C# port, turning this into a genuine "same app, two stacks" comparison portfolio piece
- Interview stories: static/serverless app architecture decisions, React-to-C# conceptual translation, ethical sourcing/attribution design in a content-aggregation app
- Proposed disposition: C SPECIALIZED — reason: simple app on its own, but the `net/` C#-porting curriculum is distinctive enough to be worth preserving and potentially executing as a cross-stack comparison piece

## Batch observations
- **The "Aral" Tagalog-learning idea appears FOUR times** in this batch (`tagalog`, `aral`, `mobiletagalog`, `aral-deploy`), each architecturally distinct rather than simple copies: `tagalog` (Next+Expo+Fastify+Postgres monorepo, the most production-shaped, with real unpushed GitHub remotes per `aral-deploy/DEPLOY.md`) is the canonical current build; `aral` is a separate, architecturally more advanced greenfield rebuild (event-log sync, Hono+tRPC+libsql) that stalled (`docs/BLOCKED.md`); `mobiletagalog` is an explicit standalone port of `tagalog`'s mobile app; `aral-deploy` is not a project at all, just a compiled content snapshot proving `tagalog` had pending pushes as of 2026-09-08. Recommend treating `tagalog` as the portfolio entry and `aral`'s design docs as a supplementary architecture case study, while archiving `mobiletagalog`/`aral-deploy` as derivative.
- **`jobtrack` and `calendar+jobtrack` are a genuine near-duplicate pair**: both are local-first "calendar + job-application tracker" apps built independently, but `calendar+jobtrack` (Questboard) is strictly more capable (TypeScript, feature-sliced architecture, Zustand, Tailwind4, gamification, charts) while `jobtrack` (Daybook) is plain-JS and flatter, with one standout feature (`jobBackup.js` export/backup) worth porting over before consolidating.
- **Two cooking-domain apps (`recipeview`, `recipeweb`) are NOT true duplicates** despite the shared subject matter — one is a personal cook-log/journal with a real Express+SQLite backend, the other is a static curated-recipe browser with a shopping list and no backend at all. Different products, same kitchen.
- **A repeating "Astra curriculum overlay" pattern** across nearly every project in this batch: a standardized 7-file `astraupskill/` pack (01-CODEBASE-MAP through 07-TRACE-LAB, plus a VERIFICATION.md and sometimes an evidence/snapshots dir), frequently paired with a `dfableandopus/` interview-prep pack (6 files: interview questions, stories-and-resume, code-reading drill, take-home, system-design followups, flashcards). This is consistent with the "Fable review + fix pass of Astra improvements" project referenced elsewhere in this archive's history — nearly every project here was likely part of that same 153-project Astra pass.
- **`jobtrack` is the one project with duplicated curriculum trees** (`astraupskill/` AND a separate, differently-structured `fabledocs/`) covering similar ground — worth resolving as documentation debt rather than treating both as independent value.
- **A recurring "preserve the pre-refactor original" convention**: both `buildbusinesses` (`docs/original/LocalOperationsApp.tsx.txt`) and `buildsql` (`docs/original/*.txt`) keep flattened snapshots of the single-file pre-upskill source alongside the refactored app — a genuinely useful before/after teaching pattern worth replicating deliberately elsewhere in the archive rather than treating as incidental.
- **Notable gap**: almost no server-side test coverage gap flags surfaced except in `buildevent` (`web` app's test script is a literal no-op echo) — otherwise this batch shows unusually consistent test-suite presence across both frontend and backend layers, a positive signal relative to typical AI-generated-app patterns.
- **Two projects have no `.git` in their directory** (`buildwhiteboard`, `calendar+jobtrack`, `jobtrack`) — completeness/history claims for these three rely on file contents and (where available) prior memory records rather than commit history; flag for a "does this need its own repo" pass in any later consolidation stage.
- **Rarity note**: `borrowbox` is the only C#/.NET project in this batch (and has the deepest documentation of the batch); nearly everything else is TypeScript/React-centric, so it's disproportionately valuable for demonstrating backend-language range.
