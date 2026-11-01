# Decision log

Status: Record of business-owner decisions after the [Phase 1 review](phase-1-review.md). A decision narrows scope or modelling direction; it does not approve individual concept definitions, which remain Draft.

## Sponsor answers — 2026-11-01

Evidence: sponsor answer in the project conversation, 2026-11-01, in reply to the execution reviewer's owner questions in the [2026-11 expert review](reviews/2026-11-expert-review/01-execution.md) (section 7, questions 1, 3, 4 and 8).

| Point | Decision | Consequence in the ontology | Affected IDs |
|---|---|---|---|
| 1. Service mix | The firm offers execution-only, clearing-only and full execute-and-clear. Both give-up (out) and give-in directions must be supported. Revenue is attributed per service. | Service Offering (LD-C0052) carries the service kind; LD-C0022 covers both directions; revenue is attributed per service to that service's contractual client (LD-R0077). LD-A0014 narrowed. | LD-C0022, LD-C0039, LD-C0041, LD-C0042, LD-C0052, LD-R0077, LD-A0014 |
| 2. Revenue split by order handling channel | Yes: care, algorithm, DMA and sponsored access must be distinguishable. | Order Handling Channel (LD-C0061) added at P1 and made required context of Execution Revenue. | LD-C0016, LD-C0041, LD-C0061, LD-R0046 |
| 3. Third-party execution | In scope: executions routed through another venue member where the firm is not a member. Memberships are never inferred. | Trading Venue Member (LD-C0058) kept distinct from Executing Broker (LD-C0006); third-party access is an access model of LD-C0059. | LD-C0006, LD-C0058, LD-C0059, LD-A0035 |
| 4. Average pricing | Both venue or CCP average-price facilities and broker-side averaging are in scope. The treatment of rounding residuals is not known by the sponsor. | LD-C0021 qualifier "averaging performed by" takes both values. Residuals remain an open question for Finance and Operations; proposed default: separately identifiable amounts. | LD-C0021 |

## Sponsor decision — 2026-11-01 (give-up completion)

Evidence: sponsor accepted the suggested default for open question 1 ("ok défaut") in the project conversation, 2026-11-01.

| Point | Decision | Consequence in the ontology | Affected IDs |
|---|---|---|---|
| 5. Give-up completion and authoritative record | A give-up is complete when the full allocated quantity is registered to the receiving clearing member's CCP account, per the CCP record. Partial take-ups are reported separately. Member acceptance and CCP registration times are both kept. When internal and CCP records disagree, the CCP record is authoritative for completion and the discrepancy is reported as a break, never silently resolved. | LD-A0010 decided for the default answer of AG-004; the definitions of LD-C0022, LD-C0023 and LD-C0053 remain Draft. | LD-C0022, LD-C0023, LD-C0053, LD-A0010, LD-A0034 |

## Sponsor decision — 2026-11-01 (meaning changes kept as Draft)

Evidence: sponsor answered "ok" in the project conversation, 2026-11-01, after an explanation of each change (open question 2).

| Point | Decision | Consequence in the ontology | Affected IDs |
|---|---|---|---|
| 6. Meaning changes and clarifications from the expert review | Accepted as Draft: Instrument narrowed to standardised specifications; give-up as attribution at or after CCP registration; Clearing Acceptance as the CCP side with member take-up separate; Collateral as a State (title transfer or security interest); Party Role as the role assignment; Product relabelled Product Family. | The changes stay in the catalogue as Draft. This accepts the direction of the changes, not a Reviewed or Approved status for the definitions. | LD-C0003, LD-C0013, LD-C0014, LD-C0022, LD-C0023, LD-C0047 |

## Sponsor decision — 2026-11-01 (reference clearing services)

Evidence: sponsor answer in the project conversation, 2026-11-01 (open question 3).

| Point | Decision | Consequence in the ontology | Affected IDs |
|---|---|---|---|
| 7. Reference clearing services for rulebook evidence | Five public CCPs seed the evidence for AG-004: Eurex Clearing, ICE Clear Europe, LCH (SwapClear service), CME Clearing and Euronext Clearing. | These become the first Clearing Service instances whose public rulebooks are cited for interposition mechanism and moment, give-up deadlines and cut-offs. Instances and rulebook facts belong to the hub's evidence layer, not to the concept catalogue; each fact must cite the public rule and its version. | LD-C0051, LD-C0054, LD-C0065, LD-A0009, LD-A0017 |

## Sponsor decision — 2026-11-01 (regulatory regime priority)

Evidence: sponsor answer in the project conversation, 2026-11-01 (open question 5).

| Point | Decision | Consequence in the ontology | Affected IDs |
|---|---|---|---|
| 8. Regulatory regime priority | Global scope. Priority 1: Europe (EU: EMIR including EMIR 3, MiFID II/MiFIR, CRR; and UK) and United States (CFTC and SEC). Priority 2: Asia-Pacific regimes, to be scoped. | Regime instances for AG-002 and AG-003 are seeded in this order; US futures and cleared-swaps structures are no longer treated "in general terms" only. | LD-C0063, LD-C0067, LD-C0068 |

## Sponsor decisions — 2026-11-01 (consultations and default date)

Evidence: sponsor answers in the project conversation, 2026-11-01 (open questions 6 and 7).

| Point | Decision | Consequence in the ontology | Affected IDs |
|---|---|---|---|
| 9. Consultations and sign-off | Consultations and draft rules are analysed as rule changes, with a mandatory status and a "not yet in force" flag. Readings flagged "interpretation required" are reviewed by Regulatory Affairs and business management first, with Legal and Compliance. Agent outputs are labelled "public-layer reading, not legal advice". | Rule Change carries a lifecycle status (consultation, adopted, in force, withdrawn); the reviewer roles are recorded as governance roles, not people. | LD-C0064, LD-R0053, LD-A0022 |
| 10. Default meaning of "today" and "current" | The clearing date of the relevant CCP, in that CCP's time zone, stated in every answer. | Date role "clearing date" is the default for operational questions; other date roles must be requested explicitly. Record time stays in the model for later audit needs. | LD-C0015, LD-C0066, LD-A0015, LD-A0023 |

Apart from LD-A0010 (decision 5), these answers do not resolve any ambiguity entry, approve any definition, formula or cost perimeter, or change the deferral of Commission and Transaction.
