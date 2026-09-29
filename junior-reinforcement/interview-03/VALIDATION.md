# Interview expansion verification

Verified 2026-09-28 using Node v22.16.0.

## What was added

- 316 new files across the ten project interview folders and this central guide.
- 60 distinct project scenario briefs, each practiced in eight interview rounds: **480 scenario/round combinations**, with 480 corresponding interviewer sections. Common round instructions are presented once per round; the repeated round structure supports cross-project comparison.
- 10 distinct new executable coding challenges, 30 timed mock-interview scripts with separate interviewer notes, project-defense worksheets, study plans, and scorecards.
- A shared 40-question interview-foundations guide and links to reviewed primary references.

## Executed checks

- All 10 reference challenges ran together: **70 tests passed, zero failures**.
- All 10 starters ran separately from reference selection: **70 expected failures, zero passes**. Each failure includes the intentional `Not implemented` starter error. The learner's solutions remain unfinished.
- The documented individual reference invocation was also checked for the first project: seven tests passed. This repeats those cases; it is not counted as seven additional distinct tests.
- New-file hashes, Markdown code-fence pairing, all local links, source-map targets, scenario/answer pairing, and content counts checked. Final link count is recorded in the manifest after inclusion of this report.
- **2,502 existing files match the pre-change SHA-256 snapshot.** The snapshot covers selected source/configuration/documentation extensions in the ten repositories plus the complete previous central learning index. Dependency/generated/internal operational directories and files larger than 8 MB were excluded. This is a scoped preservation check, not a complete disk backup.

## Five-times content target

The baseline includes both earlier reinforcement blocks in each project. The added interview block is at least five times that baseline's Markdown word count for every project; the final combined pack is therefore more than six times its previous size. Counts use the same word-token expression before and after. Runnable code and central shared guides are excluded from these project-level word totals.

| Project | Previous words | Added words | Combined words | Added / previous | Combined / previous |
|---|---:|---:|---:|---:|---:|
| RouteIQ / lucasrouter | 6,053 | 33,901 | 39,954 | 5.60x | 6.60x |
| Perch | 5,794 | 33,610 | 39,404 | 5.80x | 6.80x |
| Grok multitenant project | 5,703 | 33,259 | 38,962 | 5.83x | 6.83x |
| GitJira | 5,752 | 33,773 | 39,525 | 5.87x | 6.87x |
| Bazaar | 5,609 | 33,689 | 39,298 | 6.01x | 7.01x |
| Helios / astra1 | 5,736 | 33,519 | 39,255 | 5.84x | 6.84x |
| aaa1 CRM | 5,849 | 33,500 | 39,349 | 5.73x | 6.73x |
| BuildEvent | 5,690 | 33,206 | 38,896 | 5.84x | 6.84x |
| ShipShape / buildermentor | 5,662 | 33,364 | 39,026 | 5.89x | 6.89x |
| Warband / astraspacegameweb | 6,216 | 33,377 | 39,593 | 5.37x | 6.37x |

These are content-volume counts, not a count of unique concepts or estimated learning improvement. Scenarios are reused across interview roles intentionally, and the common assessment structure appears in all projects. The library is designed for selective practice, not reading every page in sequence.

## Evidence limits

The executable checks establish synthetic JavaScript teaching contracts. No application code was changed, no existing tests were weakened, and no application build, browser workflow, TypeScript compilation, database integration, provider call, or proposed capstone was run for this content expansion. Historical application evidence remains attributed to its original record. Human mastery and interview readiness remain unassessed.

From a project's coding folder, run `node --test check.mjs` for the learner solution or `node check.mjs --reference` for the separate reference. Use the project's scorecard to record independent reasoning, help used, changed-input follow-ups, and actual evidence.
