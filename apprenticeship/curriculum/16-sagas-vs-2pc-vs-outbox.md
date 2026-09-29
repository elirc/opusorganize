# 16 — Sagas vs 2PC vs outbox: keeping multi-step work consistent

**Problem.** A business action spans several services or resources: reserve stock, capture the payment, ship.
There is no single database transaction around all of them. What do you do when step 3 fails after steps 1–2 committed?

| Approach | How | Use when | Costs |
|---|---|---|---|
| **2PC / distributed transaction** | a coordinator locks all participants, then commits all | the participants support it and hold times are tiny | blocking, a coordinator SPOF, and it's unsupported by most modern stores and APIs (Stripe can't take part) |
| **Outbox** ([01](01-transactional-outbox.md)) | one local transaction writes the state plus an event, then relays it | *one* service must reliably tell others about its own change | it's a building block, not a multi-step workflow |
| **Saga (orchestrated)** | a coordinator runs steps and, on failure, runs **compensations** in reverse | multi-step business processes across services and external APIs | compensations must be idempotent; a workflow state machine is required |
| **Saga (choreographed)** | services react to each other's events | a few loosely coupled steps | the flow is invisible, and hard to debug and change |

**Rules that make sagas actually work**
1. **Every step and every compensation is idempotent** ([02](02-idempotency.md)); both will be retried.
2. **Persist saga state *with* the step's effect** in one local transaction. If they're split across two commits, a crash leaves a step done but unrecorded.
3. **Compensation is a business action, not a rollback.** A refund is not "un-capture", and some steps (sending an email) can't be undone.
4. **Every non-terminal state needs a timeout and a recovery scan,** plus an alert on "stuck for more than X". A saga that can hang forever will.
5. **Contracts between steps are versioned.** A renamed enum value can silently route an order into a state nothing handles.

**Worked examples in your repos**
- **astra5 (Stockade, Next.js + .NET):**
  - `training/incidents/001-payment-status-drift`: a Stripe `requires_action` mapping drift means 3-D Secure orders fall out of reconciliation forever.
  - Real finding: `services/Fulfil/Services/Worker.cs:70-78` splits capture-then-compensate across two committed transactions, so a crash leaves a captured order invisible to recovery *and* to the `stuckSagas` metric.
  - The interview set covers sagas vs 2PC vs outbox.
- **relay:** `training/ladder/S1`, a multi-day onboarding workflow with human approval, where compensations are derived from the checkpoint log and run in reverse with a bounded failure path. Engine mechanics are covered in [18](18-durable-execution.md).
- **eShop:** choreographed order flow via integration events (`training/navigation/01-checkout-outbox-correctness.md`).
- **modular-monolith-with-ddd:** cross-module integration events plus an internal-command queue (`training/navigation/03-*`).
- **atlas:** outbox plus webhook delivery; ticket S2 turns payroll preparation into a durable job.
