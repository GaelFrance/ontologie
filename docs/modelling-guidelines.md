# Modelling guidelines

Status: Draft

## Identity and types

Use immutable concept IDs `LD-C0001` onward. Do not encode domain or mutable names in IDs. Relationship IDs use `LD-R`; ambiguity IDs use `LD-A`. Never reuse a retired ID.

Concept types, with the working definitions adopted on 2026-11-01 (review 08):

| Type | Definition |
|---|---|
| Entity | Thing with a persistent identity independent of any single event. |
| Role | Contextual, time-bounded function held by a party in a relationship, service or arrangement. |
| Agreement | Arrangement creating rights and obligations between identified parties. |
| Instruction | Request to act; can be accepted, rejected, amended or cancelled. |
| Event | Dated occurrence; corrections are new events referencing the original. |
| Process | Coordinated instructions and events directed at an outcome. |
| State | Condition holding over an interval or at an as-of time. |
| Obligation | Duty of a debtor toward a creditor with due terms. |
| Measure | Quantity determined under a stated method, scope, time and unit. |
| Reference Concept | Governed classification, rule or specification, usually versioned. |

Type assignments in the catalogue are proposals requiring review. A Measure is not settled or secured; obligations are. Classes are not declared disjoint: one object may carry two classifications if it is counted once.

## Business objects and records

A business object (for example a Trade, Position, Account or give-up) has one identity. Sources hold records of it, each with its own identifiers, version, status values and record time; a trade record is a representation of the trade, not the trade. Several records can represent one object: a difference between them is a discrepancy to reconcile, not a second object. No identifier *is* the identity; identifiers are unique only within their scheme's scope. Statuses are assertions by a stated source about an object, valid over a period; native status values are kept beside any harmonised value, and "unknown" (no record) is never shown as another status.

## Time convention

Time-varying facts carry **valid time** (effective period, business date by date role) and **record time** (when the source recorded the fact and when it was received). In questions and answers:

- **current** means valid now, using the latest non-superseded record from the stated source;
- **as of D** means valid at business date D;
- **as known at T** means using only records received by T.

Corrections supersede, cancellations end validity, nothing is deleted. Every answer states its source, as-of date and freshness. Event timestamps are kept in UTC beside business dates; business dates are resolved against a named business calendar and time zone. Regulatory classifications follow the same pattern ("unknown" is a value, never a default).

Do not confuse classes with instances: Central Counterparty is a concept, a named CCP legal entity is an instance participating in that role.

## Hierarchy and relationships

Use `is_a` only when every instance of the child meets the parent's definition. Distinguish it from `part_of`, `plays_role`, temporal succession and mere relatedness. Derive child lists from parent references in a future machine-readable model. Multiple parents require justification.

Define each relationship once in the relationship register. Include source/target types, meaning, applicability, context qualifiers and cardinalities when validated. Do not assert universal cardinalities from a single workflow. N-ary and time-dependent relationships should be represented by contextual assignments/events, not flattened into unqualified binary edges.

## Labels and monetary semantics

Aliases must be marked exact, contextual or ambiguous, with their scope; an ambiguous alias returns candidates, never a single concept. Concepts whose meaning is deferred carry the resolution flag `blocked-pending-decision`. Until concept fiches exist, aliases, flags, specialisations, required context and French labels are kept in [concept annotations](../ontology/concept-annotations.md). Commission, brokerage, fees and revenue are not global synonyms.

Record debtor, creditor and service for a charge. Record payer/payee for a cash movement. A collecting party need not be the economic beneficiary. A source's positive/negative sign is not a business definition. Reversals must reference the original economic event and their own effect.

## Authoring

Use the [concept template](../templates/concept-template.md). Preserve all fields; write `Not applicable — reason` or `To validate — question` rather than silently omitting unresolved information. The catalogue deliberately contains short definitions only; full template completion belongs to Phase 2.

Keep the registers machine-readable: one row per ID in the catalogue, no `|` inside a table cell, new columns appended only after checking how the hub reader parses that table, and temporary IDs (`NEW-…`) never in a register. Relationship endpoints use concept IDs only; a union of targets is written `LD-Cnnnn / LD-Cnnnn` and is an explicit declared range. Tagging a document with a concept ID is an annotation, not an instance relationship.
