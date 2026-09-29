# Batch 13 — Numbered Experiments (triage)
Scope: `C:\Users\Owner\Desktop\_Organized Desktop\05 Numbered Experiments\` (all 86 top-level folders: B1, D1-D3, e1-e20, f1, g1, J1, j2-j7, rn1, w21-w25, ww1-ww55, X1, z1-z9, zz1-zz9)  |  Candidate dirs inspected: 86  |  Meaningful projects (full record below): 8 (incl. 1 cluster record standing for ~65 folders)  |  Tiny/empty/boilerplate: 2 empty (f1, j6) + ~78 template-pattern folders covered by the cluster record

## Headline finding

**This entire batch is a single machine-generated corpus, not 86 separate portfolio projects.** 83 of the 86 folders contain an `astraupskill/` subfolder — the same "Astra" teaching-pack pattern already reviewed once in `fablereview-astra-audit.md` (153 projects, 2026-09-16/18). This looks like a **new, later wave** of the same pipeline: almost every folder's mtime is 2026-09-17 through 2026-09-23 (this week), none are git repos (`git log` empty everywhere), and the `astraupskill/` packs follow the identical 7-chapter template (`01-CODEBASE-MAP` → `02-CONCEPTS` → `03-WORKED-CHANGE` → `04-TESTING-AND-DEBUGGING` → `05-PRACTICE` → `06-SOLUTIONS-AND-REVIEW`, sometimes `+07-TRACE-LAB`), plus an `astraupskill/evidence/*-astra-runtime.log` proving a runtime lab was executed. Each folder = one synthetic mid-size Next.js/Prisma (or Java/Python) app built specifically to host **one narrow, named CRUD-safety lesson** (a transaction gap, a TOCTOU race, an idempotency miss, a soft-delete leak, an authorization boundary, etc.). Business domain (CRM, HR, ticketing, marketplace, scheduling...) is randomized per folder purely as lesson flavor — the underlying lesson skeleton repeats.

Given that, per the brief's clustering instruction, I am **not** writing 65+ near-identical full records. Below: one quick-table row per folder (all 86), one consolidated cluster record for the repetitive Astra single-lesson apps, and full records only for the folders that structurally diverge from the template (real open-source substrate, multi-app bundles, career-prep packs, or data-hygiene anomalies).

## Quick table (all 86 candidates)

| Project | Path | Type | Origin | Stack | Complexity | Docs | Disp |
|---|---|---|---|---|---|---|---|
| B1 | B1/ | web app (+ scripts +career pack) | COURSE/GENERATED | Next.js/TS, in-process store | Mid | STRONG (astraupskill + dfableandopus career pack) | G ARCHIVE (see full record) |
| D1 | D1/ | web app | COURSE/GENERATED | Next.js, Socket.IO, Drizzle | Mid | USEFUL | G ARCHIVE |
| D2 | D2/ | web app | COURSE/GENERATED | Next.js, Drizzle | Junior+ | USEFUL | G ARCHIVE |
| D3 | D3/ | web app | COURSE/GENERATED | Next.js, service layer | Mid | USEFUL | G ARCHIVE |
| e1 | e1/ | web app | COURSE/GENERATED | Next.js, Prisma, Docker | Mid | USEFUL | G ARCHIVE |
| e11 | e11/ | web app | COURSE/GENERATED | Express + Vite SPA, JSON store | Junior+ | USEFUL | G ARCHIVE |
| e12 | e12/ | web app (+ SDK +career pack) | COURSE/GENERATED | Node service, SDK, verification/ | Mid | STRONG | G ARCHIVE (see full record) |
| e13 | e13/ | web app (+career pack) | COURSE/GENERATED | Next.js, Prisma, commerce domain | Mid | STRONG | G ARCHIVE — **representative example, see full record** |
| e14 | e14/ | web app / CLI (+career pack) | COURSE/GENERATED | Python, pyproject, observability | Mid | STRONG | G ARCHIVE |
| e15 | e15/ | web app (+career pack) | COURSE/GENERATED | Python, help-desk domain | Mid | STRONG | G ARCHIVE |
| e17 | e17/ | web app | COURSE/GENERATED | Next.js, Prisma, forum domain | Junior+ | USEFUL | G ARCHIVE |
| e2 | e2/ | web app | COURSE/GENERATED | Next.js, in-process CMS store | Mid | USEFUL | G ARCHIVE |
| e20 | e20/ | web app (+career pack) | COURSE/GENERATED | Next.js, ERP domain | Mid | STRONG | G ARCHIVE |
| e3 | e3/ | web app | COURSE/GENERATED | Next.js, privacy-deletion domain | Mid | USEFUL | G ARCHIVE |
| e4 | e4/ | web app (+ extra temp-app) | COURSE/GENERATED | Next.js, Prisma, newsletters | Junior+ | USEFUL | G ARCHIVE |
| e6 | e6/ | monorepo(3 apps) | COURSE/GENERATED | Fastify API + Next web + worker, Turborepo-style pkgs | Mid+ | USEFUL | G ARCHIVE |
| f1 | f1/ | empty | — | — | Tiny | NONE | G ARCHIVE (empty, delete candidate) |
| g1 | g1/ | web app (+ original build prompt) | ORIGINAL prompt / COURSE wrapper | Next.js, Drizzle, Vercel | Mid | USEFUL | G ARCHIVE (see full record — paired w/ X1) |
| J1 | J1/ | CLI | COURSE/GENERATED | Java, terminal task manager | Junior | USEFUL | G ARCHIVE (see Java cluster note) |
| j2 | j2/ | CLI | COURSE/GENERATED | Java, library/book tracker | Junior | USEFUL | G ARCHIVE |
| j3 | j3/ | CLI | COURSE/GENERATED | Java, bank simulator | Junior | USEFUL | G ARCHIVE |
| j4 | j4/ | CLI (+career pack) | COURSE/GENERATED | Java, question bank | Junior | USEFUL | G ARCHIVE |
| j5 | j5/ | CLI (+career pack) | COURSE/GENERATED | Java, expense tracker | Junior | USEFUL | G ARCHIVE |
| j6 | j6/ | empty | — | — | Tiny | NONE | G ARCHIVE (empty, delete candidate) |
| j7 | j7/ | CLI (+career pack) | COURSE/GENERATED | Java, order management | Junior+ | USEFUL | G ARCHIVE |
| rn1 | rn1/ | mobile app (React Native, real fork) | OPEN-SOURCE CLONE + course wrapper | RN/Expo, Bluesky `social-app` source, multi-package | Senior-oriented (host codebase) | USEFUL (single lesson on a huge real codebase) | **B HIGH-VALUE — see full record** |
| w21 | w21/ | web app | COURSE/GENERATED | Next.js, Prisma | Mid | USEFUL | G ARCHIVE |
| w22 | w22/ | web app | COURSE/GENERATED | Next.js, Prisma, refunds | Mid | USEFUL | G ARCHIVE |
| w23 | w23/ | web app | COURSE/GENERATED | Next.js, Prisma, ticketing | Mid | USEFUL | G ARCHIVE |
| w24 | w24/ | web app (+career pack) | COURSE/GENERATED | Next.js, Prisma, feature flags | Mid | STRONG | G ARCHIVE |
| w25 | w25/ | web app (+career pack) | COURSE/GENERATED | Next.js, Prisma, lock state machine | Mid | STRONG | G ARCHIVE |
| ww1 | ww1/ | web app | COURSE/GENERATED | Next.js, Prisma, review-cycle | Mid | USEFUL | G ARCHIVE |
| ww10 | ww10/ | web app (+career pack) | COURSE/GENERATED | Next.js, Prisma, lending workflow | Mid | STRONG | G ARCHIVE |
| ww11 | ww11/ | web app | COURSE/GENERATED | Next.js, Prisma, protocol versioning | Mid | USEFUL | G ARCHIVE |
| ww12 | ww12/ | web app | COURSE/GENERATED | Next.js, Prisma, conversations | Mid | USEFUL | G ARCHIVE |
| ww13 | ww13/ | web app | COURSE/GENERATED | Next.js, Prisma, grants reporting | Mid | USEFUL | G ARCHIVE |
| ww14 | ww14/ | web app (+career pack) | COURSE/GENERATED | Next.js, Prisma, LMS/compliance | Mid | STRONG | G ARCHIVE |
| ww15 | ww15/ | web app | COURSE/GENERATED | Next.js, Prisma, marketplace offers | Mid | USEFUL | G ARCHIVE |
| ww16 | ww16/ | web app | COURSE/GENERATED | Next.js, Prisma, deal registration | Mid | USEFUL | G ARCHIVE |
| ww17 | ww17/ | web app (+career pack) | COURSE/GENERATED | Next.js, Prisma, "SignalDesk" | Mid | STRONG | G ARCHIVE |
| ww18 | ww18/ | web app | COURSE/GENERATED | Next.js, Prisma, quoting engine | Mid | USEFUL | G ARCHIVE |
| ww19 | ww19/ | web app | COURSE/GENERATED | Next.js, Prisma, workflow runs, pnpm | Mid | USEFUL | G ARCHIVE |
| ww26 | ww26/ | web app | COURSE/GENERATED | Next.js, Prisma, distributed lock | Mid | USEFUL | G ARCHIVE |
| ww27 | ww27/ | web app | COURSE/GENERATED | Next.js, Prisma, API versioning | Mid | USEFUL | G ARCHIVE |
| ww28 | ww28/ | web app | COURSE/GENERATED | Next.js, Prisma, multipart uploads | Mid | USEFUL | G ARCHIVE |
| ww29 | ww29/ | web app | COURSE/GENERATED | Next.js, Prisma, notifications | Mid | USEFUL | G ARCHIVE |
| ww3 | ww3/ | web app | COURSE/GENERATED | Next.js, Prisma, compliance rules | Mid | USEFUL | G ARCHIVE |
| ww30 | ww30/ | web app | COURSE/GENERATED | Next.js, Prisma, query cache | Mid | USEFUL | G ARCHIVE |
| ww31 | ww31/ | web app | COURSE/GENERATED | Next.js, Prisma, in-memory cache/flags | Mid | USEFUL | G ARCHIVE |
| ww32 | ww32/ | web app | COURSE/GENERATED | Next.js, Prisma, chat/messaging | Mid | USEFUL | G ARCHIVE |
| ww34 | ww34/ | web app (+career pack style docs) | COURSE/GENERATED | Next.js, Prisma, "Staybound" booking | Mid | USEFUL | G ARCHIVE |
| ww35 | ww35/ | web app | COURSE/GENERATED | Next.js, Prisma/Postgres, appointment calendar | Mid | USEFUL | G ARCHIVE |
| ww36 | ww36/ | web app | COURSE/GENERATED | Next.js, Prisma, reservations | Mid | USEFUL | G ARCHIVE |
| ww37 | ww37/ | web app | COURSE/GENERATED | Next.js, in-memory repo, inventory | Junior+ | USEFUL | G ARCHIVE |
| ww39 | ww39/ | web app | COURSE/GENERATED | Next.js, Prisma, support desk | Mid | USEFUL | G ARCHIVE |
| ww4 | ww4/ | web app | COURSE/GENERATED | Next.js, Prisma, issue tracker | Mid | USEFUL | G ARCHIVE |
| ww40 | ww40/ | web app | COURSE/GENERATED | Next.js, Prisma, job board | Mid | USEFUL | G ARCHIVE |
| ww43 | ww43/ | web app | COURSE/GENERATED | Next.js, Prisma, collaborative notes | Mid | USEFUL | G ARCHIVE |
| ww45 | ww45/ | web app (extra docs2/docs3) | COURSE/GENERATED | Next.js, Prisma, knowledge base | Mid | STRONG (3 doc packs) | G ARCHIVE |
| ww46 | ww46/ | web app | COURSE/GENERATED | Next.js, Prisma, project status | Mid | USEFUL | G ARCHIVE |
| ww47 | ww47/ | web app | COURSE/GENERATED | Next.js, Prisma, job queue/aggregation | Mid | USEFUL | G ARCHIVE |
| ww48 | ww48/ | web app | COURSE/GENERATED | Next.js, Prisma, follow-ups/CRM | Mid | USEFUL | G ARCHIVE |
| ww49 | ww49/ | web app (extra docs2) | COURSE/GENERATED | Next.js, Prisma, marketplace commerce | Mid | USEFUL | G ARCHIVE |
| ww5 | ww5/ | web app (+career pack) | COURSE/GENERATED | Next.js, Prisma, People Ops/comp approval | Mid | STRONG | G ARCHIVE |
| ww50 | ww50/ | web app | COURSE/GENERATED | Next.js, Prisma, API-key management | Mid | USEFUL | G ARCHIVE |
| ww55 | ww55/ | web app | COURSE/GENERATED | Next.js, Prisma, job-board moderation | Mid | USEFUL | G ARCHIVE |
| ww6 | ww6/ | web app | COURSE/GENERATED | Next.js, Prisma, allocation runs | Mid | USEFUL | G ARCHIVE |
| ww7 | ww7/ | web app | COURSE/GENERATED | Next.js, Prisma, workflow status | Mid | USEFUL | G ARCHIVE |
| ww8 | ww8/ | web app | COURSE/GENERATED | Next.js, Prisma, document extraction jobs | Mid | USEFUL | G ARCHIVE |
| ww9 | ww9/ | web app (+career pack style) | COURSE/GENERATED | Next.js, Prisma, scheduler/waitlist | Mid | USEFUL | G ARCHIVE |
| X1 | X1/ | web app (bespoke, bagel domain) | ORIGINAL app + course wrapper | Next.js, "bagel-intel-platform" | Mid | USEFUL | C SPECIALIZED (see full record — paired w/ g1) |
| z1 | z1/ | web app (+ ADR/learning pack) | COURSE/GENERATED + ORIGINAL-style ADRs | Next.js, appointment scheduling, uploads | Mid | STRONG (real ADR-style architecture/learning docs) | **C SPECIALIZED — see full record** |
| z3 | z3/ | 2 web apps + study path | COURSE/GENERATED (older wave, Apr 2026) | Next.js, Node SQLite, 2 distinct domains | Mid | USEFUL x2 | **C SPECIALIZED — see full record** |
| z6 | z6/ | web app | COURSE/GENERATED | Next.js, Prisma, team wiki | Mid | USEFUL | G ARCHIVE |
| z7 | z7/ | web app (read-only) | COURSE/GENERATED | Next.js 16, seeded dataset, no DB | Junior+ | USEFUL | G ARCHIVE |
| z8 | z8/ | web app | COURSE/GENERATED | Next.js, Prisma, Docker, event registration | Mid | USEFUL | G ARCHIVE |
| z9 | z9/ | web app (+career pack style) | COURSE/GENERATED | Next.js, Prisma, freelancer portal, sessions | Mid | USEFUL | G ARCHIVE |
| zz1 | zz1/ | web app | COURSE/GENERATED | Next.js, Prisma, CRM deals | Mid | USEFUL | G ARCHIVE |
| zz2 | zz2/ | web app | COURSE/GENERATED | Next.js, Prisma, ticket IDs | Mid | USEFUL | G ARCHIVE |
| zz3 | zz3/ | web app | COURSE/GENERATED | Next.js, Prisma, support hub, Zod | Mid | USEFUL | G ARCHIVE |
| zz4 | zz4/ | web app (**nested duplicate**) | COURSE/GENERATED | Next.js, Prisma, approval queue | Mid | USEFUL | G ARCHIVE — flag duplicate nesting |
| zz55 | zz55/ | web app | COURSE/GENERATED | Next.js, Prisma, onboarding tasks | Mid | USEFUL | G ARCHIVE |
| zz6 | zz6/ | web app | COURSE/GENERATED | Next.js, in-memory + unused Prisma schema | Mid | USEFUL | G ARCHIVE |
| zz7 | zz7/ | web app | COURSE/GENERATED | Next.js, Prisma, purchase orders | Mid | USEFUL | G ARCHIVE |
| zz8 | zz8/ | web app | COURSE/GENERATED | Next.js, Prisma, HR self-review/integration jobs | Mid | USEFUL | G ARCHIVE |
| zz9 | zz9/ | web app | COURSE/GENERATED | Next.js, Prisma, case management | Mid | USEFUL | G ARCHIVE |

## Cluster record: "Astra single-lesson Next.js/Prisma workshop" (~65 folders)

Represents: D1, D2, D3, e1, e2, e3, e4, e17, w21, w22, w23, w24, w25, ww1, ww3, ww4, ww6, ww7, ww8, ww9, ww10-ww19, ww26-ww32, ww34-ww37, ww39, ww40, ww43, ww45-ww50, ww55, z1(app portion), z6, z7, z8, z9, zz1-zz9 (minus the anomalies called out separately). e12/e13/e14/e15/e20/B1/g1/j4/j5/j7/ww5 follow the identical lesson skeleton but additionally carry a `dfableandopus/` career-prep pack (see Batch observations) — same disposition.

- Path: many (see list above), each its own top-level folder
- Origin: COURSE/GENERATED — an LLM pipeline ("Astra") builds a synthetic mid-size CRUD app (Next.js App Router + Prisma/Drizzle/SQLite, occasionally Fastify/Express or Python), plants or finds one bounded correctness issue, then documents the fix as a course
- Type: web app, single-service, each ~65–170 files (excl. node_modules)
- State: working-looking — each ships `tests/` or a runtime lab (`*-astra-runtime.log` under `astraupskill/evidence/`) that appears to have actually executed against the real service code, not invented output
- Purpose: teach ONE CRUD-correctness concept per folder (concurrency/TOCTOU, transactional boundaries, idempotency keys, soft-delete/visibility leaks, authorization scoping, cache TTL edge cases, audit-trail completeness, pagination stability, API versioning/backcompat) using a plausible SaaS-shaped domain (support desk, CRM, HR, marketplace, scheduling, compliance, LMS, job board, ticketing, knowledge base, etc.)
- Stack: FE Next.js/React/Tailwind, BE Next.js route handlers/server actions, DB Prisma+SQLite/Postgres or Drizzle, test Vitest, no CI/deploy config, no auth beyond a simulated session/role
- Architecture: modular monolith, service→repository layering is the recurring teaching motif (route → service → repository → Prisma → audit log)
- Complexity: Junior+ to Mid — the app scaffolding itself is boilerplate-simple; the *lesson* (e.g. compare-and-set updates, updateMany row-count checks, transaction placement) is a legitimate mid-level concept, well-chosen and consistently well-explained
- Educational material: STRONG and structurally identical everywhere — `astraupskill/README.md` + numbered chapters (codebase map, concepts, worked change, testing/debugging, practice, solutions, sometimes a trace lab) + an `evidence/` runtime log. High quality per-instance, but **entirely repetitive across the cluster** — same template, same voice, same "no production behavior changed" framing seen 60+ times
- Quality observations: Zod/schema validation present in most (e.g. zz3), transactional writes correctly scoped in the ones addressing races (ww16, ww22, zz1), several instances explicitly say "no defect found, added a fault-injection lab instead" (ww23, ww26) — i.e. not every "fix" is a real bug, some are process/coverage exercises dressed as fixes
- Old-AI-generated smells: extremely uniform README phrasing ("This course follows...", "The staged improvement...", "Production source is unchanged") across dozens of unrelated domains — a clear tell of templated generation; several folders keep `.tsbuildinfo`/`.log`/`dev-server.log` artifacts checked into the folder (should be gitignored, isn't since there's no git); zz4 has an actual bug in the generation/extraction step (see anomaly below)
- Skill tags: db-transactions, db-concurrency, db-migrations, orm, authz-rbac, be-validation, be-error-handling, test-unit, design-docs-adrs, crud-basic
- Duplicate/overlap: **massive internal overlap** — this is the core finding; see Batch observations
- Learning value: Medium — good if the goal is "read one worked CRUD-safety lesson"; near-zero incremental value to read a second, tenth, or fortieth one
- Proposed disposition: **G ARCHIVE** (as individual portfolio pieces) — keep a small curated sample (3-5 covering distinct concept categories: a transaction lesson, an idempotency lesson, a concurrency/CAS lesson, an authz-scoping lesson) for reference/interview-story mining; archive or delete the rest as redundant. This is teaching-content inventory, not shippable/demoable product work.

## X1 — "bagel-intel-platform" (Astra lesson) and g1 — "Bagel Atlas" build prompt

- Path: X1/bagel-intel-platform/ and g1/ (top-level app)
- Origin: g1 is an ORIGINAL app built from an explicit hand-authored spec (`g1/BAGEL_ATLAS_CODEX_PROMPT.md`: "Build a production-ready MVP of The Bagel Atlas, a critic-first bagel discovery site... Seed cities → trigger AI research → ingest draft shops/source mentions → review/edit/publish in admin panel → render on public site"); X1 wraps a differently-scaffolded "bagel-intel-platform" app in the same Astra lesson pattern (review-moderation CRUD fix in `data.ts`/`actions.ts`)
- Type: web app (admin + public site), monorepo-ish single Next.js app in both
- State: working-looking in both; g1 additionally ships `.next-dev*.log` files (was actually run locally)
- Purpose: an AI-research-assisted local business directory/review platform — same product idea attempted twice with different scaffolds (g1 = full original build prompt with a real feature spec; X1 = same-named domain used purely as an Astra lesson host)
- Stack: g1: Next.js, Drizzle, `vercel.json`, `local-data/`, `db/` — looks like a real attempt at the MVP described in the prompt. X1: Next.js/Prisma (per generic template), `bagel-intel-platform/astraupskill/` for the lesson
- Complexity: Mid (both) — g1's prompt describes a genuinely interesting workflow (AI research ingestion → human review/publish gate) worth checking whether it was actually implemented end-to-end (NEEDS DEEPER INSPECTION — the survey only sampled top-level files)
- Educational material: g1 has a hand-authored product spec, not a generated course — different in kind from the rest of the batch
- Duplicate/overlap: X1 and g1 share the "Bagel Atlas / bagel intel" concept but are NOT the same codebase; worth a follow-up diff to see which (if either) actually finished the admin research→publish workflow
- Learning value: Medium-High for g1 if the ingestion/review/publish pipeline is real (AI-assisted content pipeline + human-in-the-loop moderation is a good interview story); Low for X1 (same Astra template as the rest of the batch)
- Proposed disposition: g1 = **C SPECIALIZED** (verify build completeness before deciding; if the AI-research→publish pipeline works end-to-end, this is a legitimately interesting portfolio piece, not just a lesson host); X1 = **G ARCHIVE** (same as the main cluster)

## z1 — appointment-scheduling-platform (architecture/learning docs, not just an Astra pack)

- Path: z1/ (app at top-level `src/`), plus `z1/appointment-scheduling-platform/docs/` (docs-only companion folder)
- Origin: COURSE/GENERATED app + what reads as a genuinely separate, real-feeling documentation exercise layered on top
- Type: web app + docs-only companion
- State: working-looking (tests/ present, real domain/services/auth structure per README: `types.ts` → `store.ts` → `workflow-service.ts` → `policy.ts` → `request-service.ts`, plus `admin-service.ts` and a test harness)
- Purpose: request-approval workflow app (bookings/appointments with an admin approval path)
- Stack: Next.js, TS, file-based store, `uploads/`
- Educational material: STRONG and **structurally different** from the rest of the batch — `appointment-scheduling-platform/docs/architecture/` holds numbered ADR-style docs (`01-major-decisions-log.md`, `02-options-considered.md`, `03-domain-model-notes.md`, `04-scheduling-engine-notes.md`, `05-auth-and-permissions-notes.md`, `06-auth-decision-justification.md`) plus `docs/learning/build-journal.md`, `file-reading-order.md`, `pr-slices.md` — this is a genuine "decisions and why" trail, not the templated Astra chapter set (z1 also has its own `astraupskill/` on top)
- Quality observations: ADR-style justification docs (options considered, decision log) are rare in this batch and valuable for interview prep ("walk me through a design decision and the alternatives you rejected")
- Skill tags: design-docs-adrs, authz-rbac, be-validation, arch-modular-monolith
- Learning value: High — the ADR pack is exactly the kind of artifact that supports a strong "how do you make architectural decisions" interview story, distinct from every other folder in this batch
- Interview stories: "here's a scheduling engine decision I documented and justified, including the options I rejected and why"
- Proposed disposition: **C SPECIALIZED** — pull the `docs/architecture/` and `docs/learning/` pack out as a standalone ADR-writing sample; archive the app/Astra-lesson portion with the rest of the cluster

## z3 — two bundled apps + a cross-app study path (older wave, Apr 2026)

- Path: z3/customer-feedback-board/, z3/founder-crm-lite/, plus z3/CODEBASE-STUDY-PATH.md and z3/README.md at the parent level
- Origin: COURSE/GENERATED, but visibly an **earlier generation wave** than the rest of the batch (folder mtime Apr 1 2026 vs. the Sep 17-23 2026 wave everywhere else) — worth checking whether this is the seed/prototype the later single-app-per-folder pattern was derived from
- Type: 2 independent web apps sharing one parent folder, each with its own `astraupskill/`
- State: working-looking; `customer-feedback-board` explicitly documents Node's built-in SQLite module usage ("Node 22.16+... experimental-feature warning")
- Purpose: customer-feedback-board = public ideas/discussion/moderation board; founder-crm-lite = lightweight founder-facing CRM (not separately inspected in depth — NEEDS DEEPER INSPECTION for founder-crm-lite specifics)
- Stack: Next.js, node:sqlite (customer-feedback-board)
- Educational material: USEFUL — `CODEBASE-STUDY-PATH.md` at the parent level suggests a deliberate cross-app reading sequence, unlike the single-app folders elsewhere in the batch
- Duplicate/overlap: template pattern shared with the main cluster, but the **two-app-per-folder + parent study path** structure is unique to z3 in this batch
- Learning value: Medium — mainly interesting as evidence of an earlier iteration of the Astra pipeline's folder-bundling approach
- Proposed disposition: **C SPECIALIZED** (keep as a structural reference for "how did this pipeline evolve"), otherwise same as main cluster

## rn1 — Astra lesson on a real Bluesky `social-app` fork

- Path: rn1/social-app/ (2,710 files excl. node_modules — by far the largest folder in this batch), rn1/astraupskill/
- Origin: **OPEN-SOURCE CLONE** — this is an actual checkout/fork of Bluesky's `social-app` (multiple real sub-packages: `bskyembed`, `bskylink`, `bskyogcard`, `dev-env`, main app), not a synthetic Astra scaffold. The Astra lesson is layered on top of it.
- Type: mobile/web social app (React Native + Expo, multi-package monorepo)
- State: this is production open-source code, not course scaffolding — working by construction
- Purpose: the lesson (`astraupskill/`) follows a real block/unblock cache-invalidation bug: "a successful create response could be followed by a detail lookup that found nothing... successful blocking invalidated [a] query but successful unblocking only reset profile feeds. The deleted account could therefore remain visible" — a genuine stale-read-model bug pattern (cache invalidation asymmetry) demonstrated against real, large-scale application code rather than a toy app
- Stack: React Native, Expo, real Bluesky AT-Protocol client stack
- Architecture: real production monorepo, multiple sub-packages, actual query-cache layer (likely React Query given the "invalidate its query" language)
- Complexity: Senior-oriented for the host codebase itself (even though the lesson slice is narrow) — reading real, large, unfamiliar code to locate one cache-invalidation asymmetry is a materially harder and more realistic skill than the synthetic-app lessons elsewhere in this batch
- Educational material: USEFUL, single lesson, but the *substrate* (a real, large open-source app) is what makes this valuable — it's the only folder in the batch offering practice at navigating an unfamiliar large codebase rather than a purpose-built teaching scaffold
- Skill tags: legacy-codebase-reading, caching, realtime-ws (AT-Proto), fe-state, mobile-rn
- Duplicate/overlap: none — structurally unique in this batch
- Learning value: Very High — "diagnose a stale-cache bug in a real, unfamiliar, large open-source mobile codebase" is a much stronger interview story than any of the synthetic-app lessons, precisely because the codebase is real and large
- Interview stories: "found/explained a cache-invalidation asymmetry (block vs. unblock) in a real large-scale social app's query layer, traced it from the mutation through to the stale UI read"
- Proposed disposition: **B HIGH-VALUE** — worth keeping and possibly writing up as a standalone case study; distinct from (and better than) the rest of the batch precisely because the host app isn't disposable

## B1 — incident-response-platform + career-prep pack

- Path: B1/ (app at top-level `src/`, plus `incident-response-platform/` — check whether this is a duplicate nested copy like zz4, NEEDS DEEPER INSPECTION), B1/dfableandopus/, B1/checks/
- Origin: COURSE/GENERATED
- Type: web app + standalone regression-check scripts (`checks/incident-detail-regression.mjs`, `checks/incident-list-pagination.mjs`) + career-prep pack
- Purpose: incident-response app; the lesson is an authorization-leak fix (`canViewIncident` reuse so a viewer can't see a confidential parent/child incident via the detail endpoint even if they could not request it directly)
- Educational material: STRONG — in addition to the standard `astraupskill/` chapters, B1 has `dfableandopus/` with `01-INTERVIEW-QUESTIONS.md`, `02-STORIES-AND-RESUME.md`, `03-CODE-READING-DRILL.md`, `04-TAKE-HOME.md`, `05-SYSTEM-DESIGN-FOLLOWUPS.md`, `06-FLASHCARDS.md` — a direct interview-prep pack built from this specific project (also present in e12, e13, e14, e15, e20, j4, j5, j7, ww5 — 10 folders total)
- Note: `B1/JSLEARNBE/` exists but is empty — dead/leftover folder
- Skill tags: authz-rbac, security-owasp, design-docs-adrs
- Duplicate/overlap: same Astra lesson skeleton as the main cluster; distinguished by the career-prep pack
- Learning value: Medium — the interview-prep pack format (flashcards, take-home, system-design follow-ups tied to a specific codebase) is a reusable pattern worth preserving even if the underlying app is archived
- Proposed disposition: **G ARCHIVE** for the app; consider extracting the `dfableandopus/` career-prep pack format as a template if it's judged higher quality than generic interview prep material (NEEDS DEEPER INSPECTION — only sampled directory listing, not pack content quality)

## Anomaly: zz4 has a nested duplicate folder

`zz4/zz4/` exists and contains its own `astraupskill/`, `prisma/`, `public/`, `src/`, `tests/` — i.e., the project appears to have been extracted/copied into itself one level deep by mistake. `zz4/astraupskill/evidence/crud-b07-astra-runtime.log` exists at both levels. This is a data-hygiene issue worth flagging for cleanup (verify which copy — if either — is canonical before archiving) rather than a meaningful project distinction.

## Batch observations

- **This batch is not 86 projects — it is one generation run (a later wave of the "Astra CRUD upskill" pipeline) producing ~78 near-identical single-lesson Next.js/Prisma (occasionally Java/Python/Express) teaching apps**, each wrapping a different SaaS-flavored domain around the same lesson skeleton (`astraupskill/` chapters 1-7 + a runtime evidence log). This matches the pattern already reviewed once at scale in `fablereview-astra-audit.md`; recommend treating this folder the same way — sample a handful for the portfolio, archive/delete the rest rather than cataloguing each individually.
- **Repeated CRUD-lesson topics observed across the cluster** (rough tally from README headlines): transactional/race-safety fixes (ww16, w22, zz1, z8, ww8, ww6, ww7) ~9-10; idempotency/duplicate-write guards (ww19, e4, ww29, ww7) ~5; authorization/visibility-scoping boundaries (B1, e2, e3, w21, z9, zz55, X1) ~7; audit/history integrity (D2, D3, ww14, ww49) ~4; cache/TTL edge cases (ww30, ww31); the remainder are single-instance topics (pagination, uploads bounds, API versioning, ID collision, etc.) — good topical diversity even though the wrapper is identical.
- **10 folders carry an extra `dfableandopus/` career-prep pack** (interview questions, stories/resume material, code-reading drills, take-homes, system-design follow-ups, flashcards) layered on top of the standard Astra course: B1, e12, e13, e14, e15, e20, j4, j5, j7, ww5. Worth reviewing as a distinct, potentially reusable "turn a project into interview prep" template, separate from the CRUD-lesson content itself.
- **6-folder Java CLI sub-cluster** (J1, j2, j3, j4, j5, j7 — j6 is empty) applies the exact same Astra teaching pattern to small framework-free Java programs (task manager, library tracker, bank simulator, question bank, expense tracker, order management), explicitly positioned as "learn CRUD reliability before you add a web framework." Structurally distinct stack from the rest of the batch but same repetitive lesson wrapper — treat as one small cluster, not 6 separate candidates.
- **2 Python folders** (e14 observability platform, e15 help-desk MVP) apply the same pattern in a `pyproject.toml`/pytest stack rather than Next.js — same disposition as the main cluster.
- **No git repos anywhere in this batch** — every `git log` check came back empty; all folders are plain filesystem drops from the generation pipeline, dated this week (2026-09-17 through 2026-09-23), except three outliers: f1 (empty, Mar 21 2026), j6 (empty, Mar 27 2026), and z3 (Apr 1 2026, the two-app-bundle structure) — these three predate the rest of the wave and may be earlier prototypes of the pipeline.
- **Two genuinely non-template folders stand out**: rn1 (a real, large Bluesky open-source fork used as lesson substrate — by far the strongest single item in this batch) and z1 (an ADR/decision-log style docs pack that doesn't follow the Astra chapter template). Both merit being pulled out and treated individually rather than archived with the cluster.
- **g1/X1 pairing**: both reference "Bagel Atlas"/"bagel intel" as a product concept, but g1 carries an original hand-written build prompt describing a non-trivial AI-research-ingestion-to-publish workflow, while X1 wraps a differently-named app of the same theme in a standard Astra lesson. Worth a closer look at whether g1 actually completed the described pipeline before deciding its disposition — it's the one folder in the batch that reads like an attempt at an original product rather than a teaching artifact.
- **f1 and j6 are empty** (0 files) — likely placeholder/reserved slots in the numbering scheme that were never populated; safe to delete.
- **Data hygiene**: zz4 contains a nested self-copy (`zz4/zz4/`) that should be resolved before any archiving decision; several folders leave build/log artifacts (`.tsbuildinfo`, `dev-server.log`, `.next-dev*.log`) checked into the folder since there's no `.gitignore`-backed git repo to keep them out.
