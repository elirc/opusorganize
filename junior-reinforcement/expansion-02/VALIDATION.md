# Expansion verification

Verified 2026-09-28 with v22.16.0.

- **20 new reference labs: 120 tests passed, zero failures.** Both checks for every project ran in one Node process with the reference flag.
- **20 learner starters: 120 expected failures, zero passes.** Every failure reports `Not implemented`; starters remain unsolved for practice.
- **2,338 pre-existing source, configuration, and learning files match their pre-expansion SHA-256 snapshots.** The snapshot covers selected text/code extensions under the ten repositories plus the original central index, excluding dependency/generated/internal operational directories and files larger than 8 MB. This is a scoped preservation check, not a backup of every filesystem object.
- Local Markdown links, source-map targets, code-fence pairs, and the new-file inventory checked. The final local-link count is recorded in the manifest after this report is included.
- 16 new files per project, plus four central navigation/tracking/manifest/verification files: **164 new files**. Existing files were retained.

## Measured content growth

Counts use the same word-token expression over Markdown in each original reinforcement pack and its new expansion. They exclude runnable JavaScript, the central index, and the larger existing Opus curriculum outside these reinforcement packs. The total is the original block plus this new block.

| Project | Before | Added | New total | Total / before |
|---|---:|---:|---:|---:|
| RouteIQ / lucasrouter | 2,149 | 3,904 | 6,053 | 2.82x |
| Perch | 2,070 | 3,724 | 5,794 | 2.80x |
| Grok multitenant project | 2,046 | 3,657 | 5,703 | 2.79x |
| GitJira | 2,038 | 3,714 | 5,752 | 2.82x |
| Bazaar | 1,954 | 3,655 | 5,609 | 2.87x |
| Helios / astra1 | 2,108 | 3,628 | 5,736 | 2.72x |
| aaa1 CRM | 2,096 | 3,753 | 5,849 | 2.79x |
| BuildEvent | 2,020 | 3,670 | 5,690 | 2.82x |
| ShipShape / buildermentor | 1,977 | 3,685 | 5,662 | 2.86x |
| Warband / astraspacegameweb | 2,120 | 4,096 | 6,216 | 2.93x |

## Scope of the evidence

The checks exercise deterministic teaching contracts with synthetic inputs. They do not run application builds, browser flows, databases, payment providers, live model calls, or proposed capstones. Reference success is author verification, not evidence that a learner completed the starters. Human mastery remains not assessed.

Run a lab from its own folder with `node --test check.mjs` for the learner solution or `node check.mjs --reference` for the sealed answer. Each project's README maps the additional application verification needed before making stronger claims.
