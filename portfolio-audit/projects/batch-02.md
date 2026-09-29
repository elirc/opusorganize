# Batch 02 — Course/sprint repos (gitvg fleet, gitjira, gitjira-app, perch)
Scope: Desktop\gitvg\* (24 entries), Desktop\gitjira, Desktop\gitjira-app, Desktop\perch  |  Candidate dirs inspected: 27  |  Meaningful projects: 19  |  Tiny/empty/boilerplate: 8

All items in this batch are LLM-built ("Fable/Opus/Claude") upskilling courses: a product clone shipped as 15 sprint PRs (or, for the `-net`/`-app` rebuilds, ~17 PRs), each sprint carrying ADRs, planted-then-harvested design flaws, and teaching commentary. None are original hand-built products. Evidence for git counts came from `git log --oneline | wc -l` and `git tag` per repo.

## Candidate table

| Project | Path | Type | Origin | Stack | Complexity | Docs | Disp |
|---|---|---|---|---|---|---|---|
| tracer | gitvg\tracer | monorepo(2 apps) | COURSE/GENERATED | Node/Fastify+React/pnpm+Turbo, Postgres | Mid | STRONG | B |
| tracer-net | gitvg\tracer-net | API | COURSE/GENERATED | C#/.NET10, EF Core | Mid | STRONG | C |
| relay | gitvg\relay | monorepo(2 apps) | COURSE/GENERATED | Node+React, Postgres, durable exec | Mid+ | STRONG | B |
| relay-app | gitvg\relay-app | monorepo(2 apps) | COURSE/GENERATED | .NET10 API + React/TS client | Mid+ | STRONG | C |
| folio | gitvg\folio | monorepo(2 apps) | COURSE/GENERATED | Node+React, CRDT/offline merge | Mid+ | STRONG | B |
| folio-app | gitvg\folio-app | monorepo(2 apps) | COURSE/GENERATED | .NET10 API + React/TS client | Mid+ | STRONG | C |
| harbor | gitvg\harbor | monorepo(2 apps) | COURSE/GENERATED | Node+React, Postgres | Mid+ | STRONG | B |
| harbor-net | gitvg\harbor-net | API | COURSE/GENERATED | C#/.NET10, EF Core | Mid+ | STRONG | C |
| pulse | gitvg\pulse | monorepo(2 apps) | COURSE/GENERATED | Node+React, event ingestion, SDK | Mid+ | STRONG | B |
| pulse-net | gitvg\pulse-net | API | COURSE/GENERATED | C#/.NET10, queue/DLQ ingestion | Mid+ | STRONG | C |
| bazaar | gitvg\bazaar | monorepo(2 apps) | COURSE/GENERATED | Node+React, caching, observability/perf dirs | Mid+ | STRONG | B |
| bazaar-app | gitvg\bazaar-app | monorepo(2 apps) | COURSE/GENERATED | .NET10 API (SQLite) + React/TS client | Mid+ | STRONG | B |
| atlas | gitvg\atlas | API-only (5-project solution) | COURSE/GENERATED | C#/.NET10, EOR domain, 508 .cs files | Senior-oriented | STRONG | A |
| atlas-net | gitvg\atlas-net | API | COURSE/GENERATED | C#/.NET10 rebuild of atlas | Mid+ | STRONG | F |
| agora | gitvg\agora | monorepo(fullstack) | COURSE/GENERATED | C#/.NET10 API + React/TS web, Course 9 | Senior-oriented | STRONG | A |
| agora-net | gitvg\agora-net | API | COURSE/GENERATED | C#/.NET10 backend-only rebuild of agora | Mid+ | STRONG | F |
| storefront | gitvg\storefront | monolith (Next.js) | COURSE/GENERATED | Next.js, Prisma, Postgres, e2e | Mid+ | STRONG | B |
| astra | gitvg\astra | curriculum/docs-only | COURSE/GENERATED | Markdown handbook/modules | n/a (curriculum) | EXCELLENT | D |
| docs (gitvg root) | gitvg\docs | docs-only | COURSE/GENERATED | Markdown sprint plan ("Meridian") | Tiny | MINIMAL | G |
| tools (gitvg root) | gitvg\tools | script | ORIGINAL | 1 PowerShell script | Tiny | NONE | G |
| gitvg\*.md prompts | gitvg\SPEC.md, bazaar-build-prompt.md, gpt56-atlas-prompt.md, gpt56-perch-prompt.md | docs-only | COURSE/GENERATED | build prompts for GPT-5.6-authored siblings | n/a | MINIMAL | G |
| gitjira | Desktop\gitjira | docs-only (spec + sprint plan) | COURSE/GENERATED | Markdown | Tiny | STRONG (spec) | G |
| gitjira-app | Desktop\gitjira-app | monorepo(3 apps) | COURSE/GENERATED | Node/Express+React+Prisma, BullMQ, Socket.IO | Mid+ | EXCELLENT | A |
| perch | Desktop\perch | monorepo(2 apps) | COURSE/GENERATED | Node+React, ATS domain | Mid+ | EXCELLENT | B |

---

## tracer
- Path: `Desktop\gitvg\tracer`            - Origin: COURSE/GENERATED
- Type: monorepo (apps/api Fastify, apps/web React) — offline-first, real-time issue tracker (Linear clone)
- State: complete (v1.0.0 tag, 15 sprint history implied by README)   - Size: ~180 files   - Last modified: 2026-07-09 (git log -1)
- Purpose: A Linear-style issue tracker (teams, workflow states, cycles, fractional-ranked backlog, real-time sync) built explicitly as a 15-sprint teaching course; the product is real and runnable but the commit history/PR trail is the actual deliverable.
- Stack: FE: React (apps/web); BE: Fastify (apps/api); DB: Postgres via packages/db, Docker Compose; ORM: unknown (needs deeper check, likely Prisma/Drizzle given `db:generate`/`db:seed` scripts); Test: `*.test.ts` (16 files found e.g. `auth/state.test.ts`, `auth/tokens.test.ts`, `lib/fanout.test.ts`); CI: `.github/workflows/ci.yml` + `deploy.yml`
- Architecture: modular monolith split into api/web workspace apps via pnpm+Turbo; realtime fanout module present (`lib/fanout.test.ts`) suggesting websocket/event fanout.
- Complexity: Mid
- Educational material: STRONG — `docs/` (sprints, ADRs implied by sibling repos' pattern), `.github/ISSUE_TEMPLATE` (bug/task/user-story), `PULL_REQUEST_TEMPLATE.md`; teaching framing baked into README itself ("planted-then-harvested design debt, inline review commentary"). Preserve.
- Quality observations:
  - 16 backend unit/integration test files present under `apps/api/src` (auth, lib) — modest coverage for an app this size; not deeply verified beyond file presence.
  - CI workflow present (`ci.yml`, `deploy.yml`), suggesting the course enforces gate discipline per sprint, consistent with the fleet-wide pattern (confirmed identically in siblings).
  - Uses pnpm workspaces + Turborepo (`turbo run dev/build/typecheck/test`), a production-typical monorepo toolchain rather than a single flat app.
- Old-AI-generated smells: none directly observed at structure level; needs deeper per-file review to confirm (not done here given batch scope — see "Duplicate/overlap").
- Skill tags: fe-react, be-node-express, realtime-ws, db-postgres, orm, test-unit, test-integration, ci-cd, arch-modular-monolith
- Duplicate/overlap: `tracer-net` is a clean-room C#/.NET10 backend-only rebuild of the same product spec (see below).
- Learning value: High — canonical original of the "Linear clone" course line, JS/TS stack, real-time + offline-first concerns.
- Transformation opportunity: Could anchor a "same domain, two stacks" comparative teaching unit against tracer-net (state-machine design compared in TS vs C#).
- Interview stories it could support: designing a Linear-style state machine for issue workflow; offline-first sync/fanout design; fractional ranking for ordered lists.
- Proposed disposition: B HIGH-VALUE — complete, well-documented original course app with a JS/TS stack that's directly relevant to the user's growth track.

## tracer-net
- Path: `Desktop\gitvg\tracer-net`            - Origin: COURSE/GENERATED (clean-room .NET rebuild of tracer)
- Type: API only (no client)
- State: complete (v1.0.0 + v2.0.0 tags, 35 commits)   - Size: ~190 files   - Last modified: 2026-07-17
- Purpose: Same Linear-clone domain as `tracer`, rebuilt backend-only in C#/.NET10 + ASP.NET Core as a distinct course exercise in translating a JS/TS API design into idiomatic .NET.
- Stack: BE: ASP.NET Core / .NET10; DB: EF Core (per README: "Teams own everything... issues move under a validated state machine... fractional rank... time-boxed cycle... filterable search endpoint"); Test: 45 `.cs` test files under `tests/`
- Architecture: layered .NET solution (typical Domain/Application/Infrastructure/Api split, confirmed pattern across all `-net` siblings).
- Complexity: Mid+
- Educational material: STRONG — `docs/` ADRs present; per-fleet memory this was one of "5 clean-room C#/.NET10 backend rebuilds ... built via parallel Opus subagents + git worktrees," 17 PRs each, COMPLETE at v2.0.0.
- Quality observations:
  - 45 test files vs tracer's 16 — the .NET rebuild has notably heavier test coverage, consistent with .NET course emphasis on state-machine/concurrency testing.
  - `tmp/` directory present at repo root — likely scratch/build artifact left in place (read-only audit, not removed).
- Old-AI-generated smells: none seen at structural level.
- Skill tags: be-dotnet, db-postgres, orm, arch-clean-hex, test-unit, test-integration, backcompat-versioning (V1/V2-style contracts implied)
- Duplicate/overlap: direct backend-only sibling of `tracer` (same domain, different stack, no shared code).
- Learning value: Medium-High — best used as the ".NET half" of a stack-comparison exercise rather than standalone.
- Transformation opportunity: n/a (paired with tracer above)
- Interview stories: implementing optimistic-concurrency/fractional-ordering in EF Core; migrating a JS API surface to C#.
- Proposed disposition: C SPECIALIZED — valuable specifically as the .NET counterpart to tracer; keep paired, not a flagship on its own.

## relay
- Path: `Desktop\gitvg\relay`            - Origin: COURSE/GENERATED
- Type: monorepo (apps/api + apps/web + packages)
- State: complete (v0.5.0, v1.0.0 tags, 16 commits)   - Size: ~239 files   - Last modified: 2026-07-09
- Purpose: A Zapier-class workflow-automation platform (triggers, actions, multi-step "relays," connector ecosystem, durable execution engine) built as a 15-sprint course.
- Stack: FE/BE: Node + React monorepo (apps/, packages/, scripts/); durable execution engine implied by README.
- Architecture: modular monolith, connector-plugin style, durable job execution (queue-like).
- Complexity: Mid+
- Educational material: STRONG — docs/ + scripts/ + course framing in README identical to fleet pattern.
- Quality observations:
  - Domain (durable multi-step workflow execution with retries) is one of the more advanced problem spaces in the batch — good for teaching idempotency/retry semantics.
  - Structure mirrors tracer/harbor/pulse/folio/bazaar exactly (apps/docs/packages/scripts), indicating a shared course-generation template across the fleet.
- Old-AI-generated smells: none seen at structural level (not deep-dived further, see batch note on fleet uniformity).
- Skill tags: be-async-jobs, queues, idempotency, arch-event-driven, fe-react, test-unit
- Duplicate/overlap: `relay-app` is the .NET10+React full-stack rebuild of this same product (server/client dirs vs apps/api+apps/web).
- Learning value: High — connector/durable-execution domain is distinct from the CRUD-heavy siblings and closer to production integration-platform work.
- Transformation opportunity: Extract the durable execution engine design as a standalone "build your own job orchestrator" teaching module.
- Interview stories: designing idempotent retries for external connector calls; multi-step workflow state persistence.
- Proposed disposition: B HIGH-VALUE

## relay-app
- Path: `Desktop\gitvg\relay-app`            - Origin: COURSE/GENERATED (full-stack .NET rebuild of relay)
- Type: monorepo(2 apps: server/client)
- State: complete (v1.0.0, v2.0.0 tags, 35 commits)   - Size: ~274 files   - Last modified: 2026-07-18
- Purpose: Same Zapier-class connectors/flows/runs domain as `relay`, rebuilt full-stack with a .NET10 API and a React/TypeScript client (per memory: one of 3 "*-app" full-stack rebuilds shipped 17 PRs each, COMPLETE v2.0.0).
- Stack: BE: ASP.NET Core/.NET10 (`/server`); FE: Vite+React+TS (`/client`, pattern confirmed identical in folio-app sibling README)
- Architecture: modular monolith, client/server split (not a monorepo workspace tool like Turbo — simple two-folder split).
- Complexity: Mid+
- Educational material: STRONG — docs/ ADRs present, same fleet pattern.
- Quality observations:
  - `tmp/` present at root (build scratch, consistent with all `-app`/`-net` siblings — likely a shared generation-tool artifact left behind).
  - Full-stack .NET+React rebuild pattern (server/client, not apps/packages) distinguishes these from the TS originals and the backend-only `-net` repos.
- Old-AI-generated smells: none seen structurally.
- Skill tags: be-dotnet, fe-react, ts-types, arch-modular-monolith, queues, idempotency
- Duplicate/overlap: full-stack .NET counterpart to `relay`.
- Learning value: Medium-High — same domain-value as relay but as the .NET/React pairing exercise.
- Interview stories: same as relay, translated to .NET/EF Core context.
- Proposed disposition: C SPECIALIZED — pair with relay; not independently a flagship.

## folio
- Path: `Desktop\gitvg\folio`            - Origin: COURSE/GENERATED
- Type: monorepo (apps/api + apps/web + packages)
- State: complete (v0.5.0, v1.0.0, 16 commits)   - Size: ~224 files   - Last modified: 2026-07-10
- Purpose: A Notion-class collaborative document editor (block-based rich text, real-time multiplayer, offline merge, comments, permissions, version history) — 15-sprint course.
- Stack: Node + React monorepo; offline-merge/CRDT-adjacent concerns per README.
- Architecture: modular monolith with real-time collab layer.
- Complexity: Mid+
- Educational material: STRONG — same fleet doc pattern (docs/, scripts/).
- Quality observations:
  - Real-time multiplayer + offline merge is one of the harder problem domains in the batch (CRDT/OT-adjacent); good teaching value for conflict resolution.
  - Structure identical to relay/tracer/harbor/pulse/bazaar (shared course template).
- Old-AI-generated smells: none seen structurally.
- Skill tags: realtime-ws, fe-react, db-postgres, arch-event-driven, authz-rbac (permissions per README)
- Duplicate/overlap: `folio-app` is the .NET10+React full-stack rebuild.
- Learning value: High — collaborative-editing domain (version history, permissions, offline merge) is distinct and valuable.
- Interview stories: designing block-based document data model; handling offline edit conflicts; permission inheritance in nested docs.
- Proposed disposition: B HIGH-VALUE

## folio-app
- Path: `Desktop\gitvg\folio-app`            - Origin: COURSE/GENERATED (full-stack .NET rebuild of folio)
- Type: monorepo(2 apps: server ASP.NET Core + client Vite/React/TS)
- State: complete (v1.0.0, v2.0.0, 35 commits)   - Size: ~227 files   - Last modified: 2026-07-17
- Purpose: Notion-style docs/knowledge-base app, same domain as folio, rebuilt full-stack in .NET10/EF Core + React/TS strict client with React Router and a typed fetch API client (per README).
- Stack: BE: ASP.NET Core/.NET10, EF Core + SQLite; FE: Vite+React+TS strict, React Router.
- Architecture: modular monolith, server/client split.
- Complexity: Mid+
- Educational material: STRONG (docs/ ADRs, fleet-consistent).
- Quality observations: same generation-tool `tmp/` artifact present; SQLite (not Postgres) used for the .NET rebuilds/apps per README — a lighter-weight DB choice worth flagging when judging production-realism.
- Old-AI-generated smells: none seen structurally.
- Skill tags: be-dotnet, fe-react, ts-types, db-sqlite, orm
- Duplicate/overlap: full-stack .NET counterpart to `folio`.
- Learning value: Medium-High
- Interview stories: same as folio, .NET/EF Core framing.
- Proposed disposition: C SPECIALIZED

## harbor
- Path: `Desktop\gitvg\harbor`            - Origin: COURSE/GENERATED
- Type: monorepo (apps/api + apps/web + packages)
- State: complete — README explicitly states "Status: v1.0.0 — all 15 sprints shipped," links `docs/COURSE-RETROSPECTIVE.md` for "eval-first arc, flaw ledger, cost tally"   - Size: ~225 files   - Last modified: 2026-07-11
- Purpose: Intercom-style customer messaging & support platform (per memory: workspaces, inboxes, conversations, SLA engine, reporting, webhooks, help center) — 15-sprint course.
- Stack: Node + React monorepo.
- Architecture: modular monolith, messaging/inbox domain.
- Complexity: Mid+
- Educational material: STRONG — `docs/COURSE-RETROSPECTIVE.md` explicitly documents the "eval-first" teaching thesis and cost tally, a step beyond the standard sprint-doc pattern seen in siblings.
- Quality observations:
  - Retrospective doc is unusually reflective/meta compared to sibling repos — worth preserving as an example of "how to structure a retro."
  - SLA engine + round-robin assignment (per memory of harbor-net README) implies non-trivial business-rule logic, good for interview prep.
- Old-AI-generated smells: none seen structurally.
- Skill tags: be-node-express, fe-react, realtime-ws, be-async-jobs, observability-logs
- Duplicate/overlap: `harbor-net` is the C#/.NET10 backend-only rebuild.
- Learning value: High
- Interview stories: SLA/escalation engine design; round-robin ticket assignment; signed webhook delivery.
- Proposed disposition: B HIGH-VALUE

## harbor-net
- Path: `Desktop\gitvg\harbor-net`            - Origin: COURSE/GENERATED (backend-only .NET rebuild)
- Type: API only
- State: complete (v1.0.0, v2.0.0, 35 commits)   - Size: ~174 files   - Last modified: 2026-07-17
- Purpose: Same Intercom-style messaging domain, backend-only .NET10/ASP.NET Core rebuild — "Workspaces, inboxes, contacts, teammates and teams, conversations with threaded messages and internal notes, round-robin assignment, an SLA engine, reporting, signed webhooks, an email channel, a help center" (README).
- Stack: ASP.NET Core/.NET10, EF Core.
- Complexity: Mid+
- Educational material: STRONG (docs/ ADRs, fleet pattern).
- Quality observations: `tmp/` artifact present (fleet-wide pattern); layered src/ (Api/Application/Domain/Infrastructure typical of the `-net` line per atlas/agora-net structure check).
- Skill tags: be-dotnet, be-async-jobs, db-postgres/db-sqlite (unconfirmed which), orm
- Duplicate/overlap: backend counterpart to harbor.
- Learning value: Medium-High
- Proposed disposition: C SPECIALIZED

## pulse
- Path: `Desktop\gitvg\pulse`            - Origin: COURSE/GENERATED
- Type: monorepo (apps/api + apps/web + packages + load/)
- State: complete (v0.5.0, v1.0.0, 16 commits)   - Size: ~332 files (largest of the JS originals)   - Last modified: 2026-07-11
- Purpose: PostHog/Mixpanel-style product-analytics platform — event ingestion, embeddable browser SDK, persons/identity resolution, insights (trends/funnels/retention), dashboards, live events, sampling, feature flags & experiments. 15-sprint course.
- Stack: Node + React monorepo; has a dedicated `load/` directory (load-testing artifacts) not seen in siblings.
- Architecture: modular monolith with event-ingestion pipeline; per fleet memory the `-net` version underwent a "PG→ClickHouse migration arc" — worth checking if that applies here too or only pulse-net/pulse-upskill course.
- Complexity: Mid+
- Educational material: STRONG.
- Quality observations:
  - Largest file count among the JS-original course repos (332), and the only one with a `load/` perf-testing directory — suggests deeper performance-engineering content than siblings.
  - Analytics-ingestion + SDK + feature-flags domain is broad; good candidate for splitting into focused exercises (ingestion pipeline vs insights query engine vs SDK).
- Old-AI-generated smells: none seen structurally.
- Skill tags: be-async-jobs, queues, db-postgres, perf-investigation, ai-llm-integration (unconfirmed — check experiments/flags module), observability-metrics-tracing
- Duplicate/overlap: `pulse-net` is the backend-only .NET rebuild.
- Learning value: Very High — analytics/event-pipeline domain is one of the most production-relevant in the batch (ingestion, sampling, dashboards).
- Transformation opportunity: The event-ingestion + SDK layer could become a standalone "build your own analytics SDK" exercise module, since it's self-contained and widely applicable.
- Interview stories: designing an event-ingestion pipeline with backpressure/sampling; person-identity merge algorithm; feature-flag evaluation service design.
- Proposed disposition: A FLAGSHIP — broadest, most production-relevant domain of the JS-original course line, with load-testing artifacts unique in the batch.

## pulse-net
- Path: `Desktop\gitvg\pulse-net`            - Origin: COURSE/GENERATED (backend-only .NET rebuild)
- Type: API only
- State: complete (v1.0.0, v2.0.0, 35 commits)   - Size: ~138 files   - Last modified: 2026-07-16
- Purpose: Same analytics-platform domain, .NET10 backend-only. README: "Projects own write keys; SDKs push events to POST /capture (async ingestion with a durable queue and dead-letter storage); resolves anonymous device ids into persons ($identify merge)..."
- Stack: ASP.NET Core/.NET10, durable queue + DLQ.
- Complexity: Mid+
- Educational material: STRONG.
- Quality observations: dead-letter-queue ingestion design explicitly called out in README — a genuinely useful production pattern to preserve as a teaching example regardless of disposition.
- Skill tags: be-dotnet, queues, idempotency, db-postgres, observability-metrics-tracing
- Duplicate/overlap: backend counterpart to pulse.
- Learning value: Medium-High
- Proposed disposition: C SPECIALIZED

## bazaar
- Path: `Desktop\gitvg\bazaar`            - Origin: COURSE/GENERATED
- Type: monorepo (apps/ + packages/ + deploy/ + observability/ + performance/ + .course-ops/)
- State: complete (v0.5.0, v1.0.0, 16 commits)   - Size: ~508 files (largest in entire batch)   - Last modified: 2026-07-12
- Purpose: Shopify-lite commerce platform: cached customer storefront + consistency-critical merchant back office. "Systems-design course" per README, explicitly framed around the storefront/back-office consistency tension.
- Stack: Node + React monorepo, with dedicated `deploy/`, `observability/`, `performance/` top-level dirs not present in any sibling — the most infra-complete of the batch.
- Architecture: modular monolith with explicit caching-vs-consistency split (storefront cache layer vs back-office strong-consistency layer).
- Complexity: Mid+
- Educational material: STRONG — `.course-ops/` directory (unique to this repo) suggests dedicated course-operations tooling beyond docs.
- Quality observations:
  - Only repo in the batch with top-level `observability/` and `performance/` directories — implies deliberate teaching content on caching invalidation, perf budgets, and monitoring that siblings only touch via docs/ADRs.
  - Largest file count (508) of any repo in this batch, including the atlas .NET original (619 is larger but that's pure C#, no client).
- Old-AI-generated smells: none seen structurally.
- Skill tags: caching, observability-metrics-tracing, perf-investigation, db-postgres, arch-modular-monolith, deploy, ci-cd
- Duplicate/overlap: `bazaar-app` is the .NET10+React full-stack rebuild.
- Learning value: Very High — caching/consistency split and dedicated observability/performance content make this the strongest "production operations" teaching material in the batch.
- Transformation opportunity: The storefront-cache vs back-office-consistency architecture split could be lifted into a standalone system-design writeup/ADR set independent of the full course.
- Interview stories: cache invalidation strategy for a storefront; consistency guarantees for inventory/order writes under load; perf budget enforcement.
- Proposed disposition: A FLAGSHIP — most infra/ops-complete repo in the batch.

## bazaar-app
- Path: `Desktop\gitvg\bazaar-app`            - Origin: COURSE/GENERATED (full-stack .NET rebuild of bazaar)
- Type: monorepo(2 apps: server + client)
- State: complete (v1.0.0, v2.0.0, 35 commits)   - Size: ~289 files   - Last modified: 2026-07-18 (most recently touched repo in the gitvg fleet)
- Purpose: Same Shopify-lite commerce domain (storefront + admin back-office), full-stack .NET10 API + React/TS client. README explicitly lists domain breadth: catalog, orders & fulfilment, discounts, reviews, returns, gift cards, tax, reports & webhooks.
- Stack: BE: ASP.NET Core/.NET10, EF Core + SQLite, layered `Bazaar.Api`/`Bazaar.Domain`/`Bazaar.Infrastructure`; FE: React+TS client.
- Architecture: modular monolith, server/client split.
- Complexity: Mid+
- Educational material: STRONG.
- Quality observations:
  - 33 C# test files (server) + 21 TS test files (client) — reasonably balanced FE/BE test coverage, best-measured of the `-app` rebuilds.
  - Broadest e-commerce domain surface of any single repo (gift cards, returns/RMA, tax, webhooks all in one).
- Old-AI-generated smells: none seen structurally.
- Skill tags: be-dotnet, fe-react, ts-types, db-sqlite, orm, be-validation
- Duplicate/overlap: full-stack .NET counterpart to `bazaar` (and structurally close to `agora`/`agora-net`, both e-commerce).
- Learning value: High — domain breadth + balanced test coverage make it a strong .NET/React showcase distinct from bazaar's ops-focused JS original.
- Interview stories: RMA/returns workflow state machine; gift-card ledger; tax-by-zone calculation.
- Proposed disposition: B HIGH-VALUE — strongest of the `-app` rebuilds on its own merits (not just a paired specialization), given domain breadth and test balance.

## atlas
- Path: `Desktop\gitvg\atlas`            - Origin: COURSE/GENERATED
- Type: API only (5-project .NET solution: Api/Application/Contracts/Domain/Infrastructure)
- State: complete (v0.5.0, v1.0.0 tags, 16 commits)   - Size: 508 `.cs` files across src+tests, 619 total files   - Last modified: 2026-07-15
- Purpose: A Velocity Global/Pebl-style Employer-of-Record (EOR) platform — global hiring, onboarding, payroll, contractor payments, compliance, invoicing across countries. Built directly as a C#/.NET10 course (not a JS-original with a later rebuild).
- Stack: ASP.NET Core/.NET10 only; domain module breadth: ApiKeys, Approvals, Auditing, Auth, Compliance, Contractors, Countries, Engagements, Expenses, Invoicing, Leave, Operations, Orgs, Payments, Payroll, Quotes, Reporting, Webhooks, Workforce (per `src/Atlas.Application/*` listing) — the widest single-domain module count in the batch.
- Architecture: clean/hexagonal layered architecture (Api/Application/Contracts/Domain/Infrastructure), with `Contracts/V1` and `Contracts/V2` present — explicit API versioning exercise.
- Complexity: Senior-oriented — per user memory, this course specifically features "hexagon+NetArchTest, all 5 planted flaws harvested," S12-15 via parallel Opus subagents, and a dedicated `Idempotency`/`Outbox`/`Shadow`/`Fx` (currency) set of infra concerns.
- Educational material: STRONG — `FLAW-LEDGER.local.md` present at repo root (planted/harvested design flaws), `docs/` ADRs, `.github/ISSUE_TEMPLATE` (story/task), CI workflow.
- Quality observations:
  - 139 test `.cs` files — the heaviest test suite of any repo in this batch by a wide margin.
  - Domain includes payroll/invoicing/multi-currency (`Fx/`) and an `Outbox` + `Idempotency` infra layer — genuinely production-grade concerns rarely modeled this completely in the other course repos.
  - `NetArchTest`-style architecture-fitness testing implied by memory notes (not independently re-verified here, but consistent with `tests/` structure and ADR count).
- Old-AI-generated smells: none seen structurally; this is the most architecturally rigorous repo in the batch.
- Skill tags: be-dotnet, arch-clean-hex, outbox, idempotency, db-transactions, backcompat-versioning, authz-rbac, security-owasp, design-docs-adrs
- Duplicate/overlap: `atlas-net` is a separate clean-room rebuild of the same spec (redundant with this repo, not a stack-variant pair like the tracer/harbor/pulse lines, since atlas is already .NET).
- Learning value: Very High — most senior-oriented, most architecturally complete repo in the entire batch.
- Transformation opportunity: The Outbox + Idempotency + multi-currency (Fx) modules could be extracted as a standalone "production patterns" reference library independent of the EOR domain, since these are broadly reusable teaching artifacts.
- Interview stories: transactional outbox implementation; idempotency-key design for payment APIs; API versioning strategy (V1→V2 contracts); payroll calculation correctness under compliance rules.
- Proposed disposition: A FLAGSHIP — the most senior/production-grade single repo found in this batch.

## atlas-net
- Path: `Desktop\gitvg\atlas-net`            - Origin: COURSE/GENERATED (clean-room rebuild of atlas)
- Type: API only
- State: complete (v1.0.0, v2.0.0, 35 commits)   - Size: ~119 files (much smaller than atlas's 619)   - Last modified: 2026-07-16
- Purpose: Rebuild of the same EOR domain as atlas, produced separately per user memory ("5 clean-room C#/.NET10 backend rebuilds... tracer/harbor/pulse/atlas/agora → *-net").
- Stack: ASP.NET Core/.NET10.
- Complexity: Mid+ (notably smaller/thinner than atlas itself — 119 files vs atlas's 619, same domain).
- Educational material: STRONG (docs/ ADRs, fleet pattern).
- Quality observations: Given atlas is already a full, senior-oriented .NET implementation of this exact domain, atlas-net appears to be a lighter/duplicate treatment of the same spec rather than a genuinely distinct stack comparison (unlike tracer/tracer-net or harbor/harbor-net, which pair a JS original against a .NET rebuild). This makes it the closest thing to a true redundant duplicate in the batch.
- Skill tags: be-dotnet, orm, db-postgres
- Duplicate/overlap: near-total domain duplicate of `atlas` — the one pairing in this batch where both sides are the same language/stack.
- Learning value: Low-Medium given the stronger atlas already covers this domain.
- Proposed disposition: F CONSOLIDATE — recommend treating atlas as canonical and archiving/merging atlas-net's unique bits (if any ADRs differ) rather than maintaining both.

## agora
- Path: `Desktop\gitvg\agora`            - Origin: COURSE/GENERATED
- Type: monorepo (fullstack: `src/Agora.Api|Application|Contracts|Domain|Infrastructure` + `web/`)
- State: complete (v0.5.0 tag, 8 commits — fewest commits of any "complete" repo in the batch, worth flagging)   - Size: ~333 files   - Last modified: 2026-07-16
- Purpose: "Course 9" — an e-commerce web app (Shopify-style single store: storefront + admin back office for products/pricing/inventory/promotions/orders), explicitly built as C#/.NET + React/TypeScript from the start (not a JS-original with a later rebuild, unlike relay/folio/bazaar). README states it's the successor to "GitJira, Tracer, Relay, Folio, Harbor, Pulse (JS/TS)" in the series.
- Stack: BE: ASP.NET Core/.NET (Api/Application/Contracts/Domain/Infrastructure layering, same clean-arch pattern as atlas); FE: React/TS (`web/`); docs include `docs/openapi/` and `docs/http/` — unique to this repo, suggesting API-contract-first tooling (OpenAPI spec + .http request files).
- Architecture: clean/layered monolith, full-stack in one repo (not client/server split like the `-app` line).
- Complexity: Senior-oriented (per memory: "Course 9 in the git-connected upskilling series," full clean-arch + React).
- Educational material: STRONG — `docs/adr`, `docs/concepts`, `docs/curriculum`, `docs/http`, `docs/openapi`, `docs/sprints`, plus `FLAW-LEDGER.local.md` at root.
- Quality observations:
  - Only 8 commits despite v0.5.0 tag and "complete"-looking structure — this is a notably thin git history relative to every other "complete" repo in the batch (which run 16–35 commits); worth flagging as `NEEDS DEEPER INSPECTION` for whether this is genuinely finished or an earlier/squashed snapshot.
  - `docs/openapi/` + `docs/http/` present nowhere else in the batch — API-contract-first workflow evidence.
- Old-AI-generated smells: the unusually low commit count for a "v0.5.0, Course 9, clean-arch" repo is itself a smell worth flagging (possible squash-import or incomplete history capture) — NEEDS DEEPER INSPECTION.
- Skill tags: be-dotnet, fe-react, ts-types, arch-clean-hex, be-rest-design, design-docs-adrs
- Duplicate/overlap: `agora-net` is the backend-only rebuild of this same product.
- Learning value: High, pending the commit-count question above.
- Transformation opportunity: If verified complete, the `docs/openapi`+`docs/http` contract-first pattern is worth extracting as a template for other repos in the fleet that lack it.
- Interview stories: designing an OpenAPI-first contract workflow; promotions/discount pricing engine.
- Proposed disposition: A FLAGSHIP (tentative) — pending verification of the thin (8-commit) git history against the v0.5.0 tag; re-check before treating as fully equivalent to atlas/pulse/bazaar in polish.

## agora-net
- Path: `Desktop\gitvg\agora-net`            - Origin: COURSE/GENERATED (backend-only rebuild of agora)
- Type: API only
- State: complete (v1.0.0, v2.0.0, 35 commits)   - Size: ~186 files   - Last modified: 2026-07-17
- Purpose: E-commerce backend only — "catalog, inventory, guest and account carts, checkout with stock reservation, zone-based tax, shipping methods, gift cards, discounts, reviews, wishlists, returns (RMA), partial fulfillment, webhooks" per README — broad domain, backend-only.
- Stack: ASP.NET Core/.NET10.
- Complexity: Mid+
- Educational material: STRONG.
- Quality observations: has a much fuller, more typical commit history (35 commits, v1/v2 tags) than its `agora` sibling (8 commits) despite covering less surface (no client) — supports treating agora-net as the more reliably "complete-per-process" of the pair.
- Skill tags: be-dotnet, db-transactions (stock reservation), orm, be-rest-design
- Duplicate/overlap: backend counterpart to `agora`; also domain-overlaps `bazaar`/`bazaar-app` (both e-commerce, different feature emphasis — agora-net adds stock reservation + RMA + partial fulfillment explicitly).
- Learning value: Medium-High
- Interview stories: stock reservation during checkout (race conditions); partial fulfillment order-state modeling.
- Proposed disposition: C SPECIALIZED

## storefront
- Path: `Desktop\gitvg\storefront`            - Origin: COURSE/GENERATED
- Type: monolith (Next.js app, not client/server split)
- State: complete-looking (12 commits, no tags — the only "finished-looking" repo in the fleet with zero git tags)   - Size: ~133 files   - Last modified: 2026-07-15 (dir mtime shows Sep 21 due to later Astra pass)
- Purpose: "A production-shaped e-commerce application" — customer surface (browse/search/cart/checkout/orders/reviews) + seller admin (product CRUD/inventory/orders/images), single Next.js codebase + one Postgres DB, framed as a 15-sprint curriculum.
- Stack: FE/BE: Next.js (single codebase, `app/(storefront)`); DB: Postgres via `db/prisma`; ORM: Prisma; Test: `e2e/`, `test/fitness`, `test/stubs`; also has its own `astraupskill/` subfolder (evidence of the later "Astra" onboarding-curriculum pass referenced in user memory, `fablereview-astra-audit.md`).
- Architecture: SSR/monolith Next.js app-router codebase, not a monorepo split like the gitvg apps/packages pattern — structurally the odd one out among the e-commerce entries (agora, agora-net, bazaar, bazaar-app).
- Complexity: Mid+
- Educational material: STRONG — `docs/adr`, `docs/concepts`, `docs/curriculum`, `docs/sprints`, PLUS a full `astraupskill/` teaching pack (01-CODEBASE-MAP through 07-TRACE-LAB, evidence/, snapshots/, VERIFICATION.md) — this is the "Astra improvements" project referenced in memory's `fablereview-astra-audit.md` (2026-09 review/fix pass across 153 Astra-changed projects).
- Quality observations:
  - Has `test/fitness` (architecture-fitness tests) and `e2e/` — combination not seen together in the JS-original gitvg apps.
  - No git tags despite 12 commits and complete-looking structure — worth flagging as unusual relative to every other "complete" repo (all others carry at least one version tag).
  - The astraupskill/ evidence dir (JSON+log pairs) suggests this repo was a live subject of the Astra review-and-fix pass, not just a course build — its current state reflects two rounds of LLM work (original build + Astra fix pass).
- Old-AI-generated smells: none new seen; per memory, the Astra fix pass already addressed "codeblocks/glossary/leaked" issues fleet-wide, so this repo should already reflect a corrected state.
- Skill tags: fe-next, be-node-express (Next API routes), db-postgres, orm, test-e2e, arch-modular-monolith
- Duplicate/overlap: another e-commerce entry alongside agora/agora-net/bazaar/bazaar-app, but the only one on Next.js/Prisma rather than the gitvg apps/packages or .NET patterns — least redundant of the e-commerce cluster architecturally.
- Learning value: High — Next.js App Router + Prisma is directly relevant to the user's stated stack focus, and it's the only Next.js entry in this whole batch.
- Interview stories: Next.js App Router SSR/data-fetching patterns for an admin+customer dual-surface app; architecture-fitness testing setup.
- Proposed disposition: B HIGH-VALUE — best Next.js-stack example in the batch; verify the missing-tags anomaly before promoting further.

## astra
- Path: `Desktop\gitvg\astra`            - Origin: COURSE/GENERATED (curriculum, not a runnable app)
- Type: curriculum/docs-only
- State: docs-only, appears complete   - Size: 47 files   - Last modified: 2026-09-04 (most recently touched non-app dir in the batch)
- Purpose: A standalone onboarding/mentoring curriculum ("Astra") teaching a new engineer to navigate an existing large codebase — modules on language/navigation, React+a11y, HTTP contracts, data/migrations, permissions, debugging/concurrency, performance/delivery, TypeScript systems, commerce, domain design, integrations, analytics/streams, support/evaluation — plus a handbook (foundations/testing/debugging/delivery/data-and-permissions/mentoring-and-assessment/glossary) and onboarding walkthroughs (first-day, local-setup, code-tour, git-contribution, first-change, troubleshooting).
- Stack: n/a — pure Markdown curriculum + `scripts/check_curriculum.py` (a linter/checker script) + templates (adr.md, baseline.md, capstone-proposal.md, debug-log.md).
- Architecture: n/a
- Complexity: n/a (curriculum, not code)
- Educational material: EXCELLENT — 16 numbered modules + 6-file handbook + 6-file onboarding walkthrough + templates + a Python curriculum-integrity checker script; this is the source curriculum that was later applied ("astraupskill/") across gitjira-app, storefront, and other repos per user memory's Astra fix-pass note.
- Quality observations:
  - Has its own `SOURCE-AUDIT.md` and `REPO-MAP.md` — meta-documentation about the curriculum's own sourcing, unusual rigor for a docs-only project.
  - `scripts/check_curriculum.py` implies automated consistency checking of the curriculum content itself.
  - No `.git` directory — not independently versioned; lives as a folder inside gitvg.
- Old-AI-generated smells: none applicable (no code).
- Skill tags: design-docs-adrs, code-review, legacy-codebase-reading
- Duplicate/overlap: this is the generator/template for the `astraupskill/` folders found inside `storefront` and `gitjira-app` (and per memory, 153 other projects) — not itself duplicated, but its output is broadly distributed.
- Learning value: High as a meta-artifact (a working example of "how to onboard a junior engineer into a large codebase") rather than as hands-on coding practice.
- Transformation opportunity: Could be repackaged as a standalone onboarding-curriculum-authoring reference independent of any single target codebase.
- Proposed disposition: D REFERENCE — valuable as a template/reference for curriculum design, not as an exercise source itself.

## docs (gitvg root)
- Path: `Desktop\gitvg\docs`            - Origin: COURSE/GENERATED
- Type: docs-only
- State: partial/planning-only — 18 files, all under `docs/sprints/`   - Size: 18 files   - Last modified: 2026-07-09
- Purpose: Sprint-planning docs (`00-workflow.md`, `flaw-ledger.md`, `sprint-01..15.md`) for "Meridian — Global Employment Platform," per the co-located root `SPEC.md` (665 lines) — this is the planning/spec stage for what appears to be a *different* EOR course than atlas (Meridian vs. atlas's unnamed EOR clone), or possibly an early/alternate name for the same course; not independently confirmed which.
- Stack: n/a (Markdown only)
- Educational material: MINIMAL as a standalone artifact (it's the planning scaffold, not the executed course) — the actual code for "Meridian" was not found as a sibling directory in this batch; only the spec and sprint plan exist here.
- Quality observations: no corresponding `meridian/` or similar code directory found among gitvg's 24 entries — this looks like a planning-stage leftover, possibly superseded by `atlas` (same EOR domain) once the course was actually built.
- Skill tags: design-docs-adrs
- Duplicate/overlap: likely an earlier planning pass superseded by `atlas` (both are EOR/Pebl-style platforms) — NEEDS DEEPER INSPECTION to confirm whether Meridian ever shipped as code elsewhere.
- Learning value: Low as-is (no code).
- Proposed disposition: G ARCHIVE — planning artifact with no corresponding shipped code found in this batch; keep only if cross-referencing confirms it's the spec that became atlas.

## tools (gitvg root)
- Path: `Desktop\gitvg\tools`            - Origin: ORIGINAL
- Type: script
- State: tiny   - Size: 1 file (`publish-organized-projects.ps1`)   - Last modified: 2026-07-18
- Purpose: A PowerShell script, apparently for publishing/organizing projects (likely related to the user's own portfolio-organization workflow rather than course content).
- Educational material: NONE
- Proposed disposition: G ARCHIVE — one-off utility script, not a project.

## Loose gitvg root prompt files
- Path: `gitvg\bazaar-build-prompt.md`, `gitvg\gpt56-atlas-prompt.md`, `gitvg\gpt56-perch-prompt.md`, `gitvg\SPEC.md`
- Type: docs-only (LLM build prompts)
- Purpose: `gpt56-atlas-prompt.md` and `gpt56-perch-prompt.md` are build prompts intended for GPT-5.6 to build atlas/perch externally (per user memory: "Perch GPT-5.6 course... built externally, not a Claude answer-key"); `bazaar-build-prompt.md` likely the analogous prompt for bazaar; `SPEC.md` is the Meridian spec tied to `docs/`.
- Educational material: MINIMAL as standalone (they're prompts, not curricula) but useful as evidence of the batch's multi-model provenance (some course repos in this fleet were built by GPT-5.6 from these prompts, not by Claude/Opus).
- Proposed disposition: G ARCHIVE — reference/provenance artifacts only.

---

## gitjira
- Path: `Desktop\gitjira`            - Origin: COURSE/GENERATED
- Type: docs-only (spec + sprint plan; the actual product lives in the separate `gitjira-app` repo)
- State: docs-only, 1 commit   - Size: `SPEC.md` (37KB) + `sprints/` (15 sprint files + README) + `WORKFLOW-IMPROVEMENTS.md`   - Last modified: 2026-07-18
- Purpose: The design spec and 15-sprint plan for a Jira-clone course; per user memory ("GitJira upskilling project... AI-generated Jira-clone curriculum, 15 sprint PRs on github.com/elirc/gitjira; answer key in Desktop\gitjira, product in Desktop\gitjira-app") this is the answer-key/spec repo, distinct from the shipped product.
- Educational material: STRONG as a spec (37KB SPEC.md), but this repo is the planning layer only — the actual "answer key" course content and shipped code is in `gitjira-app`.
- Quality observations: only 1 commit — consistent with being a static spec drop rather than an iteratively-built app.
- Skill tags: design-docs-adrs
- Duplicate/overlap: paired with `gitjira-app` (spec vs. implementation).
- Learning value: Medium as a spec-writing example; low standalone without gitjira-app.
- Proposed disposition: G ARCHIVE (as a standalone item) — keep bundled with gitjira-app as its spec, not separately significant.

## gitjira-app
- Path: `Desktop\gitjira-app`            - Origin: COURSE/GENERATED
- Type: monorepo(3 apps: api, web, worker) + 3 shared packages
- State: complete — 209 commits, tags sprint-01..sprint-15 AND v0.1.0..v1.0.0 (10 version tags) — by far the richest git history/tagging scheme in this entire batch   - Size: large (apps/api, apps/web, apps/worker, packages/shared, packages/ui, packages/test-factories)   - Last modified: 2026-09-20 (astraupskill pass) / 2026-07-10 (core build)
- Purpose: A Jira-style issue tracker (backlog, sprints, boards, notifications) built as the shipped implementation of the `gitjira` spec — Express API + React web + a background worker + shared packages, with real-time (Socket.IO) and job queue (BullMQ) infrastructure.
- Stack: BE: Express (per `docs/adr/0002-express-over-nestjs-fastify.md`); DB: Postgres, Prisma-adjacent ORM decisions (per ADR titles: fractional indexing, partial unique index, JQL-lite parser, Postgres FTS over Elasticsearch); Queue: BullMQ (ADR-0018); Realtime: Socket.IO (ADR-0016, chosen over raw WS/SSE); Validation: Zod (shared, ADR-0005); Auth: JWT with refresh rotation (ADR-0004); Test: 29 test files across apps+packages, `e2e/` dir, coverage gates ("unequal-coverage-gates" ADR-0023, "e2e-nightly-not-per-pr" ADR-0024); CI: `ci.yml`, `deploy.yml`, `e2e.yml`, `secrets.yml` + Dependabot.
- Architecture: modular monolith (npm workspaces per ADR-0001) with a background worker process, event-driven notification fanout (ADR-0019), stale-write preconditions (ADR-0017), sprint state machine (ADR-0014) — an unusually complete set of 31 numbered ADRs covering nearly every major design decision.
- Complexity: Mid+
- Educational material: EXCELLENT — 31 ADRs (`docs/adr/0001..0031` + README), `docs/concepts/` (idempotency, incremental-migration, parsing, state-machines, websockets), `docs/postmortems/2026-07-10-redis-outage.md` (a fabricated-but-realistic incident postmortem), `docs/process/AUDIT-2026-07.md` + `SKILLS-LEDGER.md` + `WORKFLOW-IMPROVEMENTS.md`, `docs/RUNBOOK.md`, `docs/security-audit.md`, `docs/threat-model.md`, `docs/GLOSSARY.md`, plus a full `astraupskill/` teaching pack (7 numbered docs + evidence/ + snapshots/ of 10 original files pre-exercise + VERIFICATION.md) — the deepest and most complete documentation set found anywhere in this batch.
- Quality observations:
  - 209 commits and 25 total git tags (15 sprint tags + 10 version tags) — this is an order of magnitude more granular git history than any other repo in the batch, suggesting either a longer iterative build or finer-grained commit discipline.
  - Explicit postmortem doc (Redis outage) and threat-model/security-audit docs go beyond what any sibling repo in this batch has — strong incident-debugging and security-review teaching material.
  - `docs/process/AUDIT-2026-07.md` and `SKILLS-LEDGER.md` suggest this repo tracks its own skill-coverage explicitly, unique in the batch.
  - `evidence/` directory present at repo root (separate from astraupskill/evidence) — worth a closer look to confirm what it captures (likely CI/test run evidence).
- Old-AI-generated smells: none seen; if anything this is the most rigorously self-documented repo in the batch — worth using as the template for what "STRONG docs" should look like in other course repos.
- Skill tags: be-node-express, fe-react, queues, realtime-ws, authn, db-postgres, db-migrations, be-validation, test-integration, test-e2e, test-ci, observability-logs, security-owasp, incident-debugging, design-docs-adrs, outbox (fanout-on-write per ADR-0019)
- Duplicate/overlap: implementation of the `gitjira` spec; conceptually the JS-stack sibling of gitjira's own spec (no separate `-net`/`-app` rebuild exists for this one, unlike the gitvg fleet).
- Learning value: Very High — richest documentation, richest git history, broadest incident/security/postmortem content in the whole batch.
- Transformation opportunity: The ADR set + postmortem + threat-model + runbook combination is close to portfolio-ready as-is; could be lightly polished into a flagship "here's how I document and operate a real system" showcase independent of the "course" framing.
- Interview stories: JQL-lite grammar/parser design; fractional indexing for board ordering; stale-write precondition (optimistic concurrency) handling; Redis outage postmortem and remediation; notification fanout architecture.
- Proposed disposition: A FLAGSHIP — best-documented, most git-disciplined repo in the entire batch; strong candidate for a portfolio centerpiece.

---

## perch
- Path: `Desktop\perch`            - Origin: COURSE/GENERATED
- Type: monorepo(2 apps: api + web) + packages (config, db, shared)
- State: complete — 18 commits, tags v0.5.0 and v1.0.0   - Size: moderate (apps/api/src, apps/web/src, packages/db/prisma)   - Last modified: 2026-07-12
- Purpose: An ATS (applicant tracking system, per memory framed against Lever/Greenhouse-style tools) — candidate pipeline, interviews/scorecards, offers, public careers site, per the ADR titles (candidate-application-identity, fractional-pipeline-order, public-careers-boundary, scorecard-visibility, offer-lifecycle). Built as a 15-sprint course.
- Stack: BE: apps/api; DB: Prisma (`packages/db/prisma`); FE: apps/web; shared config package (`packages/config`); Test: 28 `.test.ts` files across apps.
- Architecture: modular monolith (pnpm workspace, per `pnpm-workspace.yaml`/`turbo.json`), with an explicit public/private trust boundary (public careers site vs internal ATS) called out in ADR-0005 and `docs/concepts/public-trust-boundaries.md`.
- Complexity: Mid+
- Educational material: EXCELLENT — 16 ADRs (ADR-0000 "course-charter" through ADR-0015), 14 `docs/concepts/*.md` (including IDOR, cursor-stability, fractional-ordering, functional-core-imperative-shell, write-once-evaluations), `docs/COURSE-RETROSPECTIVE.md`, `docs/curriculum/SPEC.md`, `docs/demo/DEMO-SCRIPT.md`, `docs/incidents/2026-07-simulated-stage-history-incident.md` + `EXERCISE.md`, `docs/performance/sprint-12-evidence.md`, `docs/runbooks/` (backup-and-restore, deploy-and-rollback, incident-response), `docs/security/` (object-authorization-audit, scanner-verification, threat-model), `docs/accessibility/sprint-14-audit.md`.
- Quality observations:
  - `FLAW-LEDGER.local.md` at root explicitly documents 5 planted-and-harvested flaws with plant/harvest sprint numbers, location, and RED-test evidence — e.g. "Stage transition reads version then writes without conditional claim, allowing two concurrent moves" (planted S04, harvested S13), "Public application endpoint lacks idempotency key... double submit creates duplicate applications" (S05→S13), "Interviewer candidate detail checks org membership but not panel assignment (IDOR)" (S06→S11), "Offset pagination skips/duplicates candidates when concurrent insert changes ordering" (S08→S12), "CSV import... corrupts quoted commas/newlines" (S09→S13). This is a rare case in the batch where the specific security/correctness bugs are explicitly documented with evidence, not just implied.
  - Dedicated `docs/incidents/EXERCISE.md` — turns a simulated incident into a standalone practice exercise, a format not seen elsewhere in this batch.
  - Accessibility audit doc (`sprint-14-audit.md`) — a11y coverage not called out explicitly in any other repo in this batch.
- Old-AI-generated smells: none seen; the explicit flaw ledger with RED-test evidence is a strength, not a smell — it shows deliberate, tracked defect injection/repair rather than accidental bugs.
- Skill tags: authz-rbac (IDOR fix), db-concurrency (offset-pagination race), idempotency, security-owasp, fe-a11y, be-validation (CSV parsing), design-docs-adrs, incident-debugging, test-e2e
- Duplicate/overlap: none within this batch (only ATS-domain repo); loosely thematically adjacent to gitjira-app's issue-tracker domain but a different product category.
- Learning value: Very High — the explicit, evidence-backed flaw ledger (IDOR, TOCTOU-style pagination race, missing idempotency key, CSV injection-adjacent parsing bug) is directly reusable as security-review / code-review interview material.
- Transformation opportunity: The flaw ledger + incident EXERCISE.md pairing could be extracted as a standalone "find and fix these 5 real bug classes" exercise pack independent of the full ATS course.
- Interview stories: explaining and fixing an IDOR (object-authorization) bug with evidence; diagnosing an offset-pagination concurrency bug; designing idempotency keys for public-facing submission endpoints; incident postmortem/exercise writing.
- Proposed disposition: B HIGH-VALUE — one of the strongest security/correctness teaching artifacts in the batch via its evidenced flaw ledger; consider elevating to A if the actual code for the 5 flaw fixes is verified in a follow-up deep-read.

---

## Batch observations

- **Shared generation template across the gitvg fleet.** tracer, relay, folio, harbor, pulse, and bazaar all share an identical top-level layout (`apps/`, `docs/`, `packages/`, `scripts/`), identical README framing ("X is a course, not just a codebase... 15-sprint upskilling curriculum... every sprint is one pull request"), and near-identical git tagging (`v0.5.0`, `v1.0.0`, 16 commits — except bazaar/relay/folio/harbor/pulse all show exactly 16, tracer also 16). This confirms these six are outputs of one shared course-generation process/prompt template rather than independently designed products — treat quality findings from a deep-dive of any one (e.g., tracer or pulse) as broadly predictive of the others, with domain-specific exceptions noted in the per-project records above (pulse's `load/` dir, bazaar's `observability/`+`performance/`+`deploy/` dirs, harbor's `COURSE-RETROSPECTIVE.md`).
- **Three parallel rebuild lines create a lot of duplication by design, not accident.** (1) Backend-only `.NET10` clean-room rebuilds: tracer-net, harbor-net, pulse-net, atlas-net, agora-net (all 35 commits, v1.0.0+v2.0.0 tags — a matched set). (2) Full-stack `.NET10 + React` rebuilds: relay-app, folio-app, bazaar-app (also 35 commits, v1.0.0+v2.0.0 — a second matched set), plus gitjira-app as a JS-stack full implementation of a separate spec-only repo. (3) Two repos (agora, atlas) were built .NET-first with no separate JS original. This is intentional stack-comparison pedagogy for most pairs, EXCEPT atlas/atlas-net, which is the one case where both sides are the same stack and the same domain — that pairing looks like genuine redundancy rather than a deliberate stack comparison (see atlas-net's `F CONSOLIDATE` disposition).
- **agora's thin git history (8 commits) stands out.** Every other "complete, tagged" repo in the fleet has 12–35 commits; agora's 8 is an outlier worth a closer look before fully trusting its "complete" status at face value, despite its docs/ and FLAW-LEDGER looking otherwise complete.
- **storefront and its Astra pass are the clearest evidence of the "Astra" curriculum (astra/) being applied in the field.** Both storefront and gitjira-app carry `astraupskill/` subfolders with evidence/ and snapshots/ of pre-exercise file states — this matches the user's memory note about a 2026-09 Astra review-and-fix pass across 153 projects. Any Astra-related follow-up work should treat storefront and gitjira-app as known worked examples.
- **gitjira-app and perch are the documentation high-water marks of this batch**, both significantly exceeding the standard fleet template: gitjira-app with 31 ADRs + postmortem + threat-model + audit/skills-ledger + 209 commits/25 tags, and perch with an explicit, evidence-backed 5-flaw ledger plus an accessibility audit and a standalone incident exercise. Both are strong flagship/high-value candidates independent of the rest of the fleet.
- **atlas is the single most senior-oriented artifact in the batch** (139 test files, Outbox+Idempotency+multi-currency infrastructure, explicit V1/V2 API contracts, hex-architecture with fitness tests implied) — notably stronger than its own "-net" rebuild, and arguably stronger than any of the JS-original gitvg apps.
- **The `gitvg\docs` + `SPEC.md` (Meridian) pairing looks like an orphaned planning stage** — no `meridian/` implementation directory exists among the batch's 24 gitvg entries, and the domain (global EOR platform) strongly overlaps atlas's. This needs a deeper check (possibly against other batches, since atlas lives in this batch but was memory-tagged as built independently) to confirm whether Meridian was ever implemented under a different name, or was fully superseded and should be archived outright.
- **No project in this batch showed old-AI-generated quality smells** (giant files, shallow/fake tests, hallucinated APIs) at the structural/README/ADR level inspected here — but this batch's audit depth was necessarily shallow given its size (27 candidates); a smaller, targeted deep-read pass (2–4 source files each) on the "A FLAGSHIP" candidates (pulse, bazaar, atlas, agora, gitjira-app) is recommended as a follow-up before final disposition decisions are locked in, per the brief's evidence-citation standard.
