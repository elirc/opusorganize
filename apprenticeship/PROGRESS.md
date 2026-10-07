# Apprenticeship — Progress Log
Resume rule: read this file; for the current batch, any project without `batch1report/projects/<name>.md` still needs its agent re-run (brief: `apprenticeship/B01_AGENT_BRIEF.md`).

> **Incident-branch availability (checked on GitHub 2026-10-06 via `gh api …/branches`):** only **21** of the 92 `training/incidents/*` branches below are on GitHub.
> - **On GitHub:** dotnet-stripe (001, 002), astraspacegameweb (001–005), buildermentor (001–005), helios-interplanetary (= astra1; 001, 002), aicallhelper (001, 002), aiheartbeat (001, 002), globehire (001, 002), stockade (= astra5; 001).
> - **None pushed:** every other repo has no `training/*` branches on GitHub, including the `training/base/*` and `training/lab/*` bases that some labs depend on. This covers netdrop, netintercom, netramp, netauth, eShop, modular-monolith, gitjira-app, atlas, pulse, perch, bazaar, lucasrouter, outline, buildevent, relay, folio, aaa1, HNJOBTRACK, grokbuildmultitenant, meterforge, VGdemo and vg.
> - **What to do:** the `training/` docs on `main` still describe those incidents, but the bug branches exist only in local clones, if anywhere. From a fresh clone, rebuild an incident from its ticket and sealed answer, or treat it as a reading exercise.

## B01 — Desktop .NET projects (started 2026-09-23)
Tiers (chosen by Claude, user reviews in batch1report/REPORT.md):
- LAB: netdrop, netintercom
- DRILL: .netstripe, .netramp, netauth
- READ: netopen1/eShop, .netarchitectureproject/modular-monolith-with-ddd
- SKIP: netairag, netdocu, netlinear, netnotion, netshop (Net-fleet CRUD dups of netdrop/netintercom); OrchardCore, CleanArchitecture (existing EXCELLENT curricula = KEEP); Umbraco, jellyfin, nopCommerce, eShopOnWeb (huge/low marginal value); netsnapshot, netsnapshot1, csharptut, c#interview, csbootcamp (already curricula = KEEP); .nethris (empty)

| Project | Tier | Status |
|---|---|---|
| netdrop | LAB | [x] 7329298; 5 incidents build-verified |
| netintercom | LAB | [x] 467ab4a; 5 incidents build-verified, unit 27/27 on 004/005; integration tests need Docker (not run) |
| .netstripe | DRILL | [x] b0e5001; incidents build-verified; NOTE main does not compile (2 pre-existing errors; incident branches bundle 1-line fixes) |
| .netramp | DRILL | [x] d89be45; incidents build-verified; char-test verified 14/14 -> 3 fail on inc 001 |
| netauth | DRILL | [x] 9e39ddd; incidents 001/002 BUILD UNVERIFIED (global.json pins SDK 8, only SDK 10 installed) |
| eShop | READ | [x] commit 6c9ebc5 (set repo-local git identity) |
| modular-monolith-with-ddd | READ | [x] a7d111a (found outbox re-publish new-Guid duplicate gap) |
| Phase 6 consolidation (graph, curriculum, gap report, REPORT.md) | — | [x] batch1report/REPORT.md |
- TODO in Phase 6: verify all incident branches build using a temp worktree with global.json rollForward override (not committed).
- Phase 6 (orchestrator): curriculum/ pages 01-05 written (outbox, idempotency, concurrency races, characterization tests, verify-before-trust).
- Build verification netauth (SDK 10 via temp worktree global.json override, not committed): main DOES NOT COMPILE — Program.cs:141 calls nonexistent `Database.GetMigrationsAsync()` (hallucinated EF API). Incident 002 (Application project) builds 0 errors; incident 001 edits Program.cs so blocked by the pre-existing error (1-line change, syntax trivially valid).
- Waiting on: netdrop (LAB).
- B01 COMPLETE 2026-09-23. Next recommended: B02 = gitjira-app + gitvg/atlas (LAB), gitvg/pulse + perch (DRILL).

## B02 — gitvg course repos + gitjira-app (started 2026-09-23)
Tiers: LAB gitjira-app, gitvg/atlas · DRILL gitvg/pulse, perch, gitvg/bazaar (caching focus) · SKIP tracer, relay (durable exec — revisit), folio (CRDT — revisit), harbor, all *-net/*-app rebuilds, agora (8 commits), storefront, gitvg/astra (docs), gitjira (spec), gitvg/docs/tools/prompts.
Brief: apprenticeship/B02_AGENT_BRIEF.md · reports → batch2report/projects/
| Project | Tier | Status |
|---|---|---|
| gitjira-app | LAB | [x] a0b506c+b778462; 5 incidents (001/003/004 run-verified); node_modules left installed |
| atlas | LAB | [x] e85c35a; 5 incidents build + full suite (922/922 baseline); 181 dirty = CRLF churn only |
| pulse | DRILL | [x] 67fb143; 2 incidents (alert severity inversion, rollup fast-path disabled), BUILD UNVERIFIED |
| perch | DRILL | [x] f56f063; 2 frontend incidents, BUILD UNVERIFIED (no deps); sign-in has no credential check |
| bazaar | DRILL | [x] 4d6eb1f; 2 caching incidents (wire unused @bazaar/cache), BUILD UNVERIFIED |
| Phase 6 + batch2report/REPORT.md | — | [x] |
- B02: curriculum/06-caching-correctness.md written (bazaar, pulse, netintercom).
- Lesson: agents must use unique scratch subfolders (atlas/gitjira-app collided on a commit-message file; fixed by atlas agent).
- B02: curriculum 07-10 written (zero-downtime migrations, realtime fan-out, telemetry, query plans).
- B02 COMPLETE 2026-09-23 → batch2report/REPORT.md. Recommended B03: LAB astraspacegameweb + lucasrouter, DRILL astra1, READ Outline.

## B03 — operate + frontend (started 2026-09-24)
Tiers: LAB astraspacegameweb (operate live observability stack), lucasrouter (frontend perf + a11y) · DRILL astra1 (raw-SQL Postgres + OTel) · READ masteroutline/outline (git init baseline; fire drills + upstream-PR prep)
| Project | Tier | Status |
|---|---|---|
| astraspacegameweb | LAB | [x] 2fca582; 5 incidents reproduced on LIVE stack (Docker Desktop started by agent, still running) |
| lucasrouter | LAB | [x] b3ee4c8; 5 incidents measured on prod builds (4 FE-perf/a11y); vitest 167/167 |
| astra1 | DRILL | [x] 9d64e5a; inc 002 = real shipped bug (spans of 401s dropped); plans UNVERIFIED (Docker daemon down) |
| outline | READ | [x] git init baseline 37ca0d5 (master) + training cca361b |
| Phase 6 + batch3report/REPORT.md | — | [x] |
- B03: curriculum 11 (a11y) + 12 (frontend perf) written; page 10 extended with astra1. Waiting on astraspacegameweb.

## B04 — load + AI + agentic (started 2026-09-24)
Tiers: LAB buildevent (load/back-pressure), buildermentor (AI backend) · DRILL aicallhelper (AI latency/failure), aiheartbeat (agentic engineering)
| Project | Tier | Status |
|---|---|---|
| buildevent | LAB | [x] baf46ea; all 5 incidents reproduced w/ measurements (native PG18 + docker Redis, removed) |
| buildermentor | LAB | [x] e6b3925; inc 001-004 run-verified via regression tests, 005 via real pg-boss+PG container |
| aicallhelper | DRILL | [x] 5010b59; inc 001 vitest 51/53, inc 002 cargo test 7/8 (both fail as designed) |
| aiheartbeat | DRILL | [x] fcbf2af; DATA-LOSS incident (recovered, see batch4report §1) |
| Phase 6 + batch4report/REPORT.md | — | [x] |
- B03: curriculum 13 (release safety) written; page 09 extended with PromQL SLO traps.
- B03 COMPLETE 2026-09-24 → batch3report/REPORT.md (graph update deferred to after B04).
- B04: curriculum 14 (load/back-pressure) written.
- B04: aiheartbeat agent's `rm -rf node_modules` followed workspace junctions and deleted packages/*; committed code restored by agent; user's 3 uncommitted WIP files RECOVERED by orchestrator from AstraOrganized2/astra-remaining-improvements/stage/9e1958f807df (exact SHA-256 match to astraupskill/evidence/root-final-source-hashes.json). No-recursive-delete rule added to BATCH_PROMPT + all briefs.
- B04: curriculum 15 (LLM features in production) written.
- B04 COMPLETE 2026-09-24 → batch4report/REPORT.md. Graph rebuilt across B01-B04. Recommendation: stop generating; execute (real cloud deploy, SQL Server on atlas, first Outline PR). Remaining distinct topics: relay, folio.

## B05 — distributed-systems topics (started 2026-09-24)
Tiers: LAB gitvg/relay (durable execution), gitvg/folio (CRDT/offline sync) · DRILL astra5 (sagas across Next + .NET)
| Project | Tier | Status |
|---|---|---|
| relay | LAB | [x] 2cc2ec4; incidents on training/base/engine-boots (main cannot boot: BullMQ rejects queue name); all 5 reproduced live |
| folio | LAB | [x] da45b9c; 5 incidents reproduced; main offline editing broken (property test) |
| astra5 | DRILL | [x] bdd63f9; 1 incident (dotnet build OK); real saga crash-window bug Worker.cs:70-78 |
| Phase 6 + batch5report/REPORT.md | — | [x] |
- B05: curriculum 16 (sagas vs 2PC vs outbox) written.
- B05: curriculum 17 (CRDT & offline sync) written. Waiting on relay.
- B05 COMPLETE 2026-09-24 → batch5report/REPORT.md. Totals: 23 projects, 69 incidents, 18 curriculum pages. No further batch recommended.

## B06 — tenant isolation in the DB + Python (started 2026-09-24)
Tiers: LAB aaa1, HNJOBTRACK · DRILL grokbuildmultitenantproject (incidents on working-tree-snapshot base)
| Project | Tier | Status |
|---|---|---|
| aaa1 | LAB | [x] baseline 0a99ba0 + training ca1986f; base training/base/rls-foundation 4ca048e; 5 incidents live-reproduced on native PG18 |
| HNJOBTRACK | LAB | [x] baseline 2bb1f26 + training 044efd2; 5 incidents test-verified; RLS lab on native PG18 |
| grokbuildmultitenantproject | DRILL | [x] cb03e05; base training/base/working-tree-snapshot 06d0205 (contains user WIP); 2 incidents test-verified on PG18; RLS probe verified |
| Phase 6 + batch6report/REPORT.md | — | [x] |

## B07 — .NET legacy rescue + real SQL Server (started 2026-09-24)
Tiers: LAB meterforge (SQL Server track) · DRILL globehire, VGdemo (TS→.NET port), vg (punch list) · READ reviewboard (security story bank)
| Project | Tier | Status |
|---|---|---|
| meterforge | LAB | [x] 567f53a+9f5023c; lab branch training/lab/sqlserver; 5 incidents build; SQL Server runtime UNVERIFIED (no Docker/LocalDB) |
| globehire | DRILL | [x] 36018f1; 2 incidents (DI captive dependency, time-zone date) reproduced; dotnet test green on branch |
| VGdemo | DRILL | [x] baseline 61367ad (+root .gitignore) + training 1d5af1c; 2 incidents test-verified; parity TS 17/20 vs .NET 13/20 |
| vg | DRILL | [x] baseline 99bb8b2 + training c74a7f0; 2 incidents (mechanisms verified); reference suite NOT yet run (Docker hung) |
| reviewboard | READ | [x] baseline bb3d688 + training 415c038; 25 stories verified: 14 real / 10 handled / 1 unclear |
| Phase 6 + batch7report/REPORT.md | — | [x] |
- 2026-09-24 INCIDENT: C: drive filled to 46 MB free mid-B06/B07; all 7 running agents died (API SSL errors). reviewboard had finished. Freed 1.9 GB via `npm cache clean --force` (now ~1.86 GB free). Big consumers: Docker docker_data.vhdx 7.3 GB, Temp 5.8 GB, NuGet 2.3 GB, pnpm store+cache 2.8 GB, per-repo node_modules installed this session. Agents left partial state (worktrees, training/ drafts, incident branches) — resume each via SendMessage once disk space allows. Awaiting user decision on further cleanup.
- 2026-09-24: freed space → 8.49 GB (npm cache, NuGet locals, pnpm store prune, junction-safe node_modules removal in 8 finished repos: gitjira-app, lucasrouter, astraspacegameweb, buildevent, buildermentor, aiheartbeat, relay, folio — git status verified identical before/after; script scratchpad/safe-rm-nodemodules.ps1). Those 8 repos need npm ci / pnpm install again before running. All 7 B06/B07 agents resumed.
- 2026-09-24: Docker engine never recovered after disk-full; per user choice ("wipe it entirely") killed Docker processes, wsl --shutdown, deleted docker_data.vhdx (7.3 GB; all images/containers/volumes gone), relaunched Docker Desktop → 13.28 GB free. Agents: vg, globehire, grokbuildmultitenant, VGdemo DONE; HNJOBTRACK returned PARTIAL (safety classifier interrupted sealed-answer writing) → resumed with defensive-framing instruction; aaa1 + meterforge still running.
- B06/07: curriculum 19 (RLS), 20 (money & time), 21 (legacy rescue & ports) written.
- B06 COMPLETE 2026-09-24 → batch6report/REPORT.md
- 2026-09-24: Docker did not restart after data wipe — WSL shows NO installed distributions (docker-desktop distro unregistered); Docker Desktop likely waiting on a GUI dialog → USER ACTION needed (open Docker Desktop; Troubleshoot → Restart/Reset). SQL Server LocalDB not installed. meterforge told to finish SQL Server track statically (EF-generated DDL) with exact docker run commands for later.
- B07 COMPLETE 2026-09-24 → batch7report/REPORT.md. Totals B01–B07: 31 projects, 92 incidents, 22 curriculum pages. Docker needs user action (WSL distro gone).
- 2026-09-24: apprenticeship/ADVICE.md written (engineering-beyond-code advice grounded in B01–B07 findings).

## B08 — LEARN PASS (started 2026-09-26)
Goal: junior on-ramp + agentic-era study guide (`learn/` folder) in all 31 B01–B07 repos; docs-only, no installs/builds.
Brief: apprenticeship/B08_LEARN_BRIEF.md · reports → batch8report/projects/ · consolidation report → astradocs/MODIFIED_PROJECTS.md
7 Opus agents launched 2026-09-26, one per batch group (B01–B07). Fable orchestrates/reviews.

> **Status note (added 2026-10-06; this log was not updated after the B08 launch line above).** This repository snapshot (`dce83b8`, 2026-09-29) never records B08 as complete:
> - `batch8report/projects/` holds 4 of the 31 per-repo reports (astra1, astraspacegameweb, netdrop, netintercom).
> - `astradocs/MODIFIED_PROJECTS.md`, which `astradocs/README.md` lists, is not in the repo.
>
> I checked GitHub `main` for `learn/README.md` in all 31 repos, mapped to their elirc names. It exists in 14: dotnet-drop, dotnet-intercom, dotnet-stripe, dotnet-ramp, netarchitectureproject (`modular-monolith-with-ddd/learn/`), gitjira, astraspacegameweb, lucasrouter, helios-interplanetary, masteroutline (`outline/learn/`), aiheartbeat, gitvg (`relay/learn/`), aaa1, meterforge. It was not found in the other 17: dotnet-auth, eShop (netopen1), atlas, pulse, bazaar, folio, perch, build-event, buildermentor, aicallhelper, hnjobtrack, grok-build-multitenant, globehire, vgdemo, vg, stockade (= astra5), gravreviewboardjspy (= reviewboard). For atlas, pulse, bazaar and folio I checked both the standalone repos and the `elirc/gitvg` subfolders.
>
> Treat B08 as **partially delivered**. Missing `learn/` folders may exist only in local Desktop copies.
>
> Several local folder names in this log also differ on GitHub: netX → `elirc/dotnet-X`, astra1 → `elirc/helios-interplanetary`, gitjira-app → `elirc/gitjira`, buildevent → `elirc/build-event`, and the gitvg course `training/` trees are in `elirc/gitvg`.
