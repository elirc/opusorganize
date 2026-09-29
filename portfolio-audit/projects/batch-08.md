# Batch 08 — docs, plans, and prior audit/meta folders
Scope: Amasterplan, "master plan", "claude docs", GPTDocs, readme, "New folder", AstraOrganized, AstraOrganized2, geminiorganized, project-inventory, loose root *.md/*.txt/.docx, "_Organized Desktop\11 Loose Files"  |  Candidate dirs inspected: 11  |  Meaningful projects: 5 (all docs-only)  |  Tiny/empty/boilerplate: 6

This batch is almost entirely non-code: learning plans, a resume-catalog readme, and — most importantly — **two prior desktop-wide audits** whose data should be reused rather than redone. `geminiorganized` is a large stale full-copy snapshot of ~80 other projects (already covered live in other batches) and is not itself a project to audit further.

| Project | Path | Type | Origin | Stack | Complexity | Docs | Disp |
|---|---|---|---|---|---|---|---|
| Master Learning Plan | `master plan/` | docs-only (curriculum plan) | ORIGINAL (Claude-authored, human-directed) | Markdown | N/A | STRONG | B HIGH-VALUE |
| Claude study-plan drafts | `claude docs/` | docs-only (3 alternative curricula + 2 reference docs) | ORIGINAL | Markdown | N/A | USEFUL | D REFERENCE |
| GPTDocs expanded references | `GPTDocs/` | docs-only (expanded reference pair) | ORIGINAL (GPT-authored per name) | Markdown | N/A | USEFUL | F CONSOLIDATE (dupe of claude docs pair, expanded) |
| Desktop catalog readme | `readme/README.md` | docs-only (index/nav doc) | ORIGINAL | Markdown | N/A | MINIMAL | G ARCHIVE (superseded by project-inventory) |
| Full desktop project inventory | `project-inventory/` = `AstraOrganized/` (identical) | docs-only (auto-generated catalog, 341 projects) | GENERATED (LLM scan, 2026-09-06) | Markdown + JSON | N/A | STRONG (breadth, thin per-item depth) | B HIGH-VALUE (reuse as cross-reference, don't re-scan) |
| Astra fable-review audit (`fablereview/`) | `AstraOrganized2/fablereview/` | docs-only (prior KEEP/IMPROVE/REWORK audit of 153 projects) | GENERATED (18-agent Opus review + Fable synthesis, 2026-09-16/18) | Markdown + JSON | N/A | EXCELLENT | A FLAGSHIP (reuse directly — see below) |
| Astra delivery/status tracking (`astradocs/`, `astra-remaining-improvements/`, `astrafinalplan/`, `dfableandopus/`, etc.) | `AstraOrganized2/*` (minus fablereview) | ops scaffolding: scripts, backups, delivery manifests, progress JSON | GENERATED tooling | Python scripts, JSON, logs | N/A | N/A (not learning docs) | G ARCHIVE (operational residue, not curriculum) |
| geminiorganized (stale mirror) | `geminiorganized/` | ~80-project stale full-copy snapshot (mtimes ~2026-07-03, vs live originals updated since) | mirrors other batches' ORIGINAL/CLONE/COURSE projects | mixed | N/A | N/A | G ARCHIVE (stale duplicate of live projects; do not audit contents here) |
| Amasterplan | `Amasterplan/` | empty dir | N/A | N/A | N/A | NONE | G ARCHIVE |
| New folder | `New folder/` | empty dir | N/A | N/A | N/A | NONE | G ARCHIVE |
| Reps Clone upskilling plan | `Reps_Clone_Upskilling_Plan.docx` (loose root) | docs-only (build spec) | ORIGINAL | Markdown-in-docx | N/A | USEFUL | D REFERENCE |
| Astra space-game rebuild prompt | `astra-space-rebuild-prompt.md` (loose root) | docs-only (build prompt, 227 lines) | ORIGINAL | Markdown | N/A | USEFUL | D REFERENCE (references `astraspacegameweb`, covered elsewhere) |
| spacegames.txt (loose root) | `spacegames.txt` | empty file (0 lines) | N/A | N/A | N/A | NONE | G ARCHIVE |
| _Organized Desktop\11 Loose Files | `_Organized Desktop/11 Loose Files/` | 3 loose files: resume tech-stack list, a rename log, a stray `test.db` | ORIGINAL | Markdown/SQLite | N/A | MINIMAL | G ARCHIVE |

---

## Master Learning Plan
- Path: `C:\Users\Owner\Desktop\master plan\` (files: `MASTER-PLAN.md`, `00-PROJECT-LADDER.md`, `optimal-upskill-plan.md`, `README.md`; has its own `.git`)
- Origin: ORIGINAL — human-directed, Claude-authored career/upskilling plan
- Type: docs-only / curriculum plan
- State: complete as a document; describes a not-yet-fully-executed 16-week plan
- Purpose: A 16-week, 8-hr/day junior→mid SWE upskilling plan for the user (Eli), merging three earlier plan drafts found in `claude docs/`. `00-PROJECT-LADDER.md` rates every project on the Desktop (as of 2026-07-06) into 5 difficulty tiers with a concrete study order; `optimal-upskill-plan.md` is the synthesized "final answer" version.
- Educational material: STRONG — this *is* the meta-curriculum for the whole portfolio. It names ~50 specific projects by path and explains why each belongs at its tier, includes exit criteria per phase, a daily/weekly rhythm, and explicit "AI-delegation week" and "diagram discipline" mechanics.
- Quality observations:
  - Tightly project-specific (cites real paths like `.netpastebin`, `buildjira`, `grokbuildmultitenantproject`) rather than generic advice.
  - Self-aware about drift: flags empty/duplicate folders (`master555`, `recipegen-temp`≈`recipegen-app`, `Amasterplan`) and admits some folders were unreviewed due to scan timeouts.
  - Written 2026-07-06/09, i.e. **before** the Astra build wave and the Fable review (both Sept 2026) — the tier ladder does not know about `astraupskill/` curricula that now ship inside many of these projects, so it should be read as "which project" guidance, cross-checked against `fablereview/LEARNING_PATH.md` for "which curriculum inside it is good."
  - No code, so no test/security/architecture observations apply.
- Old-AI-generated smells: none seen (plan text, not code).
- Skill tags: design-docs-adrs
- Duplicate/overlap: `claude docs/` (its three source plans), `project-inventory/PROJECT_INDEX.md` (overlapping but independently-generated project catalog), `AstraOrganized2/fablereview/LEARNING_PATH.md` (a newer, evidence-based "which 30 projects are worth it" list that should now take priority for curriculum quality).
- Learning value: Very High — this is the organizing document for the user's actual goal (get hired). Its project ladder should be reconciled with the newer Fable review findings but the pedagogy (project-first + Socratic + diagram-discipline, ticket/PR simulation, AI-delegation week) is sound and worth keeping as-is.
- Transformation opportunity: Merge `00-PROJECT-LADDER.md`'s tier structure with `fablereview/LEARNING_PATH.md`'s per-project quality verdicts to produce one authoritative "what to build/study, in what order, using which of the two curriculum sets" master doc — this is likely the natural output of the whole portfolio-audit effort.
- Interview stories it could support: "how I planned and executed my own upskilling," a good narrative of self-directed learning discipline.
- Proposed disposition: B HIGH-VALUE — keep and update, don't archive; it is the connective tissue for the rest of the portfolio.

## Claude study-plan drafts (`claude docs/`)
- Path: `C:\Users\Owner\Desktop\claude docs\` (`plan-1-project-first.md`, `plan-2-socratic.md`, `plan-3-visual.md`, `production-code-best-practices.md`, `worked-examples-junior-to-senior.md`; has its own `.git`)
- Origin: ORIGINAL
- Type: docs-only
- State: complete
- Purpose: Three alternative 16-week curriculum designs (project-first/ticket-simulation, Socratic/interrogation-style, diagram-first) that were later merged into `master plan/MASTER-PLAN.md`, plus two standalone reference docs: a JS/TS/React/Node/agentic-engineering production-practices checklist (213 lines) and a worked-examples doc (792 lines, not read in full — large).
- Educational material: USEFUL — `production-code-best-practices.md` is a genuinely dense, specific checklist (e.g., correct nuance on `??` vs `||`, `Promise.allSettled` vs `Promise.all`, operational vs programmer errors, custom `AppError` with `code`/`statusCode`) that could double as a code-review rubric for the rest of the portfolio's projects.
- Quality observations:
  - `plan-1-project-first.md` is concrete and reusable as a prompt-template library (Build/Onboard/Ticket/Review/Explain prompts) independent of which plan "won."
  - The three plans were explicitly merged into `master plan/`, so as standalone plans they're now historical drafts, not the live plan.
- Old-AI-generated smells: none seen.
- Skill tags: design-docs-adrs, code-review
- Duplicate/overlap: superseded (as a plan) by `master plan/MASTER-PLAN.md`; `production-code-best-practices.md` and `worked-examples-junior-to-senior.md` have expanded duplicates in `GPTDocs/`.
- Learning value: Medium — the plans are superseded; the two reference docs (best-practices checklist, worked examples) retain standalone value as review checklists.
- Proposed disposition: D REFERENCE — keep the two reference docs (or their `GPTDocs/` expanded versions) as a rubric source; the three plan drafts are archival once `master plan/` is treated as authoritative.

## GPTDocs expanded references
- Path: `C:\Users\Owner\Desktop\GPTDocs\` (`production-code-best-practices-expanded.md` — 2063 lines, `worked-examples-junior-to-senior-expanded.md` — 2964 lines; has its own `.git`)
- Origin: ORIGINAL (GPT-authored expansions of the `claude docs/` pair, per `master plan/optimal-upskill-plan.md`'s reference: "the expanded gptdocs versions")
- Type: docs-only
- State: complete, not fully read (large; verified via line counts + prior cross-reference in `master plan/optimal-upskill-plan.md` line 79)
- Purpose: Expanded (10x+ longer) versions of the same two reference docs in `claude docs/` — a production best-practices checklist and worked before/after examples, meant for the plan's "cover the fix, write your own first" workbook-style mobile reading rotation.
- Educational material: USEFUL — explicitly designed into the master plan's mobile-reading block; not independently verified for quality/accuracy beyond the shorter `claude docs/` sibling (same topic, same author lineage).
- Quality observations: UNKNOWN / NEEDS DEEPER INSPECTION beyond the shorter sibling docs — did not read the full 5,000+ combined lines.
- Skill tags: design-docs-adrs, code-review
- Duplicate/overlap: direct duplicate pairing with `claude docs/production-code-best-practices.md` and `claude docs/worked-examples-junior-to-senior.md` (same topics, expanded).
- Learning value: Medium — useful as a denser rubric, but redundant with the shorter version; only one of the two pairs is needed in the eventual consolidated doc set.
- Proposed disposition: F CONSOLIDATE — pick one of {`claude docs`, `GPTDocs`} pair per topic (likely the expanded GPTDocs versions, since the plan already routes mobile reading to them) and archive the other.

## Desktop catalog readme
- Path: `C:\Users\Owner\Desktop\readme\README.md` (has its own `.git`)
- Origin: ORIGINAL (LLM-generated catalog/summary doc)
- Type: docs-only
- State: complete but dated — references a 12-category `_Organized Desktop` shortcut structure and lists only ~25 projects with brief purpose blurbs.
- Purpose: An earlier, hand-curated (not exhaustively scanned) narrative catalog of Desktop projects grouped by theme (Net Workspaces, Build Projects, App & Product Projects, JS Training, Multi-Project Workspaces, Career Planning, Misc), plus a 5-phase "recommended upskilling path" narrative.
- Educational material: MINIMAL — it's an index, not teaching content itself; the "recommended upskilling path" section (Phase 1–5) is a simpler, less rigorous cousin of `master plan/00-PROJECT-LADDER.md`.
- Quality observations: Predates the full 341-project `project-inventory` scan; covers a subset and is less rigorous/complete (no state/duplicate detection).
- Old-AI-generated smells: n/a (index doc).
- Skill tags: design-docs-adrs
- Duplicate/overlap: fully superseded by `project-inventory/PROJECT_INDEX.md` (exhaustive, state-tagged, duplicate-flagged) and by `master plan/00-PROJECT-LADDER.md` (more rigorous tiering with reasons).
- Learning value: Low — content is subsumed by two better documents in this same batch.
- Proposed disposition: G ARCHIVE — superseded.

## Full desktop project inventory (`project-inventory/` ≡ `AstraOrganized/`)
- Path: `C:\Users\Owner\Desktop\project-inventory\` and `C:\Users\Owner\Desktop\AstraOrganized\` — **confirmed byte-identical** (`diff -q` on both `PROJECT_INDEX.md` and `project-catalog.json` returned no differences; these are two copies of the same generated artifact, not independent audits)
- Origin: GENERATED — automated LLM scan across the whole Desktop + `_Organized Desktop`, generated 2026-09-06
- Type: docs-only (Markdown report + JSON catalog)
- State: complete, single-pass, breadth-first
- Purpose: Enumerates **341 identified codebases/repositories** on the Desktop, categorized into 19 groups (Desktop root apps, `.NET` systems, `_Organized Desktop`'s 12 numbered categories, curriculum collections like `newcodexJS`), with per-project: 1-line purpose (often just the first README line, sometimes low-signal e.g. "Application project or component in X"), detected languages/frameworks, an "apparent state" (partial / tutorial / working-looking / unknown), notable features (git, tests, Docker, Next.js SSR, etc.), and same-name-root duplicate flags (e.g. `spacegame` ↔ `spacegamev2`, `gitjira` ↔ `gitjira-app`, `jobtrack` ↔ `job track`).
- Educational material: STRONG as breadth — it is effectively the seed list this whole portfolio-audit project is working through batch by batch; NONE as depth — per-project purpose lines are often a single truncated README sentence and "apparent state" is a heuristic (git presence + test dirs + keyword grep), not a real read.
- Quality observations:
  - Summary stats: 119 `partial`, 62 `tutorial`, 21 `unknown`, 139 `working-looking` across 341 projects (2026-09-06 snapshot — some of these projects have since been touched by the Astra/Fable work described below, so states are stale for the 153 Astra-changed ones).
  - Duplicate-detection is naive (string-prefix matching on folder name), catches some real dupes (`spacegame`/`spacegamev2`) but would miss/false-positive on others — treat flags as leads, not conclusions.
  - JSON catalog (`project-catalog.json`) exists alongside the Markdown and is presumably the same data machine-readable; not diffed in detail but file sizes matched exactly between the two copies.
- Old-AI-generated smells: n/a (it's a meta-document about other projects, not project code).
- Skill tags: design-docs-adrs
- Duplicate/overlap: this **is itself a duplicate** — `AstraOrganized/` and `project-inventory/` hold the identical file. `readme/README.md` is a smaller, older, subsumed cousin. Complementary (not overlapping) with `AstraOrganized2/fablereview/` — that one covers only the 153 Astra-touched projects but in far more depth (actual code review with evidence), whereas this one covers all 341 but shallowly.
- Learning value: High as a cross-reference / checklist for this audit project itself (use it to confirm no project was missed across batches, and to seed duplicate-checking), Low as standalone learning content.
- Transformation opportunity: Use as the master "have we covered every folder" checklist against the final portfolio-audit output; retire one of the two identical copies.
- Proposed disposition: B HIGH-VALUE (as audit infrastructure — reuse, don't re-derive) but F CONSOLIDATE the duplicate copy (keep one of `AstraOrganized/` or `project-inventory/`, delete the other).

## Astra fable-review audit (`AstraOrganized2/fablereview/`)
- Path: `C:\Users\Owner\Desktop\AstraOrganized2\fablereview\` (key files: `SUMMARY.md`, `SCOREBOARD.md`/`scoreboard.json`, `LEARNING_PATH.md`, `IMPROVEMENT_BACKLOG.md`, `RUBRIC.md`, `registry.json`, 153 individual reports in `reviews/`, plus a completed fix pass in `_fix/` with `FIX_REPORT.md` and per-project reports)
- Origin: GENERATED — 18 parallel Opus review agents (2026-09-16) synthesized by Fable, followed by a complete fix pass (2026-09-18, Fable + Opus) that applied every review's top fix
- Type: docs-only (prior audit, directly matches the user's memory entry `fablereview-astra-audit.md`)
- State: complete and closed (all 153 projects reviewed, all fixes applied per `FIX_REPORT.md`)
- Purpose: This is **the single most valuable reusable artifact found in this batch** for the current portfolio audit. It reviews all 153 projects that a prior "Astra" build campaign modified (adding `astraupskill/`-style 7-file learning curricula to each — `01-CODEBASE-MAP.md` … `07-TRACE-LAB.md`), scoring each on 8 rubric dimensions (accuracy, change quality, pedagogy, CRUD relevance, reproducibility, verification honesty, junior fit, specificity), and issuing a final **KEEP / IMPROVE / REWORK** verdict plus a **core / elective / reference / skip** learning-path role for each.
- Educational material quality of the audit itself: EXCELLENT — `SUMMARY.md` is a rigorous, evidence-cited (file:line specific) meta-review: confirms real bugs found/fixed by Astra (e.g. six React apps that never called `createRoot`, a `DELETE FROM campaigns` left in a catch block, forgeable base64 session cookies, authorization checked after pagination), but also catches the review subject's own flaws (wave-1's 75 small-JS-app curricula are one template rendered 75 times, 73% median shared paragraphs, six-times-repeated trace-lab paragraphs, templated sentences that are factually false for the project they landed in).
- Directly reusable data for the ongoing portfolio audit:
  - **`SCOREBOARD.md`/`scoreboard.json`**: a ready-made KEEP(89)/IMPROVE(55)/REWORK(9) table across all 153 Astra-touched projects, with per-dimension scores (1–5), word counts, shared-paragraph %, and a one-line "top fix" — this can be dropped straight into other batches' records for any of those 153 projects instead of re-deriving a curriculum-quality verdict from scratch.
  - **`LEARNING_PATH.md`**: identifies ~30 of the 153 as `core` path-role projects — the recommended actual study sequence, evidence-based (supersedes the 2026-07-06 `master plan/00-PROJECT-LADDER.md` tiering for curriculum quality, though the ladder is still useful for raw project-selection/difficulty).
  - **Two live action items flagged (not yet resolved as of this audit)**: (1) a live Shopify `shpat_` admin token still sitting in a pre-change backup at `AstraOrganized2/astra-remaining-improvements/backups/cf8875344b43/scripts/populate-metaobjects.js` (needs revocation + deletion — matches the "revoke Shopify token" open item in the user's memory), and (2) `astraupskill/original/src/lib/commerce/commerce.test.ts` (in the e13 project) is collected by Vitest and runs `db:push`/`db:seed` against the live dev DB — needs an exclude or rename before anyone runs `npm test` there.
- Quality observations about the audit process itself:
  - Explicitly re-hashed delivered files and recounted claimed tests against files on disk rather than trusting Astra's self-reported claims — found "no inflated browser claims and only a handful of miscounts," i.e. the audit is itself evidence-based, not just LLM-vibes scoring.
  - Transparent about its own limits ("Reviewers read; they did not execute"), and about score noise ("a one-point difference between batches is noise; wave-level gaps are not").
- Old-AI-generated smells (as documented BY this audit, about the Astra deliverables it reviewed — reusable finding, not this batch's own claim): fake/templated pedagogy at scale (wave-1's single-template-×75 problem), whole-file CRLF/Prettier reformatting hiding real diffs, minified test files, dead-code helper trios injected wholesale, packages still pinned to `"latest"` with no lockfile, inherited test suites reported as new deliverables.
- Skill tags: design-docs-adrs, code-review, legacy-codebase-reading
- Duplicate/overlap: none — this is the deepest and most current audit in the whole Desktop; other batches covering any of the 153 named projects (e.g. `meterforge`, `campusops`, `borrowbox`, `formforge`, `buildsql`, `buildwhiteboard`, `netgum`, `netpastebin`, `nettrello`, `buildjira`, `buildsubbox`, `master2`–`master7`, many `_Organized Desktop/05 Numbered Experiments/*` entries, `grokbuild*` projects, `job track/*` nested apps, etc.) should cite this review's verdict and top-fix rather than re-deriving one.
- Learning value: Very High — both as a source of ready verdicts for ~150 other projects across this audit, and as a template for how to run a rigorous, evidence-cited, multi-agent review (worth reusing the `RUBRIC.md`/`REVIEW_TEMPLATE.md` methodology for this very portfolio-audit project).
- Proposed disposition: A FLAGSHIP — this folder (specifically `fablereview/`) should be treated as a primary input to the final portfolio-audit synthesis, not archived; cross-reference every other batch's coverage of the 153 named projects against it.

## Astra delivery/status tracking (remaining `AstraOrganized2/*`)
- Path: `AstraOrganized2/astradocs/`, `astra-remaining-improvements/`, `astrafinalplan/`, `astraupskill/` (a single leftover curriculum template, not the per-project ones), `dfableandopus/`, `documentation-audit/`, `dependency-quarantine/`, `independent-snapshot/`, `scripts/`, `stage/`, plus a nested nearly-empty nested copy of `_Organized Desktop/05 Numbered Experiments/e3`
- Origin: GENERATED tooling — Python scripts (`apply_delivery.py`, `finalize_*.py`, `configure_*.py`, audit/coverage scripts), JSON progress/delivery manifests, per-project backup snapshots (many dozens of `backups/<hash>/` dirs), and status reports (`ASTRA_PROJECT_STATUS_2026-09-19.md`, `CRUD_UPSKILL_BATCH_0[1-4]_REPORT_2026-09-21.md`, etc.)
- Type: docs-only / ops scaffolding — not a learning curriculum or a software project
- State: mixed — `ASTRA_PROJECT_STATUS_2026-09-19.md` (read) is a careful, reconciled status report: 153 projects delivered/reviewed and closed under Fable's registry, 161 second-wave project families still queued (14 staged, 147 not started), with explicit warnings not to re-import "old KEEP/IMPROVE/REWORK verdicts" from the closed 153 into the still-open queue.
- Purpose: This is the operational machinery (backups, delivery manifests, batch-runner scripts, coverage auditors) behind the Astra build campaign and the subsequent Fable review — useful as provenance/evidence if a specific claim in `fablereview/` needs to be double-checked (e.g. its own backup files, VERIFICATION logs), but not itself educational content.
- Quality observations:
  - Backups directory alone (`astra-remaining-improvements/backups/`) contains dozens of hash-named subfolders — this is where the live Shopify token noted above physically resides (`backups/cf8875344b43/...`); it is a real live secret sitting in a pile of scripts and backups, worth flagging loudly again here.
  - `astradocs/CRUD_UPSKILL_BATCH_0[1-4]_*` (2026-09-21) show ongoing/parallel curriculum-building work distinct from the closed 153-project Fable registry — i.e. there is a **second, still-in-progress** Astra build effort (161 families) not yet reviewed by anyone; that work has not been through the same rigor as `fablereview/` and its quality is unverified.
- Old-AI-generated smells: n/a (scripts/ops artifacts, not reviewed as code).
- Skill tags: design-docs-adrs
- Duplicate/overlap: complements `fablereview/` (provides its evidence trail) but is not itself review content; the leftover single `astraupskill/` template folder here (7 files, no project attached) appears to be a stray generator template, not a delivered curriculum.
- Learning value: Low as content, Medium as provenance (only consult when verifying a `fablereview/` claim or hunting the Shopify token).
- Proposed disposition: G ARCHIVE — keep only long enough to (a) revoke/delete the Shopify token from the backup, then archive/delete the rest; it's disk-consuming operational residue once the token is handled.

## geminiorganized (stale mirror)
- Path: `C:\Users\Owner\Desktop\geminiorganized\` — 80 top-level dirs prefixed `General_*` (43), `LLM_Generated_*` (19+), `OpenSource_Upskilling_*` (10+), plus one `FableDocs_Projects_Hermes/`
- Origin: mirrors ORIGINAL/CLONE/COURSE projects that live natively elsewhere on the Desktop (e.g. `General_Ankijs` mirrors `ankijs/`, `General_Aral` mirrors `aral/`, `OpenSource_Upskilling_.Stripe` mirrors `.netstripe/`)
- Type: full-file-copy snapshot / categorized duplicate archive, not a project of its own
- State: **confirmed stale** — spot-checked `General_Ankijs/package.json` and `README.md` against live `ankijs/`: geminiorganized's copies are dated ~2026-07-03, the live originals ~2026-09-12; content differs (package.json byte size differs: 1074 vs 1670 bytes)
- Purpose: Appears to be an earlier "organize the Desktop by category" pass (by a Gemini-branded agent, per the folder name and the `LLM_Generated_*`/`OpenSource_Upskilling_*` naming convention) that made full physical copies of dozens of projects into category buckets, rather than leaving them in place or using shortcuts/symlinks.
- Quality observations:
  - This is a real, large duplicate of disk content, not a docs-only artifact — but per the brief's scope (batch 08 covers it as "docs, plans, and prior audit/meta folders"), it should be flagged and summarized here rather than have its ~80 sub-projects individually re-audited (those live originals are each covered in whichever batch owns their canonical path, e.g. `ankijs`, `aral`, `.netstripe`, `hermes` etc.).
  - Because the copies are stale (pre-dating both the Astra build wave and Fable's review), **any analysis done against files inside `geminiorganized/` would be analyzing outdated snapshots** — always defer to the live canonical path for these ~80 projects.
- Old-AI-generated smells: n/a (duplicate archive, not itself authored content).
- Skill tags: (none — not a learning project)
- Duplicate/overlap: duplicates ~80 other projects across the whole Desktop wholesale; the `readme/README.md` in this same batch explicitly says `_Organized Desktop` is "a folder of shortcuts (.lnk)" — i.e. the *intended* organization mechanism was symlinks/shortcuts, and `geminiorganized` is a heavier, stale, full-copy alternative that likely predates or duplicates that shortcut folder's purpose.
- Learning value: Low/None as a folder in itself (mirror only); do not use as a source of truth.
- Proposed disposition: G ARCHIVE — safe to delete once confirmed no unique file exists only there (not verified in this pass; a full diff against live originals was out of scope for a read-only single-batch audit — flag for a dedicated disk-reclaim pass, likely large, tens of GB scale given full project copies across 80 dirs).

## Loose docs (Reps Clone plan, Astra space-game prompt)
- Path: `Reps_Clone_Upskilling_Plan.docx` (Desktop root, 17KB) and `astra-space-rebuild-prompt.md` (Desktop root, 227 lines)
- Origin: ORIGINAL build-spec prompts, not delivered projects
- Type: docs-only (build specs / prompts)
- State: specs only — no corresponding project folder confirmed built from either in this pass
- Purpose:
  - `Reps_Clone_Upskilling_Plan.docx` (2026-06-16): a feature spec for cloning `reps.zander.wtf` (a daily-JS-puzzle habit app, Wordle-style) on React + Next.js, then extending it with structured learning paths, difficulty tiers with progressive hints, and explanations/feedback aimed at true beginners rather than only people who can already code. Well-structured: core-clone parity table (daily puzzle, in-browser Monaco/CodeMirror editor, sandboxed Web Worker test runner, streaks, shareable results) followed by extension features.
  - `astra-space-rebuild-prompt.md`: a detailed build prompt to rebuild `astraspacegameweb` (a medieval Tribal-Wars-style game, covered in another batch) as a space-themed "Astra Expanse" with exact numbers/formulas carried over but original code (explicitly: "do not copy files wholesale and rename"). Read-only reference to the existing implementation is baked into the prompt (`docs/`, `packages/shared/game.ts`, `packages/config/worlds/w1.json`).
- Quality observations: Both are competent, specific build-prompt documents (concrete feature tables / exact formulas + explicit anti-shortcuts instructions), not vague ideas.
- Skill tags: design-docs-adrs
- Duplicate/overlap: `astra-space-rebuild-prompt.md` directly references and depends on `astraspacegameweb` (covered elsewhere in the portfolio); worth flagging that batch to check whether `astraexpanse` was ever actually built from this prompt (not found under this name during this pass — likely unbuilt).
- Learning value: Medium — reusable as project-spec templates; `Reps_Clone_Upskilling_Plan.docx` in particular is a good example of "clone + extend for a specific pedagogical purpose" spec-writing.
- Proposed disposition: D REFERENCE — keep as spec references; check the batch covering `astraspacegameweb` for whether `astraexpanse` exists anywhere else on disk (this pass found no such folder).

## Tiny / empty / boilerplate records
- `Amasterplan/` — completely empty directory. G ARCHIVE.
- `New folder/` — completely empty directory. G ARCHIVE.
- `spacegames.txt` (Desktop root) — 0-byte/0-line file. G ARCHIVE.
- `_Organized Desktop/11 Loose Files/` — three files only: `eli_resume_tech_stack_list.md` (a useful but small cross-reference of ~17 differently-named resume files and their listed tech stacks — could help resolve which resume version is canonical), `rename-log.md` (not read in detail — a housekeeping log), and a stray `test.db` SQLite file (origin unclear, likely leftover from some project's test run). All G ARCHIVE / low-value, though `eli_resume_tech_stack_list.md` is worth a 30-second glance if consolidating resumes.

---

## Batch observations

- **Reuse, don't re-derive.** The single most important finding in this batch is that a rigorous, evidence-based prior audit already exists and covers 153 of the projects other batches are independently scoring: `AstraOrganized2/fablereview/` (`SCOREBOARD.md`, `LEARNING_PATH.md`, `reviews/<project>.md`). Every other batch touching one of those 153 projects should pull its KEEP/IMPROVE/REWORK verdict and top-fix from there instead of re-scoring from scratch — the fable review is deeper (file:line evidence, re-hashed file counts, actual test-count verification) than a single-pass batch audit can be.
- **Two audit generations of the same "catalog the whole Desktop" idea exist**, at different depths: `project-inventory/`≡`AstraOrganized/` (breadth: 341 projects, shallow, 2026-09-06) and `readme/README.md` (even shallower, older, ~25 projects). The breadth-first one is worth keeping as a coverage checklist for this very portfolio-audit project; the older readme is fully superseded and can be archived.
- **Duplicate audit copies exist and should be consolidated**: `AstraOrganized/` and `project-inventory/` are byte-identical files — delete one. `claude docs/` and `GPTDocs/` hold the same two reference docs at two different lengths — keep one pair.
- **A live secret is sitting in this batch's territory**: the Shopify `shpat_` admin token in `AstraOrganized2/astra-remaining-improvements/backups/cf8875344b43/scripts/populate-metaobjects.js`, already flagged by the fable review's own `SUMMARY.md` as unresolved and matching the "revoke Shopify token" open item in the user's standing memory — this is the single highest-priority actionable item found in this batch (read-only audit here; action item only, not acted on).
- **`geminiorganized` is a large, stale, full-copy duplicate of ~80 other projects** (categorized by an earlier Gemini-branded organizing pass, prefixed `General_*`/`LLM_Generated_*`/`OpenSource_Upskilling_*`), confirmed stale by spot-check (July vs September mtimes, differing file sizes) — it should not be used as a source of truth for any of those 80 projects, and is a strong candidate for bulk deletion in a future disk-reclaim pass (not sized precisely in this read-only pass; a `du -sh` attempt timed out, but given ~80 full project copies it is plausibly multiple GB to tens of GB).
- **The user's own top-level career plan (`master plan/`) predates the Astra/Fable work by ~2 months** (2026-07-06/09 vs 2026-09-16/21) and its `00-PROJECT-LADDER.md` tiering doesn't know the newer `astraupskill/`-style curricula exist inside many tier-1/2/3 projects — reconciling the two (which project, from the ladder; which curriculum-quality verdict, from the fable review) is a natural next deliverable once all batches are in.
- **A second, unreviewed Astra build wave is in flight**: `astradocs/ASTRA_PROJECT_STATUS_2026-09-19.md` documents 161 second-wave project families (14 staged, 147 not started) that are explicitly *not* covered by the closed 153-project `fablereview/` registry — any of those, if found "complete" in another batch, should not be assumed to carry the same quality bar as the reviewed 153 until someone runs the equivalent review on them.
