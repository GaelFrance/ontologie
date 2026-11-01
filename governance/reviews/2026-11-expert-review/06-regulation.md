# Review 06 — Regulation, legal effect and prudential touch-points (v2)

Specialty: EMIR / Refit / EMIR 3, MiFID II / MiFIR, CFTC/SEC (general terms), PFMI, CRR CCP exposures, legal effect of clearing. References are to public texts. Anything marked "to verify" must be checked against the consolidated text before adoption. Nothing here says which rules apply to the firm. The v1 temporary IDs are kept; withdrawn ones are not reused.

## 1. Verdict

The foundation states the right principle ("regulatory concepts are contextual and versioned by jurisdiction, regime and effective date"; principle 9), but no concept carries it. As a result:
- AG-002 cannot answer EV-001-Q02 (who is in scope of an active-account obligation) or EV-001-Q04 (old vs new rule version).
- AG-003 cannot list "regulatory steps" (UC-002, EV-002-Q03).
- AG-004 cannot say what "cleared" legally means (EV-003-Q03).

Six concepts, one attachment rule and a few usage notes are enough. Articles, thresholds and dates are knowledge-graph instances. ADR-0003 sets the boundary: an obligation's *definition* is public, but its *applicability to a named party* is an internal, Legal-validated conclusion.

## 2. Corrections to existing items

| ID | Issue | Proposed change | Sev. | Conf. |
|---|---|---|---|---|
| LD-C0008 Central Counterparty | Mixes the role in a clearing service with the entity's regulatory status. Statuses: EMIR-authorised (Art. 14), recognised third-country Tier 1/2 (Art. 25), CFTC DCO, QCCP (CRR Art. 4(1)(88)). EMIR authorisation is extended per service (Art. 15, to verify). | Usage note: "Authorisation, recognition and QCCP status are time-bounded Regulatory Classifications (NEW-REG-03) of the legal entity, by regime and, where relevant, by Clearing Service." Mechanism: "novation, open offer or another mechanism defined by its rules and governing law." | Med | High |
| LD-C0024 Novation | Used as if it were *the* clearing mechanism. Listed markets mostly use open offer, and novation also exists outside clearing (bilateral step-in, porting). | No meaning change. The clearing-specific legal event is NEW-REG-07 CCP Interposition; novation is one of its mechanism values. | High | High |
| LD-C0023 Clearing Acceptance | Who accepts is not stated. MiFIR Art. 29(2) and RTS 26 (Delegated Reg. (EU) 2017/582), and CFTC Rules 1.73/1.74/39.12 (to verify), set separate timing for clearing members and CCPs. | Keep LD-C0023 as the parent, with children Clearing Member Acceptance and CCP Registration (as in review 03). Note: "Acceptance is evidence of, not identical to, CCP Interposition." | High | High |
| LD-C0011 Segregation Model | No regulatory frame. EMIR Art. 39: CCPs and clearing members offer at least omnibus and individual client segregation and disclose protection levels and costs (paragraphs to verify). Indirect-clearing RTS: 2017/2154 for ETD, 2017/2155 for OTC (to verify). US: futures customer segregation (Part 1), LSOC (Part 22), Part 30 secured amount. | Add: "Offered at a stated level (CCP, clearing member, indirect) under a named regime. The legal protection outcome (insolvency remoteness, portability) is a Legal conclusion, never inferred from the model name." | High | High |
| LD-C0010 Account | The EMIR 3 Active Account Requirement (Art. 7a, Reg. (EU) 2024/2987) qualifies an account at an EU CCP. The definition cannot carry that qualification. | Note: "Regulatory qualifications of an account (active-account status, segregation regime) are time-bounded, evidenced classifications, never inferred from labels." | Med | High |
| LD-C0004 Client | The regulatory "client" differs by text. EMIR Art. 2(15) is a contractual clearing relationship, matching the sponsor's choice. The MiFID II client (Art. 4(1)(9)) is broader. CFTC "customer" is the FCM relationship. | Add contextual aliases "EMIR client", "MiFID client" and "CFTC customer". Regulatory categories never attach to the Client role generically (§5). | Med | High |
| LD-C0002 Legal Entity | Holds the entity-level statuses (EMIR class, authorisations), but nothing says so. | Note: "Holder of entity-level Regulatory Classifications; identified by LEI (ISO 17442). A branch is not a separate entity, though some regimes attach duties to branches (to verify)." | Med | High |
| LD-C0009 Trading Venue | The venue type changes treatment. EMIR Art. 2(7): a derivative not executed on a regulated market or an equivalent third-country market (Art. 2a) is OTC, so MTF/OTF trades count as OTC. MiFIR Art. 29(1): RM-traded derivatives must be cleared. | Note: "Venue type (RM/MTF/OTF; DCM/SEF; equivalent third-country market) is a Regulatory Classification." Identify the venue by ISO 10383 MIC. | Med | High |
| LD-C0018 Trade | No regulatory identity. EMIR and CFTC Part 45 reports carry a UTI (ISO 23897). Cleared successor trades get new UTIs linked to the predecessor (EMIR Refit "prior UTI"; field to verify). | Note: "UTIs are per regime. Keep the predecessor/successor lineage (LD-R0014), including the UTIs." | Med | High |
| LD-C0019 Transaction | MiFIR "transaction" (Art. 26; RTS 22, Delegated Reg. (EU) 2017/590) is a binding reporting unit. | Keep deferred. Make "MiFIR transaction" an *ambiguous* alias. | Low | High |
| LD-C0012 Agreement | The client clearing legal structure belongs to the clearing agreement, not to the CCP or the segregation model. | Add the attribute "client clearing legal model" (values in §4; replaces v1 NEW-REG-06). Legal-validated. | Med | High |
| Taxonomy "Regulatory" | Missing an attachment level and date roles. | Add the axis attachment level {legal entity, role assignment, account, trade/report, CCP/venue/service}. Regulatory dates (publication, entry into force, application, phase-in, transitional end) become values of the shared Date Role vocabulary (07 NEW-REF-06). | Med | High |

## 3. Answers to open ambiguities and EV questions

**LD-A0009 Cleared.** A trade is cleared when the CCP has become legal counterparty under its rules (CCP Interposition), not when a status says "accepted".
- Under open offer, the CCP contract can arise at matching, before any registration message.
- Under novation, the CCP contract arises at registration, and the original trade is extinguished.
- A give-up changes which member holds the trade, not whether it is cleared.
- A venue-executed derivative rejected by the CCP is void or cancelled under venue rules (RTS 26 in the EU; CFTC staff practice in the US; to verify).
- Under EMIR, clearing also terminates the original report.

Confidence: high on the principle, medium on per-CCP timing. Basis: CCP rulebooks, PFMI Principles 1 and 8, Settlement Finality Directive 98/26/EC. **Legal decision needed:** the interposition timestamp, per Clearing Service.

**LD-A0017 Novation and acceptance.** Keep four distinct events: clearing-member acceptance, CCP acceptance/registration, CCP Interposition (with its mechanism), and settlement finality (out of P1).
- EU principal-to-principal model: the client's contract is a back-to-back transaction with the clearing member, created by the client clearing agreement, not by the CCP's novation.
- US models: the FCM guarantees performance. Whether customer or FCM is principal to the CCP contract varies by product and rulebook (futures vs cleared swaps).

Confidence high. **Firm decision needed:** Q2.

**LD-A0006 Client (regulatory facet).** Entity-level statuses (EMIR FC/NFC+/NFC−/small FC, authorisations) attach to the Legal Entity. Relationship-level statuses (MiFID retail/professional/eligible counterparty, opt-up/down) attach to the Party Role Assignment. Compatible with the sponsor's decision. Confidence high.

**LD-A0007 Account.** Segregation regime and active-account status are separate dimensions, each time-bounded. Confidence high.

**LD-A0008 Trade / transaction.** EMIR reports per trade (UTI) and per lifecycle event. MiFIR reports per execution by each investment firm. These are different reporting units over the same activity. The sponsor's deferral is respected. Confidence high.

**LD-A0012 Variation margin (prudential facet).** Settled-to-market vs collateralised-to-market is a rulebook term, set per CCP, service and date. It changes the legal nature of the payment, and so how exposure is measured for capital and accounting. Confidence medium-high. **Legal/Finance decision needed** per service; review 04 owns the concept.

**EV-001-Q02 (active account).** The public layer states the conditions, not the answer. The agent needs:
1. the client legal entity (LEI) and whether it is EU-established;
2. its EMIR class and clearing-threshold status per asset class, with as-of date, basis and source;
3. the product categories listed in Art. 7a;
4. activity levels, if representativeness conditions apply;
5. exemptions (e.g. intragroup);
6. the application and phase-in dates;
7. whether the client already clears at an EU CCP.

Clearing providers have their own duty to inform clients (Art. 7c, to verify). Commercial group membership is irrelevant to status. Threshold calculations may use the regulatory group, and EMIR 3 changed the calculation basis (to verify). Confidence: high on structure, medium on detail.

**EV-002-Q01/Q03 (regulatory facet).**
- Q01: EMIR Art. 4(3) and MiFIR Art. 30 recognise three routes: clearing member, client, or indirect clearing. Sponsored and direct-client models are CCP implementations of these routes.
- Q01: for a third-country CCP, its EMIR recognition (Art. 25) and its QCCP status (capital cost) are onboarding steps.
- Q03: under EMIR, at least omnibus and individual segregation must be offered and disclosed. If indirect clearing is offered, the RTS account types apply. FRANDT commercial terms also apply (Art. 4(3a); RTS 2021/1456, to verify). Other regimes differ.

Confidence high.

## 4. Proposed new concepts

| Temp ID | Name [FR] | Module | Type | Definition | Key relationships | Standard alignment (to verify) | Prio | Serves |
|---|---|---|---|---|---|---|---|---|
| NEW-REG-01 | Regulatory Regime [Régime réglementaire] | Common | Reference Concept | Body of binding rules identified by issuing authority, jurisdiction and legal instruments, applicable during an effective period (instances: EMIR, UK EMIR, MiFIR, CEA/CFTC rules). It is a concept rather than a vocabulary because equivalence and recognition decisions relate regimes to each other. | comprises Rule Provision; issued_by authority; deemed_equivalent_to Regime (dated) | FIBO regulatory concepts; ISO 3166 | P1 | EV-001-Q02, EV-002-Q03 |
| NEW-REG-02 | Regulatory Obligation [Obligation réglementaire] | Common | Obligation | Duty a regime imposes on parties holding a stated classification or role, for a defined product/activity scope, with application dates and conditions. Values: clearing, trading, active account, segregation offering, FRANDT, reporting, position limits, best execution, disclosure. | defined_in Rule Provision; conditioned_on Regulatory Classification / Party Role; scoped_by Regulated Derivative Class (03 NEW-OTC-03) | — | P1 | EV-001-Q02, EV-002-Q03 |
| NEW-REG-03 | Regulatory Classification [Classification réglementaire] | Common | State | Time-bounded status of a legal entity, role assignment, account, venue or CCP/service under a named regime. Carries basis (self-assessment, notification, authority decision, calculation), asserting source and evidence. "Unknown" is a value, never a default. Uses the same assertion pattern as 07 NEW-OPS-03. | classifies LD-C0002 / Role Assignment / LD-C0010 / LD-C0009 / LD-C0008 (Clearing Service); under Regime | EMIR Art. 2(8)–(9), 4a, 10, 25; MiFID II Annex II, Art. 30; CRR Art. 4(1)(88) | P1 | EV-001-Q02, EV-002-Q01, GDI "third-country CCP recognition" |
| NEW-REG-04 | Rule Provision [Disposition réglementaire] | Common | Reference Concept | Versioned, citable unit of a regulation, technical standard, guidance, CCP rulebook/procedure or venue rule, with issuer, version and effective period. Deadlines and thresholds are its parameters. | part_of Regime or rulebook; supersedes Rule Provision; constrains LD-C concepts / Clearing Service | ELI for EU acts | P1 | EV-001-Q04, EV-003-Q05 |
| NEW-REG-05 | Rule Change [Changement de règle] | Common | Event | New, amended, withdrawn or proposed Rule Provision, Fee Schedule (LD-C0032) or published model parameter. Has a status (consultation, adopted, in force, applicable) and role-qualified dates. It is the trigger object of change impact. | changes Rule Provision / LD-C0032; announced_in Change Notice; affects (n-ary, §5) | CFTC Part 40; EMIR Art. 49 (instances) | P1 | all EV-001, EV-005-Q01 |
| NEW-REG-07 | CCP Interposition [Interposition de la CCP] | Common | Event | Event by which a CCP becomes counterparty to each side of a trade under its rules, at the moment the rulebook defines, by mechanism {novation, open offer, other}. It is the legal meaning of "cleared"; "cleared" itself is a derived status. | concerns LD-C0018; effected_by LD-C0008 in a Clearing Service; evidenced_by LD-C0023; creates successor Trades (LD-R0014) | PFMI Principle 1; CDM/FpML clearing events | P1 | EV-003-Q02, EV-003-Q03 |
| NEW-REG-08 | Regulatory Report [Déclaration réglementaire] | Common | Instruction | Submission of trade, transaction or position data under a regime, with responsible and reporting party and identifiers (UTI, UPI/ISIN, LEI). | reports LD-C0018/0017/0026; under Regime | ISO 20022; ISO 23897/4914/17442 | **P3** (no EV question yet) | Placeholder |

**Withdrawn from v1:**
- **NEW-REG-06 Client Clearing Legal Model** becomes a Legal-validated attribute of the client clearing agreement or access arrangement. Values: principal-to-principal (back-to-back), agency/guarantee (FCM-type), indirect chain. Commercial labels such as "sponsored" or "direct" map to these values per CCP.
- **NEW-REG-09** is merged into 04 NEW-MC-08 Default Fund Contribution. Its prudential treatment (CRR Art. 307–309, to verify) is a P3 note.

The following are values or bases of NEW-REG-02/03, not concepts: individual obligations, clearing threshold, QCCP, equivalence decisions.

## 5. Relationships

| Subject – predicate – object | Notes |
|---|---|
| Regulatory Regime – comprises – Rule Provision | A CCP rulebook belongs to the CCP (a Party), not to a Regime; its provisions use the same concept with a rulebook parent. |
| Rule Provision – supersedes – Rule Provision | Temporal succession; answers EV-001-Q04. |
| Rule Change – changes – Rule Provision / LD-C0032 | Change type: new / amend / withdraw / propose. Dates qualified by Date Role. |
| Rule Change – affects – LD-C concept or Clearing Service | n-ary: impact type (scope, timing, data, legal effect, cost), affected role, confidence, `interpretation_required`. The core edge for AG-002. |
| Regulatory Obligation – conditioned_on – Regulatory Classification / Party Role | Applicability = classification × product scope × date. A pattern, never a universal fact. |
| Legal Entity – subject_to – Regulatory Obligation | Contextual assertion (scope, period, basis, evidence, asserted_by Legal/Compliance). **Instances are internal-zone only.** |
| Regulatory Classification – classifies – LD-C0002 / Party Role Assignment (08 NEW-COM-02) / LD-C0010 / LD-C0009 / LD-C0008 or Clearing Service | Entity status (NFC+ per asset class); relationship status (MiFID category); active account; venue type; recognition tier. |
| CCP Interposition – evidenced_by – LD-C0023; – has_mechanism – {LD-C0024, open offer, other} | Reframes LD-R0013/R0014: acceptance is evidence, interposition is the legal effect. |
| Segregation Model – offered_at – level – under – Regime | Serves EV-002-Q03. |

**Attachment rule.** Regulatory classifications attach to the Legal Entity, or to the Role Assignment for relationship-level statuses. They never attach to the Client role as such, nor to a commercial group. When a calculation uses a regulatory consolidation group, that group is not the commercial Client Group. Each classification records regime, asset class where relevant, basis, effective period and as-of evidence.

## 6. Proposed new ambiguity entries

| Temp ID | Term | Required distinction | Reviewer |
|---|---|---|---|
| NEW-A-REG-01 | "Client" in regulatory texts | EMIR client vs MiFID client vs CFTC customer vs LD-C0004; indirect client. | Legal / Compliance |
| NEW-A-REG-02 | "OTC" / "listed" | EMIR Art. 2(7) makes MTF/OTF trades OTC; equivalence changes the treatment; "cleared" is a separate dimension. | Legal / Product |
| NEW-A-REG-03 | "Effective date" | **Merged** into one canonical entry (§8b). | — |
| NEW-A-REG-04 | Classification ownership and staleness | Self-declared vs firm-determined; calculation group vs entity status; stale or missing evidence means "unknown", not NFC−. | Compliance / Client Data |
| NEW-A-REG-05 | "Protected" / "segregated" / "portable" | Model offered vs legal insolvency protection vs porting achieved. Only Legal concludes on protection. | Legal / Clearing Product |
| NEW-A-REG-06 | Fact vs interpretation | Rule text vs industry reading vs firm applicability (EV-005-Q01). | Legal / Sponsor |
| NEW-A-REG-07 | "Group" | Regulatory consolidation group (EMIR thresholds, CRR) vs commercial Client Group vs CCP "affiliate" vs GLEIF parent (EV-001-Q02). | Compliance / Client Data |

## 7. Questions only the business owner or internal sources can answer

1. **Which regimes first?** This sets the Regime instances. *Default:* EU (EMIR/EMIR 3, MiFID II/MiFIR, CRR) plus UK at P1; US CFTC/SEC, in general terms, at P2.
2. **Client clearing legal model per entity and service**, and whether indirect clearing is offered. This decides EV-003-Q02. *Default:* model all values; every firm fact is TO VALIDATE by Legal.
3. **Which firm legal entities and branches act as clearing member, executing broker or FCM-type registrant, under which regime?** Obligations attach to them. *Default:* recorded in the internal overlay only.
4. **Who is the authoritative owner of counterparty classifications** (EMIR class, MiFID category)? *Default:* Compliance / Client Data, always cited with an as-of date.
5. **Should consultations and drafts count as change events?** *Default:* yes, with a mandatory status and a "not yet law" flag.
6. **Is prudential cost (CCP exposures, default fund, leverage) inside the UC-004 contribution perimeter?** *Default:* no; P3, as in review 04's Q6.
7. **Who signs off `interpretation_required` outputs?** *Default:* Legal/Compliance; labelled "public-layer reading, not legal advice".

## 8. Cross-review

**(a) Disagreements**
- **02 NEW-COM-02 Open Offer as an Event.** Open offer is a standing mechanism in the rulebook; the event is the interposition it produces. A sibling of Novation also fails because Novation exists outside clearing. Proposal: one concept, CCP Interposition, with a mechanism attribute.
- **02 and 08 narrowing LD-C0023 to the CCP.** This is a meaning change. Review 03's approach (parent plus two children) gives the same precision without a migration.
- **02 on LD-A0009** ("cleared when registered"). Registration is evidence. Under open offer the contract can arise before registration, so the agent must state the rulebook moment.
- **03 on LD-C0024** ("US client is party to the CCP contract"). This holds for some cleared-swap rulebooks, not for US futures. It should be qualified per product and DCO.
- **02 NEW-ETD-03** ("FCM" as an alias of Clearing Broker). FCM is a regulatory registration, i.e. a value of NEW-REG-03. I agree with 03 NEW-A-OTC-04.
- **05 NEW-COM-10 Regime at P2.** It must be P1, for EV-001-Q02 and EV-002-Q03. Jurisdiction is a vocabulary, not a separate concept.
- **My own v1.** NEW-REG-06 and NEW-REG-09 were over-modelled (see §4).

**(b) Duplicates: one canonical name each**

| Canonical | Merges |
|---|---|
| **Rule Provision** (NEW-REG-04) | 05 NEW-COM-05; 08 NEW-COM-03 |
| **Rule Change** (Event; NEW-REG-05) | 02 NEW-COM-06; 08 NEW-COM-04; event part of 05 NEW-COM-04 |
| **Change Notice** (Reference Concept, P2): the published document (circular, consultation, OJ act, guidance) announcing 1..n Rule Changes. It is evidence, not an event; GDI items point to it. | 02 NEW-COM-07; document part of 05 NEW-COM-04 |
| **Regulatory Regime** | 05 NEW-COM-10 |
| **Regulatory Obligation** (NEW-REG-02, with 03's subtypes) | 03 NEW-COM-04 |
| **Regulated Derivative Class** (03 NEW-OTC-03, widened to any regulatory product scope, e.g. Art. 7a categories) | my v1 "regulatory class" axis |
| **Clearing Service** (also the unit of EMIR service authorisation) | 02/03 NEW-COM-01, 05 NEW-COM-03, 08 NEW-COM-01 |
| **Clearing Member Acceptance** and **CCP Registration** (children of LD-C0023) | 02 NEW-ETD-06, 03 NEW-COM-02/03, 08 NEW-ETD-01 |
| **Market Access Arrangement** (05's name; type {direct membership, client clearing, indirect, sponsored/DEA}; scope {venue, clearing service}; legal model as an attribute) | 02 NEW-COM-03, 08 NEW-COM-05, my NEW-REG-06 |
| **Default Fund Contribution** (04 NEW-MC-08) | my NEW-REG-09 |
| **Porting** (EMIR Art. 48(5)–(6), to verify) | 02 NEW-COM-04, 03 NEW-COM-08 |
| **Identifier / Identifier Scheme** (07 NEW-REF-01/02; UTI is a scheme) | 03 NEW-COM-05 |
| **Date Role** (07 NEW-REF-06), including the regulatory dates | my taxonomy proposal |
| Ambiguity **"Effective date"** (publication / entry into force / application / phase-in / transitional end, plus record time) | 02 NEW-A-04, 05 NEW-A-04, 08 NEW-AMB-02, NEW-A-REG-03 |
| Ambiguity **"Clearing broker vs clearing member vs FCM"** | 02 NEW-A-01, 03 NEW-A-OTC-04, 08 NEW-AMB-01 |

**(c) Raised by others, affecting my domain**
- **08 NEW-COM-02 Party Role Assignment** (with the LD-C0003 meaning change) is a prerequisite for my attachment rule. I endorse it.
- **07 bitemporal convention.** Classifications need both valid time and record time ("NFC− as known at T").
- **04 LD-C0047.** The title-transfer vs security-interest distinction (Directive 2002/47/EC) drives the segregation and insolvency outcomes behind NEW-A-REG-05. For NEW-MC-10, the transparency duties are in EMIR Art. 38 as amended by Refit and EMIR 3 (paragraphs to verify).
- **05 Client Group** must not be used for threshold calculations (NEW-A-REG-07).
- **01 references** (MiFID II Art. 4(1)(41) and 17(5) DEA, RTS 22 capacity, RTS 25) look right. DEA is a classification of the access arrangement.
- **05 hub fix.** Each UC concept list should cover its EV concepts. UC-001 should also list the regulatory concepts once they have IDs.
