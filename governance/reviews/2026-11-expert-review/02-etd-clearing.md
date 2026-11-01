# Review 02 — ETD Clearing (listed derivatives clearing), v2

"To verify" = not checked against the current text. My temp IDs are NEW-ETD-nn whatever the target module, since other reviews reuse NEW-COM-nn for different things.

## 1. Verdict

The foundation gets the hardest ETD principle right: instruction, acceptance and legal effect are kept apart (LD-C0022/0023/0024, LD-A0009/0010/0017). What it lacks are the anchors those principles hang on:
- "Clearing service" is used in LD-C0007 and LD-C0023 but never defined.
- Nothing separates a clearing broker from a clearing member, a member's take-up from CCP registration, or a CCP account from an internal account.
- Novation is the only interposition mechanism, and there are no position events.

AG-004, AG-003 and AG-002 reason over exactly these objects. Seven P1 and five P2/P3 concepts plus ten corrections close the gap. Membership categories, fee types and physical delivery should stay qualifiers or taxonomy values.

## 2. Corrections to existing items

| ID | Issue | Proposed change | Sev. | Conf. |
|---|---|---|---|---|
| LD-C0007 Clearing Member | Points to an undefined "clearing service" and does not say what the role entitles its holder to. Agents treat "clearing broker", "FCM" and "non-clearing member" as variants of it. | "Role of a party admitted to a Clearing Service (NEW-ETD-01) under a membership category, entitling it to have transactions registered in its name in CCP accounts within that category's clearing scope." Exclusions: a non-clearing member is a venue member without this role (R01 NEW-EXE-05). FCM is a US registration. Clearing broker is a separate role (NEW-ETD-03). | High | High |
| LD-C0008 Central Counterparty | Mixes the role with its services and with the entity's regulatory status. | Keep the definition. Add "exercised through one or more Clearing Services". Regulatory status (authorised, recognised, QCCP) is a separate classification (agrees with R06). Align with EMIR Art. 2(1). "DCO" is a contextual alias (US). | Med | High |
| LD-C0005 Broker | A placeholder; it cannot resolve "clearing broker". | Keep it as an umbrella and add the specialisation NEW-ETD-03. A bare "broker" is *ambiguous* in ETD. | Med | High |
| LD-C0022 Give-up / Take-up | "Delivering and accepting a trade for clearing" implies the trade is not yet cleared. Where the CCP first registers the trade to the executing member (common in ETD), a give-up moves an already-cleared trade. Where a member is designated at trade time (e.g. CMTA-type arrangements in US listed options, to verify), attribution happens at registration. The giving side is missing. | "Process by which all or part of an executed trade is attributed for clearing from the executing side to a receiving clearing member, through a give-up instruction and that member's acceptance or rejection; depending on the Clearing Service it occurs at or after CCP registration." Qualifier `attribution timing`. Scope note: listed derivatives; "give-up" in OTC or FX prime brokerage is a contextual alias (agrees with R03). Add has_giving_member. | High | High |
| LD-C0023 Clearing Acceptance | The definition and LD-R0013 already describe the CCP side. Agents will still read it as the member's take-up, which MiFIR Art. 29(2), RTS 26 (Delegated Reg. (EU) 2017/582, to verify) and CFTC Reg. 1.73 (to verify) treat separately. | Clarification, not a meaning change: "Acceptance or registration of a trade by a CCP into a Clearing Service under defined criteria; evidence of, not identical to, CCP Interposition (NEW-ETD-02)." Alias "registration" (contextual). Add the sibling NEW-ETD-04. | High | High |
| LD-C0024 Novation | Agents will equate clearing with novation (EV-003-Q03). Many ETD CCPs interpose by open offer. | Keep it generic. Add: "one possible mechanism of CCP Interposition; not the definition of 'cleared'". | High | High |
| LD-C0026 Position | Lacks the ETD keys. | Required qualifiers: account (CCP or internal), series (LD-C0014), side, gross/net basis, as-of clearing date and cycle, and asserting source (CCP statement or internal). A gross client account keeps long and short open unless trades carry a "close" position effect (FIX PositionEffect, tag 77, to verify) or are adjusted. No new concept is needed. | Med | High |
| LD-C0010 Account | Does not distinguish the CCP account from internal accounts (EV-001-Q01/Q02, EV-006-Q03). | Add NEW-ETD-06 CCP Account and adopt R07's `mapped_to`. | Med | High |
| LD-C0011 Segregation Model | No public anchors. It conflates the model, the account type and the legal protection. | Usage note. Instances: EMIR Art. 39(2) omnibus and 39(3) individual segregation, offered to clients under 39(5) and disclosed under 39(7) (paragraphs to verify); indirect structures (MiFIR Art. 30, Delegated Reg. (EU) 2017/2154, to verify); CFTC Reg. 1.20 ff. futures-customer segregation; Part 30 secured amount; Part 22 LSOC (OTC only). A model is *implemented by* CCP Account types. Legal protection is a conclusion for Legal (R06). | Med | High |
| LD-C0036 / LD-C0037 | ETD fees are charged per contract, often billed together to the clearing member, and many arise from post-trade events. | No per-fee concepts. Add LD-C0031 arises_from event and a "chargeable event" facet. EMIR Art. 38(1) has fees disclosed per service (scope to verify), which supports a Fee Schedule per Clearing Service. | Med | Med |
| LD-R0011 / LD-R0013 | Cover the receiving side only. R0013 has no service. | Keep both. Add has_giving_member. Qualify R0013 "within Clearing Service". | Med | High |

## 3. Answers to open ambiguities and EV questions

**LD-A0009 Cleared.**
- *Answer:* a trade is cleared when the CCP has become counterparty under a Clearing Service's rules (CCP Interposition). Registration in a member's CCP account is the evidence.
- *When:* at open-offer CCPs this happens at matching or trade registration, before any give-up. Some rulebooks place substitution at the CCP's acceptance instead.
- *Give-up:* a completed give-up changes *which* member's account holds the trade, not *whether* it is cleared.
- *Confidence:* high on the principle, medium on each CCP's moment.
- *Basis:* rulebooks; MiFIR Art. 29.
- *Firm decision:* which timestamp reporting uses.

**LD-A0010 / EV-003-Q01 Successful give-up.**
- *States:* instructed → pending → accepted (claimed/taken up), in full or in part, or rejected → registered to the receiving member's CCP account. A give-up can also be not taken up by the deadline.
- *Acceptance vs registration:* they coincide when the take-up happens in the CCP's system, and differ when acceptance happens elsewhere (a utility, or pre-designation).
- *Recommendation:* *complete* = the full quantity is registered to the receiving member. *Partial* = the remainder stays with the giving member. Hold the status per allocation line, as asserted by a source at a time (R07 NEW-OPS-03).
- *Confidence:* high on the pattern; deadlines and partial rules are CCP-specific.
- *Firm decision:* Q2.

**EV-003-Q02 Who holds the obligation before take-up?**
- *Registration first:* the executing clearing member faces the CCP (margin, settlement, default exposure) until take-up.
- *Pre-designation:* the designated member faces the CCP from registration.
- *Client side:* the client's exposure to the executing broker meanwhile is governed by the Give-up Agreement.
- *Confidence:* high, with CCP variants.

**EV-003-Q05 Give-up rejected or not taken up by the deadline.**
- *Status:* the trade stays in the giving member's account, still valid and cleared. This is an Operational Exception (LD-C0030), not a trade failure.
- *CCP-specific resolution paths:* a late give-up or Position Transfer (often with fees), re-attribution, or the executing side closing out and recovering costs under the Give-up Agreement.
- *Confidence:* high.

**LD-A0017 / EV-003-Q03 Novation and acceptance.**
- *Events:* model three: Clearing Member Acceptance, CCP acceptance (LD-C0023), and CCP Interposition with its mechanism.
- *Timing:* CCP acceptance normally implies "cleared" in ETD, but the rulebook fixes the legal moment; under open offer it can precede the acceptance message.
- *Client side:* under the EU principal model, the client's contract is with the clearing member.
- *Confidence:* high.
- *Firm decision:* none; per-service evidence is required.

**LD-A0013 Position.**
- *Answer:* per CCP account × series × side. House accounts are generally net; client omnibus accounts are net or gross by account type. Gross accounts rely on position effect or adjustments.
- *Firm decision:* Q3.

**LD-A0007 / EV-001-Q01 Account.**
- *Answer:* three levels, linked by `mapped_to`:
  - (a) the CCP Account per Clearing Service: house; client omnibus, net or gross; individual segregated; indirect variants;
  - (b) the member's internal client account;
  - (c) execution-side and give-up references.
- *For EV-001-Q01:* impact is decided by Clearing Service × CCP Account type × segregation model, then by the internal accounts mapped to the affected CCP accounts (internal overlay).
- *Confidence:* high.

**EV-002-Q01/Q02 Access and agreements.**
- *Clearing without membership:* (i) as a client of a clearing member (including the NCM model); (ii) indirect clearing; (iii) a CCP sponsored or direct-client model.
- *Execute here, clear there:* requires a Give-up Agreement, a Client Clearing Agreement with the clearing broker, execution terms with the executing broker, venue access on the executing side, and CCP access on the clearing side.
- *Basis:* MiFIR Art. 30; rulebooks.
- *Confidence:* high.

**LD-A0003 / LD-A0005 Fees.**
- *Brokerage:* the client usually owes the executing brokerage, and the clearing broker often pays it and debits the client (payer ≠ debtor).
- *Exchange fees:* per-contract transaction fees plus event fees (give-up, transfer, exercise, delivery), invoiced to the clearing member, sometimes collected by the CCP for the exchange. A recharge to the client is a separate charge.
- *Confidence:* medium-high to high.

**LD-A0015 / EV-001-Q05 Business date.**
- *Trade date vs clearing date:* evening or overnight sessions and trades after the cut-off fall on the next clearing date.
- *ETD key dates:* these are Date Role values (R07): last trading day, expiry, exercise deadline, first notice day, final settlement day, delivery day.
- *24/5 trading:* moves cut-offs, margin runs and give-up deadlines, all set relative to the clearing date.
- *Confidence:* high.

## 4. Proposed new concepts

| Temp ID | Name | Module | Type | Definition | Key relationships | Alignment (to verify) | Pri. | Needed by |
|---|---|---|---|---|---|---|---|---|
| NEW-ETD-01 | Clearing Service | Common | Entity | Distinct clearing offering of a CCP for a defined product scope, governed by identified rulebook provisions, with its own admission categories, account structures, margin methodology, fee schedule and default-management arrangements (default resources may be shared). | operated_by LD-C0008; LD-C0007 admitted_to | Rulebooks; EMIR Art. 14–15 | P1 | UC-001/002/003 |
| NEW-ETD-02 | CCP Interposition | Common | Event | Event by which a CCP becomes counterparty to each side of a transaction under a Clearing Service's rules, with a rulebook-defined mechanism and moment. Mechanisms: novation (LD-C0024); *open offer* (the rules make the CCP counterparty as soon as a qualifying transaction is matched or registered, replacing no prior bilateral contract); other. "Cleared" is the resulting state. | concerns LD-C0018; evidenced_by LD-C0023 | Rulebooks; CDM clearing events | P1 | EV-003-Q03 |
| NEW-ETD-03 | Clearing Broker | Common | Role | Role of a party that provides clearing of a client's transactions in a Clearing Service and is responsible to that client for them, either as clearing member of that service or through one. | specialises LD-C0005; toward LD-C0004; via LD-C0007 | US FCM (contextual) | P1 | EV-002-Q01/Q02, UC-004 |
| NEW-ETD-04 | Clearing Member Acceptance | Common | Event | Decision by a clearing member to accept, wholly or partly, or reject clearing responsibility for a trade or allocation attributed to it for an identified client or account, after its own checks. It is either explicit (take-up, claim) or given in advance through pre-execution limits. | decided_by LD-C0007; part_of LD-C0022; precedes or coincides with LD-C0023 | FIXML allocation/claim flows; RTS 26; CFTC 1.73 | P1 | EV-003-Q01/Q02, EV-006-Q01 |
| NEW-ETD-05 | Give-up Agreement | Common | Agreement | Agreement among a client, its executing broker(s) and clearing broker(s) on how executions are given up and taken up: acceptance conditions and limits, responsibility for trades not taken up, brokerage rates, billing and payment. | specialises LD-C0012; governs LD-C0022 | FIA International Uniform Brokerage Execution Services ("Give-Up") Agreement | P1 | EV-002-Q02, EV-003-Q02/Q05 |
| NEW-ETD-06 | CCP Account | Common | Entity | Account opened by a CCP within a Clearing Service in a clearing member's name, of a defined type (house; omnibus client, net or gross; individual segregated; indirect variants; US customer origins), recording positions, margin and collateral. | specialises LD-C0010; implements LD-C0011 | EMIR Art. 39 | P1 | EV-001-Q01/Q02, EV-006-Q03 |
| NEW-ETD-07 | Market Access Arrangement (R05 NEW-COM-02) | Common | Agreement | Add clearing values: direct membership (by category); client of a clearing member (including NCM); indirect clearing; CCP sponsored or direct-client models. | for NEW-ETD-01; intermediated_by LD-C0007 | MiFIR Art. 30; RTS 2017/2154 | P1 | EV-002-Q01 |
| NEW-ETD-08 | Position Transfer | ETD Clearing | Event | Movement of open positions between CCP accounts outside a give-up, under the Clearing Service's transfer rules (normally no change of beneficial owner), at a rule-set price basis and fee. Trigger: correction, client move, member exit. | from/to NEW-ETD-06 | FIXML PositionMaintenanceRequest | P2 | UC-001, EV-003-Q05 |
| NEW-ETD-09 | Porting | Common | Process | Process under a CCP's default rules by which positions and collateral recorded for the clients of a defaulting clearing member are transferred to back-up member(s), or else closed out with any balance returned for the clients' account. | from/to NEW-ETD-06; moves LD-C0047 | EMIR Art. 48(5)–(7); PFMI P14 | P2 | UC-001, UC-005 (GDI "portability") |
| NEW-ETD-10 | Expiry | Common | Event | Lifecycle event at which a listed series reaches the end of its life under its contract specification, triggering final settlement, exercise or abandonment, or delivery. | of LD-C0014; may_trigger NEW-ETD-11 / LD-C0028 | Rulebooks | P2 | UC-001, UC-006 |
| NEW-ETD-11 | Exercise | ETD Clearing | Event | Exercise of an option position by holder instruction or automatically at expiry, under the service's thresholds and contrary/abandon rules. | results_in NEW-ETD-12 | FIXML exercise/abandon | P2 | UC-001 |
| NEW-ETD-12 | Assignment | ETD Clearing | Event | Allocation of exercised contracts by the CCP to members' short positions, and by members to their accounts, under a stated method. | follows NEW-ETD-11 | Rulebooks | P3 | UC-001 |

**Dropped since v1:**
- *Clearing Membership* and *Membership Category*: use the LD-C0007 role assignment `admitted_to` NEW-ETD-01, with a category qualifier whose taxonomy value carries a "clearing scope" (own / affiliates / clients / NCMs).
- *CCP Account Position*: covered by the LD-C0026 qualifiers.
- *Open Offer as an event*: it is a mechanism value of NEW-ETD-02.
- *Physical Delivery Obligation*: covered by LD-C0028 with the cash/physical facet.
- *Notice*: use R05/R06's notice object, at P2.

**Not proposed:** fee or membership-label concepts; Give-up Instruction (R01's Allocation Instruction covers it); a Default Management Process.

## 5. Proposed new/changed relationships

- NEW-ETD-01 – operated_by – LD-C0008. One service has one CCP; a CCP has 1..n services.
- LD-C0007 role assignment – admitted_to – NEW-ETD-01. Qualifiers: category, effective period. Depends on R08's Party Role Assignment.
- Listed Contract Specification / LD-C0013 – eligible_in – NEW-ETD-01. Effective-dated. Eligibility ≠ firm coverage.
- NEW-ETD-02 – within – NEW-ETD-01; – has_mechanism – {LD-C0024, open offer, other}; – evidenced_by – LD-C0023.
- LD-C0022 – has_giving_member – LD-C0007. LD-C0022 – governed_by – NEW-ETD-05. A missing agreement is a failure cause.
- NEW-ETD-04 – decided_by – LD-C0007, with outcome, quantity and time. NEW-ETD-04 – precedes_or_coincides_with – LD-C0023; the order is stated per service.
- NEW-ETD-06 – held_in_name_of – LD-C0007; – implements – LD-C0011. LD-C0010 – mapped_to – LD-C0010: many-to-one is typical for omnibus, but this is not a universal cardinality.
- NEW-ETD-08 / NEW-ETD-09 – from/to_account – NEW-ETD-06, with a trigger qualifier. NEW-ETD-09 – moves – LD-C0047; collateral can fail to port separately from positions.
- NEW-ETD-10 – may_trigger – NEW-ETD-11 / LD-C0028. NEW-ETD-11 – results_in – NEW-ETD-12.
- LD-C0031 – arises_from – LD-C0017 / LD-C0023 / LD-C0025 / period. This lets UC-004 attribute event fees without fee subconcepts.
- Rule Change – affects – {NEW-ETD-01, CCP Account type, LD-C0011, give-up Cut-off, LD-C0032, LD-C0043, LD-C0047}. Qualifiers: impact type and date roles. This is AG-002's entry point.

## 6. Proposed new ambiguity entries

| Temp ID | Term | Required distinction | Reviewer |
|---|---|---|---|
| NEW-ETD-A1 | Clearing broker / clearing member / FCM | Service role toward the client vs admission at a CCP vs US registration status. Merge with R03 NEW-A-OTC-04 and R08 NEW-AMB-01. | Product / Legal |
| NEW-ETD-A2 | Give-up vs transfer vs porting | Trigger, consent, applicable rule, ownership conditions, fees, and whether collateral moves. | ETD Ops / Legal |
| NEW-ETD-A3 | Omnibus | EMIR omnibus (net/gross) vs US futures-customer omnibus vs indirect omnibus vs firm-internal pooled account. | Legal / Clearing Product |
| NEW-ETD-A4 | Who carries the trade before take-up | Registration to the executing member vs pre-designation. Decides who bears margin, fees and default exposure. | ETD Ops |

"Effective date" should be a single entry (adopt R06 NEW-A-REG-03). Expiry dates belong in R07's Date Role vocabulary.

## 7. Questions only the business owner can answer

1. **Access models for UC-002:** direct categories, third-party clearing, indirect, sponsored? *Why:* scope of NEW-ETD-03/07. *Default:* all, generically.
2. **"Successful give-up":** is it member acceptance or registration to the receiving member, and does a partial count? *Why:* EV-006-Q01, EV-003-Q01. *Default:* full-quantity registration; report partials separately.
3. **Position basis:** gross or net by default? *Why:* EV-006-Q03. *Default:* none; ask, or return both, labelled.
4. **Give-up direction:** the giving side, the receiving side, or both? *Why:* role qualifiers, fee flows, revenue split. *Default:* both.
5. **Lifecycle in the pilot:** do exercise, assignment, expiry or delivery matter for the first UC-001 questions? *Why:* NEW-ETD-10..12 priority. *Default:* Expiry P2; the others P2/P3.
6. **Grain of "our service" in the overlay:** *Why:* where AG-002 stops. *Default:* Clearing Service × CCP Account type × client segment.
7. **Event fees in management revenue:** are recharged post-trade event fees counted in LD-C0042? *Why:* the LD-A0002 boundary. *Default:* model them via arises_from; Finance decides inclusion.
8. **Reference services for AG-004:** which 2–3 public clearing services seed the rulebook evidence? *Why:* AG-004 must show where CCPs differ. *Default:* at least one open-offer service and one acceptance-based service.

## 8. Cross-review

### (a) Disagreements

- **R03, LD-C0023 as the parent of member acceptance plus a new "CCP Registration".** A take-up is not "acceptance into a clearing service", and "CCP Registration" duplicates LD-C0023. Keep LD-C0023 as the CCP side, with a sibling (agrees with R08).
- **R05, "clearing broker" as an alias of LD-C0007.** EV-002-Q01 ("offer clearing where we are not a member") needs a role that exists *without* membership, and an alias cannot carry that.
- **R08, a generic "Service".** Keep the CCP's Clearing Service apart from the firm's Service Offering (R05). AG-002 goes from a change to *the CCP's* service, then to *our* offering. A merged concept recreates the ambiguity.
- **R03, moving LD-C0022 to ETD Clearing.** The executing side is a party to it (R01). Keep it in Common with a scope note.
- **R03, Porting "on default or at client request".** Narrow Porting to default (EMIR Art. 48; no consent from the defaulter). A voluntary move is a Position Transfer.
- **R05, Change Notice as one object.** One circular carries several changes with different effective dates, and one change passes through consultation and final notices. Keep Rule Change (P1) separate from the notice (P2, often a GDI item).
- **R06, "listed markets typically use open offer at matching".** True of many European ETD CCPs. Some rulebooks place substitution at CCP acceptance (to verify per rulebook). Set no default.
- **R01, give-up "claimed for full quantity" as the default.** It coincides with registration when the claim is made in the CCP's system. Registration is safer because UC-006 reconciles against CCP statements (owner decides, Q2).

### (b) Duplicates and canonical names

| Canonical name | Also proposed as | Choice |
|---|---|---|
| Clearing Service | R03 NEW-COM-01, R05 NEW-COM-03, R08 NEW-COM-01 | NEW-ETD-01 text; Entity; Common |
| Clearing Member Acceptance | R03 NEW-COM-02, R08 NEW-ETD-01 | NEW-ETD-04 (includes the pre-execution limit variant OTC needs) |
| CCP Interposition | R06 NEW-REG-07; R03 qualifier | R06 name; mechanism values as in NEW-ETD-02 |
| Give-up Agreement | R01 NEW-EXE-04, R08 NEW-COM-07 | NEW-ETD-05 text |
| Market Access Arrangement | R05 NEW-COM-02, R08 NEW-COM-05 | R05 name (venue and clearing); clearing values from NEW-ETD-07 |
| Porting | R03 NEW-COM-08 | NEW-ETD-09 (default-triggered) |
| Expiry | R07 NEW-PTL-01 | Common; NEW-ETD-10 text |
| Rule Provision / Rule Change | R05 NEW-COM-05/04, R06 NEW-REG-04/05, R08 NEW-COM-03/04 | R06 definitions (most complete date roles and statuses) |
| Regulatory Obligation | R03 NEW-COM-04, R06 NEW-REG-02 | R06 |
| Default Fund Contribution | R04 NEW-MC-08, R06 NEW-REG-09 | R04; linked to membership category |
| Margin Methodology | R04 NEW-MC-01, R05 NEW-RSK-01 | R04 |
| Listed Contract Specification | R07 NEW-REF-03, R08 NEW-EXE-01 | This name, Common: CCP eligibility, exercise style and delivery attach to it |
| Relations | R01 giving_member / my sending_member; R05/R08 arises_from / my triggered_by | `has_giving_member`; `arises_from` |
| Ambiguities | "effective date" (R05, R06, R08, mine); "product" (R05, R07) | One entry each |

NEW-COM-01 means three different things across R03, R05 and R08. The steward should assign the final temp IDs centrally.

### (c) Points from others that affect ETD clearing

- **R08:** Party Role Assignment underpins `admitted_to`. Its proposed affected-ID column for ambiguities is critical: today A0009 and A0010 attach to no concept, so AG-004 gets no warnings.
- **R07:** Cut-off, Status Assignment, Business Record and Reconciliation Break carry give-up deadlines (EV-001-Q04, EV-003-Q05), give-up status history (EV-006-Q01) and CCP vs internal positions (EV-006-Q03). ETD reconciliation types to seed: position vs CCP statement, give-up/allocation, executing-brokerage invoice, exchange/CCP fee invoice.
- **R04:** the margining tier and the segregation-to-margin-basis link match the CCP Account types; gross omnibus needs client-level position reporting to the CCP. NEW-A-MC-05 ("house vs client") sits beside NEW-ETD-A3.
- **R03:** extend Client Clearing Agreement to ETD, since EV-002-Q02 contrasts the give-up and clearing agreements. R06's Client Clearing Legal Model fits as a facet of that agreement.
- **R06:** under EMIR Art. 2(7), derivatives executed on an MTF or OTF are "OTC". Scope the ETD module by listing and clearing structure, not by that label.
- **R01:** the venue-member role gives the NCM a home. "Allocation to an account carried by another clearing member = give-up" is correct. Off-book trades matter to clearing because their registration path and deadlines differ (support P2).
