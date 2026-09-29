# Educational Content Index

The archive contains far more learning material than code you could ever work through: `astraupskill/` packs in ≈200 folders,
`fabledocs*/` curricula in ~35, `dfableandopus/` interview packs in ~40, plus `docs/upskill` (Net-fleet, 10×47 files) and standalone curricula.
**The constraint is not material — it is doing the work.** Use this index to pick the few best packs; ignore the rest.

## Content families (formats you will keep meeting)

| Family | Where | Shape | Quality verdict | Keep? |
|---|---|---|---|---|
| **fabledocs "codebase cartography" (old)** | OSS clones in 03 Master Projects (`fabledocs/upskill/`, 53 files: 00-fast-track → 09-reference) | map → stack → architecture → code-reading gym → contribution practice → reference | Project-specific, cites real files; repetitive across clones by design | Keep; read at most 3 |
| **fabledocs 9-module (new)** | masterfinisc\infisical `fable-docs/` (60 files), masterflag, masteridur | adds self-graded modules + an **architecture critique** with file/line-cited races, missing outbox, god-files | Best single-generation OSS curriculum style | Keep; use as template |
| **fabledocs 2/3/4 waves** | masteroutline, mastertwenty, masteropen, netcleanarch | fabledocs2 onboarding · fabledocs3 **10 ADRs with interview translation** · fabledocs4 fire drills, capstones, SQL/front labs, flashcards, 4-week plan | Deepest and most senior material in the archive | **Keep — top tier** |
| **astraupskill (worked change)** | ≈200 folders (Astra pipeline, 2026-09) | 01-CODEBASE-MAP → 02-CONCEPTS → 03-WORKED-CHANGE → 04-TESTING/DEBUGGING → 05-PRACTICE → 06-SOLUTIONS → 07-TRACE-LAB + VERIFICATION, `evidence/`, `snapshots/` | 01/03/07 are project-specific; 02/05 are template text (per `AstraOrganized2/fablereview/LEARNING_PATH.md`) | Keep only where listed in LEARNING_PATH |
| **dfableandopus (career pack)** | ~40 folders (B1, e12–e20, master2–6, grokbuild*, build*, …) | interview Qs · stories/resume · code-reading drill · take-home · system-design follow-ups · flashcards | Useful but templated | Keep for your 5 flagships only |
| **Net-fleet docs/upskill** | netairag, netauth, netdocu, netdrop, netintercom, netlinear, netnotion, netshop, .netramp, .netstripe | 8 sections, ~47 files each; sampled content is project-specific (real file/line citations) | Good .NET reading material | Keep 1–2 (netdrop, netintercom) |
| **Course-repo docs** (gitvg fleet, gitjira-app, perch) | `docs/` + 15 sprint PRs + FLAW-LEDGER | sprint specs, ADRs, planted-flaw ledgers, postmortems | High — PR-per-sprint history is itself the lesson | **Keep** |

## Top 12 learning assets (ranked)

| # | Asset | Path | Why | Rating |
|---|---|---|---|---|
| 1 | Outline 4-wave pack | `Desktop\masteroutline\outline\fabledocs, fabledocs2..4` | onboarding + 10 ADRs w/ interview translation + fire drills + outbox & collab capstones | EXCELLENT |
| 2 | eShop story course + grader | `Desktop\netopen1\eShop\astra\` (72 stories, `check_course.py`) | only auto-graded story backlog on a real distributed .NET system | EXCELLENT |
| 3 | Infisical architecture critique | `O\03 Master Projects\masterfinisc\infisical\fable-docs\` | file/line-cited races, missing outbox, god-files: model senior review writing | EXCELLENT |
| 4 | Twenty / OpenStatus 4-pass packs | `O\03\mastertwenty\twenty\fabledocs*`, `O\03\masteropen\openstatus\fabledocs*` | metadata-driven CRM; quorum/alerting reliability capstones | EXCELLENT |
| 5 | gitjira-app docs | `Desktop\gitjira-app\docs\` (adr/, postmortems/, threat-model.md, RUNBOOK.md, security-audit.md, performance.md) | the most complete "real team" doc set on a codebase you own | EXCELLENT |
| 6 | OrchardCore reading paths | `Desktop\.netopen2\OrchardCore\fabledocs\upskill\` | Jr/Mid/Sr reading paths with explicit "ignore this" guidance | EXCELLENT |
| 7 | Flaw ledgers | `globehire`, `meterforge` (`FLAW-LEDGER.local.md`), `perch`, `gitvg\harbor`/`pulse`/`atlas` (5 planted flaws each) | planted-then-harvested bugs = ready interview stories | STRONG |
| 8 | fablereview LEARNING_PATH | `Desktop\AstraOrganized2\fablereview\LEARNING_PATH.md` + `SCOREBOARD.md` + `reviews/` | already-curated CRUD-reliability path (Stages 0–4) across 30 of the Astra projects | STRONG (reuse, don't redo) |
| 9 | Warband postmortem + ops docs | `spacegamev2` fabledocs (v1 postmortem), `astraspacegameweb\docs` | rewrite postmortem + observability/chaos | STRONG |
| 10 | C# trio | `csharptut` (read) → `csbootcamp` (auto-graded) → `c#interview` (490 Q&A, mock scripts) | complementary, not redundant | STRONG |
| 11 | unionboot + jstrain2.2 | `Desktop\unionboot` (verify-*.cjs, verification-report.json), `O\04\jstrain2.2` | verified exercise banks for fundamentals | EXCELLENT (but fundamentals) |
| 12 | stellar-conquest-architecture | `C:\Users\Owner\stellar-conquest-architecture` (1,761-line design doc) | only long-form design doc you have for a realtime system | STRONG |

## Gaps in the learning material
- 5 clones have **no curriculum**: Novu, Supabase, ToolJet, Typebot, Indico. Don't add any — you have plenty.
- Almost no material on: **cloud deployment (AWS/Azure), SQL Server, zero-downtime migrations, query-plan reading/indexing, frontend performance/a11y, on-call/incident command**.
- Duplicated or leftover doc trees need no action beyond ignoring: `docsclaude/`, `docs-codex-learning/`, `docs2/`, `docs3/`, `docs2.0/` (e.g. netairag docs2.0 duplicates docs/upskill).
- `master plan\00-PROJECT-LADDER.md` (2026-07-06) predates the Astra pass; `fablereview\LEARNING_PATH.md` (2026-09-18) supersedes its Tier 0–2. PRIORITY_ROADMAP.md supersedes both for Mid→Senior work.
