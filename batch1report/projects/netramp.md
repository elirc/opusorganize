# netramp — ExpenseManagement — B01 batch report

**Tier:** DRILL (Phase 3 review + incidents, plus a small Phase 5 interview kit
per B01_AGENT_BRIEF.md's tier table: "DRILL = Phase 3 (+ a small Phase 5
interview kit: PROJECT_STORIES + 10 TECHNICAL_QUESTIONS)").

Path: `C:\Users\Owner\Desktop\.netramp` — flat ASP.NET Core 8 (single project,
no Application/Domain/Infrastructure split, "deliberately small dependency
footprint" per its own README) + React frontend. Zero NuGet packages on the
backend. Zero test files anywhere in the repo (confirmed again this batch via
`find . -iname "*test*"`, matching the prior audit's finding).

## What was created

All under `<repo>\training\`, committed to `main` at `d89be45` (pathspec commit,
`training/` only — nothing else in the working tree was touched or staged):

- `training/README.md` — index, suggested order (~2.5–3.5 hrs), layout map,
  incident branch commits, honest unverified-scope note.
- `training/review/EXERCISE.md` — 60-minute blind code review exercise over
  the whole backend, with specific angles to chase (thread-safety comment vs.
  actual mutation paths, the login timing-safety comment, file-leak tracing,
  zero-tests-vs-testing-docs).
- `training/review/CHARACTERIZATION_TEST_EXERCISE.md` — the requested
  characterization-test exercise for the approval state machine
  (`ExpenseStateMachine`): write an exhaustive test over the `(from, to, role)`
  space, prove it catches incident 001's regression.
- `training/incidents/001-fast-track-reimbursement.md` — symptom-only brief
  (Audit + Support tickets), no cause stated.
- `training/incidents/002-receipt-extension-trust.md` — symptom-only brief
  (security review finding), no cause stated.
- `training/interview/PROJECT_STORIES.md` — 5 STAR prompts tied to the specific
  exercises above (debugging, trade-off, incident, code-review, testing-practice).
- `training/interview/TECHNICAL_QUESTIONS.md` — 10 questions, each citing real
  files/lines in this repo (API design ×2, data modeling ×2, React/testing ×1,
  testing ×1, security ×2, operability ×1, background jobs/idempotency ×1).
- `training/_answers/review.md` — 18 ranked findings (severity: correctness,
  concurrency, security, operability, tests, maintainability), each with
  file:line evidence and a production-impact sentence; closes with an explicit
  "old-AI-generated smells present" summary.
- `training/_answers/COMPARE.md` — your-findings-vs-sealed template with a
  calibration section.
- `training/_answers/characterization-test.md` — the full legal-transition
  table extracted from source, a complete reference xUnit test, and a verified
  run log (see Verification below).
- `training/_answers/001-fast-track-reimbursement.md` and
  `.../002-receipt-extension-trust.md` — root cause, exact diff location,
  exploitability analysis (incident 002 specifically distinguishes "confirmed
  exploitable today" from "broken invariant / latent risk"), fix, regression
  test, and a "model postmortem" section per Phase 3's spec.

### Incident branches

- `training/incidents/001-fast-track-reimbursement` @ `6db91f4` — one-entry
  addition to `ExpenseStateMachine.Transitions` (`[Submitted][Reimbursing] =
  Finance`) framed as a "fast-track for pre-approved recurring vendors" PR that
  in fact has no vendor/recurrence predicate anywhere, so it lets Finance
  reimburse *any* Submitted expense without a manager ever approving it.
  Symptom given: Internal Audit finds `Reimbursed` expenses with no `Approved`
  event in history; a manager's dashboard still shows expenses as "awaiting
  approval" that were already paid.
- `training/incidents/002-receipt-extension-trust` @ `f9adecc` — a "fix false
  rejects on mobile uploads" PR in `ReceiptStorage.SaveAsync` that (correctly)
  removes an overly strict extension-vs-content-type equality check, but also
  (the actual bug) switches the on-disk filename's extension source from the
  validated content-type allowlist to the client-supplied, unvalidated
  filename extension — directly contradicting the class's own doc comment
  ("allowlist of content types + extensions ... never trust the client
  blindly"). Symptom given: a quarterly security review finds stored receipt
  files whose on-disk extension doesn't match their declared `Content-Type`.

Both branches are based on `main` @ `c5ef2a7` (HEAD before the `training/`
commit) and were never merged; the main working tree's branch was never
switched.

## Verification

- **`dotnet --version`** on this machine: `10.0.302`. No `global.json` in this
  repo, so SDK resolution is unconstrained — the orchestrator's global.json
  workaround wasn't needed.
- **Both incident branches build clean**: `dotnet build` inside each worktree
  (`backend/ExpenseManagement.Api.csproj`, target `net8.0`) → `Build succeeded.
  0 Warning(s). 0 Error(s).` for both. Worktrees were removed after committing;
  branches themselves remain.
- **The reference characterization test in `_answers/characterization-test.md`
  was actually compiled and run** — not just written. I scaffolded a
  throwaway `dotnet new xunit` project in the scratchpad referencing only
  copies of `Domain/ExpenseStateMachine.cs` + `Domain/Enums.cs` (no DI/DataStore
  needed, matching the exercise's own "cheapest possible test" framing):
  - Against unmodified `main`: `Passed! - Failed: 0, Passed: 14, Skipped: 0,
    Total: 14`.
  - After applying incident 001's exact one-line diff to the copy: `Failed! -
    Failed: 3, Passed: 11, Skipped: 0, Total: 14`, with the failing assertions
    naming the exact triple (`CanTransition(Submitted, Reimbursing, Finance)
    expected False but was True`) — confirmed the test would have caught the
    planted bug, not just theoretically.
  - The scratchpad throwaway project was deleted after verification; nothing
    from it was committed anywhere.
- **UNVERIFIED, stated in `training/README.md`:** the reference test was not
  run against a real `backend/ExpenseManagement.Api.Tests` project referencing
  the actual `.csproj` (that scaffold doesn't exist yet in this repo — creating
  it is the exercise-doer's job, not this batch's). The rest of the app
  (frontend, `Reports` endpoints, the background worker's real timing) was read
  for the review but never run end-to-end — no dev server was started.

## Issues found in the project (beyond what was planted)

These are pre-existing, not planted — full detail + file:line evidence in
`training/_answers/review.md`:

- **Zero test files anywhere**, despite a curriculum tree (`docs/upskill/05-
  quality-engineering/`) that documents a testing strategy — the same
  "docs describe testing that code doesn't have" smell the prior audit flagged.
- **Real concurrency race** (not the planted incident): `ExpenseService
  .Transition` mutates a shared `Expense` object with no lock while
  `BackgroundJobs.ProcessReimbursement` mutates the same instance from a
  different thread; `DataStore`'s doc comment claims `ConcurrentDictionary`
  thread-safety covers this, which is only true for the dictionary's own
  add/remove, not for mutating the objects it holds.
- **Real security smell** (not the planted incident): `AuthService.Login`'s
  comment claims constant-time password verification, but the `user is null ||
  !Verify(...)` short-circuit skips the (slow) PBKDF2 call entirely for
  nonexistent emails — a genuine timing side-channel for account enumeration,
  contradicting the adjacent comment.
- **Uploaded/replaced receipt files are never deleted from disk** — both
  `ReceiptService.UploadAsync` (replacing a receipt) and `ExpenseService
  .Delete` (deleting an expense) only remove the in-memory dictionary entry;
  `ReceiptStorage` has no delete method and nothing calls one. Unbounded
  storage leak in any persistent deployment.
- **Expired sessions are pruned only lazily**, on next use of that exact token
  — a session nobody presents again lives in `DataStore.Sessions` forever
  (slow, unbounded memory leak, same root pattern as the file leak above).
- Minor: no rejection-reason clearing on resubmit (stale `RejectionReason` can
  survive a full re-approval cycle), no correlation ID on error responses, no
  `UseHttpsRedirection`, truncated-GUID payment references with no uniqueness
  check.
- **No secrets found** in this project (no hardcoded connection strings, API
  keys, or credentials beyond the intentionally-documented demo password
  `Password123!` in `DataSeeder.cs`, which is explicitly a seeded-demo-data
  password, not a real secret).

## Skill links (for the competency graph — not written there, per the brief)

- `authz-rbac` / `state-machine-design` → `training/incidents/
  001-fast-track-reimbursement.md` + `_answers/001-fast-track-reimbursement.md`
  + `training/review/CHARACTERIZATION_TEST_EXERCISE.md` +
  `interview/TECHNICAL_QUESTIONS.md` Q1
- `security-owasp` (file upload / content-type trust) → `training/incidents/
  002-receipt-extension-trust.md` + its answer + `TECHNICAL_QUESTIONS.md` Q8
- `security-owasp` (timing side-channel / auth) → `training/_answers/
  review.md` finding #6 + `TECHNICAL_QUESTIONS.md` Q7
- `concurrency` (shared-mutable-entity race) → `_answers/review.md` finding #4
  + `TECHNICAL_QUESTIONS.md` Q10 (background-job idempotency angle)
- `test-unit` / `characterization-testing` (zero-test codebase) →
  `training/review/CHARACTERIZATION_TEST_EXERCISE.md` +
  `_answers/characterization-test.md` (verified reference + verified
  incident-catch) + `TECHNICAL_QUESTIONS.md` Q5, Q6
- `operability` (resource leaks with no error signal) → `_answers/review.md`
  findings #8, #9 + `TECHNICAL_QUESTIONS.md` Q9
- `code-review` → `training/review/EXERCISE.md` + `_answers/review.md` +
  `_answers/COMPARE.md`
- `db-modeling` (in-memory dict → real DB port) → `TECHNICAL_QUESTIONS.md`
  Q3, Q4

## Curriculum needs (concepts referenced that deserve ONE central page)

Not written to `apprenticeship\curriculum\` per the brief — reporting only:

- **"Characterization tests vs. correctness tests"** (2-line scope: when and
  why to pin down *current* behavior of untested legacy-ish code before
  changing it, vs. writing tests from a spec of what *should* happen; this
  batch's exercise is a concrete worked example worth linking from a central
  page rather than re-explaining per project).
- **"Comments that assert a security/thread-safety property the code doesn't
  actually have"** (2-line scope: a named smell-pattern — how to spot it by
  re-reading the code under a doc comment's claim line-by-line instead of
  trusting the claim — this project has two independent instances: the login
  timing comment and the DataStore thread-safety comment).
- **"Table-driven state machines: the single-entry-away-from-a-bypass risk"**
  (2-line scope: why a dictionary/table-driven authorization state machine
  needs an exhaustive test over its full input space, illustrated by incident
  001 — likely recurs across other fleet apps with similar patterns, e.g.
  netdocu's envelope/document lifecycle).

## Existing learning-doc trees in this repo — KEEP/MERGE/CONVERT/IGNORE

- `docs/upskill/` (46 files, 8-section structure: `00-fast-track.md` +
  `01-codebase-cartography` through `08-reference`) — **KEEP**. Per the prior
  audit this reads as genuinely project-specific (real file/line citations),
  same pipeline as the other 9 "Net-fleet" apps' curricula. I did not do a
  full line-by-line re-verification of all 46 files in this batch (out of
  DRILL-tier scope), but spot-checked `05-quality-engineering/
  01-testing-strategy.md` and `02-writing-tests-here.md` exist and are
  file-titled consistently with the prior audit's description. Link it from
  the competency graph rather than duplicating any of it into `training/`.
  No MERGE/CONVERT action needed — it's reading material that complements,
  not duplicates, the hands-on exercises created this batch.

## Honest caveats

- This is a DRILL-tier pass: no `ladder/`, `navigation/`, or `agentic/`
  directories were created, per the brief's tier table. If this project is
  later promoted to LAB tier, those phases still need doing.
- The characterization-test reference was verified against a standalone throwaway
  project, not the real (nonexistent) `backend/ExpenseManagement.Api.Tests` —
  stated explicitly in `training/README.md`'s "What's genuinely unverified"
  section so this doesn't get silently presented as more verified than it is.
- `docs/upskill/`'s full 46 files were not re-audited file-by-file this batch;
  the KEEP verdict rests on the prior audit's sampling plus a 2-file spot check,
  not an independent full read.
- I did not run the frontend or start the backend server at all — all
  verification was `dotnet build`/`dotnet test` only, consistent with the
  brief's "don't start long-running servers" rule.
