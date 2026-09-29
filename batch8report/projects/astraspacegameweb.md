# astraspacegameweb: B08 learn pass

**Path:** `C:\Users\Owner\Desktop\astraspacegameweb` · **Tier:** LAB (operate a live observability stack)
**Branch:** `main` (same branch as B03's training commit `2fca582`) · **Commit:** `2f18042` `docs(training): add learn/ study guide + junior on-ramp (B08)`
(pathspec `learn training`, 7 new files, 682 lines. The working tree was clean before and after. Not pushed.)

## Files added
- `learn/README.md`: study guide. It covers what the app is, 6 prerequisites linked to curriculum 09/10/08/13/07/14/05 plus exact code lines, and a
  12-session route (~14 h) with exit criteria. It has a do-vs-delegate table per session, a done definition, and next repos.
- `learn/00-onramp.md` + `learn/_answers/00-onramp.md`: 10 warm-ups, all grounded in real code:
  - role loops in `index.ts`
  - the outbox→Redis→WS→`queryRefresh.ts` trace
  - the WS registry closure
  - histogram-quantile math on `metrics.ts:19`
  - why `warband_lock_retries_total` never moves (`transaction(fn, 1)` + swallowed `WB_BUSY`)
  - the migration checksum and CRLF
  - `/api/health` callers
  - the Redis fallback in `redis.ts`
  - the `scheduled_events`/`events_due` schema
  - a characterization test for `committedResolutions`
- `learn/01-agentic-practice.md` + `learn/_answers/01-agentic-practice.md`: 5 drills and a 20-item verification checklist naming real files (boundaries probe,
  migrations immutability, `le` normalization, bounded labels, the auth skip list at `transport/app.ts:79`, the JWT fallback at `:47`, `artifacts/`).
  - The drills: M1 SLOs via the existing WORKFLOW, INC-003 fix, INC-005 health split, INC-002 bucket-vs-threshold guard, INC-004 migration-immutability CI + `.gitattributes`.
  - The rubrics list typical agent mistakes. One example: normalizing the checksum without a transition crash-loops CRLF-migrated databases.

## Gap filled (under training/)
- `training/ops/NO-DOCKER-ROUTE.md` + sealed `training/_answers/no-docker-route.md`.
- **Gap:** every exercise in the B03 lab assumes a running Docker stack, and Lab 0 §6's fallback only covers questions 1–6. Docker is currently broken here (the WSL distro is gone).
- **What it adds:** a no-Docker substitute for every incident, using `git`, plain `node` and the recorded evidence JSONL.
  - Part A: Lab 0 from the evidence file.
  - Part B: INC-002 quantile by hand plus a promtool test written but not run.
  - Part C: a 25-line INC-003 simulation. It also shows that fixing only the handler still leaves the branch's tabs flapping.
  - Part D: INC-004 via `git ls-files --eol` and sha256 LF vs CRLF.
  - Part E: INC-005 caller table.
  - Part F: an INC-001 Monte Carlo of window overlap (about 0.6 on main vs 1.0 on the branch).

## Skipped / UNVERIFIED
- Docs-only pass: nothing installed, built or run. **Docker down:** every live step is marked "requires Docker, currently down" and has a substitute.
  **`node_modules` absent:** `pnpm install --frozen-lockfile` is needed before on-ramp #10 and every drill.
- The reference test (on-ramp #10), the promtool YAML (B2) and the node scripts (C, F) were not executed, so they're marked UNVERIFIED in the sealed files.
  The Monte Carlo figure comes from an analytic estimate.
- Checked on 2026-09-26: the migrations show `i/lf w/lf`, `core.autocrlf=true`, and there's no `.gitattributes`. That matches B03's CRLF finding.
- I did not add a pointer row to `training/README.md`, to leave B03 content untouched. `learn/README.md` links to the new file instead.

## Study route in 3 lines
1. Read the map and the numbers first: architecture/first-change pages plus 10 on-ramp exercises (histogram clipping, swallowed contention, checksum, health, Redis fallback).
2. Operate, then diagnose: Lab 0 (fallback while Docker is down), then INC-002 → 003 → 004/005 → blind review → INC-001, each with a no-Docker substitute.
3. Direct and verify agents: M1 SLOs plus 4 incident drills against a codebase-specific checklist, then the interview kit. Next: buildevent (load, curriculum 14), then gitjira-app (real cloud deploy).
