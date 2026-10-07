# 04 — Characterization tests for untested code

**When.** You must change code that has no tests, which is very common in legacy and AI-generated code. **Pin down current behavior** before you change it.

**How**
1. Pick the seam: a mostly pure service such as a state machine or pricing engine.
2. Cover the input space systematically (every state × every action × every role) with table-driven tests.
3. Assert what the code *does today*, even if it looks wrong. Mark suspicious cases `// BUG?` and file them; don't silently "fix" them.
4. Refactor or change the code under that safety net. A failing test is then a *decision*, not an accident.

Characterization tests are not correctness tests: they pin down reality, while correctness tests encode the spec. You need the first before you can safely move to the second.

**Worked examples in your repos**
- netramp: `training/review/CHARACTERIZATION_TEST_EXERCISE.md` (the approval state machine). The reference was verified: 14/14 pass on main, and 3 fail once incident 001's one-entry bypass is applied.
- netstripe: `training/review/characterization-tests-billingengine.md` (BillingEngine). It had zero tests, and `main` didn't even compile (see [05](05-verify-before-trust.md)).

**Where these repos live now.** netramp → `elirc/dotnet-ramp` · netstripe → `elirc/dotnet-stripe`. Re-read on 2026-10-06 at dotnet-ramp `709feb8` and dotnet-stripe `8f40257`. Line numbers are for those commits.

> **What "verified" means above.** The netramp 14/14 → 3-fail run (B01, 2026-09-23) was made on a *standalone* `dotnet new xunit` project that held copies of `ExpenseStateMachine.cs` and `Enums.cs` and targeted `net10.0`. It was not run against the real `net8.0` project, because no test project exists in the repo. `_answers/characterization-test.md` says so itself. Both repos still have **zero test files** at HEAD: `find . -iname "*test*"` returns only docs and the exercise files. netramp's incident branches were never pushed (see `training/README.md`, status note at lines 64-75). The one-entry diff is described in the sealed answer, so you re-apply it by hand. netstripe's branches are on GitHub.

---

## Worked trace: dotnet-ramp's `ExpenseStateMachine`

`elirc/dotnet-ramp: backend/Domain/ExpenseStateMachine.cs` is a perfect first seam. It's a static class with no DI and no `DataStore`, and its doc comment (lines 4-6) claims it is the "single source of truth … so that illegal transitions are impossible".

**The input space** comes from `backend/Domain/Enums.cs`. There are 3 roles (`UserRole`, lines 4-12: Employee, Manager, Finance) and 6 statuses (`ExpenseStatus`, lines 17-26: Draft, Submitted, Approved, Rejected, Reimbursing, Reimbursed). That gives 6 × 6 × 3 = **108** `(from, to, role)` triples for `CanTransition`, and 36 pairs for `CanSystemTransition`.

**The behavior** is all in one dictionary (lines 19-43):

| From | To | Roles |
|---|---|---|
| Draft | Submitted | Employee |
| Rejected | Submitted | Employee |
| Submitted | Approved | Manager |
| Submitted | Rejected | Manager |
| Approved | Reimbursing | Finance |
| Reimbursing | Reimbursed | *(empty array = system-only)* |

Now read the four members against that table:
- `CanTransition` (51-54) needs the `from` key, the `to` key **and** the role in the array. So it is true for exactly **5** of the 108 triples. The empty array on the last row makes `Reimbursing → Reimbursed` false for every human role.
- `CanSystemTransition` (57-58) skips the role check, so it is true for exactly **6** of the 36 pairs.
- `IsTerminal` (45) is true only for `Reimbursed`.
- `NextStates` (47-48) returns the dictionary keys for `from`. `Reimbursed` has no entry, so it returns an empty array.

That's the whole characterization: two "exact legal set" assertions plus 6 `IsTerminal` cases and 6 `NextStates` cases. **2 + 6 + 6 = 14**, which matches the reference test's count.

## The failure window: one dictionary entry

Incident 001's "fast-track" PR adds one line under `[ExpenseStatus.Submitted]`: `[ExpenseStatus.Reimbursing] = new[] { UserRole.Finance }`. Here is what changes:

1. `CanTransition(Submitted, Reimbursing, Finance)` flips to true. Finance can now pay an expense no manager approved.
2. `CanSystemTransition(Submitted, Reimbursing)` flips to true.
3. `NextStates(Submitted)` gains `Reimbursing`.
4. `IsTerminal` doesn't change.

So an exhaustive test catches it **three times** (the recorded run: "Failed: 3, Passed: 11"). A spot-check test like "Manager can approve a Submitted expense" stays green. The bug lives in the cases nobody thought to write, which is why step 2 of "How" says to cover the input space *systematically*.

The callers inherit whatever the table allows. `ExpenseService.Transition` (`backend/Services/ExpenseService.cs:169-179`) asks only `CanTransition` (line 171), and `StartReimbursement` (150-156) goes through it. There's no second check downstream.

## The second seam: dotnet-stripe's `BillingEngine`

`elirc/dotnet-stripe: src/Billing.Api/Infrastructure/BillingEngine.cs` is less pure. Its constructor takes `BillingStore` and `IBillingClock` (line 7), and `BillingStore`'s constructor seeds fixed data from the clock (`BillingStore.cs:19-22` calls `Seed`, which starts at line 267). The exercise's tip is to pass a fake clock that returns a fixed instant, so seeded periods and due dates are deterministic. Its 8 cases include two deliberate "write down what it does, even if it's wrong" probes: item 6 (`RunBillingCycle` twice, pointing at the race in [03](03-concurrency-races.md)) and item 8 (`ApplyPaymentResult` twice, pointing at the missing webhook dedup in [02](02-idempotency.md)). Those are the `// BUG?` cases from step 3 of "How".

**A precondition the netramp seam doesn't have:** dotnet-stripe's `main` doesn't compile ([05](05-verify-before-trust.md)), so `dotnet new xunit … && dotnet add reference` will fail until you apply the two one-line fixes. The incident-001 commit `8b0c838` shows them (a `using Billing.Api.Domain;` and a `(Money?)null` cast). Making those fixes is your first characterization decision. They change compilation, not behavior.

## Verified senior findings

- **Characterize the fields too, not just the transitions.** `ExpenseService.Reject` sets `RejectionReason` (`ExpenseService.cs:144`), and nothing clears it. `grep -rn RejectionReason backend` finds only the property (`Expense.cs:30`), the DTO, the mapping (`Mappings.cs:33`) and that one setter. An expense that was rejected, resubmitted and approved still carries the old reason. A transition-only characterization misses this. Pin it with a test that asserts the stale value, marked `// BUG?`, then fix it under the dotnet-ramp ticket `training/tickets/J1-clear-stale-rejection-reason.md`.
- **Money math is a characterization trap.** `Money.Multiply` (`src/Billing.Api/Domain/Money.cs:43-45`) rounds with `MidpointRounding.AwayFromZero`. Incident 002 (`bfce8de`) replaces that with a truncating cast. Round-number inputs give identical results either way, so a characterization test with hand-picked whole-dollar inputs won't catch it. Include inputs whose fractional minor unit is ≥ 0.5 (the brief `training/incidents/002-mrr-rounding-drift.md` explains the drift).

## Goal + Check ladder

**Goal:** before changing untested code, produce a fast, exhaustive test that would turn red on any behavior change, and show that it does.

1. **Junior: derive the legal table by reading.** Using only `ExpenseStateMachine.cs` and `Enums.cs`, write the table above yourself.
   **Check:** 5 true `CanTransition` triples, 6 true `CanSystemTransition` pairs, 1 terminal state. Compare with the sealed `training/_answers/characterization-test.md` only afterwards.
2. **Junior: write the test** in a new `backend/ExpenseManagement.Api.Tests` project (`dotnet new xunit`, referencing `ExpenseManagement.Api.csproj`).
   **Check (run locally):** `dotnet test` reports 14 passed if you follow the reference shape. A different but exhaustive shape is fine; count your own cases.
3. **Junior+: prove it bites.** Apply incident 001's one entry by hand (the branch isn't on GitHub) and re-run.
   **Check (run locally):** exactly the `CanTransition` set, `CanSystemTransition` set and `NextStates(Submitted)` cases fail. Then revert.
4. **Mid: dotnet-stripe items 1-8.** Make `main` build first.
   **Check:** items 6 and 8 have a written prediction *and* a recorded actual result, each marked `// BUG?` where they differ from what you'd want.
5. **Mid→senior: change under the net.** Fix the stale `RejectionReason` (netramp J1) or add webhook `EventId` dedup (netstripe).
   **Check:** exactly the `// BUG?` tests you meant to change go red, you update them in the same commit with a message saying why, and nothing else changes.

## Debugging scenario

*"Internal Audit found `Reimbursed` expenses with no `Approved` event in their history."* (This is netramp INC-001's symptom.)

1. Behavior was gated by one table, so diff that table first: `git log -p -- backend/Domain/ExpenseStateMachine.cs`.
2. Without history, ask the code directly. Your characterization test does that. Run it, and the failing triple names the illegal edge (`Submitted, Reimbursing, Finance`).
3. Check the blast radius: which expenses have a `History` (`Expense.cs:39`) entry going `Submitted → Reimbursing`? Those were paid without approval.
4. Root-cause lesson: the PR passed review because no test enumerated the space. Add the characterization test to CI before reverting the entry, so the revert is itself under test.
