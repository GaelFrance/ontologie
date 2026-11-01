# Derivatives Business Ontology

A governed business foundation for **Listed Derivatives Execution, ETD Clearing and OTC Client Clearing**.

**Stage: Phase 1 foundation approved on 2026-09-20; Phase 2 in progress after the 2026-11 expert review. Individual concept definitions remain Draft.**

The ontology is independent of any LLM, database, application, API or MCP implementation. Canonical names and repository artefacts are in English. Markdown is the canonical format, written for business readers. Any machine-readable form (JSON or YAML) is generated automatically from the Markdown and is never edited or reviewed by hand (sponsor decision, 2026-11-01).

## Start here: review by domain

**[One page per business domain](domains/README.md)**: parties and roles, products and reference data, execution, clearing, margin and collateral, fees and revenue, regulation, post-trade operations. Each page gathers the definitions, connections, open ambiguities with proposed answers, decisions taken, and what the reviewer is asked. Give each reviewer the page of their domain.

> **En bref (FR)** — Pour relire l'ontologie, commencer par le dossier [`domains/`](domains/README.md) : une page par domaine métier, avec les définitions et ce qu'il faut vérifier.

## Review the foundation

1. [Scope and phase boundaries](docs/scope.md)
2. [Architecture and modelling choices](docs/architecture.md)
3. [Concept catalogue (74 concepts)](ontology/foundation.md) and [concept annotations](ontology/concept-annotations.md) (aliases, specialisations, required context)
4. [Relationships](relationships/relationships.md)
5. [Taxonomy design](taxonomies/README.md)
6. [Ambiguities, affected concepts and proposed answers](governance/ambiguity-register.md)
7. [Open questions for the business owner](governance/open-questions-for-owner.md)
8. [Concept template](templates/concept-template.md)
9. [Exact repository structure](docs/repository-structure.md)

## Decisions and reviews

- [Phase 1 sponsor review](governance/phase-1-review.md) and [decision log](governance/decision-log.md) (sponsor answers of 2026-11-01)
- [2026-11 expert review and arbitration](governance/reviews/2026-11-expert-review/ARBITRATION.md)

## Maintenance

- [Principles](docs/principles.md), [modelling guidelines](docs/modelling-guidelines.md) and [governance](docs/governance.md)
- [Contribution process](CONTRIBUTING.md) and [change history](CHANGELOG.md)
- [Semantic contracts](semantic-layer/README.md) and [future mapping methodology](mappings/README.md)
- [Questions the ontology must eventually support](examples/natural-language-queries.md)

## Approval boundary

The sponsor approved the foundation and development sequence; see the [review decision](governance/phase-1-review.md). Phase 2 may develop Common, Execution, ETD Clearing and OTC Clearing in that order. Individual definitions remain Draft.

Revenue modelling now prioritises business performance and client contribution analysis, with revenue distinguished from contribution and profitability after costs; revenue is attributed per service (sponsor decision 2026-11-01). Commission and Transaction remain unresolved. No physical mappings, production data, executable metrics or detailed domain expansion are included in this foundation.
