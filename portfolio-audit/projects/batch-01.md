# Batch 01 — Desktop .NET projects
Scope: netairag, netauth, netcleanarch, netdocu, netdrop, netintercom, netlinear, netnotion, netopen1, netopen3, netopen5, netshop, netsnapshot, netsnapshot1, nopsolutionsnet, csharptut, c#interview, "_Organized Desktop\01 Net Workspaces\csbootcamp", .netarchitectureproject, .netopen2, .netramp, .netstripe, .nethris, .nettodo  |  Candidate dirs inspected: 24  |  Meaningful projects: 23  |  Tiny/empty/boilerplate: 1

## Quick table

| Project | Path | Type | Origin | Stack | Complexity | Docs | Disp |
|---|---|---|---|---|---|---|---|
| NetAiOps (netairag) | Desktop\netairag | web app / API monorepo | COURSE/GENERATED | .NET8 API + React frontend + Postgres | Mid | EXCELLENT (docs/upskill 47, docs2.0 47 dup, astraupskill 18) | B HIGH-VALUE |
| NetAuth0 (netauth) | Desktop\netauth | API + SPA (IdP) | COURSE/GENERATED | .NET8 API + React/Vite + Postgres, JWT/OIDC | Mid | EXCELLENT (docs/upskill 47, docs2 13) | B HIGH-VALUE |
| CleanArchitecture (netcleanarch) | Desktop\netcleanarch\CleanArchitecture | template/reference API+Blazor | OPEN-SOURCE CLONE (jasontaylordev) | .NET, MediatR, EF Core, Blazor client, NuGet template | Production-like | EXCELLENT (4 curriculum generations: fabledocs 09-dir, fabledocs2 6 files, fabledocs3 10 ADRs, fabledocs4 labs) | A FLAGSHIP |
| NetDocu (netdocu) | Desktop\netdocu | web app / API monorepo | COURSE/GENERATED | .NET8 API + React/TS, Postgres | Mid | USEFUL (docs/upskill 47) | B HIGH-VALUE |
| NetDropbox (netdrop) | Desktop\netdrop | web app / API monorepo | COURSE/GENERATED | .NET8 API + React/TS + Postgres | Mid+ | EXCELLENT (docs/upskill 47, astraupskill 23) | A FLAGSHIP |
| NetIntercom (netintercom) | Desktop\netintercom | web app / API monorepo (2 FE apps) | COURSE/GENERATED | .NET8 API + SignalR + 2x React (widget+inbox) + Postgres + Hangfire | Mid+ | USEFUL (docs/upskill 47) | A FLAGSHIP |
| NetLinear (netlinear) | Desktop\netlinear | web app / API monorepo | COURSE/GENERATED | .NET8 API + React/TS + Postgres | Mid | USEFUL (docs/upskill 47) | B HIGH-VALUE |
| NetNotion (netnotion) | Desktop\netnotion | web app / API monorepo | COURSE/GENERATED | .NET8 API + React/TS + Postgres | Mid | USEFUL (docs/upskill 47 + docs/fable 8, two curricula) | B HIGH-VALUE |
| eShop (netopen1) | Desktop\netopen1\eShop | microservices monorepo | OPEN-SOURCE CLONE (dotnet/eShop) | .NET Aspire, Blazor, gRPC, RabbitMQ/EventBus, Postgres, Redis | Senior-oriented | EXCELLENT (fabledocs 10-dir + fabledoc2 stub + astra/ 72-story curriculum) | A FLAGSHIP |
| Umbraco-CMS (netopen3) | Desktop\netopen3\Umbraco-CMS | CMS platform | OPEN-SOURCE CLONE (umbraco/Umbraco-CMS) | .NET, huge multi-project CMS | Production-like | MINIMAL at repo root (astraupskill = single bounded bug-fix exercise, not full curriculum) | C SPECIALIZED |
| jellyfin (netopen5) | Desktop\netopen5\jellyfin | media server platform | OPEN-SOURCE CLONE (jellyfin/jellyfin) | .NET, huge multi-project media server | Production-like | MINIMAL (fabledocs partial: only 2 sections; astraupskill = single bounded bug-fix exercise) | C SPECIALIZED |
| NetShopifyLite (netshop) | Desktop\netshop | web app / API monorepo | COURSE/GENERATED | .NET8 API + React + Postgres | Mid | USEFUL (docs/upskill 47) | B HIGH-VALUE |
| NetAiOps snapshots (netsnapshot) | Desktop\netsnapshot | curriculum (15 full-copy checkpoints) | COURSE/GENERATED | simulated .NET/React ops-ticket app, not meant to compile | Junior-Mid progression | STRONG (whole project IS the curriculum) | E EXERCISE SOURCE |
| Atlas Global Workforce snapshots (netsnapshot1) | Desktop\netsnapshot1 | curriculum (15 full-copy checkpoints) | COURSE/GENERATED | simulated TS/Node + React HR/workforce app, not meant to compile | Junior-Mid progression | STRONG (whole project IS the curriculum) | E EXERCISE SOURCE |
| nopCommerce (nopsolutionsnet) | Desktop\nopsolutionsnet\nopCommerce | e-commerce platform | OPEN-SOURCE CLONE (nopSolutions/nopCommerce) | ASP.NET Core, huge multi-project, MySQL/Postgres/SQL Server | Production-like | USEFUL (fabledocs 10-dir single generation) | C SPECIALIZED |
| C# language tutorial (csharptut) | Desktop\csharptut | curriculum, docs-only | COURSE/GENERATED | C#/.NET language + EF Core + ASP.NET Core topics, 24 lesson+example pairs | Tutorial | STRONG (whole project is the curriculum, 24 topics x2 files) | E EXERCISE SOURCE |
| C# interview prep (c#interview) | Desktop\c#interview | curriculum, docs-only | COURSE/GENERATED | interview prep: phases, question vault, mock scripts | Tutorial/Interview-prep | STRONG (per user's memory, ~490 Q&A + flashcards + gotchas already built) | E EXERCISE SOURCE |
| csbootcamp | Desktop\_Organized Desktop\01 Net Workspaces\csbootcamp | curriculum, exercise pack + docs | COURSE/GENERATED | offline auto-graded C# exercises (progress.cs/verify.cs) + cheatsheets + quizzes | Tutorial | STRONG (31 exercises/solutions + cheatsheets + quizzes + astraupskill bonus) | E EXERCISE SOURCE |
| modular-monolith-with-ddd (.netarchitectureproject) | Desktop\.netarchitectureproject\modular-monolith-with-ddd | reference DDD monolith | OPEN-SOURCE CLONE (kgrzybek) | .NET, DDD/CQRS, module-per-boundary | Senior-oriented | MINIMAL (astraupskill = single bounded exercise, kept separate from repo, not integrated) | D REFERENCE |
| OrchardCore (.netopen2) | Desktop\.netopen2\OrchardCore | modular multi-tenant CMS framework | OPEN-SOURCE CLONE (OrchardCMS/OrchardCore) | .NET10, ~200 projects, Yarn4 frontend, multi-tenant | Production-like | EXCELLENT (fabledocs/upskill 54 files, project-specific, line-cited) | A FLAGSHIP |
| ExpenseManagement (.netramp) | Desktop\.netramp | web app / API monorepo | COURSE/GENERATED | ASP.NET Core (flat, no layering) + React, file uploads, state machine | Junior+ | USEFUL (docs/upskill 46) | C SPECIALIZED |
| SubscriptionBillingDashboard (.netstripe) | Desktop\.netstripe | web app / API monorepo | COURSE/GENERATED | .NET8 minimal APIs + React19/Vite6, billing domain | Mid | EXCELLENT (docs/upskill 46 + docs2 47, two curricula) | B HIGH-VALUE |
| .nethris client stub | Desktop\.nethris | empty/stub | UNKNOWN | — | Tiny | NONE | G ARCHIVE |
| eShopOnWeb (.nettodo) | Desktop\.nettodo\eShopOnWeb | reference e-commerce app | OPEN-SOURCE CLONE (dotnet-architecture/eShopOnWeb) | ASP.NET Core, Clean Architecture, Blazor admin | Mid+ | USEFUL (fabledocs 10-dir single generation) | D REFERENCE |

---

## Batch pattern note (read first)

This batch splits cleanly into four families:

1. **The "Net-fleet" of custom domain-clone apps** — netairag, netauth, netdocu, netdrop, netintercom, netlinear, netnotion, netshop, .netramp, .netstripe (10 apps). All are COURSE/GENERATED originals (not real product code, not open-source clones): a small, single-tenant .NET 8 API (mostly `Api -> Application -> Domain -> Infrastructure` layering, MediatR/CQRS-lite, FluentValidation, EF Core + PostgreSQL) paired with a React/TypeScript/Vite frontend, each cloning the shape of a well-known SaaS product (Auth0, DocuSign, Dropbox, Intercom, Linear, Notion, Shopify admin, Ramp/Expensify, Stripe Billing) as a *learning* artifact. Every one of them ships a `docs/upskill/` (or `astraupskill/`, `docs2`, `docs/fable`) curriculum of ~13–47 files generated by the same pipeline (evidently "Fable"/"Astra" tooling per file naming), each with 8 sections: codebase-cartography, stack-and-language-mastery, architecture-and-patterns, code-reading-gym, quality-engineering, contribution-practice, career-and-collaboration, reference. Content sampled (netdrop, netairag) is genuinely project-specific (real file paths + line ranges cited), not generic boilerplate.
   - Only 8 of 10 have single-commit git history (netairag/netauth/netdocu/netdrop/netintercom/netlinear/netnotion/netshop); .netramp and .netstripe are on-disk but not git repos in the same pattern check (actually they ARE — see git log check, single commit each 2026-07-18).
   - `.netramp` and `.netstripe` are noticeably weaker: **zero test files found** in either (`find -iname "*test*"` only turns up doc filenames, no actual `*Test*.cs`/`*.spec.ts`), unlike the other 8 which all have dedicated `tests/` projects (Unit/Integration/E2E in some cases). `.netramp`'s README self-reports "source is complete but has not been compiled/run in this environment" — an explicit unverified-build flag worth preserving as a caveat.
   - `.netramp` also lacks the `Api/Application/Domain/Infrastructure` layering the rest use (flat `backend/Controllers,Domain,Services,...`), and has no dedicated `src/*.Domain` project — a genuine architecture divergence, not just naming.
2. **Verbatim open-source clones with a generated curriculum layered on top** — netcleanarch (CleanArchitecture/jasontaylordev), netopen1 (eShop/dotnet), netopen3 (Umbraco-CMS), netopen5 (jellyfin), nopsolutionsnet (nopCommerce), .netarchitectureproject (modular-monolith-with-ddd/kgrzybek), .netopen2 (OrchardCore/OrchardCMS), .nettodo (eShopOnWeb/dotnet-architecture). All confirmed via `git remote -v` + full genuine upstream commit history (hundreds to tens-of-thousands of real commits, real authors, real dates) — these are **not** hand-modified, they are clean clones with docs added alongside. The added curriculum varies a lot in maturity:
   - **Full multi-generation curricula** (richest): netcleanarch has FOUR generations (`fabledocs/` 9-section, `fabledocs2/` 6-file architecture-notes, `fabledocs3/` 10 ADRs + interview-translation, `fabledocs4/` guided labs + fundamentals primers) — clearly the most-iterated teaching asset in the batch. netopen1/eShop has `fabledocs/` (10-section) + a near-empty `fabledoc2/` stub + a separate, much richer `astra/` tree (12 lessons, 72 numbered ASTRA-### user stories, templates, a `tools/check_course.py` grader) — this is a full course-with-verification, not just reading material.
   - **Single-generation full curricula**: nopsolutionsnet and .nettodo/eShopOnWeb each have one `fabledocs/` 10-section tree.
   - **Bounded "source-based improvement course" exercises** (materially different in kind — NOT a full-codebase curriculum, just one worked bug-fix walkthrough with a guard-clause fix, tests, and a verification record): netopen3/Umbraco, netopen5/jellyfin, .netarchitectureproject each have only a thin `astraupskill/` (7 files) at the *parent* directory (outside the actual clone), and netopen5 additionally has a partial `fabledocs/` (only 2 of 10 sections present — looks incomplete/abandoned).
   - **.netopen2/OrchardCore** stands out: only `AGENTS.md` is genuinely upstream-tracked (confirmed via `git ls-files`); the rest of the agent-tooling (`.agents/skills/`, `CLAUDE.md`, `MCP.md`, `context7.json`, `.mcp.json`) either doesn't exist or is untracked scaffolding. Its `fabledocs/upskill/` (54 files, single generation) is high quality and deeply project-specific (verified sample: exact file/line citations, correct domain vocabulary).
3. **Snapshot-history teaching artifacts** — netsnapshot ("NetAiOps", ops ticket/incident domain) and netsnapshot1 ("Atlas Global Workforce", HR/workforce domain) are NOT duplicates of each other despite structural similarity (both 15 numbered snapshot folders, each a full copy-of-the-codebase-so-far, growing from 19-21 files at `00-walking-skeleton` to 81-106 files at `14-polish-and-docs`). Different domains, different milestone names (e.g. netsnapshot's "05-incidents-and-relationships" vs netsnapshot1's "05-second-entity-relationship"), different stacks (netsnapshot = .NET+React per README implication; netsnapshot1 explicitly "TypeScript/Node backend + React"). Both are explicitly **simulated/non-compiling** teaching fiction ("does not need to compile" / "not a diff").
4. **Pure-docs C#/.NET curricula** — csharptut (24 topic+example file pairs, language fundamentals through EF Core/ASP.NET/testing/capstone), c#interview (phased interview-prep: setup, foundations, portfolio projects, interview phase, 15-file question vault including spot-the-bug and mock screener scripts — consistent with user's memory noting ~490 Q&A already built), csbootcamp (auto-graded exercise bootcamp: `bootcamp/` modules with `progress.cs`/`verify.cs` runner, 31 exercises + 31 solutions across 4 modules so far, plus `cheatsheets/`, `quizzes/`, `FLIGHTPLAN.md`, and its own `astraupskill/` bonus). These three overlap heavily in scope (C# fundamentals) but serve different learning modes: csharptut = read-then-example, csbootcamp = write-and-auto-grade, c#interview = recall-under-pressure — genuine complementary redundancy, not pure duplication.

## netairag — NetAiOps
- Path: Desktop\netairag            - Origin: COURSE/GENERATED
- Type: monorepo (API + React frontend)
- State: working-looking (README says "Phase 1 foundation implemented")     - Size: ~67 .cs + ~20 ts/tsx files, plus 47+18 doc files   - Last modified: 2026-07-18 (single git commit)
- Purpose: Simulated enterprise IT-ops platform: CRUD workflows, RAG over internal runbooks, "autonomous investigation agents," MCP-style mock integrations, an eval harness. Phase 1 only (CRUD + basic ops) is implemented per README.
- Stack: FE React (in `frontend/`); BE .NET8 API layered Api/Application/Domain/Infrastructure (implied by other fleet members, confirmed via `src/Infrastructure/Operations/OperationsService.cs` reference in astraupskill); DB Postgres (implied, docker-compose present); Test `tests/UnitTests`
- Architecture: layered monolith with an "Operations" service performing incident investigation over logs + a lexical retriever (RAG-lite) — no external LLM call confirmed, appears to be a heuristic/mock retrieval implementation
- Complexity: Mid
- Educational material: EXCELLENT — `docs/upskill/` (47 files, 8 sections) + `docs2.0/` (47 files, apparently a **duplicate/second generation of the same 8-section structure** — file lists match exactly, worth diffing before consolidating to avoid keeping two copies) + `astraupskill/` (18 files: single bounded "worked change" exercise on `OperationsService.RunIncidentInvestigationAsync`, verified project-specific via source excerpt). ADR folder (`docs/adr`) and `docs/phases` also present. Preserve — genuinely deep, cite real code.
- Quality observations:
  - Domain/Application separation is real: `LexicalRetriever` explicitly has "no dependency on EF, HTTP, or a model provider" per the astraupskill trace — a deliberate hexagonal boundary.
  - RBAC-flavored guard clause present (`IsAdminOrEngineer` check before incident lookup) — auth-aware application logic, not just CRUD.
  - Test evidence: JSON evaluation fixture is "copied to test output and actually loaded" (per astraupskill notes) — i.e., not a decorative fixture, an actually-exercised one.
  - Only 4 unit test files found by extension scan — test coverage is thin relative to app surface.
  - `docs2.0` appears to duplicate `docs/upskill` — possible redundant regeneration, needs a diff before any cleanup.
- Old-AI-generated smells: none seen in the sampled code/docs; content reads specific and grounded (real method names, real branching logic described accurately).
- Skill tags: be-dotnet, be-rest-design, be-validation, authz-rbac, ai-llm-integration, db-postgres, arch-clean-hex, test-unit, design-docs-adrs
- Duplicate/overlap: part of the 10-app "Net-fleet" (see batch note). Domain overlap with netsnapshot ("NetAiOps" name is reused by netsnapshot's simulated ticket/incident course — likely the seed concept for both, but netairag is a real implemented app while netsnapshot is a fictional/non-compiling teaching history).
- Learning value: High — RAG/agentic-investigation domain is directly relevant to the user's ai-llm-integration interests, plus real RBAC + hexagonal boundaries.
- Transformation opportunity: Could become a genuine small RAG/agent-ops demo if wired to a real LLM call (currently retrieval looks heuristic/lexical only) — a natural "v2" story similar to other apps in the portfolio that got real Astra/Fable review passes.
- Interview stories it could support: "designing a permission-checked investigation service," "separating retrieval logic from EF/HTTP so it's independently testable," "why I kept the sample size separate from the total match count in an evidence UI."
- Proposed disposition: B HIGH-VALUE — solid architecture + deep curriculum, but Phase 1-only completeness and a likely-duplicated docs2.0 folder keep it below flagship.

## netauth — NetAuth0
- Path: Desktop\netauth            - Origin: COURSE/GENERATED
- Type: API + SPA (identity provider)
- State: working-looking     - Size: ~26 .cs + ~14 ts/tsx files, 47+13 doc files   - Last modified: 2026-07-18 (single commit)
- Purpose: Standalone OAuth2/OIDC identity provider — JWT signing, refresh-token rotation, RBAC, MFA, audit logging — explicitly built as a learning project for these primitives.
- Stack: FE React/Vite (`frontend/src/{api,components,pages,routes,styles}`); BE .NET8 Web API layered Api→Application→Domain→Infrastructure (`src/NetAuth0.Application/{Abstractions,Admin,Audit,Common,Identity,OAuth}`); DB Postgres via EF Core; Test `tests/NetAuth0.{IntegrationTests,UnitTests}`
- Architecture: layered monolith, clean-architecture style, explicit OAuth/Identity/Audit module separation
- Complexity: Mid
- Educational material: EXCELLENT — `docs/upskill/` (47 files, 8 sections) + `docs2/` (13 files, second lighter-weight generation). Preserve.
- Quality observations:
  - Explicit module boundaries for Identity vs OAuth vs Audit vs Admin inside Application layer — a real separation-of-concerns choice for an auth domain, not a single God-service.
  - MFA + refresh-token rotation + audit logging are all named directly in README as implemented concerns — auth domain depth beyond basic login/JWT.
  - Both integration and unit test projects exist, appropriate for an auth server (integration tests matter most here).
  - Smallest `.cs` file count (26) of the fleet — likely the leanest/most focused of the ten apps.
- Old-AI-generated smells: none seen in structure; would need a deeper read of token-rotation code to fully rule out weak-auth smells (UNKNOWN / NEEDS DEEPER INSPECTION on rotation correctness specifics).
- Skill tags: authn, authz-rbac, security-owasp, be-dotnet, db-postgres, orm, test-integration
- Duplicate/overlap: Net-fleet member; conceptually the auth building block other fleet apps' "JWT/refresh-token auth" descriptions (netdrop, netlinear, netshop, netintercom) likely each reimplement independently rather than depending on netauth — worth checking whether their auth code duplicates netauth's OAuth module.
- Learning value: High — auth/OIDC/MFA is a strong, concrete interview domain (authn is one of the harder things to explain correctly).
- Transformation opportunity: Could be extracted as a shared auth-service reference the other fleet apps point to, replacing each app's presumably-simpler embedded JWT auth — a good "why we extracted a service" interview story.
- Interview stories it could support: "implementing refresh-token rotation safely," "designing an audit log for identity events," "RBAC vs claims-based authorization tradeoffs."
- Proposed disposition: B HIGH-VALUE — focused, real auth-domain depth, solid curriculum; not flagship only because it's smaller/less feature-complete than netdrop/netintercom/netopen1.

## netdocu — NetDocu
- Path: Desktop\netdocu            - Origin: COURSE/GENERATED
- Type: monorepo (API + React)
- State: working-looking     - Size: ~55 .cs + ~22 ts/tsx files, 47 doc files   - Last modified: 2026-07-18 (single commit)
- Purpose: DocuSign-style e-signature workflow app — envelopes, documents, signing workspace, dashboard.
- Stack: FE React/TS (`frontend/src/{api,components,features,lib,styles}`); BE .NET8 Web API layered, `src/NetDocu.Application/{Auth,Common,Dashboard,Documents,Envelopes}`; DB Postgres/EF Core; Test `tests/NetDocu.Api.IntegrationTests` + `tests/NetDocu.ArchitectureTests` (a dedicated architecture-fitness test project — notable, only one of the fleet observed to have this explicitly named)
- Architecture: clean/layered monolith, Envelope/Document as core domain concepts
- Complexity: Mid
- Educational material: USEFUL — `docs/upskill/` (47 files, 8 sections). No second generation. Preserve.
- Quality observations:
  - Has a dedicated `NetDocu.ArchitectureTests` project — suggests explicit architecture-boundary enforcement (e.g. NetArchTest-style layer dependency rules), a mid-to-senior practice not seen named elsewhere in the fleet listing.
  - README explicitly calls out RFC 7807-style problem responses and JWT/refresh-token auth as implemented concerns.
  - Envelope/signing state machine domain (multi-party signing workflows) is a genuinely nontrivial state-machine problem, good for teaching.
- Old-AI-generated smells: none seen; UNKNOWN whether ArchitectureTests actually enforce anything meaningful without reading the test file directly.
- Skill tags: be-dotnet, be-rest-design, authn, db-postgres, orm, test-integration, arch-clean-hex
- Duplicate/overlap: Net-fleet member; signing-workflow domain is unique in the batch (no other clone of DocuSign).
- Learning value: Medium-High — good state-machine/workflow teaching material, ArchitectureTests is a distinctive artifact worth preserving as a pattern example.
- Interview stories it could support: "modeling a multi-party signing workflow as a state machine," "enforcing architecture boundaries with an automated test."
- Proposed disposition: B HIGH-VALUE — solid, distinctive (ArchitectureTests, signing domain), one curriculum generation only.

## netdrop — NetDropbox
- Path: Desktop\netdrop            - Origin: COURSE/GENERATED
- Type: monorepo (API + React)
- State: working-looking, most-developed of the fleet     - Size: ~55 .cs + 6 ts/tsx files (thin FE relative to BE), 47+23 doc files   - Last modified: 2026-07-19 (astraupskill evidence dir suggests later activity)
- Purpose: Personal/team cloud storage — chunked uploads, versioning, sharing, background processing (dedupe/scan) via a worker.
- Stack: FE React/TS + TanStack Query (`web/` — thin, few files); BE .NET8 API layered `Api/Application/Domain/Infrastructure`, `Application/{Files,Shares,Uploads}`, `Infrastructure/{Persistence,Processing,Services}`; DB Postgres/EF Core; Test `tests/NetDropbox.Tests`
- Architecture: layered monolith + a background `ProcessingWorker` (hosted service) for chunk assembly/dedupe/virus-scan-style processing — closest thing to async-jobs/queue architecture in the fleet
- Complexity: Mid+
- Educational material: EXCELLENT — `docs/upskill/` (47 files) + `astraupskill/` (23 files with `evidence/` and `snapshots/` subfolders — the richest astraupskill instance of any fleet app, suggesting deeper iterative review). Verified sample (`01-system-map.md`, `02-file-reading-order.md`) is precise: exact file+line-range citations, correctly describes upload-chunk idempotency, owner/session checks, dedupe consistency risk across DB/blob/queue, concurrency tokens. Preserve as a strong worked example.
- Quality observations:
  - Explicit "consistency risks across DB, blob storage, and queue" called out in its own file-reading-order doc — the curriculum itself flags a real distributed-consistency teaching seam (likely dual-write / no-outbox pattern).
  - Chunked upload with per-chunk checksum verification, idempotent `StartUploadHandler`, quota boundary check — real production-shaped upload semantics, not toy CRUD.
  - Curriculum explicitly assigns a "learning exercise": find where `UploadsController.Status` leaks query logic back into the API layer — i.e., the docs deliberately preserve a real architectural smell as a teaching seam rather than hiding it.
  - Frontend is comparatively thin (6 ts/tsx files) vs backend depth — likely an admin-lite UI, most of the interesting engineering is server-side.
- Old-AI-generated smells: none seen — curriculum explicitly documents a real leaky-abstraction spot rather than papering over it, which is the opposite of a typical "everything's perfect" AI-generated smell.
- Skill tags: be-dotnet, be-async-jobs, queues, db-postgres, db-transactions, db-concurrency, idempotency, orm, arch-clean-hex, test-unit
- Duplicate/overlap: Net-fleet member; only fleet app with a hosted background worker + chunk/dedupe consistency story — differentiates it from the more purely-CRUD fleet members.
- Learning value: Very High — the DB/blob/queue consistency risk plus chunked-upload idempotency is exactly senior-interview material (distributed consistency, at-least-once processing).
- Transformation opportunity: Fix or explicitly document (as an ADR) the dual-write consistency gap using an outbox pattern — would turn a flagged smell into a concrete "here's how I fixed a real consistency bug" story.
- Interview stories it could support: "why chunked upload assembly needs idempotency," "the dual-write problem across DB/blob/queue and how I'd fix it with an outbox," "finding and documenting a leaky controller."
- Proposed disposition: A FLAGSHIP — most architecturally interesting of the fleet (async worker + real consistency risk + curriculum that honestly documents its own flaw as a teaching seam).

## netintercom — NetIntercom
- Path: Desktop\netintercom            - Origin: COURSE/GENERATED
- Type: monorepo (API + 2 React apps: widget + inbox)
- State: working-looking     - Size: ~61 .cs + ~16 ts/tsx files, 47 doc files   - Last modified: 2026-07-18
- Purpose: Two-sided live chat: embeddable visitor widget + agent inbox, SignalR real-time messaging, inbox routing, SLAs, canned replies, presence.
- Stack: FE two separate React apps (`frontend/widget`, `frontend/inbox`); BE .NET8 API, CQRS-lite with MediatR, FluentValidation, EF Core/Postgres, **Hangfire** (Postgres storage) for background jobs, **SignalR** for realtime, Serilog, OpenTelemetry, JWT+refresh; `Application/{CannedReplies,Conversations,Reports,Routing,Sla,Teams}`
- Architecture: real-time event-driven-ish monolith (SignalR hub + Hangfire jobs for SLA timers/routing), two independent SPA front-ends against one API
- Complexity: Mid+
- Educational material: USEFUL — `docs/upskill/` (47 files, 8 sections), single generation. Preserve.
- Quality observations:
  - Widest tech stack of the fleet: SignalR (realtime-ws), Hangfire (background jobs), OpenTelemetry (observability) all named explicitly in README — most "production infra shaped" of the ten.
  - SLA + routing + canned-replies + presence are genuinely nontrivial support-inbox features (SLA timers alone imply scheduled/background evaluation logic).
  - Two independent frontend apps against one backend is a legitimate multi-client API design exercise.
  - Only 4 test-ish files found by extension scan despite the widest feature surface — test coverage likely thin relative to complexity (flag for deeper inspection).
- Old-AI-generated smells: none seen in structure; UNKNOWN whether SignalR reconnection/presence logic is production-realistic without deeper read.
- Skill tags: realtime-ws, be-async-jobs, queues, observability-metrics-tracing, be-dotnet, db-postgres, arch-event-driven, authz-rbac
- Duplicate/overlap: Net-fleet member; unique in the fleet for realtime + observability + multi-frontend combination.
- Learning value: Very High — SignalR + Hangfire + OpenTelemetry + SLA timers is the richest infra-pattern combination in the batch's custom-app family, strong for "real-time system design" interview prep.
- Transformation opportunity: A deeper test pass (given the feature/test-count mismatch) would turn this into the strongest realtime-systems flagship in the portfolio.
- Interview stories it could support: "building a two-sided real-time chat with SignalR," "SLA timer design with background jobs," "why I split the widget and inbox into separate frontends."
- Proposed disposition: A FLAGSHIP — broadest and most production-infra-shaped stack in the fleet, held back only by thin visible test coverage relative to its complexity.

## netlinear — NetLinear
- Path: Desktop\netlinear            - Origin: COURSE/GENERATED
- Type: monorepo (API + React)
- State: working-looking (README calls it a "scaffold")     - Size: ~47 .cs + ~12 ts/tsx files, 47 doc files   - Last modified: 2026-07-18
- Purpose: Linear/Jira-style issue tracker.
- Stack: FE React/TS (`web/src/api`); BE .NET8 API, `Application/{Issues}` (single-feature-folder — narrower than siblings), MediatR + FluentValidation, `Domain/{Issues,Organizations}`, `Infrastructure/{Notifications,Persistence}`; DB Postgres; Test `tests/NetLinear.Tests`
- Architecture: layered monolith, notification fan-out contracts mentioned in README (`Infrastructure/Notifications`)
- Complexity: Mid
- Educational material: USEFUL — `docs/upskill/` (47 files), single generation.
- Quality observations:
  - README explicitly calls itself a "scaffold" — self-reported lower completeness than netdrop/netintercom.
  - Typed filter compilation + pagination mentioned in README under Application layer — decent query-layer sophistication for an issue list.
  - Notification fan-out contracts present but implementation depth unverified (UNKNOWN — needs deeper inspection to see if it's a real dispatcher or a stub interface).
  - Narrowest Application-layer feature folder set (only `Issues`) of the fleet apps sampled — likely the least feature-complete.
- Old-AI-generated smells: none seen structurally; "scaffold" self-label is an honest completeness signal rather than a smell.
- Skill tags: be-dotnet, db-postgres, be-validation, db-modeling
- Duplicate/overlap: Net-fleet member; same "issue tracker" domain family as netsnapshot's ticket-tracking teaching app and the user's broader portfolio (Tracer/gitjira per memory) — likely redundant with more complete issue-tracker clones elsewhere in the archive (out of scope for this batch, flag for cross-batch dedup).
- Learning value: Medium — decent CQRS/filter-pagination example but self-described as a scaffold, so less complete than peers.
- Interview stories it could support: "typed filter compilation for a query API," "designing notification fan-out contracts."
- Proposed disposition: B HIGH-VALUE — solid pattern demo, but explicitly the least mature of the fleet by its own README.

## netnotion — NetNotion
- Path: Desktop\netnotion            - Origin: COURSE/GENERATED
- Type: monorepo (API + React)
- State: working-looking     - Size: ~83 .cs (largest backend in the fleet) + ~12 ts/tsx files, two doc trees (47 + 8 files)   - Last modified: 2026-07-18
- Purpose: Notion-style collaborative docs/wiki — blocks, comments, workspaces.
- Stack: FE React/TS (`client/src/{api,components,features,routes,styles}`); BE .NET8 API, `Application/{Auth,Blocks,Comments,Common}`, custom `Api/{Auth,Middleware,Responses}`; DB Postgres; Test `tests/NetNotion.{E2ETests,IntegrationTests,UnitTests}` — the only fleet app confirmed with all three test tiers (unit+integration+E2E) as named projects
- Architecture: layered monolith, block-based document model (tree/recursive content structure implied by "Blocks" module)
- Complexity: Mid
- Educational material: USEFUL, TWO generations — `docs/upskill/` (47 files, standard 8-section) AND `docs/fable/` (8 files: fast-track, codebase-map, stack-mental-models, architecture-tour, code-reading-gym, quality-engineering, practice-tickets) — a differently-branded but overlapping curriculum, worth diffing/consolidating.
- Quality observations:
  - Largest `.cs` file count in the fleet (83) — block/tree document modeling (Notion-style nested blocks) is inherently more complex than flat CRUD domains like NetShopifyLite or NetLinear.
  - Only fleet app with all three test tiers (unit/integration/E2E) as explicitly separate projects — a genuine testing-maturity differentiator.
  - Custom `Api/Middleware` and `Api/Responses` folders (vs siblings' simpler Api layer) suggest bespoke error/response handling rather than generic ASP.NET defaults.
  - Two parallel curriculum trees (`docs/upskill` vs `docs/fable`) risk drift/duplication — needs reconciliation before any "final" curriculum designation.
- Old-AI-generated smells: none seen structurally.
- Skill tags: be-dotnet, db-postgres, test-e2e, test-integration, test-unit, be-error-handling, db-modeling
- Duplicate/overlap: Net-fleet member; two parallel curricula (`upskill` vs `fable`) within the same project is unique to netnotion in this batch — flag for consolidation.
- Learning value: High — recursive block-document modeling + full test-tier coverage is a good structural-data + testing-maturity example.
- Interview stories it could support: "modeling a recursive block/document tree," "structuring unit vs integration vs E2E test tiers for a CRUD-heavy app."
- Proposed disposition: B HIGH-VALUE — most structurally complex + best test-tier coverage of the pure-CRUD fleet members, docked slightly for the duplicate curriculum trees.

## netshop — NetShopifyLite
- Path: Desktop\netshop            - Origin: COURSE/GENERATED
- Type: monorepo (API + React)
- State: working-looking     - Size: ~42 .cs + 4 ts/tsx files (thinnest FE in the fleet), 47 doc files   - Last modified: 2026-07-18
- Purpose: E-commerce admin + lightweight storefront scaffold.
- Stack: FE React (`frontend/src` — very thin, 4 files); BE .NET8 API, `Application/{Carts,Catalog,Common,Dashboard,Orders}`, `Domain/{Catalog,Common,Customers,Inventory,Sales,ValueObjects}` (richest Domain-layer module breakdown in the fleet, including explicit ValueObjects); DB Postgres; Test `tests/NetShopifyLite.{IntegrationTests,UnitTests}`
- Architecture: layered monolith, richest domain-modeling surface (Inventory + Sales + Customers + ValueObjects as separate concerns) despite a thin frontend
- Complexity: Mid
- Educational material: USEFUL — `docs/upskill/` (47 files), single generation.
- Quality observations:
  - Domain layer explicitly separates `ValueObjects` from entities — one of few fleet apps to name this DDD pattern directly in its folder structure (Money/SKU-style value objects likely).
  - Inventory + Sales + Customers as separate Domain subfolders suggests genuine bounded-context thinking for an e-commerce domain (stock vs order vs customer).
  - Frontend is the thinnest in the fleet (4 files) — likely just enough for demoing, not a full storefront UI.
- Old-AI-generated smells: none seen structurally.
- Skill tags: be-dotnet, db-modeling, db-postgres, db-transactions, orm
- Duplicate/overlap: Net-fleet member; domain overlaps with any other e-commerce/inventory projects elsewhere in the user's archive (cross-batch check recommended — user's memory references multiple grokbuild*/ecommerce projects).
- Learning value: Medium-High — value-object modeling and bounded Inventory/Sales/Customer separation are good DDD teaching material even with a thin UI.
- Interview stories it could support: "modeling money/SKU as value objects," "separating inventory, sales, and customer bounded contexts."
- Proposed disposition: B HIGH-VALUE — strong domain modeling, weak/thin frontend keeps it below flagship.

## CleanArchitecture (netcleanarch)
- Path: Desktop\netcleanarch\CleanArchitecture            - Origin: OPEN-SOURCE CLONE (jasontaylordev/CleanArchitecture, verified via `git remote -v`)
- Type: library/template (NuGet solution template) — API + Blazor client + Angular/React alt-frontends per the template's convention
- State: complete, production-like reference template     - Size: large (930 real upstream commits)   - Last modified: upstream commit 2026-04-13 (renovate dependency bump — actively maintained upstream)
- Purpose: The widely-used "Clean Architecture" ASP.NET Core solution template by Jason Taylor — reference implementation of Clean Architecture / CQRS-with-MediatR for .NET, distributed as a `dotnet new` template.
- Stack: .NET, MediatR, FluentValidation, EF Core, `Directory.Packages.props` central package management, Renovate-managed dependency bot, NuGet template packaging (`CleanArchitecture.nuspec`), `.devcontainer`, `.aspire`
- Architecture: textbook Clean Architecture (Domain/Application/Infrastructure/Web) with CQRS-lite via MediatR
- Complexity: Production-like
- Educational material: EXCELLENT — FOUR distinct curriculum generations at the repo root: `fabledocs/` (9 sections incl. interview-prep), `fabledocs2/` (6 files: architecture, API design, data access, testing strategy, error handling, observability), `fabledocs3/` (10 numbered ADRs — e.g. adr-004 "EFCore in Application, no repository," adr-009 "in-process pre-commit domain events," adr-010 "schema by convention, no migrations" — plus an interview-translation doc), `fabledocs4/` (5 guided labs: first change, add a field, validation and errors, first tests, fix a real bug — plus 5 fundamentals primers: DI, async/await, web auth, what a transaction is, HTTP/REST). This is the most-iterated curriculum in the entire batch — clearly used as a flagship teaching vehicle multiple times. Preserve all four generations; fabledocs3's ADR set in particular is uniquely valuable (reverse-engineered architecture decisions with interview translation).
- Quality observations:
  - Real, actively-maintained upstream project (Renovate bot commits through 2026-04) — this is genuine production-grade reference code, not a toy.
  - ADR set (fabledocs3) directly documents real architectural choices like "no repository pattern, EF Core used directly in Application layer" and "no migrations, schema by convention" — both are debatable/controversial choices worth discussing in interviews.
  - Guided labs (fabledocs4) are structured as hands-on exercises ("fix a real bug") rather than passive reading — the most exercise-oriented of any curriculum generation seen in this batch.
  - `.aspire` presence suggests the template has been updated for .NET Aspire orchestration — current/modern tooling.
- Old-AI-generated smells: none in the base app (real upstream code); curriculum layers are well-differentiated by purpose rather than redundant duplicates, unlike some Net-fleet apps' overlapping doc trees.
- Skill tags: arch-clean-hex, be-dotnet, be-rest-design, design-docs-adrs, test-unit, ci-cd, deploy
- Duplicate/overlap: Conceptually related to the Net-fleet apps' own Api/Application/Domain/Infrastructure layering (they likely borrowed this template's pattern) and to .netarchitectureproject's modular-monolith-with-ddd (both are canonical .NET architecture references, but DDD-modular-monolith vs Clean-Architecture-CQRS are different schools worth contrasting).
- Learning value: Very High — most mature, most-iterated curriculum in the batch, real production template.
- Transformation opportunity: Use fabledocs3's ADR set as a template for writing ADRs on the user's OWN original apps (the Net-fleet) which currently lack ADR-style docs.
- Interview stories it could support: "why Clean Architecture puts EF Core in Application, not behind a repository," "schema-by-convention vs migrations tradeoffs," "domain events fired pre-commit vs post-commit."
- Proposed disposition: A FLAGSHIP — richest, most-iterated curriculum + genuine production-grade reference architecture.

## eShop (netopen1)
- Path: Desktop\netopen1\eShop            - Origin: OPEN-SOURCE CLONE (dotnet/eShop, verified via `git remote -v`, 342 real commits)
- Type: monorepo (microservices)
- State: complete, production-like reference     - Size: large   - Last modified: upstream 2026-04-21
- Purpose: Microsoft's official .NET microservices reference e-commerce app (successor to eShopOnContainers) — catalog, ordering, basket, identity as separate services, orchestrated via .NET Aspire.
- Stack: .NET Aspire orchestration, Blazor web frontend, gRPC inter-service calls, RabbitMQ-style EventBus, PostgreSQL, Redis, Playwright e2e (`e2e/`, `playwright.config.ts`), Spectral API linting (`.spectral.yml`)
- Architecture: microservices, event-driven (EventBus), API gateway pattern
- Complexity: Senior-oriented
- Educational material: EXCELLENT and unusually rich — THREE layers: `fabledocs/` (10-section, includes interview-prep), a near-empty `fabledoc2/` (just a README stub, likely an abandoned second attempt), and a substantial independent `astra/` tree: `00-onboarding/` (4 files: first-day, environment, run-and-debug, first-contribution), `01-lessons/` (12 lessons from codebase-map through capstone, covering Blazor, HTTP contracts, basket/state, data/domain, testing strategy, identity/security, events/consistency, debugging/observability, design/delivery), `02-stories/` (**72 numbered ASTRA-### user stories** — the largest single exercise set found in this batch), `03-reference/` (assessment, commands, glossary, troubleshooting, verification), `04-templates/` (7 templates incl. ADR, debugging-journal, incident, PR, review, user-story), plus `PROGRESS.md`, `CURRICULUM.md`, and a `tools/check_course.py` grading script. This is a full course-with-automated-verification, not just reading material.
- Quality observations:
  - Real Microsoft reference microservices app — directly relevant to "how do you design microservices" interview questions with genuine event-driven consistency concerns (EventBus).
  - 72-story ASTRA curriculum with a Python verification tool (`check_course.py`) is the most rigorous, most exercise-driven curriculum construct in the entire batch — worth deep-diving as a template for future curriculum generation elsewhere in the archive.
  - `fabledoc2/` being nearly empty (1 README stub) suggests an abandoned/superseded generation attempt — safe to prune/ignore in favor of `astra/`.
  - Playwright e2e config present at repo root — real e2e test tooling, not just unit tests.
- Old-AI-generated smells: none in the base app; the `astra/` curriculum's scale (72 stories) means quality could vary story-to-story — recommend spot-checking a sample of ASTRA-### files before treating all 72 as uniformly high quality (NEEDS DEEPER INSPECTION for full confidence, only spot-checked structure not content here).
- Skill tags: arch-microservices, arch-event-driven, queues, db-postgres, caching, test-e2e, design-docs-adrs, cloud-azure (Aspire), incident-debugging
- Duplicate/overlap: Domain overlap with .nettodo's eShopOnWeb — both are Microsoft e-commerce reference apps but eShop (this one) is the microservices/Aspire successor while eShopOnWeb is the earlier monolithic Clean Architecture reference. Good "compare monolith vs microservices for the same domain" teaching pair.
- Learning value: Very High — richest curriculum construct in the batch (72-story graded course) + genuine microservices/event-driven architecture.
- Transformation opportunity: The `astra/tools/check_course.py` grading pattern is worth extracting as a reusable template for auto-grading curricula on the user's other original (Net-fleet) apps.
- Interview stories it could support: "microservices vs monolith tradeoffs (paired with eShopOnWeb)," "event-driven consistency across Catalog/Ordering/Basket," "using .NET Aspire for local service orchestration."
- Proposed disposition: A FLAGSHIP — best-verified, most rigorous curriculum in the batch (auto-graded 72-story course) on top of a genuine senior-level microservices reference app.

## Umbraco-CMS (netopen3)
- Path: Desktop\netopen3\Umbraco-CMS            - Origin: OPEN-SOURCE CLONE (umbraco/Umbraco-CMS, verified via `git remote -v`, 72,389 real commits — by far the largest history in the batch)
- Type: CMS platform (huge multi-project solution)
- State: complete, production-like     - Size: very large   - Last modified: upstream 2026-07-16
- Purpose: Umbraco, a mature open-source ASP.NET Core CMS, cloned wholesale.
- Stack: .NET, large multi-project CMS solution, `.claude/`, `.mcp.json`, `context7.json` present at repo root (agent-tooling config, likely upstream-shipped given Umbraco's active AI-agent support — UNKNOWN whether tracked or added, not verified with git ls-files for this repo)
- Architecture: modular CMS platform (content types, templates, backoffice admin)
- Complexity: Production-like
- Educational material: MINIMAL for this batch's purposes — the `astraupskill/` folder lives at the *parent* `netopen3/` level (outside the actual clone) and is NOT a full-codebase curriculum but a single **bounded "source-based improvement course"**: one worked change (a template-order regression per `scripts/template-order-tests`), with CODEBASE-MAP/CONCEPTS/WORKED-CHANGE/TESTING-AND-DEBUGGING/PRACTICE/SOLUTIONS-AND-REVIEW/TRACE-LAB files plus `evidence/` and `snapshots/`. Root README explicitly frames it as "Source-based improvement course — trace requested-ID selection, stable hydration ordering, duplicate policy, and empty-page regressions." Genuinely project-specific but narrow in scope (one bug-fix trace, not the whole CMS).
- Quality observations:
  - Massive real commit history (72k+) — this is one of the most mature, real production open-source projects in the entire archive; excellent for "reading a large unfamiliar codebase" practice.
  - The astraupskill exercise targets a concrete regression class (ID selection / hydration ordering / duplicate handling / empty pages) — realistic bug categories, not contrived.
  - `scripts/template-order-tests` at the netopen3 parent level suggests a specific verification harness was built for this one exercise.
  - No full curriculum comparable to netcleanarch/eShop — this is thin relative to the size/complexity of the underlying codebase.
- Old-AI-generated smells: none seen; base app is real upstream code.
- Skill tags: legacy-codebase-reading, incident-debugging, perf-investigation, be-dotnet, code-review
- Duplicate/overlap: Same "huge real OSS codebase + one bounded exercise" pattern as netopen5/jellyfin and .netarchitectureproject — these three share a lighter-weight curriculum style distinct from netcleanarch/eShop/OrchardCore's fuller curricula.
- Learning value: Medium — valuable for reading-a-huge-unfamiliar-codebase practice and one concrete debugging exercise, but thin teaching material relative to the codebase's actual size/complexity.
- Interview stories it could support: "diagnosing a hydration-ordering regression in a large legacy codebase," "reading an unfamiliar 70k-commit codebase efficiently."
- Proposed disposition: C SPECIALIZED — valuable as a "large legacy codebase" reading exercise and one debugging story, not developed enough to be a flagship teaching asset on its own.

## jellyfin (netopen5)
- Path: Desktop\netopen5\jellyfin            - Origin: OPEN-SOURCE CLONE (jellyfin/jellyfin, verified via `git remote -v`, 29,332 real commits)
- Type: media server platform (huge multi-project solution)
- State: complete, production-like     - Size: very large   - Last modified: upstream 2026-07-15
- Purpose: Jellyfin, an open-source Netflix/Plex-style media server, cloned wholesale.
- Stack: .NET, huge multi-project (Emby.*, Jellyfin.*, MediaBrowser.* namespaces — legacy Emby fork lineage visible in project names), fuzz testing (`fuzz/`)
- Architecture: modular media server (library scanning, transcoding, API, plugin system)
- Complexity: Production-like
- Educational material: MINIMAL/inconsistent — `fabledocs/` at repo root has only 2 of the standard 10 sections present (`00-fast-track.md` and `09-reference`) plus a README — looks abandoned mid-generation. The real teaching content is `astraupskill/` at the *parent* `netopen5/` level (same bounded-exercise pattern as netopen3/Umbraco): one worked change on the "latest media" API endpoint's limit-parameter validation (rejecting zero/negative/overflow-prone limits before hitting the library/user layer), with a full CODEBASE-MAP/CONCEPTS/WORKED-CHANGE/TESTING/PRACTICE/SOLUTIONS/TRACE-LAB set.
- Quality observations:
  - The astraupskill exercise is a genuinely well-chosen bug class: an unvalidated caller-supplied integer limit that can overflow downstream arithmetic (`int.MaxValue / 2` boundary) — a real, specific, correctly-reasoned security/correctness issue, not a generic example.
  - `fuzz/` directory in the real jellyfin codebase — good evidence this is a security-conscious, mature OSS project worth reading for hardening patterns.
  - `fabledocs/` being only 2/10 sections is an incomplete/abandoned generation — should either be finished or removed to avoid confusing future navigation.
  - Namespace legacy (`Emby.*` alongside `Jellyfin.*`) is itself an interesting "reading a forked/renamed codebase" exercise.
- Old-AI-generated smells: none in the base app; the incomplete fabledocs/ is a generation-process gap, not a content-quality smell.
- Skill tags: legacy-codebase-reading, security-owasp, perf-investigation, be-dotnet, be-validation, incident-debugging
- Duplicate/overlap: Same pattern family as netopen3/Umbraco and .netarchitectureproject (huge real OSS + thin/bounded astraupskill exercise).
- Learning value: Medium — the one worked bug-fix (integer overflow via unvalidated limit param) is a genuinely good, specific interview story; broader curriculum is incomplete.
- Interview stories it could support: "finding and fixing an integer-overflow-via-unvalidated-limit bug in a real API controller," "reading a codebase with legacy naming from a historical fork."
- Proposed disposition: C SPECIALIZED — one good bounded bug-fix story, incomplete broader curriculum (fabledocs abandoned at 20%).

## nopCommerce (nopsolutionsnet)
- Path: Desktop\nopsolutionsnet\nopCommerce            - Origin: OPEN-SOURCE CLONE (nopSolutions/nopCommerce, verified via `git remote -v`, 16,115 real commits)
- Type: e-commerce platform (huge multi-project solution)
- State: complete, production-like     - Size: very large   - Last modified: upstream 2026-07-10
- Purpose: nopCommerce, a mature open-source ASP.NET Core e-commerce platform, cloned wholesale, with Docker (MySQL and PostgreSQL compose variants) and upgrade-scripts tooling.
- Stack: ASP.NET Core, MySQL or PostgreSQL (both docker-compose variants shipped), plugin architecture, `upgradescripts/`
- Architecture: modular monolith e-commerce platform with plugin system
- Complexity: Production-like
- Educational material: USEFUL — single-generation `fabledocs/` (10-section, same structure as netcleanarch's fabledocs and eShop's fabledocs: cartography through interview-prep + reference). Not yet spot-read for content quality in this pass (UNKNOWN / NEEDS DEEPER INSPECTION on genericness vs project-specificity — the structural pattern matches the high-quality netdrop/OrchardCore samples verified elsewhere in this batch, so likely similarly project-specific, but not directly confirmed for this repo).
- Quality observations:
  - Real, large, actively-developed e-commerce platform — directly comparable domain to netshop (NetShopifyLite) for a "toy vs real" e-commerce architecture comparison.
  - Dual-database docker-compose (MySQL and Postgres) is a good example of DB-portability design worth reading.
  - `upgradescripts/` directory suggests real schema-migration/versioning practices across major versions — valuable zero-downtime-migration reading material.
- Old-AI-generated smells: none seen; base app is real upstream code, curriculum not deeply sampled.
- Skill tags: db-migrations, db-sqlserver (mssql supported upstream), be-dotnet, docker, zero-downtime-migration, legacy-codebase-reading
- Duplicate/overlap: Domain overlap with netshop (NetShopifyLite, the fleet's toy e-commerce app) — a good "toy vs real" comparison pair.
- Learning value: Medium-High — real e-commerce platform with genuine migration/versioning history, single solid curriculum generation.
- Interview stories it could support: "how a mature e-commerce platform handles cross-database portability," "reading real schema upgrade scripts across major versions."
- Proposed disposition: C SPECIALIZED — solid single curriculum generation on a real, large e-commerce reference; not as deeply iterated as netcleanarch/eShop/OrchardCore.

## modular-monolith-with-ddd (.netarchitectureproject)
- Path: Desktop\.netarchitectureproject\modular-monolith-with-ddd            - Origin: OPEN-SOURCE CLONE (kgrzybek/modular-monolith-with-ddd, verified via `git remote -v`, 330 real commits)
- Type: reference DDD/CQRS modular monolith
- State: complete, reference-quality     - Size: medium   - Last modified: upstream 2024-04-20 (oldest upstream last-commit date in this batch — less actively maintained than the others)
- Purpose: Kamil Grzybek's widely-cited reference implementation of a modular monolith using DDD, CQRS, and module-per-bounded-context — a canonical .NET architecture teaching repo in its own right (independent of this archive's curriculum layer).
- Stack: .NET, NUKE build automation (`.nuke/`), Azure Pipelines CI, Docker Compose, module-per-business-capability structure (`src/`)
- Architecture: modular monolith, DDD tactical patterns, CQRS, module boundaries enforced at the solution level
- Complexity: Senior-oriented
- Educational material: MINIMAL as packaged here — the `astraupskill/` (7 files, same CODEBASE-MAP/CONCEPTS/WORKED-CHANGE/... structure as netopen3/netopen5) lives at the *parent* `.netarchitectureproject/` level, kept deliberately separate from the actual clone directory (unlike netopen3/netopen5 where the parent-level pattern is consistent, this one is explicitly the only place holding curriculum since the repo itself has zero added docs). One bounded worked-change exercise, not a full curriculum.
- Quality observations:
  - This repo is already a canonical, widely-referenced .NET architecture teaching resource on its own merits — even without any added curriculum, it's directly valuable as a reference to read (module boundaries, DDD tactical patterns, integration-events-between-modules).
  - Least recently updated upstream (2024-04-20) — may be missing 1.5+ years of .NET ecosystem changes (framework version, NuGet updates) relative to the other clones in this batch, worth flagging if used as a "current best practice" reference.
  - NUKE + Azure Pipelines CI setup is a good example of build-automation-as-code, distinct from the simpler `docker-compose.yml`-only setups in the Net-fleet apps.
- Old-AI-generated smells: none seen; genuine long-standing reference project.
- Skill tags: arch-modular-monolith, design-docs-adrs, arch-event-driven, ci-cd, be-dotnet, db-transactions
- Duplicate/overlap: Same "canonical .NET architecture reference" role as netcleanarch/CleanArchitecture, but representing the competing DDD-modular-monolith school vs Clean-Architecture-CQRS — valuable as a direct architectural-philosophy contrast pair.
- Learning value: High — as a reference architecture on its own merits (module boundaries, DDD), even with minimal added curriculum.
- Transformation opportunity: A fuller fabledocs-style curriculum here (paired explicitly against netcleanarch's) would make an excellent "compare two competing .NET architecture philosophies" teaching set.
- Interview stories it could support: "modular monolith vs microservices vs clean architecture — when I'd choose each," "enforcing module boundaries without full microservice overhead."
- Proposed disposition: D REFERENCE — valuable as a real, canonical architecture reference to point to/read, under-invested in curriculum relative to its teaching potential.

## OrchardCore (.netopen2)
- Path: Desktop\.netopen2\OrchardCore            - Origin: OPEN-SOURCE CLONE (OrchardCMS/OrchardCore, verified via `git remote -v`, 9,667 real commits)
- Type: modular multi-tenant CMS/application framework
- State: complete, production-like     - Size: very large (~200 projects per its own docs)   - Last modified: upstream 2026-07-16
- Purpose: Orchard Core, a modular, multi-tenant ASP.NET Core CMS/application framework — cloned wholesale, with genuinely upstream-shipped `AGENTS.md` (confirmed via `git ls-files`) documenting how LLM agents should work in the codebase, plus locally-added `fabledocs/`.
- Stack: .NET10, Yarn4 frontend asset pipeline, ~200-project solution across three tiers (host apps, framework, modules), multi-tenant shell architecture
- Architecture: modular, multi-tenant (per-tenant shell/container isolation), plugin/module system
- Complexity: Production-like
- Educational material: EXCELLENT — `fabledocs/upskill/` (54 files total, single generation but the most files of any single-generation curriculum in the batch, covering `adrs/` plus the standard 01-09 sections incl. interview-prep). Directly verified for quality: `01-system-map.md` correctly describes the 3-tier ~200-project structure and Yarn4 asset pipeline; `02-file-reading-order.md` gives a 28-file reading order split into Junior (1-14) / Mid (1-22) / Senior (all) paths with specific "why it matters / look for / ignore" guidance per file — genuinely didactic, not just a file list; `03-domain-glossary.md` correctly defines "Tenant" with exact code citation (`ShellSettings.cs:9-13`) and correctly distinguishes it from near-synonym confusion terms. This is some of the highest-quality, most pedagogically deliberate curriculum content sampled in this entire batch.
- Quality observations:
  - Confirmed via `git ls-files` that only `AGENTS.md` is genuinely upstream; the CLAUDE.md/MCP.md/context7.json files initially suspected did not actually exist in this clone (verified — they returned "No such file" on direct check), so no confusion between upstream and added agent-tooling files.
  - The multi-tenant, per-shell-container architecture is a genuinely advanced (senior-level) architectural pattern, well-suited for multitenancy interview questions.
  - Curriculum's graduated Junior/Mid/Senior reading paths (with explicit "ignore" guidance, e.g. "ignore NLog" for a first-day file) shows deliberate instructional design, not a flat file dump.
  - ~200-project solution size is itself a "navigating a huge real codebase" exercise independent of the curriculum.
- Old-AI-generated smells: none seen — curriculum content is specific, accurate, and cites real code with correct line numbers.
- Skill tags: multitenancy, arch-modular-monolith, legacy-codebase-reading, design-docs-adrs, be-dotnet, ci-cd
- Duplicate/overlap: Only true multi-tenant CMS clone in the batch — no direct overlap with netopen3 (Umbraco, also a CMS, but not verified multi-tenant in this pass) beyond both being ASP.NET Core CMS platforms; worth a "CMS architecture comparison" pairing with Umbraco.
- Learning value: Very High — best-verified curriculum quality in the batch, genuinely advanced multitenancy architecture.
- Transformation opportunity: The graduated Junior/Mid/Senior reading-path pattern used here is worth extracting as a template for improving the thinner curricula elsewhere in this batch (e.g. netopen3/netopen5's minimal astraupskill exercises).
- Interview stories it could support: "how per-tenant shell isolation works in a multi-tenant ASP.NET Core app," "navigating and onboarding into a 200-project real codebase."
- Proposed disposition: A FLAGSHIP — highest directly-verified curriculum quality in the batch, on a genuinely advanced multi-tenant architecture reference.

## ExpenseManagement (.netramp)
- Path: Desktop\.netramp            - Origin: COURSE/GENERATED
- Type: monorepo (API + React)
- State: working-looking but **self-flagged unverified**: README states "the source is complete but has not been compiled/run in this environment"     - Size: ~28 .cs files, 0 ts/tsx counted by extension scan (frontend exists but wasn't picked up by the ts/tsx glob — likely .jsx/.js, needs confirmation), 46 doc files   - Last modified: 2026-07-18
- Purpose: A learning-oriented clone of Ramp/Expensify/Brex expense workflows — file uploads, validation, background processing, a state machine, security, reporting, explicitly built "with a deliberately small dependency footprint."
- Stack: ASP.NET Core (flat structure: `backend/{Background,Controllers,Domain,Dtos,Middleware,Properties,Security,Services,Storage}` — no separate Application/Infrastructure projects, unlike every other fleet app); React frontend (`frontend/src/{api,auth,components,pages,util}`)
- Architecture: single-project layered-by-folder monolith (not multi-project clean architecture like its siblings) — an intentional "small footprint" divergence per its own README
- Complexity: Junior+
- Educational material: USEFUL — `docs/upskill/` (46 files, same 8-section structure), including explicit `05-quality-engineering/{01-testing-strategy.md, 02-writing-tests-here.md}` files.
- Quality observations:
  - **No actual test files found anywhere in the project** (`find -iname "*test*"` only returns the two doc-content filenames about testing strategy — there is no `Tests/` project or `*.spec.*` file) despite the curriculum having dedicated "writing tests here" guidance — a real gap between documented intent and actual code.
  - README's own unverified-build disclosure is an honest and useful caveat to preserve — this project should not be presented as "known working" without a compile check first.
  - Deliberately single-project (no Application/Domain/Infrastructure split) — a legitimate simpler alternative architecture worth contrasting against the fleet's Clean-Architecture default, but also could read as under-designed for the stated feature scope (state machine, background processing, security).
  - Expense-approval state machine + background processing + file uploads is a reasonably rich feature set for a flat single-project structure to carry.
- Old-AI-generated smells: **zero tests despite testing-strategy docs existing** is a notable AI-generated-project smell (docs describing testing without actual tests being written) — flag explicitly. Also unverified build status is itself a smell pattern worth tracking across the archive.
- Skill tags: be-dotnet, be-async-jobs, db-sql-raw (likely, unconfirmed ORM choice), config-secrets, security-owasp
- Duplicate/overlap: Net-fleet member; only fleet app confirmed to lack a multi-project clean-architecture split.
- Learning value: Medium — decent domain (expense workflows/state machine) but real doubts about whether it compiles/runs and a confirmed test-coverage gap.
- Interview stories it could support: "designing an expense-approval state machine" (with the caveat that this specific implementation is unverified).
- Proposed disposition: C SPECIALIZED — needs a compile/run + test-writing pass before it can be trusted as a portfolio piece; useful now mainly as a state-machine design reference, not as "working code."

## SubscriptionBillingDashboard (.netstripe)
- Path: Desktop\.netstripe            - Origin: COURSE/GENERATED
- Type: monorepo (minimal API + React)
- State: working-looking     - Size: ~14 .cs + 4 ts/tsx files (smallest backend file count in the whole batch, though likely fewer/larger files not necessarily less code), 46+47 doc files   - Last modified: 2026-07-18
- Purpose: A Stripe Billing/Chargebee-style subscription billing dashboard — customers, plans, subscriptions, coupons, invoices, usage events, webhooks; money stored as integer minor units to avoid float drift.
- Stack: .NET8 **minimal APIs** (not MVC controllers, unlike most of the fleet) + React19/Vite6 SPA; `src/Billing.Api/{Contracts,Domain,Infrastructure,Properties}` (flatter than the Application/Domain/Infrastructure/Api 4-project split used elsewhere — Domain lives inside the Api project itself)
- Architecture: single-project minimal-API monolith with an internal Domain/Infrastructure folder split (not separate projects); explicitly named idempotency + webhook-verification + background-worker concerns per curriculum
- Complexity: Mid
- Educational material: EXCELLENT — TWO curriculum generations: `docs/upskill/` (46 files, standard 8-section) AND `docs2/` (47 files, same 8-section structure but independently numbered "01.01", "01.02" style headers — verified sample shows genuinely detailed, accurate system-map content: correctly notes ".sln contains ONLY Billing.Api — the web app is on disk, not in the .sln", a real and specific observation about the actual solution file, not generic boilerplate).
- Quality observations:
  - Money-as-integer-minor-units is a correct, specific billing-domain best practice explicitly called out — good evidence of real domain knowledge embedded in the app, not generic CRUD.
  - Curriculum correctly identifies a real oddity (Billing.Web not included in the .sln) — this is either a genuine project-setup gap or an intentional "the SPA builds independently" choice; either way the docs caught and explained it rather than glossing over it.
  - **No actual test files found** (`find -iname "*test*"` returns nothing but the two testing-strategy doc filenames) — same test-coverage gap pattern as .netramp, despite curriculum discussing quality-engineering.
  - Minimal-API style (vs MVC controllers) is architecturally distinct from the rest of the fleet — good contrast example for "minimal APIs vs controller-based APIs" discussions.
- Old-AI-generated smells: same test-coverage gap noted for .netramp — testing-strategy docs exist, but no test project/files found in the source tree.
- Skill tags: be-dotnet, idempotency, security-owasp (webhook verification), db-modeling, be-rest-design
- Duplicate/overlap: Net-fleet member; only fleet app using minimal APIs instead of MVC controllers; billing domain overlaps conceptually with any Stripe-integration work elsewhere in the user's archive (cross-batch check recommended).
- Learning value: High — correct money-handling domain knowledge (integer minor units) + webhook/idempotency concerns are genuinely valuable billing-system interview material, docked for missing tests.
- Transformation opportunity: Writing the missing test suite (idempotency-key handling and webhook-signature verification tests especially) would turn this into a strong "payments correctness" portfolio piece.
- Interview stories it could support: "why money should be stored as integer minor units," "designing idempotent webhook handlers for a billing system."
- Proposed disposition: B HIGH-VALUE — strong domain correctness and two curriculum generations, held back by a confirmed test-coverage gap.

## .nethris client stub
- Path: Desktop\.nethris            - Origin: UNKNOWN (no source files present to classify)
- Type: empty/stub
- State: skeleton     - Size: 0 files found under `.nethris/client` (directory exists but is empty of countable files)   - Last modified: 2026-06-09 (dir mtime; no git repo to date more precisely)
- Purpose: UNKNOWN / NEEDS DEEPER INSPECTION — name suggests an HR-information-system (HRIS) clone intended to join the Net-fleet (paralleling .netramp/.netstripe naming), but only an empty `client` subfolder exists; no backend, no docs, no code.
- One-line record only per brief's tiny/empty rule: an abandoned or never-started HRIS-clone stub — the only truly empty candidate in this batch.
- Proposed disposition: G ARCHIVE — nothing to preserve; safe to delete or leave as a placeholder if the user intends to eventually build "NetHRIS" as an 11th fleet member.

## eShopOnWeb (.nettodo)
- Path: Desktop\.nettodo\eShopOnWeb            - Origin: OPEN-SOURCE CLONE (dotnet-architecture/eShopOnWeb, verified via `git remote -v`, 825 real commits)
- Type: reference e-commerce app (monolith + separate Blazor admin)
- State: complete, reference-quality     - Size: medium   - Last modified: upstream 2025-01-13
- Purpose: Microsoft's earlier reference e-commerce app demonstrating Clean Architecture principles in a simpler, monolithic (non-microservices) form — the predecessor concept to netopen1/eShop's microservices approach.
- Stack: ASP.NET Core, EF Core, Azure deployment config (`azure.yaml`, `infra/`), Docker Compose, code-coverage tooling (`CodeCoverage.runsettings`), a Blazor admin app alongside the main web app (`Everything.sln` vs `eShopOnWeb.sln` suggests two solution scopes)
- Architecture: Clean Architecture monolith (single deployable, layered internally) — direct architectural contrast to netopen1/eShop's microservices approach on the *same* e-commerce domain
- Complexity: Mid+
- Educational material: USEFUL — single-generation `fabledocs/` (10-section, same structure as netcleanarch/nopsolutionsnet/eShop's first-generation curricula).
- Quality observations:
  - `azure.yaml` + `infra/` present — real Azure deployment-as-code example, useful cloud-azure teaching material not seen elsewhere in this batch's other clones.
  - `CodeCoverage.runsettings` at repo root — explicit code-coverage tooling configured, a concrete CI-quality-gate example.
  - Two solution files (`eShopOnWeb.sln` and `Everything.sln`) suggest a deliberate "minimal app" vs "everything including admin/functional tests" solution-scoping pattern — a good example of managing solution-file scope in a larger repo.
- Old-AI-generated smells: none seen; real upstream reference code.
- Skill tags: arch-clean-hex, cloud-azure, ci-cd, test-integration, be-dotnet
- Duplicate/overlap: Direct architectural-contrast pair with netopen1/eShop (same e-commerce domain, monolith vs microservices) — deliberately pair these two in any teaching sequence about architecture evolution.
- Learning value: Medium-High — best used paired with netopen1/eShop as a before/after microservices-migration teaching story; solid standalone Azure-deployment reference.
- Interview stories it could support: "clean architecture monolith vs microservices for the same e-commerce domain," "scoping multiple .sln files in one repo," "deploying to Azure with azure.yaml/infra as code."
- Proposed disposition: D REFERENCE — valuable primarily as the "before" half of a monolith→microservices pairing with netopen1/eShop.

## NetAiOps snapshot history (netsnapshot)
- Path: Desktop\netsnapshot            - Origin: COURSE/GENERATED
- Type: curriculum (15 sequential full-copy checkpoints of a simulated app)
- State: docs-only / **simulated, explicitly does not need to compile**     - Size: 21→106 files across 15 growing snapshots (~830 files total across all snapshots)   - Last modified: 2026-07-18
- Purpose: A 15-step teaching history for a junior engineer: a simulated full-stack ops-ticket/incident-tracking platform ("NetAiOps"), where each snapshot folder is a complete copy of the codebase at that milestone (not a diff), meant to be diffed in an editor against the adjacent snapshot to see how the system evolves.
- Stack: implied .NET/React based on naming conventions matching the Net-fleet (unconfirmed — README doesn't state the stack explicitly, and code is stated to be simulated/non-compiling, so stack claims are UNKNOWN/NEEDS DEEPER INSPECTION beyond structural naming).
- Architecture: N/A (simulated teaching fiction, not a real running system)
- Complexity: Junior→Mid progression (00-walking-skeleton through 14-polish-and-docs, explicitly covering domain modeling, CRUD, validation, second-entity relationships, auth/authz, service refactor, frontend data maturity, testing harness, observability/config, N+1 performance, search/filter/pagination, hardening, polish)
- Educational material: STRONG — the entire project IS the curriculum; each snapshot has `NOTES.md` and `CHANGES.md` per the README's stated structure (not independently verified content-by-content in this pass, but structure is fully confirmed: 15 snapshot dirs, growing file counts consistent with incremental real development). `LEARNING-JOURNAL.md` explicitly states "the code is realistic in organization and naming...but intentionally simulated and does not need to compile."
- Quality observations:
  - Deliberate incremental-diff teaching design (compare snapshot N to N-1 in an editor) is a strong pedagogical pattern distinct from a flat curriculum — teaches "how a codebase grows," not just "what a finished codebase looks like."
  - Milestone sequence (auth introduced at step 06, service-refactor at 07, performance/N+1 at 11) models a realistic development order, including revisiting earlier decisions ("07-service-refactor" explicitly framed as "once duplication is visible").
  - Explicitly simulated/non-compiling status must be preserved as a caveat — this should never be mistaken for a working app in any consolidation pass.
  - Shares its "NetAiOps" name with the real, working netairag app — likely the same underlying concept/seed, worth clarifying the relationship (is netsnapshot the planning/teaching precursor to netairag, or an independent parallel exercise using the same name?) — UNKNOWN, NEEDS DEEPER INSPECTION to resolve definitively.
- Old-AI-generated smells: none seen structurally — the explicit "intentionally simulated, does not need to compile" self-disclosure is itself a transparency strength, not a smell.
- Skill tags: legacy-codebase-reading, code-review, design-docs-adrs, db-modeling, authz-rbac, db-indexes-perf, test-unit
- Duplicate/overlap: Shares "NetAiOps" naming and ops/ticket/incident domain with netairag (the real implemented app) — needs reconciliation to clarify relationship. Also structurally parallel to netsnapshot1 (different domain, same 15-step snapshot pattern/generator).
- Learning value: High — the incremental-diff teaching pattern is genuinely distinctive and valuable for showing "how software grows," complementing (not duplicating) the fleet's finished-state curricula.
- Interview stories it could support: "walking through how I'd incrementally build out auth, then a service-layer refactor, then N+1 fixes, in a realistic order."
- Proposed disposition: E EXERCISE SOURCE — best used as a step-by-step reading/diffing exercise, not a deployable app.

## Atlas Global Workforce snapshot history (netsnapshot1)
- Path: Desktop\netsnapshot1            - Origin: COURSE/GENERATED
- Type: curriculum (15 sequential full-copy checkpoints of a simulated app)
- State: docs-only / explicitly simulated, "not a diff"     - Size: 19→81 files across 15 growing snapshots (~660 files total)   - Last modified: 2026-07-18
- Purpose: A 15-step teaching history for a TypeScript/Node backend + React frontend, inspired by enterprise global-workforce platforms (HR/workforce management domain) — explicitly distinct in both stack and domain from netsnapshot.
- Stack: TypeScript/Node backend, React frontend (explicitly stated in README, unlike netsnapshot's implied/unconfirmed stack) — a genuine stack variation within the archive's otherwise .NET-heavy portfolio.
- Architecture: N/A (simulated teaching fiction)
- Complexity: Junior→Mid progression, with its own distinct milestone naming (e.g. "02-backend-crud" vs netsnapshot's "02-backend-ticket-crud"; "12-full-stack-workflow" vs netsnapshot's "12-search-filter-pagination" — genuinely different milestone content, not just renamed copies)
- Educational material: STRONG — same "full copy per checkpoint, diff in editor" design as netsnapshot, confirmed via matching structural evidence (`snapshots/*/` growing file counts, `LEARNING-JOURNAL.md`/`README.md` present).
- Quality observations:
  - Genuinely distinct domain (HR/workforce vs IT-ops/incident) and stack (Node/TS vs implied .NET) from netsnapshot — confirmed NOT a near-duplicate rerun despite the identical 15-snapshot structural pattern; this is real content variety from the same generator.
  - Milestone 12 diverges meaningfully ("full-stack-workflow" vs netsnapshot's "search-filter-pagination") — suggests the two courses were designed with somewhat different final emphases, not identical templates with find/replace naming.
  - Same simulated/non-compiling caveat applies.
- Old-AI-generated smells: none seen structurally.
- Skill tags: fe-react, be-node-express (implied), ts-types, legacy-codebase-reading, design-docs-adrs, db-modeling
- Duplicate/overlap: Structurally parallel to netsnapshot (same generator/pattern) but content-distinct (different domain and stack) — a genuine second course, not a duplicate. No other Node/TypeScript-backend project in this .NET-heavy batch, making it the batch's only non-.NET-backend example.
- Learning value: High — same incremental-diff pedagogical value as netsnapshot, plus stack diversity (the only TS/Node-backend example in an otherwise all-.NET batch).
- Interview stories it could support: "building a workforce-management CRUD app incrementally in a Node/TS + React stack, from skeleton through hardening."
- Proposed disposition: E EXERCISE SOURCE — same category as netsnapshot; valuable for its incremental-diff teaching pattern and as the batch's one non-.NET example.

## C# language tutorial (csharptut)
- Path: Desktop\csharptut            - Origin: COURSE/GENERATED
- Type: curriculum, docs-only
- State: docs-only, appears complete     - Size: 24 topic files + 24 matching "-examples.md" files = 48 markdown files, plus 5 adjacent tutorial dirs (dotnet-tutorial, javascript-tutorial, nodejs-tutorial, react-tutorial, typescript-tutorial — these are separate curricula bundled in the same folder, not part of the C# sequence, and are OUT OF SCOPE for this .NET batch but worth flagging their presence for whichever batch covers JS/TS tutorials)   - Last modified: 2026-07-18
- Purpose: A from-scratch C#/.NET language tutorial: setup/tooling → basics → types → control flow → methods → OOP (classes, inheritance, structs/records/enums) → collections/generics/LINQ → exceptions → delegates/events/lambdas → async/await → pattern matching → nullable reference types → file I/O/JSON → HTTP/APIs → DI/config → EF Core → ASP.NET Core Web API → testing → a capstone CRUD API → a closing "how to learn and what's missing" reflection.
- Stack: N/A (pure teaching content, spans the full modern C#/.NET web stack conceptually: EF Core, ASP.NET Core, xUnit-style testing implied by topic 21)
- Architecture: N/A
- Complexity: Tutorial (explicitly a ground-up language course, topic ordering runs from absolute basics to a capstone project)
- Educational material: STRONG — the whole project is the curriculum. 24 topics is a genuinely complete language-to-web-API arc (basics through capstone), each topic paired with a dedicated examples file (i.e., concept explanation kept separate from runnable/illustrative code samples) — a clean, consistent authoring pattern across all 24 topics.
- Quality observations:
  - Topic ordering is pedagogically sound: language fundamentals (01-15) fully precede web/data concerns (16-22), with testing (21) placed just before the capstone (22) — mirrors how a real curriculum should sequence prerequisite knowledge.
  - Topic 23 ("how to learn and what's missing") is a self-aware closing chapter acknowledging the course's own scope limits — a mature curriculum-design choice rather than presenting itself as exhaustive.
  - Dedicated Nullable Reference Types (15) and Pattern Matching/modern C# (14) topics show attention to modern C# idioms, not just legacy syntax.
  - Consistent examples-file pairing across all 24 topics (verified via directory listing, not per-file content) suggests a disciplined single-pass generation rather than drifting quality over time — though content depth per topic was not individually read in this pass (spot-check recommended before treating uniformly).
- Old-AI-generated smells: none seen structurally; would want to spot-check 2-3 example files for repetition/genericness across topics before fully certifying (not done in this pass beyond structural verification).
- Skill tags: ts-types (N/A—C# focused; use general), be-dotnet, orm, be-rest-design, test-unit, db-postgres (implied via EF Core topic)
- Duplicate/overlap: Significant scope overlap with csbootcamp (also C# fundamentals, but exercise/auto-graded rather than read-then-example) and c#interview's foundations phase — genuine complementary redundancy (different learning modes for the same base knowledge), not pure waste.
- Learning value: High — most complete single-arc "start to capstone" C# curriculum in the batch.
- Interview stories it could support: N/A directly (it's the study material, not a project) — but topic 22's capstone CRUD API is itself a legitimate small project to discuss.
- Proposed disposition: E EXERCISE SOURCE — best-organized foundational C# reading curriculum in the batch; keep as the "read this first" companion to csbootcamp's exercises.

## C# interview prep (c#interview)
- Path: Desktop\c#interview            - Origin: COURSE/GENERATED
- Type: curriculum, docs-only
- State: docs-only, appears complete/mature per user's own memory notes (confirmed independently: question-vault dir has 15 files matching memory's description)     - Size: 5 phase dirs (00-setup through 04-question-vault) with 30+ files total   - Last modified: 2026-07-17
- Purpose: A structured junior→mid .NET backend interview-prep program: environment/AI-workflow setup → phase 1 foundations (weekly guides + concept checklist) → phase 2 portfolio (project spec, git/PR workflow, CI/CD/deploy guide) → phase 3 interviews (question bank, two take-home simulations, live-coding drills, system-design-lite, behavioral story bank, resume/applications) → phase 4 question vault (14 topic files: C# language, async/concurrency, ASP.NET Core, EF Core, SQL/databases, testing, HTTP/REST API design, security/auth, architecture patterns, DevOps/git/Docker/CI-CD, rapid-fire trivia, code-output gotchas, spot-the-bug, mock screener scripts).
- Stack: N/A (interview-prep content, but topic coverage spans the full .NET backend interview surface)
- Architecture: N/A
- Complexity: Tutorial/Interview-prep, explicitly phased (00→04) as a progressive program rather than a flat reference
- Educational material: STRONG — per user's own memory index, this was built out to ~490 letter-prefixed Q&A + 270 flashcards + 32 gotchas + 24 spot-the-bug + 3 mock scripts (the question-vault dir structure directly confirms the file-level organization claimed: 12-code-output-gotchas.md, 13-spot-the-bug.md, 14-mock-screener-scripts.md all present as named).
- Quality observations:
  - Phase structure moves from foundations → building a real portfolio project (with actual git/PR workflow and CI/CD deploy guidance, not just reading) → interview-specific drilling — a genuinely complete "get hired" pipeline, not just a Q&A dump.
  - Two take-home-simulation files (phase 3) and dedicated mock-screener-scripts (phase 4) show deliberate design toward realistic interview conditions, not just static trivia.
  - "Spot-the-bug" and "code-output-gotchas" files are a more advanced/active recall format than plain Q&A — good for testing actual comprehension vs memorization.
  - Content depth/accuracy not independently re-verified line-by-line in this pass (relying on structural confirmation + prior memory record); recommend treating as high-confidence given the specificity of the memory record's numbers matching the observed file list.
- Old-AI-generated smells: none seen structurally.
- Skill tags: be-dotnet, orm, db-sql-raw, security-owasp, be-rest-design, test-unit, ci-cd, code-review, design-docs-adrs
- Duplicate/overlap: Overlaps with csharptut (fundamentals) and csbootcamp (exercises) in base C# knowledge, but is the only one of the three oriented specifically around interview performance (behavioral stories, take-homes, live-coding drills, resume prep) — least redundant of the three once you account for purpose.
- Learning value: Very High — most interview-outcome-directly-relevant curriculum in the batch, already substantially built out per prior work.
- Interview stories it could support: the "06-behavioral-story-bank.md" file is literally designed to answer this question directly.
- Proposed disposition: B HIGH-VALUE — mature, purpose-built interview program; not "A FLAGSHIP" only because it's pure study material rather than a demonstrable working project, but extremely high practical value.

## csbootcamp (offline C# bootcamp)
- Path: Desktop\_Organized Desktop\01 Net Workspaces\csbootcamp            - Origin: COURSE/GENERATED
- Type: curriculum, exercise pack (auto-graded) + reference docs
- State: in progress (4 of presumably more modules built: 01-language-core, 02-methods-and-delegates, 03-collections-and-linq, 04-strings-and-time)     - Size: 31 exercise files + 31 matching solution files across 4 modules, plus cheatsheets/ (3 files), quizzes/ (6 items), guides/, docs/ (OVERVIEW.md, ROADMAP.md), FLIGHTPLAN.md, and its own astraupskill/ (7 files, same bounded-exercise pattern seen elsewhere in the batch)   - Last modified: has its own `.git` (not dated in this pass; distinct repo from the rest of Desktop)
- Purpose: "A personal, offline, test-graded C# bootcamp" — runs purely on the .NET SDK, no other dependencies. Each exercise is one file: a prompt in comments, a stub that throws, and tests underneath; a `progress.cs`/`verify.cs` harness (with a `_lib/Check` helper) auto-grades completion.
- Stack: pure .NET SDK (no web framework — this is language-level, not web-app, practice), custom lightweight test/check library (`_lib/Check`)
- Architecture: N/A (exercise harness, not an app)
- Complexity: Tutorial (offline, self-paced, auto-graded exercises)
- Educational material: STRONG — the project's docs (`docs/OVERVIEW.md`) explicitly lay out a deliberate multi-modality design: `bootcamp/` = "reach for it when you are about to write code," `cheatsheets/` = "ten-second lookup," `quizzes/` = "know what you actually retained," `FLIGHTPLAN.md` = "a ten-hour schedule" for a specific constrained-time use case (explicitly framed as "you have a flight and a laptop"). This multi-modal, purpose-differentiated design is more deliberate than any other curriculum in the batch.
- Quality observations:
  - The "one file: prompt + stub-that-throws + tests underneath" exercise format is a clean, runnable, self-checking design — genuinely more rigorous than passive-reading curricula (you cannot "complete" an exercise without making the stub's test pass).
  - `_lib/Check` custom assertion helper + `progress.cs`/`verify.cs` at the bootcamp root suggests a working auto-grading harness distinct from a generic test framework — worth reading directly to understand the grading mechanism (not independently verified in this pass beyond directory presence — NEEDS DEEPER INSPECTION to confirm the harness actually runs/passes).
  - Only 4 modules built so far (language-core, methods/delegates, collections/LINQ, strings/time) — an in-progress curriculum, likely earlier in its arc than csharptut's full 24-topic sweep; the `ROADMAP.md` should clarify what's planned next (not read in this pass).
  - Bonus `astraupskill/` follows the same bounded-exercise pattern seen in netopen3/netopen5/.netarchitectureproject — interesting that even this originally-standalone curriculum project got the same treatment layered on top.
- Old-AI-generated smells: none seen structurally; the self-checking exercise design is actually a positive signal against typical "boilerplate that doesn't verify anything" AI-course smells.
- Skill tags: be-dotnet, test-unit, ts-types (N/A, C#-only — general language fundamentals)
- Duplicate/overlap: Same base-C#-knowledge overlap as csharptut and c#interview, but distinguished by being the only auto-graded/self-checking exercise format of the three — genuinely the most rigorous practice-mode option, complementary rather than redundant.
- Learning value: High — the auto-graded, runnable-exercise format is the most rigorous hands-on practice mode in the batch's C#-fundamentals cluster; in-progress status (4/N modules) is the main limiter.
- Interview stories it could support: N/A directly (practice tool, not a discussable project).
- Proposed disposition: E EXERCISE SOURCE — best hands-on/auto-graded practice format for C# fundamentals in the batch; continue building out remaining modules per its own ROADMAP.md.

## Batch observations

- **The "Net-fleet" is the batch's dominant cluster** (10 of 24 candidates): a single generator pipeline clearly produced netairag/netauth/netdocu/netdrop/netintercom/netlinear/netnotion/netshop/.netramp/.netstripe as parallel SaaS-clone learning apps, each with the same Api/Application/Domain/Infrastructure .NET8 + React/Postgres shape and a ~47-file 8-section curriculum. Quality is generally high and project-specific (verified via direct content sampling in netdrop, netairag), but two members (.netramp, .netstripe) have a **confirmed zero-test-file gap** despite shipping "testing strategy" docs — this is the clearest concrete AI-generated-project smell found in the batch and should be prioritized for a fix pass (write the missing tests) before these two are presented as complete portfolio pieces, matching the pattern the user has already run "Fable review + fix pass" audits for elsewhere (per memory).
- **Curriculum-generation is itself versioned and iterative**: several projects show 2-4 successive curriculum generations layered on the same codebase (netcleanarch has 4: fabledocs/fabledocs2/fabledocs3/fabledocs4; netairag, .netstripe, netnotion each have 2). These generations are NOT always redundant — netcleanarch's four generations serve distinct purposes (full curriculum, architecture notes, ADRs+interview-translation, guided labs+primers) — but at least netairag's `docs/upskill` vs `docs2.0` appear to be near-identical duplicates by filename and deserve a diff-and-consolidate pass rather than automatic "preserve both."
- **A distinct, thinner curriculum style ("astraupskill" bounded bug-fix exercises) is reserved for the very large real open-source clones** (netopen3/Umbraco, netopen5/jellyfin, .netarchitectureproject/modular-monolith-with-ddd, plus csbootcamp as an outlier bonus) — one worked change with CODEBASE-MAP/CONCEPTS/WORKED-CHANGE/TESTING/PRACTICE/SOLUTIONS/TRACE-LAB, kept at the *parent* directory outside the actual clone. This is a sensible scoping choice (you can't realistically produce a full 47-file curriculum for a 70,000-commit codebase the same way you would for a 50-file custom app) but means these clones' teaching value is currently much thinner than their codebase size would justify — netopen3/netopen5 in particular could support much richer curricula given their scale and maturity.
- **netopen1/eShop's `astra/` curriculum (72 numbered user stories + Python auto-grading tool) is the single most rigorous teaching construct found in this batch** — it's the only example of automated verification (`check_course.py`) paired with a large numbered story backlog, and is worth using as a template if the user wants to build similarly rigorous curricula for other large clones in this batch (Umbraco, jellyfin, nopCommerce) that currently only have thin astraupskill exercises.
- **Genuine architectural diversity exists even within the "toy" Net-fleet**: .netramp deliberately skips the Application/Domain/Infrastructure split (flat backend/), .netstripe uses minimal APIs instead of MVC controllers, netdrop is the only one with a real background worker + distributed-consistency risk, netnotion is the only one with all three test tiers named as separate projects. This is healthy variety, not copy-paste sameness — worth highlighting to the user since it means the fleet isn't just 10 identical apps with different names.
- **Naming collision worth resolving**: both netairag (a real, partially-implemented app) and netsnapshot (a simulated, explicitly-non-compiling teaching history) are titled "NetAiOps" and share the ops/ticket/incident domain. The relationship between them (precursor sketch vs independent exercise vs accidental reuse of a name) was not determinable from structure alone and should be clarified directly with the user or via a deeper read of both READMEs' framing language.
- **The three pure-C#-curriculum projects (csharptut, c#interview, csbootcamp) are complementary, not redundant**, despite all covering C# fundamentals: csharptut = read-then-see-example, csbootcamp = write-code-and-auto-grade, c#interview = recall-under-interview-pressure. Worth explicitly cross-referencing them (e.g., "finish csharptut topic N, then do the matching csbootcamp module, then drill the matching c#interview question-vault section") rather than treating any of the three as disposable.
- **Every open-source clone in this batch checked out clean** — no evidence of local modification found in any of the eight real-project clones (all confirmed via genuine, large, multi-year upstream git histories with real author names and dates); all "generated" content is additive documentation living in clearly-separated folders (fabledocs*/astra/astraupskill), never mixed into the application source itself. This means these eight clones can be safely re-synced to upstream at any time without losing the added curricula, which is a good state to be in.
- **Surprise**: OrchardCore's curriculum (`.netopen2/fabledocs/upskill`) was the highest-quality single-generation curriculum directly verified by content sampling in this pass — better than several of the "flagship" candidates' curricula on first read — specifically because of its graduated Junior/Mid/Senior reading-path design with explicit "ignore this" guidance, a pattern not seen elsewhere in the batch and worth propagating.
