# Compare boundaries across projects

Use these after completing one project design. They are transfer exercises with worked reasoning, not a request to build a new distributed platform. Follow the [project index](README.md) to the source maps and detailed contracts.

## 1. Browser promise sharing versus durable command identity

**Compare:** GitJira's refresh gate with Helios's documented command-replay boundary.

**Worked distinction:** a shared pending promise can reduce duplicate work among callers that share that in-memory owner. After process loss it has no durable record. A command receipt is about recovering a logical accepted outcome after retries and lost responses. The receipt still needs scope, payload compatibility, retention, and a relationship to the effect's commit.

**Changed case:** restart the process after the effect but before the response. Explain which mechanism retains useful evidence. Then keep the process alive but log out during refresh; durable mutation identity does not answer which browser session may apply that refresh response.

**Artifact:** two timelines and one sentence per guarantee. Avoid saying both mechanisms provide exactly once without specifying what, where, and for how long.

## 2. A cache miss is not an authorization check

**Compare:** Bazaar catalog sharing, Perch private recruiter reads, and buildermentor source retrieval.

**Worked distinction:** equivalent public catalog requests may share a representation. Private candidate fields or user-owned chunks can require a narrower scope. Authorization must remain correct even when a cache or index bypasses the original query path. Query text alone does not identify a safely shareable private result.

**Changed case:** revoke access after a cached result is produced. Explain future reads, invalidation, deletion propagation, and whether an already delivered response can be retracted. Do not promise a stronger revocation effect than the system can implement.

**Artifact:** one key/representation table with a pair that may share and a pair that must not, plus a test inspecting raw returned data.

## 3. Select work, own work, and report work are separate steps

**Compare:** aaa1 row processing and Warband scheduled-event resolution.

**Worked distinction:** ordering pending work answers what a worker wants to attempt. Claiming or a conditional transaction determines who may apply the effect. Reporting progress describes stored outcomes. A correct selector can coexist with duplicate effects or misleading progress if the later boundaries are wrong.

**Changed case:** two workers select the same item, one pauses, its lease expires, and it resumes after another worker completes. A lease-based design needs an ownership check at the effect/commit boundary, not only at initial selection.

**Artifact:** a five-stage diagram and a crash table. Include the identity checked by each stage and the durable state visible to a replacement worker.

## 4. Local rollback versus external reconciliation

**Compare:** Helios repair rollback with BuildEvent payment evidence and buildermentor provider usage.

**Worked distinction:** included database writes can share a local atomic boundary. A provider may have performed work even when the local caller loses its response. Rolling back local rows does not necessarily reverse a payment or eliminate a generation bill. An uncertain result needs correlation and reconciliation, not a fabricated success or failure.

**Changed case:** restore the database to an earlier point while the provider still remembers a successful request. Explain how a restored receipt or reconciliation process avoids repeating an external effect blindly.

**Artifact:** mark the boundary of the local transaction and draw each external effect outside it. State the recovery question in terms of actual facts available from each side.

## 5. An offline draft and an accepted shared record

**Compare:** RouteIQ pending delivery intent, Perch edited forms, and Grok versioned project changes.

**Worked distinction:** retaining a user's draft is a UI ownership decision. Accepting a shared change is an authorization/concurrency decision. A refresh should not silently erase newer edits, but preserving a draft does not entitle it to overwrite a newer accepted server revision.

**Changed case:** a user reconnects with an old expected revision after another actor changes the record. Show the current record, local draft, and accepted or conflicting operation as three separate values.

**Artifact:** a state table with a conflict result and a reconciliation path. A whole-object rollback that erases unrelated changes should fail the example.

## 6. Global averages versus a hot key

**Compare:** one popular ticket tier, one busy world, one hot catalog product, and one very large organization.

**Worked distinction:** equal aggregate request rates can produce very different contention and fanout. An additional API instance does not necessarily relieve a single authoritative row or an ordered stream. A cache can help a hot public read but may not be permitted for the critical write decision.

**Changed case:** concentrate half of the exercise load on one entity while leaving the total unchanged. Revisit queue fairness, lock contention, partition key, and downstream delivery. State which measurement would distinguish the bottlenecks.

**Artifact:** two workload sketches and one bounded intervention. Avoid adding every scaling mechanism at once, since that makes the source of improvement impossible to assess.

## A two-session capstone

In session one, choose two projects and produce a single comparison page: user journey, invariant, authority, repeated-operation identity, tolerated stale read, critical failure, and actual evidence. In session two, exchange the failure scenarios between them and explain which assumptions no longer hold.

The strongest result may be that the same abstract principle requires different implementations. A small React state owner, a conditional database write, and a provider reconciliation record are not interchangeable simply because all involve freshness or identity. Preserve that distinction in both the diagram and the spoken explanation.
