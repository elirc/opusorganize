# netdrop — B08 learn pass

**Path:** `C:\Users\Owner\Desktop\netdrop` (LAB tier, B01)
**Branch / commit:** `main` @ **`cb32ec5`** `docs(training): add learn/ study guide + junior on-ramp (B08)`. Parent `7329298` is the B01 training commit.
**Commit method:** `git add learn training` + `git commit -F <scratch msg> -- learn training` (pathspec). `git show --stat HEAD` shows only `learn/**` and `training/**`. The user's 15 uncommitted Astra entries in `git status --short` are byte-identical before and after (diffed).

## Files added (8 paths, +482 lines)
- `learn/README.md`: the study guide. Sections: what/why, known state of main, 6 prerequisites (curriculum 01/02/03/05/10 plus repo files), 11 timed sessions each with Files/branches, Do by hand, Delegate then verify, and Exit criterion; done criteria; next repo.
- `learn/00-onramp.md`: 8 junior warm-ups grounded in committed source:
  1. `UserStorageAccount` predict-the-output, with Release's 0 callers
  2. duplicate-folder request trace, with the non-unique index at `NetDropboxDbContext.cs:38`
  3. `FileNode.Move` dead guard and the folder cycle
  4. schema: unique indexes, the single FK, inert `Version` token
  5. `CompleteUpload` side-effect / transaction-boundary map
  6. `BlobObjectTests` characterization test
  7. resume edge cases (hash case, no `ExpiresAt` filter vs 15-min janitor)
  8. SPA expired-token lockout
- `learn/_answers/00-onramp.md`: sealed answers, with line citations.
- `learn/01-agentic-practice.md`: 4 drills (A: INC-004 query-shape test; B: INC-003 authorization matrix; C: INC-005 fail-closed JWT options; D: ladder M3 scan invariant), plus a 9-item NetDropbox-specific verification checklist that extends `training/agentic/VERIFY_CHECKLIST.md`.
- `learn/_answers/01-agentic-practice.md`: sealed rubrics (6 pts spec / 4 pts review each), with the named traps: InMemory makes a `DbCommandInterceptor` test pass vacuously; agents edit matrix expectations; `ProcessingWorker.cs:62` marks the node Clean without a current-version check.
- `training/ladder/J4-web-upload-client.md` + `training/_answers/ladder-J4.md` (new ticket), plus one row in `training/ladder/README.md`.

## Gaps filled
- **Web/TS thin** (batch1report netdrop skill links: "web/TS/React" was only 2 interview questions and 1 review item). J4 is the first frontend ladder ticket. It covers 401 not clearing the token (`api.ts:67-82`), `Promise.all` freezing the progress UI (`App.tsx:67-72`), progress keyed by `file.name`, whole-file `arrayBuffer()` hashing (split out as a follow-up), and adding the first web test runner (`web/package.json` has none).
- Caching (also flagged thin) was not addressed. There's no natural cache seam in this app; bazaar covers it.

## Skipped / UNVERIFIED
- Docs-only pass: nothing was built, tested or installed.
- UNVERIFIED claims, marked in the files:
  - the 6 domain tests building on `main` without J0 (inferred from the test csproj referencing only Domain and Application)
  - J4 reference code (not run)
  - the `revokeObjectURL`-after-click browser behavior
  - SQLite as an alternative provider for Drill A
  - the `ProcessingWorker.cs:62` stale-version race (code reading only)
- Runtime facts are cited from batch1report: main doesn't build; EF model throws; 5 incident branches build; 6/6 tests on INC-001.
- New finding while writing (not fixed, only in sealed answers): the `StartUpload.cs:51-58` resume lookup compares the raw request hash against a lower-cased stored hash and has no `ExpiresAt` filter.

## Study route (3 lines)
1. Sessions 1–4: read the shape, domain and schema; trace the three-store upload; write a first characterization test; get `main` building via J0 (agent types, you verify on a clean clone).
2. Sessions 5–9: junior tickets J1/J4, a hand-only blind review, then incidents 004/003/001/002/005 with agent-written regression tests under drills A–C, and M1 via `training/agentic/EXERCISE.md`.
3. Sessions 10–11: mid ladder M3/M4/M2 (drill D for M3), then trade-offs, S1–S3 designs and the interview kit with an agent as hostile interviewer. Next: **netintercom**.
