# Architecture

Status: Draft

## Five distinct assets

| Asset | Purpose |
|---|---|
| Business glossary | Definitions, labels and usage notes for humans |
| Taxonomy | Classification along explicitly defined axes |
| Business ontology | Concepts, identity boundaries, typed relationships and constraints |
| Semantic layer | Governed question and metric interpretation: population, grain, dimensions, time, units, aggregation and exclusions |
| Physical mapping | Later correspondence to actual source fields, APIs and transformations |

```text
Natural-language question
    -> concept and context resolution
    -> ontology relationships and semantic contracts
    -> appropriate domain / data product
    -> authorised access interface (API, MCP or query service)
    -> physical source
```

The last three implementation stages require future source and service information. MCP is an interface, not the ontology or its source of truth.

## Modules and dependencies

Common contains reusable meanings. Execution, ETD Clearing and OTC Clearing specialise or apply them without duplicating them. Owning domain identifies stewardship; applicable domains identify use. Common concepts must not depend on an application-specific or domain-specific implementation.

## Business context

A context can identify service/domain, observing legal entity, participant roles, contractual relationship, account, CCP/venue, jurisdiction, business date, effective period and management measurement basis (the current revenue priority). Require only relevant dimensions. Context cannot silently redefine a concept: materially different meanings need separate concepts.

Model a party separately from a role assignment. Party Role (LD-C0003) is the role assignment (party-in-role): it relates a party to a role kind, counterparties, a service (Clearing Service or Service Offering), an agreement where applicable, and an effective period; role kinds such as Client or Clearing Member are its specialisations. An entity can hold multiple roles simultaneously. Client is a role; Legal Entity is an entity type. Entity-level regulatory statuses attach to the legal entity, relationship-level statuses to the role assignment, never to a commercial group.

Trading Venue is distinct from its legal operator. CCP and Clearing Member are roles in a defined Clearing Service, which is distinct from the Service Offering a provider sells to clients. An account's owner, operator, beneficiary and reporting attribution must not be inferred from its label.

## Formats

Markdown is canonical during foundation review. Stable IDs and consistent tables/templates make migration possible without claiming that free text is already executable logic. If YAML is later approved, introduce schemas and validators, preserve IDs, and generate human-readable concept pages from that single source. Do not maintain two independent canonical definitions.

SKOS/OWL exports may be evaluated later; no graph database or ontology runtime is selected now.

## Reference values

Currencies, units and date roles require governed reference policies and remain vocabularies, not concepts. Business Calendar became a concept (LD-C0066) in the 2026-11 review because circulars change calendars and cut-offs are expressed against them; individual calendars are instances. Currency of charge, payment, collateral and reporting must be distinguished. Business dates require a date role and relevant calendar/time-zone conventions.
