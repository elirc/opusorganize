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
