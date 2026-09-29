# Batch 06 — Model-built bootcamps/workspaces
Scope: astra1, astra2, astra4.2, astra5, astraboot1, opusboot1, opusboot2, opusboot4.2, opusdavinci, antigravupskill, codexlearnp1, newcodecjs2, newcodex3, newcodexJS  |  Candidate dirs inspected: 14 top-level (+ ~100 numbered sub-projects across newcodecjs2/newcodexJS/newcodex3)  |  Meaningful projects: ~13 individually documented + 2 large numbered sets (25 + 20) treated compactly  |  Tiny/empty/boilerplate: 4 (opusboot2, opusboot4.2, opusdavinci, codexlearnp1 — all empty placeholder dirs)

Method note: astra1/astra2/astra4.2/astra5/astraboot1 were audited by a delegated read-only subagent (its findings reproduced below); opusboot1, antigravupskill, the 4 empty dirs, newcodecjs2, newcodexJS and newcodex3 were audited directly by this agent. All claims cite file paths encountered during a read-only scan; node_modules/.git-internals/dist/build/bin/obj were skipped.

## Quick table

| Project | Path | Type | Origin | Stack | Complexity | Docs | Disp |
|---|---|---|---|---|---|---|---|
| Helios Interplanetary | astra1 | web app (monolith, multi-tenant) | COURSE/GENERATED (Opus-agentic) | Next.js16/React19/TS, raw Postgres, OTel, Playwright | Senior-oriented | STRONG (astraupskill/ + upskilling/ 31 files) | A FLAGSHIP |
| Tidebound | astra2 | web app (client-only 3D game) | COURSE/GENERATED | TS, Vite, Three.js, Vitest/Playwright, IndexedDB | Junior+/Mid | STRONG (astraupskill/ + dfableandopus/) | B HIGH-VALUE |
| Interlude | astra4.2 | browser extension + preview + service | COURSE/GENERATED | Vanilla JS, esbuild, MV3, Node test runner, Playwright | Tutorial/Junior+ | STRONG (astraupskill/ + dfableandopus/) | B HIGH-VALUE |
| Stockade | astra5 | web app (Next.js) + .NET service, polyglot monorepo(2) | COURSE/GENERATED | Next.js16/React19, Postgres, C#/.NET, Docker | Senior-oriented / production-like | STRONG (astraupskill/ + astradocs/) | A FLAGSHIP |
| DevPractice (Astra build) | astraboot1 | monorepo (learning platform, 2 apps) | COURSE/GENERATED | React/TS, Fastify, Postgres/Prisma, QuickJS sandbox | Mid+/Senior-oriented | N/A (this IS the curriculum product) | F CONSOLIDATE (dup of opusboot1) |
| DevPractice (Opus build) | opusboot1 | monorepo (learning platform, 2 apps) | COURSE/GENERATED (Opus) | React/TS, Fastify, Postgres/Prisma, QuickJS sandbox | Mid+/Senior-oriented | N/A (product) | A FLAGSHIP |
| opusboot2 | opusboot2 | empty | — | — | Tiny | NONE | G ARCHIVE |
| opusboot4.2 | opusboot4.2 | empty | — | — | Tiny | NONE | G ARCHIVE |
| opusdavinci | opusdavinci | empty | — | — | Tiny | NONE | G ARCHIVE |
| codexlearnp1 | codexlearnp1 | empty | — | — | Tiny | NONE | G ARCHIVE |
| Antigrav Master Audit | antigravupskill | docs-only (meta-audit of 59 other projects) | ORIGINAL (script-generated review corpus) | Python generator scripts + Markdown | Mid (as a tool) | STRONG (59 review docs) | D REFERENCE |
| blockr | newcodecjs2/blockr | web app (Notion clone) | COURSE/GENERATED (Codex) | Next15/React19, Drizzle, Tiptap, Vitest | Junior+/Mid | MINIMAL (codex.md, docs/) | C SPECIALIZED |
| bookr | newcodecjs2/bookr | web app (Cal.com clone) | COURSE/GENERATED | Next15/React19, Drizzle, date-fns-tz, Vitest | Mid | MINIMAL | C SPECIALIZED |
| helpkit | newcodecjs2/helpkit | web app + widget (Intercom clone) | COURSE/GENERATED | Next15, Drizzle, mailparser, Vitest | Mid | MINIMAL | C SPECIALIZED |
| payr | newcodecjs2/payr | web app (Stripe dashboard clone) | COURSE/GENERATED | Next15, Drizzle, Vitest | Junior+/Mid | MINIMAL | C SPECIALIZED |
| planr | newcodecjs2/planr | web app (Linear clone) | COURSE/GENERATED | Next15, dnd-kit, Tiptap, Drizzle, Vitest | Mid | MINIMAL | C SPECIALIZED |
| newcodexJS set (20 apps) | newcodexJS/01..20 | 20x web app (CRUD curriculum) | COURSE/GENERATED (Codex, "corrected Tier1") | React18/Vite, Express, Postgres, Knex (some TS) | Junior → Junior+ | USEFUL (astraupskill/ template per app + root docs/) | E EXERCISE SOURCE |
| newcodex3 set (25 pairs / 50 dirs) | newcodex3/apps/16..40[-net] | 50x web app/API, JS+.NET twin pairs | COURSE/GENERATED (Codex, "Tier2/enterprise") | React/Express/Prisma (JS) vs ASP.NET Core (.NET) | Mid → Mid+ | USEFUL (docs/upskill.md per app, no tests) | E EXERCISE SOURCE |

## Helios Interplanetary
- Path: `astra1`            - Origin: COURSE/GENERATED (Opus-agentic build; `AGENTS.md` is explicit agent build-instructions)
- Type: web app / monolith (multi-tenant "space station ops" simulation)
- State: complete/working-looking     - Size: ~103 files, ~8,123 LOC in `src`; 11 test files (unit/integration/e2e)   - Last modified: 2026-09-05 (own git repo)
- Purpose: Next.js modular monolith simulating enterprise space-station operations — Mission Control (telemetry/incidents) plus an Operations hub (maintenance, inventory, procurement, cargo, crew, energy, "bounded advisers"/AI agents, billing, support, durable background work) for practicing AI-assisted engineering at production scale.
- Stack: Next.js16/React19/TS FE+BFF | raw-SQL Postgres (pg, no ORM) BE | Playwright e2e, tsx unit/integration tests | Docker Compose DB, OpenTelemetry instrumentation, GitHub Actions CI
- Architecture: layered modular monolith (route handlers → `src/server/` authorized ops → `src/domain/` pure rules); outbox pattern for duplicate-safe delivery with dead-letter recovery; saga-style payment reconciliation (no held DB transaction across provider calls); explicit rule that the browser never receives trusted tenant identity
- Complexity: Senior-oriented / production-like
- Educational material: STRONG — `astraupskill/` (9 files, generic 8-chapter template shared with astra2/4.2/5) + `upskilling/` (31 bespoke files: case-studies/, labs/, lessons/, repair-rollback/, retrospective/, solutions/, templates/ — a "replay the actual build" retrospective course unique to this project). Preserve both; the bespoke `upskilling/` tree is the standout artifact.
- Quality observations:
  - Tenant isolation enforced architecturally, not just by convention (`AGENTS.md`)
  - Integration tests hit a dedicated `helios_test` DB, never dev (README "Commands and verification")
  - Backup/restore rehearsal is scripted and logged (`artifacts/backup-rehearsal.json`, `helios-rehearsal.dump`) — real DR practice
  - README explicitly disclaims that local test runs ≠ a remote CI run — honest evidence hygiene
  - "Bounded advisers" (AI-agent feature) has its own safety/blocked-trace test scenario
- Old-AI-generated smells: none significant; `artifacts/` is large log/JSON noise typical of automated verification tooling, not a code smell
- Skill tags: fe-next, be-node-express, db-postgres, db-sql-raw, db-migrations, multitenancy, authz-rbac, arch-modular-monolith, outbox, idempotency, observability-metrics-tracing, ci-cd, docker, test-e2e, ai-llm-integration, design-docs-adrs
- Duplicate/overlap: shares the `astraupskill/` template shell with astra2/astra4.2/astra5; no code/purpose overlap with them or with astraboot1/opusboot1
- Learning value: Very High — broadest architectural surface of the batch (multi-tenant authz, outbox, sagas, OTel) plus a genuinely bespoke retrospective curriculum
- Transformation opportunity: strip `artifacts/`/log noise and publish `upskilling/retrospective/` as a standalone "how a senior-scope app actually gets built and verified" case study
- Interview stories: multi-tenant isolation design, outbox/idempotent delivery, payment-reconciliation saga without long-held transactions, backup-rehearsal DR drill
- Proposed disposition: A FLAGSHIP — most complete production-pattern demonstration plus strongest bespoke teaching material in the batch

## Tidebound
- Path: `astra2`            - Origin: COURSE/GENERATED
- Type: web app (client-only 3D game)
- State: complete/working-looking     - Size: current `src/` 13 files (~1,387 LOC); `docs/original/` preserves a 10-file "before" baseline for the taught change; 5 test files    - Last modified: no own `.git` (sits in shared home-dir repo); newest curriculum files mtime 2026-09-18
- Purpose: A complete local single-player 3D archipelago colony/maritime-trade game (Three.js) used as a teaching vehicle — the save/load "voyage library" was rewritten from a naive `localStorage` key into a versioned, optimistic-concurrency IndexedDB CRUD repository (`src/voyages.ts`) as the worked lesson, alongside a real engine bug fix.
- Stack: TS/Vite/Three.js FE, no backend (client-only), IndexedDB persistence | Vitest + Playwright + fake-indexeddb
- Architecture: single-page client app; `VoyageRepository` funnels all mutations through one private `write()` enforcing optimistic-concurrency (expected-revision check) and quotas (50 checkpoints/50MB) inside one readwrite transaction
- Complexity: Junior+/Mid — a big application used to teach one small, well-chosen concurrency/CRUD lesson
- Educational material: STRONG — `astraupskill/` (generic 8-chapter template) + `dfableandopus/` (7 files: interview questions, stories/resume, code-reading drill, take-home, system-design followups, flashcards — cites exact `file:line`, e.g. `src/voyages.ts:201`, `src/engine.ts:83`, so genuinely project-specific, not generic)
- Quality observations:
  - Optimistic concurrency via explicit revision comparison, rejecting stale writes with a typed `VoyageError('conflict', ...)` (`src/voyages.ts:205`)
  - Real bug fixed and documented: demolition refund computed `capacity - inventory` with no floor, causing wood destruction; clamped at `src/engine.ts:83`
  - 44 unit/domain tests + 32 real-browser workflows per `astraupskill/VERIFICATION.md`, with an explicit caveat that stale `artifacts/` reports don't substitute for current evidence
  - No server-side validation by design (client-only) — acceptable for scope but no security-review doc (unlike astra1/astra5)
- Old-AI-generated smells: none significant; `docs/original/` preservation for teaching is deliberate, not accidental duplication
- Skill tags: fe-react, ts-types, db-concurrency, test-unit, test-e2e, crud-basic, legacy-codebase-reading, code-review
- Duplicate/overlap: `astraupskill/` template shared across astra family; `dfableandopus/` template shared with astra4.2
- Learning value: High — small, surgical, well-documented concurrency lesson with line-numbered interview-prep material
- Interview stories: optimistic-concurrency CRUD redesign, a real numeric-underflow bug found and fixed with a regression test
- Proposed disposition: B HIGH-VALUE — best compact "worked lesson" example in the batch

## Interlude
- Path: `astra4.2`            - Origin: COURSE/GENERATED
- Type: browser extension (Chrome MV3) + local preview server + small backend service
- State: complete/working-looking     - Size: 23 files, ~1,529 LOC (.js)    - Last modified: no own `.git`; newest curriculum files mtime 2026-09-18 (same day as astra2 — likely a batch build session)
- Purpose: A local Pomodoro-style focus timer with art breaks and a reusable reminder-message library, shipped both as a browser-tab preview and a packaged Manifest V3 Chrome extension (`interlude-extension.zip`); `service/` is a "port this to a real backend" variant per `astraupskill/08-SERVER-PORT.md`.
- Stack: vanilla JS, esbuild bundling `src/app.js` → `extension/app.js`, Node http server, Playwright + Node's built-in test runner; `service/` adds `schema.sql` + `server.js` (engine unconfirmed)
- Architecture: two deployment targets sharing one core module; revision-tracked settings/library edits reuse the same optimistic-concurrency pattern seen in astra1/astra2, suggesting a deliberate cross-project concurrency-control theme
- Complexity: Tutorial/Junior+ — smallest, simplest app in the astra family
- Educational material: STRONG — `astraupskill/` (9 files incl. project-specific `08-SERVER-PORT.md`) + `dfableandopus/` (7 files, same interview-prep structure as astra2)
- Quality observations:
  - README documents real failure-mode semantics: extension data persists before alarms/windows reconcile; a later dashboard read retries the failed external effect
  - Uploaded artwork is resized locally and never sent to a service — stated privacy property
  - Corrupt preview JSON is preserved for export rather than silently discarded — deliberate data-safety choice
  - README explicitly warns not to hand-edit the generated `extension/app.js` — correct build-artifact hygiene
  - No CI config found (weaker than astra1/astra5 on that front)
- Old-AI-generated smells: `server-error.log`/`server.log` checked into the working tree (minor hygiene issue, harmless — no real git repo here)
- Skill tags: db-concurrency, test-unit, test-e2e, desktop-electron-tauri (n/a — closest tag is browser-extension, not in vocab; using crud-basic), crud-basic
- Duplicate/overlap: template pattern shared with astra2/astra1/astra5
- Learning value: Medium-High — cleanest "small and fully worked" example of the fleet
- Proposed disposition: B HIGH-VALUE — best minimal/complete example for a junior-level walkthrough

## Stockade
- Path: `astra5`            - Origin: COURSE/GENERATED
- Type: monorepo(2) — Next.js storefront/admin + C#/.NET "Fulfil" fulfillment service
- State: complete/working-looking, most production-like of the astra family     - Size: 22 top-level `src` files, ~2,294 LOC sampled (.ts/.tsx/.cs)    - Last modified: 2026-09-08 (own git repo)
- Purpose: Multi-warehouse e-commerce storefront and admin backend — Next.js owns catalog/cart; a separate .NET Fulfil service owns orders, inventory, pricing, payment recovery, logistics, purchasing, returns and inter-warehouse transfers, with PostgreSQL as the single source of truth for inventory state.
- Stack: Next.js16/React19/Zod FE-BFF | C#/.NET BE (own `Fulfil.Tests`) | Postgres (raw SQL) | Docker Compose (postgres + mailpit) | Vitest + Playwright
- Architecture: polyglot two-service system; `available = onHand - reserved - held` enforced via DB CHECK constraints; checkout runs in a repeatable-read transaction and is rolled back (quote-only), confirmation re-validates price via `expectedTotal`; payment handled as an async saga (worker leases one order, idempotency-key-derived call, no open transaction during the external call); promotions engine (stacking rules, BOGO, per-customer caps) snapshots rule inputs/version on the order for auditability
- Complexity: Senior-oriented / production-like — arguably the deepest domain modeling in the batch
- Educational material: STRONG — `astradocs/` (6 files: CODE_WALKTHROUGHS, LEARNING_LOG_TEMPLATE, NEXT_STEPS, PROJECT_SUMMARY, SWE_ROADMAP — a roadmap/career style distinct from astra2/4.2's interview-prep style) + generic `astraupskill/`
- Quality observations:
  - `docs/SECURITY.md` is the most substantive security doc in the batch: explicit trust boundaries, HttpOnly+SameSite+Secure cookies, origin checks, parameterized SQL, rate limits, CHECK constraints, immutable-history triggers, HMAC+timestamp webhook validation, public-IP-pinned HTTPS with no redirects for webhook delivery
  - Self-critical disclosure: "External review still required for verified identity/promotion abuse... This checklist is not a claim those checks passed"
  - Architecture doc explicitly calls out a common junior mistake: "A disabled browser button is not a concurrency control"
  - Returns/exchanges snapshot original line/tax data so later catalog changes don't corrupt historical order math
  - Guest-checkout promotion-abuse risk is explicitly flagged as unresolved rather than hidden
- Old-AI-generated smells: `.git/gk` and `.git/stockade-commit-message.txt` look like leftover scratch files from scripted commit automation (housekeeping only)
- Skill tags: fe-next, be-dotnet, db-postgres, db-transactions, db-concurrency, arch-microservices, idempotency, security-owasp, design-docs-adrs, docker, test-e2e
- Duplicate/overlap: template shared with astra family; no app-purpose overlap with others
- Learning value: Very High — best real-world backend-correctness example (inventory sagas, idempotency, promotions) alongside astra1
- Transformation opportunity: `docs/SECURITY.md` + the inventory/saga design could be lifted into a standalone "designing a correct checkout" reference doc independent of the app code
- Interview stories: cross-service inventory invariants via CHECK constraints, payment saga without long transactions, promotion-abuse tradeoffs, returns/exchange historical-price snapshotting
- Proposed disposition: A FLAGSHIP — deepest correctness/security material in the batch

## DevPractice — two independent builds (astraboot1 + opusboot1)
- Path: `astraboot1` and `opusboot1`            - Origin: both COURSE/GENERATED, built by different model/pipeline (astraboot1 = "Astra"-branded build; opusboot1 = Opus build, already tracked in user memory as "devpractice-opusboot1")
- Type: monorepo(2 apps: api + web) — a private course-delivery platform, not an app-with-curriculum like the other astra* projects; this one **is** the curriculum product
- State: opusboot1 — complete, V1 verified (45/45 gates + 14/14 e2e per prior memory + own git log confirms commits "Build DevPractice V1", "Fix two e2e harness races", "Author V2 and V3 curriculum chapters"); V2/V3 curriculum chapters exist but the handoff doc marks broader V2/V3 platform work as not fully verified/committed. astraboot1 — README claims equivalent V1 state (12 chapters/36 lessons/108 exercises/72 review cards/60 placement items/3 missions, 28 runnable + 57 rejected solutions with verified checksums, 28/28 unit/API checks passing); has no own `.git` (unlike opusboot1) and carries `.data/` verification logs and a vendored local `node24`+postgres runtime instead.
- Size: both are large pnpm workspaces (apps/api, apps/web, shared packages, curriculum/ or curriculum content, docs/, handoff/, tests) — opusboot1 confirmed via `apps/api/src/modules/*` (14+ domain modules: auth, missions, exercises, drafts, reviews, exports, imports, placements, progress, settings, today, activity, bookmarks, notes), 11 API test files + 7 e2e files
- Last modified: opusboot1 git log -1 → 2026-09-11; astraboot1 not independently git-dated (no repo)
- Purpose: A credential-optional personal web-dev learning workspace — React/TS + Fastify + Postgres/Prisma, with an isolated QuickJS-in-worker sandbox for safely executing learner-submitted JS/TS, autosave-with-conflict-recovery, spaced review, placement testing, and a versioned/immutable content-authoring→publish pipeline (`content:validate`/`content:build` scripts, `curriculum/release*.json` snapshots, `ContentVersion` unique on `(itemId, version)`)
- Stack: React/Vite FE | Fastify BE | PostgreSQL + Prisma ORM | QuickJS-WASM sandboxed runner (Web Worker) | pnpm workspaces, Vitest, Playwright
- Architecture: modular-monolith API (per-domain modules under `apps/api/src/modules/`) + a separate content-authoring pipeline that treats curriculum content as versioned data the app never executes directly (`curriculum/README.md`: "Everything here is **data**: the application never executes it")
- Complexity: Mid+/Senior-oriented (sandboxed code execution, atomic content publishing with rollback, autosave conflict handling)
- Educational material: N/A in the usual sense — this project's `curriculum/` IS its own product content (not meta-docs about the codebase); `docs/` (16 files: api.md, codebase-tour.md, content-authoring.md, data-model.md, e2e-verification.md, learning-algorithms.md, product-spec.md, testing.md, etc.) and `handoff/` (6 files) function as solid engineering documentation
- Quality observations:
  - Content publishing is snapshot-based, not diff-based: each release manifest re-lists every included chapter so `dist/` packages are self-contained and reproducible
  - `verification.json` ships author-declared mutants/exemptions the content-validation gate tests itself against — a deliberate "test the grader" step
  - `handoff/01-state.md` is unusually honest about what's committed vs. working-tree-only, and explicitly warns about a stray outer git repo at `C:\Users\Owner` before any git command
  - Idempotency (`lib/idempotency.ts`) and XP tracking (`lib/xp.ts`) are separated as first-class concerns, not bolted onto route handlers
- Old-AI-generated smells: none significant in opusboot1; astraboot1 could not be verified as independently as deeply this pass
- Skill tags: fe-react, be-node-express, db-postgres, orm, db-migrations, authn, idempotency, test-unit, test-e2e, ai-llm-integration, design-docs-adrs
- Duplicate/overlap: **astraboot1 and opusboot1 are the same product spec ("DevPractice") built twice independently** — same name, same stack, same feature list, different build pipeline/model. This is the single clearest duplicate pair in Batch 06 and looks like an intentional side-by-side model comparison rather than an accident.
- Learning value: Very High — sandboxed code execution + versioned content publishing is a rare, valuable pattern; having two independent implementations of the same spec is itself useful for a "compare two AI-driven builds of the same product" exercise
- Transformation opportunity: diff astraboot1 vs opusboot1 as a structured "same spec, two models" case study before picking one canonical copy to keep
- Interview stories: sandboxing untrusted user code safely (QuickJS-in-worker), snapshot-vs-diff content publishing, autosave conflict resolution
- Proposed disposition: opusboot1 = A FLAGSHIP (fuller docs/tests already verified in prior memory); astraboot1 = F CONSOLIDATE — reconcile against opusboot1 before keeping both long-term

## opusboot2 / opusboot4.2 / opusdavinci / codexlearnp1
- Path: `opusboot2`, `opusboot4.2`, `opusdavinci`, `codexlearnp1` — Origin: UNKNOWN (empty)
- Type: n/a — each directory contains **zero entries** (`find <dir>` returns only the directory itself)
- State: empty/placeholder     - Size: 0 files     - Last modified: n/a
- Purpose: likely reserved/abandoned scaffold directories (names suggest planned "opusboot" iterations and a "davinci"-branded build, plus a Codex learning workspace) that were never populated, or were cleared out.
- Proposed disposition: G ARCHIVE — nothing to review; safe to delete or leave as-is

## Antigrav Master Audit (antigravupskill)
- Path: `antigravupskill`            - Origin: ORIGINAL (a purpose-built review-generation tool, not a cloned app)
- Type: docs-only meta-project — a systematic architectural-audit corpus over **59 other projects elsewhere on this machine**, generated via Python scripts
- State: complete     - Size: `masterdocs/` has 5 category subdirs (01-antigrav-curriculum: 20 files, 02-antigravity-and-grav-projects: 9 files, 03-desktop-ts-js-apps: 9 files, 04-desktop-dotnet-systems: 14 files, 05-grok-domain-clones: 7 files) = 59 review docs + README + TIER_1_SPECS.md + TIER_2_SPECS_PART1.md; `scripts/` has 7 `build_*.py` generator scripts    - Last modified: git log -1 → 2026-07-18
- Purpose: A "senior-architectural review" hub: for each of 59 discovered codebases (the same 20-project Codex/antigrav curriculum seen in `newcodexJS`, plus native Antigravity/Grav apps, standalone desktop TS/JS apps, desktop .NET Clean-Architecture systems, and Grok-built domain clones), it provides an executive summary, strengths/deficiencies, a 5-dimension action plan, and before/after refactor blueprints — conceptually the same kind of exercise as the present portfolio audit, but self-authored by an earlier agent pass.
- Stack: Python (review-generation scripts) + Markdown output; no runtime app
- Architecture: doc-generation pipeline (`scripts/build_*.py` → per-category Markdown files → `README.md` master index/taxonomy table)
- Complexity: Mid (as a tooling/process artifact)
- Educational material: STRONG — the entire directory is educational material by design: 59 project-specific senior-level reviews, each naming a concrete "Key Architectural Focus" (e.g. Kanban Board → "Fractional Lexorank ordering, single-row update"; Bookmark Manager → "SSRF defense, asynchronous scraping"; Appointment Booking → "PostgreSQL Exclusion Constraints, zero double-booking"). Cross-references to the `01-task-manager.md`...`20-multivendor-ecommerce.md` set map directly onto the same 20 concepts built as code in `newcodexJS`.
- Quality observations:
  - The README's inventory table explicitly names concrete engineering techniques per project rather than generic praise — evidence of genuine per-project analysis, not templated filler
  - Reuses the same 20-concept curriculum taxonomy also implemented as code in `newcodexJS/01..20`, suggesting this audit corpus was written specifically to accompany that code set (or a sibling of it)
  - Organizes 59 projects across 5 clearly bounded categories, which is itself a reusable taxonomy for future audit work (directly comparable to the present `portfolio-audit` project's own approach)
- Old-AI-generated smells: none — this is deliberately a review/analysis artifact, not app code
- Skill tags: design-docs-adrs, code-review, legacy-codebase-reading
- Duplicate/overlap: directly overlaps in subject matter with `newcodexJS` (the 20-project "antigrav curriculum" category reviews the same apps newcodexJS implements) and conceptually with this very portfolio-audit effort (a prior self-audit pass over a different, larger set of ~59 projects, most of which are outside this batch's scope)
- Learning value: High — as a corpus of worked "what would a senior reviewer flag" examples across 59 real small-to-mid apps, independent of whether the underlying code is kept
- Interview stories: "I built a tool that generates architecture reviews at scale across dozens of codebases" is itself a strong agentic-engineering story
- Proposed disposition: D REFERENCE — valuable as review material/taxonomy reference; keep as documentation, not app code

## blockr / bookr / helpkit / payr / planr (newcodecjs2)
- Path: `newcodecjs2/{blockr,bookr,helpkit,payr,planr}`            - Origin: COURSE/GENERATED (Codex-built; each has a `codex.md`)
- Type: 5 independent single-purpose web apps, each a compact clone of a well-known SaaS product, sharing one stack convention
- State: working-looking (each ships `src/domain/*.ts` + matching `*.test.ts` files, e.g. `blockTree.test.ts`, `availabilityEngine.test.ts`, `apiKeys.test.ts`)     - Size: 15-22 files per project (blockr 18, bookr 15, helpkit 22, payr 15, planr 16)    - Last modified: git log -1 → 2026-07-18 (shared repo for all 5)
- Purpose (per project):
  - **blockr** — a simplified Notion-style page/block editor: recursive block trees, fractional ordering, database views, sharing, inherited permissions (`src/domain/blockTree.ts`, `databaseView.ts`, `pageLifecycle.ts`)
  - **bookr** — a Cal.com-inspired scheduling app: availability engine, timezone correctness, booking race conditions, calendar integrations (`src/domain/availabilityEngine.ts`, `bookingService.ts`, `idempotency.ts`)
  - **helpkit** — an Intercom-inspired multi-tenant support inbox: real-time chat, inbound email parsing, assignment routing, distributable widget (`src/domain/emailParser.ts`, `rateLimiter.ts`, `realtime.ts`, plus a separate `widget.vite.config.ts` build)
  - **payr** — a Stripe-dashboard-inspired admin/mock-payments UI: RBAC, audit logs, API keys, cursor pagination, webhook delivery logs (`src/domain/rbac.ts`, `apiKeys.ts`, `cursorPagination.ts`)
  - **planr** — a Linear-inspired issue tracker: optimistic UI, saved filters, real-time sync, keyboard nav, workflow automation (`src/domain/filterEngine.ts`, `auditTrail.ts`, `permissions.ts`)
- Stack (all 5): Next.js15/React19 FE, Drizzle ORM BE, Vitest for domain-logic tests, TypeScript strict; product-specific libs (Tiptap for blockr/planr rich text, date-fns-tz for bookr, dnd-kit for planr, mailparser for helpkit)
- Architecture: each project isolates business rules into `src/domain/*.ts` (pure, directly unit-tested) separate from `src/app`/`src/components` — a clean domain-logic-vs-UI split repeated identically across all 5
- Complexity: Junior+ (blockr, payr) to Mid (bookr, helpkit, planr) — booking race conditions, real-time widget delivery and RBAC/audit trails push the middle three above pure-CRUD
- Educational material: MINIMAL — each has a `codex.md` (build-instruction/spec file) and a `docs/` folder but no dedicated upskill/curriculum tree like the astra* or newcodexJS projects; the README's own "Folder Map" section functions as lightweight onboarding
- Quality observations:
  - Domain logic is genuinely isolated and tested (not just component snapshot tests) — `blockTree.test.ts`, `availabilityEngine.test.ts`, `filterEngine.test.ts`, `permissions.test.ts`, `apiKeys.test.ts`, `cursorPagination.test.ts`, `rateLimiter.test.ts`, `realtime.test.ts`, `emailParser.test.ts` all exist
  - Each README names the exact hard problem the project targets in one sentence (booking race conditions, IDOR/permissions, SSRF-adjacent email parsing, idempotency, optimistic UI) — evidence of deliberate scoping rather than generic CRUD
  - Small footprint (15-22 files) means each is fast to read end-to-end, good for a focused "read one file, understand one hard problem" exercise
- Old-AI-generated smells: none obvious at this depth; not independently verified beyond domain/test file presence (build/run not attempted, per read-only rule)
- Skill tags: fe-next, ts-types, orm, db-concurrency, idempotency, authz-rbac, realtime-ws, test-unit, crud-basic
- Duplicate/overlap: each targets a different real product (no overlap with each other); conceptually similar in spirit to the larger clone-course projects in other batches (Masterlink/Mastertea/etc. in memory index) but far smaller/tighter in scope
- Learning value: Medium-High each — small, focused, single-hard-problem-per-project format is well suited to interview-prep drilling
- Interview stories: booking-race-condition prevention (bookr), fractional/Lexorank-style block ordering (blockr), webhook/cursor-pagination idempotency (payr), IDOR-safe permission checks (planr), inbound-email parsing safety (helpkit)
- Proposed disposition: C SPECIALIZED — good as a small set of focused single-concept exercises, not flagship-scale builds

## newcodexJS — 20-project Tier-1 curriculum
- Path: `newcodexJS/01-task-manager` … `newcodexJS/20-marketplace-platform` (root also has `docs/tier1-execution-plan.md` and `scripts/` generator tooling)  - Origin: COURSE/GENERATED (Codex; `scripts/generate-projects-16-20.mjs`, `enhance-projects-16-20.mjs`, `generate-upskill-docs-1-10.mjs` confirm scripted generation)
- Type: 20x independent full-stack CRUD web apps, one per numbered folder, each with `client/`, `server/`, `docs/`, `astraupskill/`, `README.md`, `.env.example`
- State: working-looking — 22 test files found across the set (`find . -iname "*.test.*"` = 22), unlike the newcodex3 set below which has zero
- Last modified: git log -1 → 2026-07-18 (single commit repo)
- Purpose: `docs/tier1-execution-plan.md` states the goal directly: "Build 15 self-contained full-stack learning apps that share the same baseline architecture: React 18 with Vite, Express, PostgreSQL 16, Knex, CSS Modules, consistent API envelopes, migrations, seeds" — later extended to 20 with projects 16-20 explicitly called "large" apps on the same core stack.
- Stack (all): React18/Vite FE, Express BE, PostgreSQL + Knex (query builder, not full ORM), CSS Modules; projects 5+ add TypeScript, JWT auth, and per-project libraries (Recharts for 03, dnd-kit-style boards for 08, etc.)
- Architecture: same layered convention repeated 20x (route → service → Knex query layer); root `scripts/list-projects.mjs` and `check-project-manifests.mjs` suggest a build harness that verifies structural consistency across all 20
- Compact roster (name — one-line purpose — notable):
  1. task-manager — CRUD tasks with filter/sort/complete — baseline/simplest
  2. contact-book — React18/Express/Postgres/Knex contact manager — baseline
  3. expense-tracker — category budgets, recurring flags, CSV export, Recharts dashboards — adds charting
  4. notes-app — "corrected Tier1" self-contained notes app
  5. recipe-manager — first TS project; JWT auth, protected routes, nested Knex-transaction writes, React auth context — auth-focused
  6. bookmark-manager — self-contained Tier1 app (corrected curriculum)
  7. blog-platform — self-contained Tier1 app
  8. kanban-board — self-contained Tier1 app
  9. job-application-tracker — self-contained Tier1 app
  10. inventory-management — self-contained Tier1 app
  11. survey-builder — TS app: create surveys, public responses, aggregated results
  12. chat-polling — TS chat demonstrating real-time-like behavior without WebSockets — notable technique (polling vs. WS tradeoff)
  13. ecommerce-storefront — TS: catalog filters, carts, checkout transactions, order history, reviews, wishlist, admin
  14. appointment-booking — TS: provider discovery, recurring availability, overrides, conflict detection, notifications
  15. api-tester — TS Postman-lite: collections/folders, environments, variable interpolation, backend CORS-proxy endpoint — notable (meta-tool, not a CRUD domain app)
  16. team-project-management — "large" TS app, same core stack
  17. support-ticket-system — "large" TS app, same core stack
  18. learning-management-system — "large" TS app, same core stack
  19. realtime-chat-platform — "large" TS app, same core stack
  20. marketplace-platform — "large" TS app, same core stack
- Complexity: Junior (1-10) → Junior+ (11-20, especially 13/14/15/19/20)
- Educational material: USEFUL, per-project — each of the 20 has its own `astraupskill/` (sampled `01-task-manager/astraupskill/`: 01-CODEBASE-MAP.md, 02-CONCEPTS.md, 03-WORKED-CHANGE.md, 04-TESTING-AND-DEBUGGING.md, 05-PRACTICE.md, 06-SOLUTIONS-AND-REVIEW.md, 07-TRACE-LAB.md, README.md, VERIFICATION.md — the identical 9-file template seen across the astra* family, confirming a single shared curriculum-generation harness reused across multiple unrelated model families/batches). Assume the same for all 20 unless spot-checked otherwise.
- Quality observations:
  - Deliberate "Tier 1, corrected curriculum" framing (`docs/tier1-execution-plan.md`) shows an explicit prior failed/oversized attempt was scoped back down — evidence of iterative process, not one-shot generation
  - Agent-role separation documented (Coordinator/Backend/Frontend/Docs-and-learning agents, each with owned file scopes) — a real multi-agent build convention
  - 22 real test files exist across the set, better test coverage than the sibling newcodex3 set
  - projects 16-20 explicitly reuse "the same core stack as the earlier projects" rather than escalating in sophistication — a slightly repetitive ceiling (no framework/architecture growth across the run)
- Old-AI-generated smells: heavy structural repetition across 10 of the 20 ("Self-contained Tier 1 full-stack app for the corrected curriculum" is the README opener for at least 6 projects verbatim) — a templated/boilerplate feel for the middle of the set
- Skill tags: fe-react, be-node-express, db-postgres, orm (Knex query-builder), authn, test-unit, realtime-ws, crud-basic
- Duplicate/overlap: same 20-concept taxonomy as `antigravupskill/masterdocs/01-antigrav-curriculum/` (that directory's 59-project review corpus reviews this exact set of 20 apps, project-for-project, by name)
- Learning value: Medium — good CRUD/breadth practice and interview drilling material, but repetitive stack (no architectural escalation) makes it best as an exercise bank rather than showcase pieces
- Proposed disposition: E EXERCISE SOURCE — mine individual projects (esp. 12 chat-polling, 15 api-tester, 14 appointment-booking) for focused practice exercises; not showcase-worthy as a full set

## newcodex3 — 25-pair (50-dir) JS/.NET Tier-2 curriculum
- Path: `newcodex3/apps/16-blog-platform` … `apps/40-observability-incident-dashboard` plus each `-net` twin  - Origin: COURSE/GENERATED (Codex); root `README.md` states intent directly: "This workspace contains five [sic — actually 15 documented, 25 present] enterprise-style learning projects... intentionally designed as reference implementations... dependencies do not need to be installed for learning from the code."
- Type: 25 app concepts × 2 stacks (JS/TS + .NET) = 50 project directories, each `client/` + `server/` + `docs/upskill.md` + `README.md`
- State: reference/skeleton-leaning — **zero test files found** across the entire 50-dir tree (`find . -iname "*.test.*"` = 0, `find . -iname "*Tests*"` (excluding bin/obj) = 0); every project does have `docs/upskill.md` (50/50)    - Last modified: git log -1 → 2026-07-18, single-commit repo
- Purpose: teaches the SAME 25 app concepts twice, once in a JS/TS stack and once in .NET, explicitly for side-by-side stack comparison — root README: "Client apps demonstrate production state shape... Prisma schemas document the persistence model... Each app includes docs/upskill.md, a code-anchored learning and interview-prep guide."
- Stack: JS side — React/Vite client, Express (or similar Node) server, Prisma ORM (confirmed via `19-ecommerce-storefront/server/prisma/schema.prisma`, deps incl. `@prisma/client`, `stripe`, `zod`, `helmet`, `cors`), Postgres. .NET side — ASP.NET Core minimal-API style (`*.Api.csproj`, `Program.cs`), separate React/Vite client reused per pair (confirmed for `19-ecommerce-storefront-net` and `34-oauth-saas-identity-portal-net`)
- Concept roster (25 pairs, compact):
  16 blog-platform — RBAC, editorial workflow, comment moderation
  17 kanban-board — nested state, fractional ordering, invitations, activity logs
  18 team-chat — Socket.IO, cursor pagination, unread counts, optimistic reconciliation, Redis presence
  19 ecommerce-storefront — variant catalog, guest carts+login merge, Stripe Checkout, webhooks, inventory transactions (sampled in depth: real Prisma schema + Stripe/zod/helmet deps confirmed)
  20 event-booking — capacity locks, QR tickets, email confirmations, waitlist promotion jobs
  21 invoicing-app — clients/line items, integer money, tax rules, PDFs, payment links, recurring jobs
  22 team-wiki — nested pages, immutable version history, diffs/restore, recursive CTEs, full-text search
  23 survey-form-builder — JSONB schemas, conditional logic, response validation, CSV export
  24 file-sharing-app — presigned S3 upload/download, resumable-upload metadata, quotas, secure share links
  25 discussion-forum — nested comments, votes/karma, hot/top/new ranking, Redis rate limiting
  26 subscription-reminders — timezone-correct reminders, BullMQ scheduling, digests, spending analytics
  27 ats-lite — public job applications, resume-scan hooks, pipeline stages, interview conflict detection
  28 restaurant-reservations — table combinations, interval availability, floor view, no-shows, SMS confirmations
  29 personal-finance-dashboard — messy CSV imports, idempotent ingestion, rules/AI-assisted categorization, net worth
  30 headless-cms — capstone: dynamic content schemas, publish lifecycle, hashed API keys, versioned public API, rate limits, webhooks
  31 multi-tenant-crm — (name implies tenant-scoped CRM; not deep-sampled)
  32 helpdesk-ticketing — (not deep-sampled)
  33 inventory-warehouse-manager — (not deep-sampled)
  34 oauth-saas-identity-portal — OAuth/SaaS identity (sampled: has `server/prisma/` on JS side, `.csproj` on .NET side, both with `docs/upskill.md`)
  35 analytics-reporting-dashboard — (not deep-sampled)
  36 feature-flag-management — (not deep-sampled)
  37 bulk-import-review-tool — (not deep-sampled)
  38 admin-settings-permissions-console — (not deep-sampled)
  39 third-party-integration-sync-hub — (not deep-sampled)
  40 observability-incident-dashboard — (not deep-sampled)
  (root README only documents concepts 16-30 in prose; 31-40 exist on disk with the same `client/server/docs` shape per directory listing but were not individually read this pass — flag as UNKNOWN/NEEDS DEEPER INSPECTION for their specific feature scope)
- Complexity: Mid (16-25) → Mid+ (26-40, esp. 34 OAuth/identity, 39 integration-sync, 40 observability — enterprise-flavored concepts)
- Educational material: USEFUL but shallow-verified — every one of the 50 dirs has a `docs/upskill.md` (confirmed by count), but with **zero automated tests anywhere in the tree**, the "reference implementation" claim in the README (demonstrating "security boundaries," "service-layer code") cannot be cross-checked against passing tests the way newcodexJS or the astra family can.
- Quality observations:
  - README explicitly states "Database writes that change money, inventory, capacity, or ordering are modeled as explicit transactions" and "Authorization is centralized through shared RBAC helpers" as stated design intent — not independently verified against code this pass beyond the ecommerce-storefront Prisma schema sample
  - Genuinely enterprise-flavored concept selection (OAuth/SaaS identity, feature flags, observability/incident dashboards, third-party sync hubs) — broader real-world domain coverage than the more consumer-CRUD-flavored newcodexJS set
  - Complete absence of test files across all 50 directories is the single biggest quality gap found in this batch — contrasts sharply with newcodex1/newcodecjs2/astra* projects, all of which have real unit tests
  - JS side confirmed to use a real ORM (Prisma) with real schema files, not just raw SQL strings, for at least the ecommerce-storefront sample
- Old-AI-generated smells: root README undercounts its own scope ("five... learning projects" heading text vs. 15 bullet points vs. 25 actual pairs on disk) — a documentation/generation-consistency smell suggesting the README was written for an earlier, smaller version of the set and not fully updated as scope grew to 40
- Skill tags: fe-react, be-node-express, be-dotnet, orm, db-postgres, db-transactions, authz-rbac, queues, realtime-ws, idempotency, ci-cd (absent — no CI found), crud-basic
- Duplicate/overlap: concept-level overlap with `newcodexJS` at the low end (kanban/blog/wiki-adjacent ideas recur), but newcodex3 is consistently the more "enterprise" version of similar ideas and adds the JS-vs-.NET comparison angle newcodexJS lacks entirely
- Learning value: Medium — strong domain/concept breadth and a genuinely useful JS-vs-.NET side-by-side comparison angle, capped by the total absence of tests (can't verify claimed correctness, e.g. "zero double-booking," without running/testing the code — out of scope for this read-only pass)
- Transformation opportunity: pick 3-5 of the strongest pairs (ecommerce-storefront, event-booking, oauth-saas-identity-portal look most complete) and add real test suites — would turn "reference implementation, trust the docs" into a genuinely verifiable stack-comparison portfolio piece
- Interview stories: "same spec built in Node+Prisma vs. ASP.NET Core, here's what changed" is a strong comparative-architecture story regardless of test coverage
- Proposed disposition: E EXERCISE SOURCE — valuable as a concept/domain bank and JS-vs-.NET comparison reference; not yet verifiable enough to be a showcase without adding tests

## Batch observations
- **Two clear duplicate/parallel-build clusters found**: (1) astraboot1 vs opusboot1 — the identical "DevPractice" product spec built independently by two different model pipelines (Astra-branded vs Opus-branded), same stack/feature list, worth reconciling into one canonical copy rather than keeping both. (2) The 20-concept curriculum taxonomy appears in at least three independent places: as reviewed docs in `antigravupskill/masterdocs/01-antigrav-curriculum/`, as built code in `newcodexJS/01..20`, and by name in `newcodex3`'s concept selection continuing the numbering from 16 onward — suggesting one master curriculum spec was reused across at least 3 separate build/review passes by different tools (Codex, Antigravity, and whatever generated the master audit).
- **A recurring curriculum-generation harness ("astraupskill/") is the one true constant across the entire batch** — it appears with an identical 7-8 file shell inside astra1, astra2, astra4.2, astra5, and every one of the 20 newcodexJS projects (at least the one sampled), regardless of which model or app concept it's attached to. This strongly indicates a single, reusable "attach a standard learning-course template to any finished app" script exists somewhere in this user's toolchain and has been run repeatedly across unrelated batches.
- **Test coverage varies enormously by generation pipeline, not by app complexity**: astra1/astra2/astra4.2/astra5 (Opus/Fable-built) and newcodecjs2 (Codex-built) all have real, substantive unit tests tied to domain logic. newcodexJS has partial coverage (22 test files across 20 projects). newcodex3 — the most "enterprise-scoped" set by concept selection — has **zero** test files anywhere across 50 directories, despite README claims of "security boundaries" and "service-layer code" as deliverables. This is the single most actionable gap in the batch.
- **Verification/evidence-capture tooling is itself a repeated pattern**: astra1, astra2, astra4.2, astra5, and astraboot1 all separately generate `artifacts/`- or `.data/`-style directories full of `*-verification.json`, `*-report.json`, and multi-viewport screenshots as part of their build process — a consistent automated QA harness reused across the whole astra fleet, independent of what each app actually does.
- **Optimistic-concurrency / revision-checked writes as a deliberately repeated lesson**: independently (not via shared code) implemented in astra2's `VoyageRepository`, astra4.2's settings/library edit flow, and referenced in astra1's tenant-ops design language — suggests whoever authored the astra curriculum treats concurrency control as a core recurring teaching objective across otherwise-unrelated app domains.
- **Gap/surprise**: `antigravupskill` is not itself an app at all but a meta-audit tool nearly identical in purpose to the present portfolio-audit exercise, reviewing 59 projects (most outside this batch's scope) — worth cross-referencing against the master portfolio-audit index once other batches are compiled, since it may already contain independently-generated review notes for projects assigned to other batch numbers.
- Four directories (opusboot2, opusboot4.2, opusdavinci, codexlearnp1) are completely empty and contribute nothing to the portfolio; safe candidates for cleanup.
