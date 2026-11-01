# Phase 1 review

Status: Foundation approved for further development, with open semantic questions

## Sponsor decision — 2026-09-20

Evidence: the business sponsor explicitly responded to the seven review points in the project conversation. This approves the architecture and development direction, not every individual concept definition.

| Point | Decision | Consequence |
|---|---|---|
| 1. Scope and architecture | Approved | Shared core plus Listed Execution, ETD Clearing and OTC Clearing modules. |
| 2. Foundation and sequence | Approved | Retain the 50 concepts as a provisional foundation; develop Common, Execution, ETD Clearing, then OTC Clearing. |
| 3. Client | Approved | Start with the contractual service-recipient role; distinguish legal entity, commercial group and beneficial owner. |
| 4. Revenue perspective | Management focus requested | Prioritise business performance: what the activity earns and what a client brings to the business. Accounting revenue is not the current modelling priority. |
| 5. Commission and Transaction | Deferred: “a voir” | Keep both Draft. Their firm-specific meanings and equivalences remain unresolved. |
| 6. Relationships | General approach approved | Refine constraints by context; no universal fill-to-trade cardinality is approved. |
| 7. Governance | Proposed approach approved | Sponsor arbitrates Business/Product scope; Operations, Finance, Risk and Legal review relevant subjects. Individual reviewers remain to be assigned. |

Later sponsor answers are recorded in the [decision log](decision-log.md).

## Remaining boundaries

All individual concept definitions remain Draft until specifically reviewed and approved. The approval permits Phase 2 development; it does not approve detailed taxonomies, metric formulas, query-resolution demonstrations or physical mappings.

The request to model what the business earns does not settle the distinction between revenue and contribution after costs. Gross/net treatment, pass-through charges, broker/exchange/CCP costs, shared-cost allocation and timing remain open. Keep revenue and profitability measures distinguishable rather than silently treating them as equivalent.
