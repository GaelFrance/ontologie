# Review 01 (v2): Listed Derivatives Execution (futures and options)

Scope: orders, fills, care/DMA/algo, block/EFRP, executing-side give-up, average price, allocation, venue/MIC, MiFID II/MiFIR, FIX, execution fees. Against `ontologie` @ 59c1998 and the hub (UC/EV-001 to 006). Unconfirmed references are marked "to verify".

## 1. Verdict

The principles are right: Order, Execution and Trade are separate, no universal fill-to-trade cardinality, and allocation, averaging and give-up are distinct. LD-C0016/0017 are sound if read from the order's perspective. Five gaps block the pilot agents:
- no executing-side party in give-up (only LD-R0011 receiving member) and no give-up agreement, which EV-002-Q02 and EV-003-Q02 need;
- no venue-member role separate from the client-facing executing broker, which EV-002-Q01 needs;
- no allocation instruction, so allocation deadlines have no home (UC-003);
- no execution method (on-book vs block/EFRP), which most exchange circulars change (UC-001);
- no handling channel (care/algo/DEA) for management revenue (UC-004).

Five new concepts and about ten clarifications close them, with no meaning change to an existing ID (v1 proposed nine concepts; four are now facets or qualifiers).

## 2. Corrections to existing items

| ID | Issue | Proposed change | Sev. | Conf. |
|---|---|---|---|---|
| LD-C0016 Order | Does not say who instructs whom; care/algo handling turns one client order into many venue orders. | Clarified definition (same meaning): "Instruction from one party to another, or to a trading venue, to buy or sell a specified quantity of an instrument under stated execution conditions (order type, limit, time in force, handling instructions)." Add the qualifier *client-facing / venue-facing* and NEW-R-EXE-01 (parent/child). Alignment, to verify: FIX NewOrderSingle (D), NewOrderMultileg (AB), OrdType, TimeInForce, Side; state vocabulary from FIX OrdStatus. | Med | High |
| LD-C0017 Execution | v1 wrongly proposed a venue-level redefinition. The current text is the order-perspective *fill* and should stay; missing are how it was formed and that one match yields one Execution per participating order. | Keep the meaning. Add usage notes: (i) "on listed markets an execution results from matching on a trading venue or from registration of a privately negotiated trade under venue rules" (NEW-EXE-01); (ii) a broker's venue-facing and client-facing executions are separate Executions linked through the order hierarchy, and need not be 1:1; (iii) busts and corrections are Lifecycle Events (LD-C0025) referencing the original, with the originator (venue or member). Alias "fill": *contextual* (NEW-A-EXE-01). Alignment, to verify: FIX ExecutionReport (8) with ExecType Trade / Trade Cancel / Trade Correct, ExecID, LastQty, LastPx, LastMkt, TransactTime. | Med | High |
| LD-C0006 Executing Broker | Conflates the client-facing provider, the venue member entering the order and the MiFIR "executing entity"; the giving clearing member is a fourth party. | Keep it as the client-facing service role. Note: "not necessarily the Trading Venue Member (NEW-EXE-02), the MiFIR executing entity, or the giving clearing member (NEW-R-EXE-06)". Alias "executing firm" *ambiguous* (NEW-A-EXE-04). | High | High |
| LD-C0009 Trading Venue | No identifier; operator, venue and segment not separated (master prompt v2). | Identify by ISO 10383 MIC. The operating MIC is the venue/operator level and a segment MIC a segment (to verify per use). Add the relation `operated_by` LD-C0002 (alias "market operator" *contextual*, MiFID II). No Market Segment concept yet. | Med | High |
| LD-C0020 Allocation | Not distinguished from give-up; LD-R0007/0008 attributes belong to a missing instruction. | Rule: "An allocation to an account carried by a clearing member other than the one to which the execution is registered initiates a give-up (LD-C0022). Otherwise it is an internal allocation." Create the instruction specialisation now (NEW-EXE-03). | High | High |
| LD-C0021 Average Price Group | Does not say who averages (a venue/CCP facility registering trades at the average, or the broker booking the client at the average); residuals unmodelled. | Qualifier *averaging performed by: venue/CCP facility / broker*. Rule: rounding residuals are recorded as separate amounts; their treatment is to validate. Note: averaging groups and allocation distributes; they are chained but distinct (EV-003-Q04). US conditions under CFTC 1.35 (to verify). | Med | High |
| LD-C0022 Give-up / Take-up | No executing side and no governing agreement. Terms: "give-in" is the receiving side's view; "claim"/"take-up" is the receiving member's act. | Add NEW-R-EXE-06 (giving member) and NEW-R-EXE-07 (Give-up Agreement). Support the ETD reviewer's redefinition ("from the executing side to a receiving clearing member… before or after registration"). Aliases: give-in, claim, take-up all *contextual*. | High | High |
| LD-C0018 Trade | v1 asserted that an execution "normally" yields separate member-side and client-side trades. That is not universal. | Usage note: the number of trades derived from one execution depends on the client clearing legal model (principal back-to-back vs agency), on allocation and on averaging. Record lineage, not counts. | Med | High |
| LD-C0033 Client Execution Fee | No charge basis or grain; all-in rates hide exchange fees. | Note: state the basis (per contract side, per round turn, per allocation, per ticket, bps of notional) and the grain. An all-in rate that includes venue/CCP fees must be decomposed before comparison with LD-C0036/0037 (LD-A0005, LD-A0018). | Med | High |
| LD-C0035 Executing Broker Brokerage Charge | No viewpoint: received as executing broker, paid and recharged as clearing broker. | Support the label "Executing Brokerage Charge" (label only). Debtor, payer and recharge must be explicit (LD-A0003). | Med | Med |
| LD-C0041 Execution Revenue | The revenue split by channel and by service mix has no qualifiers. | Required context: handling channel (NEW-EXE-05), service mix (execution-only, execute-and-clear), venue, product. | Med | Med |
| LD-R0003 / R0004 / R0006 | R0003 has no recipient. R0004 ignores child orders. R0006 treats on-book matching and off-book registration as the same. | R0003: add NEW-R-EXE-02. R0004 note: "directly or via derived child orders". R0006: qualify by execution method; for off-book trades the venue *registers* rather than matches. | Med | High |
| Taxonomy: orders/executions | The "service channel" axis has no values; there are no execution-method or capacity axes. | Values from NEW-EXE-05. Add axes: execution method, order type, time in force, trading capacity (agency / principal / riskless principal, aligned to MiFIR RTS 22 AOTC/DEAL/MTCH and FIX OrderCapacity; to verify). | Low | High |

## 3. Answers to open ambiguities

**LD-A0001 Execution fee.** There are three charges, told apart by creditor and service:
- (i) the client execution charge owed to the executing broker (LD-C0033), often called "execution commission";
- (ii) executing brokerage owed for given-up executions (LD-C0035), usually billed to the clearing broker or to the client;
- (iii) the venue transaction fee (LD-C0036), whose debtor is set by the venue/CCP (entering member or clearing member; it may follow the give-up; to verify per venue).

Basis: exchange fee schedules, FIA give-up agreement framework. Confidence: high. **Firm decision:** does "execution fee" mean (i) alone or (i) plus passed-through (iii) (all-in vs fees-plus)?

**LD-A0004 Commission (deferred, for information).** Usually per-contract client remuneration (per side or round turn) for execution, clearing or both: a label, not an economic category. Confidence: medium. Keep Draft.

**LD-A0008 Trade / transaction / execution.** FIX separates the order, the execution report (per order event, including each fill), the trade capture report (TradeCaptureReport, AE) and the allocation messages (AllocationInstruction J, AllocationReport AS). The MiFIR "transaction" (Art. 26; RTS 22 = Delegated Reg. (EU) 2017/590) is a regulatory reporting unit. RTS 22 also defines "execution" broadly enough to include some order transmission (Arts. 3–4, to verify). The MiFIR "transaction" should be an *ambiguous* alias, never LD-C0019. Confidence: high. LD-C0019 itself remains deferred.

**LD-A0010 Successful give-up (executing side).** On the executing side the steps are: allocation/give-up instruction captured → give-up submitted on the CCP/exchange platform (possibly designated at order entry) → pending → claimed (full or partial) or rejected/expired. A trade not claimed by the deadline stays with the giving member (the deadline is CCP-specific). Hold status per allocation line, not per execution, keeping the native status (see 07's Status Assignment). Confidence: medium-high; illustration in SRC-003. **Firm decision:** Q7.

**LD-A0015 Business date (execution part).** An ETD trade date is the venue's trading date. For evening/overnight sessions it can differ from the calendar date at the execution timestamp. Record the execution timestamp in UTC; MiFID II RTS 25 (Delegated Reg. (EU) 2017/574) sets clock-synchronisation requirements. Confidence: high (verify per venue). **Firm decision:** Q6. Merge with 07's NEW-A-06.

**LD-A0016 Product / instrument (listed part). Corrects v1.** v1 equated Product with the contract specification. That conflicts with LD-C0013 as written ("family") and with the taxonomy axes. Use three layers:
- Product = classification family (LD-C0013);
- Contract Specification = the exchange-defined template (07's NEW-REF-03; also 08's NEW-EXE-01);
- Instrument = the tradeable series (expiry, plus strike and call/put), typically with an ISIN (ISO 6166) and a CFI classification (ISO 10962).

Listed strategies are Instruments with legs; a strategy execution yields leg executions. Confidence: high; no firm decision needed.

**Fill-to-trade cardinality (sponsor point 6).** Industry practice confirms the decision: child orders fan out, averaging fans in, allocation fans out, strategies split into legs, and a block trade is one negotiated execution registered for two sides. Model lineage only.

## 4. Proposed new concepts

| Temp ID | Name | Module | Type | Definition | Key relationships | Standard alignment (to verify) | Prio | Use case |
|---|---|---|---|---|---|---|---|---|
| NEW-EXE-01 | Execution Method | Common (used by Execution, OTC) | Reference Concept | How an execution was formed: matching of orders/quotes on a venue (order book or RFQ), registration on a venue of a privately negotiated trade (block trade; exchange for related position: EFP, EFR/EFS, options-for-options; other venue-defined types), or bilateral off-venue (outside listed execution). | LD-C0017 has_method (exactly one); qualifies LD-R0006; EFRP carries a related-position qualifier | FIX TrdType (828) values incl. Block Trade, EFP; venue rules, e.g. CME Rules 526/538, Eurex T7 Entry Service; MiFIR RTS 2 deferrals post-2024 review | P1 | UC-001 (block thresholds, EFRP rules), UC-003 |
| NEW-EXE-02 | Trading Venue Member | Common | Role | Role of a party admitted under a trading venue's rules, as member or participant, to enter orders and register trades in its own name. Distinct from clearing membership (a non-clearing member is a venue member without LD-C0007) and from the client-facing executing broker. | conferred by a direct-membership access arrangement; enters LD-C0016 (NEW-R-EXE-03) | MiFID II "member or participant", Art. 53 for RMs; FIX PartyRole "Executing Firm"/"Entering Firm" | P1 | UC-002 (EV-002-Q01/Q02), UC-003 |
| NEW-EXE-03 | Allocation Instruction | Common | Instruction | Instruction from a client or its investment manager specifying how an executed or average-priced quantity is split across target accounts and, where relevant, clearing brokers. It is given before execution (pre-allocation) or after it, and is amendable until a venue/CCP deadline. | instructs LD-C0020; references LD-C0017 / LD-C0021; targets LD-C0010 | FIX AllocationInstruction (J) / AllocationReport (AS); CFTC 1.35(b)(5) (US bunched orders) | P1 | UC-003 (EV-003-Q04), UC-006 |
| NEW-EXE-04 | Give-up Agreement (canonical for 02 NEW-ETD-05, 08 NEW-COM-07) | Common | Agreement | Agreement among a client, one or more executing brokers and one or more clearing brokers under which executions are given up to a designated clearing broker. It covers acceptance and rejection, brokerage terms and responsibility before acceptance. | is_a LD-C0012; governs LD-C0022 | FIA give-up agreement family (title/version to verify); not the FIA/ISDA Cleared Derivatives Execution Agreement (OTC) | P1 | UC-002 (EV-002-Q02), UC-003 (EV-003-Q02) |
| NEW-EXE-05 | Order Handling Channel | Execution | Reference Concept | How an order is worked and reaches the venue: care (worked by a person at the broker), broker algorithm, direct market access (client-generated orders routed through the broker's infrastructure under its membership) or sponsored access (client connects directly under the member's code). Whether the client itself uses an algorithm is a separate attribute. | LD-C0016 has_handling_channel; required context of LD-C0041 | MiFID II Art. 4(1)(39) algorithmic trading, 4(1)(41) DEA (covers DMA and sponsored access), Art. 17(5); RTS 6 (Delegated Reg. (EU) 2017/589); RTS 24 order-record DEA/algo indicators; FIX HandlInst (21), CustOrderHandlingInst (1031) | P2 (P1 if Q3 = yes) | UC-004, UC-001 (DEA/algo rule changes) |

**Dropped from v1 or not proposed:**
- *Trading Capacity*: now a qualifier.
- *Off-Book Trade*: a value of NEW-EXE-01.
- *Market Segment*: covered by the MIC pattern; P3.
- *Execution Correction*: a lifecycle facet value.
- *Fill*, *Child Order*, *Order Type*, *Time in Force*: qualifiers or NEW-R-EXE-01.
- *MiFIR transaction report*: owned by 06 NEW-REG-08.

## 5. Proposed new or changed relationships

| Ref | Subject – predicate – object | Notes |
|---|---|---|
| NEW-R-EXE-01 | LD-C0016 – derived_from – LD-C0016 | Parent/child slicing. 0..1 parent per order within one handling party. |
| NEW-R-EXE-02 | LD-C0016 – submitted_to – party in LD-C0006 role assignment, or LD-C0009 | Completes LD-R0003. The sender may be an investment manager, not the account owner. |
| NEW-R-EXE-03 | LD-C0016 (venue-facing) – entered_by – NEW-EXE-02 | DEA orders carry the member's identity although the client generates them. |
| NEW-R-EXE-04 | LD-C0017 – has_method – NEW-EXE-01 | Exactly one (definitional). |
| NEW-R-EXE-05 | LD-C0016 – has_handling_channel – NEW-EXE-05 | Time-stamped. It may change, e.g. a care order passed to an algo. Child orders inherit it unless re-routed. |
| NEW-R-EXE-06 | LD-C0022 – has_giving_member – LD-C0007 | Canonical name for 02's "sending_member". Relabel LD-R0011 `has_receiving_member` (label only, per 08). |
| NEW-R-EXE-07 | LD-C0022 – governed_by – NEW-EXE-04 | Where one exists. A missing agreement is a rejection cause (EV-003-Q05). |
| NEW-R-EXE-08 | NEW-EXE-03 – instructs – LD-C0020; – references – LD-C0017/LD-C0021; – targets – LD-C0010 | Versions are kept. The deadline is a Cut-off (07 NEW-OPS-01) of the venue/CCP. |
| NEW-R-EXE-09 | LD-C0020 – may_initiate – LD-C0022 | Only when the target account is carried by another clearing member (rule in §2). |

## 6. Proposed new ambiguity entries

| Temp ID | Term | Required distinction | Reviewer |
|---|---|---|---|
| NEW-A-EXE-01 | Fill | Venue-facing fill vs client-facing fill vs allocation line vs ExecutionReport message. Counts of fills, executions and trades differ. | Execution Product / Operations |
| NEW-A-EXE-02 | Block trade | Venue off-book block facility (negotiated, minimum size) vs MiFIR large-in-scale transparency treatment vs buy-side bunched order for later allocation. | Execution Product / Compliance |
| NEW-A-EXE-03 | DMA / DEA / algo | Broker DMA vs MiFID II DEA (DMA and sponsored access) vs broker algorithm vs client's own algorithm. Obligations depend on regime and venue. | Execution Product / Compliance |
| NEW-A-EXE-04 | Executing broker / firm / entity | Client-facing provider vs venue member vs MiFIR executing entity vs giving clearing member. | Execution / ETD Ops / Compliance |
| NEW-A-EXE-05 | "Execution" (merges 08 NEW-AMB-04) | Event LD-C0017 vs service vs module; service mix execution-only (give-up out) vs execute-and-clear vs clearing-only (give-in). | Execution & Clearing Product / Finance |

v1's "Volume" entry merges into 05 NEW-A-03, adding per side vs round turn and single- vs double-counted venue volume.

## 7. Questions only the business owner or internal sources can answer

1. **Service mix.** Must the model support execution-only (give-up out), execute-and-clear and clearing-only (give-in), with revenue attributed per service? *Why:* LD-C0041/0042 on one client trade; both give-up directions. *Default:* yes, all three.
2. **Charge and volume basis** for management figures: per side, round turn, allocation or ticket? *Why:* EV-004 comparability. *Default:* store per contract side; derive the rest.
3. **Revenue split by handling channel** (care / algo / DMA / sponsored)? *Why:* it decides whether NEW-EXE-05 is P1. *Default:* yes.
4. **Third-party execution.** Must the model cover executions routed through another venue member (where the firm is not a member)? *Why:* the NEW-EXE-02 vs LD-C0006 split and brokerage paid (EV-004-Q02). *Default:* yes. Never infer memberships.
5. **Internal meaning of "fill" and "trade".** Which records carry these names (venue-facing, client-facing, allocation)? *Why:* the alias table for agents. *Default:* both are *ambiguous* aliases.
6. **Trade date for management revenue** in evening/overnight sessions: venue trading date or booking date? *Default:* venue trading date.
7. **Give-up "done" for operations KPIs.** *Default (aligned with 02):* the full allocated quantity is registered to the receiving member's CCP account. Partial take-ups are reported separately; claim time and registration time are both kept.
8. **Average pricing.** Venue/CCP facilities, broker-side averaging or both? Are rounding residuals tracked? *Why:* the qualifier on LD-C0021 and residual amounts in UC-004. *Default:* both, with residuals as separate amounts.

## 8. Cross-review

### (a) Disagreements

- **LD-C0023 shape.** 02 and 08 narrow LD-C0023 to the CCP and add Clearing Member Acceptance as a sibling. 03 keeps LD-C0023 as the parent with two children (CM Acceptance, CCP Registration). **I support 03.** There is no meaning change to an existing ID, and the parent also covers *pre-execution* clearing-member limit checks (DEA orders, venue-hosted pre-trade limits), which are acceptances that precede execution. LD-R0013 then moves to the CCP Registration child.
- **Open Offer as an Event (02 NEW-COM-02).** Open offer is a mechanism, not an occurrence. **I support 06's CCP Interposition** (event with mechanism ∈ {novation, open offer, other}); LD-C0024 stays generic.
- **Product (05).** Renaming LD-C0013 "Derivative Product" and glossing it as "a listed futures contract" merges classification with the contract specification. Keep LD-C0013 as the family (07). Add Contract Specification at P1, not P2 (08): tick size, trading hours and new expiries are among the most frequent UC-001 circulars.
- **"Clearing broker" as an alias of LD-C0007 (05, 03).** I prefer 02's Clearing Broker role (a sibling of LD-C0006 under LD-C0005). The give-up counterpart of the executing broker is a client-facing service role, and that role may clear through another member.
- **Citations to check.** 02's CFTC 1.73/1.74 relate mainly to FCM risk controls and swap STP acceptance. Their bearing on ETD give-up claims is weak; to verify.
- **Interaction with 08's specialisation note.** Accepting "Execution is_a LD-C0025" (08) is fine, but the alias "fill" must be *contextual*, not exact (NEW-A-EXE-01).

### (b) Duplicates and proposed canonical names

| Canonical | Merges | Note |
|---|---|---|
| Give-up Agreement (Common) | 01 NEW-EXE-04, 02 NEW-ETD-05, 08 NEW-COM-07 | Definition in §4. |
| has_giving_member | 01, 02 "sending_member" | Pairs with relabelled LD-R0011. |
| Clearing Member Acceptance (Common, child of LD-C0023) | 02 NEW-ETD-06, 03 NEW-COM-02, 08 NEW-ETD-01 | Common, because OTC and pre-trade checks use it. |
| Market Access Arrangement (Common) | 02/08 "Clearing Access Arrangement", 05 NEW-COM-02, 01 DEA access | One concept for venues *and* clearing services, with a model facet: direct membership, via member, DEA (DMA/sponsored), client clearing, indirect, sponsored clearing. It confers NEW-EXE-02 or LD-C0007. |
| Service (parent) → Clearing Service, Service Offering | 02/03 NEW-COM-01, 05 NEW-COM-01/03, 08 NEW-COM-01 | LD-C0006 "execution service concerned" needs Service Offering. |
| Execution Method | 01 NEW-EXE-01, 03 "execution-method facet" | Includes "bilateral off-venue". |
| fee `arises_from` | 02 `triggered_by`, 05/08 `arises_from` | Targets LD-C0017, LD-C0025, LD-C0023, period. |
| Contract Specification | 07 NEW-REF-03, 08 NEW-EXE-01 | Common; P1. |
| Identifier (+ scheme) | 07 NEW-REF-01/02, 03 NEW-COM-05 | Covers ClOrdID/OrderID/ExecID and venue trade IDs, unique only per venue/session. |
| Rule Provision + Rule Change | 02, 05, 06, 08 | Execution-side `affects` targets: Execution Method, Contract Specification, Fee Schedule, NEW-EXE-05. |
| "Product", "Volume", "Effective date" ambiguities | 05/07; 01/05; 02/05/06/08 | One entry each. |

### (c) Points from other reviews that affect execution

- **06:** under EMIR Art. 2(7), MTF/OTF-executed derivatives are OTC, so venue regulatory type must qualify LD-C0009; MiFID client category (best execution) attaches to the service relationship. NEW-REG-06 (client clearing legal model) governs how many trades an execution yields.
- **05:** service mix and all-in vs fees-plus shape LD-C0033/0041; Fee Rebate covers venue incentive programmes.
- **02:** registration to the executing clearing member at match, and the pre-/post-registration qualifier, define who holds the trade before take-up (executing-side states in §3).
- **03:** clearing-member pre-execution credit checks mean CM acceptance can precede execution. The order lifecycle needs a "rejected by pre-trade limit" outcome.
- **07:** Status Assignment, Business Record and Cut-off host order, give-up and allocation statuses and deadlines.
- **08:** Party Role Assignment makes LD-C0006 and DEA permissions per client, service and period; FIX/RTS alignments go in front matter with `verified: false`.
- **04:** no execution impact.
