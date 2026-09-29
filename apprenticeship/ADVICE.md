# Advice: engineering after code got cheap

*Written 2026-09-24, after auditing ~350 project folders and turning 31 of them into training labs (batches B01–B07).
Every claim below points at something that actually happened in your own repos.*

---

## 1. The comment is right, and your archive is the proof

> "Engineering is not writing code."

You have roughly **350 project folders** on this machine. Almost all were written by models: 12 help desks, 12 issue trackers,
13 e-commerce apps, 7 EOR/payroll platforms, and about 200 generated `astraupskill` curriculum packs. **Code is not scarce for you.** You can
produce a plausible SaaS app in an afternoon, and so can everyone else.

What the seven batches kept finding was never "the code is missing". It was that **nobody had checked whether the code was true**:

| What the code or docs claimed | What was actually true | Human skill that would have caught it |
|---|---|---|
| netauth, netdrop, netstripe: 47–93-file curricula describing runtime behaviour | `main` **doesn't compile**. netauth calls an EF method that doesn't exist; netdrop's `.gitignore` swallowed its storage code | Verification: "does it even build?" |
| relay: 151 tests green, CI green | the engine **can't start**: BullMQ rejects the queue name `relay:runs` | Knowing what your tests *don't* touch |
| folio: an "offline-first" collaborative editor | **offline edits never reach the server** (a property test fails on its first case) | Understanding the problem space |
| buildermentor: an AI study engine with "cost guardrails" | generated questions from one user's **private upload are served to every user**; the budget is a pre-check that concurrent calls race past | Data model design; system design |
| HNJOBTRACK: "Supabase with RLS" | two tables have **no RLS**, so the public anon key can rewrite job apply links | Access control |
| aaa1, grokbuild: tenant scoping everywhere | a session-level `SET` on a pooled connection **leaked a tenant and deleted another tenant's row** | Distributed/concurrent reasoning |
| gitjira-app, relay, folio, atlas: runbooks, postmortems, ADRs | describe circuit breakers, alerts, drills and adapters that **aren't wired in** | Ops honesty, reading code over docs |
| VGdemo: a ".NET port" of a working TS app | the token is the raw user id, so **anyone can log in as anyone** | Porting judgement: what the old stack gave you for free |
| reviewboard: 25 generated security tickets | only **14 were real**; 10 were already handled, and 1 got the rule backwards | Verifying the ticket before building it |

Every one of those is a failure of **reasoning, verification, data modelling, access control or operations**, which is exactly the list in the comment.
None is a failure of typing code.

## 2. What that means for you specifically

You are not short on material. You are short on **reps of judgement under consequences**. The archive shows a clear pattern:

- **Overtrained:** generating apps, reading generated curricula, CRUD + auth + tenant scoping. Stop adding to these.
- **Undertrained:** everything that happens *after* code exists. That's deploying it, operating it, measuring it, finding out it's wrong,
  explaining trade-offs to someone who disagrees, and owning the consequences.

The honest risk: you can spend another year producing impressive-looking repos and still not be able to answer
"what happens if the worker dies *here*?" in an interview. The labs you now have are built to close exactly that gap, **if you do them by hand, with your own reasoning**.

## 3. The skills that matter now, and where to practise each in your archive

| Skill (from the comment) | Why a human still owns it | Where to practise (already built) |
|---|---|---|
| **Understanding the problem space** | the model optimises what you asked for, not what the business needs | folio offline M1 (what does "offline-first" *promise*?) · buildevent (what happens at a 50k-user ticket drop?) |
| **Working with stakeholders** | requirements are negotiated, not given | every ladder ticket's "explain before touching" questions; write the ticket back in your own words and list what you'd ask the PM |
| **Data model design** | the most expensive thing to change later | buildermentor (the `items` table has no owner) · aaa1 RLS lab · meterforge collation/decimal incidents · curriculum 19, 20, 22 |
| **System design and trade-offs** | there's no single right answer, only defended choices | the "Why?" drills (~35) and S-rung scenarios in every LAB; curriculum 16 (sagas vs 2PC vs outbox), 18 (durable execution) |
| **Distributed systems** | failure windows are invisible in happy-path code | relay (leases, replay, timers) · folio (CRDT convergence) · astra5 (saga crash window) · curriculum 01, 02, 03, 14, 17 |
| **Containerization, packaging, deployment** | "works on my machine" is where most AI code stops | astraspacegameweb (a CRLF checkout breaks migrations; no image tag means no rollback) · curriculum 13 · **actually deploy gitjira-app or atlas** |
| **DevOps / operations** | someone has to be paged, and someone has to decide | astraspacegameweb live Prometheus/Grafana/Tempo lab · curriculum 09 (telemetry you can trust) · 92 incident branches |
| **Access control** | "human access control" includes controlling *your agents* | netauth, HNJOBTRACK, VGdemo, aiheartbeat (agent tool allowlists) |

## 4. Lessons from running this very apprenticeship with agents

This project was itself an agentic-engineering exercise: about 50 subagents across 7 batches. It produced two real incidents worth learning from.

1. **An agent's "cleanup" destroyed real work.** `rm -rf node_modules` followed Windows workspace junctions into `packages/*` and deleted source,
   including 3 of your uncommitted files. They were recovered only because an earlier pass had recorded SHA-256 hashes and kept staged copies.
   **Lesson:** destructive commands need guardrails even for "harmless" cleanup. Keep recoverable artifacts, and never grant blanket delete.
2. **Parallel agents filled the disk and took each other down.** 8 agents doing installs, Docker pulls and worktree copies drove C: to 46 MB free.
   Every agent died, and Docker lost its VM. **Lesson:** capacity is a shared resource. Automation needs budgets (disk, CPU, cost) and a human watching the aggregate.

Both are senior-engineer interview stories, precisely *because* no individual line of code was wrong.

**Rules for working with coding agents** (from what went right and wrong here):
- **Write the spec and the "explain before touching" answers yourself, first.** An agent implements, and you decide.
- **Verify, don't trust:** build → run tests → read the whole diff → check every claim in the PR description against code (curriculum 05).
- **Adversarial review** by a second model, limited to correctness, security, data, concurrency and failure handling. Then *you* write the final explanation.
- **Least privilege for agents:** scoped tool allowlists, no recursive deletes, no pushes, and a human gate on irreversible actions.
- **Treat model output like any untrusted input,** whether it's generated tickets, docs, reviews or "fixed" code. Reviewboard's 10 already-handled stories, and the agent that self-reported a probe incorrectly and had to fix it, both show why.

## 5. Stop / start

**Stop**
- Generating new apps, clones or curriculum packs. You have 92 incidents and 22 concept pages waiting.
- Reading sealed answers before attempting. The value is in being wrong first.
- Measuring progress by repo count.

**Start**
- **Doing labs by hand**, with your own notes, timing yourself.
- **Running things for real:** fix Docker, run the meterforge SQL Server lab, and deploy one app to AWS or Azure and keep it alive for 30 days.
- **Writing:** one design doc and one postmortem per month, in your own words. This is the "communication" half of the job.
- **Shipping to other humans:** one upstream PR (Outline's kit has 3 candidates), and one app someone other than you uses (tagalog or gitjira-app).

## 6. A weekly routine (about 10–12 hours)

| Day | Session | Output |
|---|---|---|
| 1 | **Incident drill** (60–90 min, timed): pick one incident branch, diagnose from the symptom only | your root-cause note, then compare with `_answers/` |
| 2 | **Blind review** (60 min) of one repo | findings list, then `COMPARE.md`: what you missed and the pattern behind it |
| 3–4 | **One ladder ticket** end to end: explain before touching → spec → agent implements → you verify and adversarially review | a PR-sized change, plus your written explanation |
| 5 | **Design/trade-off**: one "Why?" drill or S-rung scenario, written up as a 1-page design doc | a doc you could hand a senior engineer |
| 6 | **Interview rep**: run a `MOCK_DEFENSE.md` with a model interviewer that rejects buzzwords | a scored rubric and 3 study pointers |
| monthly | **Operate something real**: the deploy, SLO or migration track on gitjira-app / atlas | a runbook entry and a postmortem |

Keep a **blind-spot log**: every time the model's review or answer catches something you missed, write one line. After a month, the patterns tell you what to study.

## 7. A 90-day plan

- **Days 1–30: verification and operations.**
  - Fix Docker.
  - Work the "what to do first" lists in `batch1report`–`batch3report`.
  - Priorities: netdrop J0 (make a broken repo boot), gitjira-app INC-003 (a deploy that dropped data), astraspacegameweb LAB0 + M1 (SLOs on a live stack).
- **Days 31–60: data and distributed systems.**
  - aaa1 RLS lab, relay J1 + INC-003, folio M1, buildevent M1 (a real Serializable → 500 bug under load).
  - Run the meterforge SQL Server lab for real.
- **Days 61–90: ship and communicate.**
  - Deploy gitjira-app (AWS) or atlas (Azure) with a rehearsed rollback.
  - Open one upstream PR to Outline.
  - Write 3 design docs and 2 postmortems.
  - Do 6 mock defenses.

By day 90 you should be able to tell, without notes, the **five interview stories** this archive now supports:
1. **Green CI, broken product** (relay / folio): how you found what the tests didn't cover.
2. **A data leak no line of code "looked" wrong for** (buildermentor shared items / aaa1 pooled tenant context).
3. **A deploy that lost data** (gitjira-app INC-003): expand/contract and rollback.
4. **A performance regression proven with numbers** (lucasrouter, buildevent, atlas query plans).
5. **Running AI agents safely** (aiheartbeat plus the `rm -rf` and disk-full incidents from this very project).

## 8. Honest caveats

- The comment is partly opinion. Reading and verifying code **still requires fluency in code**; you can't review what you can't read.
  Keep fundamentals sharp through incidents and reviews, not by building a 13th CRUD app.
- The junior market is hard, and "engineers are still needed" doesn't mean every junior gets hired. The differentiator is **evidence of judgement**:
  things you ran, broke, measured, fixed and explained, which is exactly what this apprenticeship is built to produce.
- Everything here is only worth what you *do* with it. The material is finished. The work is yours.
