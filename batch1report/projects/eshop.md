# eShop (netopen1/eShop) — READ tier

## What was created

Phase 4 only (READ tier), per `apprenticeship/B01_AGENT_BRIEF.md`. No source edits, no incident branches — this
is an OSS clone with an existing `astra/` curriculum and `check_course.py`; I deliberately did not duplicate it.

- `training/README.md` — index, reading order (~2 hrs), points to existing `fabledocs`/`astra`/`fabledoc2` first.
- `training/navigation/00-how-this-pack-fits.md` — KEEP/MERGE/IGNORE verdicts for all three existing doc trees
  and what this pack adds vs. skips.
- `training/navigation/01-checkout-outbox-correctness.md` — a re-verified (not re-explained) guarantee-ledger
  trace of checkout → ordering → outbox (`IntegrationEventLogEF`) → RabbitMQ, organized as "what guarantee holds
  at each step / what defeats it," cross-checked against `fabledocs` Flow 3/6, `fabledoc2` ADR-003, and
  `astra/01-lessons/09-events-and-consistency.md`.
- `training/navigation/02-first-change-onboarding.md` — 1-page first-change primer (DB-per-service, event
  choreography not calls, outbox usage, the publish-failure gap, guarded state machine, 4 validation layers).
- `training/navigation/03-outbox-sweeper-tradeoff.md` — one senior trade-off card (Problem→naive→options A/B/C→
  trade-offs→choice→failure modes→tested/monitored→when-to-revisit) on the concrete gap ADR-003 names but doesn't
  design: no retry for stranded `NotPublished`/`PublishedFailed` outbox rows.
- `training/navigation/04-change-request.md` + sealed `training/_answers/04-change-request.md` — the Phase 4
  "change request" deliverable: place a retry-sweeper feature (files, interface change, per-service vs. shared,
  idempotency risk, tests, failure bound) before implementing. No implementation — this project doesn't get
  source edits.

Commit: `6c9ebc5` on `main`, "training: add B01 apprenticeship materials", staged/committed by pathspec
(`git add -- training`, `git commit ... -- training`). Only `training/` is tracked; `astra/`, `fabledocs/`,
`fabledoc2/` remain untouched/untracked exactly as found. Note: repo had no `user.name`/`user.email` set (local
scope only); I set them locally in this repo (not `--global`) to `elichessmaster@gmail.com` / "Eli (apprenticeship
agent)" so the commit could be created — flagging this since the brief's git rules don't explicitly cover a repo
with no identity configured at all.

## Verification

Re-read (not trusted from existing docs) this pass, 2026-09-23, against baseline `9b4f943`:
- `src/IntegrationEventLogEF/Services/IntegrationEventLogService.cs` (full) and its interface — confirmed
  `RetrieveEventLogsPendingToPublishAsync` is scoped by `transactionId` only, no global/stale query exists.
- `src/Ordering.API/Application/IntegrationEvents/OrderingIntegrationEventService.cs` (full) — confirmed
  publish failures are caught, marked `PublishedFailed`, and swallowed with no rethrow/retry.
- `src/Ordering.API/Application/Behaviors/TransactionBehavior.cs` (partial) and
  `src/Ordering.API/Application/Commands/IdentifiedCommandHandler.cs` (partial) — confirmed transaction wrapping
  and idempotency short-circuit shape matches what `fabledocs` Flow 3 claims.
- `grep -rn "PublishedFailed"` and `grep -rn "BackgroundService"` across `src` — confirmed zero readers of
  failed/stale outbox rows and exactly two `BackgroundService`s in the repo, neither touching the outbox table.
- `grep -rln "IIntegrationEventLogService\|AddIntegrationEventLog\|IntegrationEventLogService<"` — confirmed only
  `Catalog.API` and `Ordering.API` register it, each closed over their own `DbContext`, `AddTransient`.
- `grep -rln "PublishedFailed\|PublishEventsThroughEventBusAsync" tests` — zero hits, confirming no test coverage
  of the failure path (used in the change-request answer to justify requiring a new test).

**Not independently re-verified this pass** (inherited from `fabledocs`/`astra`, both of which independently
agree, but I didn't re-open the file myself): `src/EventBusRabbitMQ/RabbitMQEventBus.cs`'s ack-even-on-exception
behavior, and `Order.cs`'s per-transition status guards. Flagged explicitly in
`01-checkout-outbox-correctness.md` rows 5-6 as cross-checked-not-re-read.
**Genuinely unresolved** (flagged, not asserted either way, in the sealed answer's Q5): whether Catalog's
stock-decrement handler (`OrderStatusChangedToPaidIntegrationEventHandler`) is itself idempotent against a
sweeper's redelivery — a decrement is not naturally safe to replay, unlike the other consumers checked. This is
the deliberate "honest gap" the grading notes reward finding.

## Issues found

- No new secrets found beyond what `fabledocs`/`astra` already document (hardcoded `ClientSecret = "secret"` and
  test card `1111...4444` — both already flagged as sample-only in the existing docs; not re-reported as new).
- Confirmed (not previously stated this precisely elsewhere): the outbox's publish-failure path has **zero test
  coverage** in `tests/`, not just "no sweeper" — worth a line in the competency graph as a testing gap, not only
  a reliability gap.
- Nothing presented as working that isn't, specific to this pass — the three existing doc trees are honest about
  their own uncertainty (`ValidateAudience = false`, `GetOrderAsync` ownership check flagged as "investigate" not
  asserted).

## Skill links (for COMPETENCY_GRAPH.md — not written there, per the brief)

- async jobs/queues/idempotency/outbox → `training/navigation/01-checkout-outbox-correctness.md`,
  `training/navigation/03-outbox-sweeper-tradeoff.md`, `training/navigation/04-change-request.md` +
  `_answers/04-change-request.md`; also `fabledocs/01-codebase-cartography/05-key-flows.md` Flow 3/6,
  `fabledoc2` ADR-003, `astra/01-lessons/09-events-and-consistency.md`, stories ASTRA-049/ASTRA-051.
- design docs/ADRs → `training/navigation/03-outbox-sweeper-tradeoff.md` (sequel-card format); primary source
  `fabledoc2/README.md` (10 ADRs).
- unfamiliar-codebase navigation → `training/navigation/00-how-this-pack-fits.md`,
  `training/navigation/02-first-change-onboarding.md`; primary source `fabledocs/01-codebase-cartography/`.
- testing (unit/integration) → the coverage gap noted above, evidenced in
  `training/navigation/03-outbox-sweeper-tradeoff.md` "How it's tested" and reused in the change-request answer.
- data modeling/transactions/concurrency → `training/navigation/01-checkout-outbox-correctness.md` rows 1-3
  (idempotency + transactional outbox), reinforcing but not duplicating `astra` stage 9 and `fabledocs` Flow 3.

## Curriculum needs (central page candidates, not written)

- **"Transactional outbox pattern: guarantees and failure windows"** — this concept now has near-identical
  writeups in `fabledocs`, `fabledoc2`, `astra`, and this pack, across at least this project. If other batch
  projects (e.g. anything else using an outbox/CDC pattern) recur, this deserves one `curriculum/` page so future
  projects link instead of re-deriving it.
- **"Placing a change in a services-per-database, event-choreographed system"** — the reasoning pattern in
  `04-change-request.md`'s answer (per-service vs. shared component decision, interface-boundary check before
  design) is reusable across any Aspire/microservices-shaped project in the archive.

## Existing learning-doc trees — verdicts

| Tree | Verdict | Why |
| --- | --- | --- |
| `astra/` (72-story bootcamp, 12 stages) | **KEEP** | Richest, most exercise-dense track; stage 9 already covers checkout/outbox directly with stories, a rubric, and a progress tracker. Nothing to merge — it's already structured better than a merge would produce. |
| `fabledocs/` (9-track reference curriculum) | **KEEP** | Deepest evidence-backed flow traces (Flow 3/6 especially) and the only existing interview-prep track (45+ questions, cram plan) — this pack explicitly builds on it rather than repeating it. |
| `fabledoc2/` (10 reverse-engineered ADRs) | **KEEP** | Only source of senior-trade-off ADR writeups; this pack adds one sequel card (`03-outbox-sweeper-tradeoff.md`) rather than restating any of the 10. |

No MERGE candidates found — all three trees are self-consistent, cite the same baseline commit, and don't
conflict with each other in the areas I cross-checked. No IGNORE candidates — none of the three is generic or
duplicate; all three are already codebase-specific with verified evidence.

## Honest caveats

- This pack assumes the reader has already engaged with at least one of `fabledocs`/`astra` for the full
  checkout trace — `01-checkout-outbox-correctness.md` deliberately doesn't repeat their file:line tables and
  will read thin without them open alongside it.
- The change-request answer's Q5 idempotency concern (stock decrement) is a design judgment, not something I
  verified by reading `OrderStatusChangedToPaidIntegrationEventHandler.cs` line-by-line this pass — I verified
  its existence and rough behavior via the `fabledocs` citation, not independently. Flagged as such in both the
  exercise commentary and the sealed answer, consistent with "evidence or it didn't happen."
- I did not run `check_course.py` (astra's own verifier) — it verifies astra content, not this pack, and running
  it wasn't necessary to produce or validate `training/`.
- No `dotnet build` was run — READ tier makes no source edits, so there was nothing to build.
