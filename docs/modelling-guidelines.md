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

What an agent knows about a fact is kept apart from the fact itself. For each fact an answer relies on, the agent states one knowledge state: **observed** (a valid record from the stated source), **missing** (no record received where one is expected), **stale** (the latest record is older than the freshness the question needs), **conflicting** (valid sources disagree; reported as a break, never resolved by choosing one silently) or **not applicable**. A business value of "unknown" asserted by a source is different again: it is an observed value. A missing or stale record never allows the agent to assert a business state, nor to deny that an event took place. Links between objects are also kept apart: **same business object** (several records of one object), **successor** (an object created from another, for example by clearing, give-up registration or porting) and **economically related** (for example the same instrument or the same client); a shared instrument identifier or product identifier never proves that two trades are the same.

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

The catalogue deliberately holds short definitions; the other facts about a concept live in the annotations and are shown on the generated concept cards. A complete concept record covers these fields (key names in backticks are fixed for tooling): ID; canonical English name; business definition; owning and applicable domains; concept type; aliases (`aliases`, marked exact, contextual or ambiguous with scope); abbreviations; parents (`parents`, justified is_a); identity criteria and identifier schemes (`identity`); temporal pattern (`temporal_pattern`); required context (`required_context`); resolution (`resolution`); relationships; business rules; calculation (or Not applicable; never invented); unit and currency; sign convention and observing party; examples (synthetic) and counterexamples; ambiguities; sensitivity; owner; status; standard alignments (`alignments`, `verified: false` until checked); competency questions served; sources and decisions; version and effective period; validation questions. Write `Not applicable — reason` or `To validate — question` rather than silently omitting a field.

Keep the registers machine-readable: one row per ID in the catalogue, no `|` inside a table cell, new columns appended only after checking how the hub reader parses that table, and temporary IDs (`NEW-…`) never in a register. Relationship endpoints use concept IDs only; a union of targets is written `LD-Cnnnn / LD-Cnnnn` and is an explicit declared range. Tagging a document with a concept ID is an annotation, not an instance relationship.

## Classification axes

Detailed taxonomies are Phase 3 work. Use several axes rather than one artificial tree; separate is_a specialisations from contextual categories and overlapping facets; assume no disjointness or exhaustiveness without review. Cleared is not exchange-traded, and regulatory "OTC" is not off-venue (LD-A0032). High-touch or low-touch describes a handling channel, not an asset class or venue. A charge's classification does not decide its accounting recognition. Named markets, entities and currencies are instances, not subclasses.

| Taxonomy | Proposed axes |
|---|---|
| Participants | Party type; service role; contractual role; membership category; client segment |
| Products | Asset class; derivative family; contractual form; trading mode; clearing eligibility; regulatory product class |
| Orders, executions, trades | Instruction type; order handling channel (LD-C0061); execution method; trading capacity; order type; time in force; strategy; event; lifecycle state; clearing tier |
| Fees | Service; service nature; chargeable event; debtor; creditor; collector; beneficiary; tariff basis; pass-through treatment; amount certainty; billing stage; recurrence; incentive programme |
| Accounts | Function; maintaining party; holder; recording level; CCP account type; segregation regime |
| Positions | Scope; gross or net; direction; status; as-of basis |
| Margin | Type; component; tier (provider and taker); risk scope; run type; VM treatment; margining basis; calculation and call frequency |
| Collateral | Asset class; currency; cash or non-cash; legal form; eligibility; valuation basis; mobilisation state |
| Settlement | Cash or physical; obligation; method; due date; status |
| Post-trade lifecycle | Event; transition; economic effect; legal effect; interposition mechanism |
| Regulatory | Jurisdiction; regime; obligation; responsible role; attachment level; classification basis; date role |
| Access | Access model; scope (venue or clearing service); intermediary; status |
| Costs | Cost category |

Draft seed values (vocabulary values, not concepts, no IDs); value lists carried by a single concept are in the [concept annotations](../ontology/concept-annotations.md#values).

| Vocabulary | Seed values |
|---|---|
| Order handling channel (values of LD-C0061) | care; broker algorithm; direct market access; sponsored access |
| Execution method | matching on a venue (order book or request for quote); registration on a venue of a privately negotiated trade (block trade, exchange for related position, other venue-defined types); bilateral off-venue |
| Trading capacity | agency; principal; riskless principal (alignment with transaction-reporting capacity values to verify) |
| Clearing tier | pre-clearing; CCP–member house; CCP–member client account; member–client; client–indirect client; uncleared bilateral |
| Interposition mechanism | novation; open offer; other |
| Access model | direct membership (by category); through a third-party member; direct electronic access; client clearing; indirect clearing; sponsored or direct-client model |
| Client clearing legal model | principal-to-principal; agency or guarantee; indirect chain |
| Margin component | base initial margin; add-ons; premium or net liquidation value margin; variation margin |
| Run type | scheduled end-of-day; scheduled intraday; ad hoc |
| VM treatment | settled-to-market; collateralised-to-market; not applicable |
| Collateral legal form | title transfer; security interest |
| Fee chargeable event | execution; give-up; transfer; exercise or assignment; delivery; OTC registration or maintenance; compression; porting; periodic |
| Fee amount certainty and billing stage | estimated, final; accrued, invoiced, disputed, adjusted, settled, written off |
| Cost category | non-recharged venue and CCP fees; third-party brokerage; third-party clearing; connectivity and market data; funding and collateral; allocated shared cost |
| Regulatory attachment level | legal entity; role assignment; account; trade or report; CCP, venue or clearing service |
| Date role | trade date; CCP clearing date; value date; booking date; reporting date; last trading day; expiry; exercise deadline; first notice day; final settlement day; delivery day; publication; entry into force; application; phase-in; end of transition; as-of date |
