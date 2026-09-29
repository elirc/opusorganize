# Verification report

Verified on 2026-09-28.

- Ten project packs, nine new files each; eight shared files including this report and the manifest: **98 new files**.
- Thirty hypothetical project capacity calculations plus four shared/boundary checks: **34 passed, zero failed** with `node --test tools/check-capacity.mjs` from this folder.
- The checks caught and corrected the CRM polling worksheet: 500 active clients making two reads per minute produce approximately 16.67 requests per second.
- 238 local Markdown link occurrences resolve, excluding the forward link to this report while it was being generated; that target is now present.
- Markdown code fences are paired. Ten Mermaid architecture blocks are present; diagrams were not rendered or parser-tested.
- **3322 pre-existing files** in the fresh preservation snapshot retain their SHA-256 hashes. This snapshot covers the earlier selected application/configuration files and learning content, not an exhaustive inventory of every repository file.
- Each decision record includes a viable alternative, its cost, and a condition for reconsidering the choice. Current-source observations and proposed architectures remain explicitly separate.

The new folders contain teaching documents, worksheet data, and an offline arithmetic calculator. These checks do not establish application throughput, concurrency correctness, deployment readiness, provider behavior, or learner mastery. No application build, migration, browser scenario, database integration test, or live provider call was performed for this documentation addition.

The [manifest](manifest.json) lists hashes for all new files except itself. See the [study route](README.md) for all ten cases.
