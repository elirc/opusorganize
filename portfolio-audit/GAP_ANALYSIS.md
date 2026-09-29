# Gap Analysis, Outdated AI Patterns, Exercise & Modernization Candidates

## 1. Undertrained skills → which existing project should teach each

| Gap | Why it blocks Mid→Senior | Best existing host | What to add there (future work, not done) |
|---|---|---|---|
| **Cloud deployment (AWS/Azure)** | nothing you own runs in production; can't tell deploy/rollback stories | **atlas** → Azure (App Service or Container Apps + Azure SQL); **gitjira-app** → AWS (ECS Fargate/RDS) — it already has `deploy.yml` | IaC (Bicep/Terraform), environments, secrets in a vault, rollback drill |
| **SQL Server + query plans** | stated target stack; only 2 records touch it | **atlas** (EF Core; switch provider or add a SQL Server profile) | seed 1–5M rows, capture execution plans, add covering/filtered indexes, compare before/after |
| **Postgres indexing / EXPLAIN** | 5 records; CRUD corpus never measures | **astra1** (raw SQL, multi-tenant) or **pulse** (event ingestion, has `load/`) | `EXPLAIN (ANALYZE, BUFFERS)` journal, partial/composite indexes, `pg_stat_statements` |
| **Zero-downtime migrations** | 1 record | **gitjira-app** (Prisma, CI, real history) | expand/contract rename of a hot column under a running load script; backfill job; feature flag |
| **Metrics / tracing / SLOs** | the infrastructure exists but has never been *used* against a failure | **astraspacegameweb** (Prometheus/Grafana/Tempo, `infra/tempo.yaml`) | define 2 SLOs, alert rules, one dashboard; run its chaos tests and write the incident |
| **Incident response** | postmortems exist only as generated docs | astraspacegameweb chaos + **Outline fabledocs4 fire drills** + gitjira-app `postmortems/` | timed fire drills, write your own postmortem, runbook edits |
| **Performance investigation** | 6 records | **lucasrouter** (Lighthouse/bundle), **pulse** (ingest throughput), **buildevent** (ticket drop spike) | k6 load test, flame graph, fix one bottleneck with before/after numbers |
| **Backward compatibility / API versioning** | 7 records | **atlas** (already has V1/V2 contracts) | contract tests (Pact or snapshot), deprecation headers, client-compat matrix |
| **Distributed system you operate** | microservices only in OSS you've read (eShop, OpenSlides) | **eShop** (Aspire, RabbitMQ) as a lab; or split atlas payroll into a worker + queue | break RabbitMQ, observe retries/DLQ, idempotent consumer |
| **Caching** | 10 records, shallow | **bazaar** (caching dir) / buildevent (Redis) | stampede protection, invalidation on write, cache-hit metrics |
| **Frontend perf / a11y / testing** | 4 / 4 / 8 records | **gitjira-app** web, **lucasrouter** | axe + keyboard audit, React Profiler session, component tests for 1 complex view |
| **Writing design docs** | ~66 records of docs you *read*, near-zero authored by you | any flagship | write one design doc per wave *before* asking an agent to build |
| **Code review of others' code** | fablereview was model-written | 4 bare OSS clones (Novu, Supabase, ToolJet, Typebot) — review real merged PRs there | timed review of 5 upstream PRs, compare with maintainers' comments |
| **Upstream contribution** | 40 OSS clones, 0 contributions found | Outline, Twenty, OpenStatus (curricula already list "good first tickets", e.g. Umami `06-contribution-practice/01-good-first-tickets.md`) | one merged upstream PR = best "unfamiliar codebase" interview story |

## 2. Outdated / old-AI-generated patterns found (with evidence)

| Pattern | Where (evidence) | Teaching use |
|---|---|---|
| **Hardcoded JWT-secret fallback** (`process.env.JWT_SECRET \|\| 'secret'`-style) repeated verbatim | antiemponb, antihelpdesk, antiinv, antitestbuild, vg, jeopardy-game-refactor, stellar-conquest [batch-14] | one portfolio-wide "config fails closed" exercise |
| **Session token = raw user ID** after a .NET port | VGdemo `migrated-dotnet/` [14] | "port regression" security story |
| **Template reskinning** — identical models renamed by namespace | JS1 `asset-depreciation-dotnet/Models.cs` ≡ `board-resolutions-dotnet/Models.cs` [07] | spot-the-generated-code review drill |
| **Copy-pasted manifests** | grokbuild ecommerce/team `package.json` description "Educational HR Platform backend" [07] | — |
| **Testing docs without tests** | .netramp, .netstripe (0 test files, ship "testing strategy" docs) [01]; newcodex3 (50 dirs, 0 tests) [06]; buildevent web `test` script is a no-op echo [04] | "write the missing test suite" exercises |
| **Fake/scaffold presented as app** | buildecom (deps never installed), buildCRMPYJS (no CRUD routes), grokbuildsupportproject (plan only), jstrain3 3× dead deskpilot scaffolds, missioncontrol 4/8 phases [09,07,12,05] | completeness check exercise |
| **Misleading naming** | buildCRMPYJS / buildScedulingPYJS have no Python [09]; "jstrain*" are unrelated apps [12] | — |
| **Tests touching live dev DB** | e13 `commerce.test.ts` runs `db:push`/`db:seed` on collection [08 via fablereview] | test isolation lesson |
| **Secrets in working trees** | Shopify `shpat_` token in `AstraOrganized2/astra-remaining-improvements/backups/.../populate-metaobjects.js`; real `.env` in buildreviewer [08,04] | **action item, not an exercise — revoke** |
| **Broken build shipped as done** | ~\obsidian-claude missing `mcp-server/src/index.ts` [14] | debugging exercise |
| **Work never committed** | grokbuild* (all post-snapshot work uncommitted); most of 02/03/05/07/08/12 have no git at all [07,09,10,11,13,14] | git hygiene; risk of loss |
| **Architecture astronautics** | 4-layer Api/Application/Domain/Infrastructure on small .NET CRUD apps (Net-fleet); .netramp deliberately flat for contrast [01] | "when is Clean Architecture overkill" discussion |
| **Generated doc sprawl** | ≈200 astraupskill packs with template chapters 02/05; duplicate doc trees `docs2.0`, `docsclaude`, `docs-codex-learning` [all] | none — ignore |

Newer-model (Opus/Fable) builds are markedly better: astra1/2/4.2/5, aicallhelper, gitjira-app, lucasrouter show domain-level tests, measured claims
and honest READMEs (several explicitly self-report partial status — batch-09). Older Grok/Codex-era output is where the smells cluster.

## 3. Exercise candidates (debugging / refactoring / review / incident / legacy)

| Source | Exercise type | Starting evidence |
|---|---|---|
| globehire, meterforge `FLAW-LEDGER.local.md` | find the planted bug before reading the ledger (IDOR, money rounding drift, idempotency-key regeneration, non-atomic concurrency) | ledger files |
| perch, gitvg harbor/pulse/atlas (5 planted flaws each) | same, in TS and .NET | FLAW-LEDGER / sprint PRs |
| vg (unfixed security bugs, no tests) | security review + write the tests first; punch list in `vg/fable/02-bugs-and-security.md`: BigInt JSON 500 *after* commit (payroll.service.js:522), payslip path traversal/IDOR (`api/documents/payslips/[id]`), cross-tenant IDs trusted (contract.service.js:154, leave.service.js:130), LOCKED users can log in; ~half the Prisma schema has no code; outbox only logs; committed `.env` | batch-14 |
| Review Board `User Stories/` (US-01..25) | security exercise bank on a mature Django+TS codebase: diff-access guard, self-approval, LocalSite API scoping (IDOR), webhook SSRF, throttling, N+1 | `O\09 Grav\gravreviewboardjspy\reviewboard\User Stories\` |
| VGdemo TS vs .NET port | diff two implementations, find the regression | `migrated-dotnet/` |
| rewritepy2js | reproduce the IDOR (comment delete by id not slug), then read the fix | snapshots + regression test |
| anti* JWT fallback | fail-closed config refactor across 4 repos | batch-14 |
| buildaffiliate | Redis-TTL redirect bug, unauthenticated postbacks | memory + batch-09 |
| buildagentteachGEM | committed `dev.db` drift | batch-09 |
| obsidian-claude | fix a broken build in an unfamiliar TS/MCP repo | missing entrypoint |
| newcodex3 / .netramp / .netstripe | add tests to untested code (characterization testing) | 0 test files |
| grokbuild* originals vs fixed | review diff of "Grok starter → hardened" | uncommitted working trees vs snapshot commit |
| fablereview 9 REWORK projects | legacy-rescue exercises with review already written | `AstraOrganized2/fablereview/SCOREBOARD.md` |
| Outline fabledocs4 fire drills, OpenStatus quorum-flip race, Twenty at-most-once webhooks | incident / reliability drills on real code | fabledocs4 |
| netsnapshot / netsnapshot1 | 15-checkpoint "read the history" exercises | checkpoints |
| rn1 (Bluesky) | navigate a 2,700-file RN codebase and ship one change | batch-13 |

## 4. Modernization candidates (benefit most from a current model pass — later, not now)

| Project | Why | Scope of eventual modernization |
|---|---|---|
| atlas | best .NET base; needs cloud + SQL Server + perf | add Azure deploy, SQL Server profile, load test |
| gitjira-app | real history + CI + docs; needs production ops | deploy, zero-downtime migration, SLOs |
| buildevent | great domain for spikes (ticket drops), but thinner docs and a no-op web test | queue back-pressure, idempotent payments, load test |
| tagalog | has CI and real remotes, unpushed commits | ship to a real host; mobile + web release story |
| grokbuildmultitenantproject | good tenancy story but Grok-era scaffold, uncommitted | commit, then add RLS in Postgres as defense-in-depth |
| master1 | TS twin of atlas with Testcontainers | only if you want a TS backend flagship instead of gitjira-app |

**Not** worth modernizing: numbered experiments, newcodex3, newcodexJS beyond LEARNING_PATH items, Net-fleet beyond netdrop/netintercom,
JS1, grokjs/groktuts, jstrain* apps, recipe/jeopardy apps, geminiorganized.
