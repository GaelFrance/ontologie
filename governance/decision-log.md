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

These answers do not resolve any ambiguity entry, approve any definition, formula or cost perimeter, or change the deferral of Commission and Transaction.
