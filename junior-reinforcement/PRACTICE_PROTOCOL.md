# How to use the reinforcement packs

## Predict, implement, transfer, explain

Write a prediction before running a test. A wrong prediction is useful: record the assumption it exposed. Solve the first lab yourself. Ask an agent for a hint or an explanation of a test failure only after you can state the input and expected behavior.

The isolated `.mjs` labs model one boundary with synthetic data. Their tests use `node:test` and `node:assert/strict`, need no install, and never contact the applications. Starters intentionally throw. `--reference` loads the sealed answer and is not your completion signal.

Once the model works, read the transfer exercise. Locate the real app's owning layer. Do not paste the model into production: compare domain contracts, validation, types, persistence, and failure handling first. If there is already a correct implementation, add missing evidence or write a characterization test instead of replacing it.

## Four kinds of evidence

| Evidence | What it establishes | What it does not establish |
|---|---|---|
| Source reading | A concrete code path and assumption | Runtime behavior or reachable wiring |
| Isolated model tests | The exercise contract on synthetic inputs | React, HTTP, database, or service integration |
| Application tests | Behavior at the boundaries actually exercised | Other environments or unexplored failures |
| Manual/runtime observation | The observed action in that environment | Universal reliability or future regressions |

Record the exact command, current commit, relevant working-tree differences, expected result, actual result, and the next unverified boundary. Save actual numbers rather than borrowing earlier report measurements.

## Working with existing code

Use read-only `git status --short`, `git diff --stat`, and `git diff -- <path>` before choosing an exercise workspace. Untracked files need inspection too. A worktree at HEAD omits uncommitted changes; never assume it is equivalent to the current app. In the Grok project, read the documented training snapshot before using an incident branch.

No reset, stash, mass cleanup, or recursive deletion is needed for this curriculum. Keep learner submissions in the new pack or an isolated practice branch. Before an app test, inspect its scripts and fixture rules, especially Helios's separate test database. Use one install/build at a time on this shared machine. Do not use live payments, real customer data, or paid model calls for these exercises.

## Agent practice after the first manual attempt

Give an agent a concrete spec: current behavior, requested change, allowed files, two acceptance examples, and one forbidden shortcut. Let it propose a diff; review every changed line and run the relevant checks yourself. Ask it to name assumptions and evidence, not to declare the project production-ready.

Keep your own prediction and final explanation. A useful review note says: “This test passes even if X is broken because Y is mocked; add a check at Z.” A vague “looks good” does not exercise judgment.

## A manageable week

Use four 45–90 minute sessions: source reading; lab; app transfer; recall and review. Finish projects 1–4 before opening the advanced half of the list. If setup is blocked, complete the source trace and pure lab and mark transfer pending. Do not award yourself runtime evidence from a reference answer.
