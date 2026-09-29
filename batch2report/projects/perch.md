# Perch — B02 apprenticeship report

**Repo**: `C:\Users\Owner\Desktop\perch` (ATS course monorepo, Node/Fastify API + React/Vite web,
Prisma schema present but unused by the running server — see finding below)
**Tier**: DRILL (per assignment: 2 new incidents biased to frontend — this is a thin skill here
since the ledgered flaws are backend correctness/security)
**Main HEAD after this batch**: `f56f063` (training-only commit on top of `1cfb059`, the repo's
pre-existing HEAD; nothing else on `main` touched)

## What was created

All under `<repo>\training\`:

- `training/README.md` — index, suggested order (~2–2.5h), spoiler warning list.
- `training/review/EXERCISE.md` — 60-minute blind code review, frontend-weighted pointers
  (search debounce, funnel report free-text job ID, bulk-stage loop) alongside backend ones
  (sign-in has no credential check, server.ts vs. Prisma repos, idempotency-map lifecycle).
- `training/_answers/review.md` — 14 ranked findings (2 blocker / 4 high / 5 medium / 3 low+test),
  each with file:line evidence and an "old-AI smell" tag where applicable.
- `training/_answers/COMPARE.md` — self-review comparison template.
- `training/incidents/001-search-debounce-timer-leak.md` + `_answers/001-...md` — **frontend
  rendering/perf incident**: a plausible "add debounce to candidate search" PR where the debounce
  utility never calls `clearTimeout`, so calls are delayed but not coalesced (request-volume
  spike + flickering intermediate search results).
- `training/incidents/002-careers-email-validation-drift.md` + `_answers/002-...md` — **frontend
  form/validation-drift incident**: a new client-side email regex on the public careers apply
  form that's stricter than the API's actual rule (`createCandidate` in `packages/shared`),
  silently blocking real candidates with plus-addressed emails (`name+tag@gmail.com`) — request
  never leaves the browser, so no server-side signal exists.
- `training/interview/PROJECT_STORIES.md` — 4 filled STAR slots tied to this batch's exercises +
  1 note that the agentic/LAB-only story slot doesn't apply to a DRILL-tier project.
- `training/interview/TECHNICAL_QUESTIONS.md` + `_answers/TECHNICAL_QUESTIONS.md` — 10 questions
  (API design ×2, DB/concurrency, DB/pagination, React/rendering, React/data-fetching, testing,
  security/authz, security/authn, operability), each citing real files/lines.

No `ladder/`, `navigation/`, or `agentic/` — out of scope for DRILL per `B02_AGENT_BRIEF.md`.

### Incident branches (worktree-based, base `main`@`1cfb059`)

| Branch | Symptom (no cause) | Commit |
|---|---|---|
| `training/incidents/001-search-debounce-timer-leak` | Candidate-search API request volume up ~4x after a "debounce search input" deploy; recruiters report search results flashing/changing after they've stopped typing | `7f80e7e` |
| `training/incidents/002-careers-email-validation-drift` | Careers-page candidates report the apply form always says "Enter a valid email address" and never actually submits; no server-side error logged because the request never fires | `46cc8b4` |

Both worktrees were removed after committing; branches remain on the repo, `main`'s working tree
was never switched.

## Verification

- `git status` on `main` is clean; `training/` is the only change on `main`, committed via
  pathspec commit as instructed.
- **BUILD: UNVERIFIED (no deps installed)** for both incidents — `apps/web` has no `node_modules`
  on this machine and only the gitjira-app agent is authorized to run `npm ci`/`pnpm install` this
  batch. Verified by careful reading instead:
  - Incident 001: traced `debounce()`'s `setTimeout`/`clearTimeout` semantics by hand against the
    new `debounce.test.ts` (which uses `vi.useFakeTimers()`, a pure function test requiring no
    DOM — consistent with every existing `.test.ts` in `apps/web/src`, none of which render JSX).
    Confirmed the RED assertion (`calls` would be `["a","ad","ada"]` against the buggy code,
    `["ada"]` once `clearTimeout` is added).
  - Incident 002: confirmed by direct text comparison that `EMAIL_PATTERN`'s local-part character
    class `[A-Za-z0-9._%-]` excludes `+`, and cross-checked against
    `packages/shared/src/recruiting.ts:6-7`'s actual server-side rule (`email.includes("@")` only)
    — the drift is unambiguous from source, no runtime needed to confirm it.
  - Both diffs are single-file-additions + one small wiring change each; kept intentionally small
    (~25–35 line diffs) per the brief's "plausible PR" sizing rule.
- Review findings (`_answers/review.md`) were derived from reading `apps/api/src/app.ts`,
  `sessions.ts`, `careers.ts`, `recruiting.ts`, `server.ts`, `index.ts`, `packages/db/src/auth.ts`,
  `packages/db/src/index.ts`, and `apps/web/src/{PipelineBoard,CandidateSearch,ReportingWorkspace,
  BulkWorkspace,CollaborationPanel,CareersPage}.tsx` plus their `.ts` logic modules — not
  guessed from file names.

## Issues found in the project (beyond the two planted incidents)

- `apps/api/src/sessions.ts` `SessionService.signIn` grants a session from email + organizationId
  alone — no password or other credential check. Deliberate demo simplification, but flagged as a
  **blocker-severity finding in the review exercise** since it's the kind of pattern that's
  dangerous if ever copied into a real product without a real credential check added.
- `apps/api/src/server.ts` wires only the in-memory `createDemoRepositories()`; the Prisma-backed
  repository classes in `packages/db/src/index.ts` are never constructed anywhere in `apps/api`,
  meaning `docs/runbooks/deploy-and-rollback.md` / `backup-and-restore.md` describe procedures
  for a persistence layer the running app doesn't actually use. Flagged as "docs claiming
  something the code doesn't do."
- `apps/api/src/careers.ts`'s idempotency `#attempts` map only evicts on failure — successful
  entries live for the process lifetime with no TTL (unbounded memory growth).
- `savedViews` (`apps/api/src/app.ts:42`) is a plain in-memory `Map` inside `buildApi`, unlike
  every other piece of state which goes through a `*Repository` interface — inconsistent with the
  app's own architecture, lost on restart, invisible to Prisma migration work.
- Bulk stage-move (`/applications/bulk-stage`) awaits each of up to 100 applications sequentially,
  no transaction, no rollback of already-succeeded moves on partial failure.
- No secrets/`.env` files found anywhere in the repo during this pass — nothing to report beyond
  that negative confirmation.
- Nothing found that was clearly presented-as-working-but-isn't beyond the server/Prisma gap above
  — the rest of the app's docs (ADRs, concept pages, the existing flaw ledger) matched the code on
  spot-checks.

## Skill links (for COMPETENCY_GRAPH)

- **web/TS/React (rendering/perf)** → `training/incidents/001-search-debounce-timer-leak.md` +
  `_answers/001-...md`; review finding #8 (`_answers/review.md`).
- **web/TS/React (forms/validation, client-server contract drift)** →
  `training/incidents/002-careers-email-validation-drift.md` + `_answers/002-...md`; interview
  `TECHNICAL_QUESTIONS.md` Q9 (auth) is adjacent but distinct.
- **accessibility (fe-a11y)** → already fully covered by the repo's own
  `docs/accessibility/sprint-14-audit.md`; this batch did **not** add a new a11y incident (see
  caveats) — no new link to add here beyond noting the existing doc as the current source.
- **authn/authz** → review findings #1 (no credential check) and #7 (funnel report capability
  mismatch); `TECHNICAL_QUESTIONS.md` Q8/Q9.
- **API design** → `TECHNICAL_QUESTIONS.md` Q1/Q2; review finding #6 (public endpoint rate
  limiting).
- **data modeling/SQL/pagination** → `TECHNICAL_QUESTIONS.md` Q4; review finding #9 (free-text
  job ID vs. real job list).
- **testing** → review finding #14 (no component-level frontend tests, no jsdom/testing-library);
  `TECHNICAL_QUESTIONS.md` Q7.
- **operability / docs-vs-code** → review findings #2, #12; `TECHNICAL_QUESTIONS.md` Q10.
- **code review** → `training/review/EXERCISE.md` + `_answers/review.md` + `_answers/COMPARE.md`.
- **unfamiliar-codebase navigation** → not built this batch (DRILL tier skips Phase 4); Perch's
  own ADRs/concept docs already serve this role — see disposition below.

## Curriculum needs (concepts referenced, not written — for `apprenticeship\curriculum\`)

- **"Client validation vs. server validation: who's the source of truth"** (2-line scope: when to
  duplicate a validation rule on the client for UX vs. when to just surface the server's error;
  how to test that a duplicated rule can't drift stricter than the real one). Directly motivated
  by incident 002; likely recurs across other B0x projects with public-facing forms.
- **"Debounce vs. throttle: what each actually guarantees"** (2-line scope: debounce coalesces a
  burst into one trailing call, throttle caps call rate; the specific bug class of "delays but
  never cancels" that looks like a debounce but isn't). Directly motivated by incident 001.

## Existing learning-doc trees — KEEP / MERGE / CONVERT / IGNORE

| Tree | Verdict | Note |
|---|---|---|
| `FLAW-LEDGER.local.md` (root) | **KEEP** | Answer key for 5 planted-and-harvested flaws with RED-test evidence; do not reuse as source material for new incidents (already followed for this batch). Link from COMPETENCY_GRAPH as-is. |
| `docs/sprints/flaw-ledger.md` | **KEEP** (mirror) | Same content surfaced in the sprint docs; keep both, they serve different readers (root = private answer key, sprints = narrative). |
| `docs/incidents/2026-07-simulated-stage-history-incident.md` + `EXERCISE.md` | **KEEP** | Well-built standalone incident exercise, format worth reusing elsewhere. Already flagged as a spoiler for this batch's review exercise (concurrency answer). |
| `docs/accessibility/sprint-14-audit.md` | **KEEP** | Genuine a11y audit, unique in this batch of projects. No new a11y incident was needed/added — see caveats. |
| `docs/adr/ADR-0000..0015` (16 ADRs) | **KEEP** | High-value, evidence-backed. Good raw material for a future navigation/senior-trade-offs pack if Perch is ever upgraded to LAB tier. |
| `docs/concepts/*.md` (14 files) | **KEEP** | Concept pages are project-specific and well-targeted (idor.md, cursor-stability.md, etc.) — not generic tutorials, so no MERGE into central curriculum needed; they already do what curriculum pages are for, scoped to this repo. |
| `docs/security/*.md`, `docs/runbooks/*.md`, `docs/performance/sprint-12-evidence.md`, `docs/demo/DEMO-SCRIPT.md`, `docs/COURSE-RETROSPECTIVE.md`, `docs/curriculum/SPEC.md` | **KEEP** | All project-specific and evidence-backed; the runbooks are actually where this batch's review found the "docs vs. running server" gap, which makes them *more* valuable as review material, not less. |

Nothing here needs MERGE into `apprenticeship\curriculum\` (no generic tutorial content found) or
CONVERT/IGNORE — Perch's existing docs are unusually good and none were duplicative of central
curriculum material.

## Honest caveats

- Per the tier assignment, this batch deliberately did **not** add a third, accessibility-specific
  incident, since the existing `docs/accessibility/sprint-14-audit.md` already covers a11y at
  Sprint 14's snapshot and the brief asked for exactly 2 new incidents biased toward frontend
  broadly (rendering/perf, a11y, validation drift) — 001 and 002 were judged the two most concrete
  and diagnosable given the codebase as it stands today. If a dedicated a11y-regression incident
  is wanted later, `PipelineBoard.tsx`'s "Move to {stage}" buttons or `CareersPage.tsx`'s form
  labeling would be the natural targets — neither was touched by this batch.
- No component-level (`.tsx`) tests exist anywhere in `apps/web`, and no `@testing-library/react`
  or jsdom/happy-dom config is present. Both incidents were deliberately designed around new
  *pure-function* modules (`debounce.ts`, `careers-validation.ts`) wired into the JSX rather than
  bugs inside the JSX rendering itself, specifically so their regression tests run under the
  existing `vitest` setup without installing anything. A true React-rendering-storm or a11y-markup
  bug would need `@testing-library/react` + jsdom added first — flagged in review finding #14 and
  `TECHNICAL_QUESTIONS.md` Q7, not silently worked around.
- `BUILD: UNVERIFIED (no deps installed)` on both incidents, per B02 rule (only gitjira-app agent
  may `npm ci`/`pnpm install` this batch). Confidence is high from direct reading (both bugs are
  small, mechanical, and don't depend on framework/runtime behavior beyond `setTimeout` semantics
  and regex evaluation, both standard JS), but this is not a substitute for actually running
  `pnpm --filter @perch/web test`.
- Did not verify `dotnet build`-equivalent (`pnpm turbo run typecheck`/`build`) for the same
  no-install-allowed reason; the two new `.ts`/`.tsx` files were written to match this codebase's
  existing TypeScript conventions (explicit types on exported functions, no `any`) but a real
  `tsc --noEmit` pass was not run.
