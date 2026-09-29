# Batch 11 — Master Projects: mostly cloned open-source apps + generated upskill curricula
Scope: 03 Master Projects\{mastermorphic, masternext, masternovu, masteropen, masteropenedxPYJS, masterpaper, masterplane, masterpload, masterpostiz, masterpre, masterrnative, mastersaleorPY, mastershadcn, MasterStore, mastersupa, mastertea, mastertool, mastertwenty, mastertypebot, masterumami, masterzulipPY}  |  Candidate dirs inspected: 21  |  Meaningful projects: 21 (curriculum quality varies; 4 are bare clones with no curriculum)  |  Tiny/empty/boilerplate: 0

No git history exists for any of these repos (`git log` fails with "does not have any commits yet" everywhere — these are working-tree clones/snapshots, not committed repos). All dates below are directory mtimes, not commit dates.

| Project | Path | Type | Origin | Stack | Complexity | Docs | Disp |
|---|---|---|---|---|---|---|---|
| Morphic clone + curriculum | mastermorphic\morphic | monorepo(web app) | OPEN-SOURCE CLONE (Morphic AI answer engine) | Next.js, Drizzle, Bun | Production-like | STRONG (fabledocs/, 53 files, flat layout) | B |
| NextCRM clone + curriculum | masternext\nextcrm-app | monorepo(web app) | OPEN-SOURCE CLONE (NextCRM) | Next.js 16, Prisma 7/Postgres, better-auth, Inngest | Production-like | STRONG (fabledocs/upskill/, 53 files) | B |
| Novu clone (bare) | masternovu\novu | monorepo(N apps) | OPEN-SOURCE CLONE (Novu notifications infra) | Nx/pnpm, apps/, libs/, enterprise/ | Production-like | NONE | D |
| OpenStatus clone + curriculum pack | masteropen\openstatus | monorepo(N apps) | OPEN-SOURCE CLONE (OpenStatus status pages) | Next.js, tRPC, Hono/Bun, Go checker, Drizzle/libSQL, Tinybird | Production-like | EXCELLENT (fabledocs 1-4, 79 files total) | A |
| Open edX Platform clone + curriculum | masteropenedxPYJS\openedx-platform | monolith (LMS+CMS) | OPEN-SOURCE CLONE (Open edX) | Django (lms/cms), Python, JS | Production-like | STRONG (docs/upskill/, 53-file structure) | B |
| Paperless-ngx clone + curriculum | masterpaper\paperless-ngx | monorepo(web app) | OPEN-SOURCE CLONE (Paperless-ngx) | Django, Celery, Angular (src-ui) | Production-like | STRONG (fabledocs/, 53 files) | B |
| Plane clone + curriculum | masterplane\plane | monorepo(N apps) | OPEN-SOURCE CLONE (Plane PM) | Django/DRF, Celery, MobX SPAs, Hocuspocus CRDT | Production-like | STRONG (fabledocs/, 53 files, flat layout) | B |
| Payload CMS clone + curriculum | masterpload\payload | monorepo(N apps) | OPEN-SOURCE CLONE (Payload CMS) | Next.js, TS, multi-adapter DB, Sentry | Production-like | STRONG (fabledocs/, 53 files) | B |
| Postiz clone + curriculum | masterpostiz\postiz-app | monorepo(N apps) | OPEN-SOURCE CLONE (Postiz social scheduler) | NestJS, Temporal, Next.js 16, Jenkins/Sonar | Production-like | STRONG (fabledocs/, 53 files) | B |
| pretalx clone + curriculum | masterpre\pretalx | monolith (conference tool) | OPEN-SOURCE CLONE (pretalx) | Django 6, Celery, django-scopes | Production-like | STRONG (fabledocs/, 53 files) | B |
| RN CRUD app + review pack | masterrnative | mobile app (RN/Expo) | ORIGINAL (Fable-built) + AI review artifact | Expo 54, React Native 0.81, React 19, react-hook-form, zod | Junior | USEFUL (astraupskill/, 12 files — Astra fleet-review sample, not curriculum) | C |
| Saleor clone + curriculum | mastersaleorPY\saleor | monolith/API (GraphQL commerce) | OPEN-SOURCE CLONE (Saleor) | Django, GraphQL (Graphene), Postgres | Production-like | STRONG (docs/upskill/, 53-file structure) | B |
| shadcn/ui clone + curriculum | mastershadcn\ui | monorepo(N apps) | OPEN-SOURCE CLONE (shadcn/ui) | React, Vite/Turbo, Vitest, CLI packages | Mid+ | STRONG (fabledocs/, 53 files) | B |
| Spree storefront app + learning docs | MasterStore\storefront (+ MasterStore\astraupskill review pack) | web app (Next.js e-commerce) | ORIGINAL (Fable-built, Spree SDK client) | Next.js 16, @spree/sdk, Stripe/Adyen/PayPal, next-intl, Vitest | Mid+ | STRONG (docs/mission-learning-path + architectural-cartographer + user-story-build-path, ~15 files) + separate astraupskill review pack (12 files) | B |
| Supabase clone (bare) | mastersupa\supabase | monorepo(N apps) | OPEN-SOURCE CLONE (Supabase) | Postgres, pnpm/Turbo monorepo | Production-like | NONE | D |
| Teable clone + curriculum | mastertea\teable | monorepo(N apps) | OPEN-SOURCE CLONE (Teable, Airtable clone) | NestJS, Next.js (pages), ShareDB, dual-Prisma | Production-like | STRONG (fabledocs/, 53 files) | B |
| ToolJet clone (bare) | mastertool\tooljet | monorepo(FE+BE) | OPEN-SOURCE CLONE (ToolJet low-code) | React frontend, Node/Rails-style server, plugins | Production-like | NONE | D |
| Twenty CRM clone + curriculum pack | mastertwenty\twenty | monorepo(N apps) | OPEN-SOURCE CLONE (Twenty CRM) | Nx/Yarn monorepo, Next/React, NestJS-ish backend | Production-like | EXCELLENT (fabledocs 1-4, 79 files total) | A |
| Typebot clone (bare) | mastertypebot\typebot.io | monorepo(N apps) | OPEN-SOURCE CLONE (Typebot chatbot builder) | Nx, Next.js, packages/ | Production-like | NONE | D |
| Umami clone + curriculum | masterumami\umami | monorepo(web app) | OPEN-SOURCE CLONE (Umami analytics) | Next.js, Prisma, Postgres/ClickHouse, Cypress | Production-like | STRONG (fabledocs/, 53 files) | B |
| Zulip clone + curriculum | masterzulipPY\zulip | monolith (chat app) | OPEN-SOURCE CLONE (Zulip) | Django (zerver/), Python, TS/JS (web/) | Production-like | STRONG (docs/upskill/, 53-file structure) | B |

All curriculum-bearing projects share one generation template (confirmed by directory listing across the batch): `00-fast-track.md`, `01-codebase-cartography/`, `02-stack-and-language-mastery/`, `03-architecture-and-patterns/`, `04-code-reading-gym/`, `05-quality-engineering/`, `06-contribution-practice/`, `07-career-and-collaboration/`, `08-interview-prep/`, `09-reference/` (or `08-reference/` for the 9-module variant used on masteropenedxPYJS/mastersaleorPY/masterzulipPY), plus `README.md` — ~53 files. Four projects (masteropen, mastertwenty) additionally have `fabledocs2/3/4` (7/12/7 files: onboarding pack, ADRs w/ interview translation, practice pack) authored on top of the base 53, matching this user's known "second pass" pattern from other batches.

## Morphic clone + curriculum
- Path: `mastermorphic\morphic` — Origin: OPEN-SOURCE CLONE (Morphic AI answer engine) — Type: web app (monorepo-flavored single Next.js app)
- State: complete (full clone, curriculum complete) — Size: large clone (app/, components/, lib/, drizzle/) — Last modified: 2026-07-10 (dir mtime)
- Purpose: AI-powered answer-engine/search UI (Perplexity-style) with model routing, tool-calling search, and a Postgres/Drizzle persistence layer.
- Stack: FE Next.js/React; BE Next.js route handlers; DB Postgres via Drizzle; Auth n/a-in-clone; Infra Docker/docker-compose, searxng-limiter.toml; notable: AGENTS.md/CLAUDE.md agent-instruction files present in repo root.
- Architecture: SSR/monolith Next.js app with tool-calling AI backend.
- Complexity: Production-like (real OSS project, not a toy).
- Educational material: STRONG — `fabledocs/` (53 files, flat top-level module layout unlike the `upskill/`-nested variant used elsewhere in this batch): 00-fast-track.md through 09-reference/ + README.md. Not deep-read beyond structure/README in this pass; layout matches the verified-high-quality template seen in nextcrm-app and umami (file:line-anchored, project-specific).
- Quality observations:
  - Ships `docker-compose.yaml` + `Dockerfile` — deployable clone, not just source dump.
  - Has both `docs/` (project's own) and `docs-codex-learning/` (a separate, non-Fable learning artifact) alongside `fabledocs/` — three doc trees coexist; worth reconciling before reuse.
  - `drizzle.config.ts` + `drizzle/` present — real migration-based ORM, good DB-migrations teaching material.
  - `instrumentation.ts` at root suggests observability wiring is present.
- Old-AI-generated smells: none seen (upstream clone, not LLM-authored source).
- Skill tags: fe-next, fe-react, be-node-express, db-postgres, db-migrations, orm, ai-llm-integration, docker
- Duplicate/overlap: none in this batch (only Morphic clone).
- Learning value: High — real production AI-search app with a matching file-anchored curriculum.
- Transformation opportunity: Reconcile the three doc trees (`docs/`, `docs-codex-learning/`, `fabledocs/`) into one canonical curriculum; could anchor an "AI product engineering" module in a broader course library.
- Interview stories it could support: explaining tool-calling/agentic search architecture; Drizzle migration workflow; Docker-compose multi-service local dev.
- Proposed disposition: B HIGH-VALUE — real, currently-relevant AI-app stack (LLM tool-calling + Postgres) with a full matching curriculum; keep as-is, dedupe docs trees before use.

## NextCRM clone + curriculum
- Path: `masternext\nextcrm-app` — Origin: OPEN-SOURCE CLONE (NextCRM) — Type: web app (monorepo-flavored single Next.js app)
- State: complete — Size: large clone (app/, actions/, components/, inngest/, emails/, i18n/) — Last modified: 2026-07-11
- Purpose: Open-source CRM covering accounts/contacts/leads/opportunities/contracts, invoicing, cold-email campaigns, AI-powered enrichment, and an MCP server exposing CRM tools to agents.
- Stack: FE Next.js 16/React 19/TS; BE Next.js route handlers + Inngest background jobs; DB Postgres via Prisma 7 (migrated off MongoDB — migration scripts kept in scripts/); Auth better-auth (Google OAuth + email OTP); Test Jest + Playwright E2E (`__tests__/`, `__mocks__/`, `jest.config.ts`); notable: MinIO/S3 storage, Resend email, next-intl, pgvector semantic search, OpenAI-agents enrichment.
- Architecture: modular monolith, Next.js App Router, background-job worker via Inngest.
- Complexity: Production-like.
- Educational material: EXCELLENT — `fabledocs/upskill/` (53 files, README + 00 through 09). Directly read README.md and `03-architecture-and-patterns/` listing: content is project-specific with exact file/line citations (e.g. "`lib/authz/` scope layer is the remediation" for a real published CVE `GHSA-mg5f-m89f-4gmc`), time-budgeted learning paths (weekend/2-week/8-week/interview-cram), and a dedicated architecture-critique doc. Quality: deep, project-specific, not generic. Preserve as-is.
- Quality observations:
  - Curriculum explicitly calls out a real historical security advisory (BOLA/IDOR) and points to the actual remediation code — strong authz teaching seam.
  - Serializable-transaction invoice numbering mentioned in README as a DB-transactions teaching point.
  - Has both Jest unit tests and Playwright E2E present in the clone (`__tests__/`, presumably `e2e`/playwright config not confirmed beyond top-level listing).
  - Three doc trees exist (`docs/`, `docs2/`, `docs3/`, plus `fabledocs/`) — same "multiple learning-pack passes" pattern as other repos in this batch; `docs2/docs3` are likely upstream project docs, not Fable-authored — needs verification before consolidation.
- Old-AI-generated smells: none seen in clone itself (upstream OSS).
- Skill tags: fe-next, fe-react, ts-types, be-node-express, be-async-jobs, authn, authz-rbac, db-postgres, db-transactions, db-migrations, orm, test-unit, test-e2e, ai-llm-integration, security-owasp
- Duplicate/overlap: none in this batch.
- Learning value: Very High — real CVE-backed authz story + Serializable invoice numbering + async job pipeline, all with file:line-anchored curriculum.
- Transformation opportunity: Use `08-interview-prep/07-two-week-cram-plan.md` and the authz remediation story directly as a mid-level interview prep module; strong flagship candidate for a "real security incident" teaching case study.
- Interview stories it could support: "found/fixed a real IDOR vulnerability", "migrated Mongo→Postgres/Prisma", "built Serializable-transaction invoice numbering to avoid duplicate invoice numbers under concurrency".
- Proposed disposition: A FLAGSHIP — production-grade CRM with a genuine security-advisory teaching hook and deep, verified curriculum; strongest single project in this batch alongside masteropen/mastertwenty's multi-pass packs.

## Novu clone (bare)
- Path: `masternovu\novu` — Origin: OPEN-SOURCE CLONE (Novu notification infrastructure) — Type: monorepo (apps/, libs/, packages/, enterprise/)
- State: working-looking (full upstream clone) — Size: large (Nx monorepo) — Last modified: 2026-06-09 (dir mtime, earliest/generic timestamp shared by all "bare" clones in this batch)
- Purpose: Open-source notification infrastructure (email/SMS/push/in-app) with a workflow builder.
- Stack: Nx + pnpm monorepo, biome, enterprise/ split-license packages (EE-PACKAGES-LICENSE), jest.
- Architecture: microservices-flavored monorepo (apps/ + libs/ + packages/ + playground/).
- Complexity: Production-like.
- Educational material: NONE — no `fabledocs*` or `upskill*` found anywhere under this tree.
- Quality observations:
  - Has `_templates/`, `domain-connect/`, `enterprise/` — real notification-infra complexity (queue-driven, multi-channel).
  - `skills-lock.json` present — Nx workspace metadata, not curriculum.
  - No evidence this clone was ever processed by the Astra/Fable curriculum pipeline (mtime identical to 3 other untouched clones in this batch).
- Old-AI-generated smells: none seen (untouched upstream clone).
- Skill tags: be-node-express, queues, arch-microservices, arch-event-driven, be-async-jobs
- Duplicate/overlap: none in batch; conceptually adjacent to masterpostiz (both event/notification-pipeline-shaped).
- Learning value: Medium — good raw material (queue-driven multi-channel notification system) but no curriculum has been generated yet.
- Proposed disposition: D REFERENCE — solid source for a future curriculum pass (queues/event-driven patterns) but currently just a raw clone; not worth promoting until curriculum work is done.

## OpenStatus clone + curriculum pack
- Path: `masteropen\openstatus` — Origin: OPEN-SOURCE CLONE (OpenStatus status-page/monitoring) — Type: monorepo(N apps)
- State: complete — Size: large (apps/, packages/, infra/) — Last modified: 2026-07-16
- Purpose: Status-page and uptime-monitoring platform with a distributed checker.
- Stack: FE Next.js/tRPC; BE Hono on Bun; checker in Go; DB Drizzle/libSQL; analytics Tinybird; Infra Docker Compose, Coolify deployment docs, devbox.
- Architecture: polyglot microservices-in-a-monorepo (Next/tRPC web, Hono/Bun API, Go checker service, Tinybird analytics pipeline).
- Complexity: Production-like / Senior-oriented (polyglot, quorum-based alerting).
- Educational material: EXCELLENT — four doc trees: `fabledocs/` (53 files, base curriculum), `fabledocs2/` (7 files, onboarding pack), `fabledocs3/` (12 files, reverse-engineered ADRs with interview translation), `fabledocs4/` (7 files, practice pack: fire drills, alerting capstone, SQL+Go labs, flashcards, 4-week plan). This is the deepest single curriculum in the batch (79 files across 4 passes). Also `docsclaude/` (separate, likely non-Fable) and a top-level `OPEN_SOURCE_UPSKILL_DOCS_MASTER_PROMPT.md` (the generation prompt itself, left in-repo).
- Quality observations:
  - Per-batch memory context confirms a specific, non-generic top teaching seam: a quorum-flip race condition and trigger-before-send at-most-once alerting bug — real distributed-systems teaching material, not boilerplate CRUD.
  - `CRITIQUE-codex-vs-claude.md` at root — an unusual artifact comparing two AI tools' output on this repo; interesting but not part of the curriculum proper.
  - Multiple deployment docs (`COOLIFY_*`, `DOCKER.md`) suggest this clone has real deploy documentation beyond the curriculum.
- Old-AI-generated smells: none seen in clone; the leftover `OPEN_SOURCE_UPSKILL_DOCS_MASTER_PROMPT.md` and `CRITIQUE-codex-vs-claude.md` are process artifacts that should probably be excluded/cleaned before repurposing this as a teaching asset.
- Skill tags: fe-next, be-node-express, be-rest-design, db-sqlite, db-concurrency, arch-microservices, arch-event-driven, queues, observability-metrics-tracing, incident-debugging, design-docs-adrs, docker, deploy
- Duplicate/overlap: none directly; polyglot-checker pattern is unique in this batch (only Go-language teaching material here besides none elsewhere).
- Learning value: Very High — genuine distributed-systems race condition + polyglot stack (Go+TS) + a 4-pass curriculum (base/onboarding/ADRs/practice) is the richest package in the batch.
- Transformation opportunity: Flagship "incident debugging" / "distributed systems" course — the quorum-flip race + at-most-once alerting bug can anchor a standalone "find the race condition" interview-prep module reusable across other courses.
- Interview stories it could support: diagnosing a quorum-flip race in a distributed alerting system; designing idempotent alert triggers; polyglot service boundary design (Go checker vs TS web).
- Proposed disposition: A FLAGSHIP — deepest, most senior-oriented curriculum + genuinely hard distributed-systems bug in the batch.

## Open edX Platform clone + curriculum
- Path: `masteropenedxPYJS\openedx-platform` — Origin: OPEN-SOURCE CLONE (Open edX) — Type: monolith (LMS + CMS)
- State: complete — Size: very large (lms/, cms/, common/, openedx/, themes/) — Last modified: 2026-06-09 (dir mtime; curriculum content itself not separately dated)
- Purpose: Full learning-management-system platform (course delivery, authoring/CMS, grading) powering edX-style MOOCs.
- Stack: BE Django (Python), test tox/pytest (tox.ini, conftest.py), FE jest.config.js for JS pieces, mypy for typing, pylint.
- Architecture: large modular Django monolith split into lms/ (learner-facing) and cms/ (authoring/Studio) apps.
- Complexity: Production-like / Senior-oriented (one of the largest, oldest open-source EdTech codebases).
- Educational material: STRONG — `docs/upskill/` (53-file structure: 00-fast-track through 08-reference/ + README, 9-module variant). Not deep-read this pass beyond directory structure; matches verified template quality seen elsewhere in batch.
- Quality observations:
  - Real CI config present (`codecov.yml`) and a Backstage `catalog-info.yaml` — production-grade repo hygiene.
  - `test_root/` — dedicated test fixture root, suggests substantial test infrastructure.
  - Curriculum lives under `docs/upskill/` (nested inside the project's own docs/) rather than a standalone `fabledocs/` — same generation family, different placement convention (shared with mastersaleorPY, masterzulipPY).
- Old-AI-generated smells: none seen (upstream clone).
- Skill tags: be-python, db-postgres (typical Open edX default), db-migrations, authn, authz-rbac, multitenancy, test-unit, test-integration, ci-cd, legacy-codebase-reading
- Duplicate/overlap: none in batch (only Django LMS).
- Learning value: High — huge, real legacy Django codebase; strong "legacy codebase reading" and Django-at-scale material.
- Interview stories it could support: navigating/reading an unfamiliar 10+ year old large Django monolith; explaining LMS/CMS domain modeling.
- Proposed disposition: B HIGH-VALUE — legitimate large legacy-codebase teaching asset with matching curriculum; not flagship only because content depth wasn't independently re-verified beyond structure.

## Paperless-ngx clone + curriculum
- Path: `masterpaper\paperless-ngx` — Origin: OPEN-SOURCE CLONE (Paperless-ngx) — Type: monorepo (Django API + Angular UI)
- State: complete — Size: large (src/, src-ui/) — Last modified: 2026-07-11
- Purpose: Self-hosted document-management/OCR archive system.
- Stack: BE Django + Celery (Python), FE Angular (src-ui/), pyproject.toml/uv.lock for deps.
- Architecture: modular monolith with async task queue (Celery) for OCR/consumption pipeline.
- Complexity: Production-like.
- Educational material: STRONG — `fabledocs/` (53 files, README + 00-09). Not re-read in depth this pass; per prior audit context the documented top teaching seams are a dedupe TOCTOU race and an SSRF-prone webhook transport — concrete, non-generic security/concurrency material.
- Quality observations:
  - `docsclaude/` present alongside `fabledocs/` — second, likely non-Fable doc tree; needs reconciliation.
  - Celery-based document consumption pipeline (OCR) is a strong async-jobs/queues teaching case.
  - `install-paperless-ngx.sh` at root — real deployment script, not just source.
- Old-AI-generated smells: none seen (upstream clone).
- Skill tags: be-python, be-async-jobs, queues, db-postgres, security-owasp, db-concurrency, fe-a11y (Angular UI), test-unit
- Duplicate/overlap: none in batch.
- Learning value: High — real dedupe-race + SSRF webhook bugs give concrete security/concurrency interview material.
- Interview stories it could support: fixing a TOCTOU dedupe race; hardening a webhook transport against SSRF.
- Proposed disposition: B HIGH-VALUE — solid async-pipeline + security teaching seams with full curriculum.

## Plane clone + curriculum
- Path: `masterplane\plane` — Origin: OPEN-SOURCE CLONE (Plane project-management) — Type: monorepo(N apps)
- State: complete — Size: large (apps/, packages/, deployments/) — Last modified: 2026-07-11
- Purpose: Linear/Jira-style project-management tool with real-time collaborative editing.
- Stack: BE Django/DRF + Celery; FE MobX-based SPAs; realtime Hocuspocus CRDT server; Infra Docker Compose (local + prod), pnpm/Turbo.
- Architecture: modular monolith backend + event-driven realtime collab layer (CRDT via Hocuspocus).
- Complexity: Production-like / Senior-oriented.
- Educational material: STRONG — `fabledocs/` (53 files, flat layout like mastermorphic). Per prior audit context, top seams are an advisory-lock sequencing issue, split authorization logic, and CSRF disabled somewhere in the stack — concrete security/concurrency findings, not generic advice.
- Quality observations:
  - Hocuspocus/CRDT realtime editing is a genuinely advanced teaching topic (conflict-free collaborative editing), rare in this batch.
  - CSRF-disabled finding is a real, citable security smell for an OWASP-focused lesson.
  - `AGENTS.md` + `COPYRIGHT_CHECK.md` present — repo has agent-facing instructions and licensing tooling.
- Old-AI-generated smells: none seen (upstream clone).
- Skill tags: be-python, db-postgres, db-concurrency, realtime-ws, authz-rbac, security-owasp, arch-event-driven, queues, docker
- Duplicate/overlap: conceptually adjacent to mastertea (Teable) which also has a CRDT/ShareDB realtime layer — both good for a "realtime collaborative editing" comparison module.
- Learning value: Very High — CRDT realtime collaboration + concrete authz/CSRF findings.
- Transformation opportunity: Could anchor a "building realtime collaborative editors" module alongside Teable's ShareDB approach for a compare/contrast CRDT vs OT lesson.
- Interview stories it could support: reasoning about advisory-lock ordering bugs; explaining CRDT vs OT tradeoffs; split-authorization-logic cleanup.
- Proposed disposition: B HIGH-VALUE — advanced realtime-collab content, strong pairing candidate with Teable.

## Payload CMS clone + curriculum
- Path: `masterpload\payload` — Origin: OPEN-SOURCE CLONE (Payload CMS) — Type: monorepo(N apps)
- State: complete — Size: large (packages/, templates/, examples/, test/) — Last modified: 2026-07-11
- Purpose: Headless CMS/application framework (core + admin UI + Next.js integration) with pluggable DB adapters.
- Stack: FE/BE Next.js (App Router, RSC-based admin UI); TS core; multi-adapter DB layer (`payload.db` present, 5 supported adapters per prior context); Infra Sentry client/server config, release-please config.
- Architecture: modular monolith (core + ui(RSC) + Next.js adapter) over a pluggable persistence contract.
- Complexity: Production-like / Senior-oriented.
- Educational material: STRONG — `fabledocs/` (53 files). Per prior audit context, concrete bugs identified: a `handleEndpoints` fallbackLocale bug, an email-send-inside-transaction issue, and a fail-open jobs-run fallback — real, specific findings, plus documented strengths (access-as-query pattern, `safeFetch` SSRF guard).
- Quality observations:
  - Two extra doc trees (`docs2/`, `docs3/`) alongside `fabledocs/` — same multi-pass pattern as other repos, needs dedup check.
  - Real Sentry instrumentation (`sentry.client.config.ts`/`sentry.server.config.ts`) — good observability teaching material.
  - `test/` directory present at root — substantial test suite in the clone.
- Old-AI-generated smells: none seen (upstream clone).
- Skill tags: fe-next, be-node-express, be-async-jobs, db-postgres (one of several adapters), orm, security-owasp, observability-logs, test-integration
- Duplicate/overlap: none in batch.
- Learning value: High — real transactional-email-in-transaction bug and fail-open job fallback are strong "things that look fine but aren't" interview material.
- Interview stories it could support: explaining why sending email inside a DB transaction is risky; auditing a "fail-open" background job fallback for silent data loss.
- Proposed disposition: B HIGH-VALUE — concrete, specific bugs (not generic) with full curriculum.

## Postiz clone + curriculum
- Path: `masterpostiz\postiz-app` — Origin: OPEN-SOURCE CLONE (Postiz social-media scheduler) — Type: monorepo(N apps)
- State: complete — Size: large (apps/, libraries/, dynamicconfig/) — Last modified: 2026-07-10
- Purpose: Social-media post scheduling/management platform across multiple channels.
- Stack: BE NestJS + Temporal (workflow engine); FE Next.js 16; Test Jest; Infra Jenkins, SonarQube (sonar-project.properties), Docker Compose (dev variant).
- Architecture: modular monolith with a durable-workflow engine (Temporal) for scheduled/multi-step publishing jobs.
- Complexity: Production-like.
- Educational material: STRONG — `fabledocs/` (53 files). Per prior audit context, top seams: plaintext OAuth tokens at rest and an `editTag` IDOR — concrete, citable security findings.
- Quality observations:
  - Temporal usage is a genuinely advanced durable-workflow teaching topic, uncommon in this batch.
  - Plaintext OAuth token storage is a strong, realistic "secrets/config" security lesson (social-media integrations hold real user credentials).
  - Jenkins + SonarQube config present — real CI/quality-gate tooling, useful for a ci-cd teaching angle even without git history.
- Old-AI-generated smells: none seen (upstream clone).
- Skill tags: be-nest, arch-event-driven, queues, security-owasp, config-secrets, authz-rbac, ci-cd, fe-next
- Duplicate/overlap: none in batch (only Temporal-based project).
- Learning value: High — Temporal durable workflows + concrete IDOR/plaintext-token findings.
- Interview stories it could support: designing durable multi-step publish workflows; explaining IDOR on a tag-edit endpoint; why storing OAuth tokens in plaintext is a real, common mistake.
- Proposed disposition: B HIGH-VALUE — unique durable-workflow (Temporal) content plus concrete security findings.

## pretalx clone + curriculum
- Path: `masterpre\pretalx` — Origin: OPEN-SOURCE CLONE (pretalx conference/CfP management) — Type: monolith (Django app)
- State: complete — Size: large (src/) — Last modified: 2026-07-11
- Purpose: Conference talk submission, review, and scheduling platform.
- Stack: BE Django 6, Celery, django-scopes (tenant scoping); Docs Sphinx (`doc/`, `_build/`).
- Architecture: modular monolith with tenant-scoped querysets via django-scopes.
- Complexity: Production-like.
- Educational material: STRONG — `fabledocs/` (53 files). Per prior audit context, top seams: `freeze_schedule` race condition and a `send_draft` double-send bug — concrete concurrency/idempotency findings.
- Quality observations:
  - `django-scopes` tenant isolation pattern is a strong multitenancy teaching case, one of few in this batch besides Open edX/Zulip/Saleor.
  - `docsclaude/` present alongside `fabledocs/` (same dual-tree pattern seen elsewhere) — needs reconciliation.
  - No git commits (confirmed) — matches prior audit note that this repo has no git history at all, not just no commits in this snapshot.
- Old-AI-generated smells: none seen (upstream clone).
- Skill tags: be-python, multitenancy, db-concurrency, idempotency, be-async-jobs, queues, arch-modular-monolith
- Duplicate/overlap: none in batch.
- Learning value: High — concrete race condition + double-send bug, real multitenancy pattern (django-scopes).
- Interview stories it could support: fixing a schedule-freeze race condition; preventing double-send in an email/notification path; explaining scoped-queryset multitenancy.
- Proposed disposition: B HIGH-VALUE — concrete concurrency/idempotency findings, solid multitenancy teaching case.

## RN CRUD app (Astra review sample)
- Path: `masterrnative` — Origin: ORIGINAL (Fable-built, farm-management CRUD app) — Type: mobile app (Expo/React Native)
- State: complete/working-looking — Size: ~49 TS/TSX source files under `src/`, 7 test files under `tests/` — Last modified: astraupskill content authored recently; app itself undated beyond dir listing
- Purpose: Pig-farm operations app — batch lifecycle, feed cost allocation, transactions, break-even analysis, CSV export/import, backup/restore, dashboards with charts.
- Stack: FE Expo 54 / React Native 0.81 / React 19, React Navigation, react-hook-form + zod validation, AsyncStorage persistence, react-native-chart-kit; Test Node's built-in `node --test` + Playwright (`@playwright/test` in devDeps); TS throughout.
- Architecture: single-tier mobile app with a Context-based in-memory/AsyncStorage data layer (`AppDataContext.tsx`) — no backend/API.
- Complexity: Junior/Junior+ (17 feature docs under `docs/features/` describe fairly involved CRUD+reporting features for a client-only app).
- Educational material: USEFUL but narrow — `astraupskill/` (12 files: 01-CODEBASE-MAP through 07-TRACE-LAB, README, VERIFICATION, evidence/, snapshots/). This is NOT a full course; it documents one specific staged bug-fix (a `map`-based update silently no-op'ing on missing IDs, replaced with an explicit `replaceRecordById` helper that throws on missing-id) as a single worked "change + review" exercise, matching the "Fable review + fix pass of Astra improvements" pattern already recorded in memory (fablereview-astra-audit.md). Preserve as a worked example, not a full curriculum.
- Quality observations:
  - `docs/features/` (17 numbered feature-spec files) is separate from `astraupskill/` and documents real, specific functionality (feed cost allocation, break-even analysis, backup validation) — good evidence this is a genuinely built app, not a stub.
  - The worked-change README is explicit about scope limits ("does not add a database, change AsyncStorage formats... package dependencies and the TypeScript compiler are absent in this staged environment") — honest about what wasn't verified, a good practice example itself.
  - `evidence/` contains `results.json` and a runtime log (`crud-b03-astra-runtime.log`) — the fix claim is backed by an actual captured run, not just narrative.
  - Uses zod + react-hook-form for validation — decent forms-validation teaching material for a junior-level RN app.
- Old-AI-generated smells: none seen; explicitly disclaims environment limitations rather than overclaiming.
- Skill tags: fe-forms-validation, ts-types, mobile-rn, test-unit, db-sqlite (AsyncStorage-analog), crud-basic, code-review
- Duplicate/overlap: none in batch; part of the broader Astra fleet-review effort already tracked in memory across other batches.
- Learning value: Medium — good as a small, focused "before/after with tests" case study on identity validation before async side effects, not a broad curriculum.
- Interview stories it could support: "found a silent no-op bug where an update on a missing ID looked successful but wrote nothing" — a clean, small STAR story.
- Proposed disposition: C SPECIALIZED — narrow but well-evidenced single-bug teaching artifact; useful as one exercise in a "spot the silent failure" module, not a flagship.

## Saleor clone + curriculum
- Path: `mastersaleorPY\saleor` — Origin: OPEN-SOURCE CLONE (Saleor commerce platform) — Type: monolith/API (GraphQL-first e-commerce)
- State: complete — Size: large (`saleor/` app package, `deployment/`) — Last modified: 2026-06-09 (dir mtime)
- Purpose: Headless, GraphQL-native e-commerce backend (orders, checkout, payments, catalog).
- Stack: BE Django + Graphene (GraphQL), Postgres, `uv.lock`/pyproject.toml for deps; `AGENTS.md`/`CLAUDE.md` present at root.
- Architecture: modular monolith exposed entirely through a GraphQL API layer.
- Complexity: Production-like / Senior-oriented (GraphQL schema design at scale, checkout/payment domain).
- Educational material: STRONG — `docs/upskill/` (53-file, 9-module structure: 00-fast-track through 08-reference + README), same placement convention as Open edX/Zulip. Not deep-read this pass beyond structure.
- Quality observations:
  - GraphQL-first architecture (via Graphene) makes this the only strong `be-graphql-trpc` teaching source in the batch.
  - Checkout/payment domain (real e-commerce complexity: multi-currency, payment gateways, tax) is senior-oriented material.
  - `AGENTS.md`/`CLAUDE.md` present — repo already has agent-facing operating instructions, suggesting active agentic tooling use on this clone.
- Old-AI-generated smells: none seen (upstream clone).
- Skill tags: be-python, be-graphql-trpc, db-postgres, db-transactions, be-validation, authz-rbac
- Duplicate/overlap: conceptually adjacent to MasterStore\storefront (both e-commerce-domain, though storefront targets a different backend — Spree — not Saleor); worth a compare/contrast note if both are used in the same course track.
- Learning value: High — GraphQL API design + payment/checkout domain complexity, unique in this batch.
- Interview stories it could support: designing a GraphQL schema for a checkout flow; explaining idempotent payment processing.
- Proposed disposition: B HIGH-VALUE — only strong GraphQL/e-commerce-backend teaching source in the batch.

## shadcn/ui clone + curriculum
- Path: `mastershadcn\ui` — Origin: OPEN-SOURCE CLONE (shadcn/ui) — Type: monorepo(N apps: CLI + docs site + registry packages)
- State: complete — Size: large (apps/, packages/, templates/, skills/) — Last modified: 2026-07-11
- Purpose: Component-registry CLI and copy-paste component library/design-system tooling (not a runtime app — a build-time/dev-tool product).
- Stack: FE React components, Vite/Turbo monorepo, Vitest (`vitest.config.ts`, `vitest.workspace.ts`).
- Architecture: monorepo of a CLI tool + component registry + docs site.
- Complexity: Mid/Mid+ (CLI/tooling-focused rather than a typical CRUD web app — different shape than most of this batch).
- Educational material: STRONG — `fabledocs/` (53 files). Not deep-read this pass; template matches verified quality elsewhere.
- Quality observations:
  - Distinctive `skills/` top-level directory (not verified in depth — worth checking whether this is shadcn's own "skills" concept or something curriculum-related).
  - CLI-tooling domain (registry resolution, component scaffolding) is a good complement to the mostly-CRUD-app shape of the rest of the batch.
  - Uses Vitest workspace config — multi-package test orchestration is a decent testing-architecture teaching point.
- Old-AI-generated smells: none seen (upstream clone).
- Skill tags: fe-react, ts-types, test-unit, arch-modular-monolith (as applied to a CLI/registry tool)
- Duplicate/overlap: none in batch (only CLI/design-system-tooling project).
- Learning value: Medium-High — different domain shape (dev-tooling vs CRUD app) is valuable for variety even if less "enterprise backend" than others.
- Interview stories it could support: explaining CLI tool architecture and component-registry resolution.
- Proposed disposition: B HIGH-VALUE — useful for stack variety (tooling/CLI vs the batch's dominant CRUD-monolith shape).

## Spree storefront app + learning docs (MasterStore)
- Path: `MasterStore\storefront` (app) + `MasterStore\astraupskill` (separate Astra review pack, same 12-file structure as masterrnative's) — Origin: ORIGINAL (Fable-built Next.js storefront consuming the Spree commerce API) — Type: web app (Next.js e-commerce storefront)
- State: complete/working-looking — Size: 195 TS/TSX files under `src/`, only 2 files under `tests/` (test coverage appears thin relative to app size) — Last modified: 2026-09-21 (by far the most recent mtime in this batch)
- Purpose: Customer-facing multi-market, multi-locale e-commerce storefront built on `@spree/sdk`, with payments via Stripe, Adyen, and PayPal.
- Stack: FE Next.js 16 (App Router, Turbopack), react-compiler babel plugin, next-intl (i18n across en/de/pl locales), biome (lint/format), Sentry, Vercel Analytics/Speed Insights; Test Vitest (`vitest.config.ts`); notable `check:locales` script for i18n parity checking.
- Architecture: SSR/App-Router monolith consuming an external headless-commerce API (Spree) as its backend, with layered providers (Store → Auth → Cart context).
- Complexity: Mid/Mid+ (multi-payment-provider, multi-market/locale storefront — realistic e-commerce frontend complexity).
- Educational material: STRONG — `docs/` inside storefront has three distinct packs: `mission-learning-path/` (6 files: tiered "missions" — read the actual README excerpt: Mission 1 "The App's Heartbeat" cites exact `package.json:5-14`, `src/app/layout.tsx:37-62` line ranges with real code excerpts and inline comments explaining intent), `architectural-cartographer/` (7 files), `user-story-build-path/` (2 files), plus a separate `feature-expansion-plan.md`. This is a different (but comparably high-quality) curriculum template than the `fabledocs` 53-file family used elsewhere in the batch — it uses a "mission" framing with time estimates, analogy-based concept explanations, and exact line-range code citations. Separately, `MasterStore\astraupskill` (12 files, same structure as masterrnative) documents one Astra-fleet worked bug-fix, not a course. Preserve both.
- Quality observations:
  - Test coverage looks thin: only 2 files under `tests/` for 195 source files, though there's also a `src/__tests__/` directory not yet counted — worth deeper verification before assuming good coverage.
  - Real multi-payment-provider integration (Stripe + Adyen + PayPal) in one app is unusually broad payment-domain surface for a portfolio project.
  - i18n parity is enforced via a dedicated `check:locales` script — a good example of guarding against silent i18n drift.
  - `proxy.ts` at `src/` root plus `instrumentation.ts`/`instrumentation-client.ts` suggest deliberate middleware/observability wiring, not default scaffolding.
- Old-AI-generated smells: none confirmed; thin test-to-source ratio (2 files in `tests/` vs 195 in `src/`) is worth flagging as NEEDS DEEPER INSPECTION — could be that most tests live under `src/__tests__/` instead (seen in listing but not counted).
- Skill tags: fe-next, fe-react, ts-types, fe-forms-validation, config-secrets (payment provider keys), test-unit, observability-logs, ai-llm-integration (not confirmed — no evidence found; omit if verifying)
- Duplicate/overlap: conceptually adjacent to mastersaleorPY (both e-commerce, different backend integration target — Spree vs Saleor GraphQL).
- Learning value: High — most recently touched project in the batch, real multi-payment-provider + i18n storefront with a distinctive "mission"-style curriculum.
- Transformation opportunity: The mission-learning-path's analogy-driven, line-range-cited teaching style is worth studying as an alternate curriculum template to the standard 53-file `fabledocs` family — could inform future curriculum generation.
- Interview stories it could support: integrating multiple payment providers behind one checkout flow; enforcing i18n locale parity in CI; explaining state-ownership decisions (Spree vs cookies vs React Context vs URL) as documented in Mission 9.
- Proposed disposition: B HIGH-VALUE — freshest project in the batch, genuine multi-payment/i18n complexity, and a distinctive high-quality curriculum worth preserving; verify actual test coverage before treating it as production-like.

## Supabase clone (bare)
- Path: `mastersupa\supabase` — Origin: OPEN-SOURCE CLONE (Supabase) — Type: monorepo(N apps)
- State: working-looking (full upstream clone) — Size: very large (apps/, packages/, blocks/, examples/, e2e/) — Last modified: 2026-06-09 (dir mtime)
- Purpose: Open-source Firebase alternative — Postgres + Auth + Realtime + Storage + Edge Functions platform and dashboard.
- Stack: pnpm/Turbo monorepo, i18n/, docker/, `supa-mdx-lint` custom tooling.
- Architecture: microservices/platform monorepo (studio dashboard + docs + multiple backend services).
- Complexity: Production-like / Senior-oriented.
- Educational material: NONE — no `fabledocs*`/`upskill*` anywhere under this tree.
- Quality observations:
  - `e2e/` directory present at root — real end-to-end test infra in the clone.
  - `blocks/` and `docs-codex-learning/` present — the latter is a non-Fable learning artifact (same pattern as seen in mastermorphic) that could be mined before writing a curriculum.
  - This is one of the largest, most architecturally rich codebases in the batch and currently has zero generated curriculum — a notable gap.
- Old-AI-generated smells: none seen (upstream clone).
- Skill tags: db-postgres, authn, realtime-ws, arch-microservices, db-migrations, cloud-aws (self-host/cloud deploy docs typically present)
- Duplicate/overlap: none in batch.
- Learning value: Medium (as-is, no curriculum) but High potential — Postgres+Auth+Realtime+Storage platform is excellent raw material.
- Proposed disposition: D REFERENCE — notable gap; flag for a future curriculum pass given its high potential value (this is genuinely one of the more instructive stacks in the batch if a curriculum were generated).

## Teable clone + curriculum
- Path: `mastertea\teable` — Origin: OPEN-SOURCE CLONE (Teable, Airtable-style spreadsheet-database) — Type: monorepo(N apps)
- State: complete — Size: large (apps/, packages/, plugins/, dottea/) — Last modified: 2026-07-11
- Purpose: Airtable-like no-code database/spreadsheet hybrid with real-time collaborative editing.
- Stack: BE NestJS + dual-Prisma; FE Next.js (pages router); Realtime ShareDB (OT-based collab); pnpm monorepo.
- Architecture: v2 hexagonal rewrite behind canary flags (per prior audit context) — layered/clean architecture in transition alongside legacy code.
- Complexity: Production-like / Senior-oriented.
- Educational material: STRONG — `fabledocs/` (53 files). Per prior audit context, top seams: a split-brain dynamic-DDL data model, a computed-field transactional outbox pattern, and a share-projection leak (labeled R7) — concrete, specific findings including an outbox-pattern teaching case.
- Quality observations:
  - The hexagonal-rewrite-in-progress (v2 behind canary flags) is a rare "watch an architecture migration happen live" teaching case, uncommon across this batch.
  - Outbox pattern usage (computed-field transactional outbox) is directly relevant to the `outbox` skill tag — one of few repos in the batch demonstrating it concretely.
  - Dual-Prisma setup (likely one schema per bounded context or old/new schema during migration) is worth verifying as a db-migrations teaching point.
- Old-AI-generated smells: none seen (upstream clone).
- Skill tags: be-nest, db-postgres, db-migrations, outbox, realtime-ws, arch-clean-hex, orm, security-owasp (share-projection leak)
- Duplicate/overlap: conceptually adjacent to masterplane (Plane) — both have realtime CRDT/OT collaborative editing; good compare/contrast pair (Teable=ShareDB/OT, Plane=Hocuspocus/CRDT).
- Learning value: Very High — outbox pattern + live hexagonal migration + a labeled security leak (R7) make this one of the most architecturally interesting repos in the batch.
- Transformation opportunity: Pair with Plane for a "realtime collaboration: OT vs CRDT" comparison module; use the hexagonal-migration-in-progress as a live "reading an architecture migration" exercise.
- Interview stories it could support: explaining outbox pattern for computed fields; diagnosing a share-projection data leak; navigating a codebase mid-migration to hexagonal architecture.
- Proposed disposition: A FLAGSHIP — outbox pattern + live architecture migration + realtime OT collaboration is unusually rich, specific teaching material.

## ToolJet clone (bare)
- Path: `mastertool\tooljet` — Origin: OPEN-SOURCE CLONE (ToolJet low-code internal-tools builder) — Type: monorepo (frontend + server + plugins)
- State: working-looking (full upstream clone) — Size: large (frontend/, server/, plugins/, marketplace/, cli/) — Last modified: 2026-06-09 (dir mtime)
- Purpose: Low-code/AI-native platform for building internal tools, workflows, and drag-and-drop UIs connected to databases/APIs/SaaS apps.
- Stack: React frontend, server (Node/Rails-style structure not confirmed), plugins/ marketplace architecture, Cypress (`cypress-tests/`), Terraform (`terraform/`), Docker.
- Architecture: plugin-based platform (core + marketplace plugins) with a visual query/app builder.
- Complexity: Production-like.
- Educational material: NONE — no `fabledocs*`/`upskill*` found.
- Quality observations:
  - `terraform/` present — real infra-as-code, unusual and valuable in this batch (most other clones don't ship IaC).
  - `cypress-tests/` — real E2E test suite present.
  - Plugin/marketplace architecture (extensible connector system) is a good `arch-modular-monolith`/plugin-pattern teaching case, currently unexploited (no curriculum).
- Old-AI-generated smells: none seen (upstream clone).
- Skill tags: fe-react, be-node-express, test-e2e, deploy, cloud-aws (terraform likely targets AWS/generic cloud)
- Duplicate/overlap: none in batch.
- Learning value: Medium (no curriculum yet) but the Terraform + plugin-architecture combination is genuinely differentiated raw material.
- Proposed disposition: D REFERENCE — good candidate for a future curriculum pass, particularly for IaC/deploy content which is thin elsewhere in this batch.

## Twenty CRM clone + curriculum pack
- Path: `mastertwenty\twenty` — Origin: OPEN-SOURCE CLONE (Twenty, open-source Salesforce/CRM alternative) — Type: monorepo(N apps)
- State: complete — Size: large (packages/) — Last modified: 2026-07-16
- Purpose: Open-source, extensible CRM with a metadata-driven object system.
- Stack: Nx/Yarn monorepo, Next/React frontend, NestJS-style backend (per package structure).
- Architecture: modular monorepo, metadata-driven object/field system (common in modern CRM platforms).
- Complexity: Production-like / Senior-oriented.
- Educational material: EXCELLENT — four doc trees like masteropen: `fabledocs/` (53 files, base), `fabledocs2/` (7 files, onboarding pack), `fabledocs3/` (12 files, reverse-engineered ADRs w/ interview translation), `fabledocs4/` (7 files, practice pack: fire drills, outbox capstone, front/SQL labs, flashcards, 4-week plan) — 79 files total, the same depth as masteropen.
- Quality observations:
  - Per prior audit context, top seams are "at-most-once webhooks" and a "missing outbox" — directly matches the `outbox`/`idempotency` skill tags and pairs well with mastertea's outbox-pattern content for a compare/contrast (Twenty lacks one, Teable has one, mid-migration).
  - No git commits confirmed; per prior context, commands used in the curriculum were inferred rather than run.
  - `fabledocs4` practice pack explicitly includes a 4-week study plan and flashcards — directly reusable interview-prep material.
- Old-AI-generated smells: none seen (upstream clone).
- Skill tags: be-nest, fe-next, fe-react, outbox, idempotency, be-async-jobs, db-postgres, db-modeling, design-docs-adrs
- Duplicate/overlap: conceptually pairs with masternext (NextCRM) as a second, differently-architected open-source CRM in this batch — good compare/contrast ("metadata-driven object system" vs "fixed-schema Prisma CRM").
- Learning value: Very High — missing-outbox/at-most-once-webhook finding is a clean, concrete "spot the reliability gap" teaching case, backed by the deepest curriculum pack in the batch (tied with masteropen).
- Transformation opportunity: Pair with masternext for a "two CRMs, two architectures" comparative module; use the missing-outbox finding as a hands-on "add the outbox pattern" exercise contrasted with Teable's implemented version.
- Interview stories it could support: explaining why missing outbox pattern causes at-most-once delivery gaps for webhooks; comparing metadata-driven vs fixed-schema CRM data modeling.
- Proposed disposition: A FLAGSHIP — tied for deepest curriculum pack in the batch, concrete reliability-gap finding, strong pairing potential with NextCRM and Teable.

## Typebot clone (bare)
- Path: `mastertypebot\typebot.io` — Origin: OPEN-SOURCE CLONE (Typebot conversational-form/chatbot builder) — Type: monorepo(N apps)
- State: working-looking (full upstream clone) — Size: large (apps/, packages/, opensrc/, plans/) — Last modified: 2026-06-09 (dir mtime)
- Purpose: Drag-and-drop conversational form/chatbot builder with embeddable runtime.
- Stack: Nx monorepo, Next.js, Bun (`bun.lock`, `bunfig.toml`), Docker Compose (build/dev variants).
- Architecture: monorepo builder-app + embeddable runtime + backend API.
- Complexity: Production-like.
- Educational material: NONE — no `fabledocs*`/`upskill*` found; has `docs3/`, `docs4/`, `docs-test/` (likely upstream project docs plus test fixtures, not Fable curriculum).
- Quality observations:
  - Embeddable-widget + builder split architecture is a distinct shape from the rest of the batch (most are single monolithic web apps) — good variety if curriculum were built.
  - `plans/` directory at root — possibly product/roadmap docs, not verified.
  - No curriculum despite otherwise similar mtime/clone pattern to the other three "bare" clones (novu, supabase, tooljet) — consistent with those four never having gone through the curriculum-generation pass.
- Old-AI-generated smells: none seen (upstream clone).
- Skill tags: fe-react, fe-next, be-node-express, docker
- Duplicate/overlap: none in batch.
- Learning value: Medium (no curriculum yet); builder+embeddable-runtime split is a decent architecture teaching case if developed.
- Proposed disposition: D REFERENCE — untapped, good candidate for a future curriculum pass; embeddable-widget architecture is under-represented in this batch's existing curricula.

## Umami clone + curriculum
- Path: `masterumami\umami` — Origin: OPEN-SOURCE CLONE (Umami web analytics) — Type: web app (monorepo-flavored single Next.js app)
- State: complete — Size: large (src/, prisma/, db/) — Last modified: 2026-07-11
- Purpose: Privacy-focused, self-hosted web-analytics platform (pageview/event tracking, dashboards).
- Stack: FE Next.js; BE Next.js API routes; DB Prisma over Postgres or ClickHouse; Test Cypress; vanilla-JS tracker script (rollup-built, `rollup.tracker.config.js`).
- Architecture: SSR monolith + ingestion pipeline for high-volume event tracking, dual-DB support (relational vs columnar).
- Complexity: Production-like.
- Educational material: STRONG — `fabledocs/upskill/` (53 files). Directly read `06-contribution-practice/01-good-first-tickets.md`: content is concrete and verifiable — e.g. Ticket 1 asks the learner to unit-test `hasBlockedIp` CIDR matching at `src/lib/detect.ts:140-170`, gives exact acceptance criteria, a "what could go wrong" hint (`ipaddr.parse` throwing on malformed input), and an interview-story framing. This confirms the same high, project-specific quality bar as nextcrm-app and the zulip sample.
- Quality observations:
  - Per prior audit context, top seams: fire-and-forget Kafka silent-loss, a per-handler IDOR, a latent `orderBy` injection, and cookieless hashed identity — a strong cluster of concrete security/reliability findings.
  - Dual-DB support (Postgres vs ClickHouse) is a good db-choice/tradeoffs teaching point, relatively rare in this batch.
  - Cypress E2E present (`cypress.config.ts`, `cypress/`).
- Old-AI-generated smells: none seen (upstream clone); the curriculum ticket read is itself a model of specificity (exact env vars, exact test assertions, exact file/line).
- Skill tags: fe-next, be-node-express, db-postgres, db-sql-raw, security-owasp, test-unit, test-e2e, observability-metrics-tracing (analytics domain)
- Duplicate/overlap: none in batch (only web-analytics project).
- Learning value: Very High — a cluster of four distinct, concrete security/reliability findings (Kafka silent-loss, IDOR, orderBy injection, cookieless identity) plus directly-verified high curriculum quality.
- Interview stories it could support: diagnosing silent event loss in a fire-and-forget Kafka producer; finding and fixing an `orderBy` SQL injection; explaining cookieless identity hashing for privacy-focused analytics.
- Proposed disposition: A FLAGSHIP — directly-verified excellent curriculum quality plus a rich cluster of concrete, specific security findings (SQL injection, IDOR, silent data loss).

## Zulip clone + curriculum
- Path: `masterzulipPY\zulip` — Origin: OPEN-SOURCE CLONE (Zulip team chat) — Type: monolith (Django backend + web frontend)
- State: complete — Size: very large (zerver/, web/, analytics/, corporate/, confirmation/) — Last modified: 2026-06-09 (dir mtime)
- Purpose: Topic-threaded team chat application (email/chat hybrid).
- Stack: BE Django (`zerver/`), Python, Postgres (typical Zulip default) + pgroonga (full-text search, `pgroonga/` dir present); FE TS/JS (`web/`), stylelint; Infra puppet manifests, Docker (postgresql Dockerfile).
- Architecture: large Django monolith with a real-time event system (`server_events.js`, `events_register.py`) for pushing chat updates to clients.
- Complexity: Production-like / Senior-oriented (one of the largest, most mature codebases in the batch).
- Educational material: STRONG — `docs/upskill/` (53-file, 9-module structure). Directly read `04-code-reading-gym/01-annotation-drills.md`: five drills each cite exact file:line-range excerpts (`zerver/views/message_send.py:105-244`, `web/src/compose.ts:185-236`, `zerver/views/events_register.py:65-132`) with specific analytical prompts (e.g. "mark spectator-only versus authenticated-user behavior") — confirms the same rigorous, project-specific quality bar seen elsewhere.
- Quality observations:
  - Real-time event distribution system (`server_events.js`/`events_register.py`) is a strong `realtime-ws`/event-driven teaching case with exact citations already provided by the curriculum.
  - `pgroonga` full-text search extension usage is a distinctive Postgres-extension teaching point, unique in this batch.
  - Large, mature, well-organized monolith (separate `analytics/`, `corporate/`, `confirmation/` apps within one Django project) is excellent "legacy codebase reading" material.
- Old-AI-generated smells: none seen (upstream clone); curriculum content directly verified as specific and non-generic.
- Skill tags: be-python, realtime-ws, arch-event-driven, db-postgres, db-indexes-perf (pgroonga/full-text search), legacy-codebase-reading, code-review
- Duplicate/overlap: none in batch (only real-time chat application); loosely thematically adjacent to masternovu (Novu, notification infra) but different domain.
- Learning value: Very High — directly-verified excellent curriculum quality on one of the largest, most architecturally mature codebases in the batch.
- Interview stories it could support: explaining how a real-time event-distribution system partitions and orders events for clients; reading and annotating an unfamiliar 100k+-line Django codebase under time pressure.
- Proposed disposition: A FLAGSHIP — directly-verified excellent, specific curriculum on a large, mature, real-time-architecture codebase.

## Batch observations
- **No git history anywhere in this batch.** Every one of the 21 project roots reports "does not have any commits yet" — these are all working-tree snapshots/clones dropped into place, not committed repos. All dates in this report are directory mtimes, which cluster into two groups: a generic bulk-clone timestamp (`2026-06-09 15:13:xx`, shared by novu, openedx-platform, saleor, supabase, tooljet, typebot.io, zulip) versus later, curriculum-authoring-pass timestamps (`2026-07-10` through `2026-07-16`, shared by every project that actually got a `fabledocs`/`docs/upskill` pass). This strongly suggests a two-phase pipeline: bulk-clone first, curriculum-generation second, and four repos (novu, supabase, tooljet, typebot.io) never received the second pass — a clean, actionable gap list.
- **One dominant curriculum template, two placement conventions.** All curriculum-bearing clones use the identical 53-file "00-fast-track → 09-reference" structure (or an 8-module "…→08-reference" variant for openedx-platform/saleor/zulip). Placement varies: `fabledocs/` (or `fabledocs/upskill/`) at repo root for most, versus `docs/upskill/` nested inside the project's own `docs/` for the three Python/Django repos placed differently (openedx-platform, saleor, zulip) — worth normalizing if these get consolidated into one course library.
- **Two projects (masteropen/openstatus, mastertwenty/twenty) got a deeper 4-pass treatment** (`fabledocs` + `fabledocs2` onboarding + `fabledocs3` ADRs + `fabledocs4` practice pack, ~79 files each) — these are the two strongest, most senior-oriented, and should be treated as the batch's flagships alongside NextCRM, Teable, Umami, and Zulip (whose curriculum content was directly spot-verified in this pass).
- **Duplicate/leftover doc trees are common and need reconciliation before reuse.** Several repos carry a second, apparently non-Fable doc tree alongside the curriculum: `docs-codex-learning/` (mastermorphic, mastersupa), `docsclaude/` (masteropen, masteropenedxPYJS, masterpaper, masterpre), and plain numbered `docs2/docs3` (masternext, masterpload, mastertool via other repos in this family, mastertypebot). None of these were confirmed as Fable-authored — flag for exclusion or separate review before treating this batch's total file counts as curriculum-only.
- **Two original (non-clone) projects hide inside this "clone" batch**: `masterrnative` (Expo farm-management CRUD app) and `MasterStore\storefront` (Next.js Spree e-commerce storefront) — both were built by Fable directly, not cloned from an open-source repo, and both additionally carry a small (12-file) "Astra fleet review" worked-bugfix pack (`astraupskill/`) rather than a full curriculum — this matches the `fablereview-astra-audit.md` effort already tracked in memory. `MasterStore\storefront` also has its own distinct "mission-learning-path" curriculum style, different from the 53-file `fabledocs` template used everywhere else — worth comparing the two templates for quality/reuse.
- **Recurring, specific security/reliability findings cluster around concurrency and trust boundaries**, not generic advice: SQL injection via `orderBy` (Umami), IDOR/BOLA with a real CVE (NextCRM), plaintext OAuth tokens (Postiz), CSRF disabled (Plane), SSRF webhook transport (Paperless-ngx), advisory-lock/TOCTOU races (Plane, Paperless-ngx, pretalx), missing/partial outbox patterns and at-most-once delivery gaps (Twenty, Teable). This cluster is unusually strong material for an OWASP/`security-owasp` + `db-concurrency` + `idempotency` teaching module spanning multiple stacks (Node, Python/Django, NestJS).
- **Realtime collaborative editing appears twice with different techniques** — Plane uses Hocuspocus/CRDT, Teable uses ShareDB/OT — a clean, ready-made "CRDT vs OT" compare/contrast module.
- **CRM domain appears twice with genuinely different architectures** — NextCRM (fixed Prisma schema) vs Twenty (metadata-driven object system) — another ready-made compare/contrast pairing.
- **E-commerce domain appears twice with different backend targets** — Saleor (GraphQL-native Django backend) vs MasterStore\storefront (Next.js frontend consuming Spree's REST/JSON API) — different layers of the same domain, good for a "backend-for-frontend" discussion.
- **Stack variety gaps**: this batch is heavily Node/Next.js and Python/Django CRUD-monolith shaped; the only CLI/dev-tooling project is shadcn/ui, the only low-code/plugin-architecture project is ToolJet (uncurriculated), and there is no C#/.NET or SQL Server representation anywhere in this batch — worth noting for a developer whose stated focus includes .NET/SQL Server, since this batch contributes nothing there.
