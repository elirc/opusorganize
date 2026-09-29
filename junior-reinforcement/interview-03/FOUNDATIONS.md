# Interview foundations: explain, demonstrate, transfer

Use these as short reference answers after an attempt, not scripts to memorize. For each question, give a concrete input, predict the result, and connect the mechanism to one of the project scenarios. The [official references](REFERENCES.md) support language and framework study; project-specific claims still require inspecting local source. Examples here are teaching examples, not descriptions of newly implemented features.

## JavaScript and data structures

### 1. What does copying an object with spread actually copy?

A spread creates a new outer object containing copied property values. If one value is another object, both outer objects can still refer to that same nested object. Demonstrate this with two stop records sharing an address. Copy the path you intend to change and assert that the unrelated record stays unchanged. Explain ownership before reaching for a universal deep-cloning solution.

### 2. When would you choose Map instead of repeated array searches?

Use an index when the operation repeatedly looks up records by identity. Building it has a time and space cost, so compare the complete workload rather than one lookup. In a merge of n rows and m updates, an index can avoid scanning all n rows for every update. Keep output order as a separate contract; a faster lookup structure does not choose the product's display order.

### 3. What problem does Set solve, and what does it leave undecided?

A Set removes repeated values under its equality rules. It does not decide whether differently cased skill names or email strings represent the same domain identity. Normalize only according to a stated policy before deduplicating. For object values, distinct objects with identical-looking fields remain distinct identities. Explain why a set of record objects differs from a set of record IDs.

### 4. Why is a deterministic tie breaker important?

A primary sort field can be equal for several records. If a page boundary or batch limit cuts through that group, the contract needs a complete order to produce reproducible results. Use a stable opaque identifier as a secondary field when appropriate. A tie breaker fixes ambiguity within a snapshot; it does not freeze concurrent changes to the collection.

### 5. How do you discuss time complexity without overselling it?

Define the input sizes and count the work that grows with them. Include preprocessing, sorting, repeated scans, and output construction. Distinguish average or expected behavior from a worst-case guarantee when relevant. A helper using a Map can still be quadratic if it scans an entire second collection inside a loop. State string-processing costs when identifier or text length is not bounded.

### 6. What is the difference between working space and output space?

Working space is temporary storage used to compute a result; output space is storage required by the returned result. A function returning n records cannot claim constant total space merely because it uses only a few loop variables. State whether your complexity explanation excludes output. An immutable result may intentionally use more space to preserve caller-owned inputs.

### 7. When is a graph a useful model?

Use a graph when the important relationship connects entities rather than placing them in one simple list. Issue prerequisites form directed edges. A topological order is possible only when the directed dependency graph is acyclic. Missing referenced IDs are a different error from a cycle, and a partial order returned after getting stuck should not be described as a complete successful plan.

### 8. What do BFS and DFS help you explain?

Both explore reachable nodes while tracking visited state. Breadth-first traversal explores increasing edge distance in an unweighted graph; depth-first traversal follows a branch before returning. Choose based on the required result, not familiarity alone. If you need shortest paths with weighted costs, explain why an unweighted BFS assumption no longer suffices. Count vertices and edges in the complexity argument.

### 9. When does a sliding window apply?

A sliding window is useful when a range can be updated incrementally as its boundaries move and the condition supports that strategy. State the invariant that allows the left boundary to advance. Do not apply it to arbitrary inputs merely because the problem mentions a subarray. For example, assumptions about nonnegative values can matter when searching by accumulated sum.

### 10. What should you clarify in a string question?

Ask whether comparison is case-sensitive, whether whitespace is meaningful, and whether the unit is code units, code points, or user-perceived characters. An interview can explicitly restrict input to ASCII; name that restriction instead of claiming the same implementation handles every language. For opaque IDs, avoid applying human-text normalization unless the identity contract permits it.

## Asynchronous behavior and APIs

### 11. What does a closure retain?

A closure retains access to its lexical environment. The important interview task is to identify which binding or value a later callback observes, not to say that closures always preserve a frozen copy of everything. Trace creation, mutation, and invocation in order. In React, relate a handler to the render that produced it and distinguish that from a deliberately mutable reference.

### 12. Why can a successful earlier request still be obsolete?

Success describes the request's outcome, not whether its result belongs to the current view. A user can change search text, organization, world, or selected item while the request is pending. Associate results with their request and scope identity, and check that identity when applying them. A later arrival is not necessarily a newer observation.

### 13. What does cancellation fail to prove?

Stopping local waiting or signaling abort does not prove that a remote side effect never occurred. The server might have committed before the client lost interest or connectivity. Keep cancellation, stale-result rejection, and durable operation reconciliation as separate ideas. Use a lost-response example to explain why an uncertain mutation should not automatically be retried with a new identity.

### 14. What goes wrong when promises are created but not returned or awaited?

The caller can finish before the work it intended to observe, and errors may escape the intended chain. Draw which promise represents completion of the whole operation. Ask whether a callback intentionally starts independent background work or accidentally detaches required work. A passing assertion immediately after launch may inspect state before the relevant operation has settled.

### 15. Does Promise.all start asynchronous work?

The operations generally start when the expressions producing their promises execute. Promise.all combines the supplied outcomes; it is not a concurrency limiter. A rejection does not by itself cancel the other operations. If a task needs at most a fixed number of active requests, define a scheduling policy and test the active-count boundary rather than assuming aggregation supplies one.

### 16. How do you test a race without arbitrary sleeps?

Control the order that produces the race. Create two deferred operations, start both, resolve the second first, and assert what is accepted before resolving the first. Inject time when deadlines matter. This makes the causal order explicit and reduces dependence on machine speed. A fixed delay that happens to expose the bug locally is weaker evidence.

### 17. What is the useful distinction between authentication and authorization?

Authentication establishes the identity the system accepts for a caller. Authorization decides whether that caller may perform this action on this resource in this scope. A valid session does not authorize every organization or project. Trace the trusted context and the scoped operation; hiding an edit button does not enforce a server-side permission boundary.

### 18. What makes an operation retryable?

The answer depends on its side effects, identity, failure mode, and server contract. A failed read and a mutation with a lost response present different risks. Bound attempts and identify which failures qualify. For repeated logical writes, explain the durable mechanism that recognizes the same intent. A client-generated key is only useful if the server applies an appropriate contract to it.

### 19. Why distinguish missing, null, zero, and empty string?

They can represent different intentions. In a patch, omission may preserve a value while null clears it; zero may be a valid estimate. An empty string may be a valid value, normalized input, or a validation error depending on the field. State those meanings explicitly and test them separately. Truthiness shortcuts often erase exactly the distinction the public contract needs.

### 20. What is an honest response to an uncertain mutation result?

Keep uncertainty visible and retain the operation identity needed for reconciliation. Do not label a timeout as a confirmed rollback or encourage a new irreversible action without checking the original outcome. Design a bounded status lookup or retry according to the actual service contract. The interface should help the user recover without claiming more certainty than the system has.

## React and TypeScript

### 21. What belongs in component state?

Start with information the component must remember across interactions, then identify its owner. A local draft, selected ID, and request status can have different lifetimes. Values derived from existing inputs need not become another independently updated copy. Demonstrate the ownership choice with a refresh arriving during an edit, and explain which value is allowed to win.

### 22. Why can array-index keys cause confusing behavior?

An index identifies a position, which can change when records are filtered, inserted, or reordered. If component identity should follow the record, a stable record ID is the appropriate key. Explain a concrete case involving per-row input state. Do not claim index keys are universally forbidden; explain whether the list can change and what identity the UI needs.

### 23. How do you decide whether an effect is appropriate?

Name the external thing being synchronized and the condition that starts and ends that synchronization. If the work is a calculation from current render inputs or a response to one user action, explain why it belongs there instead. When an effect owns a subscription, describe corresponding cleanup. Adding dependencies is not a substitute for deciding who owns a draft.

### 24. What does useMemo fail to guarantee?

Memoization is a performance tool, not a replacement for correct state ownership or a public semantic guarantee that work happens exactly once. Identify an actual expensive calculation and its inputs before proposing it. A stale response bug will not be fixed by memoizing a result with the wrong identity. Discuss observed cost separately from hypothetical optimization.

### 25. How should you model remote data states?

Represent states that require different behavior explicitly: initial, pending, success, empty success, failure, and possibly stale or uncertain. Avoid treating an empty array as both not loaded and loaded with no results. A discriminated representation can prevent contradictory combinations such as successful data with an unexplained error flag. Define whether old data remains visible during a refresh.

### 26. Why start external data as unknown?

It forces the code to establish a usable shape before consuming it. A cast can tell the type checker what to assume without examining the value. Narrow or validate at the boundary and construct an internal representation whose preconditions are clear. In a JavaScript project, JSDoc and runtime schemas can support the same distinction without converting the whole application.

### 27. What is the purpose of an exhaustive outcome handler?

Different outcome variants can require different UI or domain behavior. An exhaustive handler makes a new variant visible to reviewed callers instead of silently falling into success. Static checking helps current compiled code; an older deployed client still needs a runtime fallback for unfamiliar data. Explain both sides of compatibility rather than treating compilation as the entire deployment story.

### 28. Why is valid JSON not sufficient validation?

Parsing establishes syntactic validity. The application may still need required fields, ranges, allowed identifiers, and relationships such as a correct option belonging to the supplied options. After those checks, factual accuracy and authorized grounding can remain separate concerns. Use a payload that is structurally plausible but violates one cross-field rule to demonstrate the distinction.

### 29. What would you test in an accessible form interaction?

Choose a concrete workflow: locate a labeled control, enter data, submit by keyboard, observe pending behavior, and discover a meaningful error or result. For dialogs, inspect focus entry and recovery in an actual browser. A role query is useful but does not establish complete accessibility. Prefer semantic controls and verify the behavior the product actually requires.

### 30. How do you handle an old saved object after a schema change?

Define a compatibility policy at the restore boundary. Optional additions may have a justified default; missing required data may require rejection or migration. Preserve an old fixture and test its result alongside the new shape. Do not assume an assertion, a renamed interface, or recompiling current callers changes bytes already stored in a browser or database.

## Testing, design, and project defense

### 31. What makes a test discriminating?

It fails for a plausible implementation that violates the intended behavior. Name that wrong implementation before writing the assertion. For identity bugs, assert the specific entity and an unrelated unchanged entity. For transaction behavior, inspect persisted effects after the failure. Passing a happy-path test tells you little about a failure branch that the fixture never exercises.

### 32. When does a mock hide the problem?

A mock can assume the property the test is supposed to establish. If a mocked repository always returns scoped records, the test cannot prove the actual query includes tenant scope. If a mock throws before any real write, it cannot prove a real transaction rolls back late effects. Use controlled dependencies at the right boundary and name what the test leaves outside its evidence.

### 33. What does a database transaction buy you?

It gives a defined atomic boundary for the work actually included in it, subject to the database's semantics and the implementation. Identify every write and where commit occurs. A remote effect is not automatically part of that transaction. A function containing several database calls is not proof they share a transaction. Trace and test a late failure window.

### 34. Why can a balanced total hide incorrect groups?

Errors in different groups can cancel when aggregated. A journal audit should preserve the organization and journal identity at which the invariant is defined. The same idea applies to per-tenant counts or per-job progress. Show two individually invalid groups whose global sum appears correct, then explain why the grouping key belongs in the verification contract.

### 35. What belongs in a cache key?

Include the dimensions that change the cached representation or its sharing scope. Determine whether localization, currency, store, or authorization-dependent data is inside the cached computation. Normalize only according to the field's semantics. More fields do not automatically make a key correct, and removing an entry does not prevent an older in-flight loader from filling it again.

### 36. What is the difference between selection and ownership?

A selector decides which work a caller would like to perform. Ownership or an idempotent application boundary determines whether competing callers can apply the same effect safely. Sorting due events does not claim them. A per-batch quota also does not establish long-term fairness. Keep these properties separate in both the diagram and the tests.

### 37. How do you choose an index in a design discussion?

Start with a concrete query's predicates and ordering, expected data shape, and the write workload. Describe the plan you want the database to support and the measurement that would confirm it. Do not promise an index makes every query fast or has no cost. For keyset pagination, ensure the cursor tuple matches the query's complete ordering contract.

### 38. What is a useful observability signal?

It has a known writer, meaning, scope, and failure interpretation. A recent HTTP response can establish request availability while domain work remains stalled. A histogram of completed work does not automatically describe work that never completes. Combine signals only after explaining what each observation confirms and which unknowns remain. Avoid invented production thresholds or performance measurements.

### 39. How should you describe a project built with assistance?

State your actual role and evidence. You can discuss requirements you defined, code you traced, tests you wrote, suggestions you rejected, and changes you verified. Distinguish those from existing implementation and reference answers. An honest study example is valid interview material when named as such; invented ownership or impact makes follow-up questions impossible to answer reliably.

### 40. What do you do when you do not know the answer?

State the uncertainty, give the part you can reason about, and propose the smallest check that would settle the rest. Ask a contract question when the requirement is ambiguous. If time is limited, preserve a clear partial solution and identify its missing branch. Confidence is useful only when it matches evidence; a precise verification plan is better than an unsupported guarantee.

## Ten-minute retrieval routine

Choose two questions from different sections. Answer each aloud in ninety seconds, then produce a concrete fixture for one of the ten projects. Give a wrong implementation and the assertion that would reject it. Close the reference and repeat with one changed assumption. Record what changed in your explanation, not merely whether your wording matched this page.
