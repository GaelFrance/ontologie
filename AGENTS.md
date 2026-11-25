# Instructions for AI agents working in this repository

This file is read automatically by OpenCode, Roo Code and other coding agents. It tells you what this repository is, the rules you must never break, and the exact steps for the usual tasks. Follow it even if the model you run on has not seen this project before.

## 1. What this repository is

A governed business ontology for listed derivatives execution, ETD clearing and OTC client clearing: what each business word means, how concepts connect, and which questions are still open. It is Markdown only. People read the pages in `domains/`; AI agents use the registers to answer questions without guessing.

The person you work for is usually the **Ontology Lead**, who maintains the registers and assigns IDs. Domain owners approve meanings; the sponsor arbitrates across domains. **Nothing you do approves a meaning.** Every definition is Draft until its owner approves it, and that approval is recorded by a person in the decision log.

Read before your first change: `README.md`, `docs/architecture.md`, `docs/modelling-guidelines.md` and `docs/governance.md`.

## 2. Where things are

| Path | What it holds | Edit? |
|---|---|---|
| `ontology/foundation.md` | Concept catalogue: one row per concept ID (LD-C) with name, module, type, definition (and level and domain for level-2 rows) | Yes, by hand |
| `ontology/concept-annotations.md` | Specialisations, resolution flags, aliases, required context, usage notes, priority and alignment, plain-language summaries, values | Yes, by hand |
| `relationships/relationships.md` | Relationships between concepts (LD-R) | Yes, by hand |
| `governance/ambiguity-register.md` | Ambiguous words and open meaning questions (LD-A) | Yes, by hand |
| `governance/review-domains.md` | The ten domains, owners, reviewers, primary and "also shown" concepts, backlog | Yes, by hand |
| `governance/decision-log.md`, `governance/open-questions-for-owner.md` | Decisions taken and questions for the sponsor | Only to record what a person decided or asked |
| `domains/<domain>/overview.md`, `domains/<domain>/company-questions.md` | Hand-written introduction and questions for our firm | Yes, by hand |
| `domains/<domain>/README.md`, `concepts.md`, `review.md`, `domains/README.md`, `glossary.md` | **Generated** pages | **Never by hand.** Rebuild them |
| `domains/<domain>/questions-for-experts.xlsx` | **Generated** interview workbook; experts fill in the answers | Rebuild only with the tool, which keeps the answers already entered |
| `.agents/skills/<domain>-expert/SKILL.md` | One expert skill per domain | Only when asked |
| `tools/` | `build_domain_views.py`, `build_question_workbooks.py`, `next_ids.py` | Only when asked |

The ten domain folder names are: `parties-and-roles`, `instruments-venues-and-calendars`, `service-offering-and-market-access`, `execution`, `clearing-give-up-and-acceptance`, `clearing-services-and-accounts`, `margin-and-collateral`, `fees-revenue-and-contribution`, `regulation-and-rule-changes`, `post-trade-operations`. The matching skill is `<domain>-expert` (for example `execution-expert`).

## 3. Rules you must never break

1. **English only** in every file.
2. **Business meanings only.** No firm-specific facts, client names, internal system names, internal pricing, positions or source mappings in definitions, annotations or examples. Examples are synthetic (Client A, Executing Broker X, Clearing Broker Y, CCP Z, Venue V). How our firm works goes into the questions for our firm and the answers in the expert workbooks, never into definitions.
3. **Phase gates.** Phase 2 (concepts) is authorised. Do not write metric formulas, calculations, detailed taxonomies (list values on a concept instead), links to source systems or worked question-to-answer demonstrations.
4. **IDs are permanent.** Never renumber, reuse or delete an ID, including a retired one. Never put a temporary ID (`NEW-…`) in a register. Get new IDs only from `python3 tools/next_ids.py` and only when the Ontology Lead asked you to apply the change.
5. **No silent meaning change.** A change of scope, type or rule is a *meaning change*: list it for the sponsor in `governance/open-questions-for-owner.md` unless the person tells you it was decided. Better wording with the same meaning is a *clarification*.
6. **Never write a decision or an approval** that a person did not state. Never change a status to Reviewed or Approved on your own.
7. **Keep the tables parseable:** one row per ID, no `|` inside a cell, never reorder or remove columns. Downstream tools read `ontology/foundation.md`, `ontology/concept-annotations.md`, `relationships/relationships.md` and `governance/ambiguity-register.md`.
8. **Do not edit generated files.** Change the registers, then rebuild.
9. **Words that are blocked:** "transaction" and "commission" never resolve to one concept. List the candidates and ask.
10. **Record every change** in `CHANGELOG.md` under "Unreleased", one short bullet saying what changed and whether any meaning changed.

## 4. Checks to run

Run both after any change to a register or a hand-written page, and fix every failure before you say the work is done:

```bash
python3 tools/build_domain_views.py          # rebuild the generated pages
python3 tools/build_domain_views.py --check  # must print nothing and exit 0
```

If you changed `company-questions.md` or the review questions, also run `python3 tools/build_question_workbooks.py` (needs `openpyxl`). It keeps the answers already entered; if it stops because an answer no longer matches a question, tell the person and never use `--force` unless they ask. Show the person the output of the checks; never claim a check passed without running it.

## 5. How to do the usual tasks

Work on **one domain at a time** and read only the files you need. The registers are long; search them (grep for the ID or the name) instead of reading them whole.

### Answer a business question
1. Load the skill of the domain the question belongs to.
2. Find the concepts by name and alias (`glossary.md`, then the Aliases section of `ontology/concept-annotations.md`).
3. If a word is ambiguous (see the skill's "Words people use" section and the ambiguity register), list the candidate meanings and ask which one is meant.
4. Answer in plain words, naming concepts first and giving the ID in brackets. Say which context you assumed (venue, CCP, regime, date role; default date role is the CCP clearing date).

### Review a domain (one expert)
1. Load `<domain>-expert`. Read `domains/<domain>/concepts.md` and `domains/<domain>/review.md`.
2. Apply the skill's review checklist to each concept: write *OK*, *Clarify* (with proposed wording) or *Meaning change* (with the reason).
3. Write the findings to `.review-notes/<yyyy-mm-dd>-<domain>.md` (this folder is not committed). Do not edit the registers during a review.

### Cross-review (several experts, then a supervisor)
1. One reviewer per domain as above, each in its own context (in OpenCode use the `domain-reviewer` subagent; in Roo Code the Orchestrator with the "Domain reviewer" mode).
2. The `cross-checker` reads the findings of all domains and looks for conflicts between domains, duplicate concepts, broken relationships and concepts shown in several domains whose owners disagree.
3. The `review-supervisor` consolidates everything into one decision list for the Ontology Lead: clarifications ready to apply, meaning changes for the sponsor, new concepts proposed, questions for the firm. It applies nothing.

### Apply an agreed change
1. Confirm the list of changes the person agreed to. Apply only those.
2. New concept: run `python3 tools/next_ids.py`; add a catalogue row in the right section of `ontology/foundation.md` (level-2 rows also fill Level and Domain); add its summary, aliases and required context in `ontology/concept-annotations.md`; add its relationships; list it as primary in exactly one domain in `governance/review-domains.md`.
3. Changed definition: edit the row in place, keep the ID; note in the change log whether it is a clarification or a meaning change.
4. Rebuild and check (section 4). Add the change-log bullet.
5. Commit on a branch with a message that names the IDs changed. Do not push to the main branch.

### Record answers from the firm
Answers go into the domain's `questions-for-experts.xlsx` workbook (filled by the experts). If an answer shows a definition is wrong, propose a change as above; do not paste firm facts into definitions.

## 6. When you are unsure

Stop and ask the person. Asking is always better than inventing a meaning, an ID, a source, a regulatory reference or an approval. Say "to verify" for any rule, section number or URL you have not checked.
