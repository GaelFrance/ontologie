# Architecture, scope and principles

Status: Draft

## Scope

| Domain | In scope |
|---|---|
| Listed Derivatives Execution | High-touch and electronic execution; orders, fills, instruments, venues, clients and accounts; brokers; revenue and costs; allocation, average pricing, give-up; corrections and cancellations; reporting; connectivity, routing, algorithms and market access; exceptions and reference data |
| ETD Clearing | Client clearing; CCP/member/broker relationships; registration and take-up; accounts and segregation; positions, margin, collateral and relevant default-fund concepts; fees and brokerage; settlement, cash movements, expiry, exercise, assignment and transfers; reconciliation, exceptions and reporting |
| OTC Clearing | Client clearing of IRS and other eligible OTC derivatives; submission, acceptance and legal transformations; accounts, positions, segregation, margin and collateral; settlement, compression and portability; fees, reconciliation, exceptions and reporting |

Regulatory concepts are contextual and versioned by jurisdiction, regime and effective date; nothing here asserts that an obligation applies universally. The catalogue (230 concepts, all Draft) is a prioritised foundation, not a completeness claim. What each domain still lacks is listed in the "Not yet in the catalogue" column of [review domains](../governance/review-domains.md).

## Phases

1. **Foundation** (approved 2026-09-20): architecture, concept template, first 50 concepts, relationships, ambiguities.
2. **Concepts** (authorised, in progress): Common, Execution, ETD Clearing, then OTC Clearing. Management revenue first, kept apart from contribution and profitability after costs.
3. **Taxonomies**: detailed participant, product, lifecycle, fee, account, position, margin, collateral, settlement and regulatory classifications (axes and seed values in the [modelling guidelines](modelling-guidelines.md#classification-axes)).
4. **Resolution demonstrations**: natural-language questions resolved and ambiguity handling tested.
5. **Physical mappings**: only after real source schemas are supplied.

Phase 2 approval does not approve individual definitions, metric formulas, detailed taxonomies, query-resolution demonstrations or physical mappings.

## Principles

1. Meaning precedes source systems and field names.
2. Shared meanings have one identity; domain specialisations state what changes.
3. A familiar label does not prove equivalence. Scope aliases and abbreviations.
4. Separate entities, roles, instructions, events, processes, states, obligations and measures.
5. Separate trade identity from operational records and preserve lifecycle lineage.
6. Separate a fee charge, recognised revenue or cost, a settlement obligation and the actual cash movement.
7. Distinguish requirement, call, eligible collateral, posted collateral and remaining shortfall.
8. Require viewpoint, grain, time and currency before adding up money.
9. Do not infer legal effect from a technical status or assume one CCP's workflow is universal.
10. Unknown, not applicable and not yet reviewed are different states.
11. Preserve uncertainty and validation questions; do not invent precision.
12. Keep source evidence, modelling proposals and business approval distinguishable.
13. Seeing the ontology does not grant access to the underlying client, trade or financial data.

## Five distinct assets

| Asset | Purpose | Here |
|---|---|---|
| Business glossary | Definitions, labels and usage notes for humans | [glossary](../glossary.md), domain pages |
| Taxonomy | Classification along explicitly defined axes | Phase 3 |
| Business ontology | Concepts, identity boundaries, typed relationships and constraints | registers |
| Semantic layer | Governed interpretation of questions and metrics | later phase (below) |
| Physical mapping | Correspondence to actual source fields, APIs and transformations | Phase 5 |

```text
Natural-language question
    -> concept and context resolution
    -> ontology relationships and semantic contracts
    -> appropriate domain / data product
    -> authorised access interface (API, MCP or query service)
    -> physical source
```

The last three stages need future source and service information. MCP is an interface, not the ontology or its source of truth.

## Modules and context

Common holds reusable meanings; Execution, ETD Clearing and OTC Clearing specialise or apply them without duplicating them. Owning domain means stewardship; applicable domains mean use.

A context can name the service or domain, observing legal entity, participant roles, contractual relationship, account, CCP or venue, jurisdiction, business date, effective period and management measurement basis. Require only the relevant dimensions. Context cannot silently redefine a concept: materially different meanings need separate concepts.

Model a party separately from a role assignment. Party Role (LD-C0003) is the party-in-role: it relates a party to a role kind, counterparties, a service (Clearing Service or Service Offering), an agreement where applicable, and an effective period; role kinds such as Client or Clearing Member are its specialisations. One entity can hold several roles at once. Entity-level regulatory statuses attach to the legal entity, relationship-level statuses to the role assignment, never to a commercial group. Trading Venue is distinct from its operator. CCP and Clearing Member are roles in a Clearing Service, which is distinct from the Service Offering sold to clients. An account's owner, operator, beneficiary and reporting attribution are never inferred from its label.

Currencies, units and date roles are governed reference vocabularies, not concepts; Business Calendar (LD-C0066) is a concept because circulars change calendars and cut-offs are expressed against them. Currency of charge, payment, collateral and reporting must be distinguished.

## Formats

Markdown is canonical (sponsor decision, 2026-11-01) because business reviewers must be able to read it. Machine-readable exports (JSON or YAML) are generated from it and are never a second source of truth. SKOS/OWL exports may be evaluated later; no graph database or ontology runtime is selected.

## Later phases: requirements already known

**Semantic contracts.** For each future metric, state: concept references, population, grain, dimensions, observing entity, management measurement basis, time basis, currency and FX policy, sign convention, aggregation, exclusions, reversal handling, internal elimination, double-counting controls, freshness and permissions. Keep revenue, contribution after named costs, and profitability after further allocation apart; Execution Revenue is not automatically the sum of client execution fees. No formula or default deduction is approved. When a question is ambiguous, resolution returns candidate concepts and the missing context; it never picks a source or invents a metric from a label.

**Physical mappings.** Start only with real schemas: source ownership, schema version and permitted access; target concept IDs and context; grain, keys, cardinality and temporal semantics; fields, transformations, code translations, units and sign conversion; tests of completeness, duplicates, reconciliation, reversals and lineage; gaps, owner review and effective dates. A shared field name is not evidence of shared meaning.

**Competency questions** the ontology must eventually support, or answer with the missing context: execution revenue by client; brokerage paid to executing brokers; clearing fees charged to a client; exchange fees last month; top clients by revenue; trades not successfully given up; margin required for a client; a client's cleared positions at a CCP. They must distinguish revenue from fees and cash, fees paid from pass-through charges, contractual clients from commercial groups, complete from partial give-ups, CCP–member from member–client margin, and gross from net positions. The evaluation question sets live in the agent hub.

## Background sources

W3C [SKOS](https://www.w3.org/TR/skos-reference/) and [OWL](https://www.w3.org/OWL) informed the vocabulary and ontology distinction; no implementation format is selected. Public CCP documentation (for example CME allocation management and LCH SwapClear risk management) illustrates context-dependent workflows, not universal rules. None of these is a source-level validation of a definition; for any adopted rule, record the exact document, version, section, date, jurisdiction or service, and reviewer.
