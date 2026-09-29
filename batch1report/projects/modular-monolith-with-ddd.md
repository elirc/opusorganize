# modular-monolith-with-ddd — B01 report

**Path:** `C:\Users\Owner\Desktop\.netarchitectureproject\modular-monolith-with-ddd`
**Tier:** READ (Phase 4 only, per apprenticeship brief). No source edits, no incidents.
**Origin:** kgrzybek/modular-monolith-with-ddd, verified real OSS clone (`git remote -v`, 330
upstream commits, last upstream commit 2024-04-20 — least recently updated project in the batch).

## What was created

All under `training/` in the repo, committed by pathspec, commit `a7d111a`
("training: add B01 apprenticeship materials"):

- `training/README.md` — index, reading order (~2–2.5h), scope note.
- `training/navigation/01-module-boundaries.md` — how the 5 modules (Administration, Meetings,
  Payments, Registrations, UserAccess) are separated and how `NetArchTest`-based `ArchTests`
  enforce it at two levels (solution-level API namespace checks in `src/Tests/ArchTests/`, and
  per-module assembly checks in each module's own `Tests/ArchTests/`), with the three explicit
  carve-outs (`INotificationHandler<>`, `*IntegrationEventHandler`, `EventsBusStartup`) that are
  the *only* legal cross-module reference points.
- `training/navigation/02-command-flow-create-meeting.md` — `POST api/meetings/meetings` traced
  file-by-file: controller → `IMeetingsModule` facade → `CommandsExecutor` (Autofac scope) →
  Validation/Logging/UnitOfWork decorator stack → `CreateMeetingCommandHandler` → `MeetingGroup`
  aggregate factory → `MeetingRepository` (stage-only, commit happens in the decorator).
- `training/navigation/03-integration-event-flow-meeting-attendee-added.md` — the cross-module
  flow `MeetingAttendeeAddedDomainEvent` (Meetings) → outbox → `InMemoryEventBusClient` →
  Payments inbox → `MeetingAttendeeAddedIntegrationEventHandler` → `CreateMeetingFeeCommand` via
  Payments' internal-command queue, 10-file trace with a "why three hops" explanation.
- `training/navigation/04-outbox-inbox-processing.md` — outbox/inbox table shape and the two
  polling jobs, plus a **found, evidence-backed reliability gap**: because
  `MeetingAttendeeAddedPublishEventNotificationHandler` mints a fresh `Guid.NewGuid()` on every
  republish, an outbox-processing crash between "publish" and "mark processed" can produce two
  *different-Id* inbox rows describing the same event — the `Id` primary key does not catch it, so
  Payments can create two `MeetingFee`s for one attendee in that crash window. Documented with file
  citations, not fixed (READ tier — no source edits).
- `training/navigation/05-why-modular-monolith-vs-microservices.md` — two "Why?" write-ups in the
  brief's required format (Problem → naive → where it fails → A/B/C → trade-offs → choice → failure
  modes → tested → monitored → when to revisit): (1) modular monolith vs. full microservices vs.
  flat monolith, (2) outbox+inbox+internal-command-queue vs. sync call vs. fire-and-forget pub/sub.
- `training/navigation/06-first-change-onboarding.md` — 1-page, 8-point checklist grounded in real
  files (module ArchTests, decorator pipeline, transaction boundary location, rule classes,
  DB-schema-as-source-of-truth, and an explicit call-out not to touch the 6 dirty files).
- `training/navigation/07-change-request.md` + `training/_answers/07-change-request-answer.md` —
  a real, evidence-grounded feature request: Payments already raises
  `MeetingFeeExpiredDomainEvent` internally but never tells Meetings (confirmed:
  `MeetingFeeExpiredIntegrationEvent` does not exist under
  `src/Modules/Payments/IntegrationEvents/`, only the `Paid` sibling does). Exercise asks for a
  written placement plan (which project gets the new type, which existing command to reuse —
  `RemoveMeetingAttendeeCommand` already exists — which translation-handler template to copy). The
  sealed answer also flags that Payments' `Paid`-event translation goes through `IAggregateStore`
  + snapshot rather than reading the domain event directly (unlike the Meetings-side pattern traced
  in doc 03) — a genuine, citable architectural inconsistency between two modules' outbound-event
  handling.

No `ladder/`, `review/`, `incidents/`, `agentic/`, or `interview/` — out of scope for READ tier.

## Incident branches

None — READ tier, OSS clone rule ("no incident branches, no source edits").

## Verification

- Confirmed via `git status --short` before and after the pass that the pre-existing 6 dirty files
  (`ChangeMeetingMainAttributesCommandHandler.cs`, `CreateMeetingCommandHandler.cs`,
  `MeetingTerm.cs` modified; `MeetingTermMustEndAfterStartRule.cs`,
  `MeetingTermCommandHandlerTests.cs`, `MeetingTermTests.cs` untracked) are byte-identical
  before/after — not staged, not touched.
- Every file/method/line cited in the navigation pack was read directly from the working tree in
  this session (not inferred) — command flow, integration-event flow, outbox/inbox jobs, arch
  tests, and the change-request's cited files (`RemoveMeetingAttendeeCommand`,
  `MeetingFeePaidNotificationHandler`, `IntegrationEvents` project contents) were all opened and
  quoted from source, not guessed.
- **UNVERIFIED:** did not run `dotnet build` or any test suite (not required at READ tier per the
  brief — no source edits were made, so nothing needed compiling). Did not verify the outbox
  duplicate-delivery gap by actually running the code/reproducing a crash window — it's a static
  trace of the code path (fresh `Guid.NewGuid()` per republish + no unique constraint beyond `Id`),
  not an observed runtime failure. Flag this as reasoning-from-code-reading, not a confirmed bug
  report, if it's ever escalated.
- Did not open every one of the 5 modules' individual `Tests/ArchTests` projects — verified
  Meetings' in full (`ApplicationTests.cs`) and confirmed by directory listing that Administration,
  Payments, Registrations, UserAccess each have their own `Tests/ArchTests/*.csproj`; assumed
  (not verified line-by-line) that each mirrors the same 8-test shape based on the consistent
  project-file naming pattern across modules — UNKNOWN if any module's internal-layering tests
  diverge from Meetings'.

## Issues found in the project

- **Reliability gap in outbox→bus→inbox delivery** (see `04-outbox-inbox-processing.md` above):
  potential duplicate cross-module side effects (e.g. duplicate `MeetingFee`) on an outbox-job
  crash between publish and mark-processed, because the integration event's `Id` is freshly
  generated on every republish rather than carried through from the outbox row. Documented, not
  fixed (READ tier).
- **No secrets found** in this pass (didn't specifically grep for them beyond normal file reading;
  this is a stock OSS clone with no `.env`/config edits made).
- **Nothing presented as working that isn't** — this is a mature, 330-commit reference repo; no
  README claims contradicted by code in what was read.
- Upstream is 1.5+ years stale (last commit 2024-04-20) relative to current .NET tooling — noted
  already in the prior audit (`portfolio-audit/projects/batch-01.md`), repeated here for visibility
  since it affects anyone treating this as a "current best practice" reference.

## Skill links (for the competency graph)

- `arch-modular-monolith` → `training/navigation/01-module-boundaries.md`,
  `training/navigation/05-why-modular-monolith-vs-microservices.md`
- `arch-event-driven` / `async jobs / outbox-inbox / idempotency` →
  `training/navigation/03-integration-event-flow-meeting-attendee-added.md`,
  `training/navigation/04-outbox-inbox-processing.md`
- `design-docs-adrs` / `unfamiliar-codebase navigation` →
  `training/navigation/06-first-change-onboarding.md`, `training/README.md`
- `code review` (spotting an inconsistency between two modules' patterns; spotting a
  duplicate-delivery risk from reading code, not from a failing test) →
  `training/_answers/07-change-request-answer.md` (section 4), `training/navigation/04-*.md`
- `API design` / CQRS command pipeline (decorators, transaction boundary placement) →
  `training/navigation/02-command-flow-create-meeting.md`

## Curriculum needs (concepts referenced that deserve one central `apprenticeship/curriculum/` page — not written here)

1. **"Outbox pattern: at-least-once delivery and where duplicate-handling responsibility actually
   lands"** — this project's outbox/inbox is the clearest real example found so far of the pattern
   *and* of a subtle way to defeat its own idempotency guarantee (new-Guid-per-republish). Several
   other batch projects (netairag, the Net-fleet apps) likely touch outbox/inbox more shallowly;
   this could be the canonical page, cross-linked from here.
2. **"Architecture tests (NetArchTest) as a build gate for module boundaries"** — the two-level
   (API-namespace + module-assembly) pattern with named carve-outs is a reusable teaching example
   distinct from "just don't do it" code-review guidance.
3. **"Modular monolith vs. microservices vs. flat monolith — the actual decision framework"** — the
   Problem/naive/options/trade-offs/choice/failure-modes format used in doc 05 is itself a
   reusable interview-answer template worth centralizing, not just this project's content.

## Existing learning-doc trees — KEEP / MERGE / CONVERT / IGNORE

- **`..\astraupskill\` (i.e. `Desktop\.netarchitectureproject\astraupskill\`, one level above this
  clone — 7 files + `evidence/`/`snapshots/` + `VERIFICATION.md`):** a single bounded "worked
  change" course on the exact `MeetingTerm` start/end-date mapping defect that the 6 dirty
  working-tree files also address (same bug, independently — the pack's `README.md` and
  `01-CODEBASE-MAP.md` describe fixing `CreateMeetingCommandHandler`/
  `ChangeMeetingMainAttributesCommandHandler` to pass `TermEndDate` instead of `TermStartDate`
  twice, plus a new `MeetingTermMustEndAfterStartRule`). **Verdict: KEEP as-is, no action.** It
  does not overlap in scope with the navigation pack built here (one bug walkthrough vs.
  whole-system architecture/boundaries/events), it's already correctly kept outside the actual
  clone directory (doesn't pollute upstream source), and it's already high quality (specific line
  citations, real test names, an explicit non-goals section calling out what it does NOT establish
  — DB transaction rollback, HTTP formatting, deployed scheduling). One thing worth flagging to the
  user: the pack's exercise and the repo's actual dirty files describe/implement the *same fix*, so
  if the user is going to commit those 6 dirty files at some point, `astraupskill`'s worked-change
  narrative would then match the repo's real history — a nice coincidence, not an action item.

## Honest caveats

- This pack focuses on Meetings↔Payments as the one cross-module event flow per the brief's
  instruction ("one cross-module integration-event flow traced file by file"). Other real flows
  exist (Administration→Meetings `MeetingGroupProposalAccepted`, UserAccess→{Meetings,Payments,
  Administration} `NewUserRegistered`) and were located but not traced in equal depth — noted in
  `01-module-boundaries.md`'s evidence list only in passing. If a second flow is ever wanted, the
  `NewUserRegistered` fan-out (one publisher, three subscribers) would be the most interesting one
  (only cross-module event with more than one consumer, confirmed via
  `grep -rl NewUserRegisteredIntegrationEventHandler`).
- The duplicate-delivery finding in doc 04 is a code-reading deduction, not a reproduced bug — flag
  this if it's escalated anywhere as more than "worth investigating."
- Did not read every file in every one of the 5 modules; the navigation pack is deliberately scoped
  to the two traced flows plus the architecture-test/outbox-inbox mechanics common to all modules,
  per the brief's Phase 4 scope (not a full codebase inventory).
