# Review 05 (v2): Product management, commercial model and agent usability

Lens: service catalogue, market and CCP access, onboarding, fees, pricing and rebates, management revenue and contribution, change notices, public competitive intelligence. Above all, I test whether agents AG-001..006 can use the ontology. Temporary IDs use the prefix `NEW-PRD-` to avoid collisions with other reviewers (§8b).

## 1. Verdict

The foundation is strong on what not to conflate: charge vs revenue vs cash, acceptance vs legal effect, role vs party. LD-C0031..C0042 are a usable start for the management-revenue priority.

What is missing is the product backbone:
- the **service** sold to clients, and the CCP **clearing service** it relies on (five definitions already reference one: C0003, C0004, C0006, C0007, C0023);
- **how access** to a venue or clearing service is obtained;
- the **rule change** that triggers AG-002;
- the **contribution** and **commercial group** concepts that UC-004 needs.

Of the 25 evaluation questions, 1 is broadly answerable today, 16 partially and 8 not at all (§1.1). Six product concepts, about ten concepts from other reviewers and a few facets would close most gaps. Commission and Transaction stay deferred, but should be machine-flagged so that no agent resolves them silently.

### 1.1 Coverage of the evaluation questions (hub pin 59c1998)

| EV | Today | Missing (canonical names, §8b) |
|---|---|---|
| 001-Q01 | Partial | Clearing Service; Rule Change; edge between Account and Segregation Model |
| 001-Q02 | Gap | Regulatory Regime/Obligation/Classification (R06); Commercial Group |
| 001-Q03 | Partial | margining tier, Margin Call Cycle (R04) |
| 001-Q04 | Gap | Rule Provision, Rule Change, date roles |
| 001-Q05 | Gap | Business Calendar, Date Role, Cut-off (R07) |
| 002-Q01 | Gap | Market Access Arrangement; Clearing Service; Clearing Broker |
| 002-Q02 | Gap | Give-up Agreement; Client Clearing Agreement |
| 002-Q03 | Partial | Clearing Service; Regulatory Regime |
| 002-Q04 | Gap | Contract Specification; `C0009 operated_by C0002`; eligibility edge from contract to clearing service |
| 003-Q01 | Partial | Clearing Member Acceptance; status semantics |
| 003-Q02 | Partial | Give-up Agreement; sending member |
| 003-Q03 | Partial | CCP Interposition (novation or open offer) |
| 003-Q04 | Mostly | "averaging performed by" qualifier (R01) |
| 003-Q05 | Partial | Cut-off |
| 004-Q01 | Partial | Commercial Group; attribution to role assignment; service mix |
| 004-Q02 | Partial | `recharges`; observing entity |
| 004-Q03 | Partial | billing-stage and amount-certainty facets |
| 004-Q04 | Partial | service-nature facet; Fee Rebate; date basis |
| 004-Q05 | Gap | Contribution; Commercial Group |
| 005-Q01 | Partial | Rule Change; "client clearing model" ambiguity (NEW-A-PRD-06) |
| 005-Q02 | Gap | Margin Methodology (R04) |
| 005-Q03 | Partial | Collateral Eligibility Schedule (R04); Rule Change |
| 006-Q01 | Partial | status assignment; Clearing Member Acceptance; Cut-off |
| 006-Q02 | Partial | margining tier; edge between account and client |
| 006-Q03 | Partial | CCP account; account mapping |

**Fixes in the hub, not in this repo.**
- **UC concept lists.** These concepts appear in a use case's question set but not in its `concepts` list (checked by script): UC-001 (C0004, C0015, C0046, C0049), UC-002 (C0022), UC-005 (C0010, C0044, C0048), UC-006 (C0004, C0008). Add a `hub_check.py` rule to catch this.
- **Missing questions.** EV-004 has no question on contribution after costs or on pass-through of CCP fees, although UC-004 lists C0037, C0040 and C0042. EV-002 has none on execution access without venue membership, and EV-005 has none on volumes or published tariffs. Add one question to each set; the owner writes the expected answers.

## 2. Corrections to existing items

| ID | Issue | Proposed change | Sev. | Conf. |
|---|---|---|---|---|
| LD-C0004 Client | Refers to a service that has no concept. No client segment. | Keep the sponsor's contractual-role definition. Link it to Service (NEW-PRD-01) through the role assignment (R08) `in_service`. Add a **client segment** axis to the Participants taxonomy. | High | High |
| LD-C0005 Broker | Placeholder definition. My v1 made "clearing broker" an alias of C0007. **That was wrong**: a clearing broker may clear through a third-party member. | "Role of a party that executes orders and/or clears or carries trades on behalf of others under an identified agreement." Keep it abstract. Support Clearing Broker (R02) in Common. "FCM" is a contextual US alias of Clearing Broker and also a regulatory status. | Med | High |
| LD-C0009 Trading Venue | No operator link. "Exchange" can mean the venue, its operator or the exchange group. | Add the edge `operated_by` LD-C0002 (I withdraw my v1 Venue Operator role). The exchange group is the legal parent, taken from GLEIF Level 2 data (to verify); it is not a concept. Make "exchange" an **ambiguous** alias. Use ISO 10383 MICs: operating MIC for the venue, segment MIC for its segments. | Med | High |
| LD-C0013 Product | Label collision. Product teams say "product" for a service ("our OTC clearing product"), and venues use it for a contract specification. This breaks EV-002-Q04. | Keep the ID and the definition. Change the **label** to **Product Family**, which matches "Family defined by…". Make "product" an **ambiguous** alias resolving to {C0013, Contract Specification, Service}. Map CFI (ISO 10962) as a classification only (to verify). | High | Med-High |
| LD-C0019, LD-C0038 | Deferred by the sponsor, but nothing stops an agent from treating them as exact matches. | Do not define them. Add R08's flag `resolution: blocked-pending-decision`, so the agent returns candidates instead. Transaction → {C0017, C0018, C0025, C0029, MiFIR "transaction"}. Commission → {C0033, C0034, a bundled execute-and-clear charge}. | Med | High |
| LD-C0031 Fee Charge | No service, no chargeable event, no stage. R08 notes that "chargeable" sits badly with the Obligation type. | The obligation arises at the chargeable event under the tariff. Add two facets. **Amount certainty**: estimated or final. **Billing stage**: accrued, invoiced, disputed, adjusted, settled or written off. Add the edges `charged_for` and `arises_from` (§5). This answers LD-A0018. | High | High |
| LD-C0032 Fee Schedule | Mixes a public venue/CCP tariff (versioned, published by circular) with confidential negotiated client terms. | Make it the generic parent, with qualifiers: issuer, scope (Service, clearing service, venue or segment, contract), version, effective period. A Rule Change can target it. | High | High |
| LD-C0036 Exchange Fee Charge | A vertical group bills trading, post-trade, market data, connectivity and membership together, and the CCP often collects them. | Creditor is the venue operator. Record the collector separately (R0022). Make the service-nature facet mandatory. Charges whose creditor is a CCP stay under C0037. | Med | High |
| LD-C0037 | Could absorb default-fund and collateral costs. | Adopt R04's exclusion of both. | Low | High |
| LD-C0039 Revenue | The required context is implicit. | Mandatory context: observing entity, attribution target, management basis, period, currency, and gross or net of pass-through charges. AG-005 refuses to answer without it. | Med | High |
| LD-C0040 Cost | No categories, so no cost perimeter can be stated. | Add a cost-category facet: non-recharged venue/CCP fees, third-party brokerage, third-party clearing, connectivity and market data, funding/collateral, allocated shared cost. | Med | High |
| LD-C0042 Clearing Revenue | Interest on client cash collateral is material for many clearing businesses. Its inclusion is unstated. | Usage note: inclusion of Collateral Remuneration (R04 NEW-MC-11) is undecided (NEW-A-PRD-04). It must never be implicit. | Med | High |
| Fees taxonomy | In v1 I asked for a charge-unit axis and a rechargeability axis. The existing "tariff basis" and "pass-through treatment" axes already cover them. | Add only four axes. **Chargeable event**: execution, give-up, transfer, exercise or assignment, delivery, OTC registration or maintenance, compression, porting, periodic. **Service nature.** **Recurrence.** **Incentive programme.** | Med | High |

Withdrawn from v1: module moves for fee and revenue concepts (the current split between Execution and Common is consistent); the C0035 rename; the Venue Operator role; Jurisdiction (use R06's Regime instead); Margin Methodology (use R04's); Market Share (a semantic-layer ratio).

## 3. Answers to open ambiguities

**LD-A0001 Execution fee.** The term has three industry meanings:
- the client execution charge (C0033);
- the venue transaction fee (C0036);
- executing brokerage under a give-up (C0035).

Creditor plus service nature separates them, so "execution fee" should be an ambiguous alias. Public basis: exchange fee schedules and the FIA give-up agreement framework (title to verify). Confidence: high. **Firm decision:** whether client pricing is all-in or fees-plus (Q1).

**LD-A0002 Fee, revenue, cash.**
- The charge accrues at the chargeable event, then is invoiced (or debited on the clearing statement) and settled.
- In ETD, the cash evidence is often a C0029 on the client's account at the clearing broker.
- For pass-through charges, IFRS 15 principal-versus-agent guidance is a reasoned public analogue for gross or net presentation. It is not a management-basis rule.
- Income from collateral is a separate stream (NEW-A-PRD-04).

Confidence: high on the stages, medium on the treatment. **Firm decision:** date basis, gross or net presentation, and collateral income (Q2).

**LD-A0003 Brokerage paid.** Under a give-up, the client usually owes the executing brokerage. The clearing broker often pays it and debits the client. Model this as two C0031 charges linked by `recharges`, with debtor, payer and observing entity explicit. EV-004-Q02 ("we paid") cannot be answered without the observing entity. Confidence: high. **Firm decision:** which model applies per client or market.

**LD-A0004 Commission.** In listed derivatives, "commission" is the client-facing remuneration per contract, quoted per side or per round turn. It covers execution, clearing or both; the UK and EU often say "brokerage". EU cost-and-charges disclosure lists commissions among other cost items (MiFID II Art. 24(4); Delegated Regulation (EU) 2017/565, Annex II, to verify). It is therefore a commercial label, not an economic category. Treat it as a blocked alias with no fee parent. Confidence: medium. **Firm decision:** Q4.

**LD-A0005 Exchange fees.** Decompose bundled bills by service nature before aggregating, and separate transactional from periodic fees. CCPs and clearing members must publicly disclose their prices and fees per service, including discounts and rebates (EMIR Art. 38(1); PFMI Principle 23; wording and key consideration to verify). These tariffs are therefore legitimate input for UC-005. Confidence: high. **Firm decision:** treatment of market data, connectivity and rebate netting (Q7).

**LD-A0006 / A0014 Client; revenue by client.** Attribute revenue to the **contractual client of each service relationship**, then roll it up to a Commercial Group. Regulatory statuses attach to legal entities, never to groups (R06's attachment rule). Client revenue figures are comparable only when split by **service mix**: execute-and-clear, execution-only (given up) and clearing-only (given in) (R01 NEW-A-06). Intra-group clients need an elimination flag. Confidence: high on the structure. **Firm decision:** Q5.

**LD-A0018 Overlapping charge types.** Use the facets from §2. Declare **creditor × service nature × chargeable event** as the only additive key. "Commission", "execution fee" and bundled labels are non-additive views over it. Confidence: high. **Firm decision:** Finance confirms the key.

## 4. Proposed new concepts (product-owned)

| Temp ID | Name | Module | Type | Definition | Key relationships | Alignment (to verify) | Pri. | Needed by |
|---|---|---|---|---|---|---|---|---|
| NEW-PRD-01 | Service (co-proposed with R08) | Common, Commercial | Reference Concept | Defined offering through which a provider performs execution, clearing or related post-trade activity for recipients. Its scope is stated in product families or contracts, venues or clearing services, channel and client segment. | provided/received via role assignments; `relies_on` Clearing Service or C0009; priced_by C0032 | FIBO FND Products and Services; PFMI Principle 23 | P1 | 001-Q01, 002-*, 004-Q01/Q05 |
| NEW-PRD-02 | Market Access Arrangement | Common | Agreement (is_a C0012) | Arrangement by which a party can execute on a venue or clear in a clearing service. It has an access model (direct membership with category; via a third-party member; sponsored or direct-client; indirect clearing; DEA), an optional intermediary, a status (proposed / live / suspended / terminated) and an effective period. | held_by C0001; grants_access_to; intermediated_by role assignment | EMIR Art. 4(3); indirect-clearing RTS 2017/2154 and 2017/2155; MiFID II Art. 4(1)(41); PFMI Principle 19 | P1 | 002-Q01, UC-002 gap analysis, GDI "sponsored clearing" |
| NEW-PRD-03 | Commercial Group | Common | Entity | Grouping of parties that a provider manages as one commercial relationship. Distinct from legal consolidation; carries no legal or regulatory status. | C0001 member_of (time-bound) | Contrast with GLEIF Level 2 | P1 | 004-Q01/Q05, 001-Q02 |
| NEW-PRD-04 | Contribution | Common, Commercial | Measure | Management revenue attributable to a target (client relationship, Commercial Group, Service, venue or clearing service), less the costs inside an explicitly approved cost perimeter, for a stated observing entity, period and currency. No formula or default perimeter is implied. | derived_from C0039, C0040 | none | P1 | 004-Q05, UC-004 |
| NEW-PRD-05 | Fee Rebate | Common, Commercial | Obligation | Amount owed or credited by a fee creditor to the debtor because programme or tier conditions were met over a period (venue incentive or market-making programme, client volume tier). Excludes negotiated rates and waivers. | adjusts a set of C0031; defined_in C0032 | EMIR Art. 38(1) "discounts and rebates" | P1 | 004-Q04, 004-Q01/Q05 |
| NEW-PRD-06 | Activity Volume | Common | Measure | Quantity of execution or clearing activity for a scope and period. Unit (side, round turn, trade, notional) and source (published or firm) are mandatory. | measured_for venue, clearing service, C0013, client, Service | FIA volume statistics; CPMI-IOSCO quantitative disclosures | P2 | UC-005 positioning; UC-004 rate per contract |

**Shared dependencies** (canonical owner in brackets; I support them all as P1):
- Party Role Assignment (R08)
- Clearing Service as an is_a of Service (R02/R03)
- Clearing Broker (R02)
- Give-up Agreement (R01/R02/R08)
- Client Clearing Agreement (R03)
- Rule Provision, Rule Change, Regulatory Regime (R06)
- Contract Specification (R07)
- Margin Methodology and Collateral Eligibility Schedule (R04)
- Collateral Remuneration (R04), P1 only if Q2 says yes

**Not proposed:**
- *Competitor*: a query over Service, not a concept.
- *Coverage*: Service × Market Access Arrangement (NEW-A-PRD-01).
- *Onboarding*: modelled as the lifecycle states of NEW-PRD-02 and of the agreements.
- *Market Share*: a semantic-layer metric.
- *Change Notice*: the circular is provenance for one or more Rule Changes.
- *Client Fee Arrangement*: only if Q7 says yes.
- *Business Capability*: belongs to master-prompt step 5.

**Usability for agents.** Use the template's existing "Subdomain" field as the retrieval scope, with values Parties & Roles, Market Structure & Access, Trade & Lifecycle, Commercial, Margin & Collateral and Change & Rules. AG-005 then reads Commercial, and AG-002 reads Change & Rules plus Market Structure. No new modules are needed.

## 5. Proposed new or changed relationships

- **Role assignment – `in_service` – NEW-PRD-01.** Time-bound. Replaces a direct "Client receives Service" edge.
- **NEW-PRD-01 – `relies_on` – Clearing Service | C0009.** Qualified `via` NEW-PRD-02. This is the coverage edge and the second hop for AG-002. Instances are internal.
- **NEW-PRD-02 – `grants_access_to` – C0009 | Clearing Service.** Also `held_by` C0001 and `intermediated_by` a role assignment (0..1).
- **AG-002 path.** Rule Change – `amends` – Rule Provision | C0032 – `applies_to` – Clearing Service | C0009 ← `relies_on` – Service. The public half stops at the Clearing Service, so context mode can start now.
- **C0032 – `applies_to` – Service | Clearing Service | C0009 | Contract Specification; `issued_by` C0001.** Versioned.
- **C0031 – `charged_for` – Service; C0031 – `arises_from` – C0017 | C0018 | C0025 | period.**
- **C0031 – `recharges` – C0031.** 0..n.
- **NEW-PRD-05 – `adjusts` – set of C0031.**
- **C0039/C0040 – `attributed_to` – role assignment | NEW-PRD-03 | Service.** Observing entity, period and currency are mandatory.
- **NEW-PRD-04 – `derived_from` – C0039, C0040.**
- **C0001 – `member_of` – NEW-PRD-03.** Time-bound.
- **C0009 – `operated_by` – C0002.**

## 6. Proposed new ambiguity entries

| Temp ID | Term | Required distinction | Reviewer |
|---|---|---|---|
| NEW-A-PRD-01 | "We cover market X" | Membership vs access through a third party vs a service actually offered, per venue or clearing service | Product |
| NEW-A-PRD-02 | "Product" (merges R07 NEW-A-03) | Product Family vs contract specification vs Service | Product / Ref. Data |
| NEW-A-PRD-03 | "Volume" (merges R01 NEW-A-05) | Side vs round turn vs trades vs notional; single- vs double-counted; executed vs cleared; published vs firm | Product / Finance |
| NEW-A-PRD-04 | Clearing revenue scope | Fee income vs collateral remuneration vs recharged market data and connectivity | Finance |
| NEW-A-PRD-05 | Rebate / discount / waiver | Venue incentive received vs client rebate granted vs negotiated rate vs waiver | Finance / Product |
| NEW-A-PRD-06 | "Client clearing model" (GDI topic) | Combines access model, legal model (principal or agency), segregation model and margining basis. Never resolve it to only one of them. | Product / Legal |

## 7. Questions only the business owner can answer

1. **All-in or fees-plus pricing for clients?** *Matters for* how C0033 relates to C0036, and for gross vs net. *Default:* support both, with a flag per agreement.
2. **Is collateral income part of clearing revenue?** Same question as R04's Q1. *Default:* a separate measure, excluded until decided.
3. **What is the first cost perimeter for Contribution?** *Default:* direct third-party variable costs only; no shared-cost allocation.
4. **What does "commission" mean locally?** *Default:* a blocked alias that returns candidates.
5. **How are split flows attributed?** For execution-only and clearing-only clients, is revenue attributed per service to each service's contractual client? Aligned with R01's Q1. *Default:* yes, with the service mix shown.
6. **At what granularity does the business steer services?** Aligned with R02's Q7. *Default:* service type × product family × venue or clearing service × channel.
7. **Rebates and pricing.** Are venue rebates netted against exchange fees? Do negotiated client terms differ structurally from tariffs? *Default:* show both gross and net; no new concept.
8. **What is the perimeter for competitive intelligence?** Which public sources apply (EMIR Art. 38 tariffs, CFTC FCM financial data, FIA volumes, CCP quantitative disclosures), and may peers be named in the public-zone hub? *Default:* all four sources; peers named only when publicly sourced.

## 8. Cross-review

**(a) Disagreements**

- **R08's Service vs R02/R03's Clearing Service.** These are not competing proposals. Clearing Service should be an is_a of Service, carrying membership categories and the default fund. The firm's own offering is a Service whose provider holds a broker role, so it needs no third concept.
- **R02's Clearing Access Arrangement and Clearing Membership, and R08's NEW-COM-05 (clearing only).** Merge them into Market Access Arrangement covering **execution and clearing**: UC-002 is about "execution and/or clearing", and access through a third-party member is a real model on both sides. Treat membership category as a qualifier. Keep Clearing Membership separate only if obligations such as the default-fund contribution cannot attach to the Clearing Member role assignment.
- **R02's Market Infrastructure Notice.** It should be provenance, not a concept. A consultation is a Rule Change with status "proposed", as R06 suggests.
- **What "Product" means.** I side with R07/R08 that it is a classification, over R01's reading as the contract specification. I add the relabel to Product Family. Contract Specification should be **P1**, not P2 as R08 proposes: EV-002-Q04 needs it, and circulars often amend it.
- **R08's restriction of C0031.** It is not needed. An estimate is a value of the amount-certainty facet, not a separate object.
- **R06's Client Clearing Legal Model.** I would make it a qualifier on Client Clearing Agreement rather than a concept, and keep the NEW-A-PRD-06 ambiguity entry.
- **My own v1 errors**, now corrected: "clearing broker" as an alias of C0007, and redundant fee axes.

**(b) Duplicates and canonical forms**

| Canonical | Merges |
|---|---|
| Service, with Clearing Service as is_a | R08 NEW-COM-01; R02/R03 NEW-COM-01; my v1 Service Offering |
| Market Access Arrangement | R02 NEW-COM-03; R08 NEW-COM-05 |
| Give-up Agreement (Common) | R01 NEW-EXE-04; R02 NEW-ETD-05; R08 NEW-COM-07 |
| Clearing Member Acceptance (is_a C0023) | R02 NEW-ETD-06; R03 NEW-COM-02; R08 NEW-ETD-01 |
| Rule Provision / Rule Change | R06 NEW-REG-04/05; R02 NEW-COM-06; R08 NEW-COM-03/04 |
| Regulatory Obligation | R06 NEW-REG-02; R03 NEW-COM-04 |
| CCP Interposition (mechanism: novation or open offer) | R06 NEW-REG-07; R02 Open Offer |
| Default Fund Contribution | R04 NEW-MC-08; R06 NEW-REG-09 |
| Porting | R02 NEW-COM-04; R03 NEW-COM-08 |
| Contract Specification | R07 NEW-REF-03; R08 NEW-EXE-01 |
| Expiry | R02 NEW-ETD-12; R07 NEW-PTL-01 |
| Collateral Arrangement | R04 NEW-MC-03; R08 NEW-COM-06 |
| Ambiguity "effective date" | R02 NEW-A-04; R06 NEW-A-REG-03; R08 NEW-AMB-02 |
| Ambiguity "clearing broker vs member" | R02 NEW-A-01; R03 NEW-A-OTC-04; R08 NEW-AMB-01 |
| Edge `arises_from` | also covers R02's `triggered_by` |

`NEW-COM-01` currently names three different things. The steward should keep one register of temporary IDs before consolidating.

**(c) Points from other reviews that affect my domain**

- **R01:** handling mode (care, algo, DEA) should also be a facet of Service. The taxonomy README already calls it a service channel, and it drives the revenue split.
- **R02/R03:** ETD and OTC event fees are values of the chargeable-event axis, not new fee concepts.
- **R04:** Collateral Remuneration makes NEW-A-PRD-04 concrete. Default fund and capital stay outside the first contribution perimeter (as in R06 Q5).
- **R06:** EMIR Art. 38 gives a public basis for pricing intelligence. Delegated reporting is a Service instance. The attachment rule confirms that Commercial Group carries no regulatory status.
- **R07:** an accrual vs invoice comparison is a fee reconciliation between Business Records, which EV-004-Q04 needs.
- **R08:** use the blocked-resolution flag for C0019 and C0038. The Party Role Assignment change is a prerequisite for revenue attribution, and I support it.
