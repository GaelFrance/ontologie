# Taxonomy design

Status: Phase 1 axes, extended with Draft seed values by the 2026-11 expert review. Detailed taxonomies are deferred to Phase 3.

| Taxonomy | Proposed classification axes |
|---|---|
| Participants | Party type; service role; contractual role; membership category; client segment |
| Products | Asset class; derivative family; contractual form; trading mode; clearing eligibility; regulatory product class |
| Orders / executions / trades | Instruction type; order handling channel (LD-C0061); execution method; trading capacity; order type; time in force; strategy; event; lifecycle state; clearing tier |
| Fees | Service; service nature; chargeable event; debtor; creditor; collector; beneficiary; tariff basis; pass-through treatment; amount certainty; billing stage; recurrence; incentive programme |
| Accounts | Function; maintaining party; holder; recording level; CCP account type; segregation regime |
| Positions | Scope; gross/net; direction; status; as-of basis |
| Margin | Type; component; tier (provider and taker); risk scope; run type; VM treatment; margining basis; calculation and call frequency |
| Collateral | Asset class; currency; cash or non-cash; legal form; eligibility; valuation basis; mobilisation state |
| Settlement | Cash/physical; obligation; method; due date; status |
| Post-trade lifecycle | Event; transition; economic effect; legal effect; interposition mechanism |
| Regulatory | Jurisdiction; regime; obligation; responsible role; attachment level; classification basis; date role |
| Access | Access model; scope (venue or clearing service); intermediary; status |
| Costs | Cost category |

## Seed values from the 2026-11 expert review

Draft seed values, to be completed in Phase 3. They are vocabulary values, not concepts, and carry no IDs.

| Vocabulary | Seed values |
|---|---|
| Order handling channel (values of LD-C0061) | care; broker algorithm; direct market access; sponsored access |
| Execution method | matching on a venue (order book or request for quote); registration on a venue of a privately negotiated trade (block trade, exchange for related position, other venue-defined types); bilateral off-venue |
| Trading capacity | agency; principal; riskless principal (alignment with transaction-reporting capacity values to verify) |
| Clearing tier | pre-clearing; CCP–member house; CCP–member client account; member–client; client–indirect client; uncleared bilateral |
| Interposition mechanism | novation; open offer; other |
| Access model | direct membership (by category); through a third-party member; direct electronic access; client clearing; indirect clearing; sponsored or direct-client model |
| Client clearing legal model | principal-to-principal; agency or guarantee; indirect chain |
| Give-up status (harmonised) | pending; accepted in full; accepted in part; rejected; lapsed; cancelled; reversed; unknown — native statuses always kept |
| Margin component | base initial margin; add-ons; premium or net liquidation value margin; variation margin |
| Run type | scheduled end-of-day; scheduled intraday; ad hoc |
| VM treatment | settled-to-market; collateralised-to-market; not applicable |
| Collateral legal form | title transfer; security interest |
| Fee chargeable event | execution; give-up; transfer; exercise or assignment; delivery; OTC registration or maintenance; compression; porting; periodic |
| Fee amount certainty and billing stage | estimated, final; accrued, invoiced, disputed, adjusted, settled, written off |
| Cost category | non-recharged venue and CCP fees; third-party brokerage; third-party clearing; connectivity and market data; funding and collateral; allocated shared cost |
| Regulatory attachment level | legal entity; role assignment; account; trade or report; CCP, venue or clearing service |
| Date role | trade date; CCP clearing date; value date; booking date; reporting date; last trading day; expiry; exercise deadline; first notice day; final settlement day; delivery day; publication; entry into force; application; phase-in; end of transition; as-of date |

## Constraints

Use multiple axes rather than a single artificial tree. Separate is_a specialisations from contextual categories and overlapping facets. No disjointness or exhaustiveness is assumed without review.

Cleared is not equivalent to exchange-traded, and regulatory "OTC" is not equivalent to off-venue (LD-A0032). High-touch/low-touch describes a service or handling channel rather than an asset class or venue. A charge's classification does not determine its accounting recognition. Named markets, entities and currencies are reference instances, not automatic subclasses.
