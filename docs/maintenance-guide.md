# Architecture and maintenance guide

Status: Draft, 2026-11-25

How the repository is built, how the pieces depend on each other, and how to keep it healthy. For scope, phases and principles see [architecture, scope and principles](architecture.md); for modelling rules see the [modelling guidelines](modelling-guidelines.md); for who does what see the [contributor guide](contributor-guide.md).

## 1. The idea in one picture

```text
          hand-written sources (edited by people and agents)
 ┌──────────────────────────────────────────────────────────────────┐
 │ ontology/foundation.md          concept catalogue (LD-C)         │
 │ ontology/concept-annotations.md aliases, summaries, context ...  │
 │ relationships/relationships.md  relationships (LD-R)             │
 │ governance/ambiguity-register.md ambiguous words (LD-A)          │
 │ governance/review-domains.md    10 domains, owners, questions    │
 │ governance/decision-log.md      decisions                         │
 │ domains/<d>/overview.md, company-questions.md                    │
 └──────────────────────────────────────────────────────────────────┘
        │ tools/build_domain_views.py            │ tools/build_question_workbooks.py
        ▼                                        ▼
 generated pages (never edited)          domains/<d>/questions-for-experts.xlsx
 domains/README.md, domains/<d>/README.md,     (generated structure, answers typed
 concepts.md, review.md, glossary.md            by experts and kept on rebuild)
                                                 │ tools/read_answers.py
                                                 ▼
                                         .review-notes/answers/<d>.md (for agents)
```

Everything a reader sees is generated from a few Markdown tables. Change a table, rebuild, and every page that shows that concept changes with it.

## 2. The building blocks

### Identifiers

| Prefix | What | Where it is defined |
|---|---|---|
| `LD-C` | Concept | One row in `ontology/foundation.md` |
| `LD-R` | Relationship between two concepts | One row in `relationships/relationships.md` |
| `LD-A` | Ambiguous word or open meaning question | One row in `governance/ambiguity-register.md`, with its proposed answer below the table |

IDs are permanent and never reused, even when a concept is retired. `python3 tools/next_ids.py` gives the next free ones. Human pages show names first and IDs in brackets.

### The registers

- **Catalogue** (`ontology/foundation.md`): one row per concept, in sections (Phase 1 foundation, 2026-11 additions, level 2). Columns: ID, canonical English name, owning module, proposed type (Entity, Role, Event, Agreement, Measure and so on), working business definition; level-2 rows add Level and Domain. Definitions are short; the rest lives in the annotations.
- **Annotations** (`ontology/concept-annotations.md`): tables keyed by concept, each with fixed headers that the generator recognises: Specialisations (child, parent, link), Resolution flags, Aliases (word, resolves to, scope), Required context, Usage notes, Priority and alignment, Plain-language summaries (in short, example, not to be confused with), Values.
- **Relationships** (`relationships/relationships.md`): source concept, relation (such as `is_a`, `part_of`, `fulfilled_by`), target concept, meaning and conditions. Endpoints are concept IDs only.
- **Ambiguities** (`governance/ambiguity-register.md`): the word, the distinction to make, the reviewer, affected IDs, status; the proposed answer is a `### LD-Annnn` paragraph after the table. A proposed answer is not a decision.
- **Domains** (`governance/review-domains.md`): for each of the ten domains its page name, wave, owner role, reviewer roles, **primary concepts** (exactly one domain per concept) and concepts **also shown**; the page content (why it matters, generic sequence, backlog); the questions put to each reviewer role.
- **Decisions and questions** (`governance/decision-log.md`, `governance/open-questions-for-owner.md`): what the sponsor and owners decided, and what is still open.

### Generated pages and workbooks

`python3 tools/build_domain_views.py` reads all the registers and writes, for each domain, `domains/<d>/README.md` (the domain page), `concepts.md` (one card per concept: definition, example, not to confuse with, relationships, aliases, status) and `review.md` (the review sheet), plus `domains/README.md` and `glossary.md`. With `--check` it rebuilds in memory and fails if a file on disk differs or a concept does not have exactly one primary domain.

`python3 tools/build_question_workbooks.py` writes `domains/<d>/questions-for-experts.xlsx` from `company-questions.md`, the reviewer questions and the open ambiguities of the domain. It keeps everything experts typed (matched by question reference) and stops rather than lose an answer whose question disappeared.

### Agent layer

| Piece | Role |
|---|---|
| `AGENTS.md` | The rules and procedures every agent reads first (OpenCode and Roo Code load it automatically) |
| `.agents/skills/<d>-expert/SKILL.md` | One expert per domain: scope, distinctions, venue and regime differences, pitfalls, review checklist, lifecycle, words, what to ask |
| `.opencode/agents/` | Reviewer subagents for cross-reviews (domain reviewer, cross-checker, supervisor) |
| `.opencode/commands/`, `.roo/commands/` | The same slash commands in both tools |
| `.roomodes`, `.roo/rules/` | Roo Code modes and a pointer to `AGENTS.md` |
| `.review-notes/` | Working notes of agents; not committed |

### Collaboration layer

| Piece | Role |
|---|---|
| `.gitattributes` + `tools/merge_answers.py` | Git merges two versions of a workbook answer by answer; same cell changed twice becomes `CONFLICT` |
| `tools/setup_computer.py` | Registers that merge once per clone |
| `tools/pr_scope.py` | Before a merge: domains touched, owners to approve, shared files, duplicate new IDs |
| `tools/weekly_report.py` | Weekly report of merged changes in `reports/weekly/` |
| `governance/experts.md` | Domain owners and experts |

## 3. How to change things safely

Every change: on a branch, edit the hand-written sources only, rebuild, `--check`, add a change-log line, pull request. Then:

| You want to | Edit | Then |
|---|---|---|
| Clarify a definition | Its row in `foundation.md` | Rebuild. Say "clarification" in the change log |
| Change a meaning | Its row, after the owner (or sponsor across domains) agreed | Rebuild; record the decision in the decision log; say "meaning change" in the change log |
| Add a concept | New row with the next ID (`next_ids.py`); summary, aliases and context in the annotations; relationships; primary domain in `review-domains.md` | Rebuild; `pr_scope.py` checks the ID is not taken twice |
| Retire a concept | Keep the row, say "Deprecated, replaced by …" in the definition; move relationships | Never delete or reuse the ID |
| Add an alias | Aliases table in the annotations | Rebuild |
| Record an ambiguity | New row and proposed-answer paragraph in the ambiguity register | Rebuild; the workbooks show it in sheet 3 after `build_question_workbooks.py` |
| Add questions for the firm | `domains/<d>/company-questions.md` | `build_question_workbooks.py`, then rebuild |
| Move a concept to another domain | Its ID between "Primary concepts" cells in `review-domains.md` | Rebuild; tell both owners |
| Change owners or reviewers | `review-domains.md` (roles), `experts.md` (names) | Rebuild |
| Teach the agents something | One plain sentence in `AGENTS.md`, or in the domain skill | Test it with `/ask` on a case that went wrong |

### Keeping the tables machine-readable

- One row per ID, no `|` inside a cell, no line breaks inside a cell.
- Never rename or reorder a column header: the tools find tables by their headers (for example "Working business definition", "Relation", "Affected IDs", "Primary concepts").
- Add a column only at the end and only after checking `tools/build_domain_views.py` (function `load`).
- Ranges such as "LD-C0031 to LD-C0042" are allowed in `review-domains.md` only.

## 4. Routine maintenance

| When | What | How |
|---|---|---|
| Every change | Checks pass | `/check` |
| Before each merge | Scope and duplicate IDs | `/scope` |
| Weekly | Report of merged changes, shared with the owners | `/weekly-report`, then commit `reports/weekly/<date>.md` |
| Monthly | Stale branches deleted; open pull requests chased; open questions reviewed with the sponsor | Repository service; `governance/open-questions-for-owner.md` |
| Each release | Change log section renamed from "Unreleased" to the version and date; tag created | `CHANGELOG.md`, tag in the repository service |
| When a tool is updated | Workbooks and pages rebuilt and checked | `build_question_workbooks.py`, `build_domain_views.py --check` |

## 5. When something goes wrong

| Symptom | Cause and fix |
|---|---|
| `--check` says a page is stale | Someone edited a register without rebuilding, or edited a generated page. Run `python3 tools/build_domain_views.py` and commit the result |
| `--check` says a concept has no primary domain | A new concept was not added to `review-domains.md`; add it to exactly one domain |
| A page shows a raw ID instead of a name | The ID is not in the catalogue (typo, or a concept not yet added) |
| Conflict on generated pages when merging the main branch | Take either side, then rebuild: generated pages are never merged by hand |
| Conflict on a workbook | Run `python3 tools/setup_computer.py` once, then `git pull origin main` again; resolve cells marked `CONFLICT` in Excel |
| `build_question_workbooks.py` stops | An answered question no longer exists. Copy the answer to the right question by hand, or use `--force` to drop it on purpose |
| `pr_scope.py` reports a duplicate ID | Two branches took the same new ID. Renumber the new IDs of the branch not yet merged |
| The agent ignores a rule | Add one plain sentence to `AGENTS.md`; start a new session; keep tasks smaller |
| The agent cannot read files or run commands | Tool calling is off on the model server, or the agent was started outside the repository folder |

## 6. Python and dependencies

The tools need Python 3 and `openpyxl` only. `build_domain_views.py`, `pr_scope.py` and `next_ids.py` use the standard library; the workbook tools and the weekly report need `openpyxl`. There is no build server: the checks run on each contributor's computer, and an optional automated check in the repository service can run `python3 tools/build_domain_views.py --check` on each pull request.
