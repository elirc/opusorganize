# B07 — reviewboard (gravreviewboardjspy\reviewboard) — READ tier

Repo: `C:\Users\Owner\Desktop\_Organized Desktop\09 Grav And VG Projects\gravreviewboardjspy\reviewboard` (OSS clone of Review Board, Django + TS/Spina/Backbone).

## Git
- **The repo had no .git.** I ran `git init`, set a repo-local identity (`elirc <elichessmaster@gmail.com>`; there's no global git identity on this machine), and
  set `core.autocrlf false`. Baseline commit `bb3d688` "chore: baseline snapshot before training" (3,585 files, respects `.gitignore`; no node_modules/.venv existed).
- Training commit `415c038` "training: add B07 apprenticeship materials" (pathspec `-- training`). No remote, nothing pushed, no incident branches (READ tier).

## Created
- `training/README.md`: index, order, ~6 h estimate
- `training/navigation/SECURITY-STORY-BANK.md`: all 25 stories verified with file:line evidence, grouped by OWASP (A01, A02/A10, A03, A04, A09, plus non-security), difficulty J/M/S, module-level hints, and 8 ★ placement exercises. Evidence sits in collapsed `<details>` blocks so the learner classifies first.
- `training/_answers/SECURITY-STORY-BANK-placements.md`: sealed file-level placements for the top 8 (US-16, 06, 04, 12, 10, 22, 24, 01) with a 40-point rubric
- `training/navigation/SEAM-DJANGO-TS.md`: the Django-backend / TS-frontend seam (pipeline-built bundles, Python-gated npm workspace, 256 .ts vs 132 .es6.js, hand-mapped snake/camel contract, two test runners), one "Why?" trade-off, and one exercise
- `training/navigation/DOC-TREE-VERDICTS.md`

## Verification result: 14 REAL / 10 ALREADY-HANDLED / 1 UNCLEAR
- ALREADY-HANDLED: US-02 (sitewide-login setting + `is_accessible_by`), 05 (ChangeDescription history), 07 (`reviews_allow_self_shipit`, default True), 08, 09 (the ticket gets the verification rule backwards), 14 (2 MiB diff cap), 17 (mostly), 20 (no DELETE route), 21 (`issue-open-count-gt` exists), 23 (`log_timed`).
- REAL: 01, 03, 04, 06, 10 (IP only), 11, 12 (emails exist, no audit log), 13 (API only), 16, 18, 19, 22, 24 (partial), 25. UNCLEAR: 15 (incoherent premise).
- Only ~11 of the 25 are really security tickets. Cross-cutting defect in the story set: every schema story says `makemigrations`, but RB uses **Django Evolution**. The code samples also invent APIs (`super().publish()`, `get_approval_state`, `type` for `close_type`).
- Method: static reading plus grep only. Python deps and djblets are not installed, so anything inside djblets is marked UNVERIFIED (token `last_used` update path, `log_timed` thresholds, API auth rate limiting, `HealthCheckView`). One Python one-liner confirmed the webhook header bug.

## Issues found in the project (upstream code, not fixed, per READ tier)
1. **Real bug:** `reviewboard/notifications/webhooks.py:429-430`: `'Basic %s' % b64encode(...)` formats bytes, so the header is `Basic b'...'` (reproduced). Webhooks with URL credentials send a broken Authorization header. No test covers it.
2. **Credential leak to logs:** the same file at `:416-417, :440-442` logs `webhook_target.url` including `user:pass@`.
3. Webhook dispatch has no private-IP/SSRF guard and signs with HMAC-SHA1 (`webhooks.py:411-438`).
4. **Suspected authz gap (UNVERIFIED):** `webapi/resources/repository_info.py:36`, `repository_branches.py:80` and `repository_commits.py:106` fetch the repo through `get_object`, which filters only by local site (`repository.py:214`), and never call `has_access_permissions`. Compare `diff_context.py:109`. Tests only cover site-level denial. Confirming it needs a failing test in a real env.
5. `settings.py:601` joins NODE_PATH with `:`, which will likely break DEBUG-mode compiles on Windows (UNVERIFIED).
6. Things presented as working that aren't: the User Stories' implementation plans (see above); `docs/upskill` never mentions Django Evolution and has 94 stale `file:///c:/Users/Owner/Desktop/gravreviewboardjspy/` links.
- Secret-looking material, all upstream test fixtures or docs config (locations only): `docs/codebase/settings_local.py:5` (`SECRET_KEY`, docs build config), `reviewboard/scmtools/testdata/stunnel.pem`, and test private keys under `reviewboard/certs/tests/testdata/file_storage/**/*.key`. No `.env` files are tracked.

## Skill links (for COMPETENCY_GRAPH)
- security (OWASP) → `training/navigation/SECURITY-STORY-BANK.md` (A01/A02/A03/A04/A09/A10 sections); ★US-16 SSRF + webhook defects
- code review / verifying AI output → the same bank (classify 25 AI-written tickets; 10 false gaps), `_answers/SECURITY-STORY-BANK-placements.md`
- unfamiliar-codebase navigation → `training/navigation/SEAM-DJANGO-TS.md`
- legacy rescue / migration-porting → `SEAM-DJANGO-TS.md` §3 (half-migrated .es6.js→TS via globals) + "Why?" + `DOC-TREE-VERDICTS.md` (Rewrite Plan as critique prompt)
- data modeling / migrations → bank "Traps" (Django Evolution vs makemigrations), ★US-01/US-10 answers (expand-contract, evolutions)
- observability / audit logging → ★US-12, ★US-10
- performance → US-13 (API-only N+1)
- reliability / timeouts → ★US-22, ★US-24
- web/TS contract → `SEAM-DJANGO-TS.md` §4
- (authz/IDOR is saturated. It's included only as classification drills, and I added no new authz exercises.)

## Curriculum needs (not written)
- **SSRF-safe outbound HTTP (webhooks, URL fetchers):** scheme allowlist, resolve-then-block private ranges, check again at dispatch time (DNS rebinding), redact credentials from logs, timeouts. Recurs across webhook-bearing clones.
- **Security audit logging vs user notifications:** what an audit event must carry (actor, target id, never the secret, source IP and proxy trust), sinks, and why signal-based hooks beat logging calls inside resources.
- **Non-Django-migrations schema tools (Django Evolution and friends):** how to recognise one, and why `makemigrations` advice from AI is wrong in such repos. Probably fits as a short section of 07-zero-downtime-migrations rather than a new page.

## Existing learning-doc trees
- `User Stories/US-01..25`: **CONVERT (done)** into the verified bank. Do not follow the plans as written.
- `User Stories/25-Mixed-User-Stories.md` + `Junior/Sprint-1..4`: **IGNORE** (generic junior tasks).
- `docs/upskill/` (20 files): **KEEP** as a reading index, plus a small MERGE candidate (the "custom API layer vs DRF" contrast) if it recurs. It has factual gaps (no Evolution) and stale links.
- `Application Rewrite Plan/` (3 files): **IGNORE** as a plan; reuse as a system-design critique prompt.
- `docs/manual|codebase|releasenotes|stories`: upstream, KEEP (not learning material).

## Caveats
- Everything is static. I ran no tests, installed nothing and started no servers or containers. Line numbers are against `bb3d688`.
- One placement (★US-10) names a djblets hook I couldn't inspect, and the answer says so.
- This project doesn't target the batch's thin skills (SQL Server, EF Core). Its value is AI-ticket verification + OWASP classification + the legacy/modern seam.
