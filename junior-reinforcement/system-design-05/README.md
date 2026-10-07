# System design across the ten projects

This additive track turns the existing projects into focused system-design cases. It preserves the [original route](../README.md), [interview library](../interview-03/README.md), and [worked journals](../guided-04/README.md).

> **Links below (checked 2026-10-06):** the project links are relative to the 2026-09-28 Desktop layout and do not resolve on GitHub. Every linked pack exists on GitHub. The [repo map in the top-level README](../README.md#where-the-packs-live-on-github-checked-2026-10-06) shows where each one lives (for example, `gitvg/bazaar` is in `elirc/gitvg` and `astra1` is in `elirc/helios-interplanetary`).

| Order | Project design pack | Design problem |
|---|---|---|
| 1 | [RouteIQ / lucasrouter](<../../../lucasrouter/reinforcement/system-design-05/README.md>) | Design reliable delivery updates across devices and intermittent connectivity |
| 2 | [Perch](<../../../perch/reinforcement/system-design-05/README.md>) | Design application submission and private recruiter search with reliable receipts |
| 3 | [Grok multitenant project](<../../../grokbuildmultitenantproject/reinforcement/system-design-05/README.md>) | Design tenant-safe project writes and predictable list reads |
| 4 | [GitJira](<../../../gitjira-app/reinforcement/system-design-05/README.md>) | Design coherent issue views, session recovery, and notification-driven refresh |
| 5 | [Bazaar](<../../../gitvg/bazaar/reinforcement/system-design-05/README.md>) | Design a cached catalog whose fast results remain correct |
| 6 | [Helios / astra1](<../../../astra1/upskilling/reinforcement/system-design-05/README.md>) | Explain and extend a transactional repair workflow without overstating its boundaries |
| 7 | [aaa1 CRM](<../../../_Organized Desktop/12 Other Projects/aaa1/reinforcement/system-design-05/README.md>) | Design a resumable import pipeline with truthful progress and recoverable row effects |
| 8 | [BuildEvent](<../../../buildevent/reinforcement/system-design-05/README.md>) | Design ticket holds and payment reconciliation without overselling inventory |
| 9 | [ShipShape / buildermentor](<../../../buildermentor/reinforcement/system-design-05/README.md>) | Design authorized retrieval and bounded generation as a recoverable workflow |
| 10 | [Warband / astraspacegameweb](<../../../astraspacegameweb/reinforcement/system-design-05/README.md>) | Design a progressing event engine and reconnectable client state |

Each project has a worked architecture, API/data contracts, a failure/recovery lab, three checked capacity calculations, a decision record with a short worked journal, a timed interview, and separate reference reasoning. Diagrams and proposed contracts are explicitly distinguished from inspected current behavior.

Start with the [design method](DESIGN-METHOD.md). Use [cross-project drills](CROSS-PROJECT-DRILLS.md) to compare the same principle at different boundaries, and [primary references](REFERENCES.md) for selected database and delivery semantics. The [verification report](VALIDATION.md) records what was actually checked.

## A manageable practice route

Use RouteIQ or Perch to practice one request/command and its user outcome. Move to Grok and GitJira for scope, concurrency, and derived views. Use Bazaar, Helios, aaa1, and BuildEvent to deepen caching, transactions, worker recovery, and external-event reconciliation. Finish with buildermentor and Warband for multi-stage workflows, bounded resources, event ownership, and progress signals.

Choose one project per design session. Read source observations, attempt the forty-five-minute design, then compare the answer notes. Preserve the long-form guided material for concepts you need to slow down and reconstruct. Do not treat reading every page as demonstrated readiness.

## Offline capacity checks

From this folder:

```powershell
node --test tools/check-capacity.mjs
```

All worksheet workloads are hypothetical. The checks verify arithmetic and calculator boundaries, not application throughput, tail latency, database isolation, or live-provider behavior. No infrastructure is installed or deployed by this track.
