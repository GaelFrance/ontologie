# Decision log

Status: Record of business-owner decisions. A decision narrows scope or modelling direction; it does not approve individual concept definitions, which remain Draft. The detailed review reports behind these decisions were removed on 2026-11-09 and remain in the repository history.

## Sponsor decision — 2026-09-20 (Phase 1 review)

Evidence: the sponsor answered the seven review points in the project conversation. This approves the architecture and development direction, not individual definitions.

| Point | Decision | Consequence |
|---|---|---|
| 1. Scope and architecture | Approved | Shared core plus Listed Execution, ETD Clearing and OTC Clearing modules. |
| 2. Foundation and sequence | Approved | The first 50 concepts are a provisional foundation; develop Common, Execution, ETD Clearing, then OTC Clearing. |
| 3. Client | Approved | Start with the contractual service-recipient role; distinguish legal entity, commercial group and beneficial owner. |
| 4. Revenue perspective | Management focus | Prioritise what the activity earns and what a client brings; accounting revenue is not the current priority. Revenue and contribution after costs stay distinct. |
| 5. Commission and Transaction | Deferred | Both stay Draft; firm-specific meanings unresolved. |
| 6. Relationships | Approach approved | Constraints refined by context; no universal fill-to-trade cardinality. |
| 7. Governance | Approach approved | Sponsor arbitrates; Operations, Finance, Risk and Legal review their subjects. |

## Sponsor answers — 2026-11-01

Evidence: sponsor answer in the project conversation, 2026-11-01, in reply to the execution reviewer's owner questions in the 2026-11 expert review (execution review, questions 1, 3, 4 and 8).

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
| 5. Give-up completion and authoritative record | A give-up is complete when the full allocated quantity is registered to the receiving clearing member's CCP account, per the CCP record. Partial take-ups are reported separately. Member acceptance and CCP registration times are both kept. When internal and CCP records disagree, the CCP record is authoritative for completion and the discrepancy is reported as a break, never silently resolved. | LD-A0010 decided for the default answer of the give-up and clearing acceptance agent; the definitions of LD-C0022, LD-C0023 and LD-C0053 remain Draft. | LD-C0022, LD-C0023, LD-C0053, LD-A0010, LD-A0034 |

## Sponsor decision — 2026-11-01 (meaning changes kept as Draft)

Evidence: sponsor answered "ok" in the project conversation, 2026-11-01, after an explanation of each change (open question 2).

| Point | Decision | Consequence in the ontology | Affected IDs |
|---|---|---|---|
| 6. Meaning changes and clarifications from the expert review | Accepted as Draft: Instrument narrowed to standardised specifications; give-up as attribution at or after CCP registration; Clearing Acceptance as the CCP side with member take-up separate; Collateral as a State (title transfer or security interest); Party Role as the role assignment; Product relabelled Product Family. | The changes stay in the catalogue as Draft. This accepts the direction of the changes, not a Reviewed or Approved status for the definitions. | LD-C0003, LD-C0013, LD-C0014, LD-C0022, LD-C0023, LD-C0047 |

## Sponsor decision — 2026-11-01 (reference clearing services)

Evidence: sponsor answer in the project conversation, 2026-11-01 (open question 3).

| Point | Decision | Consequence in the ontology | Affected IDs |
|---|---|---|---|
| 7. Reference clearing services for rulebook evidence | Five public CCPs seed the evidence for the give-up and clearing acceptance agent: Eurex Clearing, ICE Clear Europe, LCH (SwapClear service), CME Clearing and Euronext Clearing. | These become the first Clearing Service instances whose public rulebooks are cited for interposition mechanism and moment, give-up deadlines and cut-offs. Instances and rulebook facts belong to an evidence layer outside the ontology, not to the concept catalogue; each fact must cite the public rule and its version. | LD-C0051, LD-C0054, LD-C0065, LD-A0009, LD-A0017 |

## Sponsor decision — 2026-11-01 (regulatory regime priority)

Evidence: sponsor answer in the project conversation, 2026-11-01 (open question 5).

| Point | Decision | Consequence in the ontology | Affected IDs |
|---|---|---|---|
| 8. Regulatory regime priority | Global scope. Priority 1: Europe (EU: EMIR including EMIR 3, MiFID II/MiFIR, CRR; and UK) and United States (CFTC and SEC). Priority 2: Asia-Pacific regimes, to be scoped. | Regime instances for the change-impact and onboarding agents are seeded in this order; US futures and cleared-swaps structures are no longer treated "in general terms" only. | LD-C0063, LD-C0067, LD-C0068 |

## Sponsor decisions — 2026-11-01 (consultations and default date)

Evidence: sponsor answers in the project conversation, 2026-11-01 (open questions 6 and 7).

| Point | Decision | Consequence in the ontology | Affected IDs |
|---|---|---|---|
| 9. Consultations and sign-off | Consultations and draft rules are analysed as rule changes, with a mandatory status and a "not yet in force" flag. Readings flagged "interpretation required" are reviewed by Regulatory Affairs and business management first, with Legal and Compliance. Agent outputs are labelled "public-layer reading, not legal advice". | Rule Change carries a lifecycle status (consultation, adopted, in force, withdrawn); the reviewer roles are recorded as governance roles, not people. | LD-C0064, LD-R0053, LD-A0022 |
| 10. Default meaning of "today" and "current" | The clearing date of the relevant CCP, in that CCP's time zone, stated in every answer. | Date role "clearing date" is the default for operational questions; other date roles must be requested explicitly. Record time stays in the model for later audit needs. | LD-C0015, LD-C0066, LD-A0015, LD-A0023 |

## Sponsor decisions — 2026-11-01 (access models, format and governance)

Evidence: sponsor answers in the project conversation, 2026-11-01 (open questions 8 and 12).

| Point | Decision | Consequence in the ontology | Affected IDs |
|---|---|---|---|
| 11. Access models and client clearing legal models | Model all access models and both client clearing legal models (principal-to-principal and agency) generically, in every regime, including agency treatment in Europe. The firm's current and target models are internal facts and are not recorded in this repository. | No regime is tied to a single legal model; the legal model is a qualifier of the client clearing arrangement, validated by Legal in the internal layer. | LD-C0056, LD-C0057, LD-C0059, LD-A0030 |
| 12. Format | Markdown stays canonical because business reviewers must read it. Machine-readable exports (JSON or YAML) are generated by tooling and never edited or reviewed by hand. French labels are optional; superseded the same day: French labels are removed (sponsor request). | README, architecture, template and repository structure updated. | All |
| 13. Governance | The sponsor arbitrates until reviewers are named. A governance model and reviewer list were requested. | [Governance model proposal](governance-model-proposal.md) submitted for decision. | All |

## Sponsor decision — 2026-11-01 (Ontology Lead)

Evidence: sponsor choice in the project conversation, 2026-11-01.

| Point | Decision | Consequence in the ontology | Affected IDs |
|---|---|---|---|
| 14. Ontology Lead | The role previously called "semantic steward" is named **Ontology Lead**. The sponsor holds it during Phase 2, in addition to arbitration; the two should be separated once the board operates. | Governance documents renamed; the Ontology Lead prepares changes, review packs and releases but does not approve meanings. | All |

## Sponsor decision — 2026-11-01 (Revenue domain)

Evidence: sponsor answer in the project conversation, 2026-11-01 (open question 9).

| Point | Decision | Consequence in the ontology | Affected IDs |
|---|---|---|---|
| 15. Revenue domain | Revenue is a governance domain with its own owner, who answers the revenue questions. Collateral revenue is a sub-domain owned by the Collateral Manager. | Open questions 9 and 10 are assigned to the Revenue owner (collateral income part of 9 to the Collateral Manager); question 11 to the Collateral Manager with Risk. Defaults stay proposals until they answer. | LD-C0031 to LD-C0042, LD-C0074, LD-A0001, LD-A0002, LD-A0014, LD-A0033 |

Apart from LD-A0010 (decision 5), these answers do not resolve any ambiguity entry, approve any definition, formula or cost perimeter, or change the deferral of Commission and Transaction.

## Sponsor decision — 2026-11-01 (level-2 domain review)

Evidence: sponsor answer in the project conversation, 2026-11-01 ("accept everything, merge and release"), on the points listed in [open questions](open-questions-for-owner.md) (level-2 section) and the level-2 supervision report.

| Point | Decision | Consequence in the ontology | Affected IDs |
|---|---|---|---|
| 16. Meaning changes | The 13 proposed meaning changes are accepted as Draft: Party, Broker, Trading Venue, Allocation, Position, Commission, Variation Margin Requirement, Market Access Arrangement, Allocation Instruction, Rule Change, Cut-off, Regulatory Classification, CCP Account. | Definitions replaced in the catalogue; Commission keeps its resolution flag. Settlement Deadline, Firm Cut-off, Take-up Deadline and Standing Allocation Instruction no longer depend on a pending decision. | LD-C0001, LD-C0005, LD-C0009, LD-C0020, LD-C0026, LD-C0038, LD-C0045, LD-C0059, LD-C0060, LD-C0064, LD-C0065, LD-C0068, LD-C0069 |
| 17. Cut-off | A cut-off is set by a rule provision or by a term of an agreement; it is no longer a kind of Rule Provision. Only rule-set cut-offs follow the rule change lifecycle. | Specialisation removed; new relationship "set by". | LD-C0065, LD-C0063, LD-C0012 |
| 18. Third-party execution | Third-party execution also covers an executing broker that is a venue member but chooses not to use its own membership for that business (extends decision 3). | Third-Party Execution Arrangement and Third-party Executing Member widened. | LD-C0113, LD-C0130 |
| 19. Backlog triggers | Triggers waived: Identifier Scheme, Source Record, Activity Volume, Clearing Submission, Change Notice, Regulatory Obligation, Default Fund Contribution and Cash Collateral Interest are promoted now. | Concepts kept as Draft. | — |
| 20. Late and penalty charges | Fee Charge includes late and penalty charges arising from a missed cut-off or a settlement fail. | Fee Charge definition widened; no separate concept. | LD-C0031 |
| 21. OTC execution on venues | OTC derivatives executed on MTFs, OTFs and swap execution facilities are out of scope for the listed pilot and planned as a later extension of the execution domain. | Scope note on the execution page. | — |
| 22. Questions for the firm | Merged company questions are answered in joint sessions with the roles named. | Joint questions kept as written. | — |

## Sponsor decision — 2026-11-09 (missing concepts)

Evidence: sponsor answer in the project conversation, 2026-11-09, approving the proposal to add Open Trade Equity and the alias MED and to add other missing concepts of the same importance.

| Point | Decision | Consequence in the ontology | Affected IDs |
|---|---|---|---|
| 23. Statement measures | "Margin excess or deficit" (MED) is an alias of Margin Excess or Shortfall; Open Trade Equity, Account Cash Balance, Account Equity and Position Valuation are added to the margin domain. | Concepts added as Draft with summaries, required context and links; firm questions added on how equity is built and which valuation clients see. | LD-C0166, LD-C0223, LD-C0224, LD-C0225, LD-C0230 |
| 24. Other missing concepts | Option Premium and Client Statement (post-trade), Trade Confirmation (execution) and Position Limit (regulation) are added. "Maintenance margin" stays a call trigger level in Margin Call Terms, as proposed for LD-A0027; a client funds requirement stays in the backlog. | Concepts added as Draft; alias rows for maintenance margin and monthly statement; backlog item and firm question on client funds. | LD-C0165, LD-C0226, LD-C0227, LD-C0228, LD-C0229 |

## Ontology Lead decision — 2026-11-26 (risk domain)

Evidence: Ontology Lead request in the project conversation, 2026-11-26 ("Full Risk Domain but clearly identify the 3 areas: risk we take with the client we clear, execution risk, CCP Risk side").

| Point | Decision | Consequence in the ontology | Affected IDs |
|---|---|---|---|
| 25. Risk domain | An eleventh domain, Risk, is opened with three areas kept apart: the risk we take on the clients we clear, execution risk, and CCP risk. | New domain page `risk` with 22 Draft concepts, four ambiguity entries (LD-A0036 to LD-A0039) and questions for our firm; existing limit, default and default-resource concepts keep their primary domain and are shown on the risk page. Owner and classification settled by decisions 26 and 27. | LD-C0231 to LD-C0252 |

This decision opens the domain; it approves none of its definitions, which stay Draft until the risk domain owner approves them.

## Ontology Lead decision — 2026-11-26 (risk domain owner and limits)

Evidence: Ontology Lead answer in the project conversation, 2026-11-26 ("Yes to both"), to open questions 26 and 27 as proposed.

| Point | Decision | Consequence in the ontology | Affected IDs |
|---|---|---|---|
| 26. Risk domain owner | The risk domain is owned by a role in the risk function: the head of clearing risk or a delegate. Existing concepts on limits, defaults and default resources keep their primary domain and are shown on the risk page. | Owner role set in the review domains; no concept moves. | LD-C0231 to LD-C0252, LD-C0138, LD-C0119, LD-C0159, LD-C0154, LD-C0155, LD-C0172, LD-C0163 |
| 27. Clearing Limit | Clearing Limit is a kind of Risk Limit. | Specialisation kept; the Clearing Limit definition says so instead of "without a level-1 parent" (clarification). | LD-C0138, LD-C0232 |


## Ontology Lead decision — 2026-11-26 (risk domain peer review)

Evidence: Ontology Lead answer in the project conversation, 2026-11-26 ('apply everything'), on the decision list of the risk domain peer review. The Ontology Lead decided as arbiter while the domain owners are not named, and accepted the preconditions of clarification items 2 (registration as the boundary of Unaccepted Give-up Exposure), 5 (house margin only in the Default Waterfall) and 6 (a guarantee accepted as collateral is not Third-party Credit Support). Every recommended option was taken; the proposals the review dropped were not applied.

| Point | Decision | Consequence in the ontology | Affected IDs |
|---|---|---|---|
| 28. Risk domain peer review | All recommendations of the review are applied: eight concepts retired into values of the concepts they belong to, sixteen meaning changes with the recommended option, one new concept, clarifications, aliases, relationship corrections and questions for our firm. | The risk domain keeps 15 active concepts (14 kept, 1 new) and 8 deprecated rows whose IDs stay. Relationship corrections and new rows LD-R0658 to LD-R0665; LD-R0641 now ends with Give-up Registration. | LD-C0231 to LD-C0253, LD-C0119, LD-C0125, LD-C0138, LD-C0154, LD-C0159, LD-C0172, LD-C0203, LD-C0229, LD-C0064, LD-C0056, LD-C0010, LD-C0046, LD-C0071, LD-C0162 |
| 28. Retirements | Stress Loss retired into Risk Exposure (measure basis value); Client Risk Rating into Client Credit Assessment (recorded outcome); Client Default Management into Client Default (step values); Pre-trade Limit into Risk Limit (kind value); Kill Switch Activation into the risk-expert skill and a contextual alias; Execution Error into cause values on Execution Correction and Error Position; CCP Dedicated Own Resources into Default Waterfall (layer value); Default Management Auction into Clearing Member Default (step value). | Rows and IDs kept, definitions marked Deprecated with the replacing concept; relationships moved where the move gives a true statement, otherwise kept with a note. | LD-C0235, LD-C0238, LD-C0240, LD-C0241, LD-C0242, LD-C0243, LD-C0249, LD-C0251 |
| 28. M1 Firm limit versus venue rule | Option A: a parameter a venue publishes for all participants is a Rule Provision; a limit set for one participant is a Risk Limit. | Risk Limit and Pre-trade Control Check reworded; value "control checked"; new row Pre-trade Control Check may apply Rule Provision. | LD-C0232, LD-C0119, LD-C0063 |
| 28. M2 Limits a CCP sets on its members | Option A: out of scope of Risk Limit. | One sentence added to Risk Limit. | LD-C0232 |
| 28. M3 Limit Breach | Option A: warnings are not breaches; active or passive is recorded; exceeding a Position Limit is not a Limit Breach. | Definition and action values replaced. | LD-C0234 |
| 28. M4 Client Clearing Exposure | Option A: stated before or after collateral as declared; member-to-client tier; indirect clients, omnibus accounts, prefunding and give-in covered. Decided now, before the answer to q03. | Definition replaced; the collateral methodology point is in the risk-expert skill. | LD-C0236 |
| 28. M5 Unallocated quantities | Option A: kept out of Unaccepted Give-up Exposure; no sibling concept. | Alias "unallocated risk" pending; firm question q24 informs a later review. | LD-C0245 |
| 28. M6 CCP Exposure | Option A: house and client accounts, house positions, amounts due, collateral not protected, default fund contribution in all cases, assessments, client trades where the member stays liable. | Definition replaced; new row CCP Exposure includes Collateral; LD-R0644 note corrected. | LD-C0246, LD-C0047, LD-C0172 |
| 28. M7 Default Fund Assessment | Option A: a commitment; only its call gives rise to a Settlement Obligation. | Definition replaced; specialisation to Settlement Obligation removed; new row gives rise to Settlement Obligation. | LD-C0250, LD-C0028 |
| 28. M8 Waterfall layer links | Option A: layers are linked by is_used_in instead of part_of. | LD-R0650, LD-R0651 and LD-R0652 corrected in place. | LD-C0248, LD-C0172, LD-C0250 |
| 28. M9 CCP Loss Allocation | Option A: the CCP or a resolution authority acts; non-default losses included. | Definition and values replaced; Regulatory Authority gains recovery and resolution powers and the value "resolution authority". | LD-C0252, LD-C0203 |
| 28. M10 Error Position holder | Option A: the executing broker or a third-party executing member responsible. | Definition replaced; LD-R0639 note corrected. | LD-C0244 |
| 28. M11 Client default and indirect clients | Option A: the steps after a client default include handling the indirect clients' positions and collateral (to verify). | Sentence added to Client Default. | LD-C0159 |
| 28. M12 Sponsored participant default | Option A: no change now; a candidate is added to the default ambiguity. | LD-A0039 extended. | LD-A0039 |
| 28. M13 Rule Change affects | Option A: the union of LD-R0053 is not widened; Default Waterfall is changed by Rule Change instead. | New row LD-R0660. | LD-C0064, LD-C0248 |
| 28. M14 Risk Exposure scope | Option A: no change. | — | LD-C0231 |
| 28. M15 Kill switch authorised parties | Not applicable: Kill Switch Activation is retired (L12). | Who may activate it is described in the risk-expert skill. | LD-C0242 |
| 28. M16 CCP default management process | Option A: no new concept; the steps are values of Clearing Member Default. | LD-R0654 and LD-R0362 corrected to follows. | LD-C0154, LD-C0155 |
| 28. N1 Client Risk Group | A new concept for the group of clients a risk function treats as one. | New concept, primary in risk and shown on parties-and-roles. | LD-C0253 |

These decisions approve no definition: every definition, including the new and changed ones, remains Draft until the domain owner approves it.

## Ontology Lead decision — 2026-11-26 (execution simplification)

Evidence: Ontology Lead approval in the project conversation, 2026-11-26 ("ok go"), of five changes proposed after an external review of the execution domain, under his principle that the ontology should maximise agent performance, not size.

| Point | Decision | Consequence in the ontology | Affected IDs |
|---|---|---|---|
| 29. Execution simplification and knowledge layers | Prefer values on existing concepts to new concepts. Execution method, trading capacity and order state become values on Order and Execution. Transaction is retired, and the word stays ambiguous. Standing Allocation Instruction is merged into Allocation Instruction as its form "standing". Every concept gets a knowledge layer (0 Business Core, 1 Domain Core, 2 Specialist, 3 Reference), starting with the execution domain. | Value rows on LD-C0016, LD-C0017 and LD-C0060. LD-C0019 and LD-C0128 are deprecated in place. LD-R0269 moves to LD-C0060 and LD-R0270 is deprecated. A "Knowledge layers" section is added to the concept annotations. The generated pages show the layer, and say "added in review round" instead of "level". Execution method and trading capacity leave the execution backlog. | LD-C0016, LD-C0017, LD-C0019, LD-C0060, LD-C0128, LD-R0269, LD-R0270 |

This decision approves no definition: the values and layers stay Draft until the Listed Execution product owner confirms them. Merging Executed Trade (LD-C0126) into Trade is not decided; it waits for the clearing owner and the open question on the clearing tier.
