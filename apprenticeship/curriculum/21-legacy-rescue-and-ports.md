# 21 — Legacy rescue and ports: "rewrote the shape, dropped the invariant"

**Situation A: untested legacy (often AI-generated) code you must change.**
1. **Check what's real first:** does it build and boot? Which features are wired vs just schema or docs ([05](05-verify-before-trust.md))?
2. **Pin the current behaviour** with characterization tests around the flow you'll touch ([04](04-characterization-tests.md)), against a throwaway DB.
3. **Triage dead weight:** unused tables and models, unconsumed queues, dead dependencies. Record a decision for each (delete, wire, or leave with a note) instead of refactoring blindly.
4. **Fix in PR-sized steps**, each with a failing test first, never "modernize everything".

**Situation B: a port or rewrite to another stack** (TS→.NET, Python→TS, Grok starter→hardened rewrite).
- The old stack gave you things **for free** that the port must re-implement explicitly: auth middleware, validation (Zod/Pydantic), role guards, transactions, error mapping (403/404 vs 400), serialization casing, rounding.
- **Port-parity testing:** run one behavioural contract against *both* implementations and classify each difference as intended, bug in the old, or bug in the new.
- Diffs lie when files are untracked: `git diff` doesn't show new auth or migration files.

**Worked examples in your repos**
- **VGdemo:**
  - `training/review/` parity drill with `contract.mjs` (20 checks): TS 17/20 vs .NET 13/20.
  - The port's token is just the user id, and a client admin can approve their own payroll (200 vs 403).
  - Incidents: a LOCKED payroll reopened, and a new hire missing from the run.
- **grokbuildmultitenantproject:** a legacy-diff drill, Grok starter (HEAD) vs the hardened uncommitted rewrite.
- **vg:** characterize the payroll calculate→approve→process flow; dead-schema triage (about half the Prisma schema has no code); plan for the `fable/02` punch list.
- **HNJOBTRACK:** INC-003, snake_case→camelCase model drift wipes exclusions after a backend-only deploy (an API-contract break across the stack boundary).
- **reviewboard:** 10 of 25 generated security stories were already handled. Verify the ticket before you build it.
