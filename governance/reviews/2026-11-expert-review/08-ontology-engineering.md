# Review 08 (v2): Ontology engineering and knowledge architecture for AI agents

Scope: type system, identity and time, relationship design, standards alignment, machine-readable format, how agents consume the ontology, validation. State reviewed: `ontologie` @ 59c1998 (the hub pin) and the hub @ 019f844. I checked all repo claims by script, including the hub exporter's actual output.

## 1. Verdict

The foundation is disciplined. Integrity passes: 50/24/18 contiguous unique IDs, no dangling `LD-` references, no broken local links. As a machine-usable base for agents it is still thin:

- 22 of the 50 concepts have no relationship.
- `is_a` exists only in prose.
- The 10 concept types are undefined.
- There are no aliases, although hub retrieval mode assumes an alias table.
- Ambiguities carry no concept IDs. The exporter matches them to concepts by name substring and gets 5 of 18 wrong or unattached.
- The hub reader's table contract silently breaks under the edits Phase 2 will make. It relies on cell positions, uses one catalogue-wide status, and reads only `foundation.md`.

A few structural fixes, mostly fields and columns rather than concepts, make it agent-ready without breaching the YAML deferral.

## 2. Corrections to existing items

| ID | Issue | Proposed change | Sev. | Conf. |
|---|---|---|---|---|
| LD-C0003 | It is unclear whether C0003 is a role *kind* or a party's *holding* of a role. `architecture.md` implies a kind. The definition (context, period) implies a holding. | Read C0003 as the role assignment ("party-in-role"). Role kinds become its specialisations (C0004–C0008) plus Participants-taxonomy values. Definition: "Contextual, time-bounded holding of a function by a party toward identified counterparties, within a service and, where applicable, under an agreement." This is a clarification, not a meaning change; R0001 and R0002 stay valid. Align `architecture.md`. Alignment, to verify: FIBO FND Parties `PartyInRole`, CDM `PartyRole`. | High | Med-High |
| C0004/6/7/23 | They reference a "service" or "clearing service" that is defined nowhere. | Add Clearing Service and Service Offering (§4). | High | High |
| LD-C0023 | The name, the wording ("into a specified clearing service") and R0013 (`accepted_by` CCP) all point to the CCP side. Nothing covers clearing-member take-up or legal interposition, which EV-003-Q01 and EV-003-Q03 need. | Clarify C0023 as CCP acceptance/registration (contextual alias "registration"). Add the siblings Clearing Member Acceptance and CCP Interposition. Log the change in the changelog. | High | Med-High |
| Types (`modelling-guidelines.md`) | Types are named but not defined. Reviewers disagree on Entity vs Reference Concept, and domain/range cannot be validated. | Add one-line definitions (§4b). | High | High |
| Specialisations | Nine `is_a` claims sit in prose. | Add a `parents` field per concept. Do **not** add an `LD-C`-keyed table to `foundation.md`: the reader parses such rows as duplicate concepts (verified). | High | High |
| Ambiguity register | It has no affected IDs and no status. Name matching sends A0001 "Execution fee" to C0017 Execution and A0003 to C0005 Broker. A0005 and A0009–A0012 attach to nothing, so the AG-004 core (C0022, C0023, C0043, C0045) gets no warnings. | Append the columns `Affected IDs` and `Status` (Open / Narrowed / Resolved). The 2026-09-20 decisions narrow A0002, A0006 and A0014. The hub must link ambiguities by ID. | High | High |
| Catalogue status | Every card shows "Draft for all 50 entries…", so once one fiche is Reviewed the cards will be wrong. | Give each concept its own `status`, plus `deprecated` and `replaced_by` fields. Never mark deprecation in the ID cell: the reader would produce the ID "LD-C0003 (deprecated)". | Med | High |
| Relationship register | It has no cardinality, inverse, temporal or status columns. R0007, R0009 and R0017 have union targets. R0011 is a noun. `concerns` is reused across domains. | Append columns (§5). Declare union ranges explicitly. Use verb labels, e.g. R0011 → `has_receiving_member` (label only). | Med | High |
| Template | It lacks identity criteria, identifiers, temporal pattern, required context, French label, standard alignments and the competency questions served. Master-prompt step 2 asks for most of these. | Add the seven fields (§4b). | High | High |
| LD-C0047 | Typed Entity, but it denotes an asset in a role under an arrangement. C0048 is already the entity. | Retype as Role. Use review 04's wording ("by security interest or title transfer"). | Med | Med |
| LD-C0031 | Typed Obligation, but "chargeable" includes estimates. | Restrict the definition to amounts owed. Make the stage (estimated, invoiced, adjusted, settled) a governed qualifier (LD-A0018, review 05). | Med | Med |
| LD-C0005 | The definition is a placeholder. | Adopt review 05's text: "Role of a party that acts on behalf of others to execute orders and/or to clear or carry their trades, under an identified agreement". It becomes the parent of C0006 and Clearing Broker. | Med | Med |
| LD-C0019, C0038 | Both are deferred, yet an agent can resolve "transaction" or "commission" to them. | Mark both `resolution: blocked-pending-decision`, so agents return candidates and ask. MiFIR Art. 26 "transaction" is an ambiguous alias. | Med | High |
| Minor | (a) "Fill" is used in R0004 and R0005 but not recorded. (b) Event concepts do not point to C0025. (c) The identity key of C0026 Position is implicit. (d) R0007 and R0008 attach quantity and target account to a Process. | (a) Add "fill" as an *ambiguous* alias of C0017 (review 01). (b) Set `parents: [C0025]` for C0017, C0023, C0024 and the new events. (c) Name the key: account × instrument × clearing service × side basis, as a snapshot. (d) Retarget R0007/R0008 to review 01's Allocation Instruction when it exists. | Low | Med |
| Wording drift | Terms differ ("owning module" vs "owning domain"), and three files still say "after Phase 1 approval". | Use `module` with codes that match folder names. Refresh the stale wording. My v1 claim of a phase-numbering clash was wrong and is withdrawn. | Low | High |

## 3. Answers to open ambiguities (engineering view)

- **LD-A0008.** Three identity levels, linked by directional lineage and not by cardinality: execution event (FIX ExecutionReport), trade (CDM `Trade`/`TradeState`, to verify), and successor trades after clearing. Each level has its own identifier scheme; UTI is ISO 23897. Confidence high. Transaction stays deferred.
- **LD-A0009 / A0017.** "Cleared" is a derived status, not a concept. CM acceptance, CCP acceptance and CCP interposition are three timestamped events. The mechanism is a governed value per clearing service, sourced from rulebooks. Confidence high. No firm decision is needed for the pattern.
- **LD-A0013 / A0015.** Use `required_context`, not new concepts:
  - Position: {account, instrument, clearing service, gross/net, quantity kind, as-of}.
  - Business Date: {date role, calendar, time zone}.

  Date roles stay a governed vocabulary, as `architecture.md` says.
- **LD-A0016.** Four layers:
  - Product: classification. CFI (ISO 10962) is a code, not an identifier.
  - Contract Specification: new.
  - Instrument: listed series, identified by ISIN (ISO 6166).
  - Bespoke OTC economics: part of the Trade, with UPI (ISO 4914) for the product and UTI for the trade.

  Narrowing C0014 is an explicit meaning change for Reference Data and OTC Product to decide. Confidence medium-high.
- **Time.** Each concept declares a `temporal_pattern`: point-event, interval-valid, snapshot or timeless. L3 instances carry valid time and record time, which EV-001-Q04 and EV-006-Q01 need. Adopt review 07's "current / as of / as known at" convention.
- **Cardinality.** Record context-qualified constraints {context, min, max, source, status} (sponsor decision 6). Only definitional cardinalities are global, e.g. a Fee Charge has exactly one debtor and one creditor (medium confidence).

## 4. Proposed new concepts (structural set; domain duplicates consolidated in §8b)

| Temp ID | Name | Module | Type | Definition | Key relationships | Alignment (to verify) | Prio | Serves |
|---|---|---|---|---|---|---|---|---|
| NEW-ONT-01 | Clearing Service | common | Entity | Distinct clearing offering of a CCP for a defined product scope, governed by identified rule provisions, with its own membership, account structures and default arrangements. | provided_by C0008; context of C0007 and C0023 | CCP rulebooks | P1 | EV-001-Q01, EV-002-Q01, EV-003 |
| NEW-ONT-02 | Service Offering | common | Entity | Defined service a provider offers to clients, scoped by service kind, product scope, venue or clearing service, and channel. | context of C0004 and C0006; C0031 charged_for | FIBO FND products and services | P1 | C0004; UC-002, UC-004 |
| NEW-ONT-03 | Clearing Member Acceptance | common | Event | A clearing member accepts or rejects, wholly or partly, responsibility for clearing a trade or allocation for an account; it may come before or after CCP acceptance. | concerns C0018; decided_by C0007; part_of C0022 | FIXML claim flows; FpML clearing status | P1 | EV-003-Q01/Q02 |
| NEW-ONT-04 | CCP Interposition | common | Event | A CCP becomes counterparty under a clearing service's rules, by a stated mechanism (novation, open offer, other). This is the legal effect that a "cleared" status may evidence but does not establish. | effected_by C0008; evidenced_by C0023; realised_by C0024 (when the mechanism is novation) | CDM clearing | P1 | EV-003-Q03 |
| NEW-ONT-05 | Give-up Agreement | common | Agreement | Agreement among a client, executing broker(s) and a clearing broker on how trades are given up and taken up, including limits and brokerage payment. | is_a C0012; governs C0022 | FIA give-up agreement | P1 | EV-002-Q02, EV-003-Q02 |
| NEW-ONT-06 | Access Model | common | Reference Concept | Governed classification of ways to obtain execution or clearing access: direct membership, via a member, indirect, sponsored. Concrete arrangements are expressed by role assignments and agreements. | classifies C0003 | Indirect-clearing RTS; CCP sponsored models | P1 | EV-002-Q01 |
| NEW-ONT-07 | Rule Provision | common | Reference Concept | Versioned unit of a regulation, standard, rulebook, procedure or tariff, with issuer, scope and effective period, that imposes a requirement or sets a parameter. | issued_by C0003; applies_to (declared union); supersedes | none | P1 | EV-001-Q04; UC-003 deadlines |
| NEW-ONT-08 | Rule Change | common | Event | A rule provision is proposed, adopted, amended, withdrawn or replaced, with distinct publication, effective and compliance dates. | changes NEW-ONT-07 | none | P1 | UC-001, UC-005 |
| NEW-ONT-09 | Contract Specification | common | Reference Concept | Versioned venue-defined terms from which listed series are created: underlying, size, currency, expiry and settlement rules, trading hours. | C0014 listed_under it; classified_as C0013; listed_on C0009 | FIX SecurityDefinition; CFI | P1 | EV-001-Q05, EV-002-Q04 |

Party Role Assignment (v1) is dropped as redundant after the C0003 clarification. Deadlines are modelled as Cut-off, `is_a` Rule Provision.

### 4b. Format: deterministic Markdown now, YAML later

The README defers YAML "until the business model is validated". Phase 2 Markdown can still be made parseable now:

- **Fiches** use the template's field table with fixed field names and controlled values: `type`, `module`, `subdomain`, `status`, `parents`, `aliases` (label, kind, scope, language), `identity` (criteria, schemes), `temporal_pattern`, `required_context`, `ambiguities`, `alignments`, `competency_questions`, `resolution`, `label_fr`, `replaced_by`.
- **Registers** get new columns appended at the end only.
- **`foundation.md`** stays the index, one row per ID, including new and deprecated IDs, because the hub reads only that file.
- **YAML front matter** becomes canonical at the first tag, with `foundation.md` then generated from it. This needs a sponsor decision.

**Type definitions:**

| Type | Definition |
|---|---|
| Entity | Persistent identity independent of any event. |
| Role | Contextual, time-bounded function held by an entity in a relationship, service or arrangement. |
| Agreement | Creates rights and obligations between identified parties. |
| Instruction | Request to act; can be accepted, rejected, amended or cancelled. |
| Event | Dated, immutable occurrence; corrections are new events. |
| Process | Coordinated instructions and events toward an outcome. |
| State | Condition over an interval or at an as-of time. |
| Obligation | Debtor's duty to a creditor with due terms. |
| Measure | Quantity under a stated method, scope, time and unit. |
| Reference Concept | Governed classification, rule or specification. |

**Alignment:** map, don't import. Use SKOS exact/close/broad/narrow/related matches, with `verified: false` and no IRI until the published release has been checked. OWL/SKOS export stays optional.

**Hub reader, verified behaviour:**

- Concept definition = `cells[4:]` joined, so any appended column merges into the definition.
- The ambiguity reader ignores columns beyond the fourth.
- Endpoints are matched with the regex `LD-C\d{4}`, so `NEW-*` IDs and prose ranges vanish.
- There is no uniqueness check.
- An in-cell `|` splits the cell.

The PR that moves the pin must therefore switch the reader to header-based parsing. The pin shields the hub until then.

### 4c. Agent consumption, using the hub's three modes

- **Context mode (AG-002, AG-004).** The summary should carry each concept's status, resolution, required context, parents and ambiguity IDs. AG-002's multi-hop is an in-memory JSON traversal, with no graph database: Rule Change → Rule Provision → `applies_to` → Clearing Service, Segregation Model or Account → (L2 overlay) Service Offering.
- **Retrieval mode (AG-001, AG-003).** Export the alias table the hub architecture already promises. An ambiguous alias returns candidates, not a single answer.
- **Tagging is not an edge.** Tagging a notice or GDI item with an `LD-C` ID is an annotation (`concerns_concept`). It is not the instance-level `applies_to`.
- **Tool mode.** Semantic contracts get their own namespace (proposal: `LD-M`) after gate H4.

### 4d. Validation (Python CI in `ontologie`)

- IDs match `^LD-[CRAQ]\d{4}$`, are unique, and retired IDs are never reused.
- All references resolve. No `NEW-*` IDs appear in registers.
- Each `type` is one of the 10. `parents` contains no cycles and is type-compatible.
- Relationship domain and range match the declared types.
- Concepts with no relationship and no parent raise a warning.
- Every ambiguity has at least one affected ID.
- No alias is `exact` for two concepts.
- `approved` requires approver, date and evidence. `deprecated` requires `replaced_by` or a reason.
- Every new concept cites an `LD-Q`.
- No `|` appears inside a cell.
- The index and the fiches agree.

In the hub, check that each UC's concept list covers its EV set, and let EV questions cite `LD-A` IDs.

### 4e. Competency questions

Give the eight CQs IDs `LD-Q0001…`. Promote each validated public EV question into `ontologie` as an `LD-Q`, so dependencies point one way.

Structural gaps today:

| Question | Gap |
|---|---|
| EV-001-Q01 | C0011 is isolated. |
| EV-001-Q04 | No rule or version concept. |
| EV-002-Q01, EV-002-Q02 | C0006 is isolated; no access model or agreement kinds. |
| EV-002-Q04 | No venue-operator edge; C0014 is isolated. |
| EV-003-Q03 | C0023 and C0024 are unlinked. |
| EV-005-Q03 | C0048 is isolated. |
| EV-006-Q02, EV-006-Q03 | No Account–Client or Account–CCP edge. |
| EV-004 | Fee subtypes are linked only in prose. |

## 5. Proposed new or changed relationships

Columns to append to the relationship register: source type, target type, cardinality (`not asserted` or context-qualified), inverse label, temporal, status, CQs served.

- C0003 `held_toward` C0001 (temporal). C0003 `within` Clearing Service | Service Offering (0..1). R0001 and R0002 are kept, with notes.
- Clearing Service `provided_by` C0008 (exactly 1, definitional).
- C0010 `maintained_by` C0001. C0010 `held_for` C0003. C0010 `structured_under` C0011, in the context of a clearing service. Serves EV-001-Q01, EV-006 and A0007.
- C0014 `listed_under` Contract Specification. Contract Specification `classified_as` C0013, `listed_on` C0009 (temporal), and `eligible_in` Clearing Service (temporal).
- C0009 `operated_by` C0002.
- Clearing Member Acceptance `concerns` C0018, `decided_by` C0007, `part_of` C0022.
- CCP Interposition `concerns` C0018, `evidenced_by` C0023, `realised_by` C0024.
- C0022 `governed_by` Give-up Agreement. C0022 `has_giving_member` C0007.
- Rule Change `changes` Rule Provision. Rule Provision `supersedes` Rule Provision and `issued_by` C0003. Rule Provision `applies_to` {Clearing Service, C0009, Contract Specification, C0010, C0011, C0022, C0023, C0043, C0047}, declared as an explicit union, never "any concept".
- C0031 `arises_from` {C0017, C0025, Service Offering}. C0031 `charged_for` Service Offering.
- C0043 `between` the provider and taker role assignments. This pair is the tier from A0011.
- C0039 `attributed_to` C0003 or Service Offering, only under a semantic contract and with no formula.

## 6. Proposed new ambiguity entries

| Temp ID | Term | Required distinction | Reviewer |
|---|---|---|---|
| NEW-A-ONT-01 | Service | CCP Clearing Service vs firm Service Offering vs MiFID investment service. | Product / Steward |
| NEW-A-ONT-02 | Current / as of / as known at | Valid time vs record time (merges review 07 NEW-A-01). | Operations / Steward |
| NEW-A-ONT-03 | Clearing broker vs clearing member | Service role toward the client vs admission at the CCP; FCM is a registration status (merges 02 NEW-A-01, 03 NEW-A-OTC-04). | Product / Legal |
| NEW-A-ONT-04 | Collateral | Asset vs asset-in-role vs balance held (C0047, C0048; review 04). | Risk / Collateral |

## 7. Questions only the business owner can answer

1. **Format.** Should Phase 2 use deterministic Markdown fiches now, with YAML canonical from the first tag? *Default: yes, recorded as a decision.*
2. **C0003.** Should it be read as party-in-role, with role kinds as specialisations and no separate assignment concept? *Default: yes, with a changelog note.*
3. **C0023.** Should it be clarified as the CCP side, with CM Acceptance and CCP Interposition added as siblings? This is central to AG-004. *Default: yes.*
4. **Rules.** Should Rule Provision and Rule Change be ontology concepts, with instances held in GDI/L3? UC-001 multi-hop depends on this. *Default: yes.*
5. **French label.** Should `label_fr` be mandatory per concept and relationship, as the master prompt asks? *Default: yes; English stays canonical.*
6. **Aliases and repo visibility.** Where do internal-jargon aliases live? The hub registry marks `ontologie` public, but the hub CI comment calls it private. *Default: generic aliases public, firm aliases in the overlay; confirm visibility.*
7. **First tag.** When should it be cut, and does the pin-move PR own the reader update? *Default: after the Common fiches are Reviewed; yes.*
8. **Competency questions.** Should validated public EV questions be promoted to `LD-Q` competency questions in `ontologie`? *Default: yes.*

## 8. Cross-review

### 8a. Disagreements

- **02, Clearing Membership as an Agreement.** Under the party-in-role reading, a C0007 instance *is* the admission. Keep the category as a governed qualifier.
- **03, C0023 as parent of CM Acceptance and CCP Registration.** This adds a concept no question needs, because C0023 already means CCP registration. Clarify C0023 and add CM Acceptance as a sibling instead.
- **02, Open Offer, and 06, Client Clearing Legal Model.** Both should be governed values, not concepts: the mechanism of CCP Interposition, and a required attribute of Client Clearing Agreement.
- **03 and 06, Regulatory Obligation.** I would treat it as a Rule Provision with a deontic kind, `applies_to` a classification or role. Party-specific applicability is an L3 inference that Legal confirms. Medium conviction.
- **07, Status Assignment and Identifier / Identifier Scheme as P1 concepts.** These are L3 provenance patterns plus `identity` fields with a governed scheme list. Business Record is fine at P2.
- **05, Venue Operator role.** The `C0009 operated_by C0002` edge already answers EV-002-Q04.
- **04, `C0045 settled_by C0028`.** This is type-incoherent: a Measure is not settled. Use `gives_rise_to` Settlement Obligation for STM, and Margin Call for CTM.
- **02, 05 and 06, "Rule Change affects any concept".** This mixes instance edges with concept tags. Use a declared `applies_to` union for instances and `concerns_concept` for tags.
- **Priorities.** P1 should be what AG-004, AG-002 and then AG-003 need. Concepts that serve only UC-004 or UC-006 should be P2, except Client Contribution, the sponsor's priority.

### 8b. Duplicates and canonical form

Temp IDs collide across reviews: NEW-COM-01 has four meanings and NEW-A-01 has four. Merge by canonical name, and allocate `LD-C0051+` only when the fiches are drafted.

| Canonical | Type, module, prio | Merges |
|---|---|---|
| Clearing Service | Entity, common, P1 | 02/03 NEW-COM-01, 05 NEW-COM-03, v1 Service |
| Service Offering | Entity, common, P1 | 05 NEW-COM-01 |
| Clearing Member Acceptance | Event, common, P1 | 02 NEW-ETD-06, 03 NEW-COM-02, v1 NEW-ETD-01 |
| CCP Interposition (mechanism incl. open offer) | Event, common, P1 | 06 NEW-REG-07, 02 NEW-COM-02; 03 CCP Registration = clarified C0023 |
| Give-up Agreement | Agreement, common, P1 | 01 NEW-EXE-04, 02 NEW-ETD-05 |
| Client Clearing Agreement (+ legal model) | Agreement, common, P1 | 03 NEW-COM-06, 06 NEW-REG-06 |
| Clearing Broker (is_a C0005) | Role, common, P1 | 02 NEW-ETD-03; 03/05 aliases |
| Access Model | Reference Concept, common, P1 | 02 NEW-COM-03, 05 NEW-COM-02 |
| Rule Provision; Cut-off (is_a) | Reference Concept, common, P1 | 05 NEW-COM-05, 06 NEW-REG-04; 07 NEW-OPS-01 |
| Rule Change; Market Notice (P2) | Event, common, P1 | 02 NEW-COM-06/07, 05 NEW-COM-04, 06 NEW-REG-05 |
| Regulatory Regime | Reference Concept, common, P1 | 06 NEW-REG-01, 05 NEW-COM-10 |
| Contract Specification | Reference Concept, common, P1 | 07 NEW-REF-03, v1 NEW-EXE-01 |
| Margin Methodology | Reference Concept, common, P1 | 04 NEW-MC-01, 05 NEW-RSK-01 |
| Collateral Arrangement | Agreement, common, P1 | 04 NEW-MC-03 |
| Default Fund Contribution | Obligation, common, P2 | 04 NEW-MC-08, 06 NEW-REG-09 |
| Porting | Process, common, P2 | 02 NEW-COM-04, 03 NEW-COM-08 |
| Expiry | Event, etd-clearing, P2 | 02 NEW-ETD-12, 07 NEW-PTL-01 |
| Ambiguity: "Product" | n/a | 05 NEW-A-02, 07 NEW-A-03 |
| Ambiguity: rule-change dates | n/a | 02/05 NEW-A-04, 06 NEW-A-REG-03 |
| Relations `arises_from`, `has_giving_member` | n/a | 02 `triggered_by`; 01 `giving_member`, 02 `sending_member` |

### 8c. Points that affect my domain

- **06's attachment rule** puts classifications on the Legal Entity or the role assignment. That presupposes the party-in-role reading of C0003.
- **07's bitemporal convention** belongs in `modelling-guidelines.md`. **05's Subdomain proposal** gives per-agent retrieval scopes, so make `subdomain` a controlled field. 04's "Margin & Collateral" fits it.
- **05's hub finding is correct.** UC-001 omits C0004, C0015, C0046 and C0049, which its EV set uses. Add the hub check.
- **07's retyping of C0014 to Reference Concept** follows from the type definitions. Apply it with the A0016 decision.
- **04's dual classification** (C0049 also C0029) requires that classes not be declared disjoint. The validator must not assume disjointness.
- **Narrowings of C0014, C0022 and C0023** need migration notes. The pin-move PR must rerun the EV sets that cite them (ADR-0002).
