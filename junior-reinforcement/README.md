# Ten-project junior reinforcement path

New material added 2026-09-26 to complement the existing Opus apprenticeship. Begin with projects 1–4; use 5–10 after you can trace requests, explain state, and write a focused test. Each pack takes roughly 4–6 hours in addition to the existing material; repeat sessions as needed.

| Order | Open the project pack | New emphasis |
|---|---|---|
| 1 | [RouteIQ / lucasrouter](<../../lucasrouter/reinforcement/README.md>) | Derived state, identity, and immutable transformations |
| 2 | [Perch](<../../perch/reinforcement/README.md>) | Async UI state and stale-response protection |
| 3 | [Grok multitenant project](<../../grokbuildmultitenantproject/reinforcement/README.md>) | HTTP input parsing and trustworthy runtime contracts |
| 4 | [GitJira](<../../gitjira-app/reinforcement/README.md>) | Cache identity, mutation effects, and precise regression tests |
| 5 | [Bazaar](<../../gitvg/bazaar/reinforcement/README.md>) | Deterministic time, cache contracts, and honest test doubles |
| 6 | [Helios / astra1](<../../astra1/upskilling/reinforcement/README.md>) | Stable pagination and query-result reasoning |
| 7 | [aaa1 CRM](<../../_Organized Desktop/12 Other Projects/aaa1/reinforcement/README.md>) | Import previews, normalization, and row-level validation |
| 8 | [BuildEvent](<../../buildevent/reinforcement/README.md>) | Checkout-derived state and boundary arithmetic |
| 9 | [ShipShape / buildermentor](<../../buildermentor/reinforcement/README.md>) | Evaluation arithmetic and evidence-backed AI quality claims |
| 10 | [Warband / astraspacegameweb](<../../astraspacegameweb/reinforcement/README.md>) | Realtime hints, authoritative reads, and lifecycle cleanup |

Every pack contains a source map, focused foundations, an executable lab with a deliberately unfinished starter, independent contract tests, sealed reference code and reasoning, an app transfer exercise, a review challenge, and a checkpoint with spaced repetition.

## Start here

Read the [practice protocol](PRACTICE_PROTOCOL.md), open RouteIQ's pack, then use the [tracker](TRACKER.md). Do not read ten packs before attempting the first lab. The labs run independently with Node, so unavailable Docker or application dependencies need not block the fundamentals practice.

## Relationship to the existing curriculum

Existing `learn/`, `training/`, `astraupskill/`, `docs/`, and other learning trees are preserved. Helios's new pack is under `upskilling/reinforcement/` to follow its repository rules; the other nine use root `reinforcement/`. Existing incident branches and answer keys remain separate.

The new work emphasizes missing bridges: derivation and immutability; asynchronous state; input parsing; precise cache invalidation; deterministic time; stable pagination; import validation; server-authoritative checkout state; evaluation arithmetic; and realtime recovery reasoning. Advanced outbox, RLS, performance, and incident material is linked rather than rewritten.

Author verification is recorded in [VALIDATION.md](VALIDATION.md). It covers these teaching artifacts, not a fresh build or operational audit of the ten applications. Human mastery remains unassessed.
