# Software-Engineering Archive Audit — Final Report

*2026-09-23 · read-only audit · no project was modified.* Supporting files in this folder:
MASTER_INVENTORY · PROJECT_MATRIX · EDUCATIONAL_CONTENT_INDEX · DUPLICATE_CLUSTERS · SKILL_MATRIX · GAP_ANALYSIS · PRIORITY_ROADMAP ·
`projects/batch-01..14.md` (per-project evidence records with file paths).

> **Status note (added 2026-10-06):** this report is a frozen snapshot from 2026-09-23 and should be read as a historical record.
> - **Paths:** the Desktop and `_Organized Desktop` paths it cites have largely moved. Most projects are now standalone repos on github.com/elirc, sometimes under different names. For example, `.netstripe` is `dotnet-stripe`, astra1 is `helios-interplanetary`, and gitjira-app is `gitjira`.
> - **Later work:** the B01–B07 apprenticeship, which started the same day, added training material to 31 projects. Its log and outcomes are in `../apprenticeship/PROGRESS.md` and `../batch1report/` to `../batch7report/`.
> - **Counts:** figures like test-file and commit counts are as of 2026-09-23.

---

## 1. Executive summary
- You have **~354 top-level project folders** (+ ~190 nested sub-projects). About **215 are meaningful**; the rest are empty dirs, dead scaffolds, stale mirrors or superseded versions.
- The archive is **overwhelmingly LLM-built-for-you**: course repos, generated SaaS clones, and ~40 open-source clones wrapped in generated curricula. Very little is hand-written, and **most folders have no git history on disk**.
- **You are saturated on CRUD.** React + Express/Next + Prisma + Postgres + JWT + Zod + "scope by tenant" appears in 150+ folders. Help desks ×12, issue trackers ×12, e-commerce ×13, employer-of-record platforms ×7.
- **You are also saturated on learning material.** There are ≈200 `astraupskill` packs, 35 `fabledocs` curricula and ~40 interview packs. A prior review (`AstraOrganized2\fablereview`) already turned the CRUD part into a curated path. More reading is not the bottleneck.
- **The real gaps are the senior ones:** nothing is deployed to AWS or Azure; SQL Server is nearly absent; there is no query-plan, index or load-test practice, no zero-downtime migration, and no SLOs or alerts you have operated. You have read many design docs and written very few, and you have made no upstream contributions.
- **The fix is depth, not breadth.** Pick 5 flagships, operate 2 of them like production first, and use the OSS clones and flaw ledgers as drill material.
- **Two urgent hygiene items:** revoke the live Shopify `shpat_` token (see §18.1), and commit the uncommitted work in grokbuild* and elsewhere.

## 2. Portfolio statistics
| Metric | Count |
|---|---|
| Top-level candidate directories inspected | 354 (Desktop incl. hidden `.net*`, `_Organized Desktop\01–12`, 5 home-dir) |
| Nested sub-projects inside bundles | ~190 (newcodexJS 20, newcodex3 50, JS1 ~97, newcodecjs2 5, …) |
| Meaningful projects (records written) | ~215 |
| Tiny / empty / boilerplate | ~60 |
| Open-source clones | ~42 (8 .NET with real upstream history; ~31 in 03 Master/09 Grav; 4 others) |
| Original / LLM-course-built projects | ~170 |
| Projects with substantial (STRONG+) learning docs | ~150 |
| Duplicate / near-duplicate clusters | 20 |
| Archive candidates | ~130 folders (78 of them in `05 Numbered Experiments`) |
| Repos with CI workflows | ~15 |
| Raw disposition votes by batch agents (before calibration) | A 61 · B 96 · C 64 · D 37 · E 23 · F 16 · G 131 (tag mentions) |

## 3. Master project inventory
See **MASTER_INVENTORY.md**. It has a scannable table per family, with batch-file evidence pointers and calibrated dispositions.

## 4. Flagship candidates (5)
| # | Project | Why flagship | Evidence |
|---|---|---|---|
| 1 | **gitjira-app** (Jira clone, TS) | The only large app with a real team-style history (209 commits, 25 tags). It has 33 ADR files, `postmortems/`, `threat-model.md`, `RUNBOOK.md`, `security-audit.md`, `performance.md`, and 4 workflows: ci/deploy/e2e/secrets. The stack is Express+React+Prisma+BullMQ+Socket.IO. It is the ideal host for deploy, migrations and SLOs. | `Desktop\gitjira-app\docs\`, `.github\workflows\` |
| 2 | **atlas** (EOR, C#/.NET 10) | The most senior backend: hexagonal, `IdempotencyMiddleware.cs`, outbox, multi-currency, explicit V1/V2 contracts, 119 test files, CI. It is the natural host for SQL Server, query plans and an Azure deploy. | `Desktop\gitvg\atlas\src\Atlas.Api\Idempotency\`, `ci.yml` |
| 3 | **astraspacegameweb** (Warband: The Crownlands) | The only project with a full ops stack: `compose.production.yaml`, `infra/Caddyfile`, Prometheus/Grafana/`tempo.yaml`, chaos tests, refresh-token reuse detection. Its history is thin (2 commits), and it closes a 3-version rewrite narrative. | `Desktop\astraspacegameweb\infra\` |
| 4 | **astra1** (Helios, multi-tenant ops sim) | Next 16 on **raw Postgres** (not an ORM), OTel (`src/instrumentation.ts`), `api/metrics`, audit trail, sagas/outbox, CI. It is the best SQL-performance lab. | `Desktop\astra1\src\` |
| 5 | **aicallhelper** (AI Call Assistant v3, Tauri/Rust) | A real product you use, with latency budgets, 17 ADRs, ~570 tests and CI. It is the strongest AI-integration and differentiation story. Decide canonical vs aicallhelper5 (v4). | `Desktop\aicallhelper\docs\adr\` |

Near-miss: **master1** (GlobalWork EOR: NestJS, Testcontainers, payroll locking). It is excellent, but it duplicates atlas's domain.

## 5. High-value training projects
| Project | Teaches |
|---|---|
| master1 | TS backend twin of atlas: Testcontainers integration tests, outbox, payroll locking under concurrency |
| buildevent | queues (BullMQ), Stripe webhooks, signed QR, Redis; ideal load-spike lab |
| buildermentor (ShipShape) | RAG, pg-boss jobs, LLM cost guardrails, TanStack; AI-backend design |
| pulse (gitvg) | event ingestion, `load/` dir, PG→ClickHouse arc; data-intensive design |
| bazaar (gitvg) | caching, observability/perf/deploy dirs |
| astra5 (Stockade) | polyglot Next + .NET service, inventory sagas, strongest security doc |
| aaa1 | multi-tenant CRM with a worker, 21 architecture/roadmap docs |
| globehire / meterforge | .NET modular monoliths with planted-flaw ledgers (IDOR, rounding, idempotency regen) |
| perch | ATS with a 5-flaw ledger, a11y audit, incident exercise |
| grokbuildmultitenantproject | tenant-isolation vulnerability fixed, with a regression test |
| tagalog | web + mobile + API monorepo with CI and real remotes; a shipping story |
| opusboot1 (DevPractice) | sandboxed code execution (QuickJS-WASM), CSRF, e2e |
| lucasrouter | frontend perf with measured Lighthouse numbers |
| HNJOBTRACK | FastAPI + Supabase RLS + Next + OpenAI |
| borrowbox | graded .NET teaching ramp (good .NET warm-up) |

## 6. Open-source reference codebases (study deeply)
★ **Outline** (Koa/Sequelize/Yjs; 4-wave curriculum), ★ **eShop** (.NET Aspire/gRPC/RabbitMQ; 72 graded stories), ★ **Twenty** (metadata-driven CRM),
★ **OpenStatus** (Next/Hono/Go/Tinybird; reliability capstones), ★ **OrchardCore** (.NET multi-tenant; best reading paths),
★ **modular-monolith-with-ddd**, ★ **Infisical** (best architecture critique).
Paired studies: **Plane vs Teable** (CRDT vs OT) and **NextCRM vs Twenty** (fixed schema vs metadata-driven).
Security case studies: NextCRM (real IDOR CVE), Umami (`orderBy` SQLi), Paperless-ngx (SSRF), Plane (CSRF off), pretalx (TOCTOU).
**OpenSlides** is the only real microservices OSS; **rn1** (Bluesky) is the largest RN codebase.
No investment: Novu, Supabase, ToolJet, Typebot, Indico (no curriculum); Umbraco, jellyfin (minimal).

## 7. Best existing educational material
See EDUCATIONAL_CONTENT_INDEX.md. Top 5:
1. Outline `fabledocs`–`fabledocs4`.
2. eShop `astra/` graded stories.
3. Infisical `fable-docs/` architecture critique.
4. Twenty/OpenStatus 4-pass packs.
5. gitjira-app `docs/`.

Also reuse `AstraOrganized2\fablereview\LEARNING_PATH.md` (the CRUD-reliability path, already curated) rather than re-deriving it.

## 8. Duplicate project clusters
See DUPLICATE_CLUSTERS.md (20 clusters). The biggest:
- **generated CRUD corpora** (~270 folders).
- **help desk** ×12, **issue tracker** ×12, **e-commerce** ×13, **EOR** ×7.
- **AI copilot** ×5 versions, **Jeopardy** ×5.
- **Tagalog** ×4, **Warband** ×4.
- exact duplicates: **astraboot1 ≡ opusboot1**, **master6 ≡ master7**, **AstraOrganized ≡ project-inventory**.
- **geminiorganized**, a stale ~80-project mirror.

## 9. Skill coverage matrix
See SKILL_MATRIX.md (≈55 skills with counts, depth, best example and gap).

## 10. Overrepresented skills
1. CRUD with React + Node/Next + ORM + Postgres (≥150 folders).
2. Tenant/owner-scoped authorization (dozens of lessons).
3. CRUD-level transactions and races: `FOR UPDATE`, version columns, unique-key idempotency.
4. ORM usage (84 records).
5. Reading generated curricula (≈275 packs).
6. Generating SaaS clones.

**You have hit diminishing returns on all six.**

## 11. Missing / underrepresented skills
Ranked by how much each blocks senior readiness:
1. Cloud deploy (AWS 3 / Azure 3 records, nothing live).
2. SQL Server (2).
3. Indexes and query plans (5).
4. Zero-downtime migrations (1).
5. Metrics, tracing and SLOs you operate (11, none exercised).
6. Performance investigation (6).
7. Incident response (9, all generated).
8. Backward-compatible API evolution (7).
9. Frontend perf, a11y and testing (4 / 4 / 8).
10. Authoring design docs yourself.
11. Operating a distributed system (only read: eShop, OpenSlides).
12. Code review of other people's work, and upstream contributions (0).

Host mapping: GAP_ANALYSIS.md §1.

## 12. Outdated patterns (older AI-generated code)
- A hardcoded JWT-secret fallback copied across 7 repos.
- A "session token = user id" regression in the VGdemo .NET port.
- Models reskinned by namespace only (JS1 `*-dotnet`).
- Copy-pasted `package.json` descriptions (grokbuild*).
- "Testing strategy" docs with zero tests (.netramp, .netstripe, all 50 newcodex3 dirs).
- Scaffolds presented as apps (buildecom, buildCRMPYJS, jstrain3 deskpilots).
- A test that runs `db:push` on the dev DB (e13).
- Secrets in working trees.
- Heavy Clean Architecture layering on small CRUD apps (Net-fleet).
- vg: half its Prisma schema has no code, and its outbox only logs.

Newer Opus/Fable builds are clearly better: domain-level tests, measured claims, honest READMEs. Evidence: GAP_ANALYSIS.md §2.

## 13. Modernization candidates
**Worth it:**
- **atlas:** SQL Server, Azure, contract tests.
- **gitjira-app:** AWS deploy, expand/contract migration, SLOs.
- **buildevent:** load and back-pressure work.
- **tagalog:** actually ship it.
- **grokbuildmultitenantproject:** commit, then add Postgres RLS.

**Not worth it:** the numbered experiments, newcodex3/newcodexJS/JS1, most of the Net-fleet, jstrain* apps, recipe/jeopardy.

## 14. Exercise candidates
- **Planted-flaw ledgers:** globehire, meterforge, perch, gitvg harbor/pulse/atlas.
- **Ready-made bug lists:**
  - vg's `fable/02` punch list: BigInt 500 after commit, payslip path traversal, cross-tenant ID trust, locked users can log in.
  - Review Board's 25 security user stories.
- **Comparison and fix-review exercises:**
  - VGdemo's TS vs .NET regression.
  - rewritepy2js's IDOR.
  - anti*'s JWT fail-closed.
  - buildaffiliate's Redis-TTL bug and unauthenticated postbacks.
- **Debugging and testing:**
  - obsidian-claude broken build.
  - characterization tests for newcodex3/.netramp/.netstripe.
  - grokbuild* "starter → hardened" diffs.
  - the fablereview 9 REWORK projects.
- **Reliability drills on real code:** Outline, OpenStatus, Twenty fire drills.

Full list: GAP_ANALYSIS.md §3.

## 15. Interview value (strong stories, not just technologies)
| Project | Story it can produce |
|---|---|
| gitjira-app | "Took an app to production on AWS, ran a zero-downtime column migration under load, wrote the postmortem when X broke" |
| atlas | "Designed idempotent payment/payroll APIs with an outbox; evolved V1→V2 without breaking clients; tuned SQL Server queries via execution plans" |
| astraspacegameweb | "Instrumented with Prometheus/Tempo, ran chaos tests, found and fixed Y; refresh-token rotation with reuse detection" |
| astra1 | "Multi-tenant Postgres performance: found the slow query with pg_stat_statements, fixed with a composite/partial index, proved it with EXPLAIN" |
| aicallhelper | "Rewrote an Electron app in Tauri/Rust across 4 generations to hit a ~1s latency budget; ADR-driven trade-offs" |
| VGdemo / rewritepy2js / grokbuildmultitenant | "Caught an authorization regression introduced by a port / an IDOR / a tenant-isolation hole, and locked it with a regression test" |
| Warband chain | "Postmortem of v1, rewrite decisions, what I'd do differently" |
| Upstream PR (Outline/Twenty/OpenStatus) | "Navigated a 100k-line unfamiliar codebase and landed a change reviewed by maintainers" |
| aiheartbeat / fablereview | "How I run coding agents with human verification: an adversarial review caught a `Bash(gh:*)` injection hole" |

## 16. Recommended learning portfolio (the small subset)
- **Build/operate (5):** gitjira-app, atlas, astraspacegameweb, astra1, aicallhelper.
- **Drill (6):**
  - flaw ledgers (globehire/meterforge/perch)
  - vg punch list
  - Review Board stories
  - VGdemo port regression
  - Outline fire drills
  - eShop graded stories
- **Read (7):** Outline, eShop, Twenty, OpenStatus, OrchardCore, modular-monolith-with-ddd, Infisical critique.
- **Fundamentals upkeep (as needed):** fablereview LEARNING_PATH, unionboot, jstrain2.2, and the C# trio.
- **Everything else:** reference or archive.

## 17. Prioritized roadmap
| Bucket | Contents |
|---|---|
| **NOW** | Week-0 hygiene (revoke token, commit work) → **gitjira-app** production track (AWS, zero-downtime migration, SLOs, own ADR/postmortem) + **atlas** .NET track (SQL Server plans, Azure deploy, V1/V2 contract tests) |
| **NEXT** | **astraspacegameweb** (observability + fire drills), **astra1** (Postgres perf), **Outline** (fire drills + 1 upstream PR), **eShop** (distributed failure lab) |
| **LATER** | buildevent (load/queues), aicallhelper (AI evals/latency), buildermentor (RAG evals), frontend perf/a11y on lucasrouter/gitjira-app web, weekly timed exercise rotation, spec-first agentic workflow |
| **REFERENCE** | OSS list in §6, C# trio, JSTut |
| **ARCHIVE** | numbered experiments (except rn1/z1/z3/g1/X1/B1), newcodex3, most newcodexJS/JS1, grokjs/groktuts/trainjs, empty dirs, geminiorganized, AstraOrganized, superseded versions, bare OSS clones |

Details: PRIORITY_ROADMAP.md.

## 18. Top 10 highest-value next actions
1. **Revoke the Shopify admin token** in `Desktop\AstraOrganized2\astra-remaining-improvements\backups\cf8875344b43\scripts\populate-metaobjects.js`, then check `buildreviewer\.env` and `vg\.env` for real secrets.
2. **Commit the uncommitted work** in the seven `grokbuild*project` folders (all fixes after 2026-07-18 are uncommitted). Confirm that gitjira-app, atlas, astra1, astraspacegameweb and aicallhelper are pushed.
3. **Use gitjira-app as the production lab.** Wire its existing `.github\workflows\deploy.yml` to AWS (ECS Fargate + RDS). Keep it running for 30 days and write your own ADR for the hosting choice.
4. **Run a zero-downtime expand/contract migration on gitjira-app.** Rename a hot column while a k6 script hammers the API, backfill with a BullMQ job, and write the runbook.
5. **Make atlas the SQL Server/.NET lab.** Add a SQL Server EF provider profile and seed 1M payroll rows. Capture execution plans for the 2 slowest endpoints, fix them with indexes, and record before/after latency.
6. **Protect atlas's existing V1/V2 API contracts with contract tests.** Then ship a V3 change behind a deprecation header. This is your backward-compatibility story.
7. **Use astraspacegameweb's observability stack for real** (`infra/tempo.yaml`, Prometheus/Grafana). Define 2 SLOs with alerts, run its chaos tests, and write a postmortem for each alert that fires.
8. **Do one Postgres performance investigation on astra1** (raw SQL, multi-tenant). Enable `pg_stat_statements`, keep an EXPLAIN (ANALYZE, BUFFERS) journal, and ship one index change backed by numbers.
9. **Land one upstream PR** in Outline, Twenty or OpenStatus. The existing curricula list good first tickets (e.g. Umami `fabledocs\06-contribution-practice\01-good-first-tickets.md`). Do Outline's fabledocs4 fire drills first.
10. **Start a weekly 60-minute exercise rotation**, fixing each bug before reading its answer:
    - globehire/meterforge `FLAW-LEDGER.local.md`
    - vg `fable/02` punch list
    - Review Board `User Stories/`
    - VGdemo .NET auth regression
    - anti* JWT fail-closed
    - obsidian-claude broken build

    Stop generating new CRUD apps and curriculum packs until actions 3–8 are done.

---
*Caveats: batch audits were read-only structural passes (manifests, READMEs, docs, 2–4 key source files per significant project). Agent claims were spot-checked for the 5 flagships. The only material correction: atlas has 119 test files and 16 commits (a batch agent reported 139). Items marked UNKNOWN / NEEDS DEEPER INSPECTION in batch files include agora's thin history (8 commits), missioncontrol's completeness, whether aicallhelper5 surpasses aicallhelper, the lineage of the 5 apply-bots, the netsnapshot vs netairag "NetAiOps" naming, and whether the gitvg "Meridian" SPEC was ever built.*
