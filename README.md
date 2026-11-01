# Derivatives Business Ontology

The shared business vocabulary for **listed derivatives execution, ETD clearing and OTC client clearing**: what each business word means, how the ideas connect, and which questions are still open. People use it to agree on meanings; AI agents use it to answer questions without guessing.

**Stage:** Phase 2 in progress. 222 concepts in ten business domains (74 foundation concepts and 148 more detailed ones added in the November 2026 domain review). Every definition is **Draft** until its domain owner approves it.

## Start here

| If you want to… | Go to |
|---|---|
| Understand a business area | **[Domains](domains/README.md)**: one folder per area, starting with an overview in plain words |
| Look up a word | **[Glossary](glossary.md)**: every concept A to Z, plus the informal words people use |
| Review definitions as an owner or reviewer | The **review sheet** in your domain's folder |
| Explain how our firm works | The **questions for our firm** in each domain's folder (answers stay outside this repository) |
| See what was decided | [Decision log](governance/decision-log.md) and [open questions for the sponsor](governance/open-questions-for-owner.md) |

## The ten domains

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

Each domain folder holds the same four pages: **overview** (plain words), **concepts** (one card per concept with a definition, an example and what not to confuse it with), **review sheet** (what each reviewer is asked) and **questions for our firm**.

## How it is organised

- **`domains/`** is what people read. The overview and the questions for our firm are written by hand; the concept cards, review sheets, domain pages and the glossary are generated from the registers by `tools/build_domain_views.py`, so they always agree.
- **`ontology/`, `relationships/`, `governance/`** hold the registers: the catalogue of concepts, their annotations, the connections between them, the open questions on meaning and the decisions. They are the single source of truth and are maintained by the Ontology Lead; reviewers do not need to open them. See [ontology/README.md](ontology/README.md).
- **`.claude/skills/`** holds one expert skill per domain, used by AI agents that review or use this ontology.
- **`docs/`** explains the principles, scope, modelling rules and governance.

Concept references such as *LD-C0022* exist so that tools and agents can point to a concept without ambiguity. Human pages show names first and keep references in small print.

## Rules that always apply

- **Business meanings only.** No firm-specific facts, client names, internal system names or data. How our firm works is captured through the questions for our firm, and the answers live in the internal workspace.
- **Phase gates.** Phase 2 (concepts) is authorised. Metric formulas, detailed taxonomies, links to source systems and worked question-to-answer demonstrations come in later phases.
- **Markdown is the reference.** Machine-readable exports are generated, never edited by hand. English only.
- **Governance.** Domain owners approve meanings in their domain; the sponsor arbitrates across domains; the Ontology Lead maintains the registers. See the [governance model](governance/governance-model-proposal.md).

## More

- [Scope](docs/scope.md), [architecture](docs/architecture.md), [principles](docs/principles.md), [modelling guidelines](docs/modelling-guidelines.md), [governance](docs/governance.md)
- Reviews: [2026-11 expert review](governance/reviews/2026-11-expert-review/ARBITRATION.md), [classification review](governance/reviews/2026-11-classification-review/ARBITRATION.md), [level-2 domain review](governance/reviews/2026-11-level2-domain-review/SUPERVISION.md)
- [Taxonomy design](taxonomies/README.md), [questions the ontology must eventually support](examples/natural-language-queries.md), [future mapping method](mappings/README.md)
- [How to contribute](CONTRIBUTING.md) and [change history](CHANGELOG.md)
