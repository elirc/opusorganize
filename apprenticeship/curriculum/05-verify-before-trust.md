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
