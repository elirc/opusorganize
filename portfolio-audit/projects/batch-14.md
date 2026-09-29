# Batch 14 — Anti Projects, App/Product Projects, Grav/VG Projects, New Folders, Other Projects, Home-Dir Projects
Scope: `07 Anti Projects\` (4 dirs), `08 App And Product Projects\` (11 dirs), `09 Grav And VG Projects\` (5 dirs), `10 New Folders\` (12 dirs), `12 Other Projects\` (14 dirs), plus 5 home-directory projects (inventory-system, jeopardy-game-refactor, stellar-conquest, stellar-conquest-architecture, obsidian-claude)  |  Candidate dirs inspected: 51  |  Meaningful projects: ~35 (several dirs are containers holding multiple sub-projects, counted separately below)  |  Tiny/empty/boilerplate: 16 (appmaker, recipegen, recipegen-temp, 12× "New folder*", Obsidian)

> Note on git state: almost none of these directories has real commit history — most report "branch main, no commits yet" or have no `.git` at all. Dates below are therefore mostly filesystem mtimes unless a real git log is cited. Only `eliapplybot` (2 commits) and `jeopardy-game-refactor` (4 commits) had usable git history.

## Candidate table

| Project | Path | Type | Origin | Stack | Complexity | Docs | Disp |
|---|---|---|---|---|---|---|---|
| antiemponb | 07 Anti Projects\antiemponb | Monorepo(2) web+API | COURSE-GEN | Express/TS+Prisma+React/Vite | Mid | docsclaude(49f)+astraupskill(evidence-backed) | B |
| antihelpdesk | 07 Anti Projects\antihelpdesk | Monorepo(2) web+API | COURSE-GEN | Express/TS+Prisma+React/Vite | Mid | docsclaude(47f)+astraupskill | B |
| antiinv | 07 Anti Projects\antiinv | Monorepo(2) web+API | COURSE-GEN | Express/TS+Prisma+React/Vite | Junior | none | E |
| antitestbuild | 07 Anti Projects\antitestbuild | Monorepo(3) web+API+shared | COURSE-GEN | NestJS+Prisma+React/Vite | Mid+/Senior(design) | docs(9f design guide) | A(cand)/B |
| appmaker | 08 App…\appmaker | stray file (not a project) | — | — | Tiny | none | G |
| appmakertrack | 08 App…\appmakertrack | Web app (Next.js) | COURSE-GEN | Next15+Prisma/SQLite+Zustand+RQ | Junior+/Mid | astraupskill(7f)+dfableandopus(6f) | B |
| eliapplybot | 08 App…\eliapplybot | Chrome MV3 extension | ORIGINAL | React/TS/Vite, per-site adapters | Mid | none (ONBOARDING.md, fable/) | B |
| eliapplybot-python | 08 App…\eliapplybot-python | CLI + local web review UI | ORIGINAL | Python/FastAPI/Playwright/Pydantic | Mid | none | C |
| grouphelpdesk | 08 App…\grouphelpdesk | Monorepo(3) helpdesk | COURSE-GEN | React/Express/TS+Prisma+RBAC+CI/Docker | Mid/Mid+ | astraupskill+docs(sprints/learning) | A |
| HNJOBTRACK | 08 App…\HNJOBTRACK | Monorepo(2) job board+AI | ORIGINAL/AI-assisted | FastAPI+Supabase(RLS)+Next.js+OpenAI | Mid+/Senior | astraupskill | A |
| hnrandom | 08 App…\hnrandom | Monorepo(2) observability | ORIGINAL | Node/Express+DuckDB+React, OTLP | Mid+ | docs (unverified depth) | C |
| job track | 08 App…\job track | Container of 5 sub-projects | mixed | React/Express+SQLite; Next.js variant; 3 unrelated course apps | mixed | 5× astraupskill packs | F |
| recipegen | 08 App…\recipegen | empty shell | — | — | Tiny | none | G |
| recipegen-app | 08 App…\recipegen-app | Web app (Next.js, AI) | COURSE-GEN | Next16+Claude API | Junior+/Mid | astraupskill | B |
| recipegen-temp | 08 App…\recipegen-temp | boilerplate scaffold | — | Next16 default template | Tiny | none | G |
| grav1pretalx\pretalx | 09 Grav…\grav1pretalx | Monolith (Django) | OPEN-SOURCE CLONE | Django/DRF/Celery/django-scopes | Senior(app)/Junior→Mid(curric) | docs/upskill(14f)+codex_upskill(9f)+User Stories(12f)+rewrite plan(4f) | D |
| graveopenjspy\OpenSlides | 09 Grav…\graveopenjspy | Microservices(10 svc) | OPEN-SOURCE CLONE | Go/Python/Angular | Senior | docs/upskill(20f) | B |
| gravreviewboardjspy\reviewboard | 09 Grav…\gravreviewboardjspy | Monolith (Django+TS/Vite) | OPEN-SOURCE CLONE | Django+Vite/TS/Storybook | Mid+/Senior | docs/upskill(20f)+User Stories(29f, security-focused)+rewrite plan(3f) | B |
| vg | 09 Grav…\vg (root) | Monolith (Next.js) EOR SaaS | COURSE-GEN | Next.js(JS)+Prisma+BullMQ | Mid/Mid+ | fable review(5f)+docs(13f) | C |
| VGdemo\globalhire-lite | 09 Grav…\VGdemo | Monorepo(3)+.NET port EOR demo | COURSE-GEN | React/TS/Express/Prisma + C#/.NET port | Mid/Mid+ | fable(7f)+docs(30f)+prep(13f) | A(cand) |
| New folder ×12 | 10 New Folders\* | empty | — | — | — | none | G |
| 3buildhyper | 12 Other…\3buildhyper | Web app (Next.js/Plasmic/Amplify) | COURSE-GEN (derivative) | Next14+Plasmic+AWS Amplify | Mid | fabledocs(3f)+docs(4f) | F |
| aaa1 | 12 Other…\aaa1 | Web app/API multi-tenant CRM | ORIGINAL/COURSE-GEN | Next15/React19+Prisma6+worker | Senior | docs/architecture+learning+roadmap (21f) | A |
| andie | 12 Other…\andie | CLI/library Shopify migration | ORIGINAL | Node 22, zero deps | Junior+/Mid | astraupskill(11f)+dfableandopus(4f) | B |
| appmaketrck | 12 Other…\appmaketrck | Container(3 sub-projects) | mixed | airwatch, Jeopardy-Game, obsidian-claude | mixed | uneven | F |
| cc | 12 Other…\cc | Web app CMS | COURSE-GEN | Next14+Tiptap+Prisma+next-auth | Mid | none | E |
| curse | 12 Other…\curse | Jeopardy game + 2 docs | mixed | React/Express + career docs | Junior+/Mid | none (career docs) | F/D |
| FinalJep | 12 Other…\FinalJep | Container(2 scaffolds) | unclear | Convex+React; Next.js scaffold | UNKNOWN | none | G(tent) |
| finaljepgame | 12 Other…\finaljepgame | Jeopardy-maker + explanation docs | COURSE-GEN | Next.js+Prisma | Junior+/Mid | line-by-line-explanations(10+f) | C/F |
| GlobGame | 12 Other…\GlobGame | Web app daily puzzle+studio | COURSE-GEN | Next16/React19+Prisma6/Postgres | Mid/Mid+ | astraupskill(11f)+dfableandopus(7f) | A |
| hypernova-inc-main | 12 Other…\hypernova-inc-main | Web app (Next.js/Plasmic/Amplify) | COURSE-GEN (baseline) | same as 3buildhyper | Mid | fabledocs(3f) | G |
| jdtrrain2.1 | 12 Other…\jdtrrain2.1 | Web app PM/issue tracker | COURSE-GEN | Next16/React19(JS)+Prisma6/SQLite+SSE | Mid+ | astraupskill(36f, largest)+dfableandopus(7f) | A |
| Obsidian | 12 Other…\Obsidian | Obsidian vault (near-empty) | ORIGINAL | — | Tiny | — | G |
| pp8 | 12 Other…\pp8 | Web app/API Python HRIS | COURSE-GEN | FastAPI+Alembic/Postgres+frontend | Mid/Mid+ | docs/architecture+learning(11f) | B |
| pyhealth\healthchecks | 12 Other…\pyhealth | Web app cron monitor | OPEN-SOURCE CLONE | Django | Production-like | upstream docs | D |
| inventory-system | ~\inventory-system | Monorepo(2) inventory tracker | COURSE-GEN | React/Redux+Express+better-sqlite3 | Junior/Junior+ | README-as-curriculum (28.6KB) | E/D |
| jeopardy-game-refactor | ~\jeopardy-game-refactor | Monorepo(2) Jeopardy game | ORIGINAL(LLM-assisted refactor) | React+Context+Express+Prisma/Postgres+JWT | Mid | SETUP_AND_TESTING.md | B |
| stellar-conquest | ~\stellar-conquest | Monorepo(3) real-time mobile game | COURSE-GEN(spec-driven) | Expo/RN+Fastify+Prisma+Redis+WS | Mid+/Senior(design), untested(exec) | none in-repo | C/F |
| stellar-conquest-architecture | ~\stellar-conquest-architecture | Docs-only design doc | ORIGINAL | Markdown, 1,761 lines | Senior(doc) | itself is the doc | D |
| obsidian-claude | ~\obsidian-claude | Monorepo(2) MCP/PKM tool | ORIGINAL(spec-driven) | TS, better-sqlite3, MCP SDK | Mid(broken: missing entrypoint) | spec.md(1094L)+architecture.md(954L) | C |

---

## antiemponb
- Path: `07 Anti Projects\antiemponb`  — Origin: COURSE/GENERATED (LLM), includes an Astra fix-pass
- Type: monorepo(2 apps) — Employee Onboarding case-management SaaS
- State: working-looking — Size: ~159 files / ~6,423 LOC — Last modified: 2026-09-21 (astraupskill/VERIFICATION.md); core app ~2026-05-18/19
- Purpose: HR admins define onboarding workflow/task templates and track employee onboarding cases through approval stages, documents, and notifications.
- Stack: FE React 18.3+Vite+TanStack Query+Zustand+react-hook-form+Zod+Tailwind | BE Node/Express/TS+Prisma+SQLite(dev)/Postgres(.env.example)+Redis/BullMQ+JWT access/refresh+bcryptjs | Test: node:test + Vitest-style `__tests__/` | Infra: docker-compose
- Architecture: modular monolith — domain modules (approvals, auth, departments, documents, employeeProfiles, notifications, onboardingCases, onboardingTasks, reports, users, workflowTemplates); explicit onboarding-case state machine
- Complexity: Mid
- Educational material: STRONG — `docsclaude/` (49 files, 7-track curriculum: language/runtime, frontend, server, architecture, quality, practice, career) + `astraupskill/` (7 numbered lessons + evidence/results.json showing a real passing `node:test` run + snapshot of the original file before the worked change). Evidence-backed, not just prose.
- Quality observations:
  - Zod-validated env config with `safeParse` fail-fast, BUT JWT secrets have insecure `.default('super-secret-access-token-key-change-in-production')` baked into the schema — silent insecure fallback if env var missing.
  - Real state machine for onboarding-case progression with dedicated unit tests.
  - Central error middleware + `requirePermission.middleware.ts` (RBAC-ish).
  - Test coverage thin overall: only 4 test files for 6.4k LOC; concentrated on the module the Astra pass touched.
  - BullMQ job worker present, idempotency/retry not verified.
  - AuditEvent + RefreshToken modeled as first-class entities.
- Old-AI-generated smells: hardcoded fallback JWT secret in schema defaults; test coverage suspiciously concentrated only where Astra touched, implying sparse original test discipline.
- Skill tags: fe-react, fe-forms-validation, fe-state, ts-types, be-node-express, be-validation, be-error-handling, be-async-jobs, authn, authz-rbac, db-postgres, db-sqlite, db-migrations, orm, test-unit, queues, config-secrets, crud-basic
- Duplicate/overlap: shares an identical template lineage with antihelpdesk, antiinv, antitestbuild (same monorepo shape, same weak-JWT-fallback smell across all four) — see batch observations.
- Learning value: High — real state machine + async jobs + RBAC-ish middleware + a verified, evidence-backed Astra worked example.
- Proposed disposition: **B HIGH-VALUE** — solid mid-complexity domain app with genuine curriculum and a proven upskilling exercise; flag/fix the JWT-secret-default smell before showcasing.

## antihelpdesk
- Path: `07 Anti Projects\antihelpdesk` — Origin: COURSE/GENERATED (LLM), Astra fix-pass included
- Type: monorepo(2 apps) — multi-tenant Helpdesk / support ticketing
- State: working-looking — Size: ~146 files / ~4,173 LOC — Last modified: 2026-09-21 (astraupskill); core app ~2026-05-18/26
- Purpose: Organizations create/track support tickets with comments, tags, escalation rules, watchers, attachments, audit logging. README explicitly states "for learning purposes."
- Stack: FE React 19.2+Vite+TanStack Query+Zustand+react-hook-form+Zod4+Tailwind | BE Node/Express/TS+Prisma+Postgres+JWT+bcrypt | Test: 1 node:test file | Infra: docker-compose
- Architecture: modular monolith, domain modules (attachments, audit, auth, comments, dashboard, tags, tickets, users); multi-tenant via `Organization` model
- Complexity: Mid
- Educational material: STRONG — `docsclaude/` (47 files, same 7-track structure) + `astraupskill/` (7-file pack + evidence + snapshot of the permissions module before the worked change, tied to `tests/permissions-errors.test.mjs`).
- Quality observations:
  - `process.env.JWT_SECRET || 'secret'` — weak runtime fallback to a trivially guessable secret, with no env-schema validation layer at all (worse than antiemponb's approach).
  - Rich domain model: EscalationRule, TicketWatcher, TicketLink, CannedResponse, TicketTemplate.
  - AuditEvent + RefreshToken present.
  - Only 1 test file for 4.2k LOC, covering only permissions/errors (again, only where Astra touched).
- Old-AI-generated smells: hardcoded insecure JWT fallback with zero validation; near-zero baseline test discipline outside the Astra-touched module.
- Skill tags: fe-react, fe-forms-validation, fe-state, ts-types, be-node-express, be-validation, be-error-handling, authn, authz-rbac, multitenancy, db-postgres, db-migrations, orm, test-unit, config-secrets, crud-basic
- Duplicate/overlap: same template family as antiemponb/antiinv/antitestbuild.
- Learning value: High — multi-tenant modeling + escalation/audit patterns + verified Astra exercise; also usable as a "spot the insecure JWT fallback" security exercise.
- Proposed disposition: **B HIGH-VALUE** (also viable as C SPECIALIZED security-review exercise given the concrete vuln found).

## antiinv
- Path: `07 Anti Projects\antiinv` — Origin: COURSE/GENERATED (LLM), NOT part of the Astra pass
- Type: monorepo(2 apps) — Inventory Management
- State: PARTIAL/skeleton — Size: ~61 files / ~1,201 LOC (≈1/4–1/7 the size of its siblings) — Last modified: 2026-05-19, no recent touch
- Purpose: Intended warehouse/inventory management (products, vendors, purchase orders, stock transfers/adjustments, low-stock alerts, CSV import) but only basic CRUD is actually wired up.
- Stack: FE React 19.2+Vite+TanStack Query+RHF+Zod4 | BE Node/Express/TS+Prisma+Postgres+JWT+bcrypt | Test: none | Infra: docker-compose only, no README/.env.example
- Architecture: modular monolith, but only 4 of the domains implied by the 17-model Prisma schema are implemented (auth, products, users, vendors, warehouses) — PurchaseOrder, PurchaseReceipt, TransferRequest, StockAdjustment, StockMovement, CsvImportJob, LowStockAlert, InventoryLevel all defined in schema with **no** corresponding controllers/services/routes.
- Complexity: Junior (as implemented); Mid/Mid+ if completed
- Educational material: NONE — no docsclaude/astraupskill/docs of any kind; the one "anti" project without teaching material.
- Quality observations:
  - Controllers appear to be thin pass-throughs with no validation middleware visibly wired at the controller layer despite `*.schemas.ts` files existing (needs deeper check).
  - Two separate insecure-default secrets: `process.env.JWT_SECRET || 'secret'` and `process.env.REFRESH_TOKEN_SECRET || 'refresh_secret'` — worst of the four.
  - Zero tests anywhere.
  - No README, no `.env.example`.
- Old-AI-generated smells: classic "impressive schema, thin implementation" — schema generated in full up front, CRUD wiring stopped partway; double insecure-default secrets; no docs/tests.
- Skill tags: fe-react, fe-forms-validation, ts-types, be-node-express, be-validation, authn, db-postgres, db-modeling, orm, crud-basic
- Duplicate/overlap: same template family as the other three "anti" projects.
- Learning value: Medium — good as a "finish the CRUD against this schema" exercise given the schema/implementation gap; low as-is due to missing tests/docs/worst security defaults.
- Proposed disposition: **E EXERCISE SOURCE** (or G ARCHIVE if incomplete/undocumented entries aren't wanted) — best used as a "complete the missing modules" exercise, not flagship material as-is.

## antitestbuild
- Path: `07 Anti Projects\antitestbuild` — Origin: COURSE/GENERATED (LLM), not part of the Astra pass
- Type: monorepo(3 packages: apps/api, apps/web, packages/shared) — Employer-of-Record ("GlobalWorkforce OS")
- State: working-looking (most architecturally mature of the four "anti" projects), but untested — Size: ~99 files / ~8,093 LOC (largest of the four) — Last modified: 2026-05-22
- Purpose: Multi-tenant EOR SaaS — client companies, international workers, employment contracts, country compliance, onboarding, payroll cycles, benefits enrollment, support cases, under tenant isolation + RBAC.
- Stack: FE React 18.2+Vite+React Router v6+TanStack Query v5+RHF+Zod | BE NestJS+TS+Prisma+Postgres+bcrypt+JWT+class-validator/Zod pipes | Shared `packages/shared` types+Zod schemas across FE/BE | Test: Vitest configured, **0 test files exist** | Infra: docker-compose, Prettier
- Architecture: NestJS modular monolith with real guard/pipe/filter layering (`jwt-auth`, `roles`, `tenant` guards; `zod-validation.pipe`; `http-exception.filter`); domain modules: audit-logs, benefits, companies, contracts, countries, dashboard, documents, onboarding, payroll, support-cases, tenants, workers
- Complexity: Mid+/Senior-oriented in design, undermined by zero tests
- Educational material: USEFUL — `docs/` (9 numbered files: product-overview, architecture, domain-model, auth-security-rbac, api-reference, testing-strategy, local-development, "learning-guide-for-junior-to-mid-level-engineers", extension-roadmap) — cohesive design-doc/ADR-style set, no astraupskill/docsclaude split, no verified exercises.
- Quality observations:
  - Most sophisticated authz seen across all four "anti" projects: `tenant.guard.ts` explicitly handles PLATFORM_ADMIN/INTERNAL_OPS cross-tenant bypass and rejects mismatched tenant IDs from params/query/body/headers — real business logic, not a stub.
  - Still has the weak-secret smell: long-but-hardcoded JWT secret fallback.
  - class-validator + Zod pipe combo — real layered input validation.
  - `docs/testing-strategy.md` documents a strategy that was **never implemented** (0 test files) — clear docs-vs-reality gap.
  - Richest domain model of the four (ComplianceRequirement, PayrollCycle/Item, BenefitEnrollment, SupportCase+Comments, AuditLog).
  - `packages/shared` cross-FE/BE type sharing — a genuinely good pattern absent in the other three.
- Old-AI-generated smells: aspirational documentation (testing strategy) vs. zero actual test coverage; same insecure-fallback JWT pattern as all siblings, just a longer string; nothing here has been verified by any automated run.
- Skill tags: fe-react, fe-forms-validation, fe-state, ts-types, be-nest, be-validation, be-error-handling, authn, authz-rbac, multitenancy, db-postgres, db-modeling, db-migrations, orm, arch-modular-monolith, design-docs-adrs, config-secrets, crud-basic
- Duplicate/overlap: same "anti" template family (identical middleware/auth conventions translated into NestJS idiom); no domain overlap with siblings.
- Learning value: Very High for architecture/RBAC/multitenancy reading; Medium for test-writing practice since nothing exists to extend.
- Transformation opportunity: add a real test suite against the existing guard/pipe/filter layering and the documented testing-strategy.md to turn this into a genuinely verified flagship.
- Interview stories: "designed tenant-isolation guards that reject cross-tenant IDs from any request surface (params/query/body/headers)"; "built a shared-types package to keep FE/BE contracts in sync across a NestJS+React monorepo."
- Proposed disposition: **B HIGH-VALUE (flagship candidate pending tests)** — richest domain and most mature auth/tenant architecture in the batch, but the "flagship" bar should require verified, not just documented, correctness; add tests before treating as showcase-ready.

## appmaker
- Path: `08 App And Product Projects\appmaker` — NOT A PROJECT: an 8-byte stray text file (not a directory) containing the literal text `const gh`. No code, no purpose determinable.
- Proposed disposition: **G ARCHIVE**

## appmakertrack
- Path: `08 App And Product Projects\appmakertrack` — Origin: COURSE/GENERATED (LLM) — has astraupskill/ + dfableandopus/ packs
- Type: web app (Next.js full-stack, single app)
- State: working-looking, no git commits yet — Size: ~111 files — Last modified: lib/tests/package.json Sep 17 2026, astraupskill Sep 18 2026, core app Jan 6 2026
- Purpose: single-user Kanban-style project tracker MVP — projects, tickets, project-scoped team members, drag-and-drop board, time tracking with localStorage timer persistence, dashboard/reports.
- Stack: FE Next.js 15(App Router)+React19+TS+Tailwind, Zustand(timer)+TanStack Query, @dnd-kit | BE Next.js API routes | DB SQLite via Prisma 5 | bcryptjs present (auth scaffolding)
- Architecture: app/ (routes+API), components/, hooks/, lib/(db singleton, api-client, board-service, time-entry-service/validation), prisma/schema
- Complexity: Junior+/Mid
- Educational material: STRONG — `astraupskill/` (7-lesson pack + evidence/snapshots/VERIFICATION.md) + `dfableandopus/` (6-file interview-prep pack: interview questions, stories/resume, code-reading drill, take-home, system-design followups, flashcards).
- Quality observations:
  - Prisma schema has proper relations, `onDelete: Cascade`, and useful indexes (`@@index([ownerId])`, `@@index([archived])`, `@@unique([projectId, position])`).
  - Integration test (`tests/board-service.integration.test.ts`) uses a real temp-SQLite harness via Prisma CLI, gated behind `APPMAKERTRACK_INTEGRATION=1` with a clear doc-comment on the datasourceUrl gotcha — real engineering care.
  - Only 2 test files total — narrow coverage relative to app surface.
  - `lint:changed` script hardcodes a specific file list — smells like an automated-patch-application artifact.
  - No git commits despite substantial code.
- Old-AI-generated smells: none severe; the lint:changed hardcoded file list is a minor automation-artifact smell.
- Skill tags: fe-react, fe-next, fe-state, ts-types, be-node-express, be-validation, db-sqlite, orm, db-modeling, db-indexes-perf, test-integration, test-unit, crud-basic
- Duplicate/overlap: none in this batch — distinct domain from job/recipe/helpdesk trackers.
- Learning value: High — has both a curriculum pack and an interview-prep pack already built around this exact codebase, plus a real integration-test harness worth studying.
- Interview stories: "wired a real temp-SQLite integration test behind an env flag rather than mocking Prisma."
- Proposed disposition: **B HIGH-VALUE** — solid MVP + two education packs; needs a first git commit before shipping.

## eliapplybot
- Path: `08 App And Product Projects\eliapplybot` — Origin: ORIGINAL (matches prior memory: "eli apply mate extension")
- Type: Chrome MV3 browser extension
- State: working-looking/complete, real git history (`ede7ec0` "Fix autofill and profile recovery; add local audio recording", 2026-09-04; prior `00f5ebd` "eli apply mate v0.2.0"; manifest now v0.3.0)
- Size: 53 files under src/, 114 total tracked files
- Purpose: local, cautious Chrome MV3 autofill assistant for personal job applications — never auto-submits; matches/fills fields on ATS sites (Ashby, Greenhouse, Lever, Workday, generic) from a stored profile, plus a local session recorder.
- Stack: FE React18+TS+Vite (MV3 build via esbuild + custom build-extension script) | no backend/DB — chrome.storage | Test: Vitest+fake-indexeddb+jsdom
- Architecture: `src/background` (service worker, profileStore), `src/content` (autofill script, scanner, dom labels), `src/popup`, `src/options`, `src/recorder` (local IndexedDB-backed audio recording), `src/sidebar`, `src/sites/` (per-ATS adapters: ashby/greenhouse/lever/workday/generic), `src/shared`
- Complexity: Mid (real browser-extension constraints, per-site DOM adapters, async messaging)
- Educational material: NONE (no astraupskill/docsclaude/fabledocs); has `fable/`, `docs/`, `ONBOARDING.md` (19.8KB, unexplored).
- Quality observations:
  - Per-site adapter pattern with a dispatcher (`src/sites/index.ts`) — clean extensibility model for ATS-specific quirks.
  - Heavy, targeted test coverage including regression tests (`storage.regressions.test.ts`, `review-regressions.test.ts`) added after real bugs — not just up-front tests.
  - `profileSchema.ts` + `confidence.ts` show deliberate handling of uncertain autofill matches rather than blind fill.
  - Minimal-permission MV3 manifest (`activeTab`, `storage`, `scripting`; `tabCapture` optional-only) with description explicitly stating "Never submits."
  - `verify-extension.mjs` and `generate-icons.mjs` scripts show a real build/release pipeline beyond `vite build`.
- Old-AI-generated smells: none seen — commit messages, regression-test naming, and adapter structure read as genuine iterative development.
- Skill tags: fe-react, ts-types, fe-testing, test-unit, be-async-jobs, security-owasp, legacy-codebase-reading, crud-basic
- Duplicate/overlap: **domain-overlaps with eliapplybot-python** — same product concept (job-application autofill, "never submits" philosophy, identical ATS adapter set), different stack. Not code-duplicative; keep both as a "two-stack" pairing.
- Learning value: Medium-High — good example of adapter pattern + regression-driven testing in a real browser extension.
- Interview stories: "built a per-site adapter dispatcher for autofill so adding a new ATS is a new file, not a new branch"; "added regression tests specifically for bugs found after shipping."
- Proposed disposition: **B HIGH-VALUE** — complete, tested, real product with git history and a good teaching pattern.

## eliapplybot-python
- Path: `08 App And Product Projects\eliapplybot-python` — Origin: ORIGINAL (matches prior memory of a private GitHub repo — **this local copy has no `.git` directory at all**, contradicting the memory note; verify against the actual remote before assuming loss)
- Type: CLI + local web app (FastAPI review UI)
- State: working-looking — Size: 86 files (excl. venv/pycache) — Last modified: tests/README Jul 18 2026, pyproject.toml May 4 2026
- Purpose: local-first, review-first Python tool that scans job-application forms via Playwright, matches fields against a stored profile, and requires human review before any fill — same ATS-adapter set (Ashby/Greenhouse/Lever/Workday/generic) as eliapplybot.
- Stack: BE Python 3.11+, FastAPI+Jinja2+Uvicorn (local review UI), Pydantic v2, Playwright; no DB (file/JSON storage via `storage.py`); Test: pytest
- Architecture: `src/eliapplybot/` — cli.py, main.py, browser.py, matcher.py, filler.py, scanner.py, review.py, workflow.py, storage.py, profile_io.py, config.py, models.py, `adapters/{ashby,base,generic,greenhouse,lever,workday}.py`, `web/` (FastAPI app+templates)
- Complexity: Mid (Playwright automation + adapter pattern + review workflow)
- Educational material: NONE found.
- Quality observations:
  - Same per-ATS adapter structure as the extension sibling (`adapters/base.py` abstract base + concrete adapters) — consistent architecture across both implementations.
  - `ruff` configured with a real rule set (E,F,I,UP,B,SIM); `pytest` configured via pyproject (testpaths, pythonpath) — real tooling, not default.
  - "Review-first" design (dedicated `review.py`) mirrors the extension's "never submits" stance.
  - Only 3 test files vs. 6 adapters + core modules — narrower coverage than the JS sibling.
  - No `.git` present — cannot verify commit history/authorship locally.
- Old-AI-generated smells: none seen in structure.
- Skill tags: be-python, be-rest-design, be-validation, test-unit, security-owasp, legacy-codebase-reading, crud-basic
- Duplicate/overlap: same product idea as eliapplybot (see above); recommend documenting both as parallel implementations, not merging.
- Learning value: Medium — good Python/Playwright automation example paired with the TS version for a "same problem, two stacks" comparison.
- Proposed disposition: **C SPECIALIZED** — distinct stack from the extension, keep separate but note the pairing; verify remote git state before final call.

## grouphelpdesk
- Path: `08 App And Product Projects\grouphelpdesk` — Origin: COURSE/GENERATED (LLM) — explicit fictional 4-person team roster (Alex Chen/Sam Rivera/Jordan Park/Morgan Lee), `authorPersona`/`issue` fields in package.json — classic Fable/Astra-style teaching-simulation project
- Type: monorepo (3 packages: client/server/shared, npm workspaces)
- State: working-looking, substantial — Size: 219 files (excl. node_modules/.git) — Last modified: package.json May 20 2026; astraupskill/tests touched as recently as Sep 21 2026
- Purpose: learning-focused internal IT help-desk / support-ticket system simulating a 4-person team — ticket CRUD + status workflow, assignment, comments (public/internal), dashboards, knowledge-base articles, RBAC, structured logging.
- Stack: FE React18+TS+Tailwind+Vite | BE Node/Express/TS | DB SQLite via Prisma | logging via Pino (structured, request IDs) | validation via Zod | state via TanStack Query | Docker Compose + GitHub Actions CI
- Architecture: `packages/{client,server,shared}` layered monorepo; server has controllers/services/routes/middleware/validation separation (e.g. authController/authService/authSchemas/middleware/auth)
- Complexity: Mid/Mid+
- Educational material: EXCELLENT — `astraupskill/` (same 7-file structure as siblings) + `docs/` tree with `architecture/`, `guides/`, `learning/`, `learning-journal/`, `sprints/`, plus `automation-run-summary.md` and `phase-0-completion-notes.md` — a full simulated sprint-based build process was documented.
- Quality observations:
  - Clear layered backend architecture: routes → controllers → services → validation(Zod)/middleware.
  - `tests/integration/{authz,statusTransitions,tickets,validation}.test.ts` — authz and status-transition workflow explicitly tested.
  - `tests/runtime-permissions.test.mjs` + `tests/runtime-ticket-service.test.mjs` alongside TS unit tests — decent unit/component/integration split.
  - `lint`/`format`/`typecheck` wired across workspaces; Docker + CI present per README — infra maturity beyond a toy app.
  - Persona/issue-number metadata in package.json is intentional pedagogical framing (a simulated PR-review team), not a hidden defect.
- Old-AI-generated smells: none severe — fictional persona/roster is intentional teaching framing.
- Skill tags: fe-react, ts-types, be-node-express, be-rest-design, be-validation, authn, authz-rbac, db-sqlite, orm, db-modeling, test-unit, test-integration, ci-cd, docker, observability-logs, arch-modular-monolith, code-review, crud-basic
- Duplicate/overlap: none in this batch — distinct help-desk domain vs. job/recipe/ticket trackers.
- Learning value: Very High — full-stack layered architecture + RBAC + CI/Docker + structured docs/sprints tree + an Astra upskill pack, essentially production-shaped for a learning app.
- Interview stories: "simulated a 4-engineer team via authored personas to teach PR-review conventions on top of a real layered Express+Prisma app."
- Proposed disposition: **A FLAGSHIP** — most architecturally complete/production-like of this cluster (RBAC, CI, Docker, layered backend, documented sprint process).

## HNJOBTRACK
- Path: `08 App And Product Projects\HNJOBTRACK` — Origin: ORIGINAL/personal-tool-style (no persona/team-simulation markers — reads as a genuine personal tool, possibly AI-assisted but not course-framed)
- Type: monorepo (2 apps: Python FastAPI backend + Next.js frontend) + Supabase migrations
- State: working-looking, well-documented — Size: ~73 files (excl. node_modules) — no git commits — Last modified: README/migrations Feb 18 2026; astraupskill/backend Sep 21 2026
- Purpose: full-stack job browser that scrapes HN "Who's Hiring" threads monthly, uses GPT-4o-mini to parse listings into structured data (company, role, salary, skills, visa sponsorship), then offers search/filter, match scoring, application tracking, and email digest notifications.
- Stack: BE Python 3.11+/FastAPI/Pydantic v2/APScheduler | DB Supabase Postgres w/ Row Level Security + full-text search (tsvector) | Auth Supabase Auth (password + magic link) + JWT verification | AI OpenAI GPT-4o-mini structured JSON extraction | Email via Resend | FE Next.js 14 App Router + React18 + TS + Tailwind
- Architecture: `backend/app/{main,core/{config,supabase,auth},api/{jobs,saved,...}}`; `frontend/src`; `migrations/` + `supabase/schema.sql`
- Complexity: Mid+/Senior-oriented (RLS, structured AI extraction, scheduled scraping, full-text search, JWT auth) — most infra-heavy of the batch
- Educational material: USEFUL — `astraupskill/` present (same 7-file+evidence+VERIFICATION structure as siblings).
- Quality observations:
  - Real production-shaped concerns: RLS on Postgres, JWT verification middleware, full-text search via tsvector, scheduled jobs via APScheduler — not toy CRUD.
  - AI integration is structured-output-based (GPT-4o-mini JSON extraction with a stated confidence score) rather than naive prompt-and-hope — a good ai-llm-integration example.
  - `tests/` directory exists at repo root — depth not verified; NEEDS DEEPER INSPECTION.
  - No commits in git despite mature feature set.
  - Uses external paid API (OpenAI) + external services (Supabase, Resend) — meaningfully more infra-dependent than most peers; good for config-secrets/cloud-integration teaching but harder to run standalone.
- Old-AI-generated smells: none obviously seen; feature list is broad for the file count — worth verifying endpoint implementations aren't stubs (NEEDS DEEPER INSPECTION).
- Skill tags: be-python, be-rest-design, be-validation, authn, db-postgres, db-sql-raw, ai-llm-integration, be-async-jobs, config-secrets, fe-next, fe-react, ts-types, crud-basic
- Duplicate/overlap: domain-adjacent to `job track` (both job-related) but HNJOBTRACK is a **discovery/board** tool vs. `job track`'s **application-CRUD** tracker — different problem, not a duplicate.
- Learning value: Very High — best example of real external AI-API integration + RLS + scheduled jobs in this batch.
- Transformation opportunity: init/commit git, add endpoint-completeness tests, and this is a strong portfolio flagship.
- Interview stories: "used GPT-4o-mini with structured-output extraction and a confidence score rather than trusting raw LLM text"; "modeled Postgres RLS for a multi-user job board."
- Proposed disposition: **A FLAGSHIP** — most infra-realistic/AI-integration-forward project in the batch; needs git init/commit + deeper endpoint verification before shipping.

## hnrandom
- Path: `08 App And Product Projects\hnrandom` — Origin: ORIGINAL — **misleadingly named/located**: the actual product is "AI Observer," an OpenTelemetry-based observability backend, unrelated to "HN"/job-tracking despite name proximity to HNJOBTRACK.
- Type: monorepo (2 apps: Node/Express/DuckDB backend + React/Vite frontend)
- State: working-looking — has live artifact DuckDB files present (`ai-observer.duckdb`, `.wal`, `smoke-*.duckdb.wal`) proving this copy was actually run/smoke-tested — Size: 118 files (backend); no git commits — Last modified: root/CLAUDE.md Feb 19 2026; backend/frontend Jun 9 2026
- Purpose: self-hosted observability backend + dashboard for AI coding workflows — ingests OTLP traces/metrics/logs on :4318, stores in DuckDB, serves API + dashboard + live WebSocket updates on :8080.
- Stack: BE Node.js22+TS+Express+DuckDB(embedded analytical DB)+WebSocket, OTLP protobuf+JSON ingestion | FE React19+TS+Vite | Docker/Makefile/deploy/scripts/CI (.github/), CLAUDE.md at root
- Architecture: `backend/src/{api,db,otlp,services}` — REST routes, DuckDB client+schema, OTLP decode/conversion, query/store services
- Complexity: Mid+ (OTLP protocol handling, WebSocket streaming, DuckDB, Docker/CI deployment)
- Educational material: `docs/` present but content not inspected — NEEDS DEEPER INSPECTION.
- Quality observations:
  - OTLP protobuf+JSON dual decode path is a nontrivial parsing/interop feature.
  - DuckDB as the observability storage engine is an unusual, well-suited (columnar/analytical) choice — architecturally sound and atypical for AI-generated toy apps.
  - Smoke-test WAL files left uncommitted/untracked — mild repo-hygiene issue (should be gitignored) but proves real functional testing occurred.
  - Makefile + docker-compose + deploy/ + CI — real deployment tooling maturity.
  - No git commits despite mature-looking tree.
- Old-AI-generated smells: none seen; leftover DuckDB WAL/smoke-test files are a hygiene issue, not a generation smell.
- Skill tags: be-node-express, be-rest-design, db-sql-raw, realtime-ws, observability-logs, observability-metrics-tracing, docker, ci-cd, deploy, fe-react, ts-types
- Duplicate/overlap: none — unique observability-tooling domain vs. every other project in this batch; misfiled next to job-tracking-cluster folders by name coincidence only.
- Learning value: High — one of the only observability/OTLP-focused examples in this batch; specifically fills the observability-metrics-tracing skill tag.
- Proposed disposition: **C SPECIALIZED** — distinct/valuable niche, but should be reconsidered for placement outside the job-tracking-adjacent folder; needs git init/commit and a `docs/` content check.

## job track (container — NOT a single project)
- Path: `08 App And Product Projects\job track` — **this folder is a bucket holding 5 distinct sub-projects, not one app.**
  1. Root `client/`+`server/` (16 files) — the actual "Job Application Tracker" — React+Vite+React Router+Zustand+RHF+Zod frontend, Node/Express+better-sqlite3+JWT backend (`server/src/{db,middleware/auth,routes/{applications,auth,dashboard},validation,utils}`). Working-looking; ARCHITECTURE_DEEP_DIVE.md present; last touched Sep 8 2026. `astraupskill/` present at this top level too.
  2. `job-tracker-next/` (42 files) — a **second, separate Next.js-based** job-tracker with its own client/server/README/ARCHITECTURE_DEEP_DIVE.md — an alternate/rewritten implementation of the same idea, last touched Jun 9 2026.
  3. `live-chat-support-platform/` — unrelated live-chat support app (own astraupskill/, dfableandopus/, client/, server/, test/, ARCHITECTURE_DEEP_DIVE.md), last touched Sep 18 2026.
  4. `restaurant-kitchen-display-system/` — unrelated restaurant KDS app (own astraupskill/, client/, server/), last touched Sep 18 2026.
  5. `task-queue-system/` — unrelated task/job-queue system (own astraupskill/, client/, server/, docker-compose.yml), last touched Sep 18 2026.
- Origin: mixed — root app + job-tracker-next look ORIGINAL/course-style; the three unrelated apps are clearly COURSE-GENERATED-BY-LLM exercises (each has its own astraupskill pack) that were dumped into this folder rather than scoped as their own top-level directories.
- Educational material: FIVE separate astraupskill packs nested under one folder — a significant filing/organization issue for the reorg, not a content-quality issue.
- Quality observations: the folder itself is a dumping ground; auditing it "as one directory" undercounts its actual content — the root job-tracker vs. job-tracker-next is internal duplication (two implementations of the same "track job applications" idea, different stacks).
- Old-AI-generated smells: the sprawl itself (5 astraupskill packs across unrelated domains) is a filing smell, not a code-quality smell.
- Complexity: root app Junior+/Mid; other sub-apps UNKNOWN / NEEDS DEEPER INSPECTION if promoted to standalone entries.
- Skill tags (root app only): fe-react, fe-forms-validation, fe-state, be-node-express, be-validation, authn, db-sqlite, crud-basic
- Duplicate/overlap: root job-tracker vs. `job-tracker-next/` (internal duplicate); thematically adjacent to HNJOBTRACK at the folder-name level but a different problem shape (application tracker vs. job-discovery board), not a code duplicate.
- Learning value: Medium for the root app alone; High for the folder as a whole once split apart (5 distinct astraupskill-backed exercises).
- Proposed disposition: **F CONSOLIDATE** — split into its constituent projects (root job-tracker, job-tracker-next, live-chat-support-platform, restaurant-kitchen-display-system, task-queue-system) before any individual disposition can be assigned. Flag explicitly: "job track" is not one project, it's an unsorted bucket of 5.

## recipegen
- Path: `08 App And Product Projects\recipegen` — EMPTY SHELL: contains only `.claude/settings.local.json`, no source code. Proposed disposition: **G ARCHIVE**.

## recipegen-app
- Path: `08 App And Product Projects\recipegen-app` — Origin: COURSE/GENERATED (LLM), has astraupskill/
- Type: web app (Next.js full-stack, single app) with real AI integration
- State: working-looking/complete — Size: 59 files (excl. node_modules) — no git — Last modified: package.json/astraupskill/lib/tests Sep 21 2026 (most recent of the recipegen variants); other config Feb 2026
- Purpose: AI-powered recipe generator — user enters ingredients/preferences/time constraints, app calls Claude API to generate recipes, supports serving-size scaling, grocery list, shareable recipe links, favorites, and history.
- Stack: FE Next.js 16.1.6+React 19.2.3+TS+Tailwind4 | BE Next.js API routes calling `@anthropic-ai/sdk` | no DB (`lib/storage.ts`, client-side persistence + share-link encoding in `lib/share.ts`) | Test: Node's built-in test runner (`tests/*.test.mjs`)
- Architecture: `app/{page,results,favorites,history,recipe/[share]}` + `app/api/recipes/route.ts`; `lib/{generation,scaling,share,storage,types,validation}.ts`; component set for the recipe UI
- Complexity: Junior+/Mid
- Educational material: USEFUL — `astraupskill/` (7-file structure + evidence/snapshots/VERIFICATION.md).
- Quality observations:
  - `lib/generation.ts` shows real engineering discipline: validates input before calling the paid provider, retries once on malformed provider output, and explicitly avoids leaking provider error details to the browser ("Provider error details must not be exposed to the browser").
  - Dedicated `lib/validation.ts` separating validation from generation logic.
  - Only one visible test file (`tests/boundaries.test.mjs`), but apparently targeted at edge/boundary cases deliberately.
  - Shareable-link feature implies an encode/decode-without-DB scheme — worth checking whether share data is signed/validated or trivially forgeable (NEEDS DEEPER INSPECTION).
  - No git history in this copy.
- Old-AI-generated smells: none seen — the generation.ts validate/retry/no-leak pattern specifically contradicts the "shallow AI wrapper" smell common in recipe-gen demo apps.
- Skill tags: fe-react, fe-next, fe-forms-validation, ts-types, be-rest-design, be-validation, be-error-handling, ai-llm-integration, test-unit, crud-basic
- Duplicate/overlap: **direct overlap with recipegen and recipegen-temp** — recipegen-app is the fully-built, most complete version; recipegen-temp is a bare create-next-app scaffold; recipegen (bare) is an empty shell. All three are sequential iterations of the same idea; recipegen-app is canonical.
- Learning value: High — one of the better small examples of disciplined AI-API-wrapper error handling in the audited set.
- Interview stories: "wrote a bounded-retry, no-leak wrapper around a paid LLM API rather than surfacing raw provider errors to the client."
- Proposed disposition: **B HIGH-VALUE** — canonical/most-complete recipe generator; archive the other two variants once this is confirmed canonical.

## recipegen-temp
- Path: `08 App And Product Projects\recipegen-temp` — unmodified `create-next-app` scaffold (Next.js 16.1.6/React 19.2.3, same versions as recipegen-app, confirming it's an earlier init step of the same project). 18 files total, default README, no custom lib/components/API routes, no recent activity (Feb 2026). Redundant with recipegen-app. Proposed disposition: **G ARCHIVE**.

## grav1pretalx\pretalx
- Path: `09 Grav And VG Projects\grav1pretalx\pretalx` — Origin: OPEN-SOURCE CLONE (verbatim upstream pretalx source under `src/`, LICENSE/pyproject.toml intact) + curriculum layered on top
- Type: monolith web app (Django) — CFP/conference management platform
- State: complete/working-looking (real upstream codebase) — Size: ~2,297 files — Last modified: file mtimes cluster May 18 2026 (clone date); no local commits
- Purpose: open-source, multi-tenant conference/event management system (CFP submission, blind peer review, drag-and-drop scheduling, speaker email automation) used as a training substrate.
- Stack: BE Python/Django, DRF, Celery, django-scopes (multi-tenant); templated HTML views + a Svelte visual schedule editor; DB Postgres/SQLite via Django ORM
- Architecture: traditional server-rendered Django-apps layout, multi-tenant isolation via django-scopes middleware
- Complexity: Senior-oriented (real large OSS app) for reading; curriculum framed Junior→Mid
- Educational material: STRONG/EXCELLENT — `docs/upskill/` (14 files: fast-track, codebase-cartography, "Python-for-JS-devs" language bridge, architecture-and-patterns, code-reading-gym, quality-engineering, contribution-practice, interview-prep×4, reference/rosetta-stone+verification-log) + `docs/codex_upskill/` (9 more files, a parallel curriculum pass) + `User Stories/` (12 files: 5 flow-based + 4-part junior-onboarding series + mixed_developer_stories.md) + `pretalx_js_rewrite_plan/` (4 files: a hypothetical "rewrite pretalx to Next.js+NestJS/Prisma+BullMQ+React Email" architecture/migration blueprint — proposed only, not executed).
- Quality observations:
  - Real production-grade upstream: django-scopes tenant isolation, Celery async jobs, DRF API layer.
  - Two parallel curricula (docs/upskill vs docs/codex_upskill) exist side by side, redundant/not merged.
  - No evidence of Claude/agent modifications to the app source itself — purely additive docs.
- Old-AI-generated smells: none in the app (real upstream code); the rewrite plan is aspirational-only.
- Skill tags: be-python, be-rest-design, multitenancy, authz-rbac, db-migrations, orm, be-async-jobs, legacy-codebase-reading, arch-modular-monolith, design-docs-adrs, code-review
- Duplicate/overlap: **SAME underlying open-source project as `03 Master Projects\masterpre`** (per user memory), but a distinct curriculum (fabledocs/docsclaude/ADR-pack there vs. docs/upskill+codex_upskill+JS-rewrite-plan here) — recommend consolidating to one canonical vendored copy.
- Learning value: High — real, large multi-tenant OSS codebase with two curricula and a migration-planning exercise that is itself a good architecture-design teaching artifact.
- Proposed disposition: **D REFERENCE** (vendored OSS, not an original build) — `pretalx_js_rewrite_plan/` and `docs/upskill/` are candidates for E EXERCISE SOURCE if repurposed standalone; flag for dedup against masterpre.

## graveopenjspy\OpenSlides
- Path: `09 Grav And VG Projects\graveopenjspy\OpenSlides` — Origin: OPEN-SOURCE CLONE (verbatim upstream OpenSlides — Go/Python/Angular services, go.work, CHANGELOG, Makefile intact)
- Type: microservices monorepo (10 services: auth, autoupdate, backend, client, icc, manage, media, projector, proxy, search, vote) — parliamentary/assembly voting & agenda management
- State: complete/working-looking (real upstream) — Size: ~5,543 files, largest vendored clone in the batch — Last modified: services dirs Jul 30 2026 (clone date)
- Purpose: real-world open-source software for managing motions, elections, and live voting in assemblies/parliaments — used as a training substrate.
- Stack: polyglot — Python/Go backend services, Angular client, Postgres/Datastore, i18n via Transifex
- Architecture: true microservices — separate deployable services per concern (auth, vote, search, media, projector)
- Complexity: Senior-oriented (microservices, polyglot, real distributed system)
- Educational material: STRONG — `docs/upskill/` (20 files, template: 00-fast-track, cartography×2, request-flows×3, language-bridge×2, fullstack-contract, architecture×2, architecture-critique, quality×2, contribution-practice, code-reading-gym, interview-prep, reference, README, `_progress.md` learner tracker). No separate rewrite-plan or User Stories folder found.
- Quality observations:
  - Genuine multi-service architecture (auth-service, vote-service, autoupdate-service, search-service) — rare and valuable for teaching service boundaries/contracts, vs. the many monolith clones elsewhere on disk.
  - Real Go+Python+TS/Angular polyglot stack.
  - `docs/upskill/06-architecture-critique.md` teaches critical evaluation, not just walkthrough.
- Old-AI-generated smells: none (vendored real code); curriculum not independently verified line-by-line — spot-check recommended given the codebase size.
- Skill tags: arch-microservices, be-python, be-rest-design, realtime-ws, db-postgres, docker, legacy-codebase-reading, code-review, design-docs-adrs
- Duplicate/overlap: no known Master Projects equivalent elsewhere on disk; shares curriculum-template DNA (same 00–11 module numbering) with gravreviewboardjspy — likely built by the same pipeline/run.
- Learning value: Very High — one of the only genuine microservices/polyglot systems in the portfolio; strong complement to the monolith-heavy curricula elsewhere.
- Proposed disposition: **B HIGH-VALUE** (app itself is D REFERENCE since vendored; curriculum is a strong E EXERCISE SOURCE) — keep as a flagship "read a real microservices system" reference distinct from monolith clones.

## gravreviewboardjspy\reviewboard
- Path: `09 Grav And VG Projects\gravreviewboardjspy\reviewboard` — Origin: OPEN-SOURCE CLONE (verbatim upstream Review Board — pyproject.toml, COPYING, AUTHORS, conftest.py, vite/rollup/storybook configs intact)
- Type: monolith web app (Django/Python + TS/Vite frontend) — code review tool
- State: complete/working-looking (real upstream) — Size: ~3,597 files — Last modified: May 18 2026 clone
- Purpose: open-source collaborative code review platform (diff review, review requests, SCM integrations, webhooks) — used as a training substrate with an unusually rich, security-focused User Stories set.
- Stack: BE Python/Django, FE TS+Vite+Rollup+Storybook, DB via Django ORM
- Architecture: Django MVC monolith with a modern TS/Vite-built frontend layer bolted on (dual build systems)
- Complexity: Mid+/Senior-oriented (large real app, security-focused stories add depth)
- Educational material: EXCELLENT — `docs/upskill/` (20 files, identical module structure/pipeline to OpenSlides) + `Application Rewrite Plan/` (3 files, same "rewrite to JS/TS" blueprint pattern as pretalx's) + `User Stories/` (29 files: 25 numbered US-01..US-25 covering concrete security/compliance tickets — auth guards, IDOR-style repository scoping, SSRF webhook checks, rate throttling, audit logging, diff-size validation, stale-draft warnings — plus a "25-Mixed-User-Stories.md" and a Junior/ sprint subfolder). This is the richest, most security-focused User Stories set among the three grav*jspy projects.
- Quality observations:
  - Dual-stack (Django + modern Vite/TS/Storybook) exposes a real "legacy backend + modern frontend tooling" seam.
  - 25 targeted User Stories reference concrete OWASP-category bugs (IDOR, SSRF, rate limiting) grounded in a real, mature codebase — high pedagogical value if used as a find-and-fix exercise bank.
  - Same upskill template/pipeline as OpenSlides confirms a repeatable curriculum-generation process.
- Old-AI-generated smells: none in the vendored app; User Stories content not deeply verified for accuracy — spot-check recommended before use as authoritative exercises.
- Skill tags: be-python, security-owasp, authz-rbac, multitenancy, be-rest-design, db-indexes-perf, test-integration, design-docs-adrs, legacy-codebase-reading, code-review
- Duplicate/overlap: no known Master Projects equivalent for Review Board; template overlap with graveopenjspy (same pipeline) but distinct subject matter.
- Learning value: Very High — the User Stories set is a strong standalone security-exercise bank; the rewrite plan is a good system-design exercise.
- Proposed disposition: **B HIGH-VALUE**, with `User Stories/` specifically flagged as **E EXERCISE SOURCE** (strong candidate for extraction into a standalone security-bug-bank collection).

## vg
- Path: `09 Grav And VG Projects\vg` — Origin: COURSE/GENERATED-by-agent-pipeline (`fable/` review folder present), not a clone
- Type: monolith web app — Next.js App Router "Velocity Grid" EOR (Employer of Record) SaaS platform
- State: working-looking but has **confirmed defects** — a prior Fable review already documents specific confirmed bugs — Size: src/ ~101 files, ~6,444 LOC (plain JS, not TS) — Last modified: ~Feb 2026; uncommitted
- Purpose: multi-tenant EOR platform — employee/contractor lifecycle, payroll engine (tax/approval/payslip PDF), leave management, billing/invoicing, contract e-signature.
- Stack: FE Next.js App Router (plain JS)+Tailwind | BE Next.js API routes+service layer | DB Postgres via Prisma (1,097-line schema.prisma) | Redis+BullMQ for background jobs (inline-mode fallback) | Auth JWT in secure cookies | **no test files found**
- Architecture: modular monolith — `src/app/(app)/{admin,billing,contractors,contracts,dashboard,employees,leave,notifications,payroll,reports}`; domain-event outbox pattern claimed in README but, per the existing review, not actually wired to real side effects
- Complexity: Mid/Mid+ (no tests + confirmed security bugs cap it below senior-production-like)
- Educational material: USEFUL, but as a **completed code review, not a tutorial** — `fable/` (5 files: 01-architecture, 02-bugs-and-security, 03-scope-and-quality, 04-roadmap, README) is dense, evidence-based, cites exact file:line locations; `docs/` (architecture, automation-opportunities, improved-implementation-plan, file-explanations/ 9 files).
- Quality observations (per existing fable review, structurally confirmed):
  - **A1 (confirmed bug)**: payroll calculate/approve/process returns 500 on success because Prisma BigInt fields aren't JSON-serializable at the route boundary — commits then fails client-side.
  - **A2 (confirmed security)**: payslip download endpoint builds a filesystem path directly from `params.id` — path traversal + IDOR (checks "can view payroll" generically, not "can view *this* org's payroll").
  - **A3 (confirmed security)**: cross-tenant IDs (employeeId, templateId, policyId, managerId) trusted without re-scoping to the resolved org — broken object-level authorization repeated across contract/leave/employee services.
  - **A4**: UserStatus enum (LOCKED/DISABLED) exists in schema but login flow never checks it — disabled accounts can still authenticate.
  - Over-engineering: roughly half of the 1,100-line Prisma schema has zero code behind it (TimeEntry, BenefitsPackage, Termination, ComplianceDocument, Invitation, ExchangeRate, IdempotencyKey, Integration/WebhookSubscription…).
  - Unused deps (stripe, nodemailer, clsx) with zero import sites.
  - Two background-job systems (BullMQ + outbox) exist but neither produces real side effects.
  - No pagination anywhere (unbounded findMany except one 100-row cap).
  - Permission list hand-duplicated across two files (`src/lib/permissions.js` and `prisma/seed.js`) — drift risk.
  - Plain JavaScript (not TS) despite a complex domain — no static-typing safety net.
- Old-AI-generated smells: schema drastically outpacing implementation, hand-rolled CSV parser reinventing a solved problem, dead code, magic strings for roles/statuses/event types, copy-pasted boilerplate (audit-write block repeated ~20x; submitJson helper copy-pasted into 6 panels) — all textbook LLM-generated-monolith smells, already caught by the existing review.
- Skill tags: fe-next, be-node-express, be-rest-design, be-validation, authz-rbac, multitenancy, db-postgres, orm, db-migrations, queues, outbox, be-async-jobs, security-owasp, crud-basic
- Duplicate/overlap: same business domain (EOR) as VGdemo below but a larger, more ambitious, less tested build; also thematically adjacent to the user's memory-indexed "Atlas Course 8 (.NET EOR)" — three EOR-domain builds now exist across the portfolio in three stacks.
- Learning value: High specifically as a "spot and fix real bugs" exercise, since a full evidence-based bug list already exists.
- Proposed disposition: **C SPECIALIZED** — recommend either using fable/02–03 directly as a guided fix-pass punch list, or **G ARCHIVE** if not pursuing further given no tests and unfixed security issues. Not flagship-ready as-is.

## VGdemo\globalhire-lite
- Path: `09 Grav And VG Projects\VGdemo` (app at `globalhire-lite/`, plus `VGdemo/docs`, `VGdemo/fable`) — Origin: ORIGINAL/COURSE-GENERATED demo, explicitly built "for a mid-level SWE interview walkthrough" per its own README, PLUS a deliberate cross-stack migration exercise (`migrated-dotnet/`, a full C#/.NET port of the same app)
- Type: monorepo (npm workspaces, `apps/api`+`apps/web`+`packages/shared`) — "GlobalHire Lite," a smaller-scoped EOR demo
- State: working-looking; the TS app has real tests (Vitest+RTL, 6 files) — more mature than `vg` — Size: TS app ~3,885 LOC, `migrated-dotnet` C# ~1,465 LOC, ~179 total files (excl. node_modules) — Last modified: migrated-dotnet newest (~Jul 2026); `VGdemo/fable` also Jul 2 2026
- Purpose: simplified Employer-of-Record demo — hire request → onboarding → employment records → leave → timesheets → payroll preview → invoicing → offboarding — scoped small and clean for interview-prep/demo purposes, then used as the base for a TS→.NET migration exercise.
- Stack (TS app): FE React+TS+Vite+React Router+TanStack Query+RHF+Zod+Tailwind | BE Node/Express/TS+Prisma+Postgres+Zod | Auth JWT in httpOnly cookies | Test: Vitest+RTL (6 files)
- Stack (.NET port): C#/.NET (GlobalHireLite.Api + GlobalHireLite.Web under `migrated-dotnet/src`), own `tests/` dir (GlobalHireLite.Api.Tests)
- Architecture: modular monolith split FE/BE via npm workspaces for the TS version; `migrated-dotnet` a structurally similar port (Contracts/Domain/Infrastructure/Services layering)
- Complexity: Mid (TS original, well-scoped) to Mid+ (as a cross-stack migration-comparison exercise)
- Educational material: EXCELLENT — `fable/` (7 files: codebase-overview, what-is-done-well, what-needs-improvement, overengineering-and-complexity, junior-to-senior-playbook, exercises, user-stories, README — a completed code review that explicitly compares the TS original against the .NET port) + `VGdemo/docs/` (architectural-cartographer 7f, learning 14f, mission-learning-path 6f, user-story-build-path 3f) + `globalhire-lite/prep/` (13 files incl. "common-interview-story-prompts") + `globalhire-lite/docs/` (incl. "migrated-dotnet-feature-user-stories.md").
- Quality observations:
  - TS original called out (per fable/02) as having the best code in the repo: payroll DRAFT→CALCULATED→APPROVED→LOCKED workflow guards, worker activation gated on onboarding-task+contract-signed state.
  - **Confirmed critical security regression in the .NET port** (fable/03, section A1): auth token is literally the user's raw ID (`globalhire_user_id` cookie / `Bearer <id>` header both trusted directly), two seed IDs are guessable literal strings ("user-admin", "user-client"), cookie not marked Secure, token duplicated into the JSON body (XSS exposure) — versus the TS original's proper `jwt.sign()`. A textbook "the rewrite forgot why the original was safe" case.
  - TS app has real tests (Vitest+RTL, 6 files) — ahead of `vg` which has none.
  - Explicit "junior-to-senior-playbook" and "exercises" docs make this directly reusable as teaching material without further editing.
- Old-AI-generated smells: the .NET port shows a classic "rewrote the shape, dropped the security invariant" pattern (id-as-token) — worth flagging as a canonical teaching example of what NOT to do in a stack migration; the TS original is well-scoped with no evidence of the schema-outpaces-code bloat seen in `vg`.
- Skill tags: fe-react, fe-forms-validation, ts-types, be-node-express, be-validation, authn (plus a documented authn regression to study), be-dotnet, db-postgres, orm, test-unit, test-integration, legacy-codebase-reading, backcompat-versioning, code-review, design-docs-adrs
- Duplicate/overlap: same business domain (EOR) as `vg` but independent, smaller, better-tested; also overlaps thematically with memory's Atlas Course 8 (.NET EOR clone) — three EOR-domain projects now on disk across three stacks. Internally, `migrated-dotnet/` is a deliberate near-duplicate of `apps/api` by design (migration exercise), not accidental overlap.
- Learning value: Very High — the TS-vs-.NET security-regression comparison is an unusually concrete, ready-to-use teaching artifact about what breaks when migrating stacks; small enough to be approachable, layered enough to be a complete self-contained course.
- Transformation opportunity: package the fable/03 A1 finding as a standalone "spot the regression" security exercise independent of the rest of the app.
- Interview stories: "reviewed a stack migration (Express→.NET) and found the port had silently turned the user ID into the session token"; "documented a before/after security comparison across a real rewrite."
- Proposed disposition: **A FLAGSHIP (candidate)** — well-scoped, tested, has a genuinely instructive before/after security story, and rich curriculum layering already in place; recommend promoting this over `vg` as the primary EOR-domain teaching asset, optionally folding `vg`'s bug list in as a "harder, larger, more over-scoped" companion exercise.

## New folder (×12)
- Path: `10 New Folders\New folder`, `New folder (2)`, `(3)`, `(4)`, `(5)`, `(6)`, `(7)`, `(8)`, `(10)`, `(11)`, `(12)`, `(13)` — **all 12 are completely empty** (only `.`/`.` in each, total size 0). No source code, README, package.json, `.git`, or educational material in any of them. mtimes range 2026-01-07 through 2026-05-05. Note: numbering skips "New folder (9)" (does not exist), consistent with the "~12" estimate given in the task.
- Likely origin: leftover artifacts from file-extraction, drag-and-drop, or archive-unzip operations where the payload was never placed inside or was moved out afterward.
- Proposed disposition (all 12): **G ARCHIVE** (safe to delete as a single housekeeping action; contribute nothing to the portfolio).

## 3buildhyper
- Path: `12 Other Projects\3buildhyper` — Origin: COURSE/GENERATED derivative of `hypernova-inc-main` — same "HyperNova Inc" Plasmic-codegen app, with `fabledocs/` (3 files) + CONTRIBUTING.md + `__tests__/` layered on top by a Fable-style course pass
- Type: web app (Next.js 14 marketing/estimator site) with AWS Amplify backend
- State: working-looking (has tests, CI, lint configs, CONTRIBUTING doc describing PR-per-story workflow) — Last modified: Jul 25 2026 (README/lib/pages)
- Purpose: marketing/estimator site for "HyperNova Inc" — a fabledocs user-story backlog (HN-01..HN-20) layered onto a real Plasmic/Amplify-generated site.
- Stack: FE Next.js 14 (Plasmic codegen, antd5, three.js, react-slick) | BE AWS Amplify (DynamoDB, SES v2) | Auth Amplify | Test Jest (`__tests__/`, `__mocks__`, coverage.sh) | Infra AWS Amplify, `.github/` CI, husky hooks
- Complexity: Mid (real AWS integration + generated UI layer, but most complexity is tool-generated)
- Educational material: USEFUL — `fabledocs/` (3 files: app-architecture-guide, feature-backlog-user-stories, +1) + generic `docs/` (4 files).
- Quality observations:
  - CONTRIBUTING.md (7.8KB) describes a branch/PR/review workflow — deliberate "git teaching" structure similar to other Fable courses in memory.
  - `lint:ci` pins `--max-warnings=74` — pre-existing lint debt tolerated rather than fixed.
  - Real Jest test investment vs. many stub repos in the batch.
  - Heavy Plasmic vendor-lock (`plasmic.json` 123KB) — architecture largely generated, not hand-designed.
- Old-AI-generated smells: none strongly seen beyond generated Plasmic boilerplate (expected for this tool).
- Skill tags: fe-react, fe-next, be-node-express (Amplify functions), cloud-aws, test-unit, ci-cd, config-secrets
- Duplicate/overlap: **same base app as hypernova-inc-main** (identical package.json name "hypernova-inc", identical README intro, same dependency set/versions). 3buildhyper = hypernova-inc-main + fabledocs + CONTRIBUTING + tests layered on top; hypernova-inc-main is the earlier/plainer copy.
- Learning value: Medium — good AWS Amplify/Plasmic exposure and PR-workflow teaching, low for hand-written architecture since UI is codegen.
- Proposed disposition: **F CONSOLIDATE** — merge/compare against hypernova-inc-main, keep only this enhanced copy as the "final" version, archive the original as reference only.

## aaa1
- Path: `12 Other Projects\aaa1` — Origin: ORIGINAL/COURSE-GENERATED build (package name "multi-tenant-crm"; extensive `docs/learning/`+`docs/roadmap/` phased-build journal, resembles a Fable/Claude "build journal" teaching project)
- Type: web app/API — multi-tenant B2B CRM (Next.js App Router + API routes + background worker)
- State: working-looking, well-documented — Size: ~247 files (excl. node_modules/.next) — Last modified: Apr 2026
- Purpose: multi-tenant CRM (leads/deals/contacts) with RBAC, custom fields, import/export, audit trail, domain events, feature flags — deliberately built for "senior-realism" per its own `docs/learning/phase-5-platform-compliance-and-production-realism.md`.
- Stack: FE Next.js 15/React 19 | BE Next.js API routes + tsx worker (`src/worker.ts`) | DB Prisma 6 (Postgres implied, provider not directly confirmed) | Validation Zod | Data fetching TanStack Query | Test Vitest (33 test files) | Auth custom (`src/lib/auth/session.ts`, permissions.ts, fieldAccess.ts) | Multitenancy `src/lib/tenant/scope.ts`
- Architecture: layered — `src/lib/{auth,tenant,validation,http,middleware,observability,jobs,import,export,audit,filtering,serializers}/` + `src/repositories/` (11+ repository files: activity, apiToken, approval, auditLog, contact, customField, deal, dealLineItem, domainEvent, duplicate, exportRepository, featureFlag…) — repository pattern with domain events and audit logging
- Complexity: Senior-oriented (multitenancy + RBAC + field-level authz + domain events + async jobs + audit logging)
- Educational material: EXCELLENT — `docs/architecture/` (5 files: auth-and-permissions, domain-model, master-system-overview, README, request-lifecycle) + `docs/learning/` (9 files: build-journal, complexity-slice-implementation-process, concepts-demonstrated, flow-traces, guided-reading-path, load-bearing-files, phase-2..5 maturity docs, testing-rationale) + `docs/roadmap/` (5 phase files) — 21 doc files, one of the most thorough documentation sets in the whole batch, phased/staged learning narrative.
- Quality observations:
  - Domain-event + repository pattern (`domainEventRepository.ts`) suggests outbox/event-sourcing-adjacent design.
  - Explicit RBAC layer: `permissions.ts` + `fieldAccess.ts` (field-level access control) — beyond typical CRUD.
  - Tenant scoping isolated to its own module (`tenant/scope.ts`) — good multitenancy hygiene signal, though isolation enforcement not verified at every call site.
  - Background worker separated from the web process (`src/worker.ts`, `worker`/`worker:once` scripts).
  - 33 Vitest test files present — meaningfully tested vs. many zero-test repos in this batch.
  - `docs/learning/testing-rationale.md` explicitly reasons about what's tested and why.
- Old-AI-generated smells: none observed at this pass (deeper reading of route/repository internals recommended to fully confirm no God-files or hallucinated APIs).
- Skill tags: fe-react, fe-next, ts-types, be-node-express, be-rest-design, be-validation, authn, authz-rbac, multitenancy, db-postgres, orm, db-transactions, test-unit, arch-modular-monolith, outbox, be-async-jobs, observability-logs, design-docs-adrs
- Duplicate/overlap: none obvious in this batch; conceptually similar to "cc" (multi-tenant SaaS domain) but a different product (CRM vs CMS), no code overlap.
- Learning value: Very High — richest architecture-docs set in the batch, explicit phased teaching journal, RBAC/multitenancy/outbox patterns rarely this well-documented elsewhere in the portfolio.
- Interview stories: "designed field-level RBAC (not just route-level) for a multi-tenant CRM"; "kept a background worker as a separate process from the web tier for async job isolation."
- Proposed disposition: **A FLAGSHIP** — strong candidate for the portfolio's headline "senior-realism" teaching project; recommend a deeper follow-up read of actual route/repository code before finalizing.

## andie
- Path: `12 Other Projects\andie` — Origin: ORIGINAL rebuild/teaching lab — explicitly "Andie metaobject migration learning lab," replacing a legacy vulnerable script
- Type: CLI/library — Node.js metaobject-migration utility (Shopify integration)
- State: complete/working-looking, dependency-free, offline-testable — Size: 52 files — Last modified: Sep 18 2026 (most recent in this batch)
- Purpose: teaches safe external-CRUD integration — deterministic migration planning, pagination, conflict detection, partial-failure recovery, replacing a legacy script that had hardcoded Shopify credentials and unsafe write behavior.
- Stack: pure Node 22, zero third-party runtime deps | Test: node:test (42+3 cases per its own docs) | Shopify GraphQL Admin API client | CLI
- Architecture: 3-boundary design — pure planner (`scripts/lib/planner.js`), transport client (`scripts/lib/client.js`), CLI entrypoint (`scripts/populate-metaobjects.js`) that "refuses to act without an explicit command"
- Complexity: Junior+/Mid (small surface area but the concepts — cursor pagination, compare-and-set planning, partial-failure recovery — are mid-level)
- Educational material: EXCELLENT — `astraupskill/` (README + 01-CODEBASE-MAP…07-TRACE-LAB + VERIFICATION.md, ~11 files) + `dfableandopus/` (README + 01-INTERVIEW-QUESTIONS, 02-STORIES-AND-RESUME, 05-SYSTEM-DESIGN-FOLLOWUPS, 06-FLASHCARDS). Quality is high: precise file:line citations (e.g. "scripts/lib/planner.js:249-250"), explicit prerequisite/glossary tables.
- Quality observations:
  - Plan-then-apply pattern with sourceHash/targetHash compare-and-set before mutation — optimistic-concurrency-style safety.
  - Never retries a mutation with an unknown outcome (`client.js:56`) — deliberate idempotency/exactly-once-ish discipline, documented explicitly.
  - Secret-redaction regex present in `client.js` (`/shpat_[A-Za-z0-9]+/g` → `shpat_[redacted]`) — no literal leaked token found in this copy; matches the already-tracked memory item "revoke Shopify token" as an external action item, not a live leak in this repo.
  - Zero third-party runtime dependencies — reduces supply-chain surface, a deliberate teaching choice.
  - Real vendored Shopify theme assets (fonts, `.shopify` config) alongside the lab — legitimate theme scaffold, not junk.
- Old-AI-generated smells: none — reads as a carefully-reviewed, Fable-audited artifact (consistent with the fablereview-astra-audit memory entry).
- Skill tags: be-node-express, be-validation, be-error-handling, idempotency, test-unit, config-secrets, security-owasp, legacy-codebase-reading, incident-debugging
- Duplicate/overlap: none with others in this batch.
- Learning value: High — compact, focused, well-documented lesson in safe external API integration and credential hygiene.
- Proposed disposition: **B HIGH-VALUE** — small footprint but excellent teaching artifact; the historical Shopify token revocation action item remains open (already tracked in memory).

## appmaketrck (container — NOT a single project)
- Path: `12 Other Projects\appmaketrck` — holds THREE unrelated sub-projects plus junk:
  - `airwatch/` — 3D-globe air-quality monitor web app (`agents/`, `api/`, `server/`, `src/` — 40 files); README describes AQICN API integration and an "agents" dir suggesting a possible agentic component; state working-looking per README (v1.0.0). Stack details NEEDS DEEPER INSPECTION.
  - `Jeopardy-Game/` — full-stack Jeopardy web game (React FE + Node/Express BE, 111 files), simpler feature set than `curse`'s copy (no accounts/friends/sharing). **Overlaps with curse/Jeopardy-Game and the home-dir `jeopardy-game-refactor`** — same base game, this is the simpler/earlier variant.
  - `obsidian-claude/` — Obsidian+Claude Code knowledge-management integration (`docs/`, `packages/`, `scripts/`, `vault-template/` — 88 files), explicitly a "Personal knowledge management system integrating Obsidian with Claude Code" via MCP capture workflow. **Very likely the source/origin of the home-dir `obsidian-claude/` and `obsidian-vault/` entries** audited separately in this same batch — recommend a direct diff to determine which copy is canonical/newer.
  - `New folder (9)/` — empty junk leftover; `.claude/` — settings only.
- Quality observations / smells: this directory is a miscellaneous parking lot rather than a coherent project (has a stray "nul" file too) — split into its 3 real sub-projects for cataloging.
- Duplicate/overlap: `Jeopardy-Game` here is an earlier/simpler sibling of `curse/Jeopardy-Game`; `obsidian-claude` here is likely the origin of the home-dir Obsidian-Claude entries.
- Complexity: mixed (airwatch Junior+/Mid; Jeopardy-Game Junior+; obsidian-claude Mid).
- Skill tags: fe-react, be-node-express, ai-llm-integration, agentic-engineering, crud-basic
- Learning value: Medium, uneven across the three sub-projects.
- Proposed disposition: **F CONSOLIDATE** — split the three sub-projects out for individual disposition; dissolve the container folder. Jeopardy-Game sub-copy → likely **G ARCHIVE** (superseded by curse's fuller version); airwatch → **C SPECIALIZED** pending deeper inspection; obsidian-claude → needs a diff against the home-dir copies before deciding B/F.

## cc
- Path: `12 Other Projects\cc` — Origin: COURSE/GENERATED (LLM), unlabeled (no fabledocs/astraupskill, but structure/naming matches the batch's pattern)
- Type: web app — CMS/blogging platform ("cms-platform")
- State: partial/working-looking — Size: 135 files — Last modified: Feb 24 2026
- Purpose: multi-site-capable CMS/blog platform with newsletters, comments, SEO, analytics, tagging/categories.
- Stack: FE Next.js 14 + Tiptap rich-text editor (7 extensions: image, link, placeholder, code-block-lowlight, table+row+cell) | BE Next.js API routes | DB Prisma 5 (provider unconfirmed) | Auth next-auth v4
- Architecture: `src/app/(public)` + `/admin` + `/login` route groups; `src/lib/` has ~13 utility modules (analytics-utils, api-key-utils, api-utils, auth-utils, auth.ts, calendar-utils, category-utils, comment-utils, editor-utils, newsletter-utils, post-utils, seo-utils, site-context.ts, slug.ts, tracking.ts) + `middleware.ts`
- Complexity: Mid (rich-text editing, newsletters, analytics, multi-site hints) but under-tested
- Educational material: NONE found (no docs/, fabledocs/, astraupskill/).
- Quality observations:
  - Zero test coverage (0 test files across 135 files) — significant gap vs. aaa1/GlobGame/jdtrrain2.1 in the same batch.
  - `auth.ts` is only 74 lines — thin for a next-auth config; NEEDS DEEPER INSPECTION to confirm session/callback correctness.
  - 13 grab-bag "*-utils.ts" files rather than domain-organized layers — a mild code-smell, less disciplined than aaa1's repository-pattern approach.
  - `site-context.ts` suggests multi-tenant/multi-site awareness but isolation strategy is unverified.
- Old-AI-generated smells: utility-file sprawl, zero tests — matches "shallow/boilerplate" more than aaa1/GlobGame.
- Skill tags: fe-react, fe-next, be-node-express, authn, orm, db-postgres (assumed), crud-basic, multitenancy (partial/unverified)
- Duplicate/overlap: none obvious in this batch.
- Learning value: Medium — decent feature breadth, but missing tests/docs and utils-sprawl reduce its value as a "read this to learn good architecture" artifact; more useful as an exercise source.
- Proposed disposition: **E EXERCISE SOURCE** — good candidate for an "add test coverage + refactor grab-bag utils into layered modules" exercise; not flagship due to zero tests and no docs.

## curse (mixed — 1 app + 2 loose docs)
- Path: `12 Other Projects\curse` — contains:
  - `Jeopardy-Game/` — full-stack Jeopardy web game (React FE + Node/Express BE, 117 files). README: user accounts, friends system, game sharing, email/password + Google OAuth, public games, grid-based editor, real-time same-screen multiplayer. **This is the fullest-featured of the Jeopardy-game copies found across the whole archive** (vs. appmaketrck's simpler copy and finaljepgame's separate Next.js "jeopardy-maker").
  - `ai_assisted_swe_bootcamp.md` — standalone 12KB doc, "AI-Assisted SWE Survival Bootcamp," a personal/career-skills crash-course (not app code) — honest breakdown of what AI can/can't do, git basics, etc.
  - `resume_bullets.md` — 19.6KB standalone resume-bullets document, presumably drawn from this project portfolio.
- Last modified: docs Jan 2 2026; Jeopardy-Game Jul 18 2026.
- Educational material: the two root `.md` files are themselves career/interview-prep artifacts, not code docs.
- Quality observations: Jeopardy-Game here has OAuth, sharing/permissions (view-only vs collaborative), and social features — more sophisticated than sibling copies; auth/authz code not deeply read in this pass (NEEDS DEEPER INSPECTION).
- Duplicate/overlap: **Jeopardy-Game duplicated 3–4× across the archive** (curse — fullest-featured, likely canonical; appmaketrck — simpler/earlier; finaljepgame's `jeopardy-maker` — separate Next.js/Prisma rewrite; plus `jeopardy-game-refactor` in the home directory, audited separately). Recommend one consolidated cross-reference note before any disposition.
- Complexity: Junior+/Mid (given OAuth + sharing/permissions + real-time features).
- Skill tags: fe-react, be-node-express, authn (OAuth), authz-rbac (view-only vs collaborative sharing), realtime-ws (same-screen multiplayer — verify actual WS use vs. local state), crud-basic
- Learning value: Medium — useful CRUD+auth+sharing exercise; the two loose `.md` docs have separate personal/career value outside the codebase.
- Proposed disposition: **F CONSOLIDATE** (Jeopardy-Game — treat as the most-evolved candidate among the duplicates) / **D REFERENCE** (the two standalone `.md` docs — personal career material).

## FinalJep (container — 2 scaffolds)
- Path: `12 Other Projects\FinalJep` — contains:
  - `finaljep-app/` — Convex + React(Vite) + Tailwind + shadcn/ui scaffold; unedited boilerplate README from `npm create convex`, has `convex/` backend dir, `.cursor/` config.
  - `finaljep-temp/` — separate Next.js scaffold, unmodified `create-next-app` boilerplate README.
  - `.claude/settings.local.json`; a stray "nul" junk file.
- State: skeleton/docs-only for both sub-apps — both READMEs are unedited framework boilerplate, suggesting abandoned early scaffolds, OR real app code lives in `convex/`/`src/` and the READMEs were simply never updated (NEEDS DEEPER INSPECTION of `finaljep-app/convex/` before final call).
- Size: 68 files total — Last modified: Feb 7 2026.
- Purpose: appears to be an attempt at a Jeopardy game rebuild using Convex as backend (given the "FinalJep" name and sibling `finaljepgame` directory), but neither README reflects Jeopardy-specific content — unclear if this pivoted away or documentation was simply neglected.
- Educational material: none found.
- Quality observations: boilerplate READMEs on both sub-apps is itself a smell — recommend a quick peek at `finaljep-app/convex/` schema/functions before final disposition.
- Duplicate/overlap: likely part of the broader Jeopardy-game family (name + proximity to finaljepgame/curse/appmaketrck's Jeopardy-Game) but stack (Convex) differs from every other copy (Express/Prisma) — possibly an abandoned "final" rewrite attempt on a different backend.
- Complexity: UNKNOWN / NEEDS DEEPER INSPECTION.
- Learning value: Low-Medium, pending inspection.
- Proposed disposition: **G ARCHIVE (tentative)** — unedited boilerplate READMEs and "temp" naming both suggest abandoned scaffolds; revisit only if `convex/` turns out to contain real Jeopardy logic.

## finaljepgame
- Path: `12 Other Projects\finaljepgame` — contains a real Next.js/Prisma Jeopardy-maker app plus a distinctive "line-by-line-explanations" teaching artifact:
  - `jeopardy-maker/` — Next.js + Prisma app (`prisma/`, `public/`, `src/`), generic unedited create-next-app README (same smell as FinalJep).
  - `line-by-line-explanations/jeopardy-maker/` — one `.explanation.md` file per project config/source file (dev.db, eslint.config.mjs, next.config.ts, package-lock.json, package.json, postcss.config.mjs, prisma.config.ts, README.md, tsconfig.json, even a stray "nul" file — 10+ files). A distinctive per-file plain-English teaching format not seen elsewhere in the archive.
  - `.claude/` — settings only.
- State: `jeopardy-maker` looks like a working-looking scaffold (has `prisma/`, `dev.db` referenced) but README is boilerplate; the explanations set is clearly finished/complete as a teaching artifact.
- Size: 152 files total — Last modified: Feb 13 2026.
- Purpose: Jeopardy-game-maker app (Next.js/Prisma) + a parallel beginner-oriented "explain every file" course.
- Educational material: STRONG (as a format) — `line-by-line-explanations/` is a genuinely distinctive teaching pattern worth flagging independent of the Jeopardy game itself; coverage down to `package-lock.json` and even the stray "nul" file suggests the generation process was automated/exhaustive rather than curated.
- Quality observations: `dev.db` (SQLite) committed at repo root — normal for local dev, exclude from any portfolio publish.
- Duplicate/overlap: third Jeopardy-related project in this batch (with curse and appmaketrck) but a DIFFERENT implementation (Next.js+Prisma "jeopardy-maker" vs. the Express+React "Jeopardy-Game").
- Complexity: Junior+/Mid for the app; Tiny/Tutorial for the explanations pack.
- Skill tags: fe-react, fe-next, orm, db-sqlite, crud-basic, legacy-codebase-reading
- Learning value: Medium for the app; High for the line-by-line-explanations format as a reusable teaching pattern.
- Proposed disposition: **C SPECIALIZED** — the `line-by-line-explanations/` artifact is worth preserving/reusing as a teaching-format template even if the Jeopardy app itself is superseded; app itself → **F CONSOLIDATE** within the Jeopardy-game family.

## GlobGame
- Path: `12 Other Projects\GlobGame` — Origin: COURSE/GENERATED (LLM), Fable-style (distinctive careful/precise README prose matching other Fable-audited projects — andie, aaa1)
- Type: web app — daily word/puzzle game with an authoring studio (Connections/Wordle-style: four categories of four words + one theme)
- State: complete/working-looking — Last modified: Sep 18 2026 (astraupskill/dfableandopus, same day as andie — likely part of the same review pass referenced in memory's fablereview-astra-audit entry)
- Purpose: daily puzzle game (public play) + an authoring studio for creating/publishing/archiving puzzle editions with token-based auth, optimistic-concurrency version conflicts, and a demo/sample mode independent of the DB.
- Stack: FE Next.js 16/React 19 | BE Next.js API routes | DB Prisma 6 + Postgres (self-provisioned local cluster for tests) | Test node:test (unit) + Playwright (`browser-tests/`) | Infra custom `scripts/test-database.mjs` harness that spins up/tears down its own loopback Postgres cluster
- Architecture: `src/app/{api,studio}`, `src/lib/{game,puzzles}`, `src/components/globs`
- Complexity: Mid/Mid+ (optimistic concurrency, transactions, outbox/notification concepts, Web Locks, self-hosted test-DB lifecycle)
- Educational material: EXCELLENT — `astraupskill/` (11 files, explicit coverage of "account ownership, idempotency, SQL transactions, and notification outboxes") + `dfableandopus/` (7 files, interview-prep pack, same format as andie's) + `docs/globs-plan-v2.md` (explicitly marked "historical planning material" superseded by the README/course).
- Quality observations:
  - Explicit optimistic-concurrency design: version conflicts on save, "conflicts and server failures retain the editor" (no silent data loss on save failure).
  - Self-provisioning Postgres test cluster (own loopback DB, "never selects an existing personal database") — unusually careful test-isolation engineering.
  - Honest limitations documented in README rather than hidden: "no durable idempotency receipts yet," "not a complete multi-user service," "no protected leaderboard… no production-security certification" — deliberate, non-oversold documentation.
  - Demo/sample mode explicitly separated from DB-backed mode via a flag (`GLOBS_DEMO_MODE`), and failures are NOT silently replaced by sample data — avoids a common AI-slop fake-success-masking failure mode.
  - Web Locks API used for concurrent-tab conflict detection — a non-trivial browser API choice.
- Old-AI-generated smells: none seen — the README self-limitations list is the opposite of typical LLM overclaiming.
- Skill tags: fe-react, fe-next, be-rest-design, be-validation, db-postgres, orm, db-transactions, db-concurrency, idempotency, outbox, test-unit, test-e2e, test-integration, authn, design-docs-adrs
- Duplicate/overlap: none with others in this batch (unique game concept).
- Learning value: Very High — concurrency/transactions/idempotency/outbox are exactly the "senior CRUD judgment" seams called out in its own astraupskill README, and the honesty about limitations is itself a teaching artifact.
- Interview stories: "used optimistic-concurrency versioning to keep the editor's content on a failed save rather than silently discarding it"; "self-provisioned an isolated Postgres cluster for tests rather than risking a shared dev database."
- Proposed disposition: **A FLAGSHIP** — strong, well-documented, honestly-scoped CRUD+concurrency teaching project; pairs well with andie as evidence of the "Fable review pass" methodology.

## hypernova-inc-main
- Path: `12 Other Projects\hypernova-inc-main` — Origin: the user's own "HyperNova Inc" business app (bootstrapped via `create-plasmic-app`, deployed via AWS Amplify); the "-main" suffix most likely reflects a zip export of the user's own repo rather than a downloaded third-party FOSS project
- Type: web app (Next.js 14 marketing/estimator site) — the baseline copy
- State: working-looking, earlier/baseline version — Last modified: Jan 15 2026 (older than 3buildhyper's Jul 25 2026 files, confirming 3buildhyper is the evolved copy)
- Stack: identical to 3buildhyper (Next.js 14, Plasmic, AWS Amplify/DynamoDB/SES, antd5, three.js) but without CONTRIBUTING.md, fabledocs/, or meaningful `__tests__/` content; has `plasmic.lock` present (worth a direct diff vs. 3buildhyper's listing).
- Educational material: `fabledocs/` (3 files, same as 3buildhyper) + `docs/` (4 files).
- Duplicate/overlap: **confirmed duplicate/earlier version of 3buildhyper** — same package name, README intro, dependency set. This is the base copy 3buildhyper was built onto.
- Learning value: Low standalone (superseded by 3buildhyper) — keep only for diffing purposes.
- Proposed disposition: **G ARCHIVE** — superseded by 3buildhyper; diff first to verify no unique content (e.g. `plasmic.lock`) is lost, then archive.

## jdtrrain2.1
- Path: `12 Other Projects\jdtrrain2.1` — Origin: COURSE/GENERATED (LLM), Fable-style (astraupskill/ + dfableandopus/ pair, same pattern as andie/GlobGame)
- Type: web app — Jira/Linear-style team project-management platform
- State: working-looking — Last modified: dfableandopus Sep 18 2026, core app/db Feb 24 2026 (astraupskill authored Sep 12 2026, suggesting the course layer was added months after initial build)
- Purpose: Linear/Jira-clone project management tool — issue tracking, sprints, kanban, reporting.
- Stack: FE Next.js 16/React 19 (JS, not TS) + @dnd-kit (drag-and-drop Kanban) + @tanstack/react-query + @tiptap (rich text for issues/comments) + Recharts (velocity/burndown/distribution) + dayjs | BE Next.js API routes + SSE endpoint (real-time board refresh) | DB Prisma 6 + SQLite (dev.db committed, 237KB) | Test node:test
- Architecture: `src/app/api`, `src/components/{app-shell,providers}`, `src/lib/{cn,constants,prisma,search,server}`
- Complexity: Mid+ (RBAC + DnD kanban + SSE + custom query DSL + sprint reporting math)
- Educational material: EXCELLENT — `astraupskill/` (36 files, the **largest astraupskill pack in this whole batch**, likely covering the full feature set: RBAC, saved-filter query parsing, SSE, sprint burndown/velocity math) + `dfableandopus/` (7 files, interview-prep, consistent format with andie/GlobGame).
- Quality observations:
  - Custom query-syntax parser for saved filters (`assignee:me priority:high due:thisweek`) — non-trivial DSL-parsing feature, above typical CRUD.
  - SSE endpoint for real-time board refresh — a reasonable lighter-weight-than-WS real-time choice.
  - Integrations scaffold (Slack + GitHub webhook issue linking) explicitly labeled "scaffold" in the README — honest about incompleteness rather than overclaiming.
  - 4 explicit role tiers (OWNER/ADMIN/MEMBER/VIEWER) — real authz surface, not just a boolean isAdmin flag.
  - SQLite dev.db committed at repo root (237KB) — fine for local dev/course use, flag for exclusion from publish.
- Old-AI-generated smells: none strongly seen; the "scaffold" labeling for unfinished integrations is a positive honesty signal rather than a smell.
- Skill tags: fe-react, fe-next, fe-state, be-rest-design, be-validation, authn, authz-rbac, db-sqlite, orm, realtime-ws, queues, test-unit, crud-basic, design-docs-adrs
- Duplicate/overlap: none with others in this batch (unique domain — no other PM/issue-tracker tool present).
- Learning value: Very High — largest astraupskill course pack in the batch, broadest feature surface, real-time + RBAC + custom parsing combination is rare.
- Interview stories: "wrote a small DSL parser for saved-search filters (`assignee:me priority:high due:thisweek`) instead of a fixed filter UI"; "used SSE rather than WebSockets for board refresh and can explain the tradeoff."
- Proposed disposition: **A FLAGSHIP** — alongside aaa1 and GlobGame, one of the three strongest complete/well-documented/non-trivial projects in this batch.

## Obsidian
- Path: `12 Other Projects\Obsidian` — Obsidian vault (personal notes), not code. "JS Fund" vault — `Welcome.md`, `llm prompt.md`, `.obsidian/` config only (7 files total). Essentially empty/just-started, Last modified: Jan 8 2026.
- Note: name collision only with the home-dir `obsidian-vault/`/`obsidian-claude/` entries audited separately — this copy is an unrelated, near-empty personal study vault, not the KM-tool project.
- Proposed disposition: **G ARCHIVE** — one-line record, effectively empty.

## pp8
- Path: `12 Other Projects\pp8` — Origin: COURSE/GENERATED (LLM), explicitly a **comparison-pair project**: README states "This repository recreates a unified HR platform in a Python-first stack so its backend architecture can be compared over time with a TypeScript-first version" — implying a sibling TS-first HR-platform project exists elsewhere, **not found in this batch**
- Type: web app/API — Python-first "Unified HR Platform" (multi-tenant HRIS)
- State: working-looking — Size: 94 files total, 45 backend Python files — Last modified: frontend Jul 29-30 2026, docs/docker-compose Apr 9 2026
- Purpose: multi-tenant HRIS core + performance reviews/goals + integration-hub admin/job processing — explicitly framed as a backend-architecture teaching artifact meant for stack comparison (Python vs TS).
- Stack: BE Python (FastAPI implied by structure — `backend/app/`, Alembic migrations, `backend/scripts`, `backend/tests`) | DB Postgres via Alembic | FE separate `frontend/src/` (framework unconfirmed — NEEDS DEEPER INSPECTION) | Infra docker-compose.yml
- Architecture: `backend/{app,alembic,scripts,tests}`, `frontend/src`, `docs/{architecture,learning}`
- Complexity: Mid/Mid+ (multi-tenant HRIS, migrations, integration-hub job processing)
- Educational material: USEFUL — `docs/architecture/` + `docs/learning/` (11 files total, incl. a "guided-reading-path.md" — same pattern as aaa1's docs/learning/, suggesting both may share an authoring process).
- Quality observations:
  - Alembic migrations present — real DB migration discipline rather than just `db push`.
  - `docker-compose.yml` for local dev — infra-as-code present, unlike many JS/Prisma projects in this batch relying on local Postgres installs.
  - Explicit multi-tenant HRIS + integration-hub job processing implies async job handling (not directly confirmed by listing alone).
  - Deliberately meta/pedagogical framing (architecture-comparison artifact) vs. other standalone projects in this batch.
- Old-AI-generated smells: none seen at this pass; NEEDS DEEPER INSPECTION of `backend/app` internals to rule out shallow route stubs.
- Skill tags: be-python, be-rest-design, be-validation, db-postgres, db-migrations, multitenancy, docker, design-docs-adrs, be-async-jobs (tentative)
- Duplicate/overlap: references a "TypeScript-first version" sibling not present in this batch — worth searching elsewhere in the portfolio for the matching TS-first HR platform.
- Learning value: High — Python-stack counterpart specifically valuable for stack-comparison teaching purposes.
- Proposed disposition: **B HIGH-VALUE** — valuable standalone and as one half of an explicit architecture-comparison pair; locate the TS sibling for full value.

## pyhealth\healthchecks
- Path: `12 Other Projects\pyhealth\healthchecks` — Origin: **CONFIRMED OPEN-SOURCE CLONE** — literally the upstream `healthchecks/healthchecks` Django project (README badges reference `github.com/healthchecks/healthchecks/actions`, Coveralls badge, etc.); no `.git` in this copy, no local modifications evident.
- Type: web app/API — cron-job monitoring service (dead-man's-switch alerting)
- State: complete (full upstream project) but **not the user's own work** — vendored/downloaded reference copy — Size: 1,285 files total, 650 Python files, by far the largest single directory in this batch — Last modified: May 16 2026 (copy date, no `.git` to confirm upstream commit)
- Purpose: SaaS cron-monitoring service — pings from scheduled jobs, alerting when a ping doesn't arrive on time.
- Stack: BE Django (Python) | DB unspecified in this pass (upstream supports Postgres/MySQL/SQLite) | Auth WebAuthn 2FA per README, 25+ notification integrations, team/project/read-only-member management | Infra `docker/`, `.github/` CI workflows
- Architecture: standard Django app layout (`hc/` app dir, templates/, static/, docs/, stuff/)
- Complexity: Production-like (genuine, deployed open-source SaaS codebase)
- Educational material: upstream `docs/` (real Django project documentation, not portfolio-authored teaching material).
- Quality observations: a mature, real-world OSS codebase well beyond typical LLM-generated course quality (real CI, WebAuthn, 25+ integrations, Coveralls tracking) — but it is NOT built by the user/Claude; reference material only.
- Old-AI-generated smells: N/A — not LLM-generated.
- Skill tags: legacy-codebase-reading, be-python, authn, observability-logs, queues (likely), docker, ci-cd
- Duplicate/overlap: none with others in this batch. Naming ("pyhealth") is misleading — sounds health-domain but is a devops/monitoring tool; the outer folder contains only this one clone.
- Learning value: High but purely as a study/reference artifact — excellent for legacy-codebase-reading practice, should NOT be presented as original/course work.
- Proposed disposition: **D REFERENCE** — keep as a legacy-codebase-reading study artifact; explicitly exclude from "work I built" listings; verify no license-attribution obligations if ever surfaced publicly.

## inventory-system
- Path: `C:\Users\Owner\inventory-system` — Origin: COURSE/GENERATED (LLM), explicitly "an educational full-stack application" per README, heavily annotated code
- Type: monorepo(2 apps) — React/Vite frontend + Node/Express backend, Inventory Management System
- State: working-looking/docs-heavy skeleton — no `.git` repo at all, no tests found, never verified as run in this audit — Size: 53 files, ~23,000 LOC (large fraction is comment/prose — package.json even carries `_comment_*` keys explaining every dependency) — Last modified: 2026-02-02 (mtime; no git history)
- Purpose: teaches full-stack CRUD + Redux + REST patterns via a product/category/supplier/transaction inventory tracker with reorder-point alerts.
- Stack: FE React18+Redux Toolkit (createEntityAdapter)+React Router6+Tailwind3+Vite+Axios | BE Node/Express4+better-sqlite3+Zod validation+Helmet+CORS+Morgan | no ORM (raw SQL via schema.sql/queries.js) | no auth | no test framework configured
- Architecture: classic MVC-ish layering — routes → controllers → services (alertService, inventoryService, orderService) → models → SQLite; frontend uses Redux slices per domain
- Complexity: Junior/Junior+ (deliberately scoped, no auth/multitenancy/real-time)
- Educational material: STRONG — the entire project IS the educational material; README.md (28.6KB) is a full curriculum (Learning Goals, Key Concepts, Exercises for Learners, Troubleshooting). No separate docs/ dir — README + source comments serve that role, better-than-typical "why" explanations (e.g. why Zod, why better-sqlite3).
- Quality observations:
  - Zod validation middleware at the API boundary (`backend/src/middleware/validation.js`).
  - No authentication/authorization anywhere — fine for a scoped teaching app but flag if repurposed.
  - Raw SQL + prepared statements via better-sqlite3, `schema.sql` as source of truth.
  - No test suite whatsoever despite README claiming "best practices."
  - No git repository — can't verify history/provenance/completeness via commits.
  - Business logic separated into a services/ layer — decent separation of concerns, not a fat-controller anti-pattern.
  - Controllers are large (450-600 lines) but padded heavily with concept-explaining comments, not necessarily complex logic.
- Old-AI-generated smells: very high comment-to-code ratio (borderline excessive prose-as-documentation, typical of LLM tutorial generation) but not shallow/wrong — no hallucinated APIs spotted in sampled files; no tests = weak-tests smell; no git = can't confirm it was ever run.
- Skill tags: fe-react, fe-state, fe-forms-validation, be-node-express, be-validation, be-rest-design, db-sqlite, db-sql-raw, crud-basic
- Duplicate/overlap: none with the other home-dir projects.
- Learning value: Medium-High — strong narrative teaching content for junior devs on Redux Toolkit + REST + validation, but lacks tests/auth so it's an incomplete picture of production practice.
- Proposed disposition: **E EXERCISE SOURCE** (or D REFERENCE) — well-written teaching narrative and clean small-scope architecture make it a useful curated reference/exercise base; not flagship-quality given no tests/git/auth.

## jeopardy-game-refactor
- Path: `C:\Users\Owner\jeopardy-game-refactor` — Origin: ORIGINAL build with an LLM-assisted "refactor" arc (commit history shows explicit refactor stages)
- Type: monorepo(2 apps) — multiplayer Jeopardy trivia game with accounts/social features
- State: working-looking, most mature of the 5 home-dir projects — **real git history (4 commits, HEAD 2026-01-10)**, backend Jest unit tests (`backend/tests/api/sessions.test.js`) AND frontend Playwright e2e specs (game-setup, gameplay, session-end) plus a full `SETUP_AND_TESTING.md`; migrations exist (`prisma/migrations/20251231015740_init`)
- Size: 112 files, ~7,200 LOC — Last commit: 2026-01-10 15:29:19 -0800
- Purpose: multiplayer Jeopardy-style trivia game with user auth, friends, game creation/sharing (public/shared games), host controls, daily doubles — a social gaming product, not just a CRUD demo.
- Stack: FE React18+Vite+React Router+Context API (AuthContext/GameContext, not Redux)+Axios+Playwright | BE Node/Express+PostgreSQL+Prisma+Joi validation+JWT (jsonwebtoken+bcryptjs)+Jest, `docker-compose.test.yml` for a test DB, Neon serverless-Postgres config present (`backend/.neon`)
- Architecture: layered — routes → controllers → services → Prisma models; JWT bearer-token auth middleware; frontend Context-based auth/game state
- Complexity: Mid — real auth, relational data model, multiplayer session state, e2e test coverage; more than CRUD-basic but not distributed/microservices-scale.
- Educational material: NONE as a separate curriculum tree — README.md + SETUP_AND_TESTING.md are practical setup/testing guides, not a course. This is product-shaped, not course-shaped.
- Quality observations:
  - Real automated test pipeline: Jest backend API tests + Playwright e2e (3 spec files) + dedicated `docker-compose.test.yml` + `seed-e2e.js` fixture — more test rigor than any of the other 4 home-dir projects.
  - **SECURITY SMELL**: `JWT_SECRET` has a hardcoded fallback default (`process.env.JWT_SECRET || 'jeopardy-secret-key'` in authService.js) — would silently run insecure in prod if env var unset.
  - Password hashing via bcryptjs with proper salt rounds (10).
  - Joi used for request validation (`backend/src/utils/validationSchemas.js` + `middleware/validate.js`).
  - Prisma schema is clean and normalized (User, Game, Category, Question, GameSession, etc. with `@@map`, cascading deletes on Category→Game).
  - Real git history shows genuine incremental evolution: "Initial commit" → "Complete refactor with auth/friends/sharing" → "automated test pipeline" → "setup docs."
  - Controllers/services appropriately small (most <150 lines) — no god-files.
- Old-AI-generated smells: none significant — this is the most "real" looking of the 5 home-dir projects. Only flag is the hardcoded JWT secret fallback and unverified rate-limiting/authz-ownership checks on game/session endpoints (NEEDS DEEPER INSPECTION for IDOR).
- Skill tags: fe-react, fe-state, fe-testing, be-node-express, be-validation, be-error-handling, authn, db-postgres, db-migrations, orm, test-unit, test-e2e, test-ci (partial), crud-basic
- Duplicate/overlap: per naming and git history, strongly likely a rebuild/refactor of an earlier "FinalJep"-family project (the Jeopardy-game family spans curse, appmaketrck, finaljepgame, FinalJep in "12 Other Projects" — see cross-references there). Flag for direct cross-referencing/diffing against `curse/Jeopardy-Game` in particular.
- Learning value: High — good example of authn + Prisma + layered architecture + real test pyramid (unit+e2e) in a compact, readable codebase; good portfolio/interview-prep material given it visibly demonstrates a refactor arc.
- Interview stories: "walked through a refactor arc from initial commit to a fully socially-featured multiplayer game, backed by real commits and a test pipeline added along the way."
- Proposed disposition: **B HIGH-VALUE** — most production-credible of the 5 home-dir projects, has tests and real git history, reasonably sized; worth promoting/polishing (fix the JWT secret fallback) rather than archiving. Likely the strongest candidate to be "the" canonical Jeopardy game across the whole archive — cross-reference against curse/Jeopardy-Game before finalizing.

## stellar-conquest
- Path: `C:\Users\Owner\stellar-conquest` — Origin: ORIGINAL design, implementation built directly against `stellar-conquest-architecture\ARCHITECTURE.md` (confirmed: the architecture doc's route list/tech choices map onto this repo's actual `apps/api/src/routes/*.ts` files)
- Type: monorepo(3 packages: apps/api, apps/mobile, packages/shared) — real-time multiplayer mobile strategy game
- State: skeleton/partial — **no `.git` directory, no tests found anywhere**, no evidence it has ever been run — a substantial but unverified scaffold built against the architecture doc
- Size: 78 files, ~13,400 LOC (TS) — Last modified: 2026-01-07 (mtime only)
- Purpose: free-to-play persistent multiplayer space-strategy game (Tribal Wars/OGame-style: build stations, train fleets, gather resources, attack/defend, alliances) with a premium-currency ("Galactic Credits") monetization/shop system and leaderboard rewards.
- Stack: FE React Native+Expo Router (file-based routing under `app/(app)` and `app/(auth)`), Zustand stores (auth/game/shop) | BE Fastify+@fastify/jwt+@fastify/websocket+@fastify/cors+Prisma+PostgreSQL+ioredis (Redis for game-tick/queue state) | shared `packages/shared` holds game-balance formulas/constants/types used by both FE and BE
- Architecture: real-time game-server pattern — `GameTickProcessor.ts` (945 lines) runs interval-based ticks (resource production every 60s, queue completion every 1s, fleet movement every 5s) backed by Redis+Postgres, pushed to clients via a WebSocketManager; route handlers per domain (auth, account, world, player, station, fleet, alliance, shop, leaderboard, report)
- Complexity: Mid+/Senior-oriented in design intent (real-time tick engine, monetization, WebSocket sync) but Junior+/Mid in verified execution since nothing is tested or proven to run
- Educational material: NONE inside stellar-conquest itself — the narrative/teaching content lives entirely in the separate `stellar-conquest-architecture` doc.
- Quality observations:
  - JWT secret again has an insecure hardcoded fallback: `process.env.JWT_SECRET || 'your-super-secret-key-change-in-production'` — worse because the fallback string literally says "change in production" and wasn't changed.
  - Reasonably sophisticated real-time architecture: multi-tier tick rates, Redis for hot state, Postgres for durable state, WebSocket push — legitimately non-trivial system design, above tutorial level.
  - Prisma schema (569 lines) is well-normalized with explicit `@map` to snake_case columns, tracks lifetime/credit-balance separately from spendable balance — decent domain modeling for a monetized game.
  - No tests at all — can't verify the GameTickProcessor's tick math, idempotency, or race-safety under concurrent access.
  - No visible transaction wrapping observed in the tick processor at a glance (NEEDS DEEPER INSPECTION — concurrent resource-tick + queue-tick + fleet-tick on shared Postgres rows without visible locking/transactions is a plausible race-condition risk, common in this class of game-server code).
  - No CI, no docker-compose, no `.env.example` spotted — deployment/config story is undocumented in-repo.
- Old-AI-generated smells: large single-purpose files (GameTickProcessor.ts at 945 lines, "do everything in one class" pattern); zero tests despite substantial complexity is a classic AI-scaffold smell (breadth without depth/verification); hardcoded insecure JWT fallback repeats verbatim the pattern seen in jeopardy-game-refactor, suggesting a similar generation-process lineage.
- Skill tags: fe-react, mobile-rn, fe-state, be-node-express (Fastify variant), be-rest-design, be-async-jobs, authn, db-postgres, db-modeling, orm, realtime-ws, queues (Redis-based, informal), arch-event-driven, config-secrets (flagged weak)
- Duplicate/overlap: **STRONG STACK/DOMAIN OVERLAP with the user's own memory-indexed "Warband (spacegame)" project** (Desktop\spacegame — Tribal Wars-style, Expo+Fastify+Prisma+BullMQ, COMPLETE with 63 tests per memory). stellar-conquest is thematically and technically near-identical (also Tribal-Wars-style, also Expo mobile + Fastify + Prisma, also alliance/fleet/resource mechanics) but appears less complete (no tests, no git, Redis+ad-hoc intervals instead of BullMQ). Strongly recommend a direct comparison against Desktop\spacegame — this may be an earlier/abandoned/duplicate attempt at the same game concept.
- Learning value: High for the architecture/real-time-systems angle, but currently unverified — value is capped until it's actually run/tested.
- Proposed disposition: **C SPECIALIZED, pending F CONSOLIDATE review** — specialized real-time-game-server exercise, but given the likely duplicate with Desktop\spacegame, recommend explicit reconciliation before deciding keep/archive. Do not treat as flagship until tests exist and the spacegame-overlap question is resolved.

## stellar-conquest-architecture
- Path: `C:\Users\Owner\stellar-conquest-architecture` — Origin: ORIGINAL design doc, companion to `stellar-conquest`
- Type: docs-only — single design/architecture document
- State: docs-only, complete as a document — Size: 1 file, 78KB / 1,761 lines (`ARCHITECTURE.md` v2.0) — Last modified: 2026-01-07 (same day as stellar-conquest code — likely generated together/same session)
- Purpose: full game-design + system-architecture spec for Stellar Conquest, explicitly "inspired by Valor/Tribal Wars, set in space," including a full theme-mapping table (Village→Space Station, Barracks→Shipyard, etc.) and monetization/business-model rationale.
- Full table of contents: Game Overview, High-Level Architecture, Core Game Systems, Monetization, Leaderboards, Database Design, API Architecture, Real-Time Systems, Tech Stack, Infra & Deployment, Security Considerations, Extensibility.
- Relationship to stellar-conquest: **CONFIRMED direct source doc** — the code's route filenames and Fastify+Prisma+Postgres+Redis+WebSocket stack match the doc's Tech Stack and API Architecture sections; this is the design artifact stellar-conquest was implemented from (a partial implementation — code covers auth/account/world/player/station/fleet/alliance/shop/leaderboard/report, matching the doc's route inventory).
- Educational material: the document itself functions as a system-design teaching artifact (ADR-like: rationale for architecture choices, a "Security Considerations" section, an "Extensibility" section) — valuable as a design-docs-adrs exercise independent of whether the code ships.
- Quality observations:
  - Well-organized, thorough ToC-driven structure with ASCII architecture diagrams (client/backend/data-layer separation).
  - Dedicated "Security Considerations" section (not verified against the actual code — the code has at least one contradicting smell, the hardcoded JWT fallback noted above).
  - Explicit business-model/monetization design (credits, no-pay-to-win framing) — good example of translating product requirements into technical architecture.
- Old-AI-generated smells: none as a document — well-structured, not generic boilerplate, clearly customized to this specific game.
- Skill tags: design-docs-adrs, arch-event-driven, realtime-ws, security-owasp (as topic, not verified impl), observability-logs (mentioned)
- Duplicate/overlap: paired 1:1 with stellar-conquest; no overlap with the other home-dir projects.
- Learning value: High — good example of "write the architecture doc first" discipline, useful as a design-docs-adrs teaching artifact and as a rubric to grade the stellar-conquest implementation against.
- Proposed disposition: **D REFERENCE** — keep paired with stellar-conquest as its design counterpart; useful reference/rubric document regardless of what happens to the code.

## obsidian-claude
- Path: `C:\Users\Owner\obsidian-claude` — Origin: ORIGINAL, spec-driven build (companion to root-level `obsidian-claude-architecture.md` and `obsidian-claude-spec.md`, and to `C:\Users\Owner\obsidian-vault` as the runtime data directory)
- Type: monorepo(2 packages: core, mcp-server) — MCP (Model Context Protocol) server + library for Obsidian vault integration
- State: **PARTIAL/BROKEN SKELETON** — critical gap: `packages/mcp-server/package.json` declares `"main": "./dist/index.js"`, a `bin` entry, and a `tsup src/index.ts` build script, but **there is no `packages/mcp-server/src/index.ts` file** (only `src/tools/*.ts` exist) — the package cannot currently build or run as an MCP server; `src/resources/` referenced by nothing is empty; no `.git`; no tests despite vitest devDependency; `scripts/init-vault.js` is referenced by the root package.json's `init-vault` script but `scripts/` is empty.
- Size: 36 files (24 source .ts files), ~3,000 LOC — Last modified: 2026-01-07
- Purpose: a personal-knowledge-management system pairing Obsidian with Claude Code via MCP, targeted at a junior developer's structured growth tracking — daily capture, weekly review, time logging, competency-evidence tracking, and an AI "ask/explain" interface over the vault content.
- Stack: TypeScript, pnpm workspaces, better-sqlite3 (metadata cache/DB), `@modelcontextprotocol/sdk`, Zod, tsup (build), vitest (configured but unused), ESLint+typescript-eslint
- Architecture: two-package design — `packages/core` (vault.ts, parser.ts, search.ts, templates.ts, database.ts, watcher.ts, types.ts) and `packages/mcp-server` (tool handlers: ask, capture, daily, explain, log-time, monthly-snapshot, process, project-status, weekly-review — each an MCP tool)
- Complexity: Mid (MCP tool-server pattern, SQLite caching, file watching — a legitimate real-world integration pattern) but currently non-functional as shipped
- Relationship to supporting files (read as context, not deeply audited separately):
  - `C:\Users\Owner\obsidian-claude-spec.md` (1,094 lines): full product spec — user profile (junior full-stack dev, 1-3yrs, backend/Node focus), goals/anti-goals, vault structure, tag taxonomy, templates, MCP server spec, workflows, a "Senior Engineer Competency Framework," feature specs, implementation phases. Dated 2026-01-07, "Designed collaboratively with Claude Code."
  - `C:\Users\Owner\obsidian-claude-architecture.md` (954 lines): system architecture doc — layers (Claude Code CLI / Obsidian Desktop / optional Web Dashboard → MCP Server + Sync Service + optional API Server → Core Library → Data Layer: vault files + SQLite cache + FlexSearch index).
  - `C:\Users\Owner\obsidian-vault`: the actual runtime data directory — contains a real `.cache.db` (SQLite, consistent with `database.ts` schema), a genuine daily note (`daily/2026-01-08.md` — one day after the spec was written), templates/, growth/, notes/test-note.md, projects/. This is live/used evidence, not just scaffolding — the system was actually exercised for at least one day, though unclear whether via the (currently non-buildable) mcp-server or manual editing.
- Educational material: MINIMAL as codebase teaching material — the spec.md embeds a "Senior Engineer Competency Framework" intended as a personal growth-tracking curriculum for the user, not a codebase teaching artifact for others.
- Quality observations:
  - Clean separation of concerns: core (vault I/O, SQLite cache, template engine, search, file watcher) vs. mcp-server (thin tool handlers ~40-150 lines each).
  - `database.ts` schema is sensible: notes-metadata cache, time_entries, link graph (source/target wikilinks), growth evidence table — matches the spec's feature list closely (good spec-to-schema traceability).
  - **CRITICAL GAP**: missing mcp-server entrypoint (`src/index.ts`) means the system as committed cannot be built/run at all — the most incomplete/non-functional of the 5 home-dir directories despite looking well-organized on the surface.
  - No tests despite vitest configured in both package.json files.
  - No git repository — no way to see whether `index.ts` was deleted, never created, or lost.
  - The presence of a genuinely-used `obsidian-vault` (real daily note, real `.cache.db`) suggests SOME version of this ran at some point — possible drift between what ran and what's currently checked out.
- Old-AI-generated smells: classic "breadth without integration" — 9 well-scoped tool files, a solid core library, a matching SQLite schema, all individually plausible, but the piece wiring them together (the MCP server entrypoint registering these tools) is missing — a common failure mode when an LLM generates many files across a large plan but the session ends before final integration is verified.
- Skill tags: db-sqlite, db-modeling, agentic-engineering, ai-llm-integration, design-docs-adrs, arch-modular-monolith
- Duplicate/overlap: none with the other 4 home-dir projects (unique PKM/MCP domain); paired 1:1 with the two root-level `.md` files and with `obsidian-vault` as its data directory. **Very likely related to `12 Other Projects\appmaketrck\obsidian-claude`** (audited separately in that batch section) — that copy is described as a fuller/similar KM-tool implementation; recommend a direct diff to determine which is canonical/newer before disposition.
- Learning value: Medium — good MCP-server pattern reference and spec-to-code traceability example, but the missing entrypoint means it can't currently be run/demoed, capping its value until fixed.
- Proposed disposition: **C SPECIALIZED** (needs a small fix — restore/write `src/index.ts` — before it's demo-able); the spec.md/architecture.md pair is **D REFERENCE**-worthy on its own even if the code disposition changes. Flag the missing entrypoint explicitly, and flag the likely duplicate at `appmaketrck/obsidian-claude` for a direct diff.

---

## Batch observations

**Recurring "anti" template family (07 Anti Projects).** antiemponb, antihelpdesk, antiinv share an identical monorepo shape (Express+TS backend, `src/modules/<domain>/{controller,routes,schemas,service}.ts`, Prisma+Postgres, JWT access/refresh+bcrypt, Zod+RHF frontend); antitestbuild is a NestJS variant of the same conceptual template. All four share an **identical insecure hardcoded-JWT-secret-fallback smell**, strong evidence of one generator/prompt lineage. Worth a single portfolio-wide fix note rather than four separate ones. Same JWT-fallback smell independently recurs in `vg`, `VGdemo`'s .NET port (worse — token IS the raw user ID), `jeopardy-game-refactor`, and `stellar-conquest` — this is a systemic pattern across many builds in this batch, not isolated to "anti".

**Astra/Fable review-pass fingerprint.** A recognizable, repeatable teaching-pack pattern (`astraupskill/` 7-file structure + `evidence/`+`snapshots/`+`VERIFICATION.md`, often paired with `dfableandopus/` interview-prep packs) recurs across antiemponb, antihelpdesk, appmaketrack, grouphelpdesk, HNJOBTRACK, recipegen-app, andie, GlobGame, jdtrrain2.1, and the `job track` sub-projects — consistent with the user's memory entry "fablereview-astra-audit" (a 153-project Astra review+fix pass). Projects that went through this pass (antiemponb/antihelpdesk vs. antiinv/antitestbuild) show measurably better test discipline where the pass touched code, but coverage remains thin outside the touched module in every case — the underlying generation process appears to produce near-zero baseline tests, with Astra adding one verified, evidence-backed worked example per project rather than full coverage.

**The Jeopardy-game family is sprawled across at least 5 locations**: `curse/Jeopardy-Game` (fullest-featured: OAuth, friends, sharing — likely canonical), `appmaketrck/Jeopardy-Game` (simpler/earlier variant, same stack), `finaljepgame/jeopardy-maker` (separate Next.js+Prisma rewrite), `FinalJep/finaljep-app`+`finaljep-temp` (possibly an abandoned Convex-based rewrite, unclear if even Jeopardy-related — boilerplate READMEs), and the home-dir `jeopardy-game-refactor` (most production-credible: real git history, Jest+Playwright tests, JWT auth — likely the strongest candidate for "canonical"). Recommend one consolidated cross-referencing pass (ideally a real diff) before any archive/consolidate decisions.

**The obsidian-claude / PKM-tool family is duplicated at least twice**: `appmaketrck/obsidian-claude` (in 12 Other Projects) and the home-dir `obsidian-claude` (paired with `obsidian-claude-spec.md`, `obsidian-claude-architecture.md`, and the live `obsidian-vault/` data directory, which shows real one-day usage). The home-dir copy has a confirmed broken build (missing `mcp-server/src/index.ts` entrypoint) — worth checking whether `appmaketrck`'s copy has that file and is the more complete/later version.

**The recipe-gen and HyperNova pairs are simple supersession chains, not real duplicates to reconcile**: recipegen (empty) → recipegen-temp (boilerplate) → recipegen-app (full build, canonical); hypernova-inc-main (baseline) → 3buildhyper (baseline + fabledocs + CONTRIBUTING + tests, canonical). Both are safe, low-risk F/G-tier consolidations.

**The EOR (Employer-of-Record) business domain now spans at least three independent builds** across the whole portfolio in three different stacks: `vg` (Next.js/JS, larger/more ambitious, confirmed unfixed security bugs, no tests), `VGdemo/globalhire-lite` (React/Express/TS, smaller, tested, plus a `migrated-dotnet/` C# port with its own documented security regression), and the memory-indexed "Atlas Course 8 (.NET EOR)" course. `VGdemo` is the strongest of the three as a teaching asset specifically because of its documented TS-vs-.NET security-regression comparison.

**`grav1pretalx` duplicates an open-source clone already present elsewhere on disk** (`03 Master Projects\masterpre`, per user memory) — same vendored pretalx source, different (non-overlapping) curriculum layered on top. Both `graveopenjspy`/`gravreviewboardjspy` and `grav1pretalx` follow the same repeatable pattern: take a real large OSS project, leave the source untouched, and layer on (a) a docs/upskill curriculum, (b) a User-Stories/exercise set, and (c) for two of the three, a "rewrite this app in modern JS/TS" migration blueprint. `pp8` (Python-first HR platform) explicitly references an unfound "TypeScript-first version" sibling — worth searching the rest of the archive for it.

**"10 New Folders" is pure filesystem litter** — all 12 numbered "New folder*" directories are completely empty, almost certainly leftover extraction/drag-and-drop artifacts. Zero content to evaluate; safe single-action archive/delete candidate.

**Several folders are not single projects but unsorted buckets** that need to be split before individual cataloging: `08 App…\job track` (5 distinct sub-projects, only 2 of which are actually about job tracking), `12 Other…\appmaketrck` (3 unrelated sub-projects: air-quality monitor, Jeopardy game, obsidian-claude KM tool), and `12 Other…\FinalJep` (2 unrelated scaffolds). None of these should be treated as one project in any downstream reorganization step.

**Near-universal absence of committed git history.** With the sole exceptions of `eliapplybot` (2 commits) and `jeopardy-game-refactor` (4 commits), every directory audited in this batch — across all six source folders — reports "no commits yet" or has no `.git` at all, despite many being substantial, working-looking codebases. This is a portfolio-wide housekeeping gap (needs initial commits/pushes) rather than a per-project defect, and it also means every "Last modified" date above is a filesystem mtime, not a verified commit timestamp.

**Strongest candidates from this batch** (recommended A FLAGSHIP tier): `grouphelpdesk`, `HNJOBTRACK`, `aaa1`, `GlobGame`, `jdtrrain2.1` (all unconditional A), plus `antitestbuild` and `VGdemo/globalhire-lite` as flagship *candidates* pending a test-coverage pass and a formal promotion decision respectively.
