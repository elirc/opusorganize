# netintercom: B08 learn pass

- **Path:** `C:\Users\Owner\Desktop\netintercom` (LAB tier)
- **Branch:** `main`, the same branch as the B01 training commit `467ab4a`. The tree was clean before and after.
- **Commit:** `1831567` `docs(training): add learn/ study guide + junior on-ramp (B08)`. It's a pathspec commit covering `learn/` and `training/` only (8 files, +562/−2).

## Files added
- `learn/README.md`:
  - what the app is, and a "Known state of main" section (from the batch1report)
  - 6 prerequisites, linked to curriculum 01/02/03/05/06/08/10 and to repo files
  - a 12-session study route, each session with do-by-hand vs delegate-then-verify and an exit criterion
  - a "done" definition, and the next repo (modular-monolith-with-ddd)
- `learn/00-onramp.md`: 9 warm-ups on real code:
  - predicting the `Conversation` state and SLA timers
  - `OfficeHours.IsOpenAt` edge cases (overnight window never matches, silent UTC fallback for an unknown time zone)
  - `PlaceholderRenderer` outputs
  - a visitor first-message trace to both SignalR groups
  - 403 vs 404 ownership checks
  - an index-per-query schema reading, plus the `SlaTimer` that has no concurrency token
  - one characterization test to write and run
  - widget reconnect closure and group loss
  - `PresenceTracker` grace and Away states
- `learn/01-agentic-practice.md`: 4 drills. Each one has a spec template, a trap and adversarial questions:
  - A: INC-004 negative-test matrix
  - B: INC-003 idempotent sweep across replicas
  - C: INC-005 SQL-capture test
  - D: characterization-first before J3

  It also has a NetIntercom verification checklist covering visitor DTO surfaces, ownership checks, DB-level concurrency, multi-replica traps, `EnsureCreated`, base appsettings and fake behavior.
- `learn/_answers/00-onramp.md`, `learn/_answers/01-agentic-practice.md`: sealed answers and Basic/Solid/Strong rubrics.

## Gaps filled
- **Caching (B01 report: "thin, only React Query invalidation"):** new `training/ladder/M5-cache-routing-rules.md` plus sealed `training/_answers/ladder-M5.md`. The ticket is "measure first" on `ConversationRouter`'s rules query. It covers per-replica `IMemoryCache` staleness, office hours and the SLA policy cached by accident through `Include(Team)`, why presence and round-robin must never be cached, cross-replica invalidation options (DB version stamp, LISTEN/NOTIFY, short TTL), and a diagnosis of the inbox React Query over-invalidation.
- `training/README.md`: added a pointer to `learn/`, and updated the ladder and `_answers` counts to 11 and 21.

## Skipped / UNVERIFIED
- This was a docs-only pass: no build, test or npm. I re-read every line number cited in `learn/` and M5 from source on `main`.
- The on-ramp exercise 7 expected count (28 tests) assumes B01's verified 27/27 baseline. It wasn't re-run.
- The M5 latency figures are order-of-magnitude reasoning, and are marked as unbenchmarked in the answer.
- Integration tests (Docker) are still never run. Every drill tells the learner to write "integration UNVERIFIED" without Docker.
- No new incident branches (per the brief).

## Study route (3 lines)
1. Sessions 1–3: read and trace without running (architecture, on-ramp predictions, one characterization test), then the blind review by hand.
2. Sessions 4–9: J1, then security INC-004/001 (drill A), perf INC-005 (drill C), M3 reconnect, the full M2 agentic workflow, and multi-replica INC-002/003 (drill B).
3. Sessions 10–12: trade-offs, the change request and the new M5 caching ticket (drill D), the S1 design doc by hand, and the interview kit with the mock-defense rubric. Next: modular-monolith-with-ddd.
