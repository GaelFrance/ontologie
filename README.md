# Derivatives Business Ontology

The shared business vocabulary for **listed derivatives execution, ETD clearing and OTC client clearing**: what each business word means, how the ideas connect, and which questions are still open. People use it to agree on meanings; AI agents use it to answer questions without guessing.

**Stage:** Phase 2 in progress. 252 concepts in eleven business domains (74 foundation concepts, 156 more detailed ones added in the November 2026 domain review and 22 in the risk domain opened on 2026-11-26). Every definition is **Draft** until its domain owner approves it.

## Start here

| If you want to… | Go to |
|---|---|
| Understand a business area | **[Domains](domains/README.md)**: one folder per area, starting with an overview in plain words |
| Look up a word | **[Glossary](glossary.md)**: every concept A to Z, plus the informal words people use |
| Review definitions as an owner or reviewer | The **review sheet** in your domain's folder |
| Explain how our firm works | The **questions for our firm** in each domain's folder (answers are recorded in the domain's expert workbook; see the [contributor guide](docs/contributor-guide.md)) |
| See what was decided | [Decision log](governance/decision-log.md) and [open questions for the sponsor](governance/open-questions-for-owner.md) |
| Contribute as an owner or expert | **[Contributor guide](docs/contributor-guide.md)**: what each role does, in OpenCode or VS Code with Roo Code |
| Maintain the repository | [Architecture and maintenance guide](docs/maintenance-guide.md) and the [weekly reports](reports/weekly/) |

## The eleven domains

| Domain | In one line |
|---|---|
| [Parties, roles, clients and accounts](domains/parties-and-roles/README.md) | Who is involved, in which role, toward whom, and in which account |
| [Instruments, venues and calendars](domains/instruments-venues-and-calendars/README.md) | What is traded, where, and on which dates |
| [Service offering and market access](domains/service-offering-and-market-access/README.md) | What we sell and how clients reach venues and clearing houses |
| [Listed derivatives execution](domains/execution/README.md) | From the client's order to the allocated trade |
| [Clearing: give-up and acceptance](domains/clearing-give-up-and-acceptance/README.md) | Handing a trade to the clearing broker and the clearing house accepting it |
| [Clearing: services, accounts and client clearing](domains/clearing-services-and-accounts/README.md) | Clearing services, memberships, client clearing models, accounts and positions |
| [Margin and collateral](domains/margin-and-collateral/README.md) | What must be posted, called and held, at the clearing house and with clients |
| [Fees, revenue and contribution](domains/fees-revenue-and-contribution/README.md) | What we charge, what we pay away and what a client brings in |
| [Regulation and rule changes](domains/regulation-and-rule-changes/README.md) | Rules, regimes and the changes announced by regulators, venues and clearing houses |
| [Post-trade operations](domains/post-trade-operations/README.md) | Lifecycle events, settlement, deadlines, reconciliations and breaks |
| [Risk: client clearing, execution and CCP risk](domains/risk/README.md) | What we could lose on the clients we clear, in execution and at the clearing houses, and the limits and default rules that apply |

Each domain folder holds the same four pages: **overview** (plain words), **concepts** (one card per concept with a definition, an example and what not to confuse it with), **review sheet** (what each reviewer is asked) and **questions for our firm**.

## How it is organised

```text
domains/<domain>/     what people read: overview and questions for our firm (hand-written);
                      domain page, concept cards and review sheet (generated);
                      questions-for-experts.xlsx (blank interview workbook, generated)
glossary.md           every concept A to Z (generated)
ontology/             the registers: foundation.md (catalogue, one row per concept)
                      and concept-annotations.md (aliases, summaries, context, values)
relationships/        relationships.md: how concepts connect
governance/           ambiguity register, review domains (owners, reviewers, backlog),
                      decision log, open questions, governance model proposal
docs/                 architecture, scope and principles; modelling guidelines;
                      governance and contributing
tools/                build_domain_views.py, build_question_workbooks.py, read_answers.py,
                      merge_answers.py, pr_scope.py, weekly_report.py,
                      setup_computer.py, next_ids.py
reports/weekly/       weekly reports of the changes merged
.agents/skills/       one expert skill per domain, for AI agents
AGENTS.md             rules and procedures for AI coding agents (OpenCode, Roo Code);
                      see docs/working-with-ai-agents.md
```

The registers are the single source of truth, maintained by the Ontology Lead; reviewers do not need to open them. Everything generated is rebuilt by `python3 tools/build_domain_views.py` and `python3 tools/build_question_workbooks.py` (needs openpyxl; it keeps the answers already entered); `build_domain_views.py --check` fails when a page is stale or a concept has no domain. References such as *LD-C0022* (concepts), *LD-R* (relationships) and *LD-A* (ambiguities) are permanent and never reused; human pages show names first. Downstream tools read the tables in `ontology/foundation.md`, `ontology/concept-annotations.md`, `relationships/relationships.md` and `governance/ambiguity-register.md`, so their layouts should stay stable.

## Rules that always apply

- **Business meanings only.** No firm-specific facts, client names, internal system names or data. How our firm works is captured through the questions for our firm, and the answers are recorded in each domain's expert workbook; definitions stay generic.
- **Phase gates.** Phase 2 (concepts) is authorised. Metric formulas, detailed taxonomies, links to source systems and worked question-to-answer demonstrations come in later phases.
- **Markdown is the reference.** Machine-readable exports are generated, never edited by hand. English only.
- **Governance.** Domain owners approve meanings in their domain; the sponsor arbitrates across domains; the Ontology Lead maintains the registers. Nothing is approved yet: every definition is Draft.

## More

- [Architecture, scope and principles](docs/architecture.md), [modelling guidelines](docs/modelling-guidelines.md), [governance and contributing](docs/governance.md)
- [Contributor guide](docs/contributor-guide.md), [architecture and maintenance guide](docs/maintenance-guide.md), [working with AI agents](docs/working-with-ai-agents.md)
- [Change log](CHANGELOG.md). Earlier review reports (2026-11 expert, classification and level-2 reviews) are in the repository history; their outcomes are in the registers and the decision log.
