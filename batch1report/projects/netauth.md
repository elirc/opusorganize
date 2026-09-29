# netauth (NetAuth0) — B01 report

**Tier: DRILL** (Phase 3 + small Phase 5 interview kit per the B01 agent brief).

## What was created

All under `C:\Users\Owner\Desktop\netauth\training\`, committed to `main` at **`9e39ddd`**
("training: add B01 apprenticeship materials", pathspec commit, `training/` only):

- `training/README.md` — index, suggested order, time estimate (~4-5h)
- `training/review/EXERCISE.md` — 60-min blind security-focused code review, explicit
  warning not to read `docs2/08-security-review-walkthrough.md` first (see below)
- `training/_answers/review.md` — 14 ranked findings (Critical→Low), OWASP ASVS chapter tags,
  AI-generated-code-smell flags, "what NOT to over-flag" section
- `training/_answers/COMPARE.md` — self-scoring template (your findings vs. sealed, pattern
  behind misses, severity calibration)
- `training/incidents/001-clock-skew-401-spike.md` + `training/_answers/001-*.md` — on-call
  alert/logs/metrics, no cause hinted; sealed root cause + diagnostic path + fix + regression
  test + postmortem
- `training/incidents/002-redirect-uri-open-redirect.md` + `training/_answers/002-*.md` —
  external security report instead of a metrics alert (variety); same sealed structure
- `training/interview/PROJECT_STORIES.md` — 5 STAR skeletons tied to the review + both
  incidents
- `training/interview/TECHNICAL_QUESTIONS.md` — 20 questions (DRILL only requires 10; wrote
  20 so the user can pick by target role), spanning OAuth/OIDC flow, token validation,
  refresh-token concurrency, ASVS security, multi-tenancy, testing/operability

**Incident branches** (based on `main` @ `1d70eac`, via scratch worktrees, worktrees removed
after commit):

- `training/incidents/001-clock-skew-401-spike` @ `563e916` — symptom: "auth failures
  spiking after yesterday's deploy," ~6% 401 rate step-change, `IDX10223` lifetime-validation
  failures clustered within ~1-2s of each token's `exp`. (Cause, not stated in the incident
  file: `Program.cs` JWT bearer options gained `ClockSkew = TimeSpan.Zero`, removing the
  default 5-minute drift tolerance.)
- `training/incidents/002-redirect-uri-open-redirect` @ `73a0e08` — symptom: external
  security report of authorization codes being delivered to an attacker-controlled domain
  via `/connect/authorize`. (Cause, not stated in the incident file: `OAuthService.cs`'s
  `ValidateRedirectUri` changed from `string.Equals` to `string.StartsWith`, a classic
  prefix-match open-redirect regression.)

Both diffs are single-file, ~3-line, framed as plausible PRs (a security-hardening ticket and
a mobile-deep-link-compat ticket). Neither incident overlaps the 14 findings already
documented for `main` (`docs2/08` / `training/_answers/review.md`) — both are regressions
introduced into code that was previously correct, which is the point of an incident exercise
vs. a static review.

## Verification

- **Build: UNVERIFIED for both incidents.** This machine has only the .NET 10 SDK installed
  (`dotnet --version` → `10.0.302`); `global.json` pins `8.0.0` with `rollForward:
  latestFeature`, which still requires a major-version-8 SDK to be present, and none is. SDK
  resolution fails before reaching the compiler. Both diffs are small (one config-property
  addition, one method-call swap with an identical signature) and very unlikely to be
  compile errors, but this was not confirmed by an actual build — flagged in both sealed
  answer files and in `training/README.md`.
- All findings in `training/_answers/review.md` are cited to real file:line evidence in this
  repo. Two were independently spot-checked against source during this pass (not just
  copied from `docs2/08`): `OAuthController.cs:22` (unauthenticated `user_id` query param on
  `/connect/authorize`) and `frontend/src/api/client.ts:50-64` (access token in
  `localStorage`) — both confirmed as described.
- Git hygiene verified: `git status` on `main` showed a clean tree before this work; only
  `training/` was staged/committed (`git status --short` after `git add -- training` showed
  no other paths); incident worktrees were created off `HEAD`, edited, committed, and removed
  (`git worktree remove`), never switching the main working tree's branch.

## Issues found in the project (location only, no secret values)

- No secrets found in tracked files during this pass (signing keys are generated at runtime
  into Postgres, not committed; `docker-compose.yml`/`infra/postgres` use placeholder-looking
  local dev credentials — not inspected for real leaked values, out of scope for a DRILL
  pass).
- Things presented as working that aren't (already documented in `docs2/08` and reformatted
  into `training/_answers/review.md` findings #1, #5, #6, #14):
  - `/connect/authorize` trusts a raw `user_id` query parameter with no session/consent
    check — looks like an OAuth authorize endpoint but isn't actually authenticating anyone
    (`OAuthController.cs:22`).
  - Recovery codes are generated, hashed, stored, and returned to the client as if
    functional — `RecoveryCode.Use` has zero callers anywhere (`IdentityService.cs:104-111`).
  - `docs`/`docs2` describe a testing strategy and migration story that the repo doesn't
    fully back: one real unit test exists (`SecurityTests.cs`, PKCE hashing only), and no
    migrations are committed despite a `DesignTimeDbContextFactory` existing for them.

## Skill links (for `COMPETENCY_GRAPH.md` — not written there per brief; reporting only)

- authn/OAuth2/OIDC flow → `training/review/EXERCISE.md` (scope §1-3) +
  `training/interview/TECHNICAL_QUESTIONS.md` Q1-3
- token validation / clock-skew → `training/incidents/001-clock-skew-401-spike.md` +
  `_answers/001-*.md` + `TECHNICAL_QUESTIONS.md` Q4-5
- refresh-token rotation / concurrency → `_answers/review.md` finding #4 +
  `TECHNICAL_QUESTIONS.md` Q7-9
- redirect_uri / authorization-code interception (OWASP ASVS V13.2) →
  `training/incidents/002-redirect-uri-open-redirect.md` + `_answers/002-*.md`
- security-owasp / ASVS-flavored review method → `training/review/EXERCISE.md` +
  `_answers/review.md` (ASVS tags) + `_answers/COMPARE.md`
- authz / multi-tenancy (tenant-trust-from-request) → `_answers/review.md` finding #2 +
  `TECHNICAL_QUESTIONS.md` Q14
- code review skill (pattern-behind-the-miss habit) → `_answers/COMPARE.md` +
  `PROJECT_STORIES.md` story 4
- incident diagnosis / postmortem writing → both incident sealed answers +
  `PROJECT_STORIES.md` stories 1-3

## Curriculum needs (central page candidates — not written, per brief)

- **"JWT clock skew in distributed systems"** — why `ClockSkew` tolerance exists, how to size
  it, failure modes at both extremes. Referenced by incident 001; likely to recur in any
  other net-fleet app doing its own JWT validation (netdrop, netlinear, netshop,
  netintercom per the portfolio audit's cross-reference note).
- **"OAuth redirect_uri exact-match, and why 'almost equal' string comparisons are never
  safe for security-critical string matching"** — referenced by incident 002; generalizes
  beyond OAuth (webhook URL allowlists, CORS origin checks, etc. have the same shape of bug).
- **"Refresh-token rotation & reuse detection (the family model)"** — this repo's
  `FamilyId`/`RotatedFromId`/`ReplacedById` pattern is a clean concrete teaching example;
  referenced by review finding #4 and `TECHNICAL_QUESTIONS.md` Q6-8.

## Existing learning-doc trees — KEEP / MERGE / CONVERT / IGNORE

- `docs/upskill/` (v1, 47 files) — **IGNORE for active use.** Per `docs2/README.md`'s own
  admission, 34 of 47 files are empty TODO stubs and its security analysis missed real
  defects that v2 found. Superseded by `docs2/`. Not deleted (brief says don't delete
  anything); `training/README.md` points readers to `docs2/` instead.
- `docs2/` (v2, 12 files + README) — **KEEP.** Genuinely complete, code-grounded, no
  placeholders, already contains a full staff-level security findings table
  (`08-security-review-walkthrough.md`, F1-F14) with real evidence citations. This is
  unusually good pre-existing material — better than most fresh curriculum this pipeline
  would generate from scratch. `training/README.md` links to it explicitly rather than
  duplicating.
- **Important overlap note:** `docs2/08-security-review-walkthrough.md` already fully spoils
  the blind-review exercise (it contains the answer key in the open, not sealed). I handled
  this by (a) explicitly warning the reader in `training/review/EXERCISE.md` not to open it
  before doing their own pass, and (b) building `training/_answers/review.md` *on top of*
  those findings (re-ranked, ASVS-tagged, AI-smell-flagged, cross-checked) rather than
  duplicating the discovery work — this matches the "manufacture practice, don't redo
  research" spirit of the batch brief, but the user should know the exercise's spoiler risk
  is structural (the spoiler lives in the project's own docs tree, not something I can seal).
  If this project is ever handed to someone cold, the review exercise only works if they
  avoid `docs2/08` first.
- `docs2/06-code-reading-gym.md` and `docs2/10-contribution-ladder.md` — not inspected in
  depth this pass; `docs2/README.md` describes them as containing "ten find-the-real-bug
  exercises with answers" and PR-shaped tickets respectively. Likely **CONVERT-worthy** if
  this project is ever promoted to LAB tier (Phase 2 ladder / Phase 3 additional incidents
  could reuse rather than reinvent them) — flagging for whoever does that, not converting now
  since DRILL tier doesn't call for Phase 2.

## Honest caveats

- Both incidents are **build-unverified** due to this machine's SDK mismatch (only .NET 10
  installed, repo pinned to 8.0.0). The diffs are minimal and low-risk to compile
  (property addition; identical-signature method swap) but this is a real gap, not a
  formality — flagged in three places (both sealed answers, `training/README.md`).
- I did not run the app, spin up Postgres, or exercise either incident's exploit path live
  (e.g. actually hitting `/connect/authorize` with a crafted `redirect_uri` against a running
  instance). Both incident answer keys reason from the code and OAuth/JWT library semantics,
  not from an observed reproduction. This matches the brief's "don't start long-running
  servers" constraint but means "the mechanism is right" is a code-reading claim, not an
  empirically-verified one.
- `training/_answers/review.md`'s findings are substantially derived from `docs2/08`'s
  existing F1-F14 table (with citations re-verified where spot-checked, re-ranked, and
  ASVS-tagged) rather than 100% independently re-derived from a from-scratch reading of every
  file — this was a deliberate call under the batch's "don't redo research, build on it"
  rule (rule 5/7), given how strong the existing material already is, but it means the sealed
  answer inherits any error in the original `docs2/08` citations I didn't personally
  re-verify (12 of 14 findings).
- I did not audit `docker-compose.yml`/`infra/postgres` for hardcoded credentials beyond a
  glance; if this project is ever pushed somewhere public, that's worth a dedicated pass.
