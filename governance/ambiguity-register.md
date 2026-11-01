# Ambiguity register

Detailed semantic questions remain Open. The sponsor approved the foundation on 2026-09-20, selected management revenue as the priority and approved a contractual-role starting point for Client. These decisions narrow LD-A0002, LD-A0006 and LD-A0014 without resolving all their details. The sponsor answers of 2026-11-01 (see the [decision log](decision-log.md)) further narrow LD-A0014. Owner roles are suggestions; individual concept approvals are not inferred.

The 2026-11 expert review added affected concept IDs, new entries LD-A0019 to LD-A0035 and industry-informed proposed answers. **A proposed answer is not a decision**: every entry stays Open until the business owner decides, and the decision is then recorded as described at the end of this page. Columns after the fourth are appended so that existing readers of the first four columns keep working.

| ID | Term / issue | Required distinction or decision | Suggested reviewer | Affected IDs | Status |
|---|---|---|---|---|---|
| LD-A0001 | Execution fee | Separate client execution charges, executing-broker brokerage and exchange charges. | Execution Product / Finance | LD-C0031, LD-C0033, LD-C0035, LD-C0036 | Open, answer proposed |
| LD-A0002 | Fee, revenue and cash received | Separate charges, management revenue and cash settlement; define timing, gross/net, pass-through treatment and the boundary with contribution after costs. | Finance | LD-C0028, LD-C0029, LD-C0031, LD-C0039, LD-C0074 | Open, narrowed 2026-09-20, answer proposed |
| LD-A0003 | Brokerage paid | Identify debtor, actual payer, beneficiary and recharge treatment. | Clearing Product / Finance | LD-C0031, LD-C0035, LD-C0057 | Open, answer proposed |
| LD-A0004 | Commission | Validate whether this is a remuneration category, contractual charge type or local label. | Product / Finance | LD-C0038, LD-C0033, LD-C0034 | Open, deferred by sponsor, answer proposed |
| LD-A0005 | Exchange fees | Separate service nature, economic beneficiary and collecting organisation; bundled bills need explicit decomposition. | Operations / Finance | LD-C0032, LD-C0036, LD-C0037 | Open, answer proposed |
| LD-A0006 | Client | Separate contractual role, legal entity, commercial group and beneficial owner. | Product / Client Data | LD-C0002, LD-C0003, LD-C0004, LD-C0073 | Open, narrowed 2026-09-20, answer proposed |
| LD-A0007 | Account | Specify function, maintaining party, holder, beneficiary and account-to-account relationships. | Operations / Client Data | LD-C0010, LD-C0011, LD-C0069 | Open, answer proposed |
| LD-A0008 | Trade, transaction and execution | Establish identity and lineage; Transaction is provisional and must not collapse all lifecycle events. | Product / Operations | LD-C0017, LD-C0018, LD-C0019, LD-C0025 | Open, answer proposed |
| LD-A0009 | Cleared | Separate acceptance status from legal effect and record effective time. | Clearing Operations / Legal | LD-C0023, LD-C0024, LD-C0053, LD-C0054 | Open, answer proposed |
| LD-A0010 | Successful give-up | Define completion, partial acceptance, rejection, correction and current versus historical status. | Execution / ETD Operations | LD-C0022, LD-C0023, LD-C0053, LD-C0060 | Decided 2026-11-01 (sponsor; see decision log) |
| LD-A0011 | Margin required | Distinguish IM/VM, member–CCP/client–member relationship, risk scope, time and collateral coverage. | Risk / Collateral | LD-C0043, LD-C0044, LD-C0045, LD-C0069, LD-C0070 | Open, answer proposed |
| LD-A0012 | Variation margin | Specify collateral versus settlement treatment under the governing arrangement. | Legal / Risk / Finance | LD-C0028, LD-C0045, LD-C0047, LD-C0071 | Open, answer proposed |
| LD-A0013 | Position | Specify gross/net, quantity/notional/exposure, account, instrument, CCP and as-of basis. | Clearing Product / Risk | LD-C0026, LD-C0010, LD-C0069 | Open, answer proposed |
| LD-A0014 | Revenue by client | Use the approved management perspective; specify client attribution, consolidation, internal eliminations, measurement period, reporting currency and any separately defined cost deductions. | Finance / Product | LD-C0004, LD-C0039, LD-C0041, LD-C0042, LD-C0073, LD-C0074 | Open, narrowed 2026-09-20 and 2026-11-01, answer proposed |
| LD-A0015 | Business date | Distinguish trade, clearing, value and accounting dates and calendars/time zones. | Operations / Finance | LD-C0015, LD-C0065, LD-C0066 | Open, answer proposed |
| LD-A0016 | Product, instrument and OTC contract | Validate identity boundaries for listed series and bespoke OTC agreements. | Reference Data / OTC Product | LD-C0013, LD-C0014, LD-C0018, LD-C0062 | Open, answer proposed |
| LD-A0017 | Novation and acceptance | Do not assume all clearing uses the same legal mechanism or timestamp. | Legal / Clearing Product | LD-C0023, LD-C0024, LD-C0053, LD-C0054 | Open, answer proposed |
| LD-A0018 | Fee Charge and Commission types | Validate estimated versus enforceable charges and avoid additive counting of overlapping fee categories. | Finance / Ontology Lead | LD-C0031, LD-C0033, LD-C0034, LD-C0035, LD-C0036, LD-C0037, LD-C0038 | Open, answer proposed |
| LD-A0019 | Clearing broker, clearing member, FCM | Service role toward the client versus admission at a CCP versus a regulatory registration (FCM in the US). | Product / Legal | LD-C0005, LD-C0007, LD-C0057, LD-C0068 | Open, answer proposed |
| LD-A0020 | Service | A CCP's clearing service versus the firm's service offering versus a MiFID investment service; also the service mix (execution-only, clearing-only, execute-and-clear). | Product / Ontology Lead | LD-C0051, LD-C0052 | Open, answer proposed |
| LD-A0021 | Product | Product family classification versus a venue's contract specification versus a listed series versus a service offering ("our clearing product"). | Product / Reference Data | LD-C0013, LD-C0014, LD-C0052, LD-C0062 | Open, answer proposed |
| LD-A0022 | Dates of a rule change | Publication, entry into force, application, phase-in and end of transition versus the date the firm recorded the change. | Legal / Compliance | LD-C0015, LD-C0063, LD-C0064 | Open, answer proposed |
| LD-A0023 | Current, as of, as known at | Valid time versus record time: valid now and latest non-superseded record, valid at a business date, or known by a timestamp. | Operations / Ontology Lead | LD-C0015, LD-C0025, LD-C0026, LD-C0068 | Open, answer proposed |
| LD-A0024 | Fill | Venue-facing fill versus client-facing fill versus allocation line versus execution-report message; counts differ. | Execution Product / Operations | LD-C0016, LD-C0017, LD-C0020 | Open, answer proposed |
| LD-A0025 | The trade (clearing tier) | Pre-clearing (executed) trade versus CCP-facing trade versus member-client trade; which tier, identifier and counterparty view a question uses. | Clearing Product / Operations | LD-C0018, LD-C0054 | Open, answer proposed |
| LD-A0026 | Give-up, transfer, porting | Listed give-up versus voluntary position transfer versus default porting versus OTC or FX prime-brokerage "give-up"; trigger, consent, rule, fees and whether collateral moves. | ETD Operations / Legal | LD-C0022, LD-C0024 | Open, answer proposed |
| LD-A0027 | Margin and initial margin | "Margin" as requirement versus collateral held or posted; CCP initial margin versus US futures initial and maintenance call levels versus uncleared bilateral initial margin. | Risk / Collateral | LD-C0043, LD-C0044, LD-C0047 | Open, answer proposed |
| LD-A0028 | Omnibus, house and client | EMIR omnibus (net or gross) versus US customer omnibus versus indirect omnibus versus internal pooled account; CCP account type versus economic relationship of affiliates. | Legal / Clearing Product | LD-C0010, LD-C0011, LD-C0069 | Open, answer proposed |
| LD-A0029 | Eligible, mandatory, offered, covered | CCP clearing eligibility versus a regulatory clearing obligation for a counterparty pair versus the firm's offering versus "we cover market X" (membership, third-party access or actual offering). | Legal / Product | LD-C0051, LD-C0052, LD-C0059, LD-C0062 | Open, answer proposed |
| LD-A0030 | Client clearing model | Combination of access model, legal model, segregation model and margining basis; model offered versus legal protection or portability actually achieved. | Product / Legal | LD-C0011, LD-C0056, LD-C0059, LD-C0069 | Open, answer proposed |
| LD-A0031 | Group | Regulatory consolidation group versus commercial group versus CCP affiliate versus legal parent in public entity-relationship data. | Compliance / Client Data | LD-C0002, LD-C0068, LD-C0073 | Open, answer proposed |
| LD-A0032 | OTC and listed | Regulatory "OTC" (derivatives not executed on a regulated market or equivalent) versus off-venue versus not exchange-listed; cleared is a separate dimension. | Legal / Product | LD-C0009, LD-C0014, LD-C0018, LD-C0068 | Open, answer proposed |
| LD-A0033 | Volume | Per side versus round turn versus trades versus notional; single- or double-counted; executed versus cleared; published versus firm data. | Product / Finance | LD-C0017, LD-C0033, LD-C0039 | Open, answer proposed |
| LD-A0034 | Break, exception, reject, fail | Reconciliation break versus operational exception versus rejected or lapsed give-up versus settlement fail versus technology incident. | Operations | LD-C0030, LD-C0050, LD-C0053, LD-C0028 | Open, answer proposed |
| LD-A0035 | Executing broker, firm, entity | Client-facing executing broker versus trading venue member entering the order versus regulatory executing entity in transaction reports versus giving clearing member. | Execution / ETD Operations / Compliance | LD-C0006, LD-C0058, LD-C0007 | Open, answer proposed |

On resolution, retain the original issue and add decision, affected concept IDs, rationale, evidence, reviewer and date. Do not replace uncertainty with an unrecorded default.

## Proposed answers pending owner decision

From the [2026-11 expert review](reviews/2026-11-expert-review/ARBITRATION.md); review numbers in brackets. Public references marked "to verify" must be checked against the current text before adoption. "Firm decision" names what only the business can settle; see [open questions](open-questions-for-owner.md).

### LD-A0001 Execution fee
Three charges, separated by creditor and service: the client execution charge (LD-C0033); executing brokerage on given-up executions (LD-C0035); the venue transaction fee (LD-C0036), whose debtor is set by venue or CCP rules. "Execution fee" is an ambiguous alias of all three. Confidence high. Firm decision: all-in versus fees-plus client pricing. [01, 05]

### LD-A0002 Fee, revenue and cash received
A charge accrues at its chargeable event (LD-R0078), is then invoiced or debited and finally settled (LD-C0029); amount certainty (estimated or final) and billing stage are facets of LD-C0031. Collateral income is a separate stream whose inclusion in clearing revenue is undecided. Gross or net treatment of pass-through charges is a Finance decision; accounting principal-versus-agent guidance is only an analogue. Confidence high on stages, medium on treatment. [05, 04, 02]

### LD-A0003 Brokerage paid
Under a give-up the client usually owes executing brokerage and the clearing broker often pays it and debits the client: two charges linked by LD-R0080, with debtor, payer and observing entity explicit. "We paid" cannot be answered without the observing entity. Confidence high. Firm decision: which model applies per client or market. [05, 02, 01]

### LD-A0004 Commission
In listed derivatives usually the client-facing per-contract remuneration (per side or round turn) for execution, clearing or both: a commercial label, not an economic category. Keep LD-C0038 Draft with no fee parent and treat "commission" as a blocked alias that returns candidates (LD-C0033, LD-C0034, a bundled execute-and-clear charge). Deferred by the sponsor. Confidence medium. [05, 01]

### LD-A0005 Exchange fees
Decompose bundled bills by service nature (trading, post-trade, market data, connectivity, membership) before aggregating; the creditor is the venue operator and the collecting organisation (often the CCP) is recorded separately (LD-R0022). CCPs and clearing members publicly disclose prices and fees per service, including discounts and rebates (EMIR Art. 38(1), to verify). Confidence high. Firm decision: treatment of market data, connectivity and rebate netting. [05, 02]

### LD-A0006 Client
Entity-level statuses attach to the Legal Entity, relationship-level statuses (such as MiFID client category) to the role assignment (LD-C0003); revenue rolls up from the contractual client of each service relationship to a Commercial Group (LD-C0073). Regulatory texts use "client" differently: EMIR Art. 2(15) is a clearing relationship with a clearing member, the MiFID II client (Art. 4(1)(9)) is broader, and the US "customer" is the FCM relationship. Confidence high. [06, 05]

### LD-A0007 Account
Three levels: the CCP Account (LD-C0069) of each clearing service; the member's internal client account; execution-side and give-up references, which are identifiers rather than accounts. Levels are related only by explicit, time-bounded LD-R0065. Segregation regime and regulatory account statuses are separate, time-bounded dimensions. Confidence high. [02, 07, 06]

### LD-A0008 Trade, transaction and execution
Three identity levels linked by directional lineage, never by a fixed cardinality: the execution event, the trade, and successor trades after clearing (LD-R0034). Each level carries its own identifiers (for example venue trade IDs, UTI ISO 23897). The MiFIR "transaction" (Art. 26) is a regulatory reporting unit and an ambiguous alias, never LD-C0019, which stays deferred. Confidence high. [01, 03, 06, 07, 08]

### LD-A0009 Cleared
"Cleared" is a derived status meaning that CCP Interposition (LD-C0054) has occurred in a named clearing service. Three timestamps stay distinct: clearing member acceptance (LD-C0053), CCP acceptance or registration (LD-C0023), interposition. Under open offer interposition can occur at matching, before any registration message; under novation it occurs at registration. A completed give-up changes which member holds the trade, not whether it is cleared. Confidence high on the principle, medium on each CCP's moment. Legal decision: the interposition moment per clearing service, from the rulebook. [02, 03, 06, 08]

### LD-A0010 Successful give-up
States per give-up line: pending, accepted (in full or in part), rejected, lapsed (not taken up by the cut-off, so the trade stays with the giving member), cancelled, reversed where permitted, and unknown (no record), which is not "pending". Proposed definition of complete: the full allocated quantity is registered to the receiving clearing member's CCP account, as evidenced by the CCP record; partial take-ups are reported separately and both member acceptance time and registration time are kept. Where the take-up is made in the CCP's system the two coincide. Current versus historical follows LD-A0023. Confidence high on the pattern, medium on state names. Firm decision: definition of complete and source of record. **Decided 2026-11-01: the proposed definition is accepted and the CCP record is authoritative; discrepancies with internal records are reported as breaks** (see the [decision log](decision-log.md)). [01, 02, 07]

### LD-A0011 Margin required
Undefined until five qualifiers are fixed: tier (from margin provider and taker role assignments: CCP–member house, CCP–member client account, member–client, client–indirect client); component (IM, VM, add-ons, total); account and gross or net basis; as-of time and run; currency basis. Under net omnibus accounts a client-level figure exists only in the member's own calculation. Member–client IM is a CCP replication, a replication with multiplier or add-on, or an own model (LD-C0070). Confidence high. Firm decision: default tier, if any. [04]

### LD-A0012 Variation margin
Settled-to-market: the daily payment settles exposure (LD-R0067) and is accompanied by a price alignment amount. Collateralised-to-market: VM is collateral to be returned, with price alignment interest. The treatment is a versioned fact per clearing service and account type; some OTC CCPs converted some or all accounts to settled-to-market (dates per service to verify). Price alignment is never part of VM. Confidence high on concepts, medium on per-CCP facts. Legal/Finance decision per service for internal reporting. [04, 03, 06]

### LD-A0013 Position
Key: account (CCP or internal) × instrument × clearing service × side or net basis, as of a business date and cycle, with the asserting source (CCP statement or internal). House accounts are generally net; client omnibus accounts are net or gross by account type. CCP-reported and internal positions are two records of one position; a difference is a break. OTC positions are sets of open cleared trades measured by count, notional or risk sensitivity. Confidence high. Firm decision: default basis and source, or return both labelled. [02, 03, 07]

### LD-A0014 Revenue by client
Sponsor decision 2026-11-01: execution-only, clearing-only and execute-and-clear are all offered; give-up and give-in are both supported; revenue is attributed per service. Proposed: attribute to the contractual client of each service relationship (LD-R0077), show the service mix, roll up to Commercial Group, flag intra-group clients for elimination; mandatory context is observing entity, management basis, period and currency. Open: cost perimeter for Contribution (LD-C0074), pass-through and collateral income treatment. [05, 01, 04]

### LD-A0015 Business date
Every date has a role (trade date, CCP clearing date, value date, booking date, reporting date, contract key dates such as last trading day or expiry, as-of date), resolved against a named Business Calendar (LD-C0066) and time zone; event timestamps are kept in UTC. Evening or overnight sessions can carry the next day's trade date (venue-specific). Extended trading hours move cut-offs, margin runs and give-up deadlines relative to the clearing date. Confidence high. Firm decision: default role and time zone of "today". [01, 02, 07]

### LD-A0016 Product, instrument and OTC contract
Proposed (implemented in the Draft definitions of LD-C0013, LD-C0014 and LD-C0062): Product Family is a classification (CFI ISO 10962 and the UPI ISO 4914 are classification and product identifiers); Contract Specification is a venue's versioned listing template; Instrument is a standardised, counterparty-independent specification at the level at which it is listed or assigned an instrument identifier (a listed series; an OTC ISIN where assigned, with the Trade still carrying full terms); a bespoke OTC contract is a Trade, not an Instrument. Confidence high. Reference Data and OTC Product to confirm the meaning change of LD-C0014. [01, 03, 07, 08]

### LD-A0017 Novation and acceptance
Four distinct steps: clearing member acceptance, CCP acceptance or registration, CCP interposition with its mechanism (novation, open offer, other), and settlement finality (outside current scope). Under the EU principal-to-principal model the client's contract is with the clearing member and arises from the client clearing agreement, not from the CCP's novation; in US models the FCM guarantees performance, and who is principal to the CCP contract varies by product and rulebook. OTC "novation" also names bilateral step-in and step-out, which is not clearing. Confidence high. [02, 03, 06]

### LD-A0018 Fee Charge and Commission types
An estimated charge is a Fee Charge whose amount certainty is "estimated"; billing stage is a facet. Proposed additive key: creditor × service nature × chargeable event; "commission", "execution fee" and bundled labels are non-additive views over it. Confidence high. Firm decision: Finance confirms the additive key. [05, 08]

### LD-A0019 Clearing broker, clearing member, FCM
Clearing Broker (LD-C0057) is the service role toward the client and may exist without membership of the clearing service; Clearing Member (LD-C0007) is admission at the CCP; FCM is a US regulatory registration held by a legal entity, recorded as a Regulatory Classification (LD-C0068), and only a contextual alias. Confidence high. [02, 03, 05, 06, 08]

### LD-A0020 Service
Two concepts, no common parent for now: a CCP's Clearing Service (LD-C0051) and a provider's Service Offering (LD-C0052), linked by LD-R0082. A MiFID "investment service" is a regulatory category, not either concept. Confidence high. [02, 03, 05, 07, 08]

### LD-A0021 Product
"Product" returns candidates LD-C0013, LD-C0062, LD-C0014 and LD-C0052 unless context selects one; a venue's "product code" usually designates a Contract Specification. Confidence high. [01, 05, 07]

### LD-A0022 Dates of a rule change
Each Rule Change (LD-C0064) carries role-qualified dates: publication, entry into force, application, phase-in and end of transition, plus the date the firm recorded it. "Effective date" without a role is ambiguous. Confidence high. [02, 05, 06, 08]

### LD-A0023 Current, as of, as known at
Current = valid now and latest non-superseded record from the stated source; as of D = valid at business date D; as known at T = only records received by T. Every answer states source, as-of date and freshness. See the time convention in [modelling guidelines](../docs/modelling-guidelines.md). Confidence high. Firm decision: whether "as known at" history is needed. [07, 08, 06]

### LD-A0024 Fill
Contextual alias of LD-C0017 from an order's perspective; a broker's venue-facing and client-facing executions are separate Executions linked through the order hierarchy, and allocation lines are not fills. Confidence high. [01, 08]

### LD-A0025 The trade (clearing tier)
State the tier: pre-clearing trade, CCP-facing trade, member–client trade (principal model). Successor trades are linked by LD-R0034 and may carry new identifiers. Confidence high. [03]

### LD-A0026 Give-up, transfer, porting
Give-up (LD-C0022) attributes a listed trade to a receiving clearing member; a position transfer moves open positions between CCP accounts under transfer rules, usually voluntarily; porting is the default-triggered transfer of a defaulting member's client positions and collateral to a back-up member, or their close-out (EMIR Art. 48(5) to (7), to verify). Positions and collateral port as separate legs. OTC or FX "give-up" usually means prime-brokerage give-up. Position Transfer and Porting are backlog concepts. Confidence high. [02, 03, 04, 06]

### LD-A0027 Margin and initial margin
"Client margin held" usually means collateral (LD-C0047); "margin required" means LD-C0043; "margin posted" means delivered collateral. US futures initial and maintenance levels are two call-trigger levels of one requirement, not two requirement types. Initial margin under uncleared bilateral margin rules is out of scope and must not resolve to LD-C0044. Confidence high. [04]

### LD-A0028 Omnibus, house and client
EMIR omnibus and individual client segregation (Art. 39(2) and (3), to verify), US futures-customer omnibus, indirect-client omnibus account types (Delegated Regulations (EU) 2017/2154 and 2017/2155, to verify) and internal pooled accounts are different things; the CCP account type does not determine the economic relationship (affiliates may be cleared as clients or in the house account). Confidence high. [02, 04, 03]

### LD-A0029 Eligible, mandatory, offered, covered
Eligibility is a CCP fact (LD-R0050); a clearing obligation applies to a counterparty pair, a product class including trade-term ranges, and a date; offering and coverage are firm facts in the internal overlay, through a Market Access Arrangement. Never infer one from another. Confidence high. [03, 05, 06]

### LD-A0030 Client clearing model
Never resolve to a single concept: decompose into access model (LD-C0059), legal model (LD-C0056), segregation model (LD-C0011) and margining basis (LD-C0069). The model offered says nothing by itself about legal protection or portability achieved, which only Legal concludes. Confidence high. [05, 06]

### LD-A0031 Group
A regulatory consolidation group (used in some threshold calculations), a Commercial Group (LD-C0073), a CCP's "affiliate" and a legal parent in public entity-relationship data are different; regulatory statuses never attach to a commercial group. Confidence high. [06, 05, 07]

### LD-A0032 OTC and listed
Under EMIR Art. 2(7) a derivative not executed on a regulated market or an equivalent third-country market is OTC, so MTF and OTF trades count as OTC; venue type is a Regulatory Classification of LD-C0009. Scope modules by listing and clearing structure, not by that label. Confidence high. [06, 02, 03]

### LD-A0033 Volume
State unit (contract side, round turn, trade, notional), counting basis (single or double), stage (executed or cleared) and source (published or firm). Confidence high. [05, 01]

### LD-A0034 Break, exception, reject, fail
A reconciliation break says records disagree, not which is wrong; an operational exception (LD-C0030) is a situation requiring handling and may be raised by a break; a rejected or lapsed give-up is an event and may raise an exception but is not a trade failure; a settlement fail concerns LD-C0028; a technology incident is out of scope. Confidence high. [07, 02]

### LD-A0035 Executing broker, firm, entity
LD-C0006 is the client-facing service role; the Trading Venue Member (LD-C0058) enters the order in its own name; the executing entity of a transaction report is a regulatory reporting role; the giving clearing member is LD-R0035. One party may hold several of these roles; never infer one from another. Confidence high. [01]
