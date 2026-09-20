# Taxonomy design

Status: Phase 1 axes only. Detailed taxonomies are deferred to Phase 3.

| Taxonomy | Proposed classification axes |
|---|---|
| Participants | Party type; service role; contractual role; membership |
| Products | Asset class; derivative family; contractual form; trading mode; clearing eligibility |
| Orders / executions / trades | Instruction type; service channel; strategy; event; lifecycle state |
| Fees | Service; debtor; creditor; beneficiary; tariff basis; pass-through treatment |
| Accounts | Function; maintaining party; holder; recording level; segregation regime |
| Positions | Scope; gross/net; direction; status; as-of basis |
| Margin | Type; relationship; risk scope; calculation and call frequency |
| Collateral | Asset class; currency; eligibility; valuation; mobilisation state |
| Settlement | Cash/physical; obligation; method; due date; status |
| Post-trade lifecycle | Event; transition; economic effect; legal effect |
| Regulatory | Jurisdiction; regime; obligation; responsible role; effective dates |

## Constraints

Use multiple axes rather than a single artificial tree. Separate is_a specialisations from contextual categories and overlapping facets. No disjointness or exhaustiveness is assumed without review.

Cleared is not equivalent to exchange-traded. High-touch/low-touch describes a service or handling channel rather than an asset class or venue. A charge's classification does not determine its accounting recognition. Named markets, entities and currencies are reference instances, not automatic subclasses.
