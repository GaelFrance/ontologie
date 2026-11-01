# Concept annotations

Status: Draft. Companion to the [concept catalogue](foundation.md), which stays the single index of IDs and definitions.

This page holds per-concept data that does not fit the catalogue's five-column table: specialisations, aliases, resolution flags, usage notes, required context, French labels, priorities and standard alignments. It is kept separate because the agent hub currently parses the catalogue table by cell position. When detailed concept fiches are written (template fields `parents`, `aliases`, `required_context`, `label_fr`, `alignments`, `resolution`), the content below moves into them and this page is retired.

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

## Labels, priority and alignment

French labels are proposed secondary labels; English remains canonical (open question on making them mandatory). Priority is given for concepts added by the 2026-11 review.

| Concept | French label (proposed) | Priority | Source reviews | Standard alignment (to verify) |
|---|---|---|---|---|
| LD-C0001 Party | Partie | Phase 1 | — | FIBO party concepts |
| LD-C0002 Legal Entity | Entité juridique | Phase 1 | — | ISO 17442 LEI |
| LD-C0003 Party Role | Rôle de partie | Phase 1 | — | FIBO party-in-role; CDM party role |
| LD-C0004 Client | Client | Phase 1 | — | EMIR Art. 2(15); MiFID II Art. 4(1)(9) |
| LD-C0005 Broker | Courtier | Phase 1 | — | — |
| LD-C0006 Executing Broker | Courtier exécutant | Phase 1 | — | — |
| LD-C0007 Clearing Member | Membre compensateur | Phase 1 | — | CCP rulebooks |
| LD-C0008 Central Counterparty | Contrepartie centrale | Phase 1 | — | EMIR Art. 2(1) |
| LD-C0009 Trading Venue | Plateforme de négociation | Phase 1 | — | ISO 10383 MIC |
| LD-C0010 Account | Compte | Phase 1 | — | — |
| LD-C0011 Segregation Model | Modèle de ségrégation | Phase 1 | — | EMIR Art. 39 |
| LD-C0012 Agreement | Convention | Phase 1 | — | — |
| LD-C0013 Product Family | Famille de produits | Phase 1 | — | ISO 10962 CFI; ISO 4914 UPI; ISDA OTC taxonomy |
| LD-C0014 Instrument | Instrument | Phase 1 | — | ISO 6166 ISIN |
| LD-C0015 Business Date | Date métier | Phase 1 | — | — |
| LD-C0016 Order | Ordre | Phase 1 | — | FIX order messages |
| LD-C0017 Execution | Exécution | Phase 1 | — | FIX execution report |
| LD-C0018 Trade | Opération (trade) | Phase 1 | — | CDM trade; ISO 23897 UTI |
| LD-C0019 Transaction | Transaction | Phase 1 | — | — |
| LD-C0020 Allocation | Allocation | Phase 1 | — | — |
| LD-C0021 Average Price Group | Groupe de prix moyen | Phase 1 | — | — |
| LD-C0022 Give-up / Take-up Process | Processus de give-up / take-up | Phase 1 | — | — |
| LD-C0023 Clearing Acceptance | Acceptation en compensation par la CCP | Phase 1 | — | — |
| LD-C0024 Novation | Novation | Phase 1 | — | — |
| LD-C0025 Lifecycle Event | Événement de cycle de vie | Phase 1 | — | CDM business events |
| LD-C0026 Position | Position | Phase 1 | — | — |
| LD-C0027 Portfolio | Portefeuille | Phase 1 | — | — |
| LD-C0028 Settlement Obligation | Obligation de règlement | Phase 1 | — | — |
| LD-C0029 Cash Movement | Mouvement d'espèces | Phase 1 | — | — |
| LD-C0030 Operational Exception | Exception opérationnelle | Phase 1 | — | — |
| LD-C0031 Fee Charge | Frais facturable | Phase 1 | — | — |
| LD-C0032 Fee Schedule | Barème de frais | Phase 1 | — | — |
| LD-C0033 Client Execution Fee | Frais d'exécution client | Phase 1 | — | — |
| LD-C0034 Client Clearing Fee | Frais de compensation client | Phase 1 | — | — |
| LD-C0035 Executing Broker Brokerage Charge | Courtage du courtier exécutant | Phase 1 | — | — |
| LD-C0036 Exchange Fee Charge | Frais de marché | Phase 1 | — | — |
| LD-C0037 CCP Fee Charge | Frais de CCP | Phase 1 | — | — |
| LD-C0038 Commission | Commission | Phase 1 | — | — |
| LD-C0039 Revenue | Revenu | Phase 1 | — | — |
| LD-C0040 Cost | Coût | Phase 1 | — | — |
| LD-C0041 Execution Revenue | Revenu d'exécution | Phase 1 | — | — |
| LD-C0042 Clearing Revenue | Revenu de compensation | Phase 1 | — | — |
| LD-C0043 Margin Requirement | Exigence de marge | Phase 1 | — | PFMI Principle 6 |
| LD-C0044 Initial Margin Requirement | Exigence de marge initiale | Phase 1 | — | EMIR Art. 41 |
| LD-C0045 Variation Margin Requirement | Exigence de marge de variation | Phase 1 | — | — |
| LD-C0046 Margin Call | Appel de marge | Phase 1 | — | — |
| LD-C0047 Collateral | Garantie constituée | Phase 1 | — | Directive 2002/47/EC |
| LD-C0048 Collateral Asset | Actif de garantie | Phase 1 | — | — |
| LD-C0049 Collateral Movement | Mouvement de garantie | Phase 1 | — | — |
| LD-C0050 Reconciliation | Rapprochement | Phase 1 | — | — |
| LD-C0051 Clearing Service | Service de compensation | P1 | 02, 03, 04, 05, 06, 07, 08 | CCP rulebooks; EMIR Art. 14 and 15 (authorisation and its extension) |
| LD-C0052 Service Offering | Offre de service | P1 | 05, 08 | FIBO products and services |
| LD-C0053 Clearing Member Acceptance | Acceptation par le membre compensateur | P1 | 01, 02, 03, 05, 08 | FIXML allocation and claim flows; FpML clearing status; MiFIR Art. 29(2) and Delegated Regulation (EU) 2017/582; CFTC 1.73 and 1.74 |
| LD-C0054 CCP Interposition | Interposition de la CCP | P1 | 02, 03, 06, 08 | PFMI Principle 1; CDM and FpML clearing events |
| LD-C0055 Give-up Agreement | Convention de give-up | P1 | 01, 02, 08 | FIA International Uniform Brokerage Execution Services ("Give-Up") Agreement; a revised FIA standard was in public comment in 2026, version to verify |
| LD-C0056 Client Clearing Agreement | Convention de compensation client | P1 | 03, 02, 06, 08 | ISDA/FIA client cleared OTC derivatives addendum; FCM customer agreements (titles to verify) |
| LD-C0057 Clearing Broker | Courtier compensateur | P1 | 02, 05, 01, 08 | — (FCM is a contextual US alias) |
| LD-C0058 Trading Venue Member | Membre de plateforme de négociation | P1 | 01 | MiFID II "member or participant" (Art. 53 for regulated markets); FIX party roles |
| LD-C0059 Market Access Arrangement | Dispositif d'accès au marché | P1 | 05, 02, 03, 06, 01 | EMIR Art. 4(3); MiFIR Art. 30; Delegated Regulations (EU) 2017/2154 and 2017/2155; MiFID II Art. 4(1)(41); PFMI Principle 19 |
| LD-C0060 Allocation Instruction | Instruction d'allocation | P1 | 01, 02 | FIX allocation instruction and allocation report messages; CFTC 1.35 bunched orders |
| LD-C0061 Order Handling Channel | Canal de traitement des ordres | P1 (sponsor decision 2026-11-01) | 01, 05 | MiFID II Art. 4(1)(39), 4(1)(41), 17(5); Delegated Regulation (EU) 2017/589; FIX handling-instruction fields |
| LD-C0062 Contract Specification | Spécification de contrat | P1 | 07, 08, 01, 05 | FIX security definition; venue contract specifications |
| LD-C0063 Rule Provision | Disposition de règle | P1 | 06, 05, 08, 02 | ELI for EU acts |
| LD-C0064 Rule Change | Changement de règle | P1 | 06, 08, 02, 05 | CFTC Part 40 rule submissions (instances) |
| LD-C0065 Cut-off | Heure limite | P1 | 07, 08 | CCP and venue deadlines (instances) |
| LD-C0066 Business Calendar | Calendrier d'activité | P1 | 07 | Venue, CCP and payment-system calendars (instances) |
| LD-C0067 Regulatory Regime | Régime réglementaire | P1 | 06, 05, 08 | ISO 3166 for jurisdictions |
| LD-C0068 Regulatory Classification | Classification réglementaire | P1 | 06 | EMIR Art. 2(8) and (9), 10, 25; CRR Art. 4(1)(88) |
| LD-C0069 CCP Account | Compte CCP | P1 | 02, 07, 04 | EMIR Art. 39; CFTC customer account classes |
| LD-C0070 Margin Methodology | Méthodologie de marge | P1 | 04, 05 | PFMI Principle 6; EMIR Art. 41; Delegated Regulation (EU) 153/2013; CFTC 39.13 |
| LD-C0071 Collateral Arrangement | Convention de garantie financière | P1 | 04, 08 | Directive 2002/47/EC; MiFID II Art. 16(10); ISDA credit support documentation as bilateral analogue; CDM collateral |
| LD-C0072 Collateral Eligibility Schedule | Barème d'éligibilité des garanties | P1 | 04 | EMIR Art. 46; Delegated Regulation (EU) 153/2013 annexes; CDM eligible collateral |
| LD-C0073 Commercial Group | Groupe commercial | P1 | 05, 06 | Contrast with public legal-entity relationship data |
| LD-C0074 Contribution | Contribution | P1 (management revenue priority) | 05, 04, 06 | — |
