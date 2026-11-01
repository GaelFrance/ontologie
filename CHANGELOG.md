# Change log

## 2026-11-01 — Review by domain

- Classification refined after a review by three AI experts (Ontology Lead, ETD and OTC clearing, ETD execution), recorded in `governance/reviews/2026-11-classification-review/`. Ten domains instead of eight: Clearing split into "give-up and acceptance" (wave 1 pack for AG-004) and "services, accounts and client clearing"; new "Service offering and market access" (owner: product development lead, sponsor or delegate); "Products and reference data" renamed "Instruments, venues and calendars". Each concept now has exactly one primary domain (whose owner approves it) and may be shown on other pages for comment; `--check` enforces this. Reviewer roles completed (OTC Clearing product owner, Revenue domain owner, Compliance and others where their answer differs).
- Domain pages now carry: questions per reviewer role, review wave and pilot use cases, a generic sequence for process domains, a scope note, a verdict column, ambiguities in full only where their concepts are approved, and the backlog items each domain may need. The "En bref (FR)" blocks are removed. No definition changed; definition issues raised by the experts are listed for the owners in the review's arbitration note.
- New `governance/review-domains.md`: eight business review domains with owner role, reviewer roles, concept IDs and the question put to reviewers. Every concept belongs to at least one domain.
- New generated pages in `domains/` (one per domain plus an index) built by `tools/build_domain_views.py` from the catalogue, relationships, ambiguity register, annotations and decision log. `--check` fails when a page is stale or a concept has no domain. No definition changed.
- French labels removed from concept annotations, the concept template and the domain pages (sponsor request, 2026-11-01).

## 2026-11-01 — Expert review arbitration and sponsor answers

Evidence: eight specialist reviews and their [arbitration](governance/reviews/2026-11-expert-review/ARBITRATION.md); sponsor answers recorded in the [decision log](governance/decision-log.md). Everything remains Draft; only LD-A0010 is decided.

**Sponsor decisions (2026-11-01).** Service mix (execution-only, clearing-only, execute-and-clear; give-up and give-in; revenue per service); revenue split by order handling channel; third-party execution in scope; both venue/CCP and broker-side average pricing. Rounding residuals remain open. Give-up completion (LD-A0010) decided: full allocated quantity registered to the receiving member's CCP account, CCP record authoritative, discrepancies reported as breaks. Sponsor accepted the meaning changes below as Draft. Reference clearing services for AG-004: Eurex Clearing, ICE Clear Europe, LCH SwapClear, CME Clearing, Euronext Clearing. Regime priority: EU, UK and US at P1; Asia-Pacific at P2. Consultations count as rule changes (reviewed by Regulatory Affairs and business management with Legal and Compliance). Default date: CCP clearing date. Both client clearing legal models modelled in every regime. Markdown stays canonical (machine-readable exports generated); French labels optional; governance model and reviewer list proposed; role "semantic steward" renamed Ontology Lead. Revenue governance domain created (collateral revenue sub-domain owned by the Collateral Manager); open questions 9 to 11 assigned.

**Meaning and type changes (explicit, Draft):**
- LD-C0014 Instrument: narrowed to a standardised, counterparty-independent specification at the level at which it is listed or assigned an instrument identifier; bespoke OTC contracts are Trades, not Instruments. Rationale: LD-A0016 (still Open). Migration: any use of LD-C0014 for a bespoke OTC contract moves to LD-C0018.
- LD-C0022 Give-up / Take-up Process: redefined as attribution of all or part of an executed listed trade from the executing side to a receiving clearing member, at or after CCP registration. Rationale: the previous wording implied the trade was not yet cleared, which is wrong where the CCP registers first to the executing member.
- LD-C0047 Collateral: type Entity to State; "committed as security" replaced by "provided by title transfer or security interest". Rationale: title-transfer arrangements are not security interests; LD-C0048 is already the entity.
- LD-R0019: relation label `moves` to `changes` (LD-C0047 is now a State); asset transfer is the new LD-R0074.

**Label changes (meaning unchanged):** LD-C0013 Product to Product Family; LD-R0011 `receiving_member` to `has_receiving_member`.

**Refinements of placeholder definitions:** LD-C0005 Broker (operative definition); LD-C0007 Clearing Member (clearing service, membership category, clearing scope).

**Clarifications (meaning unchanged):** LD-C0003 read as the role assignment (party-in-role); LD-C0015 date role and calendar; LD-C0016 Order; LD-C0023 as the CCP side, evidence of interposition; LD-C0043 to LD-C0046 margin definitions; LD-C0049 Collateral Movement; LD-C0050 Reconciliation; conditions of LD-R0004, LD-R0006, LD-R0013, LD-R0017, LD-R0018, LD-R0024.

**Added:** concepts LD-C0051 to LD-C0074; relationships LD-R0025 to LD-R0083; ambiguities LD-A0019 to LD-A0035; affected concept IDs, status and proposed answers (pending owner decision) for every ambiguity; [concept annotations](ontology/concept-annotations.md) (specialisations, aliases, resolution flags for LD-C0019 and LD-C0038, required context, usage notes, French labels, standard alignments to verify); [open questions for the owner](governance/open-questions-for-owner.md); type definitions, the record-versus-object rule and the time convention in the [modelling guidelines](docs/modelling-guidelines.md); fixed field names in the concept template; taxonomy axes and seed values.

**Not changed:** Commission (LD-C0038) and Transaction (LD-C0019) stay deferred; no metric formula, cost perimeter, physical mapping or YAML format; no universal cardinality. Proposals not accepted are listed in the arbitration backlog.

## 2026-09-20 — Sponsor review recorded

- Recorded approval of the foundation, development sequence, Client approach, contextual relationships and governance approach.
- Prioritised management revenue for business performance and client analysis; kept the revenue-versus-profitability boundary open.
- Kept Commission, Transaction and individual definitions Draft; no metric formula or physical mapping approved.

## 2026-09-20 — Phase 1 foundation draft

- Established a Markdown-first business ontology foundation for Listed Execution, ETD Clearing and OTC Clearing.
- Added 50 stable concept IDs, major proposed relationships, taxonomy axes and an ambiguity register.
- Added concept and mapping templates, semantic-contract requirements and governance.
- Kept all meanings Draft and deferred expansion and physical mappings pending their approval gates.
