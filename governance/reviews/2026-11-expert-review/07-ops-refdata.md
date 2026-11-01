# Review 07 — Post-trade operations and reference data (v2)

Specialty: reference data, identifiers, calendars and dates, cut-offs, status models, records and versioning, reconciliations, breaks and exceptions; AG-006 / UC-006 needs. v1 temporary IDs are kept stable; withdrawn ones are listed, never reused.

## 1. Verdict

The principles are right (P5 records vs trade identity, P10 unknown ≠ not applicable, date roles and calendars in architecture.md) but no concept, relationship or convention carries them. AG-006 cannot answer EV-006-Q01 ("not successfully given up": per which source, as of when, against which cut-off?), AG-004 cannot state deadlines (EV-003-Q05), AG-002 cannot reason about a calendar change (EV-001-Q05). v2 is leaner than v1: **six concepts**, **one time convention** for docs/modelling-guidelines.md, and **governed vocabularies** (date roles, statuses, break and exception types) instead of concept trees.

## 2. Corrections to existing items

| ID | Issue | Proposed change | Sev. | Conf. |
|---|---|---|---|---|
| LD-C0013 Product | "Product" means a classification family, a venue's listed contract (exchange product code) or the firm's service offering; the definition covers only the first. | State the scope: "Classification grouping of instruments or trades sharing economic and contractual characteristics, independent of any venue; not a venue's listed contract (NEW-REF-03) and not a service offering." Support the label "Derivative Product" (review 05). Make "product" an *ambiguous* alias (NEW-A-03). | High | High |
| LD-C0014 Instrument | "Can be traded or contracted" makes every bespoke OTC trade an instrument. | "Standardised derivative specification, identifiable independently of any counterparty pair or single trade, at the level at which it is listed, identified and held. For listed derivatives this is the series (contract + expiry, + strike and call/put for options). A bespoke OTC trade is not an instrument; it carries its own economic terms and a product identifier (UPI)." This is a meaning change, justified by LD-A0016. Keep the type Entity. | High | High |
| LD-C0015 Business Date | A date only has meaning with a role; venue trade date, calendar date and CCP clearing date can all differ. | "Date assigned to a business object or event under a stated **date role**, resolved against a named **business calendar** and time zone." Date role (governed vocabulary, §4) and calendar (NEW-REF-05) become mandatory qualifiers. | High | High |
| LD-C0030 Operational Exception | Ops manage exceptions as cases (owner, ageing, resolution); LD-R0024 also makes it absorb reconciliation discrepancies. | Meaning change, agreeing with review 08: "**Case** raised when an expected operational outcome, rule or cut-off is not met for identified business objects, with category, owner, priority and a lifecycle (raised, assigned, resolved, closed). It is distinct from the break, rejection or event that revealed it." Retype from State to Entity. | High | High |
| LD-C0050 Reconciliation | Does not say what is compared or what comes out. | Append: "…between source records (NEW-OPS-02) of a stated reconciliation type (trade, give-up, position, cash, margin, collateral, fee), scope, business date, matching keys and tolerance; produces matches and breaks." | Med | High |
| LD-R0024 | `Reconciliation identifies Operational Exception` merges a break with an exception. | Explicit retarget with migration note: `LD-C0050 identifies NEW-OPS-04`, plus `NEW-OPS-04 may_raise LD-C0030`. Keep the existing caveat ("a break does not prove underlying trade failure"). The ID is unchanged. | High | High |
| LD-C0010 Account | Each maintaining party knows the account differently (internal, CCP, executing broker, give-up reference); no lifecycle. | Append: "An account has identifiers per maintaining party, a lifecycle status (opened, active, suspended, closed) and an effective period. Correspondence between accounts maintained by different parties is an explicit, time-bounded mapping, not identity." A give-up reference or mnemonic is an *identifier* that points to the receiving member's account; it is not an account in its own right. | Med | High |
| LD-C0025 Lifecycle Event | No time semantics. | Append: "Carries occurrence time, effective time and recording time, plus business dates by role. Corrections and cancellations are events that reference the original; nothing is deleted." | Med | High |
| LD-C0026 Position | "As-of time" is too loose for ops (start/end of day, CCP vs internal, before/after give-up). | Required qualifiers: as-of business date and cycle (start-of-day, intraday, end-of-day), asserting source (internal or CCP statement), and gross/net basis. Identity key as in reviews 02/08 (account × instrument × CCP service). | Med | High |
| LD-C0002 Legal Entity | Agents treat an LEI as identifying a client, group or account. | Usage note: "An LEI (ISO 17442) identifies a legal entity (GLEIF also registers certain international branches — to verify). It never identifies an account, desk or commercial group. GLEIF Level 2 parent data describes accounting consolidation, not a commercial group." | Low | Med-High |

## 3. Answers to open ambiguities

**LD-A0015 Business date.** *Industry answer:* every date has a role, resolved against a named calendar and time zone, with event timestamps kept in UTC. Roles:
- trade date (venue-assigned; e.g. CME Globex evening sessions carry the next day's trade date — verify per venue);
- CCP clearing date; value date (payment calendar, e.g. TARGET for EUR); booking and regime-specific reporting dates;
- contract key dates (last trading day, expiry, exercise deadline, first notice, final settlement, delivery); as-of date.

FIX carries TradeDate and ClearingBusinessDate separately (tags to verify). *Confidence:* high. *Firm decision:* default role and time zone of "today" (Q2). This absorbs review 02 NEW-A-05 (expiry dates) and my v1 NEW-A-06 (extended sessions, withdrawn).

**LD-A0007 Account.** *Industry answer:* three levels — (i) the clearing member's CCP account (house; client omnibus net/gross or individually segregated, EMIR Art. 39(2)/(3), or other regimes' equivalents); (ii) the member's internal client account; (iii) the executing broker's client account, plus give-up references, which are identifiers. Relate levels only by explicit, time-bounded `mapped_to` maintained by an identified party, never by name equality; many internal accounts typically map to one omnibus CCP account. *Confidence:* high. *Firm decision:* levels needed first (Q4).

**LD-A0010 Successful give-up: current vs historical.** *Industry answer:* a status is an assertion by a source about an object, valid over a period, recorded at a time. Native state names are CCP-specific; a workable harmonised vocabulary (values, not concepts):
- pending (alleged, awaiting take-up); accepted (taken up / claimed); rejected;
- lapsed (not taken up by the cut-off, so the trade stays with the giving member; CCP-specific); cancelled (withdrawn by the giver); reversed (where permitted);
- unknown (no record received) — not "pending" (P10).

Hold status per give-up/allocation line (agrees with review 01). "Complete" is derived per instruction: all lines accepted for full quantity; otherwise "partial". "Current" = latest non-superseded assertion from the authoritative source, valid now; "historical" = valid at a past date, as known now or then (§4). Proposed EV-006-Q01 population: give-up lines whose current CCP-sourced status is not "accepted for full quantity" at a stated clearing date, flagged before/after cut-off, excluding trades with no give-up intended. *Confidence:* high for the pattern, medium for state names. *Firm decision:* vocabulary (Q3); "done" (§8a).

**LD-A0013 Position (ops).** CCP-reported and internal positions are two records of one position (NEW-OPS-02); a difference is a break, not two positions. Trades pending give-up sit in the giving member's CCP account, causing predictable timing breaks. *Confidence:* high. *Firm decision:* default source (Q1).

**LD-A0016 (identifier aspect).** *Listed:* listed contract (exchange product code) → series. EU listed series carry an ISIN (ISO 6166) for MiFIR reference data (RTS 23, Delegated Reg. (EU) 2017/585 — to verify); practice elsewhere varies. CFI (ISO 10962) is a classification, not an identifier. *OTC:* UPI (ISO 4914, issued by the ANNA DSB as FSB-designated provider) identifies the product; UTI (ISO 23897, prefixed by the generating entity's LEI — to verify) the reported transaction; DSB OTC ISINs exist for certain MiFIR purposes (scope after the MiFIR review to verify). *Confidence:* medium-high. *Firm decision:* internal master granularity (Q8).

**LD-A0008 (identifier aspect).** One trade carries venue, CCP, UTI, member and client identifiers, some unique only per venue/CCP and business date; cleared OTC successors get new UTIs (review 03). Cross-reference via `has_identifier`; no identifier *is* the identity. *Confidence:* high; no firm decision.

## 4. Proposed new concepts

**Convention for docs/modelling-guidelines.md (not a concept).** A business object (Trade, Position, Account, Give-up) has one identity; sources hold *records* of it with their own identifiers and versions. Time-varying facts carry **valid time** (effective period, business date by role) and **record time** (recorded by the source, received by us). **Current** = valid now, latest non-superseded record; **as of D** = valid at business date D; **as known at T** = only records received by T. Corrections supersede, cancellations end validity, nothing is deleted. Every answer states source, as-of date and freshness. Complements review 08's `temporal_pattern`; comparable to CDM TradeState/BusinessEvent (to verify).

| Temp ID | Name | Module | Type | Definition | Key relationships | Standard alignment (to verify) | Prio | Use case |
|---|---|---|---|---|---|---|---|---|
| NEW-REF-02 | Identifier Scheme | Common | Reference Concept | Governed system for assigning identifiers to one type of business object, defining issuing authority, format, uniqueness scope (global; per issuer; per venue/CCP and business date), validity and reuse rules. | `has_identifier` (object → scheme, qualified by value, issuer, validity); `issued_by` LD-C0001 | ISO 17442, 10383 (operating vs segment MIC), 6166, 4914, 23897; FIX SecurityID/SecurityIDSource and PartyID/PartyIDSource; CDM Identifier; FpML partyTradeIdentifier. CFI is *not* a scheme. | P1 | UC-006, UC-002, UC-001 |
| NEW-REF-03 | Listed Contract Specification | Common (steward: Reference Data; applies to Execution and ETD Clearing) | Reference Concept (versioned terms, like LD-C0032) | Versioned set of standard terms under which a trading venue lists a derivative contract and from which its series are created: underlying, size/multiplier, currency, tick, expiry cycle and key-date rules, settlement method, trading hours. It is what an exchange product code designates. | LD-C0014 `listed_under`; `defined_by` LD-C0009; `classified_as` LD-C0013; `eligible_in` Clearing Service | FIX SecurityDefinition; exchange contract specifications | P1 | UC-001 (circulars change specs), UC-002 (EV-002-Q04), UC-006 |
| NEW-REF-05 | Business Calendar | Common | Reference Concept | Versioned set of business and non-business days, and where relevant trading or processing sessions with their business-date assignment rule, of a calendar owner (venue, CCP, payment system, firm) in a stated time zone. | `owned_by` LD-C0001; resolves LD-C0015; anchors NEW-OPS-01 | Exchange holiday notices, TARGET calendar (instances) | P1 | UC-001 (EV-001-Q05), UC-003, UC-006 |
| NEW-OPS-01 | Cut-off | Common | Reference Concept; specialises Rule Provision if adopted (§8) | Time limit set by an identified authority (CCP, venue, regulator, payment system or the firm) by which a process step must be completed, expressed as a local time relative to a business date of a named calendar, with the stated consequence of missing it (rejection, lapse, late handling, charge). | `applies_to` step of LD-C0020/0022/0023/0046/0028; `relative_to` NEW-REF-05; versioned by supersession; LD-C0030 `breaches` | CCP give-up/allocation deadlines; margin payment deadlines; MiFIR Art. 29 STP timing (instances) | P1 | UC-003 (EV-003-Q05), UC-001 (EV-001-Q04), UC-006 |
| NEW-OPS-02 | Source Record | Common | Entity; a new type "Representation" is a governance option | Representation of a business object, event or state held or reported by an identified source (internal function or external party, e.g. a CCP statement), with its own identifiers, version, status values and record time. Several records can represent one object. | `represents` LD-C0018/0022/0026/0010/0043/0029; `asserted_by` LD-C0001; `supersedes` and `derived_from` NEW-OPS-02 | modelling-guidelines.md ("a trade record is a representation"); FpML/CDM party-scoped identifiers | P1 | UC-006 (source divergence, status history), LD-A0008 |
| NEW-OPS-04 | Reconciliation Break | Common | Entity | Discrepancy found by a reconciliation between records expected to agree: a missing record, or an attribute, quantity or amount difference beyond tolerance. It has a type, magnitude, age and resolution status, and says that records disagree, not which one is wrong. | `identified_by` LD-C0050; `between` NEW-OPS-02 (≥2); `may_raise` LD-C0030 | Industry practice; client-asset reconciliation duties are regulatory instances (e.g. MiFID II Delegated Directive (EU) 2017/593 Art. 2 — to verify) | P1 | UC-006 |

**Governed vocabularies (values, no IDs):** Date Role (v1 NEW-REF-06, downgraded to respect architecture.md); status vocabularies per object type and authority, native and harmonised with a mapping (e.g. FIX AllocStatus, TrdRptStatus — to verify); reconciliation type; break type; exception category.

**Withdrawn from v1:** NEW-REF-01 Identifier (now the `has_identifier` assignment); NEW-OPS-03 Status Assignment (folded into NEW-OPS-02 + vocabularies, agreeing with review 08); NEW-OPS-05 Settlement Instruction and NEW-OPS-06 SSI (no evaluation question needs them; P3 for onboarding later); NEW-PTL-01 Expiry (use review 02 NEW-ETD-12).

**Not proposed:** a concept per identifier type; calendar instances; a "golden source" concept (a governance attribute of a mapping); EMIR portfolio reconciliation (uncleared OTC only, out of scope).

## 5. Proposed new or changed relationships

| Subject | Predicate | Object | Notes |
|---|---|---|---|
| any business object | has_identifier | NEW-REF-02 | Qualified by value, issuer, validity. 0..n per object. A value is unique only within its scheme's scope. |
| LD-C0014 | listed_under | NEW-REF-03 | Listed only. Exactly one spec version effective at listing. |
| NEW-REF-03 | defined_by / classified_as | LD-C0009 / LD-C0013 | CFI is a classification value, not identity. |
| NEW-REF-03 | eligible_in | Clearing Service (§8) | Time-bounded. Eligibility ≠ the firm's coverage. |
| LD-C0015 | has_role / resolved_by | Date Role value / NEW-REF-05 | Both mandatory in ops queries. |
| NEW-OPS-01 | applies_to / relative_to | process step / NEW-REF-05 | Versioned. A new version answers EV-001-Q04 (old vs new deadline, effective date). |
| NEW-OPS-02 | represents | business object | Many records : one object. Divergence = break, not two objects. |
| NEW-OPS-02 | asserted_by | LD-C0001 | Source party (internal function or external). |
| NEW-OPS-02 | supersedes / derived_from | NEW-OPS-02 | Versioning / lineage (e.g. position record derived from trade records). |
| LD-C0050 | compares | NEW-OPS-02 (≥2) | Carries type, keys, tolerance, business date. |
| LD-C0050 | identifies | NEW-OPS-04 | **LD-R0024 retargeted** (migration note). |
| NEW-OPS-04 | may_raise | LD-C0030 | 0..1. Timing breaks and auto-matched breaks usually raise none. |
| LD-C0030 | concerns / breaches | business object (1..n) / NEW-OPS-01 (0..1) | A rejected give-up is an event; it may raise an exception, but it is not a trade failure (EV-003-Q05). |
| LD-C0010 | mapped_to | LD-C0010 | Contextual, time-bounded, maintained by an identified party. n:1 typical for omnibus. Pairs with CCP Account (review 02). |

## 6. Proposed new ambiguity entries

| Temp ID | Term / issue | Required distinction | Reviewer |
|---|---|---|---|
| NEW-A-01 | "Current", "as of", "latest", "historical" | Valid time vs record time; current = valid now and latest non-superseded; as of business date vs as known at a timestamp. Merges review 08 NEW-AMB-02 for facts and statuses. Dates of rule changes are a separate entry (§8). | Operations / Semantic steward |
| NEW-A-02 | Source of record | Which record answers by default when internal and CCP/broker records diverge, and whether both are shown. | Operations / Clearing Product |
| NEW-A-03 | "Product" | LD-C0013 classification vs Listed Contract Specification vs listed series (LD-C0014) vs Service Offering. Merges review 05 NEW-A-02. | Product / Reference Data |
| NEW-A-04 | Break, exception, reject, fail, incident | Reconciliation break vs operational exception vs rejected or lapsed give-up vs settlement fail vs technology incident. | Operations |
| NEW-A-05 | "Trade ID", "reference" | Venue trade ID vs CCP trade ID vs UTI vs internal or client reference. Their uniqueness scope (per venue/CCP and day) and their change on clearing or amendment differ. | Reference Data / Operations |

## 7. Questions only the business owner (Gael) or internal sources can answer

1. **Source of record per object type** (give-up status, position, margin). *Why:* it decides EV-006-Q01/Q03. *Default:* the CCP record for CCP-held facts and the internal record for client-level facts; show the other view and any open break.
2. **Default business date and time zone for "today".** *Default:* the clearing date of the relevant CCP, in its time zone, stated in every answer.
3. **Status vocabulary.** Harmonised firm-level give-up and exception statuses, or CCP-native only? *Default:* the harmonised set in §3, with the native status always kept.
4. **Account levels for UC-006.** Internal client account, CCP account, and the executing broker's account and give-up references? *Default:* all three, linked by `mapped_to`.
5. **History depth.** Is "as known at T" (audit/replay) needed, or only current and as of a date? *Default:* current and as-of. Record time stays in the model.
6. **Reconciliations in scope first.** *Default:* position and margin against the CCP, then give-up.
7. **Existing exception or break categorisation** to align to, by role only (no system names)? *Default:* break type × process step × object type.
8. **Internal instrument and account master.** Does it cross-reference public identifiers? *Why:* it decides whether `has_identifier` instances are internal overlay (L2) content. *Default:* the cross-reference is L2; only schemes and patterns are public.

## 8. Cross-review

**(a) Disagreements**

- **01 (LD-A0016) and 05 (LD-C0013 example "a listed futures contract"):** a venue's listed contract is a versioned, venue-issued specification with its own code, key-date rules and circulars, not an instance of a classification family. Use NEW-REF-03 `classified_as` LD-C0013. I support 05's "Derivative Product" label.
- **08 ("deadlines are parameters of Rule Provision; no Status concept"):** agreed on status (Status Assignment withdrawn). Not on deadlines: agents must compute against calendar and time zone and state the breach consequence (EV-003-Q05, EV-006-Q01). Cut-off as a *specialisation* of Rule Provision reconciles both views.
- **08 NEW-EXE-01 (Execution / Entity / P2):** I propose Common, Reference Concept, P1 — ETD Clearing uses it (eligibility, expiry, positions), and LD-A0016 and EV-002-Q04 cannot close without it.
- **03 NEW-COM-05 Trade Identifier:** a trade-only concept would be repeated for accounts, instruments and parties; Identifier Scheme + `has_identifier` covers all.
- **Give-up "done": 01 default (member claim) vs 02 default (CCP registration):** on many CCP platforms the claim *is* the CCP-recorded move to the receiving member, so they coincide (verify per CCP). Where separate, default to CCP-sourced acceptance for full quantity, consistent with NEW-A-02. Confidence: medium.
- **LD-C0023:** 02/06/08 narrow it to the CCP side; 03 keeps it as parent of two children. I prefer 03 (no meaning change; "accepted for clearing" still resolves). Either works for ops if every status names the accepting role.
- **05 Change Notice typed Event:** a notice is a source document; the event is the Rule Change (06/08).

**(b) Duplicates and proposed canonical form**

| Topic | Proposals | Canonical |
|---|---|---|
| Contract spec | 07 NEW-REF-03, 08 NEW-EXE-01 | **Listed Contract Specification** (Common, Reference Concept) |
| Identifiers | 07 NEW-REF-01/02, 03 NEW-COM-05, 08 template `identity.identifiers` | **Identifier Scheme** + `has_identifier`; the template field lists the applicable schemes per concept |
| Expiry | 07 NEW-PTL-01, 02 NEW-ETD-12 | **Expiry** = 02 NEW-ETD-12; its key dates are Date Role values |
| Time ambiguity | 07 NEW-A-01, 08 NEW-AMB-02 | One entry, **"Time reference of a fact"** |
| Dates of rule changes | 02 NEW-A-04, 05 NEW-A-04, 06 NEW-A-REG-03 | One entry, **"Dates of a rule change"** (Regulatory change); values go into the Date Role vocabulary |
| "Product" | 07 NEW-A-03, 05 NEW-A-02 | One entry, four candidates (§6) |
| CCP-side account | 02 NEW-ETD-04 + `mapped_to`; 07 `mapped_to` | **CCP Account** (02) + **mapped_to** (one relationship) |
| Member acceptance | 02 NEW-ETD-06, 03 NEW-COM-02, 08 NEW-ETD-01 | **Clearing Member Acceptance**, Common (applies to both ETD and OTC) |
| CCP service | 02/03 NEW-COM-01, 05 NEW-COM-03, 08 NEW-COM-01 "Service" | **Clearing Service** (the CCP's service), distinct from review 05's **Service Offering** (the provider's offer to clients) |
| Rules | 02 NEW-COM-06/07, 05 NEW-COM-04/05, 06 NEW-REG-04/05, 08 NEW-COM-03/04 | **Rule Provision** + **Rule Change**; Cut-off specialises Rule Provision |
| Deadlines in margin | 04 NEW-MC-09 Margin Call Cycle | The call cycle *references* Cut-off and Business Calendar instances; it does not redefine them |

**(c) Points raised elsewhere that affect my domain**

- **02/06 (LD-A0009):** at open-offer ETD CCPs a trade is cleared before give-up, so "not given up" ≠ "not cleared"; AG-006 must not report pending give-ups as uncleared.
- **03:** cleared OTC successors get new UTIs and a rejected venue trade may be void → predecessor links on identifiers and a "void" status value.
- **04:** margin tier (NEW-MC-02) is a mandatory qualifier on margin records, margin reconciliations and EV-006-Q02; Collateral Balance is a snapshot record reconciled against the CCP.
- **06:** Regulatory Classification is the same time-bounded-assertion pattern as status ("unknown ≠ NFC−"); document it once in the §4 convention.
- **08:** add a bitemporal flag to `temporal_pattern`; add "Affected IDs" to the ambiguity register (today LD-A0010 never reaches LD-C0022, so AG-006 gets no give-up warning); scope ops jargon ("break", "claim", "allege", "fail") as contextual aliases.
- **01:** status per allocation line; busts/corrections reference the original; UTC timestamps beside the venue trade date — consistent with my LD-C0025 change.
- **Hub (05):** UC-006 omits LD-C0004 and LD-C0008, used by EV-006; I would add LD-C0015, LD-C0030 and LD-C0050 (hub fix, not ontology).
