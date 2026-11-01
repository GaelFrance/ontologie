# Concept annotations

Status: Draft. Companion to the [concept catalogue](foundation.md), which stays the single index of IDs and definitions.

This page holds per-concept data that does not fit the catalogue's five-column table: specialisations, aliases, resolution flags, usage notes, required context, priorities and standard alignments. It is kept separate because the agent hub currently parses the catalogue table by cell position. When detailed concept fiches are written (template fields `parents`, `aliases`, `required_context`, `label_fr`, `alignments`, `resolution`), the content below moves into them and this page is retired.

Standard alignments are "map, do not import" proposals: none has been checked against the published specification, so all are **to verify**, and no IRI or URL is asserted.

## Specialisations

`is_a` is asserted only where every instance of the child meets the parent's definition. Classes are not declared disjoint: one object may carry two classifications (for example a cash collateral transfer is both LD-C0049 and LD-C0029, counted once).

| Child | Parent | Status and source |
|---|---|---|
| LD-C0002 Legal Entity | LD-C0001 Party | Phase 1 proposal |
| LD-C0004 Client | LD-C0003 Party Role | Phase 1 proposal |
| LD-C0005 Broker | LD-C0003 Party Role | Phase 1 proposal |
| LD-C0007 Clearing Member | LD-C0003 Party Role | Phase 1 proposal |
| LD-C0008 Central Counterparty | LD-C0003 Party Role | Phase 1 proposal |
| LD-C0058 Trading Venue Member | LD-C0003 Party Role | 2026-11 review [01] |
| LD-C0006 Executing Broker | LD-C0005 Broker | Phase 1 proposal |
| LD-C0057 Clearing Broker | LD-C0005 Broker | 2026-11 review [02, 05, 08] |
| LD-C0033 to LD-C0037 fee types | LD-C0031 Fee Charge | Phase 1 proposal; not mutually exclusive, not additive |
| LD-C0041 Execution Revenue, LD-C0042 Clearing Revenue | LD-C0039 Revenue | Phase 1 proposal |
| LD-C0044 Initial Margin Requirement, LD-C0045 Variation Margin Requirement | LD-C0043 Margin Requirement | Phase 1 proposal |
| LD-C0055, LD-C0056, LD-C0059, LD-C0071 | LD-C0012 Agreement | 2026-11 review [01, 02, 03, 04, 05] |
| LD-C0069 CCP Account | LD-C0010 Account | 2026-11 review [02] |
| LD-C0065 Cut-off | LD-C0063 Rule Provision | 2026-11 review [07, 08] |
| LD-C0017 Execution, LD-C0023 Clearing Acceptance, LD-C0024 Novation, LD-C0053 Clearing Member Acceptance, LD-C0054 CCP Interposition | LD-C0025 Lifecycle Event | 2026-11 review [08]; Execution is a lifecycle event from the order's perspective |
| LD-C0075 Natural Person | LD-C0001 | 2026-11 domain review |
| LD-C0077 Investment Fund | LD-C0001 | 2026-11 domain review |
| LD-C0078 Authorised Representative | LD-C0003 | 2026-11 domain review |
| LD-C0079 Investment Manager | LD-C0078 | 2026-11 domain review |
| LD-C0080 Economic Beneficiary | LD-C0003 | 2026-11 domain review |
| LD-C0081 Indirect Client | LD-C0004 | 2026-11 domain review |
| LD-C0083 Parent Entity | LD-C0003 | 2026-11 domain review |
| LD-C0084 Contracting Entity | LD-C0003 | 2026-11 domain review |
| LD-C0085 Intra-group Client | LD-C0004 | 2026-11 domain review |
| LD-C0086 Non-Clearing Member | LD-C0004 | 2026-11 domain review |
| LD-C0087 Sponsored Clearing Participant | LD-C0003 | 2026-11 domain review |
| LD-C0088 Client Regulatory Category | LD-C0068 | 2026-11 domain review |
| LD-C0089 Counterparty Regulatory Status | LD-C0068 | 2026-11 domain review |
| LD-C0090 Client Account | LD-C0010 | 2026-11 domain review |
| LD-C0091 Market Operator | LD-C0003 | 2026-11 domain review |
| LD-C0092 Settlement or Custody Agent | LD-C0003 | 2026-11 domain review |
| LD-C0095 Listed Strategy | LD-C0014 | 2026-11 domain review |
| LD-C0096 Flexible Series | LD-C0014 | 2026-11 domain review |
| LD-C0099 Contract Adjustment | LD-C0025 | 2026-11 domain review |
| LD-C0107 Offering Eligibility Criterion | LD-C0063 | 2026-11 domain review |
| LD-C0108 Access Agreement | LD-C0012 | 2026-11 domain review |
| LD-C0110 Access Requirement | LD-C0063 | 2026-11 domain review |
| LD-C0112 Direct Electronic Access Arrangement | LD-C0059 | 2026-11 domain review |
| LD-C0113 Third-Party Execution Arrangement | LD-C0059 | 2026-11 domain review |
| LD-C0114 Non-Clearing Member Arrangement | LD-C0059 | 2026-11 domain review |
| LD-C0115 Sponsored Clearing Arrangement | LD-C0059 | 2026-11 domain review |
| LD-C0116 Indirect Clearing Arrangement | LD-C0059 | 2026-11 domain review |
| LD-C0117 Client Order | LD-C0016 | 2026-11 domain review |
| LD-C0118 Child Order | LD-C0016 | 2026-11 domain review |
| LD-C0120 Venue Execution | LD-C0017 | 2026-11 domain review |
| LD-C0121 Client Execution | LD-C0017 | 2026-11 domain review |
| LD-C0122 Block Trade | LD-C0017 | 2026-11 domain review |
| LD-C0123 Exchange for Related Position | LD-C0017 | 2026-11 domain review |
| LD-C0124 Strategy Leg Execution | LD-C0017 | 2026-11 domain review |
| LD-C0125 Execution Correction | LD-C0025 | 2026-11 domain review |
| LD-C0126 Executed Trade | LD-C0018 | 2026-11 domain review |
| LD-C0128 Standing Allocation Instruction | LD-C0060 | 2026-11 domain review |
| LD-C0130 Third-party Executing Member | LD-C0058 | 2026-11 domain review |
| LD-C0132 Give-up Designated in Advance | LD-C0022 | 2026-11 domain review |
| LD-C0133 Give-up after First Registration | LD-C0022 | 2026-11 domain review |
| LD-C0134 Giving Clearing Member | LD-C0003 | 2026-11 domain review |
| LD-C0135 Receiving Clearing Member | LD-C0003 | 2026-11 domain review |
| LD-C0136 Take-up | LD-C0053 | 2026-11 domain review |
| LD-C0137 Submission Acceptance | LD-C0053 | 2026-11 domain review |
| LD-C0138 Clearing Limit | LD-C0063 | 2026-11 domain review |
| LD-C0140 Take-up Deadline | LD-C0065 | 2026-11 domain review |
| LD-C0142 Execution Agreement for Cleared Trades | LD-C0012 | 2026-11 domain review |
| LD-C0143 CCP-facing Trade | LD-C0018 | 2026-11 domain review |
| LD-C0144 Client Back-to-Back Trade | LD-C0018 | 2026-11 domain review |
| LD-C0145 House Account | LD-C0069 | 2026-11 domain review |
| LD-C0146 Client Omnibus Account | LD-C0069 | 2026-11 domain review |
| LD-C0147 Individually Segregated Client Account | LD-C0069 | 2026-11 domain review |
| LD-C0148 Indirect Client Account | LD-C0069 | 2026-11 domain review |
| LD-C0151 Listed Position | LD-C0026 | 2026-11 domain review |
| LD-C0152 Cleared OTC Position | LD-C0026 | 2026-11 domain review |
| LD-C0153 Position Transfer | LD-C0025 | 2026-11 domain review |
| LD-C0154 Clearing Member Default | LD-C0025 | 2026-11 domain review |
| LD-C0156 Back-up Clearing Member | LD-C0003 | 2026-11 domain review |
| LD-C0157 Sponsoring Clearing Member | LD-C0003 | 2026-11 domain review |
| LD-C0158 Position Adjustment | LD-C0025 | 2026-11 domain review |
| LD-C0159 Client Default | LD-C0025 | 2026-11 domain review |
| LD-C0164 Margin Portfolio | LD-C0027 | 2026-11 domain review |
| LD-C0173 Margin Provider | LD-C0003 | 2026-11 domain review |
| LD-C0174 Margin Taker | LD-C0003 | 2026-11 domain review |
| LD-C0175 Published Fee Schedule | LD-C0032 | 2026-11 domain review |
| LD-C0176 Client Pricing Terms | LD-C0032 | 2026-11 domain review |
| LD-C0179 Pass-through Charge | LD-C0031 | 2026-11 domain review |
| LD-C0180 Bundled Execution and Clearing Fee | LD-C0031 | 2026-11 domain review |
| LD-C0181 Regulatory Transaction Fee | LD-C0031 | 2026-11 domain review |
| LD-C0182 Fee Rebate | LD-C0031 | 2026-11 domain review |
| LD-C0185 Fee Collector | LD-C0003 | 2026-11 domain review |
| LD-C0187 Collateral Revenue | LD-C0039 | 2026-11 domain review |
| LD-C0191 Clearing Obligation | LD-C0190 | 2026-11 domain review |
| LD-C0194 Rulebook | LD-C0063 | 2026-11 domain review |
| LD-C0195 Regulatory Relief | LD-C0063 | 2026-11 domain review |
| LD-C0196 Equivalence Decision | LD-C0063 | 2026-11 domain review |
| LD-C0202 Regulatory Authorisation | LD-C0068 | 2026-11 domain review |
| LD-C0203 Regulatory Authority | LD-C0003 | 2026-11 domain review |
| LD-C0204 Regulatory Reporting Role | LD-C0003 | 2026-11 domain review |
| LD-C0206 CCP Report | LD-C0205 | 2026-11 domain review |
| LD-C0208 Position Reconciliation | LD-C0050 | 2026-11 domain review |
| LD-C0211 Netted Settlement Obligation | LD-C0028 | 2026-11 domain review |
| LD-C0213 Settlement Account | LD-C0010 | 2026-11 domain review |
| LD-C0214 Settlement Deadline | LD-C0065 | 2026-11 domain review |
| LD-C0215 Firm Cut-off | LD-C0065 | 2026-11 domain review |
| LD-C0216 Expiry | LD-C0025 | 2026-11 domain review |
| LD-C0217 Exercise | LD-C0025 | 2026-11 domain review |
| LD-C0219 Assignment | LD-C0025 | 2026-11 domain review |
| LD-C0220 Final Settlement | LD-C0025 | 2026-11 domain review |
| LD-C0222 Trade Amendment | LD-C0025 | 2026-11 domain review |

Not asserted: a common "Service" parent for LD-C0051 and LD-C0052 (see LD-A0020); a parent for LD-C0038 Commission (deferred by the sponsor).

## Resolution flags

| Concept | Flag | Behaviour expected from agents |
|---|---|---|
| LD-C0019 Transaction | blocked-pending-decision | Never resolve "transaction" to this ID alone; return candidates LD-C0017, LD-C0018, LD-C0025, LD-C0029 and the MiFIR reporting "transaction", and ask. |
| LD-C0038 Commission | blocked-pending-decision | Never resolve "commission" to this ID alone; return candidates LD-C0033, LD-C0034 and a bundled execute-and-clear charge, and ask. |

Both concepts stay Draft and deferred by sponsor decision of 2026-09-20; the flag does not define them.

## Aliases

Kinds: **exact** (same meaning everywhere in scope), **contextual** (same meaning only within the stated scope), **ambiguous** (several candidates; the agent must list them and ask). Internal firm jargon is not recorded here.

| Alias | Kind | Scope | Resolves to |
|---|---|---|---|
| fill | contextual | Order perspective | LD-C0017 (see LD-A0024) |
| registration | contextual | CCP side of clearing | LD-C0023 |
| take-up, claim | contextual | Listed give-up, receiving member | LD-C0053 |
| give-in | contextual | Listed give-up, receiving side's view | LD-C0022 |
| give-up (OTC or FX) | ambiguous | OTC and FX prime brokerage | Not LD-C0022 by default (LD-A0026) |
| cleared | derived status | Any clearing service | State resulting from LD-C0054 |
| open offer | mechanism value | Clearing | Value of the mechanism of LD-C0054, not a concept |
| alpha trade | contextual | OTC clearing | LD-C0018 at the pre-clearing tier |
| clearing broker | exact | Client clearing | LD-C0057 |
| FCM | contextual | US | LD-C0057 role plus a LD-C0068 registration of the legal entity |
| DCO | contextual | US | LD-C0008 plus a LD-C0068 registration |
| non-clearing member | contextual | Listed markets | Holder of LD-C0058 without LD-C0007 for that service |
| executing firm | ambiguous | Execution | LD-C0006, LD-C0058 (LD-A0035) |
| market operator | contextual | MiFID II | LD-C0002 related by LD-R0051 |
| exchange | ambiguous | Any | LD-C0009, its operator LD-C0002, or the exchange group |
| product | ambiguous | Any | LD-C0013, LD-C0062, LD-C0014, LD-C0052 (LD-A0021) |
| exchange product code, listed contract | contextual | Listed markets | LD-C0062 |
| service | ambiguous | Any | LD-C0051, LD-C0052 (LD-A0020) |
| EMIR client | contextual | EMIR Art. 2(15) | LD-C0004 in a clearing relationship |
| MiFID client | contextual | MiFID II Art. 4(1)(9) | LD-C0004 for an investment service |
| CFTC customer | contextual | US | LD-C0004 toward an FCM |
| commission | ambiguous, blocked | Any | See resolution flags |
| transaction, MiFIR transaction | ambiguous, blocked | Any; MiFIR Art. 26 reporting | See resolution flags |
| execution fee | ambiguous | Any | LD-C0033, LD-C0035, LD-C0036 (LD-A0001) |
| brokerage | ambiguous | UK/EU usage | LD-C0035 or client remuneration (LD-A0004) |
| margin held, margin posted | ambiguous | Any | LD-C0047 versus LD-C0043 (LD-A0027) |
| collateral balance | contextual | Any | Aggregation of LD-C0047, not a separate concept |
| omnibus | ambiguous | Any | See LD-A0028 |
| deadline | contextual | Process steps | LD-C0065 |
| circular, market notice | contextual | Change impact | Source document of LD-C0064, not a concept |
| client clearing model | ambiguous | Any | Decompose (LD-A0030) |
| volume | ambiguous | Any | See LD-A0033 |
| individual | contextual | any | LD-C0075 |
| private client | contextual | when holding a client role, wealth management usage | LD-C0075 |
| establishment | contextual | regulatory usage | LD-C0076 |
| international branch | contextual | LEI usage | LD-C0076 |
| fund | contextual | any | LD-C0077 |
| sub-fund | contextual | umbrella structures | LD-C0077 |
| compartment | contextual | EU fund usage | LD-C0077 |
| authorised person | contextual | any | LD-C0078 |
| instructing party | contextual | any | LD-C0078 |
| order originator | contextual | execution usage, ambiguous | LD-C0078 |
| asset manager | contextual | any | LD-C0079 |
| fund manager | contextual | any | LD-C0079 |
| account manager | contextual | US allocation usage | LD-C0079 |
| beneficial owner | contextual | ambiguous: also the know-your-customer meaning | LD-C0080 |
| underlying client | contextual | omnibus usage | LD-C0080 |
| indirect client | contextual | EMIR usage | LD-C0081 |
| give-up reference | contextual | listed give-up usage | LD-C0082 |
| account code | contextual | any | LD-C0082 |
| mnemonic | contextual | listed markets usage | LD-C0082 |
| ownership group | contextual | any, for the set of entities under one ultimate parent | LD-C0083 |
| corporate family | contextual | sales usage | LD-C0083 |
| affiliate | contextual | CCP rulebook usage, ambiguous | LD-C0083 |
| booking entity | contextual | ambiguous: may mean the entity that records the trade | LD-C0084 |
| provider entity | contextual | any | LD-C0084 |
| affiliate client | contextual | any | LD-C0085 |
| internal client | contextual | ambiguous: may mean another desk of the same entity | LD-C0085 |
| NCM | contextual | listed markets | LD-C0086 |
| trading member without clearing rights | contextual | venue usage | LD-C0086 |
| sponsored member | contextual | CCP usage | LD-C0087 |
| direct client participant | contextual | CCP usage | LD-C0087 |
| MiFID client category | contextual | EU, UK | LD-C0088 |
| client categorisation | contextual | any | LD-C0088 |
| EMIR classification | contextual | EU, UK | LD-C0089 |
| counterparty classification | contextual | any | LD-C0089 |
| internal client account | contextual | clearing usage | LD-C0090 |
| customer account | contextual | US usage, ambiguous with the US account class | LD-C0090 |
| identifier type | contextual | any | LD-C0093 |
| symbology | contextual | market data | LD-C0093 |
| security ID source | contextual | FIX | LD-C0093 |
| segment MIC | contextual | ISO 10383 | LD-C0094 |
| market segment | contextual | — | LD-C0094 |
| trading platform | contextual | venue usage | LD-C0094 |
| spread, combo, complex instrument | contextual | venue usage | LD-C0095 |
| multi-leg instrument | contextual | FIX | LD-C0095 |
| flex, flexible contract, custom series | contextual | venue usage | LD-C0096 |
| underlier | contextual | — | LD-C0097 |
| reference asset | contextual | — | LD-C0097 |
| reference entity | contextual | credit | LD-C0097 |
| expiry rule | contextual | — | LD-C0098 |
| last trading day rule | contextual | — | LD-C0098 |
| roll convention | contextual | OTC usage | LD-C0098 |
| corporate action adjustment | contextual | — | LD-C0099 |
| contract adjustment | contextual | venue usage | LD-C0099 |
| clearing series | contextual | for one series of the clearing contract | LD-C0100 |
| CCP contract | contextual | contextual | LD-C0100 |
| clearing eligibility list | contextual | contextual | LD-C0101 |
| trading hours | contextual | — | LD-C0102 |
| trading phase | contextual | — | LD-C0102 |
| extended hours | contextual | — | LD-C0102 |
| EDSP | contextual | exchange delivery settlement price, final kind | LD-C0103 |
| ancillary service | contextual | Any | LD-C0105 |
| service feature | contextual | product usage | LD-C0105 |
| coverage | contextual | ambiguous: membership, access route or offering | LD-C0106 |
| market coverage | contextual | Any | LD-C0106 |
| client eligibility | contextual | Any | LD-C0107 |
| onboarding criteria | contextual | Any | LD-C0107 |
| membership agreement | contextual | Any | LD-C0108 |
| DEA agreement | contextual | EU | LD-C0108 |
| NCM agreement | contextual | listed markets | LD-C0108 |
| membership application | contextual | Any | LD-C0109 |
| market onboarding | contextual | UC-002 usage | LD-C0109 |
| admission criteria | contextual | CCP and venue usage | LD-C0110 |
| membership requirements | contextual | Any | LD-C0110 |
| participation requirements | contextual | PFMI | LD-C0110 |
| connectivity | contextual | Any | LD-C0111 |
| session, gateway | contextual | venue usage, contextual | LD-C0111 |
| DEA | contextual | EU | LD-C0112 |
| DMA | contextual | ambiguous: also any low-touch electronic flow | LD-C0112 |
| sponsored access | contextual | execution | LD-C0112 |
| naked access | contextual | informal, avoid | LD-C0112 |
| third-party execution | contextual | sponsor usage | LD-C0113 |
| order routing to another broker | contextual | Any | LD-C0113 |
| executing broker of the executing broker | contextual | informal | LD-C0113 |
| NCM | contextual | listed markets | LD-C0114 |
| NCM-GCM relationship | contextual | listed markets | LD-C0114 |
| sponsored clearing | contextual | CCP usage | LD-C0115 |
| direct-client model | contextual | CCP usage | LD-C0115 |
| sponsored | contextual | ambiguous: execution or clearing | LD-C0115 |
| indirect clearing | contextual | any | LD-C0116 |
| parent order | contextual | desk and algorithm usage | LD-C0117 |
| client-facing order | contextual | execution | LD-C0117 |
| slice | contextual | algorithm usage | LD-C0118 |
| venue order, market order | contextual | when sent to a venue; 'market order' is ambiguous with the order type | LD-C0118 |
| street-side order | contextual | US usage | LD-C0118 |
| clearing member pre-execution credit control | contextual | contextual | LD-C0119 |
| fill, market fill, street fill | contextual | venue-facing usage | LD-C0120 |
| exchange trade | contextual | ambiguous | LD-C0120 |
| fill, client fill | contextual | client-facing usage | LD-C0121 |
| execution report | contextual | message, not the event | LD-C0121 |
| block | contextual | venue usage | LD-C0122 |
| negotiated large trade | contextual | any | LD-C0122 |
| off-book trade | contextual | EU venue usage, ambiguous | LD-C0122 |
| EFRP | contextual | any | LD-C0123 |
| EFP, EFS, EOO | contextual | by related-position type | LD-C0123 |
| basis trade | contextual | desk usage, ambiguous | LD-C0123 |
| leg fill | contextual | desk usage | LD-C0124 |
| trade bust, busted trade | contextual | venue usage | LD-C0125 |
| error trade | contextual | venue usage | LD-C0125 |
| cancel and correct | contextual | desk usage | LD-C0125 |
| pre-clearing trade | contextual | any | LD-C0126 |
| alpha trade | contextual | OTC clearing usage | LD-C0126 |
| matched trade | contextual | venue usage | LD-C0126 |
| rounding residual | contextual | any | LD-C0127 |
| average price cash adjustment | contextual | some venues, to verify | LD-C0127 |
| standing instruction, SSI-style allocation | contextual | desk usage, ambiguous with settlement instructions | LD-C0128 |
| default allocation | contextual | any | LD-C0128 |
| allocation, alloc | contextual | desk usage | LD-C0129 |
| booking line | contextual | middle office usage | LD-C0129 |
| third-party broker, executing agent | contextual | desk usage | LD-C0130 |
| sub-broker | contextual | any, ambiguous | LD-C0130 |
| give-up instruction | contextual | listed, giving side | LD-C0131 |
| allocation | contextual | CCP or give-up facility screens, contextual | LD-C0131 |
| alleged give-in | contextual | receiving side, contextual | LD-C0131 |
| give-up at registration | contextual | former working name | LD-C0132 |
| CMTA | contextual | US listed options usage, to verify | LD-C0132 |
| give-up after registration | contextual | former working name | LD-C0133 |
| executing clearing member | contextual | contextual | LD-C0134 |
| claiming member | contextual | listed, contextual | LD-C0135 |
| give-in side | contextual | firm's view, contextual | LD-C0135 |
| carrying broker | contextual | US, contextual | LD-C0135 |
| claim | contextual | listed, contextual | LD-C0136 |
| accept give-in | contextual | contextual | LD-C0136 |
| consent | contextual | OTC clearing, contextual | LD-C0137 |
| limit check or credit check | contextual | OTC, contextual | LD-C0137 |
| clearing broker approval | contextual | contextual | LD-C0137 |
| clearing member credit limit | contextual | contextual | LD-C0138 |
| transfer | contextual | CCP reports, contextual | LD-C0139 |
| claim processed | contextual | contextual | LD-C0139 |
| give-up deadline | contextual | contextual | LD-C0140 |
| claim deadline | contextual | contextual | LD-C0140 |
| request for clearing | contextual | OTC, contextual | LD-C0141 |
| submission | contextual | contextual | LD-C0141 |
| cleared derivatives execution agreement | contextual | contextual | LD-C0142 |
| cleared trade | contextual | ambiguous with the client back-to-back trade | LD-C0143 |
| CCP trade | contextual | contextual | LD-C0143 |
| beta and gamma trades | contextual | OTC clearing, one per side | LD-C0143 |
| member-client trade | contextual | ambiguity register term | LD-C0144 |
| client trade | contextual | OTC client clearing | LD-C0144 |
| mirror trade | contextual | — | LD-C0144 |
| proprietary account | contextual | any | LD-C0145 |
| house origin | contextual | US | LD-C0145 |
| own account | contextual | EU | LD-C0145 |
| omnibus | contextual | ambiguous; see the open question on omnibus, house and client | LD-C0146 |
| customer segregated origin | contextual | US | LD-C0146 |
| OSA, omnibus segregated account | contextual | EU usage | LD-C0146 |
| ISA | contextual | EU usage | LD-C0147 |
| individual client segregation | contextual | EMIR | LD-C0147 |
| indirect clearing account | contextual | EU | LD-C0148 |
| sub-account | contextual | CCP usage, ambiguous | LD-C0149 |
| position-keeping account | contextual | any | LD-C0149 |
| segregation choice | contextual | EU | LD-C0150 |
| account type election | contextual | any | LD-C0150 |
| open position | contextual | listed | LD-C0151 |
| lots | contextual | UK usage, quantity unit | LD-C0151 |
| cleared portfolio | contextual | OTC, ambiguous with Portfolio | LD-C0152 |
| book of cleared swaps | contextual | any | LD-C0152 |
| transfer | contextual | listed, ambiguous with give-up | LD-C0153 |
| position move | contextual | any | LD-C0153 |
| default event | contextual | any, ambiguous | LD-C0154 |
| declaration of default | contextual | CCP rules | LD-C0154 |
| portability | contextual | regulatory, the property of being portable | LD-C0155 |
| transfer of client positions on default | contextual | EMIR | LD-C0155 |
| back-up clearing broker | contextual | any | LD-C0156 |
| transferee clearing member | contextual | CCP rules | LD-C0156 |
| sponsor | contextual | — | LD-C0157 |
| clearing agent | contextual | where the rulebook uses the term, to verify | LD-C0157 |
| position maintenance | contextual | — | LD-C0158 |
| position change | contextual | — | LD-C0158 |
| close-out | contextual | contextual | LD-C0158 |
| margin rates | contextual | contextual, listed derivatives | LD-C0160 |
| margin levels | contextual | contextual, circulars | LD-C0160 |
| risk parameters | contextual | contextual, CCP | LD-C0160 |
| margin cycle | contextual | contextual | LD-C0161 |
| margin calculation | contextual | contextual | LD-C0161 |
| margin component | contextual | any | LD-C0162 |
| margin breakdown | contextual | contextual, statements | LD-C0162 |
| client margin multiplier | contextual | contextual | LD-C0163 |
| house margin | contextual | ambiguous with margin on the house account; avoid | LD-C0163 |
| margin unit | contextual | contextual | LD-C0164 |
| call parameters | contextual | contextual | LD-C0165 |
| margin terms | contextual | contextual, client agreements | LD-C0165 |
| excess | contextual | contextual | LD-C0166 |
| deficit | contextual | contextual, US futures | LD-C0166 |
| margin surplus | contextual | contextual | LD-C0166 |
| haircut | contextual | any | LD-C0167 |
| valuation percentage | contextual | contextual, bilateral documentation | LD-C0167 |
| concentration cap | contextual | any | LD-C0168 |
| collateral request | contextual | contextual | LD-C0169 |
| substitution request | contextual | contextual | LD-C0169 |
| PAI | contextual | OTC clearing | LD-C0170 |
| PAA | contextual | OTC clearing | LD-C0170 |
| interest on margin | contextual | contextual | LD-C0171 |
| cash collateral remuneration | contextual | contextual | LD-C0171 |
| guarantee fund contribution | contextual | contextual, some CCPs | LD-C0172 |
| clearing fund contribution | contextual | contextual, US | LD-C0172 |
| collateral provider | contextual | contextual, in margin | LD-C0173 |
| collateral taker | contextual | contextual, in margin | LD-C0174 |
| secured party | contextual | contextual, legal | LD-C0174 |
| price list | contextual | venue and CCP usage | LD-C0175 |
| tariff | contextual | any | LD-C0175 |
| fee grid | contextual | some venues | LD-C0175 |
| rate card | contextual | sales usage | LD-C0176 |
| fee letter | contextual | contextual, the document | LD-C0176 |
| pricing schedule | contextual | any | LD-C0176 |
| tariff line | contextual | any | LD-C0177 |
| price point | contextual | any | LD-C0177 |
| incentive scheme | contextual | any | LD-C0178 |
| LP programme | contextual | venue usage | LD-C0178 |
| market-making scheme | contextual | MiFID II usage, to verify | LD-C0178 |
| recharge | contextual | any | LD-C0179 |
| exchange and clearing fees | contextual | client statement usage, contextual | LD-C0179 |
| give-up payment | contextual | contextual, executing brokerage paid on the client's behalf | LD-C0179 |
| all-in commission | contextual | contextual | LD-C0180 |
| commission | contextual | ambiguous, blocked | LD-C0180 |
| round-turn rate | contextual | listed usage, contextual | LD-C0180 |
| regulatory fee | contextual | any | LD-C0181 |
| assessment fee | contextual | US usage, to verify | LD-C0181 |
| rebate | contextual | any | LD-C0182 |
| volume rebate | contextual | any | LD-C0182 |
| LP rebate | contextual | venue usage | LD-C0182 |
| credit note | contextual | contextual, the document | LD-C0183 |
| waiver | contextual | contextual | LD-C0183 |
| fee correction | contextual | any | LD-C0183 |
| bill | contextual | any | LD-C0184 |
| monthly statement | contextual | contextual, client usage | LD-C0184 |
| billing agent | contextual | any | LD-C0185 |
| collecting organisation | contextual | repository usage | LD-C0185 |
| volume | contextual | ambiguous | LD-C0186 |
| lots | contextual | listed usage, contextual | LD-C0186 |
| tickets | contextual | OTC usage, contextual | LD-C0186 |
| collateral income | contextual | any | LD-C0187 |
| NII on client cash | contextual | finance usage, contextual | LD-C0187 |
| management basis | contextual | repository usage | LD-C0188 |
| reporting rules | contextual | any | LD-C0188 |
| cost scope | contextual | any | LD-C0189 |
| contribution level | contextual | finance usage, contextual | LD-C0189 |
| regulatory requirement | contextual | generic | LD-C0190 |
| mandate | contextual | US usage, contextual | LD-C0190 |
| mandatory clearing | contextual | contextual | LD-C0191 |
| clearing mandate | contextual | contextual | LD-C0191 |
| clearing requirement | contextual | US usage | LD-C0191 |
| class | contextual | regulatory, contextual | LD-C0192 |
| regulated derivative class | contextual | — | LD-C0192 |
| phase-in | contextual | — | LD-C0193 |
| category 1, 2, 3 | contextual | contextual, EU clearing obligation | LD-C0193 |
| compliance date | contextual | US usage, contextual | LD-C0193 |
| rules and procedures | contextual | contextual | LD-C0194 |
| clearing conditions | contextual | contextual, some CCPs | LD-C0194 |
| exchange rules | contextual | — | LD-C0194 |
| no-action letter | contextual | US, contextual | LD-C0195 |
| forbearance | contextual | contextual | LD-C0195 |
| temporary relief | contextual | — | LD-C0195 |
| equivalence | contextual | EU and UK usage | LD-C0196 |
| substituted compliance | contextual | US usage, contextual | LD-C0196 |
| circular | contextual | contextual | LD-C0197 |
| market notice | contextual | contextual | LD-C0197 |
| member notice | contextual | — | LD-C0197 |
| special executive report | contextual | one exchange group's usage | LD-C0197 |
| consultation paper | contextual | the document | LD-C0198 |
| request for comment | contextual | US usage | LD-C0198 |
| proposed rule | contextual | US usage, contextual | LD-C0198 |
| regulatory approval | contextual | contextual | LD-C0199 |
| self-certification | contextual | US usage | LD-C0199 |
| rule filing | contextual | US usage, contextual | LD-C0199 |
| impact analysis | contextual | — | LD-C0200 |
| regulatory change assessment | contextual | — | LD-C0200 |
| reading | contextual | — | LD-C0201 |
| legal view | contextual | contextual | LD-C0201 |
| industry guidance | contextual | when issued by an association | LD-C0201 |
| FCM | contextual | US, contextual | LD-C0202 |
| DCO | contextual | US, contextual | LD-C0202 |
| licence | contextual | — | LD-C0202 |
| registration | contextual | — | LD-C0202 |
| recognition | contextual | — | LD-C0202 |
| regulator | contextual | — | LD-C0203 |
| competent authority | contextual | EU usage, contextual | LD-C0203 |
| supervisor | contextual | — | LD-C0203 |
| book of record | contextual | when a rule makes the record authoritative | LD-C0205 |
| statement | contextual | broker, bank or CCP | LD-C0205 |
| report | contextual | CCP or venue | LD-C0205 |
| CCP statement | contextual | — | LD-C0206 |
| clearing report | contextual | — | LD-C0206 |
| end-of-day report | contextual | CCP | LD-C0206 |
| break | contextual | — | LD-C0207 |
| mismatch | contextual | — | LD-C0207 |
| unmatched item | contextual | contextual | LD-C0207 |
| difference | contextual | — | LD-C0207 |
| position rec | contextual | — | LD-C0208 |
| open position reconciliation | contextual | — | LD-C0208 |
| case | contextual | — | LD-C0209 |
| ticket | contextual | — | LD-C0209 |
| query | contextual | with a counterparty, contextual | LD-C0209 |
| fail | contextual | — | LD-C0210 |
| failed payment | contextual | — | LD-C0210 |
| failed delivery | contextual | — | LD-C0210 |
| late payment | contextual | contextual | LD-C0210 |
| net cash call | contextual | — | LD-C0211 |
| net settlement amount | contextual | — | LD-C0211 |
| daily settlement | contextual | CCP, contextual | LD-C0211 |
| payment order | contextual | — | LD-C0212 |
| SSI | contextual | standing settlement instructions, contextual: the standing details, not the instruction | LD-C0212 |
| direct debit | contextual | CCP | LD-C0212 |
| settlement bank account | contextual | — | LD-C0213 |
| nostro | contextual | contextual, firm's own cash account | LD-C0213 |
| SSI account | contextual | — | LD-C0213 |
| payment deadline | contextual | — | LD-C0214 |
| settlement cut-off | contextual | — | LD-C0214 |
| client cut-off | contextual | — | LD-C0215 |
| internal deadline | contextual | — | LD-C0215 |
| expiration | contextual | — | LD-C0216 |
| maturity | contextual | OTC, contextual | LD-C0216 |
| exercise notice | contextual | the instruction, contextual | LD-C0217 |
| exercise notice | contextual | — | LD-C0218 |
| abandonment instruction | contextual | — | LD-C0218 |
| contrary instruction | contextual | — | LD-C0218 |
| assignment notice | contextual | — | LD-C0219 |
| delivery | contextual | physical, contextual | LD-C0220 |
| notice of intention | contextual | — | LD-C0221 |
| tender | contextual | contextual | LD-C0221 |
| amendment | contextual | — | LD-C0222 |
| unwind | contextual | OTC | LD-C0222 |
| termination | contextual | OTC | LD-C0222 |
| trade correction | contextual | contextual | LD-C0222 |

## Required context

Agents must obtain or state these before answering; a missing item leads to a clarification, not a default.

| Concept | Required context |
|---|---|
| LD-C0015 Business Date | Date role, business calendar, time zone |
| LD-C0018 Trade | Clearing tier and counterparty view (LD-A0025) |
| LD-C0026 Position | Account (CCP or internal), instrument, clearing service, gross or net basis, quantity kind, as-of business date and cycle, asserting source |
| LD-C0043 Margin Requirement | Margin provider and taker (tier), account, component, methodology version, run type, as-of time, currency basis |
| LD-C0039, LD-C0041, LD-C0042, LD-C0074 | Observing entity, attribution target, management basis, period, currency, gross or net of pass-through, service mix; for LD-C0041 also order handling channel (sponsor decision 2026-11-01) |
| LD-C0068 Regulatory Classification | Regime, asset class where relevant, basis, effective period, evidence, as-of and record time |
| LD-C0075 Natural Person | Personal data rules apply: an agent must not expose personal identifiers; only the role and the party type are needed for most questions. |
| LD-C0076 Branch | Which legal entity it belongs to, the jurisdiction in which it is established, and whether a role or membership is held by the legal entity acting through the branch. |
| LD-C0077 Investment Fund | Whether the question concerns the umbrella or a sub-fund, and which investment manager acts for it in which period. |
| LD-C0078 Authorised Representative | Which client, which provider, which kinds of instruction and which period the authority covers. |
| LD-C0079 Investment Manager | Which funds it manages for which period; whether it is also a client in its own name. |
| LD-C0080 Economic Beneficiary | Account concerned, source of the assertion, period; whether the holder discloses beneficiaries at all. |
| LD-C0081 Indirect Client | Clearing service, the client that provides its clearing, the regime and the account structure chosen. |
| LD-C0082 Account Identifier | The identifier scheme it belongs to (the issuer's scheme), the issuing party, use and period. |
| LD-C0083 Parent Entity | Consolidation basis, direct or ultimate, source (public LEI relationship data or internal), effective period. |
| LD-C0084 Contracting Entity | Which service and which period; a client may contract with several of the firm's entities for different services. |
| LD-C0085 Intra-group Client | Ownership basis and period; observing contracting entity; regime and CCP rules on affiliates. |
| LD-C0086 Non-Clearing Member | Clearing service and the CCP's rules: whether the status is formally recognised there or the firm is simply a client. |
| LD-C0087 Sponsored Clearing Participant | CCP, clearing service, sponsor, period; the split of obligations under that CCP's rules. |
| LD-C0088 Client Regulatory Category | Regime, contracting entity, service, basis and period. |
| LD-C0089 Counterparty Regulatory Status | Regime, asset class where relevant, basis, source, as-of date and period. |
| LD-C0090 Client Account | Maintaining party, holder, function, status and period; for clearing, the mapped CCP account per clearing service. |
| LD-C0091 Market Operator | Venue or venues operated, period. |
| LD-C0092 Settlement or Custody Agent | Account holder, account, currency or asset, period. |
| LD-C0093 Identifier Scheme | Which scheme a value belongs to and its uniqueness scope; for per-day schemes, the business date and issuing venue or CCP. |
| LD-C0094 Trading Venue Segment | Whether a record or rule refers to the whole venue (operating level) or to one segment. |
| LD-C0095 Listed Strategy | Whether the strategy was defined by the venue or by a participant, and whether the question concerns the strategy or its legs. |
| LD-C0096 Flexible Series | That the series may appear intraday and be absent from start-of-day reference files. |
| LD-C0097 Underlying | Which underlying source applies (index version, benchmark, deliverable basket) at the relevant date. |
| LD-C0098 Key-Date Rule | Which calendar version the rule uses; a calendar change can move key dates without changing the rule. |
| LD-C0099 Contract Adjustment | Effective business date, the series affected and the adjusted terms; old and new series identifiers. |
| LD-C0100 Clearing Contract | The clearing service and date; whether the venue-to-CCP mapping is one-to-one. |
| LD-C0101 Clearing Eligibility Schedule | Clearing service, version and effective date; for OTC, the trade-term ranges. |
| LD-C0102 Trading Session | Venue time zone and daylight-saving rule; which contracts the session applies to. |
| LD-C0103 Settlement Price | Publisher (venue or CCP), kind (daily or final), business date and whether it is provisional or corrected. |
| LD-C0104 Processing Window | Clearing service or payment system, business date, time zone, calendar version. |
| LD-C0105 Service Component | Which offering it belongs to; whether it is bundled or priced separately. |
| LD-C0106 Offering Coverage Line | Offering, venue or clearing service, product scope, as-of date (default: clearing date of the relevant CCP) and the status of the arrangement it relies on. |
| LD-C0107 Offering Eligibility Criterion | Which offering and coverage line; the client and its regulatory classification as of the date asked. |
| LD-C0108 Access Agreement | Parties, governing rules or law, version and effective period; which arrangements it documents. |
| LD-C0109 Access Onboarding | Holder, target venue or clearing service, access model and category. |
| LD-C0110 Access Requirement | Issuer, access model and category it applies to, version and effective period. |
| LD-C0111 Connectivity Route | Venue or CCP, holder, purpose (trading, clearing, both). |
| LD-C0112 Direct Electronic Access Arrangement | Venue, member granting access, client, form (direct market access or sponsored access), status and effective period. |
| LD-C0113 Third-Party Execution Arrangement | Venue, intermediary, the firm's role toward its own client, status and effective period. |
| LD-C0114 Non-Clearing Member Arrangement | CCP and clearing service, venue, intermediary, status and effective period. |
| LD-C0115 Sponsored Clearing Arrangement | CCP and clearing service, sponsor, participant, status, effective period; which CCP model applies. |
| LD-C0116 Indirect Clearing Arrangement | Regime, clearing service, each link in the chain, account option, status and effective period. |
| LD-C0117 Client Order | Who gave the order (client or authorised representative) and to which executing broker; the handling channel and its time; under direct market access the client order and the venue order may be the same order. |
| LD-C0118 Child Order | The parent order and the handling party; whether it went to a venue or to another broker; channel changes over time. |
| LD-C0119 Pre-trade Control Check | Who set the limit (executing broker, venue member, clearing member, venue), the limit kind and the regime that requires it. |
| LD-C0120 Venue Execution | Venue, entering member, venue identifiers (unique only per venue and session), execution timestamp and the trade date assigned by the venue calendar. |
| LD-C0121 Client Execution | Client order; underlying venue executions; the order handling channel of the client order at the time of each underlying venue execution; the broker's trading capacity. |
| LD-C0122 Block Trade | Venue, contract and the venue's block rules in force at the trade date; trading capacity of the arranging broker. |
| LD-C0123 Exchange for Related Position | Venue, contract, related-position type and the venue's rules in force at the trade date; who holds the related leg. |
| LD-C0124 Strategy Leg Execution | The strategy and its legs as defined by the venue; whether the firm allocates per leg or per strategy. |
| LD-C0125 Execution Correction | Who initiated it (venue, member, broker), on which side (venue-facing or client-facing), and its effect on allocations and give-ups already made. |
| LD-C0126 Executed Trade | Counterparty view (member side or client side) and the trading capacity of the broker; on listed markets the pre-clearing tier is often very short-lived. |
| LD-C0127 Average Price Residual | Average price group, averaging performer, currency and who bears it; no treatment is approved. |
| LD-C0128 Standing Allocation Instruction | Scope, effective period and who may override it; the version in force at the execution time. |
| LD-C0129 Allocation Line | Source execution or average price group, target account and its clearing member, route and status, and the version of the instruction applied. |
| LD-C0130 Third-party Executing Member | Venue, membership category and effective period; never inferred from execution activity. |
| LD-C0131 Give-up Line | Clearing service and clearing date; which side the firm is on (giving or receiving); whether the status comes from the CCP record or an internal record. |
| LD-C0132 Give-up Designated in Advance | Clearing service and its rules on designation; whether the designation was accepted before registration. |
| LD-C0133 Give-up after First Registration | Clearing service, clearing date, deadline and its consequence; who carries margin while the line is pending. |
| LD-C0134 Giving Clearing Member | Clearing service; whether the give-up happens at or after registration; whether the executing broker is itself a clearing member. |
| LD-C0135 Receiving Clearing Member | Clearing service; account and give-up reference named; whether the clearing broker is itself a member of the service. |
| LD-C0136 Take-up | Clearing service, deadline, whether the facility is the CCP's own or a third party's, partial take-up allowed or not. |
| LD-C0137 Submission Acceptance | Clearing service, regime and its acceptance-timing rules, whether the check was pre-execution or post-execution. |
| LD-C0138 Clearing Limit | Who set the limit, for which scope and basis, version in force at the time of the trade. |
| LD-C0139 Give-up Registration | Clearing service; clearing date; CCP record as the authoritative source. |
| LD-C0140 Take-up Deadline | Clearing service, rulebook version, clearing date and the CCP's time zone. |
| LD-C0141 Clearing Submission | Clearing service; submitting party; designated clearing members; regime acceptance-timing rules. No parent: there is no broader instruction concept in the catalogue that it is a kind of. |
| LD-C0142 Execution Agreement for Cleared Trades | Regime; product scope; version of any industry standard used. |
| LD-C0143 CCP-facing Trade | Clearing service, CCP account and tier; the legal model of the client relationship for a client account. |
| LD-C0144 Client Back-to-Back Trade | Legal model of the client clearing agreement for that service and regime; tier (member to client, or client to indirect client). |
| LD-C0145 House Account | Clearing service; whether affiliates are cleared here or as clients. |
| LD-C0146 Client Omnibus Account | Clearing service, regime, net or gross basis, and the internal accounts mapped to it as of the clearing date. |
| LD-C0147 Individually Segregated Client Account | Clearing service, regime, the client's election and its effective date; where any excess collateral is held. |
| LD-C0148 Indirect Client Account | Clearing service, regime, the client that provides indirect clearing, the basic or gross form. |
| LD-C0149 CCP Position Account | Clearing service and the CCP's account structure as of the clearing date. |
| LD-C0150 Segregation Election | Client, clearing broker, clearing service, regime and effective date. |
| LD-C0151 Listed Position | Account and its level, clearing contract series (not only the venue instrument), gross or net basis, clearing date and cycle, source. |
| LD-C0152 Cleared OTC Position | Account, clearing service, tier, clearing date, source, and which measure is asked for (count, notional, sensitivity). |
| LD-C0153 Position Transfer | Clearing service, source and target accounts and members, trigger, effective clearing date; collateral moves separately if at all. |
| LD-C0154 Clearing Member Default | Clearing service, declaring CCP, date and time of declaration under its rules. |
| LD-C0155 Porting | Clearing service, account kind, segregation election, back-up member, legal form of collateral; whether it actually succeeds is a Legal and CCP fact, never inferred from the account kind. |
| LD-C0156 Back-up Clearing Member | Client, clearing service, whether pre-agreed, effective period. |
| LD-C0157 Sponsoring Clearing Member | Clearing service and the obligations its rules assign to the sponsor. |
| LD-C0158 Position Adjustment | CCP account and its gross or net basis, series, clearing date, applicable cut-off. |
| LD-C0159 Client Default | Client clearing agreement and legal model, regime, date of declaration. |
| LD-C0160 Margin Parameter Set | Clearing service, product scope, effective date and version; which methodology version it belongs to. |
| LD-C0161 Margin Run | Margin taker, run type, as-of time, time zone, methodology and parameter versions. |
| LD-C0162 Margin Requirement Component | Tier, account, run, currency basis, and the CCP's native component name. |
| LD-C0163 Client Margin Uplift | Client, product scope, clearing service, effective date and the CCP figure it is applied to. |
| LD-C0164 Margin Portfolio | Margin taker, clearing services and accounts covered, methodology version, as-of time. |
| LD-C0165 Margin Call Terms | Tier, arrangement or rulebook version, clearing service, client or client group. |
| LD-C0166 Margin Excess or Shortfall | Tier, account, as-of time, currency basis, where the excess is held. |
| LD-C0167 Collateral Haircut | Schedule version, asset, tier, currency of the requirement. |
| LD-C0168 Concentration Limit | Schedule version, tier, account, limit basis. |
| LD-C0169 Collateral Instruction | Arrangement, provider, taker, asset and quantity, requested date, status. |
| LD-C0170 Price Alignment Amount | Tier, clearing service, account, variation margin treatment, currency and period. |
| LD-C0171 Cash Collateral Interest | Tier, arrangement, currency, accrual period, whether the amount is accrued or paid. |
| LD-C0172 Default Fund Contribution | Clearing service, clearing member, recalibration date, currency. |
| LD-C0173 Margin Provider | Account, clearing service, period. |
| LD-C0174 Margin Taker | Account, clearing service, period. |
| LD-C0175 Published Fee Schedule | Issuer, scope (venue or segment, clearing service, contract), version and effective period; the date role used to pick the version. |
| LD-C0176 Client Pricing Terms | Client or commercial group, service offering, effective period and version; pricing form. |
| LD-C0177 Fee Rate | Schedule version, scope qualifiers, charge basis, currency, tier. |
| LD-C0178 Fee Incentive Programme | Issuer, participant registration, period, conditions; whether benefits are passed on to clients is a firm matter. |
| LD-C0179 Pass-through Charge | The charge passed on, its creditor, the recharge treatment, and the gross or net rule of the reporting basis. |
| LD-C0180 Bundled Execution and Clearing Fee | The service offering, the split rule, the charge basis. |
| LD-C0181 Regulatory Transaction Fee | Regime, levying body, rule and version, collector. |
| LD-C0182 Fee Rebate | Programme or terms, period, direction (received or granted), and whether it is netted against the fees it rewards. |
| LD-C0183 Fee Adjustment | Original charge, reason, approver, effective date, and whether the adjustment is in the same period as the original. |
| LD-C0184 Fee Invoice | Issuer, debtor, billing period, currency, due date; the creditor of each line. |
| LD-C0185 Fee Collector | Which creditor it collects for, and under which rule or agreement. |
| LD-C0186 Activity Volume | Unit, counting basis, stage, source, scope, period. |
| LD-C0187 Collateral Revenue | Observing entity, period, currency, streams included, and the decision on inclusion in clearing revenue. |
| LD-C0188 Management Reporting Basis | Version and owner; an answer always names the basis it uses. |
| LD-C0189 Cost Perimeter | Version, owner, approval date; categories included. |
| LD-C0190 Regulatory Obligation | Regime, holder classification or role, product scope, conditions and exemptions, application and phase-in dates, defining provisions and their versions. Applicability to a named party is never stated from the public layer. |
| LD-C0191 Clearing Obligation | Regime, both counterparties' classifications and their dates, product class with trade-term ranges, trade date and application date, exemptions claimed, CCP status (authorised or recognised). |
| LD-C0192 Regulated Product Class | Regime, defining provision version, trade-term ranges, as-of date. |
| LD-C0193 Phase-in Step | Regime, the subset it applies to, application date (date role), end of transition, defining provision version. |
| LD-C0194 Rulebook | Issuer, version and effective period, which part (rules, procedures, conditions), which clearing services or venue segments it covers. |
| LD-C0195 Regulatory Relief | Relieved provision and version, beneficiaries (named or by class), conditions, start and expiry dates, issuer and its binding force. |
| LD-C0196 Equivalence Decision | Deciding regime and authority, assessed regime, purpose, conditions, effective period and expiry. |
| LD-C0197 Change Notice | Issuer, reference, publication date and time zone, version (a notice can be corrected), language, which rule changes it announces. |
| LD-C0198 Consultation | Issuer, proposed provisions, closing date, status, link to any later adoption. |
| LD-C0199 Rule Change Approval | Infrastructure, supervisor, filing or approval route, outcome, decision date, conditions. |
| LD-C0200 Change Impact Assessment | The rule change and its status, as-of date, assessing and signing-off roles, the 'public-layer reading, not legal advice' label for agent drafts. |
| LD-C0201 Regulatory Interpretation | Provision version read, author kind, basis, confidence, sign-off status and roles; firm readings are internal. |
| LD-C0202 Regulatory Authorisation | Regime, granting authority, holder entity, scope (activity, clearing services, asset classes), period, standing, public register consulted and its as-of date. |
| LD-C0203 Regulatory Authority | Jurisdiction and remit, which regime, which entities it supervises. |
| LD-C0204 Regulatory Reporting Role | Regime, report type, execution or trade. |
| LD-C0205 Source Record | The source, its record time and version, and whether a rule makes it authoritative for the question asked. |
| LD-C0206 CCP Report | Clearing service, CCP accounts covered, clearing date and cycle, report version (CCPs reissue corrected reports). |
| LD-C0207 Reconciliation Break | Reconciliation type, business date by role and cycle, the sources compared, tolerance applied. |
| LD-C0208 Position Reconciliation | CCP account or internal account, series, gross or net basis, clearing date and cycle, tier. |
| LD-C0209 Exception Case | Owner role, priority scheme, deadline, handling state source. |
| LD-C0210 Settlement Fail | Obligation, its settlement deadline and calendar, the source asserting non-settlement, tier. |
| LD-C0211 Netted Settlement Obligation | Parties and tier, currency, cycle, settlement route, list of underlying obligations. |
| LD-C0212 Payment Instruction | Payer, payee, settlement account, currency, value date, settlement route. |
| LD-C0213 Settlement Account | Holder, maintaining institution, currency or asset, service it settles. |
| LD-C0214 Settlement Deadline | Calendar, time zone, currency, cycle, the authority that sets it, the consequence. |
| LD-C0215 Firm Cut-off | Which market cut-off it protects, who it binds, calendar and time zone, consequence. |
| LD-C0216 Expiry | Series, clearing service, expiry date by role and calendar. |
| LD-C0217 Exercise | Series, style (American, European), CCP rule on automatic exercise and threshold, tier. |
| LD-C0218 Exercise Instruction | Holder and tier, series, quantity, applicable market and firm cut-offs. |
| LD-C0219 Assignment | Tier, series, the CCP method and the member's method. |
| LD-C0220 Final Settlement | Series, settlement method, final settlement price source, tier. |
| LD-C0221 Delivery Notice | Contract, notice period dates by role (first notice day), tier. |
| LD-C0222 Trade Amendment | Clearing tier of the trade, whether a successor trade is created, which source records the change. |

## Usage notes on existing concepts

Notes clarify use; they do not change the meanings in the catalogue. Review numbers in brackets.

| Concept | Note |
|---|---|
| LD-C0002 Legal Entity | Identified by LEI (ISO 17442); certain international branches can also hold an LEI (to verify). An LEI never identifies an account, desk or commercial group, and public parent data describe accounting consolidation, not a commercial group. Holder of entity-level regulatory classifications. [06, 07] |
| LD-C0003 Party Role | Read as the role assignment (party-in-role); there is no separate role-assignment concept. Regulatory relationship statuses attach here. Alignment to verify: FIBO party-in-role pattern, CDM party role. [08, 06] |
| LD-C0004 Client | Sponsor definition unchanged. Linked to a Service Offering through LD-R0081. Client segment is a Participants taxonomy axis. [05, 06] |
| LD-C0006 Executing Broker | The client-facing service role; not necessarily the Trading Venue Member, the regulatory executing entity or the giving clearing member. Third-party execution through another venue member is in scope (sponsor decision 2026-11-01); memberships are never inferred. [01] |
| LD-C0007 Clearing Member | Membership is per clearing service. A non-clearing member is a venue member without this role. FCM is a US registration, not this role. [02, 03] |
| LD-C0008 Central Counterparty | Exercised through one or more clearing services (LD-R0025). Authorisation (EMIR Art. 14, extension per service Art. 15), recognition of third-country CCPs (Art. 25) and QCCP status (CRR Art. 4(1)(88)) are time-bounded Regulatory Classifications, to verify. [02, 06] |
| LD-C0009 Trading Venue | Identify by ISO 10383 MIC; operating MIC for the venue, segment MIC for a segment (to verify per use). Venue type (regulated market, MTF, OTF; US DCM, SEF) is a Regulatory Classification. [01, 05, 06] |
| LD-C0010 Account | Has identifiers per maintaining party, a lifecycle status and an effective period. A give-up reference is an identifier pointing to the receiving member's account, not an account. Regulatory qualifications (for example active-account status) are time-bounded classifications. [07, 06] |
| LD-C0011 Segregation Model | Public instances, not subclasses: EMIR omnibus and individual client segregation (Art. 39); indirect-clearing account structures (Delegated Regulations (EU) 2017/2154 for listed and 2017/2155 for OTC); US futures-customer segregation, cleared-swaps LSOC (17 CFR Part 22) and foreign-futures secured amount (Part 30); paragraphs to verify. State the level (CCP or member books). Legal protection is a Legal conclusion. [02, 03, 04, 06] |
| LD-C0012 Agreement | The client clearing legal model belongs to LD-C0056, not to the CCP or the segregation model. [06, 03] |
| LD-C0013 Product Family | Label changed from "Product" on 2026-11-01; meaning unchanged. OTC classification can align with the ISDA OTC taxonomy, CFI (ISO 10962) and UPI (ISO 4914), to verify. [03, 05, 07] |
| LD-C0014 Instrument | An OTC derivative has an Instrument only where a standard instrument identifier is assigned; trades with the same identifier can still differ in rate and notional, so the Trade carries the full terms. Listed strategies are instruments with legs. [01, 03, 07] |
| LD-C0016 Order | Distinguish client-facing and venue-facing orders; care or algorithmic handling turns one client order into several venue orders. Alignment to verify: FIX order messages and status vocabulary. [01] |
| LD-C0017 Execution | Formed by matching on a venue or by registration of a privately negotiated trade under venue rules (execution method, a taxonomy axis). A broker's venue-facing and client-facing executions are separate and need not be one-to-one. Busts and corrections are lifecycle events referencing the original. [01] |
| LD-C0018 Trade | One pair of counterparties per trade; clearing, compression and porting create successor trades linked by LD-R0034, never mutating the predecessor. How many trades one execution yields depends on the clearing legal model, allocation and averaging: record lineage, not counts. A bespoke OTC trade carries its own economic terms. UTIs are per regime. [01, 03, 06] |
| LD-C0020 Allocation | Allocation to an account carried by another clearing member initiates a give-up (LD-R0045); otherwise it is internal. Averaging groups and allocation distributes; they are chained but distinct. [01] |
| LD-C0021 Average Price Group | Qualifier "averaging performed by": venue or CCP facility, or broker; both are in scope (sponsor decision 2026-11-01). Rounding residuals: proposed as separately identifiable amounts, pending Finance and Operations (open question). [01] |
| LD-C0022 Give-up / Take-up Process | Listed derivatives. Qualifier "attribution timing": at registration (member designated at trade time) or after registration to the executing member. Both directions (give-up out, give-in) are in scope (sponsor decision 2026-11-01). OTC trades reach a CCP by clearing submission (backlog). [01, 02, 03] |
| LD-C0023 Clearing Acceptance | Contextual alias "registration". Rejection is an outcome value, not a separate concept. [02, 08] |
| LD-C0024 Novation | Generic legal concept: one possible mechanism of CCP interposition, and also used for bilateral step-in and step-out outside clearing. Never infer novation from "cleared" or "ported". [02, 03, 06] |
| LD-C0025 Lifecycle Event | Carries occurrence time, effective time and recording time, plus business dates by role. Corrections and cancellations reference the original; nothing is deleted. Event kinds are a taxonomy facet. [07, 03] |
| LD-C0028 Settlement Obligation | Purpose facet includes price alignment (never part of VM) and cash or physical settlement. [04, 02] |
| LD-C0030 Operational Exception | Type State kept. Exceptions are usually handled as cases with owner, priority and lifecycle; the case is a record of handling the exception. A break or a rejected give-up may raise one but is not one (LD-A0034). [07] |
| LD-C0031 Fee Charge | Facets: amount certainty (estimated, final) and billing stage (accrued, invoiced, disputed, adjusted, settled, written off). Proposed definitional cardinality: exactly one debtor and one creditor. [05, 08] |
| LD-C0032 Fee Schedule | Generic parent of public venue or CCP tariffs and negotiated client terms, distinguished by issuer and scope; versioned; a Rule Change can change it. [05] |
| LD-C0033 Client Execution Fee | State the charge basis (per contract side, round turn, allocation, ticket, notional) and grain. An all-in rate must be decomposed before comparison with LD-C0036 or LD-C0037. [01] |
| LD-C0035 Executing Broker Brokerage Charge | Viewpoint matters: received as executing broker, paid and recharged as clearing broker; debtor, payer and recharge explicit. Label unchanged. [01, 05] |
| LD-C0036 Exchange Fee Charge | Creditor is the venue operator; record the collector separately; service-nature facet mandatory. [05, 02] |
| LD-C0037 CCP Fee Charge | Distinct from default-fund contributions and from interest on cash collateral; charges for holding non-cash collateral are CCP fee charges with service nature "collateral". [04, 05] |
| LD-C0040 Cost | Cost-category facet: non-recharged venue and CCP fees, third-party brokerage, third-party clearing, connectivity and market data, funding and collateral, allocated shared cost. [05] |
| LD-C0042 Clearing Revenue | Inclusion of collateral income (interest on client cash, price alignment pass-through) is undecided and never implicit. [04, 05] |
| LD-C0044 Initial Margin Requirement | A member–client IM derived from the CCP figure is still IM at the member–client tier. US futures "initial" and "maintenance" are two call-trigger levels of one requirement. [04] |
| LD-C0045 Variation Margin Requirement | Price alignment is a separate flow. Premium-style options carry no VM; futures-style options do. [04, 03] |
| LD-C0046 Margin Call | A return of excess on request is a Collateral Movement, not a negative call; VM paid out by a CCP is a payment, not a call. [04] |
| LD-C0048 Collateral Asset | Cash in a given currency is a collateral asset. Eligibility holds only against a version of a Collateral Eligibility Schedule (LD-R0072). [04] |
| LD-C0128 Standing Allocation Instruction | Depends on the proposed meaning change to Allocation Instruction, awaiting the sponsor's decision. |
| LD-C0140 Take-up Deadline | Depends on the proposed meaning change to Cut-off, awaiting the sponsor's decision. |
| LD-C0214 Settlement Deadline | Depends on the proposed meaning change to Cut-off, awaiting the sponsor's decision. |
| LD-C0215 Firm Cut-off | Depends on the proposed meaning change to Cut-off, awaiting the sponsor's decision. |

## Priority and alignment

English names are the only labels (French labels removed by sponsor decision, 2026-11-01). Priority is given for concepts added by the 2026-11 review.

| Concept | Priority | Source reviews | Standard alignment (to verify) |
|---|---|---|---|
| LD-C0001 Party | Phase 1 | — | FIBO party concepts |
| LD-C0002 Legal Entity | Phase 1 | — | ISO 17442 LEI |
| LD-C0003 Party Role | Phase 1 | — | FIBO party-in-role; CDM party role |
| LD-C0004 Client | Phase 1 | — | EMIR Art. 2(15); MiFID II Art. 4(1)(9) |
| LD-C0005 Broker | Phase 1 | — | — |
| LD-C0006 Executing Broker | Phase 1 | — | — |
| LD-C0007 Clearing Member | Phase 1 | — | CCP rulebooks |
| LD-C0008 Central Counterparty | Phase 1 | — | EMIR Art. 2(1) |
| LD-C0009 Trading Venue | Phase 1 | — | ISO 10383 MIC |
| LD-C0010 Account | Phase 1 | — | — |
| LD-C0011 Segregation Model | Phase 1 | — | EMIR Art. 39 |
| LD-C0012 Agreement | Phase 1 | — | — |
| LD-C0013 Product Family | Phase 1 | — | ISO 10962 CFI; ISO 4914 UPI; ISDA OTC taxonomy |
| LD-C0014 Instrument | Phase 1 | — | ISO 6166 ISIN |
| LD-C0015 Business Date | Phase 1 | — | — |
| LD-C0016 Order | Phase 1 | — | FIX order messages |
| LD-C0017 Execution | Phase 1 | — | FIX execution report |
| LD-C0018 Trade | Phase 1 | — | CDM trade; ISO 23897 UTI |
| LD-C0019 Transaction | Phase 1 | — | — |
| LD-C0020 Allocation | Phase 1 | — | — |
| LD-C0021 Average Price Group | Phase 1 | — | — |
| LD-C0022 Give-up / Take-up Process | Phase 1 | — | — |
| LD-C0023 Clearing Acceptance | Phase 1 | — | — |
| LD-C0024 Novation | Phase 1 | — | — |
| LD-C0025 Lifecycle Event | Phase 1 | — | CDM business events |
| LD-C0026 Position | Phase 1 | — | — |
| LD-C0027 Portfolio | Phase 1 | — | — |
| LD-C0028 Settlement Obligation | Phase 1 | — | — |
| LD-C0029 Cash Movement | Phase 1 | — | — |
| LD-C0030 Operational Exception | Phase 1 | — | — |
| LD-C0031 Fee Charge | Phase 1 | — | — |
| LD-C0032 Fee Schedule | Phase 1 | — | — |
| LD-C0033 Client Execution Fee | Phase 1 | — | — |
| LD-C0034 Client Clearing Fee | Phase 1 | — | — |
| LD-C0035 Executing Broker Brokerage Charge | Phase 1 | — | — |
| LD-C0036 Exchange Fee Charge | Phase 1 | — | — |
| LD-C0037 CCP Fee Charge | Phase 1 | — | — |
| LD-C0038 Commission | Phase 1 | — | — |
| LD-C0039 Revenue | Phase 1 | — | — |
| LD-C0040 Cost | Phase 1 | — | — |
| LD-C0041 Execution Revenue | Phase 1 | — | — |
| LD-C0042 Clearing Revenue | Phase 1 | — | — |
| LD-C0043 Margin Requirement | Phase 1 | — | PFMI Principle 6 |
| LD-C0044 Initial Margin Requirement | Phase 1 | — | EMIR Art. 41 |
| LD-C0045 Variation Margin Requirement | Phase 1 | — | — |
| LD-C0046 Margin Call | Phase 1 | — | — |
| LD-C0047 Collateral | Phase 1 | — | Directive 2002/47/EC |
| LD-C0048 Collateral Asset | Phase 1 | — | — |
| LD-C0049 Collateral Movement | Phase 1 | — | — |
| LD-C0050 Reconciliation | Phase 1 | — | — |
| LD-C0051 Clearing Service | P1 | 02, 03, 04, 05, 06, 07, 08 | CCP rulebooks; EMIR Art. 14 and 15 (authorisation and its extension) |
| LD-C0052 Service Offering | P1 | 05, 08 | FIBO products and services |
| LD-C0053 Clearing Member Acceptance | P1 | 01, 02, 03, 05, 08 | FIXML allocation and claim flows; FpML clearing status; MiFIR Art. 29(2) and Delegated Regulation (EU) 2017/582; CFTC 1.73 and 1.74 |
| LD-C0054 CCP Interposition | P1 | 02, 03, 06, 08 | PFMI Principle 1; CDM and FpML clearing events |
| LD-C0055 Give-up Agreement | P1 | 01, 02, 08 | FIA International Uniform Brokerage Execution Services ("Give-Up") Agreement; a revised FIA standard was in public comment in 2026, version to verify |
| LD-C0056 Client Clearing Agreement | P1 | 03, 02, 06, 08 | ISDA/FIA client cleared OTC derivatives addendum; FCM customer agreements (titles to verify) |
| LD-C0057 Clearing Broker | P1 | 02, 05, 01, 08 | — (FCM is a contextual US alias) |
| LD-C0058 Trading Venue Member | P1 | 01 | MiFID II "member or participant" (Art. 53 for regulated markets); FIX party roles |
| LD-C0059 Market Access Arrangement | P1 | 05, 02, 03, 06, 01 | EMIR Art. 4(3); MiFIR Art. 30; Delegated Regulations (EU) 2017/2154 and 2017/2155; MiFID II Art. 4(1)(41); PFMI Principle 19 |
| LD-C0060 Allocation Instruction | P1 | 01, 02 | FIX allocation instruction and allocation report messages; CFTC 1.35 bunched orders |
| LD-C0061 Order Handling Channel | P1 (sponsor decision 2026-11-01) | 01, 05 | MiFID II Art. 4(1)(39), 4(1)(41), 17(5); Delegated Regulation (EU) 2017/589; FIX handling-instruction fields |
| LD-C0062 Contract Specification | P1 | 07, 08, 01, 05 | FIX security definition; venue contract specifications |
| LD-C0063 Rule Provision | P1 | 06, 05, 08, 02 | ELI for EU acts |
| LD-C0064 Rule Change | P1 | 06, 08, 02, 05 | CFTC Part 40 rule submissions (instances) |
| LD-C0065 Cut-off | P1 | 07, 08 | CCP and venue deadlines (instances) |
| LD-C0066 Business Calendar | P1 | 07 | Venue, CCP and payment-system calendars (instances) |
| LD-C0067 Regulatory Regime | P1 | 06, 05, 08 | ISO 3166 for jurisdictions |
| LD-C0068 Regulatory Classification | P1 | 06 | EMIR Art. 2(8) and (9), 10, 25; CRR Art. 4(1)(88) |
| LD-C0069 CCP Account | P1 | 02, 07, 04 | EMIR Art. 39; CFTC customer account classes |
| LD-C0070 Margin Methodology | P1 | 04, 05 | PFMI Principle 6; EMIR Art. 41; Delegated Regulation (EU) 153/2013; CFTC 39.13 |
| LD-C0071 Collateral Arrangement | P1 | 04, 08 | Directive 2002/47/EC; MiFID II Art. 16(10); ISDA credit support documentation as bilateral analogue; CDM collateral |
| LD-C0072 Collateral Eligibility Schedule | P1 | 04 | EMIR Art. 46; Delegated Regulation (EU) 153/2013 annexes; CDM eligible collateral |
| LD-C0073 Commercial Group | P1 | 05, 06 | Contrast with public legal-entity relationship data |
| LD-C0074 Contribution | P1 (management revenue priority) | 05, 04, 06 | — |
| LD-C0075 Natural Person | — | 2026-11 domain review | MiFIR transaction reporting identifiers for natural persons (to verify); FIBO natural person (to verify) |
| LD-C0076 Branch | — | 2026-11 domain review | LEI for international branches (ISO 17442 data, to verify) |
| LD-C0077 Investment Fund | — | 2026-11 domain review | LEI fund relationships in GLEIF data (umbrella and fund manager links, to verify) |
| LD-C0078 Authorised Representative | — | 2026-11 domain review | FIX party roles (to verify) |
| LD-C0079 Investment Manager | — | 2026-11 domain review | CFTC rules on post-trade allocation of bunched orders by eligible account managers (to verify) |
| LD-C0081 Indirect Client | — | 2026-11 domain review | EMIR access to clearing and Delegated Regulations (EU) 2017/2154 and 2017/2155 on indirect clearing (to verify) |
| LD-C0083 Parent Entity | — | 2026-11 domain review | GLEIF Level 2 relationship data: direct and ultimate accounting consolidating parent (to verify) |
| LD-C0085 Intra-group Client | — | 2026-11 domain review | CFTC definition of proprietary account (to verify); EMIR intragroup notions (to verify) |
| LD-C0086 Non-Clearing Member | — | 2026-11 domain review | CCP rulebooks of the reference CCPs (to verify) |
| LD-C0087 Sponsored Clearing Participant | — | 2026-11 domain review | CCP rulebooks of the reference CCPs offering such a model (to verify) |
| LD-C0088 Client Regulatory Category | — | 2026-11 domain review | MiFID II definitions of retail client, professional client (Annex II) and eligible counterparty; UK conduct rules on client categorisation (to verify) |
| LD-C0089 Counterparty Regulatory Status | — | 2026-11 domain review | EMIR definitions of financial and non-financial counterparty and clearing threshold; Commodity Exchange Act definition of eligible contract participant (to verify) |
| LD-C0093 Identifier Scheme | — | 2026-11 domain review | ISO 6166, ISO 4914, ISO 10383, ISO 17442, ISO 23897; FIX security identifier source; CDM identifier; to verify |
| LD-C0094 Trading Venue Segment | — | 2026-11 domain review | ISO 10383 operating and segment MIC; to verify |
| LD-C0095 Listed Strategy | — | 2026-11 domain review | FIX multi-leg instruments; venue strategy documentation; to verify |
| LD-C0096 Flexible Series | — | 2026-11 domain review | Venue flexible-contract rules; to verify |
| LD-C0097 Underlying | — | 2026-11 domain review | CDM underlier; FpML underlyer; ISO 10962 attributes; to verify |
| LD-C0098 Key-Date Rule | — | 2026-11 domain review | Venue contract specifications; FpML business-day conventions; to verify |
| LD-C0099 Contract Adjustment | — | 2026-11 domain review | Venue and CCP corporate-action policies; CDM corporate-action events; to verify |
| LD-C0100 Clearing Contract | — | 2026-11 domain review | CCP product lists and rulebooks of the reference CCPs; to verify |
| LD-C0101 Clearing Eligibility Schedule | — | 2026-11 domain review | CCP rulebooks and product lists; EMIR authorisation scope per service; to verify |
| LD-C0102 Trading Session | — | 2026-11 domain review | FIX trading session identifiers; venue trading-hours notices; to verify |
| LD-C0103 Settlement Price | — | 2026-11 domain review | Venue settlement-price procedures; to verify |
| LD-C0108 Access Agreement | — | 2026-11 domain review | FIA and venue or CCP standard forms where they exist (titles to verify) |
| LD-C0109 Access Onboarding | — | 2026-11 domain review | CPMI-IOSCO PFMI, access and participation requirements (to verify) |
| LD-C0110 Access Requirement | — | 2026-11 domain review | CPMI-IOSCO PFMI, access and participation requirements; CCP and venue membership rules (to verify) |
| LD-C0111 Connectivity Route | — | 2026-11 domain review | FIX Protocol session layer (to verify) |
| LD-C0112 Direct Electronic Access Arrangement | — | 2026-11 domain review | MiFID II definition of direct electronic access; Delegated Regulation (EU) 2017/589 (to verify); CFTC Rule 1.73 risk controls for clearing members (to verify relevance) |
| LD-C0114 Non-Clearing Member Arrangement | — | 2026-11 domain review | CCP clearing conditions of the reference CCPs (to verify which provide for it) |
| LD-C0115 Sponsored Clearing Arrangement | — | 2026-11 domain review | CCP sponsored or direct-client model rules (to verify per reference CCP) |
| LD-C0116 Indirect Clearing Arrangement | — | 2026-11 domain review | MiFIR indirect clearing and Delegated Regulation (EU) 2017/2154; EMIR and Delegated Regulation (EU) 2017/2155; PFMI tiered participation (to verify) |
| LD-C0117 Client Order | — | 2026-11 domain review | FIX new order message and order status (to verify) |
| LD-C0118 Child Order | — | 2026-11 domain review | FIX order messages with parent-child linking (to verify) |
| LD-C0119 Pre-trade Control Check | — | 2026-11 domain review | MiFID II controls for direct electronic access and algorithmic trading (Delegated Regulation (EU) 2017/589, to verify); CFTC and venue risk-control rules (to verify) |
| LD-C0120 Venue Execution | — | 2026-11 domain review | FIX execution report (to verify) |
| LD-C0121 Client Execution | — | 2026-11 domain review | FIX execution report on the client side (to verify) |
| LD-C0122 Block Trade | — | 2026-11 domain review | Venue block trade rules (for example CME, ICE Futures Europe, Eurex; to verify); FIX trade type 'block trade' (to verify) |
| LD-C0123 Exchange for Related Position | — | 2026-11 domain review | Venue rules on exchanges for related positions (for example CME, ICE Futures Europe, Eurex; to verify); FIX trade type values (to verify) |
| LD-C0124 Strategy Leg Execution | — | 2026-11 domain review | FIX multileg order and execution reporting (to verify) |
| LD-C0125 Execution Correction | — | 2026-11 domain review | FIX execution type values for cancel and correct (to verify); venue error-trade policies (to verify) |
| LD-C0126 Executed Trade | — | 2026-11 domain review | CDM trade and its lineage (to verify); UTI (ISO 23897) where a regime requires one (to verify) |
| LD-C0129 Allocation Line | — | 2026-11 domain review | FIX allocation instruction and allocation report (to verify) |
| LD-C0130 Third-party Executing Member | — | 2026-11 domain review | FIX party roles for entering and executing firms (to verify) |
| LD-C0131 Give-up Line | — | 2026-11 domain review | FIX allocation instruction and allocation report messages; FIXML allocation and claim messages (to verify). |
| LD-C0132 Give-up Designated in Advance | — | 2026-11 domain review | US listed options clearing member trade assignment practice (name and scope to verify). |
| LD-C0136 Take-up | — | 2026-11 domain review | FIXML claim and allocation acknowledgement flows (to verify). |
| LD-C0137 Submission Acceptance | — | 2026-11 domain review | FpML clearing consent messages; MiFIR Article 29 and Commission Delegated Regulation (EU) 2017/582; CFTC Rule 1.74 (all to verify). |
| LD-C0138 Clearing Limit | — | 2026-11 domain review | CFTC Rule 1.73 clearing-member risk management and FIA procedural guidance on '1.73 give-ups' (to verify). |
| LD-C0141 Clearing Submission | — | 2026-11 domain review | FpML clearing request messages; ISDA CDM clearing instruction (to verify). |
| LD-C0142 Execution Agreement for Cleared Trades | — | 2026-11 domain review | FIA and ISDA Cleared Derivatives Execution Agreement (title and version to verify). |
| LD-C0143 CCP-facing Trade | — | 2026-11 domain review | ISDA CDM clearing events and trade lineage; FpML clearing confirmation; to verify |
| LD-C0144 Client Back-to-Back Trade | — | 2026-11 domain review | ISDA/FIA client cleared OTC derivatives addendum (principal model); ISDA CDM; to verify |
| LD-C0145 House Account | — | 2026-11 domain review | EMIR provisions on separation of house and client assets; CFTC house origin; to verify |
| LD-C0146 Client Omnibus Account | — | 2026-11 domain review | EMIR omnibus client segregation; CFTC Section 4d, Part 22 and Part 30 account classes; to verify |
| LD-C0147 Individually Segregated Client Account | — | 2026-11 domain review | EMIR individual client segregation; to verify |
| LD-C0148 Indirect Client Account | — | 2026-11 domain review | Delegated Regulations (EU) 2017/2154 (listed) and 2017/2155 (OTC) on indirect clearing; to verify |
| LD-C0149 CCP Position Account | — | 2026-11 domain review | FIXML position maintenance and position report party and account fields; reference CCP rulebooks; to verify |
| LD-C0150 Segregation Election | — | 2026-11 domain review | EMIR obligations to offer omnibus and individual segregation and to disclose protection levels and costs; to verify |
| LD-C0151 Listed Position | — | 2026-11 domain review | FIXML position report; to verify |
| LD-C0152 Cleared OTC Position | — | 2026-11 domain review | ISDA CDM; FpML; to verify |
| LD-C0153 Position Transfer | — | 2026-11 domain review | FIXML position maintenance (transfer); reference CCP transfer rules; to verify |
| LD-C0154 Clearing Member Default | — | 2026-11 domain review | CPMI-IOSCO PFMI participant-default rules and procedures; EMIR default procedures; to verify |
| LD-C0155 Porting | — | 2026-11 domain review | EMIR provisions on porting of client positions and assets (to verify); CPMI-IOSCO PFMI segregation and portability principle |
| LD-C0156 Back-up Clearing Member | — | 2026-11 domain review | EMIR porting provisions; reference CCP default rules; to verify |
| LD-C0157 Sponsoring Clearing Member | — | 2026-11 domain review | Reference CCP sponsored or direct-client model rules; to verify |
| LD-C0158 Position Adjustment | — | 2026-11 domain review | FIX position maintenance request (position adjustment, position change submission); to verify. |
| LD-C0160 Margin Parameter Set | — | 2026-11 domain review | CCP margin parameter disclosures under CPMI-IOSCO public quantitative disclosure standards (to verify) |
| LD-C0165 Margin Call Terms | — | 2026-11 domain review | ISDA Credit Support Annex call terms as bilateral analogue only (to verify); FIA Futures and Options Agreement margin provisions (to verify) |
| LD-C0167 Collateral Haircut | — | 2026-11 domain review | EMIR collateral requirements and Delegated Regulation (EU) No 153/2013 on haircuts (to verify); CDM eligible collateral (to verify) |
| LD-C0168 Concentration Limit | — | 2026-11 domain review | EMIR collateral requirements and Delegated Regulation (EU) No 153/2013 on concentration limits (to verify) |
| LD-C0172 Default Fund Contribution | — | 2026-11 domain review | EMIR default fund provisions (to verify); CPMI-IOSCO PFMI Principle 4 (to verify); Basel CCP exposures framework (to verify) |
| LD-C0173 Margin Provider | — | 2026-11 domain review | Financial Collateral Directive collateral provider (to verify) |
| LD-C0174 Margin Taker | — | 2026-11 domain review | Financial Collateral Directive collateral taker (to verify) |
| LD-C0175 Published Fee Schedule | — | 2026-11 domain review | EMIR transparency of CCP prices and fees; MiFID II venue fee structure rules (known as RTS 10); PFMI disclosure principle; all to verify. |
| LD-C0178 Fee Incentive Programme | — | 2026-11 domain review | MiFID II market-making schemes and venue fee structure rules; to verify. |
| LD-C0179 Pass-through Charge | — | 2026-11 domain review | IFRS 15 principal-versus-agent guidance as an analogue only; to verify. |
| LD-C0181 Regulatory Transaction Fee | — | 2026-11 domain review | US: NFA assessment fee; SEC transaction fees on security futures; to verify. |
| LD-C0182 Fee Rebate | — | 2026-11 domain review | EMIR disclosure of discounts and rebates by CCPs and clearing members; to verify. |
| LD-C0186 Activity Volume | — | 2026-11 domain review | Venue and CCP published volume statistics (instances); FIA volume statistics as an analogue; to verify. |
| LD-C0190 Regulatory Obligation | — | 2026-11 domain review | To verify: EMIR obligations (clearing, active account, reporting, segregation offer); MiFIR trading and transaction reporting obligations; CFTC clearing requirement and swap trading requirements. |
| LD-C0191 Clearing Obligation | — | 2026-11 domain review | To verify: EMIR clearing obligation and the ESMA public register of classes; UK EMIR equivalent; CFTC clearing requirement rules; SEC rules on clearing of certain US Treasury transactions (outside current product scope). |
| LD-C0192 Regulated Product Class | — | 2026-11 domain review | To verify: ESMA register of classes subject to the clearing obligation; ISO 10962 CFI and ISO 4914 UPI as classification inputs (not legal classes). |
| LD-C0193 Phase-in Step | — | 2026-11 domain review | To verify: EMIR delegated regulations on the clearing obligation (categories); CFTC compliance schedules. |
| LD-C0194 Rulebook | — | 2026-11 domain review | To verify: rulebooks of the reference CCPs (Eurex Clearing, ICE Clear Europe, LCH SwapClear, CME Clearing, Euronext Clearing); CPMI-IOSCO PFMI Principle 1 (legal basis). |
| LD-C0195 Regulatory Relief | — | 2026-11 domain review | To verify: CFTC staff letters; ESMA and national authority statements on supervisory practice; UK transitional powers. |
| LD-C0196 Equivalence Decision | — | 2026-11 domain review | To verify: EU equivalence decisions for third-country CCPs and trading venues; UK equivalence directions; CFTC comparability determinations. |
| LD-C0197 Change Notice | — | 2026-11 domain review | To verify: ELI for EU acts; Federal Register document numbers; each reference CCP's notice archive. |
| LD-C0198 Consultation | — | 2026-11 domain review | To verify: ESMA and national authority consultation practice; CFTC and SEC notice-and-comment process. |
| LD-C0199 Rule Change Approval | — | 2026-11 domain review | To verify: CFTC rule submission rules for DCOs and DCMs; SEC self-regulatory organisation rule filings; EU review and validation of CCP models; Bank of England CCP rule-change process. |
| LD-C0202 Regulatory Authorisation | — | 2026-11 domain review | To verify: ESMA list of third-country CCPs; CFTC lists of registered entities; Bank of England list of recognised CCPs; CRR qualifying CCP definition. |
| LD-C0203 Regulatory Authority | — | 2026-11 domain review | To verify: FIBO regulatory agency concepts. |
| LD-C0205 Source Record | — | 2026-11 domain review | ISDA CDM (records versus business events) as analogue; to verify. |
| LD-C0206 CCP Report | — | 2026-11 domain review | FIXML trade capture and position report messages; CCP report specifications (instances); to verify. |
| LD-C0208 Position Reconciliation | — | 2026-11 domain review | FIXML position report; to verify. |
| LD-C0210 Settlement Fail | — | 2026-11 domain review | CSDR settlement discipline for securities deliveries; PFMI principles 8 and 9; to verify. |
| LD-C0211 Netted Settlement Obligation | — | 2026-11 domain review | PFMI principle 9 (money settlements); to verify. |
| LD-C0212 Payment Instruction | — | 2026-11 domain review | ISO 20022 payment initiation messages; to verify. |
| LD-C0214 Settlement Deadline | — | 2026-11 domain review | CCP rulebooks and payment system rules (instances); to verify. |
| LD-C0216 Expiry | — | 2026-11 domain review | ISDA CDM lifecycle events; FIX position maintenance; to verify. |
| LD-C0217 Exercise | — | 2026-11 domain review | FIX position maintenance (exercise, do not exercise); ISDA CDM exercise; to verify. |
| LD-C0218 Exercise Instruction | — | 2026-11 domain review | FIX position maintenance request; to verify. |
| LD-C0219 Assignment | — | 2026-11 domain review | ISDA CDM; FIX position report; to verify. |
| LD-C0220 Final Settlement | — | 2026-11 domain review | PFMI principle 10 (physical deliveries); to verify. |
| LD-C0221 Delivery Notice | — | 2026-11 domain review | Venue contract specifications and CCP delivery procedures (instances); to verify. |
| LD-C0222 Trade Amendment | — | 2026-11 domain review | ISDA CDM business events (quantity change, termination); to verify. |

## Plain-language summaries

One sentence for a newcomer, a synthetic example and the nearest concept people confuse it with. Written by the 2026-11 domain experts; Draft.

| Concept | In short | Example | Not to be confused with |
|---|---|---|---|
| LD-C0001 Party | Anyone who can act or hold rights in a business relationship: a person, a company, a branch or a fund. | Fund F, its investment manager M, Clearing Broker Y and CCP Z are all parties. | Party Role: the party is who it is; the role is what it does toward someone, for a while. |
| LD-C0002 Legal Entity | A party the law treats as a distinct person, able to sign contracts and owe money in its own name. | Client A Ltd, identified by its LEI, signs a clearing agreement with Clearing Broker Y. | Commercial Group: a legal entity is a legal person; a commercial group is the firm's own way of grouping clients. |
| LD-C0003 Party Role | One party doing one job toward someone else, in a given service, for a given period. | Bank B holds the clearing member role at CCP Z for listed futures and, separately, the client role toward Executing Broker X. | Market Access Arrangement: the arrangement is the set of agreements that grants a role; the role is the function held. |
| LD-C0004 Client | The party that has signed up to receive a service from a provider. | Fund F is the client of Clearing Broker Y for clearing at CCP Z, even though Investment Manager M sends its orders. | Commercial Group: revenue rolls up to the group, but the contract is with the client. |
| LD-C0005 Broker | A firm that executes orders or clears trades for its clients as a service. | Executing Broker X executes Client A's order on Venue V; Clearing Broker Y clears the resulting trade. | Clearing Member: a broker serves clients; a clearing member is admitted to a CCP, and the two need not be the same firm. |
| LD-C0006 Executing Broker | The firm that provides execution to the client and answers to the client for it, whether or not it is itself a member of the venue. | Executing Broker X takes Client A's order and has it executed on Venue V through Member W, because X is not a member of V. | Trading Venue Member: the member is the firm admitted to enter the order on the venue; it may be a different firm from the executing broker. |
| LD-C0007 Clearing Member | A firm admitted by a CCP to one of its clearing services, in whose name trades are registered and which answers to the CCP for them. | Clearing Broker Y is a general clearing member of CCP Z's listed derivatives service, so it may clear its own trades and those of its clients there. | Sponsored Clearing Participant: admitted in its own name under a sponsored model, but a clearing member only where the CCP's rules say so. |
| LD-C0008 Central Counterparty | The role of the clearing house that steps in between buyer and seller and becomes the counterparty to each. | After CCP Z accepts a trade between Clearing Members P and Q, P faces CCP Z and Q faces CCP Z; P and Q no longer face each other. | Clearing Service: the CCP acts through one or more services, each with its own rules. |
| LD-C0009 Trading Venue | An organised marketplace, such as an exchange or a multilateral trading facility, where many participants' buying and selling interests meet under the venue's rules. | Venue V, a regulated market operated by Operator O, with an equity derivatives segment and a commodity derivatives segment. | The operator or the CCP: the operator is the company running the venue; the CCP clears the trades and is a separate entity even in the same group. |
| LD-C0010 Account | A place in someone's books where a holder's trades, positions, cash or charges are recorded for a stated purpose. | Clearing Broker Y opens a client account for Fund F and records its futures positions there. | Account identifier: the code (such as a give-up reference) points to an account; it is not the account. |
| LD-C0011 Segregation Model | The rules that say how a client's positions and assets are kept apart from the clearing member's and from other clients'. | Under omnibus segregation, Client A's positions sit at CCP Z with other clients' but apart from Clearing Broker Y's own; under individual segregation they sit alone. | Legal protection: whether the client's assets would actually be safe in a default is a separate conclusion of Legal. |
| LD-C0012 Agreement | Any arrangement that creates rights and duties between parties, whether signed or accepted by joining published rules. | Clearing Broker Y is bound to CCP Z by its membership documents and the CCP rulebook; Client A is bound to Clearing Broker Y by its client clearing agreement. | Rule Provision: a single rule within a rulebook or regulation, not the relationship it governs. |
| LD-C0013 Product Family | A family of similar traded products, such as 'equity index futures' or 'fixed-to-floating interest rate swaps', described without reference to any exchange. | Index futures listed on Venue V and on Venue W both belong to the product family 'equity index future'. | Contract Specification: a family groups many venues' contracts; a contract specification is one venue's listing of one contract. |
| LD-C0014 Instrument | One specific thing you can buy or sell that is the same for everybody: for listed derivatives, a series such as the March future or the June 100 call. | Contract K, June expiry, call, strike 100 on Venue V is one instrument; a spread buying June and selling September is another. | Trade: the instrument is what is traded; a trade is one deal in it between two parties. A bespoke swap has no instrument, only a trade. |
| LD-C0015 Business Date | A day that a business event counts towards, always stated with its role (trade date, clearing date, value date) and the calendar it is read against. | A trade executed at 23:30 local time in Venue V's evening session has the next business day as its trade date. | Timestamp: the timestamp is the exact moment in UTC; the business date is the day the event counts for, which can differ. |
| LD-C0016 Order | A request to buy or sell a quantity of a listed contract, under conditions such as a price limit or how long it stays valid. | Client A asks Executing Broker X to buy 300 lots of an index future on Venue V at no more than a stated price, valid for the day. | Execution: the order is the request; the execution is the fill that answers it, and one order can have many fills or none. |
| LD-C0017 Execution | The moment all or part of an order is filled at a price, by matching on the venue or by the venue registering a privately negotiated trade. | Executing Broker X's child order for 50 lots is filled in two pieces of 20 and 30 lots on Venue V: two executions. | Trade: the execution is an event on one order; the trade is the resulting agreement between two counterparties, and the two need not match one to one. |
| LD-C0018 Trade | The agreed deal between two counterparties on a derivative contract, with its terms; later steps such as clearing create new linked trades rather than changing it. | After Client A's fills, the executed trade between Executing Broker X and the selling member exists; at CCP Z it is replaced by trades facing the CCP. | Execution: a trade is the agreement, an execution is the fill event; and a trade record in a system is only a representation of the trade. |
| LD-C0019 Transaction | An ambiguous word that is not used as a concept for now: ask whether the speaker means an execution, a trade, a lifecycle event, a cash movement or a regulatory transaction report. | "How many transactions did Client A do yesterday?" must be answered by asking: fills, trades, allocations or reported transactions? | Trade: a trade is a defined concept; 'transaction' is only a word that may point to it or to several others. |
| LD-C0020 Allocation | The actual split of executed quantity across the target accounts, one line per account. | Executing Broker X books 100 lots to Fund F1's account cleared in-house and 200 lots to Fund F2's account at Clearing Broker Y, which starts a give-up. | Give-up / Take-up Process: only an allocation to an account at another clearing member starts a give-up; an allocation within the same clearing member is internal. |
| LD-C0021 Average Price Group | A set of fills combined so that the client gets one average price, calculated either by a venue or CCP facility or by the broker. | Client A's 300 lots were filled at seven different prices; Client A asked for an average price, so the seven fills form one average price group. | Allocation: averaging sets one price for many fills; allocation splits the quantity across accounts. |
| LD-C0022 Give-up / Take-up Process | The hand-over of an executed listed trade, in whole or in part, from the clearing member that holds it to the clearing member that will clear it for the client; give-in is the same hand-over seen by the receiver. | Executing Broker X fills 100 futures for Client A on Venue V; X's clearing member gives them up to Clearing Broker Y, which takes them up before the deadline. | Position Transfer: a transfer moves open positions between accounts later, under transfer rules; a give-up attributes a newly executed trade. |
| LD-C0023 Clearing Acceptance | The CCP accepting a trade into one of its clearing services and registering it in a clearing member's account. | CCP Z registers the trade matched on Venue V in the house account of Executing Broker X's clearing member. | CCP Interposition: registration is the evidence; interposition is the legal moment the CCP becomes counterparty, which the rulebook fixes and may come earlier. |
| LD-C0024 Novation | Replacing an existing contract or obligation with new ones, as the law allows; in clearing it is one way the CCP steps in, and outside clearing it is also how parties step in or out of a bilateral trade. | A bilateral swap between Client A and Dealer D is novated when CCP Z registers it: the original swap ends and two new swaps with the CCP replace it. | Open offer: under open offer the CCP is counterparty from the start, so no earlier contract is replaced. |
| LD-C0025 Lifecycle Event | Anything that happens to a trade, position or obligation after it exists and changes it: a take-up, a transfer, an exercise, an expiry, a correction. | Client A's long option position in a series at CCP Z is exercised at expiry; the exercise is one lifecycle event, the resulting futures position another. | Rule Change: a rule change alters the rules or schedules; a lifecycle event alters a trade, position or obligation. |
| LD-C0026 Position | What is open in an account on a given day: how many contracts are held long and short, or which cleared swaps are still running. | On clearing date D, Client A's account at Clearing Broker Y holds 40 long and 15 short contracts in the June series of Contract K at CCP Z. | Exposure or margin: risk figures calculated from a position, not the position itself. |
| LD-C0027 Portfolio | A named group of positions or other items gathered for a purpose. | CCP Z margins all of Client A's index futures and options together as one portfolio. | Account: an account records ownership and booking; a portfolio groups items for a purpose such as margining. |
| LD-C0028 Settlement Obligation | Something that must be paid or delivered, by whom, to whom, by when and why. | After the end-of-day run, Clearing Broker Y owes CCP Z variation margin in euro, due in the next settlement cycle. | Cash Movement: the obligation is what is owed; the cash movement is what was actually paid. |
| LD-C0029 Cash Movement | Money that actually moved from one account to another, with the evidence that says so. | The settlement bank's statement shows Clearing Broker Y's payment of the net euro amount to CCP Z on the value date. | Payment Instruction: the instruction asks for the payment; the cash movement is the payment that happened. |
| LD-C0030 Operational Exception | A problem someone must act on, because something expected did not happen or a rule was not met. | A give-up line to Clearing Broker Y lapsed at the cut-off; operations raises an exception to agree with Client A how to rebook the 40 lots. | Reconciliation Break: a break says two records differ; it becomes an exception only if someone must act on it. |
| LD-C0031 Fee Charge | An amount one party owes another for a service, such as an exchange fee or a client clearing fee. | Client A owes Clearing Broker Y a clearing fee for each lot registered at CCP Z today. | Revenue: a charge is what is owed on one event; revenue is a management total built from many charges under a stated basis. |
| LD-C0032 Fee Schedule | The price list and rules that say how much is charged, published by a venue or CCP or agreed with a client. | Venue V's price list for equity index futures, valid from the first of next month. | Fee Charge: the schedule sets the rates; the charge is what is owed on a given event. |
| LD-C0033 Client Execution Fee | What a client pays its broker for executing its orders. | Client A pays Executing Broker X a fee per contract side for orders worked by the care desk. | Exchange Fee Charge: the venue's own fee, which the broker owes the venue and may pass on. |
| LD-C0034 Client Clearing Fee | What a client pays its clearing broker for clearing its trades, listed or OTC. | Client A pays Clearing Broker Y a fee per lot cleared at CCP Z and a monthly maintenance fee per open interest rate swap. | CCP Fee Charge: the CCP's own fee to its clearing member, which may be passed on. |
| LD-C0035 Executing Broker Brokerage Charge | What an executing broker is owed for executing trades that are cleared elsewhere, often paid by the clearing broker and recharged to the client. | Executing Broker X executes for Client A and gives the trades up to Clearing Broker Y, which pays X's brokerage and debits Client A. | Client Execution Fee: overlaps when the client owes its own executing broker; brokerage can also be owed by a broker that hired a third-party executing member. |
| LD-C0036 Exchange Fee Charge | A fee charged by the venue operator, for trading or related services such as market data or connectivity. | Venue V charges its member a fee per contract side traded in its order book, collected through CCP Z. | CCP Fee Charge: charged by the clearing house, not the venue, even when both appear on one bill. |
| LD-C0037 CCP Fee Charge | A fee charged by a clearing house to its clearing members for clearing and related services. | CCP Z charges Clearing Broker Y a registration fee per OTC trade and a fee for holding bonds as collateral. | Margin or default fund contribution: these are collateral the member provides, not fees. |
| LD-C0038 Commission | A loose commercial word for what a broker charges per contract; it must be resolved to a specific fee before use. | A client asks for 'our commission on Venue V futures': the answer depends on whether execution, clearing or a bundled fee is meant. | Client Execution Fee: one possible meaning of commission among several. |
| LD-C0039 Revenue | What the business earns over a period, measured under stated management rules. | Execution and clearing revenue earned from Client A last quarter, in euro, with venue fees shown net. | Cash received: revenue can be reported before or without the money arriving. |
| LD-C0040 Cost | What the business spends to deliver its services, measured under stated management rules. | Exchange fees the firm owed Venue V and did not pass on to clients last month. | Pass-through Charge: a third-party fee recharged to the client is not a cost to the firm in the same way. |
| LD-C0041 Execution Revenue | What the business earns from executing orders, per client and per handling channel. | Execution revenue from Client A's care orders and from its direct market access orders, shown separately. | Clearing Revenue: earned from clearing the trades, possibly for a different client relationship. |
| LD-C0042 Clearing Revenue | What the business earns from clearing trades, per client and per clearing service. | Clearing revenue from Client A at CCP Z's listed derivatives service, excluding interest on its cash collateral. | Collateral Revenue: income from client collateral, a separate stream with its own owner. |
| LD-C0043 Margin Requirement | How much margin one party must provide to another, for an account, at a given time. | At end of day CCP Z requires Clearing Broker Y to hold an amount of initial margin on its client omnibus account. | Collateral: the requirement is what is owed; collateral is what is actually held. |
| LD-C0044 Initial Margin Requirement | Margin held to cover the loss of closing out a defaulter's positions over a few days. | Client A's futures portfolio at Clearing Broker Y needs initial margin for a two-day close-out under CCP Z's model. | US maintenance margin: a call-trigger level of the same requirement, not a separate one. |
| LD-C0045 Variation Margin Requirement | Margin that reflects the change in value of positions at current prices, settled daily or held as collateral. | Client A's long futures lost value today, so Client A owes variation margin, which Clearing Broker Y pays on to CCP Z. | Price Alignment Amount: a small interest adjustment paid alongside variation margin, never part of it. |
| LD-C0046 Margin Call | A demand to deliver margin by a deadline, for the part of the requirement not already covered. | CCP Z calls Clearing Broker Y for cash by the morning deadline after the overnight run. | Margin Requirement: the call is only the uncovered part of the requirement, after collateral held. |
| LD-C0047 Collateral | Cash or securities actually held by one party from another to cover margin. | Clearing Broker Y holds government bonds from Client A under a security interest, valued after haircut. | Collateral Asset: an asset that could be used is not collateral until it is delivered. |
| LD-C0048 Collateral Asset | Something that could be used as collateral, such as cash in a currency or a bond. | A euro government bond is a collateral asset; it is eligible at CCP Z with a haircut. | Collateral: the asset in general, versus a quantity of it actually held. |
| LD-C0049 Collateral Movement | An actual transfer of collateral: delivery, return, substitution or move between accounts. | Client A delivers bonds to Clearing Broker Y's collateral account to meet a call. | Margin Call: the call is the demand; the movement is what actually happened. |
| LD-C0050 Reconciliation | Checking, for a given date, that two sources tell the same story about the same trades, positions or amounts, and listing where they do not. | Each morning operations compares its end-of-day positions per CCP account with CCP Z's position report for the previous clearing date. | Operational Exception: reconciliation finds differences; an exception is the situation someone must then handle. |
| LD-C0051 Clearing Service | One line of business of a CCP, such as its listed equity derivatives clearing or its interest rate swap clearing, with its own members, accounts, margin and rules. | CCP Z runs two clearing services: one for listed futures and options, one for interest rate swaps; Clearing Broker Y is a member of the first only. | Service Offering: the clearing service a broker sells to its clients, not the CCP's. |
| LD-C0052 Service Offering | A service the firm sells to clients, such as execute-and-clear on listed equity index futures for institutional clients, described by what it covers, where and through which channels. | An execution-only offering for Client A on Venue V, where Client A's trades are given up to Clearing Broker Y. | Clearing Service: that is a clearing house's own rulebook-defined service; the firm's offering may rely on it but is not it. |
| LD-C0053 Clearing Member Acceptance | The receiving clearing member's yes or no (or partial yes) to taking clearing responsibility for a trade, whether by an explicit take-up, automatically within a limit, or by consenting to an OTC clearing submission. | Clearing Broker Y takes up a give-up line for Client A's account after checking the give-up agreement and Client A's limit. | Clearing Acceptance: that is the CCP accepting or registering the trade; the member's decision can come before it or at the same moment. |
| LD-C0054 CCP Interposition | The legal moment when the CCP becomes the buyer to every seller and the seller to every buyer for a trade; this is what 'cleared' really means. | Under CCP Z's rules the CCP becomes counterparty when the trade is matched on Venue V, before any give-up happens. | Clearing Acceptance: the CCP's acceptance or registration message is evidence of interposition, not the interposition itself. |
| LD-C0055 Give-up Agreement | The signed agreement that lets a client trade with one broker and clear with another, and says who pays and who is responsible if the clearing broker does not take the trade. | Client A, Executing Broker X and Clearing Broker Y sign a give-up agreement so that X can give up Client A's futures trades to Y. | Client Clearing Agreement: that one governs the clearing service Y provides to Client A; the give-up agreement only governs the hand-over from X to Y. |
| LD-C0056 Client Clearing Agreement | The contract between a client and its clearing broker that sets how the client is cleared: legal model, segregation, margin, collateral, limits, fees and what happens on default. | Client A signs a client clearing agreement with Clearing Broker Y covering listed derivatives at CCP Z and interest rate swaps at CCP W, electing omnibus segregation at both. | Give-up Agreement: the agreement among client, executing broker and clearing broker on how executions are handed over for clearing. |
| LD-C0057 Clearing Broker | The firm that clears a client's trades for it and is answerable to that client, whether or not it is itself a member of the CCP. | Client A clears its futures at CCP Z through Clearing Broker Y, which is a member there; at CCP W, Clearing Broker Y clears Client A's trades through another member. | Clearing Member: admission at the CCP; and FCM, a US registration of the legal entity. |
| LD-C0058 Trading Venue Member | A firm admitted under a venue's rules to enter orders and register trades there in its own name. | Member W is admitted to Venue V as a trading-only member: it enters orders but clears through another firm. | Clearing Member: being admitted to trade on a venue does not mean being admitted to clear at its CCP. |
| LD-C0059 Market Access Arrangement | The route by which someone gets into one venue or one clearing house: as a member, through another member, as a client, or under a sponsored model, with its status and dates. | Broker B reaches Venue V through Member M, a third-party executing member there, because Broker B is not a venue member; the route is live from a given date. | Trading Venue Member or Clearing Member: those are the roles a route can give; the route is the relationship and paperwork that gives them. |
| LD-C0060 Allocation Instruction | The client's instruction saying which accounts, and which clearing brokers, should receive which part of the executed quantity. | Investment Manager M tells Executing Broker X to put 100 lots in Fund F1's account and 200 lots in Fund F2's account cleared by Clearing Broker Y. | Allocation: the instruction is the request; the allocation is the split actually made. |
| LD-C0061 Order Handling Channel | How one order was worked and reached the venue: by a person at the broker, by the broker's algorithm, by the client through the broker's systems, or by the client directly under the broker's membership. | Client A's order starts as a care order on the desk; two hours later the trader passes the rest to a broker algorithm, so the channel changes. | Market Access Arrangement: that says what the client is allowed to do (for example use direct electronic access); the channel says how this particular order was actually handled. |
| LD-C0062 Contract Specification | The rulebook page of one listed contract: underlying, size, tick, expiry months, settlement method and trading hours, from which all its series are created. | Venue V's specification for Contract K: a future on Index I, ten units per index point, quarterly expiries, cash settled. | Instrument: the specification is the template; the instrument is one series created from it, such as the March expiry. |
| LD-C0063 Rule Provision | One citable rule, in one version: an article of a regulation, a paragraph of a CCP rulebook, a staff relief letter or a firm procedure. | The paragraph of CCP Z's procedures that sets the latest time to take up a give-up, in the version applying from a given date. | Rule Change: the move from one version of the rule to the next; and Change Notice: the document that announces it. |
| LD-C0064 Rule Change | A change to a rule or to a published specification, followed from proposal or consultation until it applies, with its status and its dates. | CCP Z proposes to move its give-up take-up deadline thirty minutes earlier; the change is adopted, approved by its supervisor and applies from a stated clearing date. | Change Notice: the circular or publication that announces one or more changes; and a change in a client's or CCP's regulatory status, which is a new classification, not a rule change. |
| LD-C0065 Cut-off | The latest time a step can be done, with the calendar it is read against, what happens if it is missed, and who set it. | CCP Z's deadline for taking up give-ups is a stated local time on the clearing date; a line not taken up by then lapses and stays with the giving member. | Business Calendar: the calendar says which days count; the cut-off says the latest time on such a day and the consequence of missing it. |
| LD-C0066 Business Calendar | The published list of open and closed days, early closes and sessions for one venue, contract, CCP, currency or office. | CCP Z's clearing calendar shows 26 December as closed although Venue W, in another country, is open. | Cut-off: the calendar says which days count; a cut-off sets the time on such a day by which a step must be done. |
| LD-C0067 Regulatory Regime | A body of law and regulation of one jurisdiction, such as EU EMIR or the US Commodity Exchange Act with the CFTC's rules. | UK EMIR is a separate regime from EU EMIR, even where the texts started out identical. | Rulebook: the rules of one CCP or exchange, which are not part of any regime; and jurisdiction, which is just the country or area where several regimes apply. |
| LD-C0068 Regulatory Classification | A status that a regime gives to someone or something for a period, such as 'financial counterparty above the clearing threshold' or 'recognised third-country CCP'. | Client A represents that it is a financial counterparty above the clearing threshold for interest rate derivatives under EU EMIR from a stated date. | Regulatory Obligation: the duty that follows from a status; and a commercial client segment, which carries no regulatory meaning. |
| LD-C0069 CCP Account | An account that a CCP opens in one clearing service, for a member's own business or for its clients, where the CCP records positions and attributes margin and collateral. | Clearing Broker Y holds at CCP Z a house account, a net omnibus client account and an individually segregated account for Client A. | Client Account: the account the clearing broker keeps in its own books for each client and maps to a CCP account. |
| LD-C0070 Margin Methodology | The rules and numbers a CCP or broker uses to work out how much margin is needed. | CCP Z margins equity index futures with a portfolio VaR-type model; Clearing Broker Y applies CCP Z's model to Client A with a multiplier. | Margin Requirement: the methodology is the recipe, the requirement is the amount it produces. |
| LD-C0071 Collateral Arrangement | The legal terms under which collateral is given, valued, paid interest and returned. | Client A's clearing agreement with Clearing Broker Y includes collateral terms with title transfer of cash. | Client Clearing Agreement: the wider agreement that may contain the collateral terms. |
| LD-C0072 Collateral Eligibility Schedule | The list of what a collateral taker accepts, with haircuts and limits. | CCP Z's schedule accepts cash in three currencies and certain government bonds, each with a haircut and a limit. | Collateral Arrangement: the schedule says what is acceptable; the arrangement sets the legal terms. |
| LD-C0073 Commercial Group | The set of clients a provider treats as one relationship for sales, pricing and revenue. | Broker B groups Investment Manager M and the twenty funds it manages into one commercial group. | Ownership group: the commercial group is the provider's own choice and can sign nothing; the ownership group follows legal parents. |
| LD-C0074 Contribution | What a client, service or venue brings in after deducting the direct costs an approved list includes. | Client A's revenue less the venue and CCP fees the firm absorbed for it, for one quarter in euro. | Profitability: deducts more, such as shared costs, funding and capital, and is not modelled yet. |
| LD-C0075 Natural Person | A party that is a person rather than an organisation. | Trader T, an employee of Investment Manager M, is authorised to place orders for Fund F. | Authorised Representative: being a person says what the party is; being authorised to instruct is a role it holds. |
| LD-C0076 Branch | An office of a company in another place that acts for the company but is not a separate company. | Bank B's London branch holds Bank B's membership of Venue V; Bank B remains legally bound. | Subsidiary: a subsidiary is a separate legal entity owned by a parent; a branch is part of the same legal entity. |
| LD-C0077 Investment Fund | A pool of investors' money run by a manager, which trades and clears derivatives in its own name. | Sub-fund F2 of umbrella fund F has its own LEI, its own client accounts and its own clearing agreement, signed for it by Investment Manager M. | Investment Manager: the fund owns the positions and is the client; the manager instructs for it. |
| LD-C0078 Authorised Representative | Someone allowed to instruct the broker on a client's behalf. | Trader T and Investment Manager M are both authorised to send orders for Fund F to Executing Broker X; only M may send allocations. | Client: the representative instructs; the client is bound and owes the fees. |
| LD-C0079 Investment Manager | The firm that runs funds' money and trades for them. | Investment Manager M places one order for 300 lots and allocates it across Funds F1, F2 and F3, each a separate client. | Investment Fund: the fund holds the positions and is the client; the manager decides and instructs. |
| LD-C0080 Economic Beneficiary | The party that ultimately gains or loses on the positions, when it is not the account holder. | Broker Q holds an omnibus account with Clearing Broker Y; the economic beneficiaries are Broker Q's own clients. | Ultimate beneficial owner in know-your-customer checks: that is a person who owns or controls a company, a separate compliance fact. |
| LD-C0081 Indirect Client | The client of a client, in a clearing chain. | Fund F clears through Broker Q, which is itself a client of Clearing Member Y at CCP Z; Fund F is an indirect client. | Economic Beneficiary: an indirect client has a clearing relationship in the chain; a beneficiary may only bear the result. |
| LD-C0082 Account Identifier | A code that points to an account, unique only in the books of whoever issued it. | Executing Broker X tags a trade with give-up reference 'GU-77', which designates Fund F's account at Clearing Broker Y. | Account: the code is a label pointing to the account; the account is where the activity is recorded. |
| LD-C0083 Parent Entity | The company that owns or controls another company, directly or at the top of the chain. | Holding H is the ultimate parent of Client A Ltd and Client A Inc, according to public LEI relationship data. | Commercial Group: ownership follows legal parents; the commercial group is the firm's own grouping and may differ. |
| LD-C0084 Contracting Entity | Which of a provider's legal entities has the contract with the client for a given service. | Client A clears listed futures at a US CCP with Broker B's US entity and at a European CCP with Broker B's European entity: two contracting entities, two client relationships. | Branch: a branch may service the client, but the contract is with the legal entity. |
| LD-C0085 Intra-group Client | A client that belongs to the same ownership group as the provider. | Broker B's asset management subsidiary clears through Broker B's clearing entity and is flagged as an intra-group client. | Commercial Group: the provider's own grouping. And eligibility for a regulatory intragroup exemption, which is a Regulatory Relief with its own group test and conditions. |
| LD-C0086 Non-Clearing Member | A venue member that trades on the exchange but has another firm clear its trades. | Firm N is a member of Venue V and clears all its trades at CCP Z through General Clearing Member Y. | A party that reaches a venue through a Third-party Executing Member under a Third-Party Execution Arrangement is not a venue member; a non-clearing member is a venue member whose trades are cleared by a general clearing member. |
| LD-C0087 Sponsored Clearing Participant | A client that becomes a direct participant at a CCP with a clearing member as its sponsor. | Pension Fund P is admitted to CCP Z's sponsored model, with Clearing Member Y as sponsor. | Sponsored access (execution): that is a way to send orders to a venue; this is a status at a CCP. |
| LD-C0088 Client Regulatory Category | How a provider has categorised a client under conduct rules, for example professional client or eligible counterparty. | Client A is categorised as a professional client by Broker B's European entity and as an eligible counterparty for a different service. | Counterparty Regulatory Status: that belongs to the legal entity and drives obligations such as mandatory clearing; this belongs to the relationship and drives client protection. |
| LD-C0089 Counterparty Regulatory Status | The regulatory status a company has in its own right, which decides rules such as whether it must clear. | Client A Ltd declares itself a non-financial counterparty above the clearing threshold for interest rate derivatives. | Regulatory Authorisation: licences and registrations (for example swap dealer, futures commission merchant) are authorisations, not counterparty statuses. |
| LD-C0090 Client Account | The account a broker keeps in its own books for one client. | Clearing Broker Y keeps client account 'F2-futures' for Sub-fund F2, mapped to its omnibus client account at CCP Z. | CCP Account: the CCP keeps that one in the clearing member's name; several client accounts often map to one CCP account. |
| LD-C0091 Market Operator | The company that runs a trading venue. | Operator O runs Venue V and its negotiated-trade segment; Operator O belongs to Exchange Group E. | Trading Venue: the venue is the trading system; the operator is the company that runs it. 'The exchange' can mean either, or the group. |
| LD-C0092 Settlement or Custody Agent | The bank, custodian or triparty agent a party uses to pay, deliver or hold collateral. | Clearing Broker Y pays its sterling obligations to CCP Z through Settlement Bank S and holds pledged bonds with Triparty Agent T. | Clearing Broker: clears trades for a client; a settlement or custody agent only moves or holds cash and assets. |
| LD-C0093 Identifier Scheme | A numbering system, such as ISIN for instruments or MIC for venues, that says who issues the numbers, what they look like and where they are unique. | Series June of Contract K carries an ISIN, Venue V's own instrument code and CCP Z's product code; three schemes, one instrument. | Product Family classification codes: a CFI code describes what kind of thing an instrument is; it does not say which one. |
| LD-C0094 Trading Venue Segment | A section of an exchange, such as its equity derivatives market or its commodity market, that can have its own rules, hours and fees. | Venue V has an equity derivatives segment and a commodity derivatives segment, each with its own segment code. | Trading Venue: the segment is part of one venue; a separately authorised venue run by the same operator is a different venue. |
| LD-C0095 Listed Strategy | A ready-made combination, such as a calendar spread or an option straddle, that a venue lets you trade in one go. | A calendar spread on Venue V: buy one June future and sell one September future of Contract K, quoted as one price difference. | Two separate trades in the same legs: a strategy is traded as one instrument at one net price, legging in is two independent executions. |
| LD-C0096 Flexible Series | A series with custom terms, such as an unusual expiry date or strike, that a venue creates on demand for a participant. | Client A asks Venue V to create a Contract K option expiring on 17 August with strike 103; the venue creates it the same day. | Standard series: listed in the regular cycle and known in advance; a flexible series exists only once requested. |
| LD-C0097 Underlying | The thing a derivative is 'on': a share, an index, an interest rate, a commodity, or another derivative. | Contract K is a future on Index I, published by Administrator A; an option on Contract K's June future has that future as its underlying. | Instrument: the underlying is what the derivative refers to; it is an instrument only when it is itself a listed derivative. |
| LD-C0098 Key-Date Rule | The rule that says, for each series, when it stops trading, when it expires and when it settles, for example 'third Friday of the month, or the day before if that is a holiday'. | Contract K: last trading day is the third Friday of the expiry month on Venue V's calendar; if closed, the preceding business day. | Business Date: the rule computes the dates; the resulting dates are business dates with roles. |
| LD-C0099 Contract Adjustment | A change a venue makes to existing contracts because something happened to the underlying, such as a share split or special dividend. | After a 2-for-1 split of Share S, Venue V adjusts existing Contract K options to strike 50 and multiplier 200, and lists new standard series beside them. | Rule Change: a rule change alters the specification for the future; an adjustment changes existing series after an underlying event under rules already in force. |
| LD-C0100 Clearing Contract | The CCP's own version of a contract, under which it records positions, even when the contract is traded on more than one venue. | Contract K is listed on Venue V and Venue W; CCP Z holds positions from both under one clearing contract with one product code. | Contract Specification: the venue publishes the specification for trading; the CCP's clearing contract is what positions and margin are held in. |
| LD-C0101 Clearing Eligibility Schedule | The CCP's published list of what it can clear, and within which limits. | CCP Z's swap clearing service accepts fixed-to-floating swaps in currency C on index I up to a stated maximum maturity, from a stated effective date. | Collateral Eligibility Schedule: lists the assets a taker accepts as collateral; this schedule lists the contracts or OTC products a CCP accepts for clearing. And Clearing Obligation: what a regulation requires to be cleared. |
| LD-C0102 Trading Session | A part of the trading day, such as the opening auction, continuous trading or an evening session, with its hours and the trade date it counts towards. | Venue V's evening session runs from 18:00 to 22:00 local time and counts towards the next business day's trade date. | Business Calendar: the calendar says which days are open; the session says which hours of a day and which trade date they count for. |
| LD-C0103 Settlement Price | The official end-of-day (or final) price that the exchange or CCP publishes for a series and that positions are valued at. | CCP Z publishes the daily settlement price of Contract K June for Monday; at expiry it publishes the final settlement price. | Last traded price: the settlement price is set by the venue or CCP's method, and may differ from any traded price. |
| LD-C0104 Processing Window | A named stretch of a clearing day when a CCP or payment system accepts a given step. | CCP Z accepts give-ups for the clearing date from the end of trading until early evening, then opens a shorter late-correction window. | Cut-off: the cut-off is the latest time and its consequence; the window is the whole period when the step is accepted. |
| LD-C0105 Service Component | One building block of a service, for example average pricing inside an execute-and-clear service. | Broker B's execute-and-clear offering for Client A includes broker-side average pricing as a component priced separately. | Service Kind: the kind classifies the whole offering; a component is one piece inside it. |
| LD-C0106 Offering Coverage Line | One line of 'where and for what' a service is available, and which access route makes it possible. | Broker B's clearing-only offering covers equity index options in the clearing service of CCP Z, relying on Broker B's general clearing membership there. | Market Access Arrangement: the arrangement is the route into the venue or CCP; the coverage line says the firm sells a service using that route. |
| LD-C0107 Offering Eligibility Criterion | A rule the firm applies to decide which clients can get a service. | Broker B offers direct electronic access on Venue V only to clients that passed its electronic trading due diligence. | Access Requirement (set by a venue, CCP or regulator for the route itself); Clearing Eligibility Schedule (what the CCP accepts); Clearing Limit (how much the clearing member accepts automatically). |
| LD-C0108 Access Agreement | A signed document that sets up or governs a route into a venue or clearing house. | Client A signs a direct electronic access agreement with Broker B before sending orders to Venue V under Broker B's membership. | Give-up Agreement, Client Clearing Agreement (which also documents the non-clearing member model) and Execution Agreement for Cleared Trades: each keeps its own concept. |
| LD-C0109 Access Onboarding | The steps the firm, or a client, goes through to get a new route into a venue or clearing house. | To clear for clients at CCP Z, Broker B applies as a general clearing member, signs the admission documents, completes testing and goes live. | Client onboarding: answered from the Client role a client holds toward the contracting entity for an offering, with its status, agreements and mapped accounts; access onboarding sets up a route into a venue or CCP. |
| LD-C0110 Access Requirement | A condition a venue, clearing house or regulator sets before someone can use a given route in. | CCP Z requires a general clearing member to hold a stated minimum capital and contribute to the default fund. | Offering Eligibility Criterion: that is the firm's own rule for clients; an access requirement is imposed on the holder of the route. |
| LD-C0111 Connectivity Route | The technical line used to reach a venue or clearing house. | Client A's sponsored access orders reach Venue V over Client A's own direct connection using Broker B's member identity. | Direct Electronic Access Arrangement: that is the permission to send orders under a member's identity; the connectivity route is the technical line, which may be the member's or the client's. |
| LD-C0112 Direct Electronic Access Arrangement | Permission given by a venue member for a client to send its own orders to the venue under the member's identity. | Client A sends orders to Venue V through Broker B's gateway under a direct market access arrangement. | Sponsored Clearing Arrangement: sponsored access is about sending orders; sponsored clearing is about being admitted to a clearing house. |
| LD-C0113 Third-Party Execution Arrangement | A broker reaches a venue where it is not a member by passing orders to a broker that is. | Broker B sends Client A's orders for Venue V to Member M, a third-party executing member on Venue V, because Broker B is not a member there. | Give-up: third-party execution concerns who executes on the venue; give-up concerns which clearing member ends up with the trade. |
| LD-C0114 Non-Clearing Member Arrangement | A venue member that is not a clearing member gets its trades cleared by a clearing member that is. | Broker B is a member of Venue V but not of CCP Z; Clearing Broker Y, a general clearing member at CCP Z, clears Broker B's trades. | Client clearing: any client may clear through a clearing member; a non-clearing member is a venue member whose status the CCP recognises. |
| LD-C0115 Sponsored Clearing Arrangement | A client is admitted directly to a clearing house, with a clearing member standing behind it under the clearing house's rules. | Client A is admitted to the clearing service of CCP Z under its direct-client model, with Clearing Broker Y as sponsor. | Direct Electronic Access Arrangement in its sponsored access form: that concerns sending orders to a venue, not clearing. |
| LD-C0116 Indirect Clearing Arrangement | Clearing for someone who is a client of a client of the clearing member. | Broker B clears at CCP Z through Clearing Broker Y and offers clearing to Client A, who becomes an indirect client at CCP Z. | Client clearing: there the clearing member's client is the party itself; in indirect clearing there is one more link in the chain. |
| LD-C0117 Client Order | The order as the client gave it to the broker, before the broker splits or routes it. | Investment Manager M sends Executing Broker X an order to sell 500 lots of a bond future, to be worked through the day. | Child Order: the client order is what the client asked for; child orders are the pieces the broker sends to the market to work it. |
| LD-C0118 Child Order | A smaller order the broker cuts from the client's order and sends to the market. | The broker algorithm working Client A's 300-lot order sends three child orders of 100 lots to Venue V over an hour. | Allocation Line: a child order splits the order before execution to work it in the market; an allocation line splits the executed quantity across accounts afterwards. |
| LD-C0119 Pre-trade Control Check | An automatic check that stops an order going to the market if it breaks a limit. | Client A's sponsored-access order for 5,000 lots is rejected because it exceeds the maximum order size set by Member W. | Clearing Limit: the same limit set by a clearing member can be applied here before execution and again at take-up or submission acceptance after it; the check is the act of applying a limit to one order. |
| LD-C0120 Venue Execution | A fill as the venue records it, against the order the member entered there. | Venue V reports that Member W's child order bought 20 lots at one price and 30 lots at another: two venue executions. | Client Execution: the venue execution is the market-side fill; the client execution is what the broker reports to the client, possibly combining several venue fills at an average price. |
| LD-C0121 Client Execution | A fill as the broker reports it to the client. | Executing Broker X reports to Client A one fill of 300 lots at the average price of seven venue fills. | Venue Execution: the client execution faces the client and can combine several venue fills; Allocation Line: the client execution is not yet split across accounts. |
| LD-C0122 Block Trade | A large trade agreed privately between two parties and then registered on the venue under special rules. | Executing Broker X arranges a 1,000-lot block in an index future between Client A and Client B and registers it on Venue V within the reporting window. | Large-in-scale treatment, which is a transparency waiver or deferral under trading regulation, and a bunched order, which is an order placed for several accounts for later allocation. |
| LD-C0123 Exchange for Related Position | A swap of a futures position against a matching position in the underlying or in an OTC derivative, agreed privately and registered on the venue. | Client A sells 200 lots of a bond future to Executing Broker X and at the same time buys the matching bonds from X; the futures leg is registered on Venue V as an exchange for physical. | Block Trade: a block has no related position and needs a minimum size; an exchange for related position needs a genuine related position, usually without a minimum size. |
| LD-C0124 Strategy Leg Execution | The fill in one leg contract that results when a spread or option combination is filled. | Client A's calendar spread fills for 100 lots on Venue V; the venue produces a buy of 100 March futures and a sale of 100 June futures, each with its own price. | Venue Execution of a single instrument: a leg execution exists only because a strategy was filled, and its price is assigned by venue rules rather than matched alone. |
| LD-C0125 Execution Correction | A later fix or cancellation of a fill, recorded as a new event that points back to the original. | Venue V cancels a trade executed outside its price limits ten minutes after the match; Executing Broker X then corrects Client A's fill. | Trade Amendment: a change made to a registered trade under the clearing service's rules or by agreement of the parties; an execution correction comes from the venue's error-trade rules or the broker's client-facing correction, even after registration. |
| LD-C0126 Executed Trade | The trade as it exists right after execution, before the CCP steps in. | Client A's buy order is matched on Venue V against Member Q; at a CCP that novates at registration, the executed trade between Executing Broker X and Member Q exists until CCP Z registers it. | CCP-facing trade: after interposition each side faces the CCP in a new trade; the executed trade is the one before. |
| LD-C0127 Average Price Residual | The small leftover amount created when an average price is rounded. | Client A's seven fills average to a price that has to be rounded to the price increment; the leftover is recorded against that average price group. | Fee Charge: a residual is not a fee for a service; it arises from rounding a price. |
| LD-C0128 Standing Allocation Instruction | A split rule the client sets once, which the broker applies to every matching trade. | Fund F tells Executing Broker X that all its bond futures trades go to its account at Clearing Broker Y until further notice. | Clearing Designation on an order: a standing instruction covers many orders over a period; a designation is given on one order. |
| LD-C0129 Allocation Line | One row of a split: so many lots, at this price, to this account. | Executing Broker X's allocation of Client A's 300 lots has two lines: 100 lots to Fund F1 internally and 200 lots to Fund F2 at Clearing Broker Y. | Fill: an allocation line splits quantity already filled; it is never a fill. |
| LD-C0130 Third-party Executing Member | A venue member that another broker uses to reach a venue where it is not a member. | Executing Broker X is not a member of Venue T, so it routes Client A's child orders to Member W, which enters them on Venue T. | Executing Broker: the executing broker serves the client; the third-party executing member serves the executing broker on the venue. |
| LD-C0131 Give-up Line | One request to hand a stated quantity of a trade to one other clearing member's account; give-up progress is tracked line by line. | Client A's 100 lots are allocated 60 to Clearing Broker Y and 40 to Clearing Broker W: the giving member sends two give-up lines. | Allocation Line: the allocation line is the client's split of the quantity; a give-up line exists only for the part routed to another clearing member. |
| LD-C0132 Give-up Designated in Advance | A give-up where the clearing broker is named up front and the CCP books the trade straight to it. | Client A's order on Venue V names Clearing Broker Y; Y has pre-approved Client A within a limit, so CCP Z registers the fill directly in Y's account. | Give-up after Registration: there the executing side's clearing member holds the trade first and hands it over later. |
| LD-C0133 Give-up after First Registration | A give-up where the trade first lands with the executing side's clearing member and is handed over afterwards. | CCP Z registers Client A's fill in the account of Executing Broker X's clearing member at matching; Clearing Broker Y takes it up two hours later. | Position Transfer: a transfer moves open positions after the give-up window, under different rules and often for a fee. |
| LD-C0134 Giving Clearing Member | The clearing member that gives up this line. | Executing Broker X enters Client A's order through Member M, a third-party executing member on Venue V; Member M's clearing member is the giving clearing member for the line given up to Clearing Broker Y. | Executing Broker: the executing broker serves the client; the giving clearing member may be a different firm. |
| LD-C0135 Receiving Clearing Member | The clearing member named to receive this line. | Clearing Broker Y is named on Client A's give-up line and takes it up into Client A's omnibus account at CCP Z. | Clearing Broker: the clearing broker is the client's service provider; it may clear through a different receiving clearing member. |
| LD-C0136 Take-up | The receiving clearing member saying 'yes, I take this give-up line' (or part of it, or no). | Clearing Broker Y claims 60 of the 100 lots on Client A's give-up line and rejects 40 because the account is not set up. | Lapse: a line nobody takes up by the deadline lapses; a lapse is not a rejection and is counted apart. |
| LD-C0137 Submission Acceptance | The OTC clearing broker's yes or no to clearing a swap that has been sent for clearing. | Client A's swap with Dealer D is sent to CCP Z; Clearing Broker Y's limit check passes and Y consents automatically. | Take-up: take-up answers a listed give-up line; submission acceptance answers an OTC clearing submission. |
| LD-C0138 Clearing Limit | The pre-agreed ceiling up to which a clearing broker accepts a client's trades without a manual check. | Clearing Broker Y lets Executing Broker X give up Client A's trades in one futures contract up to a set number of lots per day. | Margin Requirement: the amount of margin owed on positions already held; a clearing limit caps what is accepted for clearing. |
| LD-C0139 Give-up Registration | The moment the CCP actually books the given-up quantity into the receiving member's account; this is what makes a give-up complete. | After Clearing Broker Y's claim, CCP Z moves the 60 lots from Clearing Member M's account to Y's client account. | Clearing Acceptance: clearing acceptance is the first registration of the trade into the service; give-up registration re-books an already registered (or designated) quantity to another member. |
| LD-C0140 Take-up Deadline | The CCP's latest time on a clearing date for sending and accepting a give-up, and what happens if it is missed. | Under CCP Z's rules a give-up not claimed by the evening deadline of the clearing date lapses and stays with the giving member. | Allocation instruction deadline: that is the time by which the client must give its split; the take-up deadline governs the clearing members. |
| LD-C0141 Clearing Submission | The request sent to a CCP, usually for an OTC trade, asking it to clear the trade through named clearing brokers. | A swap between Client A and Dealer D is affirmed on a platform and submitted to CCP Z naming Clearing Broker Y for Client A. | Give-up / Take-up Process: a listed give-up hands an already registered trade to another member; a clearing submission asks for clearing in the first place. |
| LD-C0142 Execution Agreement for Cleared Trades | The OTC agreement that says what happens to a swap meant for clearing if the clearing broker or CCP refuses it. | Client A and Dealer D sign it before trading swaps that will be cleared at CCP Z through Clearing Broker Y. | Give-up Agreement: used for listed futures and options, and it governs a hand-over between clearing members that does not exist in OTC clearing. |
| LD-C0143 CCP-facing Trade | The cleared trade that a member holds with the CCP after clearing, in its house account or in a client account. | Executing Broker X's trade with Executing Broker Q is cleared at CCP Z; Clearing Broker Y now holds a trade with CCP Z in its client account for Client A. | Executed trade: the trade agreed before clearing, which clearing replaces. |
| LD-C0144 Client Back-to-Back Trade | The matching trade between the clearing broker and its client that exists when the broker clears as principal. | Clearing Broker Y holds a swap with CCP Z in its client account for Client A and, on opposite terms, the same swap with Client A. | CCP-Facing Trade: the trade the member holds with the CCP; the back-to-back trade is the one it holds with the client. |
| LD-C0145 House Account | The CCP account for a clearing member's own trading. | Clearing Broker Y's own hedging trades at CCP Z are registered in its house account; its affiliate Firm R is cleared there too. | Client Omnibus Account: holds clients' positions, kept apart from the house account. |
| LD-C0146 Client Omnibus Account | One CCP account shared by several clients of a clearing member, kept apart from the member's own business. | Clients A, B and C of Clearing Broker Y are cleared at CCP Z in Y's gross omnibus client account; each client has its own position account inside it. | An internal pooled account: a grouping in the broker's own books, which the CCP does not see. |
| LD-C0147 Individually Segregated Client Account | A CCP account used for one client alone, so its positions and collateral are visible separately at the CCP. | Client A elects individual segregation at CCP Z; Clearing Broker Y opens an account for Client A alone in Y's name. | US cleared swaps (LSOC) accounts: legally segregated per customer but held in a shared omnibus account at the DCO. |
| LD-C0148 Indirect Client Account | A CCP account for the clients of a clearing member's client. | Broker B clears through Clearing Broker Y at CCP Z and offers clearing to its own client, Fund F; Fund F's positions sit in Y's indirect client account for Broker B. | Client Omnibus Account: for direct clients of the member, not for clients of its clients. |
| LD-C0149 CCP Position Account | A sub-account at the CCP where positions are kept apart inside a larger account. | Inside Clearing Broker Y's gross omnibus account at CCP Z, Client A and Client B each have a position account; margin is called on the omnibus account. | Client Account: kept by the clearing broker in its own books; a position account is kept by the CCP. |
| LD-C0150 Segregation Election | The client's recorded choice of how its positions and collateral are segregated at a given CCP. | Client A elects individual segregation at CCP Z from 1 March and stays in the net omnibus account at CCP W. | Segregation Model: the rules for each option; the election is the client's choice among them. |
| LD-C0151 Listed Position | How many contracts of a listed future or option series are open, long and short, in one account on one day. | At end of clearing date D, CCP Z reports 40 long and 15 short in the June series of Contract K for Client A's position account. | Open interest: the venue's or CCP's market-wide total, not one account's position. |
| LD-C0152 Cleared OTC Position | The cleared swaps still running in one account on one day. | Client A's account at CCP W holds 120 open interest rate swaps on clearing date D; compression the next day reduces them to 30. | Listed Position: counted in contracts of a series; a cleared OTC position is a set of trades with their own terms. |
| LD-C0153 Position Transfer | Moving open positions from one CCP account to another on request, for example when a client changes clearing broker. | Client A moves its open futures from Clearing Broker Y to Clearing Broker V at CCP Z; both members agree and CCP Z moves the positions. | Porting: a move forced by a clearing member's default, with its own rules and collateral leg. |
| LD-C0154 Clearing Member Default | The CCP formally declares that a member has failed, which starts the default procedures. | CCP Z declares Clearing Member P in default; Client A's positions held through P become eligible for porting. | A late margin payment: an exception the CCP may handle without declaring a default. |
| LD-C0155 Porting | Moving clients' positions and collateral from a failed clearing member to a back-up member, or closing them out if that fails. | After Clearing Member P defaults at CCP Z, Client A's individually segregated account is ported to Back-up Clearing Member Y; the omnibus clients who named no back-up are closed out. | Position Transfer: a voluntary move requested by the member or client. |
| LD-C0156 Back-up Clearing Member | A second clearing member ready to take over a client's positions if its usual clearing member fails. | Client A names Clearing Broker V as its back-up at CCP Z; V has pre-agreed to accept Client A's positions on a default. | A second clearing broker used day to day: that is an ordinary Clearing Broker role, not a back-up. |
| LD-C0157 Sponsoring Clearing Member | A clearing member that stands behind a client admitted directly to a CCP under a sponsored model. | Clearing Member Y, acting as sponsor, supports Fund F, which is admitted to CCP Z's repo clearing service in its own name. | Sponsored access: an execution channel at a venue, unrelated to sponsored clearing. |
| LD-C0158 Position Adjustment | A permitted correction or close-out of a position at the CCP that does not involve a new trade. | Clearing Broker Y instructs CCP Z to close out 30 long against 30 short lots held gross for Client A in the same series. | Position Transfer: moves positions between accounts; and Contract Adjustment: the venue changes the terms of a series after an event on the underlying, whereas a position adjustment changes the member's position, not the contract. |
| LD-C0159 Client Default | When a clearing broker declares its own client in default and takes action on that client's positions. | Client A misses several margin calls; Clearing Broker Y declares an event of default under their agreement and closes out Client A's futures. | Clearing Member Default: declared by the CCP against a member, not by a broker against its client. |
| LD-C0160 Margin Parameter Set | The current numbers a margin model runs on, updated more often than the model itself. | CCP Z publishes new margin rates for its equity index futures, effective next business day, without changing its model. | Margin Methodology: a methodology change alters the model; a parameter change only updates its inputs. |
| LD-C0161 Margin Run | One calculation of margin at a point in time, which produces the requirement figures. | CCP Z's midday run recalculates Clearing Broker Y's requirement on current prices; no call follows because the increase is below the threshold. | Intraday Margin Call: an intraday run is a calculation; a call is a demand that only some runs trigger. |
| LD-C0162 Margin Requirement Component | One of the pieces a margin requirement is broken into on a CCP or client statement. | CCP Z's statement to Clearing Broker Y shows base initial margin, a concentration add-on and premium margin as separate lines. | Initial Margin Requirement: initial margin is a kind of requirement; a component is a line inside one. |
| LD-C0163 Client Margin Uplift | The extra margin a clearing broker asks from a client on top of what the CCP requires. | Clearing Broker Y requires 1.2 times CCP Z's initial margin from Client A on its energy futures. | Margin Add-on: set by the CCP on the clearing member; the uplift is set by the broker on the client. |
| LD-C0164 Margin Portfolio | The group of positions whose risks are offset against each other when margin is calculated. | CCP Z margins Client A's index futures and index options in one portfolio, so the hedge reduces the requirement. | CCP Account: the account records positions and collateral; the portfolio is the scope over which offsets are allowed. |
| LD-C0165 Margin Call Terms | The rules on when a margin call is made, how big it must be and how fast it must be paid. | Client A's agreement with Clearing Broker Y sets one daily call, a minimum transfer amount and a deadline of noon local time. | Cut-off: a cut-off is a deadline in general; call terms say which deadline applies to margin calls and with which other rules. |
| LD-C0166 Margin Excess or Shortfall | How much more, or less, collateral is held than is required. | After the overnight run Client A has an excess at Clearing Broker Y, which Client A asks to be returned. | Margin Call: a shortfall becomes a call only after thresholds and minimum transfer amount; an excess is not a negative call. |
| LD-C0167 Collateral Haircut | The percentage knocked off an asset's market value when it is counted as collateral. | CCP Z values a ten-year government bond at its market value less a haircut, plus a currency haircut because the account's requirement is in another currency. | Concentration Limit: a haircut reduces the value of every unit; a limit caps how much of an asset counts at all. |
| LD-C0168 Concentration Limit | A limit on how much of one kind of asset can count towards margin. | CCP Z counts one issuer's bonds only up to a share of Clearing Broker Y's requirement; the rest is not valued. | Collateral Haircut: the haircut reduces each unit's value; the limit caps the quantity that counts. |
| LD-C0169 Collateral Instruction | A request to deliver, return or swap collateral, before anything has moved. | Client A asks Clearing Broker Y to substitute bonds for cash; Clearing Broker Y accepts and the substitution settles the next day. | Collateral Movement: the instruction is the request; the movement is the observed transfer. |
| LD-C0170 Price Alignment Amount | A small interest-like payment that goes with variation margin on cleared swaps but is not part of it. | CCP Z pays Clearing Broker Y a price alignment amount on its swap account with the daily settlement; Clearing Broker Y passes it to Client A. | Cash Collateral Interest: price alignment relates to variation margin; cash collateral interest remunerates cash held as initial margin. |
| LD-C0171 Cash Collateral Interest | Interest paid or charged on cash given as margin. | CCP Z pays Clearing Broker Y interest on euro cash posted as initial margin; Clearing Broker Y pays Client A interest on its cash under their agreement. | Price Alignment Amount: tied to variation margin, not to cash held as collateral. |
| LD-C0172 Default Fund Contribution | A clearing member's share of the CCP's shared pool for covering another member's default. | CCP Z recalibrates Clearing Broker Y's contribution to its listed derivatives default fund each month. | Initial Margin Requirement: margin covers the member's own positions; the default fund is shared among members. |
| LD-C0173 Margin Provider | The party that has to give margin. | Clearing Broker Y is the margin provider toward CCP Z and the margin taker toward Client A. | Collateral provider: usually the same party, but the collateral provider is defined by the arrangement and may be a third party pledging assets. |
| LD-C0174 Margin Taker | The party that requires margin and calls for it. | CCP Z is the margin taker toward Clearing Broker Y; Clearing Broker Y is the margin taker toward Client A. | Central Counterparty: a CCP is one kind of margin taker; a clearing broker is another, toward its clients. |
| LD-C0175 Published Fee Schedule | The public price list of a venue or CCP, which changes by circular on a set date. | CCP Z's fee schedule for its listed derivatives clearing service, version effective from the start of next quarter. | Client Pricing Terms: agreed with one client and confidential, not published. |
| LD-C0176 Client Pricing Terms | The prices a broker has agreed with one client for its services. | Client A's terms with Clearing Broker Y: a fees-plus rate per lot for listed clearing at CCP Z, with CCP fees passed on at cost. | Published Fee Schedule: public and the same for all who qualify, whereas client terms are negotiated. |
| LD-C0177 Fee Rate | One line of a price list: how much is charged for one kind of activity. | Venue V's rate per contract side for block trades in its index futures, for client accounts of non-members. | Fee Charge: the rate is the price; the charge is what is owed when the activity happens. |
| LD-C0178 Fee Incentive Programme | A scheme that lowers fees or pays rebates to those who meet agreed volume or quoting obligations. | Venue V's market-making programme for new options contracts, paying a rebate to registered members who meet quoting obligations each month. | Fee Rebate: the programme is the rule; the rebate is the amount owed when the rule is met. |
| LD-C0179 Pass-through Charge | A third-party fee that the broker recharges to its client. | Clearing Broker Y owes CCP Z a fee for Client A's lots and recharges it to Client A at cost on the monthly statement. | Client Clearing Fee: the broker's own fee for its service, as opposed to a third party's fee passed on. |
| LD-C0180 Bundled Execution and Clearing Fee | One combined price for executing and clearing the same trades. | Client A pays Broker X one rate per round turn that covers both executing and clearing its futures at CCP Z. | Client Execution Fee and Client Clearing Fee: charged separately; a bundled fee needs a split before it feeds either revenue figure. |
| LD-C0181 Regulatory Transaction Fee | A per-trade fee levied by a regulator or industry body, not by the venue or the CCP. | In a US regime, a per-round-turn assessment levied by a self-regulatory body on futures trades, collected by the clearing broker and passed on to Client A. | Exchange Fee Charge: charged by the venue operator, even if collected the same way. |
| LD-C0182 Fee Rebate | Money a venue, CCP or broker pays back after volume or quoting conditions are met. | Venue V owes Broker X a monthly rebate under its market-making programme; separately Broker X owes Client A a rebate for passing a volume tier. | Fee Adjustment: a waiver or correction changes one charge; a rebate rewards activity over a period under a programme. |
| LD-C0183 Fee Adjustment | A later change to a fee already charged, such as a correction, a waiver or a write-off. | Clearing Broker Y waives Client A's give-in fees for one month after a booking error and issues a credit against the original charges. | Fee Rebate: a rebate rewards activity under a programme, not a change to one charge. |
| LD-C0184 Fee Invoice | The bill that asks for payment of a set of fees. | CCP Z's monthly bill to Clearing Broker Y lists CCP clearing fees and Venue V's trading fees it collects for Venue V. | Cash Movement: a debit to the client's cash account in the broker's books settles the obligation; it is not a kind of invoice. |
| LD-C0185 Fee Collector | A party that collects a fee for someone else. | CCP Z collects Venue V's trading fees from Clearing Broker Y on its monthly bill and pays them to Venue V. | Creditor: the party the fee is owed to and who earns it. |
| LD-C0186 Activity Volume | How much was traded or cleared, in a stated unit and counting rule. | Client A's cleared volume at CCP Z last month in contract sides, single-counted, from the firm's records. | Position: volume counts activity over a period; a position is what is open at a point in time. |
| LD-C0187 Collateral Revenue | What the business earns from holding clients' collateral, reported separately from clearing fees. | Income from the difference between interest received on Client A's cash collateral and the interest paid to Client A, plus a fee for holding its bonds. | Clearing Revenue: fees for clearing trades; collateral revenue comes from the collateral, not the trades. |
| LD-C0188 Management Reporting Basis | The agreed rules that say how revenue figures are put together. | Revenue reported per contracting entity, by CCP clearing date, in euro, with exchange fees shown net and collateral income shown separately. | Accounting policy: management reporting may differ from the accounts and is not a statement of accounting treatment. |
| LD-C0189 Cost Perimeter | The agreed list of costs that are deducted to get contribution. | A first perimeter limited to venue and CCP fees not recharged and third-party brokerage and clearing. | Cost: the perimeter selects which costs count; cost is the expense itself. |
| LD-C0190 Regulatory Obligation | A duty the law puts on firms of a given status for given products from a given date, such as the duty to clear certain swaps. | Under a regime, financial counterparties above a clearing threshold must clear interest rate swaps of a stated class with other such counterparties from a phase-in date. | Regulatory Classification: the status that triggers the duty; and Rule Provision: one article or paragraph, whereas one obligation is often spread over several provisions with its own phase-in. |
| LD-C0191 Clearing Obligation | The legal duty for certain pairs of counterparties to clear certain swaps. | Two financial counterparties trading a euro interest rate swap of a mandated class and tenor must clear it at an eligible CCP; the same swap between an exempt pair need not be cleared. | Clearing eligibility: a CCP accepting a product for clearing does not make it mandatory; and 'cleared': a trade cleared voluntarily is not thereby subject to the obligation. |
| LD-C0192 Regulated Product Class | A legally defined group of derivatives that a rule refers to, such as 'euro fixed-to-floating interest rate swaps from 28 days to 50 years'. | A class of index credit default swaps, defined by index family, series and tenor, is declared subject to a clearing obligation. | Product Family: an economic grouping by asset class, underlying and contract form, set by industry practice, with no legal effect. Clearing Eligibility Schedule: what one CCP accepts. 'Traded on a trading venue' is a regulatory classification of an instrument, not a product class; UPI reference-data attributes, not the UPI itself, are a classification input. |
| LD-C0193 Phase-in Step | One of the dates at which a new rule starts to apply to one group of firms or products. | A clearing obligation applies first to clearing members, later to other financial counterparties, and last to smaller firms, each from its own date. | Rule Change status 'applicable': the change can apply to one group and not yet to another; and Regulatory Relief: a deferral granted after the fact. |
| LD-C0194 Rulebook | The full set of rules a CCP or exchange publishes for its members. | CCP Z's clearing rules, its procedures and its default management rules, each in a dated version, together form its rulebook. | Regulatory Regime: law of a jurisdiction; a CCP rulebook must comply with a regime but is not part of it. |
| LD-C0195 Regulatory Relief | An official statement that a rule will not be enforced, or does not apply, for some firms or products, usually for a time and on conditions. | Regulator R's staff states it will not recommend enforcement of a reporting requirement against swap dealers for a stated period while systems are updated. | Rule Change: an amendment of the rule itself; and Regulatory Interpretation: a reading of the rule, which grants nothing. |
| LD-C0196 Equivalence Decision | A formal decision that another country's rules are good enough for a stated purpose, which often lets its CCPs or venues be used. | Regime A deems Regime B's CCP rules equivalent until a stated date; CCPs of Regime B can then apply for recognition in Regime A. | Regulatory Authorisation (recognition): the status of one CCP; and qualifying CCP status, which governs capital treatment. |
| LD-C0197 Change Notice | The circular, notice or publication through which a change is announced. | CCP Z's circular announces three changes at once: a new haircut table from one date, a new cut-off from another, and a fee change still subject to approval. | Rule Change: the change it announces, which has its own status and dates; one circular is often several changes. |
| LD-C0198 Consultation | The period during which a regulator or CCP asks the market to comment on a proposed rule. | Regulator R publishes a consultation paper on changes to segregation disclosures, open for comment for three months. | Adopted rule: a consultation is not law and must always be shown as 'not yet in force'; and Change Notice: the consultation paper is the document, the consultation is the stage. |
| LD-C0199 Rule Change Approval | The regulator's sign-off of a CCP's or exchange's rule change, or the CCP's own certification where that is how the regime works. | CCP Z announces a margin model change 'subject to regulatory approval'; the approval comes two weeks later and the change applies from the next clearing date. | Rule Change status 'adopted' for a law, which needs no separate approval; and Change Impact Assessment, which is the firm's own review. |
| LD-C0200 Change Impact Assessment | The firm's written view of what a rule change touches and what it will do about it. | For CCP Z's new give-up deadline, the assessment lists the give-up process and the client documents as affected, rates confidence high, and decides to act before the application date. | Rule Change: the published change itself; and Regulatory Interpretation: one reading inside the assessment where the text is unclear. |
| LD-C0201 Regulatory Interpretation | Someone's written reading of what a rule means, kept separate from the rule itself. | An industry association reads a new active account condition one way; the firm's signed-off reading for its own case is recorded separately, in the internal layer. | Rule Provision, including official guidance: guidance is issued by the authority; an interpretation is a reading by anyone, including the firm. And Regulatory Relief, which grants something. |
| LD-C0202 Regulatory Authorisation | An official licence or registration that lets a firm, CCP or venue do a stated activity in a jurisdiction. | The legal entity acting as Clearing Broker Y is registered in the US as a futures commission merchant. | Counterparty Regulatory Status: a counterparty category (financial or not, above or below a threshold), not a licence. Qualifying CCP status is a capital-treatment classification that follows from authorisation or recognition, recorded as a separate Regulatory Classification. |
| LD-C0203 Regulatory Authority | A public body that makes or enforces financial rules, such as a market supervisor or a central bank. | Regulator R supervises CCP Z, approves its rule changes and publishes guidance on the clearing obligation. | CCP or venue operator: they issue rulebooks but do not hold this role. |
| LD-C0204 Regulatory Reporting Role | The party a regulation names as responsible for a given report on a trade. | For Client A's execution on Venue V, Executing Broker X is the executing entity in the transaction report, while Member M entered the order and Clearing Broker Y cleared it. | Executing Broker: the party that serves the client; the reporting role follows the regime's own test and may fall on another party. |
| LD-C0205 Source Record | One source's version of a trade, position or amount, with its own references and status. | Client A's 100-lot trade appears in the firm's clearing books and in CCP Z's trade register: two source records of one trade. | Business object (Trade, Position): the object exists once; each source holds its own record of it. |
| LD-C0206 CCP Report | The daily (or intraday) statement a CCP sends a clearing member about its trades, positions, margin and payments. | CCP Z's end-of-day position report for Clearing Broker Y's client omnibus account, for clearing date D. | Source Record in general: the firm's own books and broker statements are records too, but not CCP reports. |
| LD-C0207 Reconciliation Break | A mismatch between two records that should agree. | The firm's books show 100 lots long for Client A at CCP Z; the CCP position report shows 60: a 40-lot quantity break on that account and clearing date. | Operational Exception: the break is the difference; the exception is the situation someone must act on, if any. |
| LD-C0208 Position Reconciliation | Checking that the positions in our books match the CCP's (or the client's) for each account and series on a clearing date. | Operations compares Clearing Broker Y's long and short positions per series in its client omnibus account at CCP Z with CCP Z's position report for date D. | Trade reconciliation: compares individual trades; positions can match while trades differ, and the reverse. |
| LD-C0209 Exception Case | The ticket that tracks who is fixing an exception, what was done and when it was closed. | One case groups the three give-up lines to Clearing Broker Y that lapsed on the same clearing date because the give-up reference was wrong. | Operational Exception: the exception is the situation; the case is the record of handling it. |
| LD-C0210 Settlement Fail | An amount or asset that should have been paid or delivered by the deadline and was not. | Client A's variation margin payment to Clearing Broker Y due by the client deadline on date D is still unpaid at the deadline: settlement fail. | An overdue Margin Call: for a call met in cash, 'overdue' on the call and 'failed' on the resulting obligation are two views of one situation, counted once. Also not a rejected or lapsed give-up or a reconciliation break. |
| LD-C0211 Netted Settlement Obligation | One payment that covers many amounts due between the same two parties on the same day in the same currency. | CCP Z nets Clearing Broker Y's variation margin, option premium and fees in euro for the cycle into one amount Y must pay. | Settlement Obligation in general: a single obligation has one purpose; the netted one combines several and must not hide them. |
| LD-C0212 Payment Instruction | The order given to a bank or system to make a payment. | Clearing Broker Y's settlement bank receives CCP Z's direct debit for the net euro amount of the morning cycle. | Cash Movement: the instruction asks for the payment; the cash movement is the payment that happened. |
| LD-C0213 Settlement Account | The bank or delivery account a party uses to pay or receive what it owes. | Clearing Broker Y settles its sterling obligations to CCP Z through its cash account at an approved settlement bank. | CCP Account: positions and margin are recorded in the CCP account; cash moves through the settlement account. |
| LD-C0214 Settlement Deadline | The latest time a payment or delivery must reach the other side. | CCP Z requires its morning cash call in euro to be settled by a stated local time on the clearing date. | Margin Call: the call is the demand; the settlement deadline is the time by which the resulting obligation must be met. |
| LD-C0215 Firm Cut-off | An earlier deadline the firm gives clients or its own teams so that the market deadline can be met. | Clearing Broker Y asks clients to send contrary exercise instructions well before CCP Z's exercise deadline on expiry day. | Market cut-off (set by a CCP, venue or payment system): binds the member; the firm cut-off binds the client or team. |
| LD-C0216 Expiry | The day a contract series ends and every open position in it is closed out. | The March series of a futures contract at Venue V expires; Client A's remaining positions go to final settlement. | Last trading day: a date of the contract specification; expiry is the event, which may fall on a later day. |
| LD-C0217 Exercise | The option holder using its right to buy or sell, on instruction or automatically at expiry. | Client A's in-the-money calls at CCP Z are exercised automatically at expiry because no contrary instruction was received. | Assignment: exercise is the long side's act; assignment is its allocation to the short side. |
| LD-C0218 Exercise Instruction | The holder's order to exercise an option, or to override what would happen automatically at expiry. | Client A tells Clearing Broker Y not to exercise 10 calls that are just in the money, before Y's firm cut-off on expiry day. | Exercise: the instruction is the request; the exercise is the event registered by the CCP. |
| LD-C0219 Assignment | The CCP and then the clearing broker deciding which short option holders must honour an exercise. | CCP Z assigns 50 exercised puts to Clearing Broker Y's client account; Y assigns 20 of them to Client B under its allocation method. | Exercise: assignment is the short side's obligation that follows an exercise by someone else. |
| LD-C0220 Final Settlement | Closing an expiring position for good, either by paying the difference in cash or by delivering the underlying. | Client A's remaining long futures in the expiring series are cash settled against the final settlement price published by Venue V. | Variation margin: daily settlement while the position is open; final settlement closes it at the end. |
| LD-C0221 Delivery Notice | The notice that starts the physical delivery of a futures contract. | Client B, short a physically delivered commodity future at CCP Z, gives notice of intention to deliver through Clearing Broker Y on a notice day. | Exercise Instruction: exercise is an option holder's right; a delivery notice starts the delivery of a future. |
| LD-C0222 Trade Amendment | A change to, or early ending of, a trade that already exists, recorded as a new event that points to the original. | Clearing Broker Y corrects the client reference on a registered trade at CCP Z; a cleared swap of Client A is partially terminated, reducing its notional. | Execution Correction: corrects a venue execution before clearing; a trade amendment acts on the registered trade. |

## Values

Draft value lists carried by a concept (detailed taxonomies remain Phase 3 work). Values are not concepts and carry no IDs.

| Concept | Values (draft) |
|---|---|
| LD-C0077 Investment Fund | umbrella fund; sub-fund or compartment; standalone fund |
| LD-C0078 Authorised Representative | investment manager; authorised trader; introducing broker or introducer (transmits orders); other agent under power of attorney |
| LD-C0082 Account Identifier | CCP account number; provider's internal account number; give-up reference or mnemonic; venue trading account code; client's own account reference |
| LD-C0083 Parent Entity | direct parent; ultimate parent |
| LD-C0088 Client Regulatory Category | retail client; professional client (per se); professional client (elective, on request); eligible counterparty; unknown; other regimes' customer categories (to verify per regime) |
| LD-C0089 Counterparty Regulatory Status | financial counterparty above the clearing threshold (per asset class and calculation period); financial counterparty below the clearing threshold; non-financial counterparty above the clearing threshold; non-financial counterparty below the clearing threshold; third-country entity; eligible contract participant (US); US person (CFTC cross-border meaning, to verify); unknown |
| LD-C0090 Client Account | clearing client account; execution client account (records executions and charges, no positions); sub-account (subdivision for allocation or reporting) |
| LD-C0092 Settlement or Custody Agent | settlement bank; custodian; triparty agent |
| LD-C0093 Identifier Scheme | ISIN; UPI; CFI (a classification code, not an identity); MIC (venue and segment); LEI (with its registration status kept as reference data); UTI; venue product code; CCP product code; venue order identifier; client order identifier (issued by the broker or client); venue execution or trade identifier (unique per venue and session); CCP trade identifier; venue member and trader identifiers; CCP member codes; executing broker codes used on give-ups; CCP account numbers; give-up reference or account mnemonic (per venue or CCP); the firm's own party and account codes |
| LD-C0095 Listed Strategy | legs: each named by leg instrument, direction relative to the strategy and ratio |
| LD-C0097 Underlying | equity; equity index; interest rate or benchmark; bond or bond basket; currency pair; commodity; listed derivative; volatility or other index; credit |
| LD-C0098 Key-Date Rule | key dates: first trading day; last trading day; expiry day; last exercise day; first notice day; last notice day; first delivery day; last delivery day (delivery period); due date; final settlement day; settlement date; the time and consequence of an exercise or notice deadline belong to the Cut-off read against that day |
| LD-C0099 Contract Adjustment | strike and multiplier adjustment; deliverable change; underlying replacement; early settlement or termination |
| LD-C0102 Trading Session | pre-open; opening auction; continuous trading; closing auction; evening or overnight session; negotiated-trade registration window |
| LD-C0103 Settlement Price | daily settlement price; final settlement price; provisional; corrected |
| LD-C0104 Processing Window | intraday cycle; end-of-day cycle; give-up and take-up window; late give-up or correction window; exercise window; payment cycle |
| LD-C0105 Service Component | order execution; give-up processing; take-up of trades given in; average pricing; allocation; clearing and position maintenance; margin and collateral handling; exercise and delivery handling; delegated regulatory reporting |
| LD-C0108 Access Agreement | venue admission or membership agreement; CCP clearing membership agreement; direct electronic access agreement; third-party execution agreement; sponsored clearing or clearing agent agreement |
| LD-C0109 Access Onboarding | application; due diligence; legal documentation; requirements met; connectivity and conformance testing; static and account set-up; go-live; withdrawn |
| LD-C0110 Access Requirement | regulatory; financial; operational and technical; legal and documentary; staff qualification |
| LD-C0111 Connectivity Route | direct, co-located; direct, remote; through an independent software vendor or service bureau; through another member's infrastructure; order-routing network |
| LD-C0112 Direct Electronic Access Arrangement | direct market access; sponsored access |
| LD-C0115 Sponsored Clearing Arrangement | intermediary form: sponsoring clearing member; clearing agent (where the rulebook provides, to verify) |
| LD-C0119 Pre-trade Control Check | pass; reject; hold for manual review |
| LD-C0123 Exchange for Related Position | exchange for physical; exchange for swap; exchange of options for options; other venue-defined related-position types |
| LD-C0125 Execution Correction | cancellation (bust); price adjustment; quantity correction; correction of non-economic details |
| LD-C0129 Allocation Line | route: internal; give-up; allocation status: pending; booked; amended; cancelled |
| LD-C0131 Give-up Line | status: pending; accepted in full; accepted in part; rejected; lapsed (not taken up by the deadline; the quantity stays with the giving member); cancelled; reversed; unknown |
| LD-C0136 Take-up | outcome: accepted in full; accepted in part; rejected; non-acceptance reason (seed values for Phase 3): unknown account or give-up reference; no give-up agreement; clearing limit exceeded; product not covered; price or quantity mismatch; submitted after the deadline (only when actively rejected for lateness) |
| LD-C0137 Submission Acceptance | outcome: accepted; rejected; non-acceptance reason (seed values for Phase 3): clearing limit exceeded; product not eligible; missing or invalid account; no execution agreement for cleared trades |
| LD-C0141 Clearing Submission | new trade; after allocation of a block; backload of an existing bilateral trade; resubmission after rejection |
| LD-C0146 Client Omnibus Account | net omnibus (EU, UK); gross omnibus (EU, UK); US futures customer account (Section 4d segregation, to verify); US foreign futures customer account (Part 30 secured amount, to verify); US cleared swaps customer account (Part 22, LSOC, to verify) |
| LD-C0148 Indirect Client Account | basic omnibus indirect client account (EU); gross omnibus indirect client account (EU); listed and OTC variants (separate EU rules) |
| LD-C0150 Segregation Election | omnibus (net or gross where offered); individual; indirect: basic or gross omnibus (EU); no election recorded |
| LD-C0151 Listed Position | long; short; net; position effect on gross accounts: open, close |
| LD-C0153 Position Transfer | trigger: client changes clearing broker; trigger: account correction; trigger: clearing member exit or restructuring; scope: within one member, between members |
| LD-C0155 Porting | outcome: ported, closed out, partly ported; leg: positions, collateral |
| LD-C0156 Back-up Clearing Member | named in advance with pre-agreement; named in advance without pre-agreement; agreed at default |
| LD-C0158 Position Adjustment | long-short close-out; open-close correction; other rule-defined adjustment |
| LD-C0159 Client Default | outcome: close-out; transfer; hedge |
| LD-C0160 Margin Parameter Set | margin rates per contract; risk parameter file (SPAN-type); scenario set (VaR-type); liquidity or concentration factors; intraday call thresholds |
| LD-C0161 Margin Run | scheduled end-of-day; scheduled intraday; ad hoc |
| LD-C0162 Margin Requirement Component | component type: base initial margin; add-on (for example concentration, liquidity, wrong-way risk); premium or net liquidation value margin; delivery margin; variation margin is a separate kind of requirement, not a component, even when CCP statements show it on a line next to the components |
| LD-C0163 Client Margin Uplift | basis: mandated minimum (regime or CCP rule); discretionary (broker policy or client terms); form: multiplier; fixed add-on; own model; none (pure replication, only where no mandated minimum applies) |
| LD-C0164 Margin Portfolio | within an account; liquidation group; per client in a gross account; cross-product or cross-service; cross-CCP under an agreement |
| LD-C0165 Margin Call Terms | call frequency and run types; deadline: a Settlement Deadline (a kind of Cut-off) with calendar, time zone and consequence; threshold; minimum transfer amount; rounding; dispute process |
| LD-C0166 Margin Excess or Shortfall | excess; shortfall; fully covered |
| LD-C0167 Collateral Haircut | asset haircut; currency mismatch haircut; additional wrong-way or concentration haircut; client-tier haircut set by the clearing broker |
| LD-C0168 Concentration Limit | per issuer; per asset class; per currency; per security issue; absolute cap; share of requirement |
| LD-C0169 Collateral Instruction | delivery; return of excess; substitution; reallocation between accounts |
| LD-C0170 Price Alignment Amount | price alignment interest (collateralised-to-market); price alignment amount (settled-to-market) |
| LD-C0171 Cash Collateral Interest | tier: CCP to clearing member; clearing member to client; direction from the observing party: received; paid; stage: accrued; due; paid |
| LD-C0172 Default Fund Contribution | required contribution; contribution held; replenishment after use |
| LD-C0173 Margin Provider | tier: see the clearing tier vocabulary |
| LD-C0174 Margin Taker | tier: see the clearing tier vocabulary |
| LD-C0175 Published Fee Schedule | issuer kind: trading venue operator; CCP; regulator or self-regulatory body |
| LD-C0176 Client Pricing Terms | pricing form: all-in; fees-plus; pass-through rule: at cost; with mark-up; not passed on |
| LD-C0177 Fee Rate | scope: product family, contract specification or clearing contract; trading venue or venue segment; strategy versus leg; flexible versus standard series; block or negotiated trade versus on-book; account type or segregation level; service nature (for venue, CCP and regulatory fees) or service component (for the firm's own client charges); charge basis: per contract side; per round turn; per ticket or allocation; per notional; percentage of premium; periodic |
| LD-C0178 Fee Incentive Programme | kind: liquidity provider or market making; volume tier; new product launch; client volume tier |
| LD-C0179 Pass-through Charge | recharge treatment: at cost; with mark-up |
| LD-C0182 Fee Rebate | direction from the firm's view: received from a venue or CCP; granted to a client |
| LD-C0183 Fee Adjustment | kind: correction; cancellation; waiver; credit; dispute outcome; write-off |
| LD-C0184 Fee Invoice | form: invoice; client statement (periodic statement listing charges) |
| LD-C0186 Activity Volume | unit: contract sides; round turns; tickets or trades; notional; counting basis: single; double; stage: executed; cleared (open quantities are a Position, not activity); executed side: venue-facing; client-facing; strategy counting: per strategy; per leg; execution method scope: on-book only; including negotiated trades; source: published by a venue or CCP; the observing firm's records |
| LD-C0187 Collateral Revenue | stream: interest on cash collateral; non-cash collateral fees; other |
| LD-C0188 Management Reporting Basis | pass-through presentation: gross; net; rebate presentation: gross; netted |
| LD-C0189 Cost Perimeter | candidate cost categories (no default perimeter): venue and CCP fees not recharged; third-party brokerage; third-party clearing; connectivity and market data; funding and collateral; default fund funding; introducer or fee-sharing payments; attributed shared cost |
| LD-C0190 Regulatory Obligation | clearing; trading on a venue (derivatives trading obligation); active account at an EU CCP; transaction and trade reporting; offer of client segregation and disclosure of its protection and cost; fair and transparent commercial terms for clearing services; position limits and position reporting; best execution; controls on direct electronic access and algorithmic trading; client information duties; risk mitigation for uncleared trades (out of current scope) |
| LD-C0192 Regulated Product Class | clearing obligation class; trading obligation class; active account category; US future, swap or security-based swap; security futures product (US); traded on a trading venue (EU) |
| LD-C0194 Rulebook | rules; procedures; clearing conditions; trading conditions; contract terms; default management rules; fee rules |
| LD-C0195 Regulatory Relief | exemption; no-action relief; transitional measure; supervisory forbearance; deferral; exemptive order |
| LD-C0196 Equivalence Decision | equivalence; comparability determination; substituted compliance; time-limited equivalence |
| LD-C0197 Change Notice | consultation paper; final report or draft technical standard; published legal act; circular or market notice; clearing advisory; rule filing or self-certification; official guidance or Q&A; press release (low evidence) |
| LD-C0198 Consultation | open; closed; feedback published; withdrawn |
| LD-C0199 Rule Change Approval | approval requested; self-certified; approved; non-objection; validated; stayed; rejected; not required |
| LD-C0200 Change Impact Assessment | impact type: scope, timing, data, legal effect, cost, process, documentation, client communication; decision: act, plan, monitor, ignore; status: draft, under review, signed off, closed; confidence: high, medium, low |
| LD-C0201 Regulatory Interpretation | author kind: authority statement, industry association, external counsel, firm; status: draft, signed off, superseded |
| LD-C0202 Regulatory Authorisation | CCP authorisation; third-country CCP recognition (with tier where applicable); derivatives clearing organisation registration or exemption; futures commission merchant registration; swap dealer registration; designated contract market or swap execution facility designation; regulated market, MTF or OTF authorisation; investment firm or bank authorisation; qualifying CCP status (for capital treatment) |
| LD-C0203 Regulatory Authority | legislator; supervisory authority; central bank acting as supervisor; supranational authority; self-regulatory organisation (can issue rule provisions and levy fees) |
| LD-C0204 Regulatory Reporting Role | executing entity in a transaction report; reporting counterparty; entity responsible for reporting |
| LD-C0205 Source Record | firm books (by function: front office, middle office, clearing back office); CCP report; venue report; executing broker statement; clearing broker statement; settlement bank or payment system statement; client record or instruction |
| LD-C0206 CCP Report | trade register; give-up and take-up report; position report; exercise and assignment report; delivery report; margin report; collateral report; cash settlement statement |
| LD-C0207 Reconciliation Break | missing in one source; quantity difference; price or amount difference; account or attribution difference; status difference; date difference; open; under investigation; explained, awaiting correction; resolved; written off where allowed |
| LD-C0209 Exception Case | open; assigned; in progress; waiting on counterparty; resolved; closed |
| LD-C0210 Settlement Fail | end: settled late; cancelled; replaced by close-out or default procedure; still open |
| LD-C0212 Payment Instruction | created; released; rejected; cancelled; executed |
| LD-C0213 Settlement Account | cash settlement account; delivery account; collateral account (custody, pledge or triparty) |
| LD-C0214 Settlement Deadline | CCP payment deadline (per cycle); payment system closing time; client payment deadline; delivery deadline |
| LD-C0216 Expiry | outcome for the position: final settlement (cash or delivery); exercised; assigned; abandoned |
| LD-C0217 Exercise | exercise at expiry (automatic or instructed); early exercise (American style) |
| LD-C0218 Exercise Instruction | exercise; do not exercise (abandon); contrary instruction against automatic exercise |
| LD-C0219 Assignment | CCP to member; member to client; random allocation; pro rata allocation; other disclosed method |
| LD-C0220 Final Settlement | cash settlement; physical delivery |
| LD-C0221 Delivery Notice | notice of intention to deliver; delivery allocation to longs |
| LD-C0222 Trade Amendment | non-economic correction; economic change; partial termination; full termination (unwind) |
