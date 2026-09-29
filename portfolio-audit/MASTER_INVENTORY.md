# Master Project Inventory

Generated 2026-09-23 from 14 read-only batch audits. **Evidence for every row lives in `projects/batch-NN.md`** (column "B"),
which cites file paths, manifests, test dirs and docs for each project. This file is the scannable index; dispositions here are the
*calibrated* final ones (the batch agents over-assigned FLAGSHIP — ~60 "A" votes across batches — so they were re-ranked globally).

Disposition key: **A** Flagship · **B** High-value training · **C** Specialized · **D** Reference codebase · **E** Exercise source · **F** Consolidate · **G** Archive
Docs key: NONE / MIN / USEFUL / STRONG / EXCEL (learning material, not app docs)

## Portfolio statistics

| Metric | Count | Notes |
|---|---|---|
| Top-level candidate directories inspected | **354** | Desktop root (incl. hidden `.net*`), `_Organized Desktop\01–12`, 5 home-dir projects |
| Nested sub-projects inside bundles | ~190 | newcodexJS 20, newcodex3 50, JS1 ~97, newcodecjs2 5, job track 5, appmaketrck 3, … |
| Meaningful project records written | ~215 | incl. cluster records that stand for many near-identical folders |
| Empty / tiny / boilerplate folders | ~60 | e.g. all 12 `10 New Folders\*`, opusboot2/4.2, opusdavinci, codexlearnp1, master 5, master555, f1, j6, aff-wt-be06 |
| Open-source clones (real upstream code) | **~42** | 8 .NET, ~31 in 03 Master Projects/09 Grav, plus bulletproof-react, ai-observer, VTCode, rn1 (Bluesky), healthchecks |
| Original / LLM-course-built projects | ~170 | almost all built *by* LLMs *for* you (course/generated), few hand-written |
| Projects with substantial learning docs (STRONG+) | **~150** | `astraupskill/` alone appears in ≈200 folders; `fabledocs*` in ~35 |
| Duplicate / near-duplicate clusters | 20 | see DUPLICATE_CLUSTERS.md |
| Archive candidates (G) | ~130 folders | dominated by the 78-folder numbered-experiment corpus + empty dirs + stale mirrors |
| Projects with real CI workflows | ~15 | gitvg fleet (9), gitjira-app, astra1, astraspacegameweb, aicallhelper, tagalog, buildermentor |
| Projects with *no* git history on disk | majority | all of 03 Master Projects, 05 Numbered Experiments, most of 02/07/08/12 — history either on GitHub or never existed |

## Core inventory (meaningful projects, grouped by family)

### Tier-1 portfolio candidates (original / course-built, deep)
| Project | Path | Stack | Complexity | Docs | Value | Disp | B |
|---|---|---|---|---|---|---|---|
| **atlas** (EOR platform, Course 8) | Desktop\gitvg\atlas | C#/.NET 10, hex arch, outbox, idempotency middleware, v1/v2 API | Senior-oriented | STRONG | Very High | **A** | 02 |
| **gitjira-app** (Jira clone) | Desktop\gitjira-app | Node/Express+React+Prisma, BullMQ, Socket.IO, 4 CI workflows | Mid+ | EXCEL (33 ADR files, postmortems/, threat-model, RUNBOOK, 209 commits) | Very High | **A** | 02 |
| **astraspacegameweb** (Warband: Crownlands) | Desktop\astraspacegameweb | TS web+server, Postgres/Drizzle, Redis, Docker, Caddy, Prometheus/Grafana/Tempo, chaos tests | Senior-oriented | STRONG | Very High | **A** | 05 |
| **astra1** (Helios, multi-tenant ops sim) | Desktop\astra1 | Next 16, raw Postgres, OTel (`src/instrumentation.ts`), outbox/sagas, Playwright, CI | Senior-oriented | STRONG | Very High | **A** | 06 |
| **aicallhelper** (AI Call Assistant v3) | Desktop\aicallhelper | Tauri 2 / Rust + React/TS, 17 ADRs, CI | Senior-oriented | EXCEL | Very High | **A** | 03 |
| master1 (GlobalWork EOR) | O\03 Master Projects\master1 | NestJS/Next/Prisma/BullMQ/Testcontainers | Mid+ | EXCEL | High | B | 10 |
| buildermentor (ShipShape) | Desktop\buildermentor | Fastify, Drizzle+pg, pg-boss, Anthropic RAG, TanStack, CI | Mid+ | USEFUL | High | B | 04 |
| buildevent (ticketing) | Desktop\buildevent | Next+Fastify+Prisma/PG+Redis/BullMQ+Stripe+signed QR | Mid+ | USEFUL | High | B | 04 |
| borrowbox | Desktop\borrowbox | .NET 10, SQLite, xUnit, graded teaching ramp | Junior→Mid | EXCEL | High | B | 04 |
| globehire / meterforge | Desktop\globehire, \meterforge | .NET 10 modular monoliths, `FLAW-LEDGER.local.md` | Mid+ | STRONG | High | B+E | 05 |
| perch (ATS, 5-flaw ledger) | Desktop\perch | Node+React monorepo | Mid+ | EXCEL | High | B+E | 02 |
| pulse / bazaar (gitvg) | Desktop\gitvg\pulse, \bazaar | Node+React; pulse: ingestion+load/; bazaar: caching, observability/perf/deploy dirs | Mid+ | STRONG | High | B | 02 |
| astra5 (Stockade) | Desktop\astra5 | Next 16 + .NET service, Postgres, sagas, Docker | Senior-oriented | STRONG | High | B | 06 |
| aaa1 (multi-tenant CRM) | O\12 Other\aaa1 | Next 15/React 19+Prisma 6+worker | Senior-oriented | STRONG (21 arch/learning docs) | High | B | 14 |
| HNJOBTRACK | O\08 App\HNJOBTRACK | FastAPI+Supabase RLS+Next+OpenAI | Mid+ | USEFUL | High | B | 14 |
| grokbuildmultitenantproject | Desktop\grokbuildmultitenantproject | Express/TS/Prisma/PG+React; tenant-isolation vuln fixed + regression test | Mid | STRONG | High | B | 07 |
| tagalog (Aral) | Desktop\tagalog | Next+Expo+Fastify+Postgres, pnpm/Turbo, CI | Mid+ | USEFUL | High | B | 04 |
| opusboot1 (DevPractice) | Desktop\opusboot1 | Fastify/Prisma/React/QuickJS-WASM | Mid+ | product | High | B | 06 |
| lucasrouter (RouteIQ) | Desktop\lucasrouter | Next 16/Leaflet/zustand, measured perf | Mid+ | STRONG | High | B | 03 |
| aiheartbeat (Pulse orchestrator) | Desktop\aiheartbeat | claude -p heartbeat, SQLite tickets, Next dashboard | Mid+ | STRONG | High (agentic) | C | 03 |
| VGdemo / globalhire-lite | O\09 Grav\VGdemo | React/Express/Prisma + C# port with documented security regression | Mid+ | STRONG | High | C+E | 14 |
| grouphelpdesk | O\08 App\grouphelpdesk | React/Express/TS+Prisma, RBAC, CI/Docker | Mid+ | STRONG | Medium-High | C | 14 |

### Other original / course-built projects (kept)
| Project | Path | Stack | Cx | Docs | Disp | B |
|---|---|---|---|---|---|---|
| aicallhelper2 / aicallhelper5 | Desktop | Python pywebview / Tauri+React v4 | Mid+/Sr | EXCEL/STRONG | F→ lineage of aicallhelper (keep 5 if it surpasses v3 — NEEDS DEEPER INSPECTION) | 03 |
| finalcallhelp\cuedeck | Desktop\finalcallhelp | Electron/TS, Playwright | Mid+ | STRONG | C | 03 |
| tracer, relay, folio, harbor (gitvg) | Desktop\gitvg\* | Node+React course repos (15 sprint PRs each) | Mid–Mid+ | STRONG | C (folio: CRDT; relay: durable exec) | 02 |
| agora | Desktop\gitvg\agora | .NET 10 + React, Course 9 | Sr | STRONG | C (only 8 commits — verify) | 02 |
| storefront | Desktop\gitvg\storefront | Next/Prisma e2e | Mid+ | STRONG | C | 02 |
| netdrop, netintercom | Desktop | .NET 8 + React + PG (+SignalR/Hangfire) | Mid+ | EXCEL/USEFUL | C | 01 |
| netauth | Desktop\netauth | .NET 8 IdP JWT/OIDC | Mid | EXCEL | C (auth specialty) | 01 |
| buildwhiteboard | Desktop\buildwhiteboard | Yjs CRDT + ws | Mid | USEFUL | C | 04 |
| buildreviewer | Desktop\buildreviewer | NestJS/Prisma/Octokit | Mid | USEFUL | C (**real `.env` in tree**) | 04 |
| ankijs (Recall) | Desktop\ankijs | React 19 PWA, Dexie, ts-fsrs | Mid | STRONG | C | 04 |
| aral | Desktop\aral | Hono/tRPC/libsql event-log sync | Mid+ | USEFUL | C (stalled; docs/BLOCKED.md) | 04 |
| JSProjectLearn (SkillForge Quest) | Desktop\JSProjectLearn | React 19 platform, 334 missions, hash-verified | Mid | EXCEL | B (learning platform) | 07 |
| jstrain2.2 | O\04 JS\jstrain2.2 | offline JS/TS bootcamp, graded | J→Mid | EXCEL | B (fundamentals, done) | 12 |
| unionboot | Desktop\unionboot | ~24k verified exercises JS/TS/React/C#/SQL | J→Mid | EXCEL | B (exercise bank) | 05 |
| rewritepy2js | O\04 JS\rewritepy2js | FastAPI RealWorld → TS/Express/Prisma, IDOR story | Mid | USEFUL | C+E | 12 |
| aiapplybotjs / aiapplybot (ApplyPilot fork) / Desktop\aiapplybot / eliapplybot(-python) | various | job-apply automation, 5 variants | Mid | mixed | F (one lineage) | 03/12/14 |
| codehelper, think (TraceVault) | O\06 AI | LLM chat side-by-side; MCP/indexer monorepo | Mid+ | MIN–USEFUL | C | 12 |
| jsharness\ctvodejs | Desktop\jsharness | TS port of VTCode agent | Mid+ | MIN | C (agentic) | 07 |
| master2 (billing), master4, master7 | O\03 Master | Express/React/Prisma/BullMQ | Mid | EXCEL | C/E | 10 |
| buildaffiliate, buildagentteachGEM, buildagentteaching, buildagenthelpdesk, buildanalytics | O\02 Build | Next/Fastify/Prisma/PG, deterministic agents | Mid–Mid+ | STRONG | C/E (known bugs = exercises) | 09 |
| grokbuild{ecommerce,hr,order,team,ppm} | Desktop | Express/TS/Prisma/PG+React (hardened Grok starters, **uncommitted work**) | Mid | STRONG | E | 07 |
| anti{emponb,helpdesk,inv,testbuild} | O\07 Anti | Express/Nest+Prisma; shared hardcoded JWT fallback | Mid | STRONG | E | 14 |
| jdtrrain2.1, GlobGame, appmakertrack, andie, pp8, jeopardy-game-refactor | O\12/08, ~ | Next/Prisma; FastAPI HRIS; Node CLI | Mid | STRONG | C/E | 14 |
| newcodecjs2 (blockr/bookr/helpkit/payr/planr) | Desktop\newcodecjs2 | Next 15/Drizzle, domain unit tests | Mid | MIN | E | 06 |
| Net-fleet rest (netairag, netdocu, netlinear, netnotion, netshop, .netramp, .netstripe) | Desktop | .NET 8 + React + PG (**.netramp/.netstripe: 0 tests**) | Mid | USEFUL–EXCEL | E | 01 |
| netsnapshot / netsnapshot1 | Desktop | 15-checkpoint simulated histories | J→Mid | STRONG | E | 01 |
| C# curricula: csharptut, c#interview, csbootcamp | Desktop, O\01 | C# docs, 490 Q&A, auto-graded exercises | Tutorial | STRONG | B (C# refresh), keep all 3 | 01 |
| JSTut | Desktop\JSTut | 39-file JS/TS/React/C#/SQL reference | Tut→Mid | EXCEL | D (personal reference) | 07 |
| spacegamev2, stellar-conquest(+architecture doc) | Desktop, ~ | Expo/Fastify/Redis/WS | Mid+ | STRONG | F → Warband narrative | 05/14 |
| mobiletagalog, buildsmallplates, masterrnative | Desktop / O\03 | Expo RN | J+ | USEFUL | C (mobile) | 04/11 |
| MasterStore\storefront | O\03 Master | Next 16 + Spree SDK + Stripe/Adyen | Mid+ | STRONG | C | 11 |
| obsidian-claude (2 copies) | ~, O\12\appmaketrck | TS MCP server, better-sqlite3 (broken entrypoint) | Mid | spec docs | E (debug exercise) | 14 |
| hnrandom | O\08 App | Express+DuckDB+OTLP | Mid+ | USEFUL | C (observability) | 14 |
| rn1 | O\05\rn1 | Bluesky social-app fork + 1 lesson | Sr codebase | USEFUL | D | 13 |
| z1, z3, g1/X1, B1 | O\05 | Next apps; z1 has ADR pack | Mid | STRONG | C (keep as samples) | 13 |

### Open-source reference codebases (see EDUCATIONAL_CONTENT_INDEX.md for curriculum quality)
| Clone | Path | Upstream | Stack | Curriculum | Disp | B |
|---|---|---|---|---|---|---|
| Outline | Desktop\masteroutline\outline | outline/outline | Koa/Sequelize/React/Yjs | EXCEL (fabledocs 1-4, ~80 files, 10 ADRs) | **D★** | 05 |
| Twenty | O\03\mastertwenty\twenty | twentyhq/twenty | Nx, NestJS, React, metadata-driven | EXCEL (4-pass, 79) | **D★** | 11 |
| OpenStatus | O\03\masteropen\openstatus | openstatusHQ | Next/tRPC/Hono/Go/Drizzle/Tinybird | EXCEL (4-pass, 79) | **D★** | 11 |
| eShop | Desktop\netopen1\eShop | dotnet/eShop | Aspire, gRPC, RabbitMQ, Redis | EXCEL (72 stories + `check_course.py` grader) | **D★** | 01 |
| OrchardCore | Desktop\.netopen2\OrchardCore | OrchardCMS | .NET 10 multi-tenant CMS | EXCEL (Jr/Mid/Sr reading paths) | **D★** | 01 |
| modular-monolith-with-ddd | Desktop\.netarchitectureproject | kgrzybek | .NET DDD/CQRS | MIN | **D★** (architecture exemplar) | 01 |
| Infisical | O\03\masterfinisc\infisical | Infisical | Fastify/Knex/PG + React | EXCEL (best architecture critique) | **D★** | 10 |
| CleanArchitecture | Desktop\netcleanarch | jasontaylordev | .NET MediatR/EF | EXCEL (4 generations) | D | 01 |
| eShopOnWeb, nopCommerce | Desktop\.nettodo, \nopsolutionsnet | dotnet-architecture, nopSolutions | ASP.NET Core | USEFUL | D | 01 |
| NextCRM, Umami, Plane, Teable, Paperless-ngx, Payload, Postiz, pretalx, Morphic, shadcn/ui, Saleor, Zulip, Open edX | O\03 Master Projects\* | various | Next/Prisma, Django/Celery, NestJS | STRONG (53-file template) | D | 11 |
| Cal.com, Dify, Dub, Formbricks, Hoppscotch, Linkwarden, Mayan, Flagsmith, IDURAR | O\03 Master Projects\* | various | Next/Prisma, Django, MERN | STRONG–EXCEL | D | 10 |
| NocoBase | Desktop\masternocu | nocobase | Node/React plugins | STRONG (1 wave) | D | 05 |
| OpenSlides, Review Board, pretalx (grav) | O\09 Grav | various | Go/Python/Angular microservices; Django | USEFUL–STRONG | D (OpenSlides = only microservices OSS) | 14 |
| Mattermost | O\03\mastermatter | mattermost | Go + React | USEFUL (Astra lesson) | D (only Go) | 10 |
| bulletproof-react, ai-observer-reference, healthchecks | O\04, O\06, O\12 | various | React ref; Go+OTel; Django | — | D | 12/14 |
| Umbraco, jellyfin | Desktop\netopen3, \netopen5 | upstream | huge .NET | MIN | G (keep clone, no investment) | 01 |
| Novu, Supabase, ToolJet, Typebot, Indico | O\03 | upstream | various | **NONE** | G (bare clones) | 10/11 |
| VTCode | Desktop\jsharness\VTCode | vinhnx | Rust | n/a | G (third-party) | 07 |

### Archive (no further investment; nothing deleted)
- **05 Numbered Experiments** — ~78 of 86 folders: one generated corpus of single-lesson Next/Prisma (+6 Java CLI, 2 Python) CRUD-safety apps (batch-13). Keep rn1, z1, z3, g1/X1, B1 + 3–5 samples.
- **Empty dirs**: `10 New Folders\*` (12), opusboot2, opusboot4.2, opusdavinci, codexlearnp1, Amasterplan, New folder, master 5, master555, f1, j6, aff-wt-be06, .nethris, jsinterview, jstran2.0, rewritepy2jsodoo, booklearn, claudelearnpath, recipegen, grokbuildsupportproject (plan only).
- **Dead scaffolds**: jstrain3 root + deskpilot + deskpilot-app, claudeailab-temp, recipegen-temp, FinalJep, hypernova-inc-main, Obsidian vault stub.
- **Stale mirrors / meta**: geminiorganized (~80-project July copy), AstraOrganized (≡ project-inventory), readme/.
- **Superseded versions**: aihelper (v1), fableaihelperv3 (v2), fableaihelperv2\cuedeck, spacegame (v1), jobtrack, jsdrillapp/reps, astraboot1, atlas-net, agora-net, master6, aral-deploy, hermes, union-alpha-playground.
- **Redundant generated CRUD sets**: newcodex3 (50 dirs, zero tests), most of newcodexJS (keep the ~9 in fablereview LEARNING_PATH), most of JS1 (keep ones in LEARNING_PATH), grokjs + groktuts (overlap JSTut/unionboot).
