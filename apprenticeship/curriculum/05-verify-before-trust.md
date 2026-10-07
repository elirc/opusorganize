# 05 — Verifying code you didn't write (AI output, legacy code, docs)

This is the core skill of the agentic era. An agent, old AI output or a README *claims* something, and you cheaply establish what is actually true.

**Verification ladder** (stop when the code has earned your trust)
1. **Does it build?** 3 of the 5 generated B01 apps don't build from a clean clone.
   - netauth calls a nonexistent `Database.GetMigrationsAsync()` (`Program.cs:141`), an API the generator made up.
   - netdrop's `.gitignore:8` (`storage/`) swallowed `Infrastructure/Storage/*.cs`, so that code was never committed, and its EF model throws on first use (`NetDropboxDbContext.cs:44`).
   - netstripe's `main` does not compile: `IdempotencyMiddleware.cs` is missing a `using`, and `Program.cs:143` has a `Money?` ternary type error. Meanwhile 90+ files of curriculum describe its runtime behavior.
2. **Do tests exist, and do they assert something?** netramp and netstripe ship "testing strategy" docs and zero test files.
3. **Do the comments' claims hold?** In netramp, the "constant-time" login short-circuits before PBKDF2, and the "thread-safe" DataStore isn't thread-safe.
4. **Are integrations real?**
   - netstripe: webhook "delivery" never makes an HTTP call, and `PaymentWorker` hardcodes success.
   - netintercom: OTel has no exporter, and snooze never wakes.
5. **Do the repo's own reviews hold?** netintercom's `docs/architecture-review.md` §2.3 is wrong about concurrent sweeps.
6. **Run the risky path** (a concurrency test, a failing-input test) before signing off.

**Checklist for any agent PR**
- Run the tests.
- Read the whole diff.
- Check each claim in the PR description against the code.
- Grep for `TODO`, `mock`, `fake`, hardcoded success and swallowed exceptions.
- Confirm migrations are reversible.
- Confirm there are no secrets or config defaults that fail open.

Your per-project version is `netintercom/training/agentic/VERIFY_AI_OUTPUT.md`.

**Where these repos live now.** netauth → `elirc/dotnet-auth` · netdrop → `elirc/dotnet-drop` · netstripe → `elirc/dotnet-stripe` · netramp → `elirc/dotnet-ramp` · netintercom → `elirc/dotnet-intercom` (so the checklist above is at `elirc/dotnet-intercom: training/agentic/VERIFY_AI_OUTPUT.md`).

## Status of every claim above, re-checked 2026-10-06

The ladder above is the B01 snapshot (2026-09-23), when builds were run with SDK 10.0.302. For this re-check I **read the code at HEAD but did not build anything**. "Still present" means the offending line or omission is still in the file, not that I saw a compiler error.

| Claim | Repo @ HEAD | Status |
|---|---|---|
| `GetMigrationsAsync()` at `Program.cs:141` | dotnet-auth `117d9d7` | **Still present**: `src/NetAuth0.Api/Program.cs:141`, `if ((await db.Database.GetMigrationsAsync()).Any())`. EF Core is 8.0.8 (`src/NetAuth0.Application/NetAuth0.Application.csproj:12`). Also note `global.json` pins SDK `8.0.0` with `rollForward: latestFeature`, which is why B01 needed a temporary override to build on a machine with only SDK 10. |
| `.gitignore:8` swallows `Infrastructure/Storage/*.cs` | dotnet-drop `d7ae725` | **Still present.** `src/NetDropbox.Infrastructure/` has no `Storage/` folder, yet `DependencyInjection.cs:11` has `using NetDropbox.Infrastructure.Storage;`. `git check-ignore -v src/NetDropbox.Infrastructure/Storage/LocalBlobStorage.cs` prints `.gitignore:8:storage/`. |
| EF model throws (`NetDropboxDbContext.cs:44`) | dotnet-drop `d7ae725` | **Fixed after B01.** At B01, line 44 was `HasMany<FileVersion>("_versions")`, which clashed with `b.Navigation(x => x.Versions)` (sealed `training/_answers/review.md` finding 2). Commit `9d28a29` (2026-09-30) changed it. At HEAD, line 44 reads `b.HasMany(x => x.Versions)`. `training/ladder/J0-make-main-build.md` line 3 records this. |
| netstripe missing `using` + `Program.cs:143` ternary | dotnet-stripe `8f40257` | **Still present.** `IdempotencyMiddleware.cs:90` uses `IBillingClock` (namespace `Billing.Api.Domain`, `Domain/BillingClock.cs:1`) with no matching `using` in lines 1-3, and no global using exists. `Program.cs:143` is still `request.AmountOff is null ? null : Money.FromMajor(…)`. Both fixes are visible in incident commit `8b0c838`. |
| Zero test files (netramp, netstripe) | dotnet-ramp `709feb8`, dotnet-stripe `8f40257` | **Still true.** `find . -iname "*test*"` lists only `docs/…/01-testing-strategy.md`, `02-writing-tests-here.md` and the `training/` exercises. |
| "constant-time" login | dotnet-ramp | **Still present**: `backend/Security/AuthService.cs:27-29`. The comment claims a constant-time check, and line 29's `user is null \|\| !PasswordHasher.Verify(...)` skips the hash for unknown emails. |
| "thread-safe" DataStore | dotnet-ramp | **Still present**: `backend/Storage/DataStore.cs:11-12`. See [03](03-concurrency-races.md). |
| Webhook delivery never sends; `PaymentWorker` hardcodes success | dotnet-stripe | **Still present.** `WebhookDeliveryWorker.cs` contains no `HttpClient` (grep count 0), and line 35 writes `"Simulated delivery. Replace with durable HTTP delivery in production."`. `PaymentWorker.cs:42` is `succeeded: true,`. |
| OTel has no exporter; snooze never wakes | dotnet-intercom `74e0a28` | **Still present.** `src/NetIntercom.Api/Program.cs:128-130` configures a resource and ASP.NET Core tracing but no exporter. `Conversation.Snooze` sets `SnoozedUntilUtc` (`Conversation.cs:76`), and no code reads it back except the DTO mapping (`Dtos.cs:63,71`). |
| §2.3 is wrong | dotnet-intercom | **Still wrong in the text** (`docs/architecture-review.md:74`). The repo has added a correction note at line 5. |

---

## Worked trace: "does it build?" by reading, on dotnet-drop

You can often predict a clean-clone build failure without a compiler. That's useful when you're reviewing on GitHub, or when the toolchain isn't installed.

1. **List what the code imports.** `src/NetDropbox.Infrastructure/DependencyInjection.cs:11` has `using NetDropbox.Infrastructure.Storage;`, and lines 30-52 construct `FileSystemChunkStorage`, `S3CompatibleBlobStorage` and `LocalBlobStorage`.
2. **List what git tracks.** `git ls-files | grep -i "Infrastructure/Storage"` returns nothing.
3. **Ask why.** `git check-ignore -v <a path under Storage/>` names the rule: `.gitignore:8:storage/`. That rule was meant for the runtime upload folder (`DependencyInjection.cs:51` defaults to `…/storage`). But an unrooted `storage/` matches a directory of that name at any depth, and on Windows git runs with `core.ignorecase=true`, so it also matched the `Storage/` *source* folder. The files existed on the author's disk and never reached the repo.
4. **Predict the error.** A `using` for a namespace that no tracked file declares is `CS0246`. Every type it was supposed to supply is missing too.
5. **Notice what *didn't* catch it.** The author's machine built fine, because the files were on disk. Only a **clean clone** reproduces the failure, which is why rung 1 says "from a clean clone".

The same read-only method works on the other two:
- **dotnet-auth:** EF Core 8 exposes `GetMigrations()`, `GetAppliedMigrationsAsync()` and `GetPendingMigrationsAsync()`. There is no `GetMigrationsAsync()`. A plausible-sounding name on a well-known API is the classic hallucination signature. Check it against the package's API docs.
- **dotnet-stripe:** a `readonly record struct` (`Money`) in one branch of a ternary and `null` in the other has no common type. Read line 143 and the type's declaration together.

## Verified senior findings

- **Docs volume is not evidence.** dotnet-stripe has 46 `docs/upskill/` + 47 `docs2/` files (B01 count) describing runtime behavior of an API that has never compiled on `main`. dotnet-intercom's own architecture review, the best doc in the batch, still had a wrong concurrency claim (§2.3), and only reading `CheckSlaBreaches.cs:34-53` together with the `SlaTimer` mapping exposes it. Treat every doc as a *claim with a line number you haven't checked yet*.
- **Fixes landed without the checks catching up.** dotnet-drop's EF mapping was fixed in a commit titled "Sync local changes to GitHub" (`9d28a29`), but the storage folder, half of the same ticket, is still missing. "Someone fixed the build" turned out to be half true. Re-verify at HEAD before quoting any status, including this page's.

## Goal + Check ladder

**Goal:** given a repo or agent PR you didn't write, establish within 30 minutes what is true, with a file:line or command output behind every sentence.

1. **Junior: clean-clone reality check.** Run `gh repo clone elirc/dotnet-drop -- --depth 1`, then `git ls-files | grep -i storage`.
   **Check:** no `src/NetDropbox.Infrastructure/Storage/*.cs` is listed. On Windows (`core.ignorecase=true`), `git check-ignore -v` attributes it to `.gitignore:8`. On a case-sensitive Linux/macOS checkout the rule wouldn't match `Storage/`, which tells you the files were lost on the author's Windows machine.
2. **Junior: find the phantom API.** `grep -rn "GetMigrationsAsync" .` in `elirc/dotnet-auth`.
   **Check:** exactly one hit, `src/NetAuth0.Api/Program.cs:141`. You can name the three real EF Core methods it was probably confused with.
3. **Junior+: comment vs code.** Open `dotnet-ramp: backend/Security/AuthService.cs:27-29`.
   **Check:** you can explain, in one sentence, why an attacker can tell "no such user" from "wrong password" by timing.
4. **Mid: integrations.** For `dotnet-stripe`, grep `WebhookDeliveryWorker.cs` for `HttpClient` and read `PaymentWorker.cs:42`.
   **Check:** you report "webhook delivery is simulated, payment success is hardcoded", each backed by a line number. *Run locally* (after the two build fixes): every webhook row shows `Succeeded` with the "Simulated delivery" message.
5. **Mid→senior: audit an agent PR with the checklist.** Use `dotnet-intercom: training/agentic/WORKFLOW.md` + `VERIFY_AI_OUTPUT.md`.
   **Check:** every sentence of the agent's summary is ticked with a line, *or* struck through as false. Integration tests are either run or written down as "UNVERIFIED", never just accepted.

## Debugging scenario

*An agent opens a PR on dotnet-drop: "Fixed the build. All tests pass." CI is green on the PR branch.*

1. **Which build?** Check whether CI ran on a clean checkout. If the agent's workspace had untracked `Storage/*.cs` files, its local build passes and a clean clone doesn't. Run `git ls-files` on the PR branch.
2. **Which tests?** Compare the test count with `main`. "All tests pass" with the same count means nothing new was proven. The checklist line in `VERIFY_AI_OUTPUT.md` ("the count went **up** by the number of tests the agent claims to have added") applies.
3. **Which claims?** "Fixed the build" should come with a diff that adds the storage adapters *and* narrows `.gitignore:8` to the runtime path, for example a rooted `/storage/`. Without the `.gitignore` change, the next storage file will vanish too.
4. **Close the loop:** re-clone, build, test, and paste the real output into the PR. That's the whole skill: replace "it says" with "I ran" or "I read line N".
