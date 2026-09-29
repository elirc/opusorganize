# Duplicate / Overlap Clusters

Nothing has been moved or deleted. Decisions are recommendations for a later consolidation phase. Evidence: batch file in brackets.

| # | Cluster | Members | Keep | Decision |
|---|---|---|---|---|
| 1 | **AI interview/call copilot** | aihelper (v1 Electron) → fableaihelperv3 (v2) → aicallhelper (v3 Tauri/Rust) ‖ aicallhelper2 (v3 Python) → aicallhelper5 (v4 Tauri+React, built off the Python v3 per README) [03] | **aicallhelper** (570 tests, 17 ADRs, CI). Verify whether aicallhelper5 has surpassed it | KEEP BEST VERSION; the older versions stay as the "rewrite lineage" story |
| 2 | CueDeck | fableaihelperv2\cuedeck (older) vs finalcallhelp\cuedeck (newer; `diff -rq` confirmed) [03] | finalcallhelp | ARCHIVE older |
| 3 | **EOR / global workforce** | gitvg\atlas (.NET), atlas-net, master1 (NestJS), vg (Next, unfixed security bugs), VGdemo/globalhire-lite (+ .NET port), netsnapshot1 "Atlas Global Workforce", gitvg\SPEC.md "Meridian" (unbuilt), .nethris (empty) [02,10,14,01] | **atlas** (.NET) + **master1** (TS) | KEEP 2; VGdemo + vg → EXERCISE (security regressions); others ARCHIVE |
| 4 | **Help desk / support / inbox** | grouphelpdesk, buildagenthelpdesk, antihelpdesk, gitvg\harbor(+harbor-net), netintercom, newcodecjs2\helpkit, jstrain3\deskpilot-clean, master3, e15, ww39, zz3, grokbuildsupportproject (plan) [02,06,09,10,12,13,14] | harbor (course) + netintercom (.NET/SignalR) | REPURPOSE rest AS EXERCISES / ARCHIVE |
| 5 | **Issue/project tracker** | gitjira-app, gitjira (spec), tracer(+tracer-net), netlinear, newcodecjs2\planr, buildjira, buildasana, jdtrrain2.1, appmakertrack, grokbuildppmproject, ww4, ww46 [02,01,06,09,14,13] | **gitjira-app** | ARCHIVE MOST (tracer stays as the course reference) |
| 6 | **E-commerce** | gitvg\bazaar(+bazaar-app), gitvg\storefront, MasterStore, netshop, grokbuildecommerceproject, buildecom (scaffold), astra5 Stockade, newcodexJS\13, e13; OSS: eShop, eShopOnWeb, nopCommerce, Saleor [02,01,06,07,09,11,13] | bazaar + astra5; eShop (reference) | ARCHIVE MOST |
| 7 | **CRM** | aaa1, buildCRMPYJS, master3, zz1, ww48; OSS: NextCRM, Twenty, IDURAR [14,09,10,13,11] | aaa1; Twenty + NextCRM as reference pair | ARCHIVE MOST |
| 8 | **Learning/practice platforms** | opusboot1 ≡ astraboot1 (same DevPractice spec, two pipelines), skillforgejs, JSProjectLearn (SkillForge Quest), buildsql (IPSKILL), jsdrillapp\reps ≡ jsdrill_sync_20260223_125137, ankijs, devdeck, buildermentor [06,05,07,04,12] | opusboot1, JSProjectLearn, buildermentor | CONSOLIDATE (astraboot1, jsdrill pair, skillforgejs, devdeck) |
| 9 | **Fundamentals curricula** | jstrain2.2, unionboot, grokjs, groktuts, JSTut, trainjs, csharptut, csbootcamp, c#interview, JS1 [12,05,07,01] | unionboot (exercises), jstrain2.2 (bootcamp), JSTut (reference), C# trio | ARCHIVE grokjs/groktuts/trainjs (overlap) |
| 10 | **Tagalog (Aral)** | tagalog, aral (v3 rebuild, stalled), mobiletagalog (port), aral-deploy (content snapshot) [04] | tagalog | KEEP SEPARATE aral only as a "local-first sync" experiment |
| 11 | **Warband strategy game** | spacegame (v1) → spacegamev2 (rebuild + postmortem) → astraspacegameweb (browser, ops stack); stellar-conquest(+architecture doc); astra-space-rebuild-prompt.md [05,14,08] | **astraspacegameweb** | Present as ONE rewrite narrative; archive v1 |
| 12 | **Job tracking / auto-apply** | jobtrack, calendar+jobtrack, `08 App\job track` (bucket of 5), HNJOBTRACK, Desktop\aiapplybot, 06 AI\aiapplybot (ApplyPilot fork), aiapplybotjs, eliapplybot, eliapplybot-python [04,14,12,03] | HNJOBTRACK (web) + one apply-bot (eliapplybot-python) | CONSOLIDATE jobtrack→calendar+jobtrack; lineage-check the 5 apply-bots |
| 13 | **Jeopardy game** | curse\Jeopardy-Game, appmaketrck\Jeopardy-Game, finaljepgame, FinalJep, ~\jeopardy-game-refactor [14] | jeopardy-game-refactor (has git history) | ARCHIVE rest |
| 14 | **LMS / education ops** | master6 ≡ master7 (same @lms/*), buildagentteaching vs buildagentteachGEM, ww14; OSS: Open edX [10,09,13,11] | master7, buildagentteachGEM | ARCHIVE master6 |
| 15 | **Generated CRUD corpora** (overtraining) | 05 Numbered Experiments (~78), newcodexJS (20), newcodex3 (50, zero tests), JS1 (~97, `*-dotnet/Models.cs` reskinned), grokbuild* (7), anti* (4), Net-fleet (10), gitvg fleet (15), build* (13), jstrain* (7) [all] | only the ~30 items in fablereview LEARNING_PATH | ARCHIVE MOST / REPURPOSE AS EXERCISES |
| 16 | Recipes | recipeview, recipeweb, recipegen → recipegen-temp → recipegen-app, newcodexJS\05 [04,14] | recipeview | ARCHIVE rest (not duplicates, just low value) |
| 17 | obsidian-claude | ~\obsidian-claude (broken entrypoint) vs 12 Other\appmaketrck\obsidian-claude [14] | diff first | EXERCISE (debug the broken build) |
| 18 | HyperNova | hypernova-inc-main → 3buildhyper [14] | 3buildhyper | ARCHIVE baseline |
| 19 | pretalx | O\03\masterpre vs O\09\grav1pretalx (same source, different curricula) [11,14] | masterpre | CONSOLIDATE curricula |
| 20 | **Meta / prior audits** | AstraOrganized ≡ project-inventory (byte-identical), AstraOrganized2 (fablereview + tooling), geminiorganized (stale ~80-project mirror), antigravupskill (59 reviews), readme/, claude docs ≈ GPTDocs, and this portfolio-audit [08,06] | fablereview + this audit | ARCHIVE the rest (geminiorganized = big disk reclaim) |

## Why this matters
Clusters 3–7 and 15 show the same product being generated 5–15 times in different skins. Building a fourth help desk or a sixth EOR app would
teach you almost nothing new. Future effort should go **deeper on one member** (operate it, break it, scale it) rather than wider.
