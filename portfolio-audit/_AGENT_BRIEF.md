# Batch Audit Brief (read fully before starting)

You are auditing ONE batch of an archive of software projects for a developer growing junior → mid → senior
(web/TS/React/Next/Node/C#/.NET/Postgres/SQL Server focus; practical engineering, not LeetCode).

## HARD RULES
- READ-ONLY on every project. Do not edit, install, build, run tests, upgrade, delete, git commit, or git checkout anything.
  Allowed: ls/find/cat/head/grep/wc, `git log --oneline | head`, `git -C <dir> log -1 --format=%ci`.
- Write exactly ONE file: the output path given in your task. Nothing else.
- Never judge from names alone. Every claim cites evidence (relative file paths / dirs / manifests / test files).
  If unsure write `UNKNOWN / NEEDS DEEPER INSPECTION`.
- Be efficient: skip node_modules, bin, obj, .next, dist, build, .git internals, vendored deps. Use `find -maxdepth`,
  manifests, READMEs, schema/migration files, test dir listings, 2-4 key source files per significant project.
- Detect boundaries: one folder may hold several apps; several folders may be versions of one app — say so.
- Tiny experiments / boilerplate / empty folders: one-line record only (still list them).

## OUTPUT FORMAT (markdown)

Start with:
```
# Batch NN — <title>
Scope: <dirs covered>  |  Candidate dirs inspected: N  |  Meaningful projects: N  |  Tiny/empty/boilerplate: N
```
Then a quick table of ALL candidates:
`| Project | Path | Type | Origin | Stack | Complexity | Docs | Disp |`

Then, for each MEANINGFUL project, a record:

```
## <name>
- Path: ...            - Origin: ORIGINAL | OPEN-SOURCE CLONE | COURSE/GENERATED (built by an LLM as a course) | FORK
- Type: web app / API / CLI / desktop / mobile / library / curriculum / docs-only / monorepo(N apps)
- State: complete | working-looking | partial | skeleton | docs-only     - Size: ~files / ~LOC (rough)   - Last modified: date (git or mtime)
- Purpose: 1–3 sentences (what it does + business domain)
- Stack: FE | BE | DB | ORM | Auth | Test | Infra/CI | notable libs/integrations
- Architecture: (monolith/modular monolith/microservices/SPA/SSR/workers/queues/cache/event-driven/...)
- Complexity: Tiny | Tutorial | Junior | Junior+ | Mid | Mid+ | Senior-oriented | Production-like
- Educational material: NONE|MINIMAL|USEFUL|STRONG|EXCELLENT — where (paths), what kind (onboarding/ADRs/curriculum/exercises/
  interview/flashcards...), approx file count, quality notes (generic/project-specific/deep/shallow/repetitive/outdated), preserve or rewrite
- Quality observations: 3–8 bullets with evidence (arch, validation, errors, tests, security, DB access, transactions, config, observability)
- Old-AI-generated smells: bullets (fake/mock-as-complete, giant files, shallow tests, boilerplate, hallucinated APIs, weak auth, etc.) or "none seen"
- Skill tags: pick from the VOCAB below
- Duplicate/overlap: which other projects (by name/path) it overlaps, if known
- Learning value: Low | Medium | High | Very High  — one-line reason
- Transformation opportunity (only if High+): what it could become (1–3 lines)
- Interview stories it could support (only if Medium+): short list
- Proposed disposition: A FLAGSHIP | B HIGH-VALUE | C SPECIALIZED | D REFERENCE | E EXERCISE SOURCE | F CONSOLIDATE | G ARCHIVE — reason
```

End with `## Batch observations`: clusters/duplicates noticed, overtrained patterns, notable gaps, surprises.

## SKILL VOCAB (use these exact tags)
fe-react, fe-next, fe-state, fe-forms-validation, fe-a11y, fe-testing, fe-perf, ts-types,
be-node-express, be-nest, be-dotnet, be-python, be-rest-design, be-graphql-trpc, be-validation, be-error-handling, be-async-jobs,
authn, authz-rbac, multitenancy,
db-postgres, db-sqlserver, db-sqlite, db-mongo, db-modeling, db-migrations, db-sql-raw, db-indexes-perf, db-transactions, db-concurrency, orm,
test-unit, test-integration, test-e2e, test-ci,
arch-modular-monolith, arch-clean-hex, arch-microservices, arch-event-driven, queues, caching, idempotency, realtime-ws, outbox,
docker, ci-cd, cloud-aws, cloud-azure, deploy, config-secrets, observability-logs, observability-metrics-tracing,
security-owasp, perf-investigation, incident-debugging, zero-downtime-migration, backcompat-versioning, design-docs-adrs,
legacy-codebase-reading, code-review, mobile-rn, desktop-electron-tauri, ai-llm-integration, agentic-engineering, crud-basic
