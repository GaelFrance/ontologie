# Modelling guidelines

Status: Draft

## Identity and types

Use immutable concept IDs `LD-C0001` onward. Do not encode domain or mutable names in IDs. Relationship IDs use `LD-R`; ambiguity IDs use `LD-A`. Never reuse a retired ID.

Initial concept types: Entity, Role, Agreement, Instruction, Event, Process, State, Obligation, Measure, Reference Concept. Type assignments in the foundation are proposals requiring review. For example, Trade may be represented as an Agreement, while a trade record is a representation of that agreement.

Do not confuse classes with instances: Central Counterparty is a concept, a named CCP legal entity is an instance participating in that role.

## Hierarchy and relationships

Use `is_a` only when every instance of the child meets the parent's definition. Distinguish it from `part_of`, `plays_role`, temporal succession and mere relatedness. Derive child lists from parent references in a future machine-readable model. Multiple parents require justification.

Define each relationship once in the relationship register. Include source/target types, meaning, applicability, context qualifiers and cardinalities when validated. Do not assert universal cardinalities from a single workflow. N-ary and time-dependent relationships should be represented by contextual assignments/events, not flattened into unqualified binary edges.

## Labels and monetary semantics

Aliases must be marked exact, contextual or ambiguous, with their scope. Commission, brokerage, fees and revenue are not global synonyms.

Record debtor, creditor and service for a charge. Record payer/payee for a cash movement. A collecting party need not be the economic beneficiary. A source's positive/negative sign is not a business definition. Reversals must reference the original economic event and their own effect.

## Authoring

Use the [concept template](../templates/concept-template.md). Preserve all fields; write `Not applicable — reason` or `To validate — question` rather than silently omitting unresolved information. The foundation catalogue deliberately contains short definitions only; full template completion belongs to Phase 2.
