# Specialist review 04 — Margin and collateral (cleared derivatives), v2

Scope: IM/VM, CCP and member-to-client margining, collateral, the segregation link, default fund and collateral economics. Reviewed against `ontologie` (Phase 1) and `derivatives-ai-hub` (UC-001..006, EV-001..006, GDI topic mapping). References marked "to verify" have not been checked against the current consolidated text.

## 1. Verdict

The catalogue already holds seven margin and collateral concepts (LD-C0043–0049), plus principle 7, LD-R0017–0019 and LD-A0011/0012, and it separates the right things. Missing: eligibility and remaining shortfall (two of principle 7's five objects); a margin methodology (EV-005-Q02); a structural margining tier (EV-006-Q02, EV-001-Q03); collateral legal form and the collateral-to-obligation link that relationships.md defers. LD-C0047 is mistyped. Six new concepts (eleven in v1), three high-severity corrections (LD-C0043, LD-C0045, LD-C0047) and some qualifiers close the gaps, all in Common, subdomain "Margin & Collateral", stewarded by Risk/Collateral.

## 2. Corrections to existing items

| ID | Issue | Proposed change | Sev. | Conf. |
|---|---|---|---|---|
| LD-C0043 Margin Requirement | The definition is circular ("calculated margin requirement"). It omits the two qualifiers that every margin question turns on: who owes whom, and for which account. | "Amount of margin that a margin provider is required to provide to a margin taker for an identified account or risk scope, determined under an identified methodology or contractual rule at a stated as-of time and currency basis; distinct from the call that demands it and from the collateral that covers it." Mandatory qualifiers: provider and taker role assignments (the tier is derived from them); account; component; run type (scheduled end-of-day / scheduled intraday / ad hoc); methodology version. | High | High |
| LD-C0044 Initial Margin Requirement | "Potential future exposure" is too loose. Add-ons have no home. The label collides with US futures "initial vs maintenance" levels. | Append: "…over an assumed close-out (liquidation) period at a stated confidence level, including add-ons the methodology applies (e.g. concentration, liquidity, wrong-way risk)." Notes: (1) A member–client IM derived from the CCP figure is still IM, at the member–client tier. (2) The US futures "initial" and "maintenance" figures are two call-trigger levels of one requirement, not two requirement types (NEW-A-MC-06). | Med | High |
| LD-C0045 Variation Margin Requirement | It does not say that VM is two-way, or what each legal treatment produces. | "Amount payable or receivable reflecting the change in value of positions since the previous margin cycle; its direction depends on the observing party. Under settled-to-market (STM) it gives rise to a Settlement Obligation (LD-C0028); under collateralised-to-market (CTM) it gives rise to an obligation to provide collateral that must be returned (LD-A0012)." Keep the Measure type. Price alignment is a separate flow (§5). | High | High |
| LD-C0046 Margin Call | No direction, deadline or basis. | Add: "issued by the margin taker to the margin provider in a scheduled or ad hoc run, with a settlement deadline; the amount derives from the shortfall (NEW-MC-07), adjusted for any minimum transfer amount or rounding, not from the requirement alone." A return of excess on request is a Collateral Movement, not a negative call. VM paid out by a CCP is a payment, not a call. | Med | High |
| LD-C0047 Collateral | "Committed as security" is wrong for title transfer. Directive 2002/47/EC distinguishes title-transfer from security financial collateral arrangements, and CCPs commonly take cash by outright transfer (per CCP, to verify). The Entity type duplicates LD-C0048: what LD-C0047 actually describes is an asset in a status under an arrangement. | **Explicit type and meaning change: Entity → State.** "Quantity of a Collateral Asset (LD-C0048) provided by a collateral provider to a collateral taker under an identified Collateral Arrangement (NEW-MC-03), by title transfer or security interest, for an account as of a time; carries market value and value after haircut." A "collateral balance" is an aggregation of this state, not a further concept. | High | High |
| LD-C0048 Collateral Asset | Eligibility is not a property of the asset. | Add: "Cash in a given currency is a collateral asset. Eligibility holds only against a version of a Collateral Eligibility Schedule (NEW-MC-04)." | Low | High |
| LD-C0049 Collateral Movement | It overlaps Cash Movement (LD-C0029) for cash, does not mention substitution, and does not separate instruction from settlement. | Define it as an observed transfer (delivery, return, substitution, or reallocation between accounts). A cash collateral transfer is also a LD-C0029: one identity with two classifications, counted once. Express instruction status as a qualifier until a use case needs a separate concept. | Med | High |
| LD-C0011 Segregation Model | It has no link to margin, yet the model and the CCP service determine the margining basis (gross or net) and whether collateral is attributable to each client, which in turn affects portability. | Usage note: state the level (CCP books or member books) and the margining basis the model implies. Public anchors: EMIR Art. 39 (omnibus and individual segregation); CFTC requirement that DCOs margin customer accounts gross (Reg. 39.13(g)(8)(i), to verify); LSOC for cleared swaps (17 CFR Part 22). | Med | High |
| LD-C0037 CCP Fee Charge | The boundary with default fund and collateral interest is not stated. | Append: "distinct from default-fund contributions and from interest on cash collateral; CCP charges for holding non-cash collateral are CCP Fee Charges with service nature 'collateral'." | Low | High |
| LD-R0017 / R0018 / R0019 | R0017 lacks qualifiers; a call (R0018) addresses the shortfall, not the requirement; once LD-C0047 is a State, a movement (R0019) moves asset quantities. | R0017: add tier, component, methodology version, run type; at CCP tier target a CCP account (NEW-ETD-04, review 02). R0018: note "amount based on NEW-MC-07". R0019: "moves quantities of LD-C0048 and changes LD-C0047". Keep all IDs, with migration notes. | Med | High |
| taxonomies/README Margin and Collateral axes | The decisive axes are missing. | Margin: add component, run type, VM treatment (STM/CTM/not applicable), margining basis (gross/net) and tier. Collateral: add legal form (title transfer / security interest), cash/non-cash and valuation basis (market value / after haircut). | Med | High |

## 3. Answers to open ambiguities

**LD-A0011 Margin required.** Undefined until five things are fixed: (a) tier (CCP–member house account, CCP–member client account, member–client, client–indirect client); (b) component (IM, VM, add-ons, total); (c) account or segregation unit and gross/net basis; (d) as-of time and run; (e) currency basis.

Under gross omnibus and individual accounts, the CCP computes each client sub-account separately and sums them. Under net omnibus, the CCP figure nets across clients, so a client-level figure exists only in the member's own calculation. Member–client IM is usually one of three things: a replication of the CCP model, that replication scaled by a multiplier or add-on, or the member's own model. For US futures, DCOs must require members to collect more than 100% of the DCO's IM from non-hedge customers (Reg. 39.13(g)(8)(ii), to verify). EMIR 3 added clearing-member duties to explain CCP margin models to clients (Art. 38 as amended by Reg. (EU) 2024/2987; paragraph to verify).

Confidence high. Public basis: PFMI Principles 6 and 14; EMIR Art. 39 and 41; Delegated Reg. (EU) 153/2013; CPMI-IOSCO public quantitative disclosures. Firm decision: default tier (Q2).

**LD-A0012 Variation margin.** Under **STM** the daily payment settles the exposure and resets the contract, with no return obligation; a price alignment amount (PAA) accompanies it; this is the futures norm. Under **CTM** VM is collateral to be returned, with price alignment interest (PAI). From about 2017 some OTC CCPs converted cleared swaps (some or all account types) to STM; dates to verify per service. Premium-style options carry no VM; futures-style options do. Make the VM treatment a required, versioned attribute of Clearing Service × account type. Confidence: high on the concepts, medium on the per-CCP facts. A firm decision is needed only for internal reporting.

**LD-A0013 Position (margin angle).** Margin is assessed on an account or portfolio, not on a position. LD-R0017 already says "not individual-position causality". The gross or net basis of positions (review 02) feeds a gross-margined requirement. No firm decision is needed.

**Principle 7 mapping.** Requirement = LD-C0043; call = LD-C0046; eligible collateral = LD-C0048 + NEW-MC-04; posted collateral = LD-C0047 (State); remaining shortfall = NEW-MC-07.

**EV-001-Q03 resolution check.** A Rule Change (reviews 05/06/08) introduces intraday runs at the CCP–member tier of a Clearing Service → new LD-C0043 runs (run type "intraday") → LD-C0046 with a Cut-off (NEW-OPS-01, review 07) → LD-C0049 movements (also LD-C0029 when cash) → whether the member passes calls on at the member–client tier (Q5). No call-cycle concept is needed.

**GDI mapping.** Once accepted, re-point "portfolio margining" and "cross-margining governance" to NEW-MC-01, and add NEW-MC-04 to "non-cash" and "tokenised collateral". "Intraday margin" stays related to LD-C0043/LD-C0046 via the run-type qualifier.

## 4. Proposed new concepts

**Module.** Common, subdomain "Margin & Collateral", steward Risk/Collateral (named in docs/governance.md): LD-C0043–0049 are already there, and every concept below applies identically to ETD and OTC; only instances differ. Revisit beyond about 20 concepts. Named models (SPAN, PRISMA, PAIRS) are instances of NEW-MC-01, not subclasses. French labels are given in brackets, as master prompt v2 requires.

| Temp ID | Name | Module | Type | Definition | Key relationships | Standard alignment (to verify) | Prio | Needed by |
|---|---|---|---|---|---|---|---|---|
| NEW-MC-01 | Margin Methodology [Méthodologie de marge] | Common | Reference Concept | Versioned rules and parameters by which a margin taker determines margin requirements for a scope. They cover: model family (e.g. scenario-based or VaR/historical simulation), confidence level, close-out period, look-back, offsets, add-ons and anti-procyclicality measures. At the member–client tier the basis is one of: CCP replication, CCP replication with multiplier or add-on, or own model. | LD-C0043 determined_under; provided_by the CCP or clearing member role; member–client version derived_from the CCP version; affected_by Rule Change | PFMI P6; EMIR Art. 41; Delegated Reg. (EU) 153/2013; CFTC 39.13 | P1 | EV-005-Q02, EV-006-Q02, GDI "portfolio margining" |
| NEW-MC-03 | Collateral Arrangement [Convention de garantie financière] | Common | Agreement (is_a LD-C0012) | Terms under which collateral is provided, valued, substituted, remunerated and returned between a provider and a taker: legal form (title transfer or security interest), secured obligations, eligibility schedule, haircut and valuation terms, interest terms. It can be a standalone agreement or part of a CCP rulebook or client clearing agreement. | governs LD-C0047, LD-C0049; secures LD-C0043 (n:m); references NEW-MC-04 | Directive 2002/47/EC; MiFID II Art. 16(10) (no title-transfer arrangements with retail clients); CDM collateral model; ISDA CSA as the bilateral analogue | P1 | UC-001 (legal form, portability), UC-002; closes the deferred note in relationships.md |
| NEW-MC-04 | Collateral Eligibility Schedule [Barème d'éligibilité des garanties] | Common | Reference Concept | Versioned list published by a collateral taker of the assets acceptable for a service, account type and tier, with haircuts (including FX haircuts), concentration limits and wrong-way restrictions. | published_by the CCP or clearing member role; admits LD-C0048; referenced_by NEW-MC-03; affected_by Rule Change | EMIR Art. 46; Delegated Reg. 153/2013 Annexes I–II; CDM eligible-collateral specification | P1 | EV-005-Q03; GDI "non-cash" and "tokenised collateral" |
| NEW-MC-07 | Margin Excess / Shortfall [Excédent / insuffisance de couverture] | Common | Measure | Signed difference between the value after haircut of the collateral held (LD-C0047) and the margin requirement (LD-C0043), for the same provider–taker pair, account, as-of time and currency basis. A shortfall gives rise to a call; an excess may be returned on request. | compares LD-C0047 with LD-C0043; LD-C0046 based_on | Principle 7 ("remaining shortfall"); LD-R0018 note | P1 | EV-006-Q02, EV-001-Q03 |
| NEW-MC-08 | Default Fund Contribution [Contribution au fonds de défaillance] | Common | Obligation | Clearing member's pre-funded contribution to a CCP's mutualised default resources for a clearing service, sized by the CCP's stress-testing method. It is distinct from margin, which covers the member's own risk, and from fees. Assessment powers beyond it are a qualifier. | owed_by LD-C0007 to LD-C0008, per Clearing Service | EMIR Art. 42; PFMI P4 and P13 | P2 | EV-002-Q01 (cost of direct membership vs access through a member), UC-001 |
| NEW-MC-11 | Cash Collateral Interest [Intérêts sur garanties en espèces] | Common | Obligation | Interest payable between collateral taker and provider on cash collateral for a period, at a stated rate basis and spread (possibly negative), including PAI on CTM VM. | arises_under NEW-MC-03; accrues_on LD-C0047 (cash); reaches LD-C0042 only through a semantic contract | CCP interest policies are instances | P2 (P1 if Q1 says yes) | UC-004 (EV-004-Q05) |

**Withdrawn from v1 (IDs not reused):** NEW-MC-02 Tier → provider/taker qualifiers via Party Role Assignment (review 08); NEW-MC-05 Collateral Balance and NEW-MC-06 Collateral Value → LD-C0047 as State with value attributes; NEW-MC-09 Call Cycle → run-type qualifier + Cut-off (review 07) + Rule Provision; NEW-MC-10 Client Margin Policy → member–client basis of NEW-MC-01.

**Taxonomy values, not concepts:** margin component (base IM, add-ons, premium/NLV margin, VM), run type, margining basis, VM treatment, collateral legal form, cash/non-cash, "price alignment" as a purpose of LD-C0028.

## 5. Proposed new or changed relationships

- LD-C0043 – determined_under – NEW-MC-01 (one version per run); NEW-MC-01 – derived_from – NEW-MC-01 (member–client replication of the CCP method).
- LD-C0043 / LD-C0046 / NEW-MC-07 – has_margin_provider / has_margin_taker – Party Role Assignment (review 08): mandatory; tier = the two roles + account type.
- LD-C0045 – gives_rise_to – LD-C0028 (STM) or an obligation under NEW-MC-03 (CTM); treatment from Clearing Service × account type, versioned.
- LD-C0028 (purpose: price alignment) – relates_to – LD-C0045; PAI/PAA is never part of VM.
- NEW-MC-03 – secures – LD-C0043 (n:m; context tier and account); – governs – LD-C0047, LD-C0049; – part_of – LD-C0012 (client clearing agreement, review 03, or CCP rulebook).
- NEW-MC-04 – admits – LD-C0048 (haircut, limits, validity); – applies_to – Clearing Service × account type × tier.
- LD-C0047 – of_asset – LD-C0048 (quantity); – held_for – LD-C0010; – under – NEW-MC-03.
- LD-C0049 – moves – LD-C0048; – changes – LD-C0047 (LD-R0019); – also_classified_as – LD-C0029 (cash only, counted once).
- NEW-MC-07 – compares – LD-C0047 (after haircut) and LD-C0043 (same pair, account, as-of, currency). LD-C0046 – based_on – NEW-MC-07 (shortfall only); – satisfied_by – LD-C0049 (0..n, partial allowed); – subject_to – Cut-off (NEW-OPS-01).
- LD-C0011 – implies_margining_basis – {gross, net}, per Clearing Service and account type.
- NEW-MC-08 – owed_by – LD-C0007; – owed_to – LD-C0008; – for – Clearing Service.
- Rule Change – affects – NEW-MC-01 / NEW-MC-03 / NEW-MC-04: the most frequent margin-related circular targets (UC-001, UC-005).

## 6. Proposed new ambiguity entries

| Temp ID | Term | Required distinction | Reviewer |
|---|---|---|---|
| NEW-A-MC-01 | "Margin" meaning collateral | "Client margin held" usually means collateral (LD-C0047); "margin required" means LD-C0043; "margin posted" means delivered collateral. | Risk / Collateral |
| NEW-A-MC-02 | Excess | Three distinct meanings: excess at the CCP on the member's account; client excess held by the member; US customer-funds "excess" held above customer requirements (terminology to verify). State the tier and where the excess is held. | Collateral / Legal |
| NEW-A-MC-03 | Margin components across CCPs | Premium margin, NLV, spread and delivery charges, and add-ons differ by CCP. Never sum or compare them across CCPs without a component mapping. | Risk |
| NEW-A-MC-05 | House vs client | The CCP account type does not determine the economic relationship: affiliates may be cleared as clients or in the house account (cf. LD-A0007). | Clearing Product / Legal |
| NEW-A-MC-06 | "Initial margin" | Three meanings: CCP IM (exposure coverage); the US futures initial vs maintenance call levels; IM under bilateral uncleared-margin rules (out of scope, must not resolve to LD-C0044). | Risk |

v1 NEW-A-MC-04 (currency basis) is withdrawn because principle 8 already covers it.

## 7. Questions only the business owner or internal sources can answer

1. **Does management revenue include collateral economics?** That is, net interest on client cash, price alignment pass-through, and fees on non-cash collateral. This sets the scope of LD-C0042 and the priority of NEW-MC-11. *Default:* a separate measure, excluded until Finance decides.
2. **When someone asks for "margin required for this client" (EV-006-Q02), which tier applies by default?** *Default:* none, so AG-006 asks. If the business approves a default, use member–client IM plus VM.
3. **Which member–client methodology bases must the vocabulary cover?** The options are CCP replication, a multiplier or add-on, or an own model; these are values only, with no figures. *Default:* all three.
4. **How does the business take client collateral: title transfer, security interest, or both, by entity or service?** This drives the portability answers in UC-001. *Default:* model both, with firm values to validate by Legal.
5. **Are intraday CCP calls passed on to clients (EV-001-Q03)?** *Default:* model calls at both tiers; firm practice stays internal.
6. **Do default-fund contributions and the cost of funding house margin belong in the contribution-after-costs perimeter?** *Default:* no; NEW-MC-08 stays at P2.
7. **For UC-006, is the member–client requirement always the firm's own calculation, with CCP figures used only at the CCP tier?** *Default:* yes.
8. **Who is the named Risk/Collateral steward?** *Default:* the sponsor arbitrates until one is named.

## 8. Cross-review

**(a) Disagreements**
- **08, LD-C0047 retype:** agree, but to **State, not Role**; here a Role is held by a party (LD-C0003), and an asset is not one.
- **08, Collateral Arrangement at P2:** should be **P1**; STM/CTM conversions and title-transfer effects on portability are live UC-001 inputs, and relationships.md anticipates it.
- **05, Margin Methodology at P2:** should be **P1**; EV-005-Q02 is unanswerable without it.
- **07, Business Record:** a CCP-reported requirement and the member's replication of it are two records of one object (divergence = break). The member–client requirement is a different object (another tier); its difference from the CCP figure is not a break.
- **03, PAI/PAA:** agree it is a distinct flow, but as LD-C0028 with purpose "price alignment", not a new concept.
- **02/03, Porting:** positions and collateral port as separate legs with separate outcomes; collateral portability depends on segregation model and legal form, so never infer it from a successful position transfer.

**(b) Duplicates, with one canonical name each**

| Topic | Proposed by | Canonical |
|---|---|---|
| Margin methodology | 04 NEW-MC-01, 05 NEW-RSK-01 | Margin Methodology, P1, Margin & Collateral subdomain |
| Collateral arrangement | 04 NEW-MC-03, 08 NEW-COM-06 | Collateral Arrangement, Agreement, P1 |
| Default fund | 04 NEW-MC-08, 06 NEW-REG-09 | Default Fund Contribution, Obligation, P2, Risk/Collateral steward |
| Porting | 02 NEW-COM-04, 03 NEW-COM-08 | Porting, Process, Common; position and collateral legs |
| Interest income | 05 NEW-A-05, 04 Q1 | One ambiguity, "Clearing revenue scope" (Finance); obligation concept NEW-MC-11 |
| Collateral as asset, role or balance | 08 NEW-AMB-03 | No entry needed once LD-C0047 becomes a State |
| CCP service | 02/03 NEW-COM-01, 05 NEW-COM-03, 08 NEW-COM-01 | Clearing Service, distinct from 05's Service Offering. NEW-MC-01, NEW-MC-04, NEW-MC-08 and the VM treatment attach to it. |

**(c) What other reviews raise that affects margin and collateral**
- Party Role Assignment (08) carries provider and taker and replaces my v1 tier concept.
- CCP Account (02) is the CCP-tier assessment unit; its gross/net position basis drives gross-margined requirements.
- Rule Provision / Rule Change (05, 06, 08) are needed for EV-001-Q03 and for methodology and eligibility circulars.
- Cut-off and Business Calendar (07) carry call deadlines and the 24/5 effects of EV-001-Q05 (intraday runs, payment-system windows).
- Indirect Client (03) adds the client–indirect client tier; only the tier value is needed.
- Regulatory Classification (06): QCCP status drives the capital cost of NEW-MC-08 (P3, after Q6).
- 06's NEW-A-REG-05 ("protected/segregated/portable") covers my LD-C0011 caution; keep it there.
- French labels (08, master prompt) are adopted for all new concepts above.
