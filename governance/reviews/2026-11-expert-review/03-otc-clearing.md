# Review 03 (v2): OTC Client Clearing

Scope: cleared IRS, index CDS and FX NDF. Element names, article numbers and dates marked "to verify" must be checked against the published texts before adoption. My own temporary IDs use `NEW-OTC-nn`, because reviewers 02, 05 and 08 reuse `NEW-COM-nn` with different meanings.

## 1. Verdict

The OTC principles are right: acceptance is kept apart from legal effect (LD-C0023/0024, LD-A0009/0017), and identity from records (LD-C0018). The vocabulary is ETD-shaped. Member credit acceptance is not separated from CCP registration, and CCP legal interposition has no name. The executed ("alpha") trade has no lineage to the cleared trades that replace it. There is no clearing tier, clearing obligation, compression or porting. LD-A0016 closes with a three-layer rule (Product / Instrument / Trade terms). Five OTC proposals, plus shared concepts from other reviewers, would let AG-004 (UC-003) and AG-002 (UC-001) answer OTC questions without inventing structure.

## 2. Corrections to existing items

| ID | Issue | Proposed change | Sev. | Conf. |
|---|---|---|---|---|
| LD-C0014 Instrument | "Can be traded or contracted" absorbs every bespoke OTC trade, so each swap would become its own instrument. | **Explicit meaning change** (rationale: LD-A0016): "Standardised derivative specification, identifiable independently of any counterparty pair and any single trade, at the level at which it is listed or assigned an instrument identifier." Usage note: an OTC derivative has an Instrument only where a standard identifier is assigned (e.g. an OTC ISIN for EU venue-traded derivatives). Even then, trades with the same ISIN can differ in fixed rate and notional, so the Trade still carries the full terms. | High | High |
| LD-C0013 Product | The definition has no OTC anchor. | Usage note: OTC product classification aligns with the ISDA OTC taxonomy (asset class / base product / sub-product), ISO 10962 CFI, and UPI (ISO 4914, issued by the ANNA DSB). The UPI identifies a product at its finest reference-data level, with no counterparties and no maturity date (to verify). | Med | High |
| LD-C0018 Trade | Clearing extinguishes the executed bilateral trade and creates new ones: one CCP-facing trade per cleared side and, under the EU principal model, a clearing-member–client trade. "Subsequent legal transformations" gives no structure for this. | Keep the definition. Add rules: (1) A trade has exactly one pair of counterparties. Clearing, compression and porting create successor Trades linked by lineage (NEW-R-OTC-05); they never mutate the predecessor. (2) Each trade sits in one Clearing Tier (NEW-OTC-03). (3) A bespoke OTC Trade carries its own economic terms (CDM `EconomicTerms`/`Payout`; FpML product elements, to verify); there is no per-trade Instrument. Contextual alias: "alpha trade" (OTC) for the pre-clearing trade. | High | High |
| LD-C0023 Clearing Acceptance | It merges two decisions with separate regulatory timing rules: the clearing member's acceptance and the CCP's acceptance. EU: MiFIR Art. 29 and RTS 26 (Delegated Reg. (EU) 2017/582). US: CFTC rules on FCM acceptance, SD submission and DCO acceptance (Reg. 1.74, 23.506, 39.12(b)(7), to verify). | Narrow it to CCP acceptance/registration in a Clearing Service. This is consistent with LD-R0013 and with reviewers 02 and 08, so it is a clarification, but record it. Member-side acceptance becomes NEW-OTC-01. A rejection is an outcome value of each concept, not a separate failure concept. | High | High |
| LD-C0024 Novation | In OTC, "novation" means two things: the CCP's clearing novation of the alpha trade, and the bilateral step-out/step-in of an uncleared or pre-clearing trade (ISDA novation practice). Open offer is not a novation, and porting mechanics are rulebook-specific. | Keep it generic. Usage note: clearing novation is one mechanism of CCP Interposition (reviewer 06 NEW-REG-07). Bilateral novation is a lifecycle event. Never infer novation from "cleared" or "ported". See NEW-A-OTC-03. | Med | High |
| LD-C0022 Give-up / Take-up | Agents may map OTC flows onto it. OTC/FX "give-up" usually means a prime-brokerage give-up (the trade moves to a prime broker, which may then clear it), a different process. | Scope note: "ETD process; OTC trades reach a CCP by Clearing Submission (NEW-OTC-02); OTC/FX 'give-up' is an *ambiguous* alias." No meaning change. | Med | High |
| LD-C0007 Clearing Member | OTC membership is specific to a clearing service: IRS, CDS and FX services have separate admission and often separate default funds. "FCM" is a US registration status, not a role. | Point to Clearing Service (§8b). Alias "FCM": *contextual* (US regulatory status, held by a legal entity). Alias "clearing broker": *ambiguous*. | Med | High |
| LD-C0011 Segregation Model | No OTC anchors. | Reference instances (not subclasses): EMIR Art. 39(2)/(3); CFTC Part 22 LSOC; basic and gross omnibus indirect accounts (Delegated Reg. (EU) 2017/2155 for OTC, 2017/2154 for ETD; to verify). | Low | High |
| LD-C0025 Lifecycle Event | Economic changes are not distinguished from technical corrections. | Lifecycle facet (taxonomy, not concepts) aligned to CDM `EventIntentEnum` and FpML event messages (to verify): affirmation, submission, member/CCP acceptance or rejection, interposition, amendment vs correction, partial/full termination, increase, bilateral novation, compression, porting/transfer, swaption exercise, reset, payment, CDS credit event/succession, benchmark transition. | Med | High |
| LD-C0026 Position | An OTC position is a set of open cleared trades, not lots. | LD-A0013 qualifiers: measure basis (trade count / notional / DV01 or CS01), Clearing Service, Clearing Tier. | Med | High |
| LD-C0045 VM Requirement | Price alignment has no home. | Usage note: under collateralised-to-market (CTM) treatment, price alignment interest (PAI) is interest on VM collateral. Under settled-to-market (STM), the price alignment amount (PAA) is part of the daily settlement amount (LD-C0028). The treatment is a fact about service × account type × currency × date. | Med | Med |

## 3. Answers to open ambiguities and EV questions

**LD-A0016 Product / Instrument / OTC contract.** Use three layers:
1. Product (LD-C0013) is the economic family (e.g. fixed-float OIS), with the UPI as the identifier at its finest level.
2. Instrument (LD-C0014) is a standardised specification with its own identifier (a listed series, or an OTC ISIN).
3. Trade terms are dates, notional, rates, schedules and day counts. They belong to the Trade.

Clearing eligibility relates Product to Clearing Service, bounded by trade-term ranges (currency, index, maximum tenor). The clearing obligation attaches to a regulator-defined class (type, index, settlement currency, maturity range, notional type, optionality; EMIR delegated regulations, to verify), evaluated on Product + trade terms. Confidence: high. Firm decision: Q8.

**LD-A0009 Cleared.** For OTC, "cleared" means that CCP Interposition has occurred in a named Clearing Service. Three timestamps must stay distinct: member acceptance, CCP acceptance/registration, and interposition (the rulebook defines the legal moment). Usually the last two coincide. A venue-executed trade that the CCP rejects is void under venue rules (US: CFTC staff STP guidance; EU: RTS 26; both to verify). An off-venue rejected trade survives or terminates according to the parties' execution agreement. Confidence: high on the distinctions, medium on voidness details.

**LD-A0017 Novation and acceptance.** Not universal, confirmed. EU OTC rulebooks commonly interpose by novation at registration. Under the US agency (FCM) model, the FCM carries and guarantees the customer's swap with the DCO. Under the EU principal model, the member–client trade arises from the client clearing agreement, not from the CCP's novation. Confidence: high; evidence per service.

**LD-A0008 (OTC aspect).** One SEF/MTF execution, or one block allocated before submission, gives 1..n alpha trades. Each alpha gives two CCP-facing trades, plus up to two client-facing trades under the principal model. Lineage, not cardinality, consistent with sponsor decision 6. Confidence: high.

**LD-A0012 (OTC aspect).** OTC VM was historically CTM with PAI. Several OTC CCPs converted some or all accounts to STM with PAA (per service, to verify). The 2020 discounting/PAI switches to €STR and SOFR at the major swap CCPs make a good UC-001 test case (VM, PAI, valuation and compensation flows all changed). Firm/Legal decision per service.

**LD-A0015 (OTC aspect).** Distinct date roles: execution timestamp (UTC), trade date, submission timestamp, CCP registration timestamp, CCP clearing business date (cut-off driven), effective date, termination date, fixing and payment dates. Backloaded trades clear long after their trade date. Confidence: high.

**EV-002-Q02 (OTC answer).** OTC has no give-up agreement. It needs (i) an execution-side agreement for trades intended to be cleared (FIA–ISDA Cleared Derivatives Execution Agreement, title to verify), or the venue rulebook for SEF/MTF trades; (ii) a client clearing agreement per clearing member (EU: ISDA/FIA Client Cleared OTC Derivatives Addendum or equivalent; US: FCM customer agreement with cleared-swaps terms; to verify); (iii) the member's admission to the CCP service. Confidence: medium-high.

**EV-003-Q02 (OTC answer).** Before CCP acceptance, an off-venue trade is a bilateral contract between the executing parties. For venue trades, the member's pre-execution limit check commits it to accept trades within the limit (US FCM screening; EU RTS 26 pre-check, to verify).

## 4. Proposed new concepts

| Temp ID | Name | Module | Type | Definition | Key relationships | Standard alignment (to verify) | Prio | Use case |
|---|---|---|---|---|---|---|---|---|
| NEW-OTC-01 | Clearing Member Acceptance | Common | Event | Decision by a clearing member to accept or reject clearing responsibility for a trade, a quantity of it, or a pre-set limit, for an identified client or account in a specified Clearing Service. | decided_by LD-C0007; concerns LD-C0018 or NEW-OTC-02; precedes LD-C0023. Qualifiers: timing (pre-execution limit / post-execution consent), context (OTC submission / ETD take-up), outcome. | CFTC Reg. 1.73/1.74; RTS 26; FpML clearing/consent messages; FIXML claim flows (ETD) | P1 | UC-003, UC-006, UC-001 (STP rule changes) |
| NEW-OTC-02 | Clearing Submission | OTC Clearing | Instruction | Instruction, sent by an executing party, a trading venue or an affirmation/matching platform, requesting that an identified trade be cleared in a Clearing Service through designated clearing member(s). | concerns LD-C0018; designates LD-C0007; targets Clearing Service; answered_by NEW-OTC-01 and LD-C0023. Qualifier: submission reason (new, post-allocation, backload, resubmission, transfer). | FpML `requestClearing`; CDM `ClearingInstruction` | P1 | UC-003 (OTC half), UC-006 (EV-006-Q01 analogue) |
| NEW-OTC-03 | Clearing Tier | Common | Reference Concept (governed vocabulary) | Position of a trade, account or margin relationship in the clearing chain. Values: pre-clearing (alpha); CCP–member house; CCP–member client account; member–client; client–indirect client; uncleared bilateral. | Qualifies LD-C0018, LD-C0010, LD-C0026, LD-C0043. Merge with reviewer 04's NEW-MC-02. | EMIR Art. 39; indirect-clearing RTS | P1 | UC-006 (EV-006-Q02/Q03), UC-001 (EV-001-Q03) |
| NEW-OTC-04 | Client Clearing Agreement | Common | Agreement (is_a LD-C0012) | Agreement under which a clearing member clears for a client in one or more Clearing Services, setting the legal model (principal / agency), segregation election, margin terms and porting/default provisions. | governs the CM–Client role assignment; elects LD-C0011; has legal model (reviewer 06 NEW-REG-06 as its vocabulary) | See EV-002-Q02 | P1 | UC-002 (EV-002-Q01/Q02), UC-001 |
| NEW-OTC-05 | Portfolio Compression | OTC Clearing | Event (is_a LD-C0025) | Risk-reduction event that terminates and/or replaces existing trades to reduce gross notional or trade count while keeping market risk within an agreed tolerance; run by a CCP (e.g. netting or coupon blending within one account) or by a multilateral compression service. | terminates LD-C0018 (1..n); creates LD-C0018 (0..n); within Clearing Service; may trigger LD-C0031 | MiFIR Art. 31, as amended by the MiFIR review on post-trade risk reduction (to verify); CDM compression intent | P2 | UC-001, UC-004 (compression fees), UC-005 (GDI "portfolio compression" gap) |

Cut from v1 or handled elsewhere: Trade Economic Terms (a rule on LD-C0018), CCP Registration (the narrowed LD-C0023), Regulatory Obligation, Trade Identifier and Porting (shared concepts, §8b), Indirect Client (an access-arrangement value), Regulated Derivative Class (a structured obligation scope, §5). Facets, not concepts: venue type and execution method (reviewer 01), affirmation (a lifecycle value, mapped to the GDI "trade matching" topic), and the execution agreement for cleared derivatives (an agreement-type value).

## 5. Proposed new/changed relationships

| Temp ID | Subject – predicate – object | Context / cardinality notes |
|---|---|---|
| NEW-R-OTC-01 | LD-C0018 – submitted_via – NEW-OTC-02 | 0..n, because a trade can be resubmitted after rejection. The submitter role is a qualifier. |
| NEW-R-OTC-02 | NEW-OTC-02 – designates – LD-C0007 | One per side to be cleared. Designation is not acceptance (mirrors LD-R0011). |
| NEW-R-OTC-03 | NEW-OTC-01 – decided_by – LD-C0007; NEW-OTC-01 – precedes – LD-C0023 | Typical, not universal. A pre-execution limit check precedes even the execution. State the order per service. |
| NEW-R-OTC-04 | LD-C0013 – eligible_in – Clearing Service | Effective-dated. Bounded by trade-term ranges. Eligibility ≠ obligation ≠ firm offering (NEW-A-OTC-02). |
| NEW-R-OTC-05 | LD-C0018 – succeeds – LD-C0018 | Generic directional lineage. The derivation event is a qualifier: interposition, compression, porting/transfer, bilateral novation, allocation. LD-R0014 stays as the novation-specific case. |
| NEW-R-OTC-06 | LD-C0018 / LD-C0010 / LD-C0043 – in_tier – NEW-OTC-03 | Exactly one tier per object. |
| NEW-R-OTC-07 | NEW-OTC-04 – governs – Client–Clearing Member role assignment; NEW-OTC-04 – elects – LD-C0011 | Refines LD-R0002 for clearing. Time-bounded. Per Clearing Service. |
| NEW-R-OTC-08 | Clearing obligation (an instance of reviewer 06 NEW-REG-02) – applies_to – a counterparty **pair** (classifications of both parties) × class scope (Product + trade terms) × date | OTC-specific: applicability depends on both counterparties, phase-in and exemptions (e.g. intragroup, the CFTC end-user exception in Part 50). Never infer it from the product alone. |
| NEW-R-OTC-09 | Identifier (reviewer 07 NEW-REF-01) – identifies – LD-C0018 | Successor trades carry new UTIs (ISO 23897), with a prior-UTI link. Which party generates the UTI for a cleared trade is regime-specific (EMIR Refit technical standards; CFTC Part 45; to verify). |

## 6. Proposed new ambiguity entries

| Temp ID | Term | Required distinction | Reviewer |
|---|---|---|---|
| NEW-A-OTC-01 | "The cleared trade" / "the trade" | The alpha trade vs the CCP-facing trade vs the client-facing trade. State which tier, which UTI and which counterparty view a question uses. | OTC Clearing Product / Operations |
| NEW-A-OTC-02 | "Eligible", "mandatory", "clearable", "offered" | CCP eligibility vs the regulatory clearing obligation for a counterparty pair vs voluntary clearing (e.g. NDFs, currently not under an EU or US mandate; to verify) vs the firm's offering. | Legal / Compliance / Product |
| NEW-A-OTC-03 | "Novation" (OTC) | CCP clearing novation vs bilateral step-out/step-in vs porting or transfer between clearing members. | Legal / OTC Operations |
| NEW-A-OTC-04 | "Unwind", "termination", "amendment" | Client intent vs recorded events. A cleared unwind is usually an offsetting trade followed by compression. Economic amendments are usually cancel-and-resubmit (CCP-specific). | OTC Clearing Product / Operations |

## 7. Questions only the business owner can answer

1. **Which OTC products and CCP services are in Phase 2 scope?** Sets taxonomy and CDM payout coverage. *Default:* IRS first; index CDS and NDF as facet values.
2. **Which legal models are offered: EU principal, US agency, or both?** Fixes successor-trade count and the client's counterparty. *Default:* both, per service (same as reviewer 06's Q2; ask once).
3. **Are indirect, sponsored or direct-client models offered or planned for OTC?** *Default:* access-arrangement values only.
4. **When operations or finance say "the trade", which tier is meant?** Drives UC-004 attribution and UC-006 status. *Default:* separate objects with lineage; revenue attaches to the client-facing tier.
5. **Is executing-dealer business (client clears elsewhere) in scope?** *Default:* yes, as an agreement-type value.
6. **Where do clearing-member limit checks occur: pre-execution, post-execution, or both?** Affects NEW-R-OTC-03 and failure analysis. *Default:* both, with a timing qualifier.
7. **Which OTC charge bases count as management revenue (registration, maintenance, compression, porting, pass-through CCP fees)?** OTC part of LD-A0002/0014. *Default:* charge-basis facet; pass-through excluded until Finance decides.
8. **Do internal reference data treat any OTC templates as instruments?** Residue of LD-A0016. *Default:* no.

## 8. Cross-review

**(a) Disagreements**
- **02 and 08 place Clearing Member Acceptance in the ETD module.** It belongs in Common. OTC needs it even more: CFTC Reg. 1.73/1.74 and RTS 26 cover swaps, and pre-execution limit checks are OTC-central. One concept with a context qualifier (NEW-OTC-01).
- **02 proposes Open Offer as a sibling of Novation.** I prefer 06's single CCP Interposition (NEW-REG-07), with mechanism ∈ {novation, open offer, other}. It gives agents one target for "cleared?". Open offer has no predecessor contract, so it does not fit LD-R0014.
- **07 and 08 define Instrument as a listed series with an ISIN.** That is correct for ETD but excludes OTC ISINs. Use the counterparty-independent wording above, and keep 07's rule that a bespoke OTC contract is a Trade.
- **06: "Product/Instrument need only a regulatory-class axis".** This is insufficient for OTC. EMIR classes include maturity range and notional type, which are trade terms, and applicability is pair-based (NEW-R-OTC-08). NEW-REG-02's scope must be structured accordingly.
- **04 NEW-MC-11 Collateral Remuneration includes price alignment.** That holds for PAI under CTM only. Under STM, the PAA is part of the settlement obligation and must not be counted as collateral remuneration.
- **08's generic "Service"** merges the CCP's Clearing Service with the firm's Service Offering (05). Keep them apart.

**(b) Duplicates and proposed canonical names**

| Canonical name | Duplicates | Canonical definition / note |
|---|---|---|
| Clearing Service (Common, Entity) | 02 NEW-COM-01; 05 NEW-COM-03; 08 NEW-COM-01 (partly) | "Distinct clearing offering of a CCP, defined by its rulebook scope, eligible products, membership categories, account structures and default-management resources." |
| Clearing Member Acceptance | 02 NEW-ETD-06; 08 NEW-ETD-01; NEW-OTC-01 | One concept, in Common. |
| CCP Interposition | 06 NEW-REG-07; 02 NEW-COM-02 | Mechanism is an attribute. |
| Porting (Common, Process) | 02 NEW-COM-04; my v1 | "Transfer, under a CCP's default rules, of a client's positions and associated collateral from a defaulting clearing member to a back-up clearing member, or their close-out and return of collateral where transfer fails" (EMIR Art. 48(5)–(6)). Voluntary moves are Position Transfer (02 NEW-ETD-08), which should move to Common because OTC client transfers between members also exist. |
| Market Access Arrangement | 02 NEW-COM-03; 05 NEW-COM-02; 08 NEW-COM-05 | 05's broader name. Clearing values: direct membership, client clearing, indirect clearing, sponsored/direct-client models. |
| Rule Provision + Rule Change | 06 NEW-REG-04/05; 05 NEW-COM-04/05; 02 NEW-COM-06/07; 08 NEW-COM-03/04 | 06's definitions. |
| Identifier (+ Scheme); Regulatory Obligation / Classification | 07 NEW-REF-01/02; 06 NEW-REG-02/03; my v1 Trade Identifier and Regulatory Obligation (withdrawn) | Use 07's and 06's concepts. |
| Clearing Tier | 04 NEW-MC-02; NEW-OTC-03 | One vocabulary. |
| Default Fund Contribution; Give-up Agreement; Margin Methodology | 04 NEW-MC-08 = 06 NEW-REG-09; 01 NEW-EXE-04 = 02 NEW-ETD-05 = 08 NEW-COM-07; 04 NEW-MC-01 = 05 NEW-RSK-01 | One concept each, in Common. Give-up Agreement has no OTC counterpart. |
| Ambiguities: clearing broker (add "FCM"); effective date; "product" | 02 NEW-A-01 = 08 NEW-AMB-01; 02/05 NEW-A-04 = 06 NEW-A-REG-03 = 08 NEW-AMB-02; 05 NEW-A-02 = 07 NEW-A-03 | One entry each. |

**(c) Points raised by others that affect OTC**
- **06:** under EMIR Art. 2(7), MTF/OTF-executed derivatives are OTC, so the OTC module must not be defined as "off-venue". The EMIR 3 Active Account Requirement (Art. 7a) targets specified OTC IRD/STIR categories (to verify), so EV-001-Q02 is an OTC question.
- **04:** STM/CTM as a service attribute, and client IM multipliers (NEW-MC-10), are standard in OTC client clearing. Both are endorsed.
- **07:** Status Assignment and Business Record are needed for CCP clearing-status messages and for UTI/CCP-ID cross-referencing.
- **01:** Execution Method should gain OTC values: RFQ or order book on SEF/MTF/OTF, and bilateral off-venue. STP timing differs by these values. Allocation Instruction precedes Clearing Submission for block trades in OTC.
- **05:** Fee Charge `arises_from` needs OTC triggers: registration, periodic maintenance per open trade, compression and porting.
- **08:** I endorse front-matter alignments with SKOS match plus `verified: false`. All standard names in this review are written on that basis.
