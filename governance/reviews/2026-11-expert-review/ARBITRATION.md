# Arbitration of the 2026-11 expert review

Status: Draft arbitration, 2026-11-01. Senior arbitrator across listed execution, ETD and OTC clearing, margin and collateral, regulation, product and ontology design. All resulting definitions are Draft; nothing here is a business approval.

Evidence: the eight second-pass reviews in this folder ([01 execution](01-execution.md), [02 ETD clearing](02-etd-clearing.md), [03 OTC clearing](03-otc-clearing.md), [04 collateral and margin](04-collateral-margin.md), [05 product](05-product.md), [06 regulation](06-regulation.md), [07 operations and reference data](07-ops-refdata.md), [08 ontology engineering](08-ontology-engineering.md)), copied unchanged; the sponsor answers of 2026-11-01 ([decision log](../../decision-log.md)); the agent hub's use cases UC-001 to UC-006 and question sets EV-001 to EV-006 at hub commit 019f844.

## 1. Verdict

The reviews are sound and largely convergent; their cross-reviews resolved most duplicates. The foundation's principles hold. What it lacked were the anchors the pilot agents reason over: a clearing service, member-side acceptance, the legal meaning of "cleared", the agreements and access routes behind give-up and client clearing, rules and their changes, deadlines and calendars, and the margin and collateral terms that circulars change.

Accepted: 24 new concepts (LD-C0051 to LD-C0074), 59 new relationships (LD-R0025 to LD-R0083), 17 new ambiguity entries (LD-A0019 to LD-A0035), proposed answers for all 35 entries (none marked resolved), four explicit meaning or type changes (LD-C0014, LD-C0022, LD-C0047, LD-R0019), two label changes (LD-C0013, LD-R0011), two refinements of placeholder definitions (LD-C0005, LD-C0007) and 16 clarifications. About 30 further proposals go to the backlog, mostly OTC-specific, lifecycle, operations-record and prudential concepts that no pilot question needs yet. Lean criterion: a proposal enters the catalogue only if a pilot use case (UC-001, UC-002, UC-003) or the sponsor's management-revenue priority (UC-004) cannot be answered without it.

Temporary IDs collided across reviews (NEW-COM-01 had four meanings, NEW-A-01 four). Proposals were merged by canonical name and given real IDs here; temporary IDs never enter the registers.

## 2. Conflict resolution

| Issue | Positions (review) | Decision | Rationale |
|---|---|---|---|
| LD-C0023 shape | Clarify as CCP side, add Clearing Member Acceptance as sibling (02, 03 v2, 08); keep as parent of member acceptance and a new "CCP Registration" (01, 06, 07, citing 03 v1); member acceptance is_a LD-C0023 (05) | **Clarify LD-C0023 as CCP acceptance or registration; add Clearing Member Acceptance (LD-C0053) as a sibling.** Changelogged as a clarification, not a meaning change. | The existing text ("into a specified clearing service") and LD-R0013 (`accepted_by` CCP) already denote the CCP act; only a CCP accepts into its service. The parent option would broaden LD-C0023, invalidate LD-R0013 for some instances and require a new concept duplicating today's meaning, which is the larger migration. The pre-execution limit case raised by 01 is covered by LD-C0053 ("automatic within a limit agreed before execution"). |
| Open offer | Concept, sibling of Novation (02 v1); mechanism value of CCP Interposition (01, 02 v2, 03, 05, 06, 08) | **Mechanism value of CCP Interposition (LD-C0054).** LD-C0024 stays generic. | Open offer is a standing rulebook mechanism; the occurrence is the interposition it produces. Novation also exists outside clearing, so a sibling would be wrong. |
| Generic Service | Service as parent with Clearing Service is_a (05); Clearing Service plus Service Offering, no parent (02, 03, 04, 07, 08 v2) | **Two concepts, no common parent: Clearing Service (LD-C0051) and Service Offering (LD-C0052), linked by `relies_on` (LD-R0082).** "Service" is an ambiguous term (LD-A0020). | A CCP's rulebook-defined service and the firm's commercial offering have different providers, identities, change triggers and owners; AG-002 goes from one to the other, and a merged class recreates the ambiguity. No pilot question needs a superclass. The sponsor's service-mix decision attaches to Service Offering. |
| Clearing broker: role or alias | Alias of LD-C0007 (03 v2: ambiguous alias; 05 v1); separate role (01, 02, 05 v2, 08); FCM not an alias of the role (06) | **Role Clearing Broker (LD-C0057), is_a Broker.** FCM is a contextual US alias plus a Regulatory Classification of the legal entity. | EV-002-Q01 needs a role that exists without membership of the clearing service; an alias cannot carry it. 05 withdrew its v1 position. |
| LD-C0013 label | Relabel "Product Family" (05); "Derivative Product" (07, citing 05 v1); keep meaning as classification, not a contract (01, 07, 08) | **Relabel to "Product Family" (label only); meaning kept and clarified as a venue-independent classification.** "Product" becomes an ambiguous alias (LD-A0021). | All agree on the meaning. The bare label "Product" captures questions such as EV-002-Q04 ("a given new product"), which usually mean a contract specification. "Product Family" matches the existing definition ("Family defined by…"). |
| LD-C0014 scope | Listed series only (08); counterparty-independent standardised specification including OTC ISINs (03); 07 wording close to 03 and keeps Entity | **Adopt 03's counterparty-independent wording; listed series or any specification with an assigned instrument identifier; bespoke OTC contracts are Trades. Explicit meaning change; type stays Entity.** LD-A0016 stays Open. | Excluding OTC ISINs would make the same identifier scheme point to no concept. The meaning change is recorded and put to the owner (open question 2). |
| Contract Specification | P2, Execution, Entity (08 v1); P1, Common, Reference Concept, named "Listed Contract Specification" (02, 07); P1 (01, 05, 08 v2) | **P1, Common, Reference Concept, named "Contract Specification" (LD-C0062), defined as venue-defined.** | Circulars frequently amend contract terms (UC-001) and EV-002-Q04 needs it. "Listed" is dropped from the name because venues other than futures exchanges also publish contract terms; the definition keeps it venue-defined. |
| LD-C0047 type | State (04); Role (08); Entity today | **State, with explicit meaning change** ("committed as security" becomes "provided by title transfer or security interest"). | Under the catalogue's own type definitions a Role is held by a party; collateral is a quantity of an asset in a condition under an arrangement as of a time. Directive 2002/47/EC distinguishes title-transfer from security arrangements, so "committed as security" was wrong for title transfer. LD-R0019 relabelled `changes` accordingly. |
| LD-C0003 reading | Party-in-role, no new concept (08 v2); separate Party Role Assignment concept (08 v1, assumed by 04, 05, 06) | **Read LD-C0003 as the role assignment (party-in-role); no new concept.** Clarification, changelogged; architecture text aligned. | The existing definition (function held by a party within a relationship, service and period) already describes a holding; role kinds as subclasses of party-in-role is a standard pattern. Every reference to "Party Role Assignment" in the reviews maps to LD-C0003. |
| Clearing Membership vs access | Clearing Membership as Agreement (02 v1); Market Access Arrangement for venues and clearing (01, 02 v2, 03, 05, 06); Access Model as a classification only (08) | **Market Access Arrangement (LD-C0059), Agreement, for execution and clearing, with access model as a governed qualifier; no Clearing Membership concept; no separate Access Model concept.** Membership is the Clearing Member or Trading Venue Member role assignment, `admitted_to` the service or venue under a category. | UC-002 needs instances with status and intermediary (third-party execution is in scope per sponsor decision 2026-11-01). The arrangement `confers` the role, so role and arrangement are not duplicates. A classification alone cannot carry status or intermediary. |
| Rule Change vs Change Notice | One object (05); Rule Change P1 plus Change Notice P2 (02, 06, 07, 08) | **Rule Change (LD-C0064) P1; Change Notice to backlog**, recorded meanwhile as the source document of a Rule Change. | One circular carries several changes with different dates, and one change passes through consultation and final notices. The notice is evidence, not the event. |
| Regulatory Obligation | Concept (02, 03, 05, 06); Rule Provision with a deontic kind (08) | **Backlog.** Pilot needs are met by Rule Provision (LD-C0063) qualified by provision kind, Regulatory Classification (LD-C0068) and Regime (LD-C0067). | Lean choice, medium conviction. Promote if one obligation must span several provisions with its own phase-in in an evaluation question; the catalogue's Obligation type (debtor and creditor) also fits a regulatory duty poorly. |
| Give-up "done" | Member claim for full quantity (01); registration to receiving member (02); coincide often, else CCP-sourced acceptance (07) | **Proposed answer (not decided): full allocated quantity registered to the receiving member's CCP account per the CCP record; partials separate; both timestamps kept.** Open question 1. | Registration is when the receiving member faces the CCP (EV-003-Q02) and is reconcilable against CCP statements; on many platforms the claim is that registration. |
| Porting scope | Default or client request (03 v1); default-triggered only, voluntary moves are Position Transfer (02, 03 v2, 04, 06) | **Default-triggered only; voluntary moves are Position Transfer. Both concepts to backlog; the distinction is recorded now as LD-A0026.** | EMIR Art. 48 porting is a default-management process without the defaulter's consent. No pilot question needs the concepts, but agents need the distinction now (GDI "portability"). |
| LD-C0030 retype | State to Entity "case" with owner and priority (07, with 08) | **Rejected; type State kept**, with a usage note that the case is the record of handling the exception. | An exception is a condition over an interval (raised to resolved); owner and priority belong to its handling record. The retype would model workflow tooling. EV-003-Q05 is served by LD-A0034. |
| LD-R0024 retarget | Retarget to a new Reconciliation Break (07) | **Kept, with clarified conditions; Reconciliation Break to backlog.** | Break is needed by UC-006 only (later phase). Clarified wording removes the break/exception merge. |
| Cut-off placement | Parameter of Rule Provision (08 v1); concept (07); concept specialising Rule Provision (07 v2, 08 v2) | **Cut-off (LD-C0065) is_a Rule Provision.** | Agents must compute deadlines against a calendar and time zone and state the consequence of a breach (EV-003-Q05), which a parameter cannot carry; the specialisation keeps one versioning and change mechanism. |
| VM `settled_by` | `LD-C0045 settled_by LD-C0028` (04 v1); type-incoherent (08) | **`LD-C0045 gives_rise_to LD-C0028` under settled-to-market only (LD-R0067); the collateralised-to-market path runs through Margin Call (LD-R0018).** Likewise collateral `covers` a requirement (LD-R0071) rather than an arrangement "securing" a Measure. | A Measure is not settled or secured; obligations are. |
| Clearing Member Acceptance module | ETD (02 v1, 08 v1); Common (01, 03, 05, 07) | **Common.** | OTC submission and pre-execution limit checks use the same decision. |
| LD-C0022 module | Move to ETD (attributed to 03); keep Common (02, 01) | **Common, with a listed-derivatives scope note.** | The executing side is party to it; 03 v2 asks only for a scope note. |
| Margin Methodology, Collateral Arrangement priority | P2 (05 v1, 08 v1); P1 (04) | **Both P1**, with Collateral Eligibility Schedule. | Margin methodology and eligibility circulars are among the most frequent UC-001 triggers (EV-001-Q03, EV-005-Q02, EV-005-Q03); the arrangement anchors LD-A0012 and the deferred collateral relation. |
| Clearing tier | Concept or vocabulary (03); provider and taker roles instead of a tier concept (04 v2) | **Governed vocabulary, no ID**; at margin level the tier is derived from provider and taker role assignments. | Values, not a class. |
| Status Assignment, Business Record, Identifier | P1 concepts (07 v1); patterns and template fields (08) | **Status Assignment withdrawn (07 v2 agrees). Source Record, Identifier Scheme, Reconciliation Break to backlog (P2).** The record-versus-object and valid/record time conventions are adopted in the modelling guidelines now. | Needed by UC-006, a later-phase internal use case. |
| Execution Method, Order Handling Channel | Concepts (01); facets (03, 05) | **Order Handling Channel is a concept (LD-C0061, P1) by sponsor decision 2026-11-01** (revenue split by channel). **Execution Method stays a taxonomy axis** (backlog for promotion). | The sponsor made the channel a revenue dimension. Execution Method is a classification that circulars change through rule provisions; no pilot question needs its identity yet. |
| LD-C0031 scope | Restrict to amounts owed (08); keep, with amount-certainty and billing-stage facets (05) | **Keep the definition; add the facets.** | An estimated amount of a real obligation is still that obligation. |
| CFTC 1.73 citation for give-up | Cited (02); weak relevance for give-up claims (01) | **Keep as a to-verify alignment of clearing member acceptance (pre-execution limit screening).** | FIA publishes procedural guidance titled "1.73 Give-Ups", linking the FCM risk-management rule to give-up screening against clearing-broker limits. |

## 3. Decisions on proposed concepts

Final ID or location; review numbers in brackets.

| Canonical proposal | Temporary IDs merged | Decision | Final ID / location |
|---|---|---|---|
| Clearing Service | 02 NEW-ETD-01, 03 NEW-COM-01 (v1), 05 NEW-COM-03 (v1), 08 NEW-ONT-01 | Accepted | LD-C0051 |
| Service Offering | 05 NEW-PRD-01, 08 NEW-ONT-02 | Accepted with changes (no "Service" parent) | LD-C0052 |
| Clearing Member Acceptance | 02 NEW-ETD-04, 03 NEW-OTC-01, 08 NEW-ONT-03 | Accepted (sibling of LD-C0023) | LD-C0053 |
| CCP Interposition | 06 NEW-REG-07, 02 NEW-ETD-02, 08 NEW-ONT-04 | Accepted | LD-C0054 |
| Give-up Agreement | 01 NEW-EXE-04, 02 NEW-ETD-05, 08 NEW-ONT-05 | Accepted | LD-C0055 |
| Client Clearing Agreement | 03 NEW-OTC-04, 06 NEW-REG-06 (as attribute) | Accepted with changes (covers ETD; legal model is an attribute) | LD-C0056 |
| Clearing Broker | 02 NEW-ETD-03 | Accepted | LD-C0057 |
| Trading Venue Member | 01 NEW-EXE-02 | Accepted (third-party execution in scope, sponsor 2026-11-01) | LD-C0058 |
| Market Access Arrangement | 05 NEW-PRD-02, 02 NEW-ETD-07, 08 NEW-ONT-06 (Access Model) | Accepted with changes (access model is a qualifier) | LD-C0059 |
| Allocation Instruction | 01 NEW-EXE-03 | Accepted | LD-C0060 |
| Order Handling Channel | 01 NEW-EXE-05 | Accepted, P1 by sponsor decision | LD-C0061 |
| Contract Specification | 07 NEW-REF-03, 08 NEW-ONT-09 | Accepted with changes (name, P1) | LD-C0062 |
| Rule Provision | 06 NEW-REG-04, 05, 08 NEW-ONT-07 | Accepted (includes firm procedures) | LD-C0063 |
| Rule Change | 06 NEW-REG-05, 08 NEW-ONT-08, 02, 05 | Accepted | LD-C0064 |
| Cut-off | 07 NEW-OPS-01 | Accepted (is_a LD-C0063) | LD-C0065 |
| Business Calendar | 07 NEW-REF-05 | Accepted | LD-C0066 |
| Regulatory Regime | 06 NEW-REG-01 | Accepted | LD-C0067 |
| Regulatory Classification | 06 NEW-REG-03 | Accepted | LD-C0068 |
| CCP Account | 02 NEW-ETD-06 | Accepted | LD-C0069 |
| Margin Methodology | 04 NEW-MC-01, 05 NEW-RSK-01 | Accepted | LD-C0070 |
| Collateral Arrangement | 04 NEW-MC-03 | Accepted | LD-C0071 |
| Collateral Eligibility Schedule | 04 NEW-MC-04 | Accepted | LD-C0072 |
| Commercial Group | 05 NEW-PRD-03 | Accepted | LD-C0073 |
| Contribution | 05 NEW-PRD-04 | Accepted with changes (no formula, no default perimeter) | LD-C0074 |
| Execution Method | 01 NEW-EXE-01 | Backlog (taxonomy axis now) | [Taxonomies](../../../taxonomies/README.md) |
| Clearing Tier | 03 NEW-OTC-03, 04 NEW-MC-02 (withdrawn) | Backlog as concept; vocabulary now | Taxonomies |
| Regulatory Obligation | 06 NEW-REG-02, 03 (withdrawn) | Backlog | §6 |
| Change Notice | 06, 02, 08 | Backlog | §6 |
| Clearing Submission | 03 NEW-OTC-02 | Backlog (OTC module comes last) | §6 |
| Portfolio Compression | 03 NEW-OTC-05 | Backlog | §6 |
| Porting | 02 NEW-ETD-09, 03 | Backlog (definition fixed: default-triggered) | §6 |
| Position Transfer | 02 NEW-ETD-08 | Backlog | §6 |
| Expiry, Exercise, Assignment | 02 NEW-ETD-10 to 12, 07 NEW-PTL-01 | Backlog | §6 |
| Default Fund Contribution | 04 NEW-MC-08, 06 NEW-REG-09 | Backlog | §6 |
| Cash Collateral Interest | 04 NEW-MC-11 | Backlog, pending open question 9 | §6 |
| Margin Excess / Shortfall | 04 NEW-MC-07 | Backlog; note added to LD-C0046 and LD-R0018 | §6 |
| Fee Rebate | 05 NEW-PRD-05 | Backlog | §6 |
| Activity Volume | 05 NEW-PRD-06 | Backlog; ambiguity LD-A0033 added | §6 |
| Regulatory Report | 06 NEW-REG-08 | Backlog (P3) | §6 |
| Source Record | 07 NEW-OPS-02 | Backlog; convention adopted in modelling guidelines | §6 |
| Reconciliation Break | 07 NEW-OPS-04 | Backlog | §6 |
| Identifier Scheme | 07 NEW-REF-02 | Backlog; template field added | §6 |
| Status Assignment | 07 NEW-OPS-03 | Rejected (withdrawn by 07) | — |
| Party Role Assignment | 08 v1 | Rejected; LD-C0003 clarified instead | LD-C0003 |
| Clearing Membership, Membership Category | 02 v1 | Rejected; role assignment plus category qualifier | LD-R0026 |
| Open Offer as event | 02 v1 | Rejected; mechanism value | LD-C0054 |
| Generic Service parent | 05 | Rejected for now | LD-A0020 |
| Access Model as concept | 08 | Rejected; qualifier of LD-C0059 | Taxonomies |
| Venue Operator role | 05 v1 | Rejected (withdrawn); edge LD-R0051 | LD-R0051 |
| Trade Identifier | 03 v1 | Rejected (withdrawn) | Backlog Identifier Scheme |
| Collateral Balance, Collateral Value, Call Cycle, Client Margin Policy | 04 v1 | Rejected (withdrawn) | LD-C0047, LD-C0070 |

## 4. Decisions on existing items

| ID | Change | Kind | Source |
|---|---|---|---|
| LD-C0003 | Read as role assignment (party-in-role) | Clarification | 08 |
| LD-C0005 | Placeholder replaced by an operative definition | Meaning refinement | 05, 08 |
| LD-C0007 | Points to Clearing Service, membership category and clearing scope | Meaning refinement | 02, 03 |
| LD-C0013 | Label Product to Product Family; scope clarified | Label change and clarification | 05, 07, 01 |
| LD-C0014 | Counterparty-independent standardised specification; bespoke OTC contract excluded | **Meaning change** | 03, 07, 08 |
| LD-C0015 | Date role and named calendar mandatory | Clarification | 07 |
| LD-C0016 | Who instructs whom; quantity and instrument | Clarification | 01 |
| LD-C0022 | Attribution to a receiving member at or after registration; partial; executing side | **Meaning change** | 02, 01 |
| LD-C0023 | CCP acceptance or registration; evidence of interposition | Clarification | 02, 03, 08 |
| LD-C0043 | Non-circular definition with provider, taker, account, methodology, time, currency | Clarification | 04 |
| LD-C0044 | Close-out period, confidence level, add-ons | Clarification | 04 |
| LD-C0045 | Two-way amount; STM and CTM consequences | Clarification | 04 |
| LD-C0046 | Direction, run, deadline, amount from uncovered requirement | Clarification | 04 |
| LD-C0047 | Entity to State; title transfer or security interest | **Type and meaning change** | 04 |
| LD-C0049 | Observed transfer incl. substitution; dual classification with LD-C0029 | Clarification | 04 |
| LD-C0050 | Types, scope, keys, tolerance, matches and discrepancies | Clarification | 07 |
| LD-R0004, LD-R0006, LD-R0013, LD-R0017, LD-R0018, LD-R0024 | Conditions clarified | Clarification | 01, 02, 04, 07 |
| LD-R0011 | Label receiving_member to has_receiving_member | Label change | 08, 01 |
| LD-R0019 | Label moves to changes (LD-C0047 is a State); asset transfer is LD-R0074 | **Relationship meaning change** | 04 |
| LD-C0030 | Retype to Entity "case" | Rejected; usage note only | 07 |
| LD-C0035 | Relabel "Executing Brokerage Charge" | Rejected (05 withdrew; no gain) | 01 |
| LD-C0031 | Restrict to owed amounts | Rejected; facets added | 08 |
| Others (LD-C0002, 0004, 0006, 0008 to 0012, 0017, 0018, 0020, 0021, 0024 to 0026, 0028, 0032, 0033, 0035 to 0037, 0040 to 0042, 0048) | Usage notes, aliases and required context | Notes only | All |

Notes, aliases, specialisations, required context, French labels and alignments are in [concept annotations](../../../ontology/concept-annotations.md).

## 5. Claims: verified and to verify

**Checked by the arbitrator on 2026-11-01 (web search of public sources):**
- The FIA "International Uniform Brokerage Execution Services ('Give-Up') Agreement" exists (published customer versions, including one for a London metals market); FIA had a revised give-up standard agreement in public comment in 2026, so the current version must be confirmed.
- EMIR Article 7a "Active account" exists (as introduced by Regulation (EU) 2024/2987); technical standards on its conditions were finalised by ESMA in 2025 and reported as published in 2026 (exact reference to verify).
- Commission Delegated Regulation (EU) 2021/1456 specifies when commercial terms for clearing services are fair, reasonable, non-discriminatory and transparent (EMIR Art. 4(3a)).
- FIA procedural guidance links CFTC Rule 1.73 to give-up screening against clearing-broker limits.

**Consistent across reviewers and with the arbitrator's knowledge; adopted, but cite the consolidated text before any status beyond Draft:** EMIR Art. 2(1) CCP, 2(7) OTC derivative, 2(15) client, 4(3) access routes, 14, 15, 25, 38(1) price disclosure, 39 segregation, 41 margin, 42 default fund, 46 collateral, 48 porting; MiFID II Art. 4(1)(9), 4(1)(39), 4(1)(41), 16(10), 17(5), 53; MiFIR Art. 26, 29, 30, 31; Delegated Regulations (EU) 2017/582 (RTS 26), 2017/590 (RTS 22), 2017/574 (RTS 25), 2017/589 (RTS 6), 2017/2154, 2017/2155, 153/2013; Directive 2002/47/EC title-transfer and security arrangements; CRR Art. 4(1)(88) QCCP; 17 CFR Part 22 LSOC and Part 30; PFMI Principles 1, 4, 6, 13, 14, 19, 23; ISO 10383, 17442, 10962, 6166, 4914 (UPI, FSB-designated service provider), 23897; the 2020 discounting and price-alignment transition of major swap CCPs to €STR and SOFR.

**To verify (kept out of definitions or marked in annotations):** exact paragraphs of EMIR Art. 39(5) and 39(7); Art. 7c content; amended Art. 38 duties on margin-model transparency; CFTC Rules 1.74, 23.506, 39.12(b)(7), 39.13(g)(8)(i) gross customer margin and (ii) customer margin above 100% of DCO initial margin; CFTC 1.35 paragraphs for average pricing and bunched orders; which OTC CCPs converted to settled-to-market and when; per-CCP interposition moments; venue trade-date conventions for evening sessions; LEIs for international branches; scope of OTC ISINs after the MiFIR review; absence of an EU or US clearing mandate for NDFs; UTI generation responsibility for cleared trades; CRR treatment of default-fund exposures; MiFID II Delegated Directive (EU) 2017/593 Art. 2 reconciliations; all FIX, FIXML, FpML and CDM element names and tags.

**Rejected as stated by a reviewer:** "listed markets typically use open offer at matching" as a default (06) — true of many, not all, CCPs, so no default is set; "the US client is party to the CCP contract" without qualification (03) — varies by product and rulebook.

## 6. Backlog

Not in the catalogue. Promote when an evaluation question needs it, with a new ID at that time.

| Item | Kind | Priority | Trigger for promotion | Source |
|---|---|---|---|---|
| Execution Method | Concept (taxonomy axis now) | P2 | A circular-impact question needs its identity (block or EFRP rules) | 01, 03 |
| Clearing Submission | Concept, OTC | P2 | OTC phase of UC-003 | 03 |
| Portfolio Compression | Concept, OTC | P2 | UC-001 or GDI compression items | 03 |
| Porting (default-triggered) | Concept | P2 | GDI "portability" or a UC-001 question | 02, 03, 04, 06 |
| Position Transfer | Concept | P2 | UC-001 or EV-003-Q05 resolution paths | 02 |
| Expiry, Exercise, Assignment | Concepts | P2 to P3 | Lifecycle questions (open question in 02) | 02, 07 |
| Regulatory Obligation | Concept | P2 | An obligation spanning several provisions with its own phase-in | 06, 03 |
| Change Notice | Concept | P2 | GDI items need a document object | 06, 02 |
| Default Fund Contribution | Concept | P2 | EV-002-Q01 cost comparison or contribution perimeter | 04, 06 |
| Cash Collateral Interest | Concept | P2 | Open question 9 answered "include" | 04 |
| Margin Excess / Shortfall | Concept | P2 | UC-006 or a margin-call question | 04 |
| Fee Rebate | Concept | P2 | Rebate netting decision | 05 |
| Activity Volume | Concept | P2 | UC-005 positioning or rate per contract | 05 |
| Source Record, Reconciliation Break, Identifier Scheme | Concepts | P2 | UC-006 phase | 07 |
| Regulatory Report | Concept | P3 | A reporting question | 06 |
| Order parent/child (`derived_from`), Order `submitted_to` | Relationships | P2 | Execution-module fiches | 01 |
| Ambiguities: block trade; DMA, DEA and algorithm; unwind, termination and amendment; excess; margin components across CCPs; source of record; trade identifiers; rebate, discount and waiver; fact versus interpretation | Ambiguity entries | P2 | First related evaluation question | 01, 03, 04, 05, 06, 07 |
| Relationship register columns (types, inverse, temporal, status) and per-concept status | Format | P1 after hub fix | Hub reader parses by header | 08 |
| Competency questions LD-Q and metric namespace | Format | P2 | Open question 12; hub gate H4 | 08 |
| Validation script in this repository (ID patterns, references, no in-cell pipe, parents acyclic) | Tooling | P2 | Before the first tag | 08 |
| French labels for relationships | Labels | P3 | Open question 12 | 08 |

## 7. Hub follow-ups (not made here)

1. **Header-based parsing** in `tools/ontology_reader.py`: today an extra concept column merges into the definition, an extra relationship column into the conditions, and ambiguity columns beyond the fourth are ignored. Read `Affected IDs` and `Status` from the register.
2. **Ambiguity linking by ID** in `tools/export_ontology.py`: replace name-substring matching with the `Affected IDs` column; include the "Proposed answers pending owner decision" section, clearly labelled as not decided.
3. **Concept annotations**: read `ontology/concept-annotations.md` for aliases (alias table for retrieval mode), resolution flags (LD-C0019, LD-C0038 return candidates), required context, specialisations and French labels; show per-concept status rather than one catalogue-wide status.
4. **Reader checks**: ID uniqueness, reject temporary `NEW-` IDs, warn when a relationship endpoint contains no `LD-C` ID.
5. **Pin move**: after owner review, move the registry pin and every question set's `ontology_pin`; rerun the evaluation sets citing LD-C0013, LD-C0014, LD-C0022, LD-C0023 and LD-C0047 (meaning or label changes), as ADR-0002 requires.
6. **Use-case concept lists**: add concepts used by their question sets (UC-001: LD-C0004, LD-C0015, LD-C0046, LD-C0049; UC-002: LD-C0022; UC-005: LD-C0010, LD-C0044, LD-C0048; UC-006: LD-C0004, LD-C0008), add a `hub_check.py` rule that a use case's concepts cover its questions, and add new IDs: UC-001 LD-C0051, LD-C0063 to LD-C0066, LD-C0069, LD-C0070, LD-C0072; UC-002 LD-C0051, LD-C0055 to LD-C0059, LD-C0062, LD-C0067, LD-C0068; UC-003 LD-C0053 to LD-C0055, LD-C0060, LD-C0065; UC-004 LD-C0052, LD-C0061, LD-C0073, LD-C0074; UC-005 LD-C0070, LD-C0072.
7. **Question sets**: cite new IDs (EV-003-Q01/Q02 LD-C0053; EV-003-Q03 LD-C0054; EV-002-Q01 LD-C0057, LD-C0059; EV-002-Q02 LD-C0055, LD-C0056; EV-002-Q04 LD-C0062, LD-C0051; EV-001-Q01 LD-C0069, LD-C0051; EV-001-Q02 LD-C0067, LD-C0068, LD-C0073; EV-001-Q04 LD-C0064, LD-C0065; EV-001-Q05 LD-C0066; EV-005-Q02 LD-C0070; EV-005-Q03 LD-C0072; EV-004-Q05 LD-C0073, LD-C0074) and the relevant `LD-A` IDs; add questions on contribution and pass-through (EV-004), execution access without venue membership (EV-002) and published tariffs or volumes (EV-005), with owner-written answers.
8. **GDI topic mapping**: portability to LD-A0026; direct and sponsored clearing to LD-C0059; portfolio margining and cross-margining governance to LD-C0070; non-cash and tokenised collateral also to LD-C0072; client clearing models to LD-A0030; third-country CCP recognition to LD-C0068.
9. **Wording**: the registry marks `ontologie` as `zone: public` while the CI comment says the repository is private; state that the zone is a content classification.
10. **Test fixture** with appended ambiguity columns and a second concept table, to protect the parser contract.

## 8. Checks run

Files changed are listed in the [change log](../../../CHANGELOG.md) entry of 2026-11-01. Results on 2026-11-01, after the edits:

- Registers: 74 concepts, 83 relationships, 35 ambiguities; IDs unique and contiguous; every row has the expected cell count (5, 5 and 6), so no in-cell pipe; every relationship endpoint is a concept ID or an explicit union of them.
- References and links: no dangling `LD-` reference anywhere in the repository; no broken local link or anchor; no temporary `NEW-` ID outside the review evidence.
- Hub `tools/hub_check.py --require-ontology`: 0 errors against this repository (read at the hub's pin, as designed) and 0 errors against a non-git copy of the working tree (read as working tree). Only warnings: no confidential-term list configured; pin not readable in the copy.
- Hub export of the working tree: 74 concepts, 83 relationships, 35 ambiguities parsed; no relationship lost an endpoint; new ambiguity columns ignored as expected.
- Hub unit tests: 6 passed.
