# Major relationships

Status: Draft. All concept IDs refer to the [foundation catalogue](../ontology/foundation.md).

These are logical relation proposals, not database foreign keys. Source/target alternatives are not equivalence assertions. Cardinalities remain unapproved unless stated as qualified examples. Inverse labels, full constraints and contextual relation objects will be defined in Phase 2.

| ID | Source concept | Relation | Target concept | Meaning and conditions |
|---|---|---|---|---|
| LD-R0001 | LD-C0001 | has_role | LD-C0003 | Use a contextual, time-bounded role assignment; not an unqualified permanent property. |
| LD-R0002 | LD-C0003 | governed_by | LD-C0012 | Applicable to the role assignment where a governing agreement exists. |
| LD-R0003 | LD-C0004 | submits | LD-C0016 | Distinguish contractual client, representative and technical sender. |
| LD-R0004 | LD-C0016 | fulfilled_by | LD-C0017 | An order can have zero or multiple fills, directly or through derived child orders; cancellations and partial execution matter. |
| LD-R0005 | LD-C0017 | contributes_to | LD-C0018 | Do not assume a universal one-to-one fill/trade representation. |
| LD-R0006 | LD-C0017 | occurs_on | LD-C0009 | When applicable; qualify by execution method: for privately negotiated trades (block, exchange for related position) the venue registers rather than matches; distinguish execution from reporting. |
| LD-R0007 | LD-C0020 | allocates | LD-C0017 / LD-C0018 | State allocated quantity, source object and process scope. |
| LD-R0008 | LD-C0020 | targets | LD-C0010 | Target account does not by itself establish legal ownership. |
| LD-R0009 | LD-C0021 | groups | LD-C0017 / LD-C0018 | Eligibility, weighting, rounding and resulting records depend on context. |
| LD-R0010 | LD-C0022 | concerns | LD-C0018 | Carry quantity, counterparties and lifecycle history. |
| LD-R0011 | LD-C0022 | has_receiving_member | LD-C0007 | An intended recipient is not proof of acceptance (see LD-C0053). Label changed from receiving_member on 2026-11-01; meaning unchanged. |
| LD-R0012 | LD-C0023 | concerns | LD-C0018 | Specify service, acceptance criteria and time. |
| LD-R0013 | LD-C0023 | accepted_by | LD-C0008 | Within an identified clearing service (LD-C0051) and for an identified member account; acceptance is evidence of, not identical to, CCP interposition (LD-C0054). |
| LD-R0014 | LD-C0024 | transforms | LD-C0018 | Preserve predecessor and successor obligations/trades with directional lineage. |
| LD-R0015 | LD-C0026 | recorded_in | LD-C0010 | Recording does not assert beneficial ownership. |
| LD-R0016 | LD-C0026 | included_in | LD-C0027 | Membership is purpose-specific and time-bound. |
| LD-R0017 | LD-C0043 | assessed_for | LD-C0027 / LD-C0010 | Include margin provider and taker role assignments (which give the tier), component, methodology version, run type and as-of time; not individual-position causality. At CCP tier the account is a CCP Account (LD-C0069). |
| LD-R0018 | LD-C0046 | requests_satisfaction_of | LD-C0043 | Requirement, demand and remaining shortfall are different objects; the called amount derives from the requirement less collateral already held after haircut, adjusted for minimum transfer amount and rounding. |
| LD-R0019 | LD-C0049 | changes | LD-C0047 | A movement transfers asset quantities (LD-R0074) and thereby changes the collateral held; identify provider, taker, arrangement and quantity. Label changed from moves on 2026-11-01 because LD-C0047 is now a State. |
| LD-R0020 | LD-C0029 | settles | LD-C0028 | May be partial; net payment may cover several obligations. |
| LD-R0021 | LD-C0031 | has_debtor | LD-C0001 | Debtor may differ from actual payer. |
| LD-R0022 | LD-C0031 | has_creditor | LD-C0001 | Creditor may differ from collector or ultimate beneficiary. |
| LD-R0023 | LD-C0031 | calculated_under | LD-C0032 | Use the applicable tariff version and conditions; calculation is not recognition. |
| LD-R0024 | LD-C0050 | identifies | LD-C0030 | A reconciliation identifies discrepancies (breaks); only some are handled as operational exceptions, and a break does not prove underlying trade failure. |
| LD-R0025 | LD-C0051 | operated_by | LD-C0008 | Exactly one CCP per clearing service (definitional); a CCP operates one or more services. |
| LD-R0026 | LD-C0007 | admitted_to | LD-C0051 | Qualify by membership category and effective period; the category sets the clearing scope (own, affiliates, clients, non-clearing members). |
| LD-R0027 | LD-C0053 | decided_by | LD-C0007 | Record outcome (accepted, partially accepted, rejected), quantity and time. |
| LD-R0028 | LD-C0053 | concerns | LD-C0018 | Or an allocated quantity of it; designation of a member is not its acceptance (LD-R0011). |
| LD-R0029 | LD-C0053 | part_of | LD-C0022 | In listed give-up workflows; in OTC clearing it answers a clearing submission (backlog). Precedes or coincides with CCP acceptance; the order is stated per clearing service. |
| LD-R0030 | LD-C0054 | concerns | LD-C0018 | Interposition creates the CCP-facing trades; under novation the predecessor is extinguished (LD-R0014). |
| LD-R0031 | LD-C0054 | evidenced_by | LD-C0023 | Order and timing are set per clearing service; under open offer interposition can precede the acceptance message. |
| LD-R0032 | LD-C0054 | effected_through | LD-C0024 | Only when the mechanism is novation; open offer replaces no prior bilateral contract. |
| LD-R0033 | LD-C0054 | within | LD-C0051 | Mechanism and legal moment are rulebook facts per clearing service and date. |
| LD-R0034 | LD-C0018 | succeeds | LD-C0018 | Generic directional lineage qualified by the deriving event (interposition, allocation, compression, transfer, porting, bilateral novation); LD-R0014 remains the novation-specific case. No cardinality asserted. |
| LD-R0035 | LD-C0022 | has_giving_member | LD-C0007 | The clearing member holding the trade before give-up, normally the executing side's clearing member. |
| LD-R0036 | LD-C0022 | governed_by | LD-C0055 | Where one exists; a missing or inapplicable agreement is a common rejection cause. |
| LD-R0037 | LD-C0056 | elects | LD-C0011 | Per clearing service and time-bounded; legal protection is a Legal conclusion, never inferred from the model name. |
| LD-R0038 | LD-C0057 | clears_through | LD-C0007 | When the clearing broker is not itself a member of the clearing service; at most one per service and period. |
| LD-R0039 | LD-C0059 | grants_access_to | LD-C0009 / LD-C0051 | Execution access to a venue or clearing access to a clearing service. Coverage is never inferred from memberships alone. |
| LD-R0040 | LD-C0059 | confers | LD-C0003 | For example a Trading Venue Member, Clearing Member or Client role assignment; the arrangement and the resulting role are distinct. |
| LD-R0041 | LD-C0059 | intermediated_by | LD-C0003 | The intermediary's role assignment (venue member, clearing member or clearing broker); zero or one. |
| LD-R0042 | LD-C0058 | admitted_to | LD-C0009 | Qualify by membership category and effective period; venue membership does not imply clearing membership. |
| LD-R0043 | LD-C0060 | instructs | LD-C0020 | Versions are kept; the deadline is a Cut-off (LD-C0065). |
| LD-R0044 | LD-C0060 | references | LD-C0017 / LD-C0021 | The executions or average-price group whose quantity is split. |
| LD-R0045 | LD-C0020 | may_initiate | LD-C0022 | Only when the target account is carried by a clearing member other than the one to which the execution is registered; otherwise the allocation is internal. |
| LD-R0046 | LD-C0016 | has_handling_channel | LD-C0061 | Time-stamped; may change (a care order passed to an algorithm); child orders inherit it unless re-routed. |
| LD-R0047 | LD-C0014 | listed_under | LD-C0062 | Listed instruments only; one specification version effective at listing. |
| LD-R0048 | LD-C0062 | classified_as | LD-C0013 | A classification code such as CFI is a classification value, not an identity. |
| LD-R0049 | LD-C0062 | defined_by | LD-C0009 | The venue that lists the contract; time-bounded. |
| LD-R0050 | LD-C0062 / LD-C0013 | eligible_in | LD-C0051 | Effective-dated; OTC eligibility is bounded by trade-term ranges. Eligibility is not a clearing obligation and not the firm's offering (LD-A0029). |
| LD-R0051 | LD-C0009 | operated_by | LD-C0002 | The venue is distinct from its legal operator; identify the venue by ISO 10383 MIC (operating versus segment MIC, to verify per use). |
| LD-R0052 | LD-C0064 | changes | LD-C0063 / LD-C0032 / LD-C0062 / LD-C0066 / LD-C0070 / LD-C0072 | Change type new, amend, withdraw or propose; dates qualified by date role (LD-A0022). |
| LD-R0053 | LD-C0064 | affects | LD-C0051 / LD-C0009 / LD-C0069 / LD-C0011 / LD-C0022 / LD-C0023 / LD-C0043 / LD-C0047 | Instance-level impact target, declared as this explicit union; n-ary qualifiers: impact type, affected role, confidence, interpretation required. Tagging a notice with a concept ID is an annotation, not this relation. |
| LD-R0054 | LD-C0063 | supersedes | LD-C0063 | Temporal succession of versions; answers what changed and from which effective date. |
| LD-R0055 | LD-C0063 | part_of | LD-C0067 | For regulatory provisions; rulebook provisions belong to their issuing CCP or venue (LD-R0056), not to a regime. |
| LD-R0056 | LD-C0063 | issued_by | LD-C0001 | Regulator, CCP, venue operator or the firm. |
| LD-R0057 | LD-C0065 | applies_to | LD-C0020 / LD-C0022 / LD-C0023 / LD-C0046 / LD-C0028 | A step of the process or obligation concerned; versioned by supersession. |
| LD-R0058 | LD-C0065 | relative_to | LD-C0066 | Deadline in local time against the named calendar's business date. |
| LD-R0059 | LD-C0015 | resolved_against | LD-C0066 | Together with a date-role value and time zone; both mandatory in operational queries. |
| LD-R0060 | LD-C0068 | classifies | LD-C0002 / LD-C0003 / LD-C0010 / LD-C0009 / LD-C0008 / LD-C0051 | Entity-level statuses attach to the legal entity, relationship-level statuses to the role assignment; never to the Client role generically or to a commercial group. |
| LD-R0061 | LD-C0068 | under | LD-C0067 | Record regime, asset class where relevant, basis, effective period and evidence; valid time and record time both kept. |
| LD-R0062 | LD-C0069 | held_in_name_of | LD-C0007 | The clearing member in whose name the CCP opens the account. |
| LD-R0063 | LD-C0069 | within | LD-C0051 | Account types and their margining basis are defined per clearing service. |
| LD-R0064 | LD-C0069 | implements | LD-C0011 | Together with the clearing service, the model determines the margining basis (gross or net) and collateral attribution. |
| LD-R0065 | LD-C0010 | mapped_to | LD-C0010 | Explicit, time-bounded correspondence maintained by an identified party (for example internal client accounts to a CCP omnibus account); never by name equality; many-to-one is typical, not universal. |
| LD-R0066 | LD-C0043 | determined_under | LD-C0070 | One methodology version per calculation run; a member-client methodology may replicate the CCP's. |
| LD-R0067 | LD-C0045 | gives_rise_to | LD-C0028 | Under settled-to-market treatment; under collateralised-to-market treatment VM is demanded by a margin call (LD-R0018) and met with collateral. Treatment is a versioned fact per clearing service and account type (LD-A0012). |
| LD-R0068 | LD-C0047 | provided_under | LD-C0071 | Legal form (title transfer or security interest) comes from the arrangement. |
| LD-R0069 | LD-C0047 | of_asset | LD-C0048 | Quantity of the asset, with market value and value after haircut as of a time. |
| LD-R0070 | LD-C0047 | held_for | LD-C0010 | Account or segregation unit for which the collateral is held. |
| LD-R0071 | LD-C0047 | covers | LD-C0043 | Same provider-taker pair, account, as-of time and currency basis; the difference is the excess or shortfall. |
| LD-R0072 | LD-C0072 | admits | LD-C0048 | Per schedule version, with haircut, limits and validity; eligibility is not commitment. |
| LD-R0073 | LD-C0071 | references | LD-C0072 | The eligibility schedule version applicable under the arrangement. |
| LD-R0074 | LD-C0049 | transfers | LD-C0048 | Asset quantities moved; LD-R0019 records the resulting change in collateral held. |
| LD-R0075 | LD-C0001 | member_of | LD-C0073 | Time-bound commercial grouping; never used for regulatory threshold or consolidation calculations (LD-A0031). |
| LD-R0076 | LD-C0074 | derived_from | LD-C0039 / LD-C0040 | Only under an approved semantic contract and cost perimeter; no formula approved. |
| LD-R0077 | LD-C0039 | attributed_to | LD-C0003 / LD-C0073 / LD-C0052 | Only under a semantic contract; observing entity, period and currency are mandatory. Revenue is attributed per service to that service's contractual client (sponsor decision 2026-11-01). |
| LD-R0078 | LD-C0031 | arises_from | LD-C0017 / LD-C0018 / LD-C0023 / LD-C0025 | The chargeable event; periodic charges arise from a period rather than an event. |
| LD-R0079 | LD-C0031 | charged_for | LD-C0052 | The service concerned; service nature is a mandatory facet. |
| LD-R0080 | LD-C0031 | recharges | LD-C0031 | A charge passed on to another debtor, for example executing brokerage paid by the clearing broker and recharged to the client; zero or more. |
| LD-R0081 | LD-C0003 | within_service | LD-C0051 / LD-C0052 | Zero or one; for example a Client role assignment within a Service Offering, a Clearing Member role within a Clearing Service. |
| LD-R0082 | LD-C0052 | relies_on | LD-C0051 / LD-C0009 | Through a market access arrangement; instances are internal-overlay facts. |
| LD-R0083 | LD-C0032 | applies_to | LD-C0052 / LD-C0051 / LD-C0009 / LD-C0062 | Versioned; issuer and effective period required; public tariffs and negotiated client terms are distinguished by issuer and scope. |

Collateral is linked to margin through Collateral Arrangement (LD-R0068), its asset (LD-R0069), its account (LD-R0070) and the requirement it covers (LD-R0071). The obligations an arrangement secures are stated in the arrangement; a standalone general Obligation concept is still not defined, so no relation targets one. Do not invent an unresolved target concept ID.

Relations added or relabelled by the 2026-11 expert review are listed in the [change log](../CHANGELOG.md). Union targets (`A / B`) are explicit declared ranges, not equivalence assertions. Further columns (source and target types, inverse label, temporal flag, status) are deferred until the hub reader parses tables by header; appending a column today would merge it into the conditions text.
