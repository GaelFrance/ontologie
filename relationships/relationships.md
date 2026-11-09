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
| LD-R0060 | LD-C0068 | classifies | LD-C0002 / LD-C0003 / LD-C0010 / LD-C0009 / LD-C0008 / LD-C0051 / LD-C0014 / LD-C0062 / LD-C0013 / LD-C0018 | Entity-level statuses attach to the legal entity, relationship-level statuses to the role assignment; never to the Client role generically or to a commercial group. A status the regime gives to a pair of counterparties (for example an intragroup exemption) attaches to both legal entities together, for the regime, product class and period, and is never read as a status of either one alone. Targets aligned with the definition 2026-11-09. |
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

## Level 2 relationships (2026-11 domain review)

Structure links (part of, step in, state of) and plain connections proposed by the domain experts. Draft; cardinalities not asserted.

| ID | Source concept | Relation | Target concept | Meaning and conditions |
|---|---|---|---|---|
| LD-R0084 | LD-C0075 | can_hold_the_role_of | LD-C0078 | — |
| LD-R0085 | LD-C0075 | can_hold_the_role_of | LD-C0004 | — |
| LD-R0086 | LD-C0076 | part_of | LD-C0002 | Level-2 structure (2026-11 domain review). |
| LD-R0087 | LD-C0076 | may_bring_the_business_under_a_further | LD-C0067 | — |
| LD-R0088 | LD-C0077 | is_managed_by | LD-C0079 | — |
| LD-R0089 | LD-C0077 | usually_holds_the_role_of | LD-C0004 | — |
| LD-R0090 | LD-C0078 | acts_for | LD-C0004 | — |
| LD-R0091 | LD-C0078 | sends | LD-C0016 | — |
| LD-R0092 | LD-C0078 | gives | LD-C0060 | — |
| LD-R0093 | LD-C0079 | manages | LD-C0077 | — |
| LD-R0094 | LD-C0079 | gives | LD-C0060 | — |
| LD-R0095 | LD-C0079 | often_anchors | LD-C0073 | — |
| LD-R0096 | LD-C0080 | bears_the_result_of_positions_in | LD-C0010 | — |
| LD-R0097 | LD-C0080 | is_often_an | LD-C0081 | — |
| LD-R0098 | LD-C0081 | is_cleared_within | LD-C0051 | — |
| LD-R0099 | LD-C0081 | may_be_recorded_in_indirect_client_accounts_of | LD-C0069 | — |
| LD-R0100 | LD-C0081 | reaches_clearing_through | LD-C0059 | — |
| LD-R0101 | LD-C0082 | part_of | LD-C0010 | Level-2 structure (2026-11 domain review). |
| LD-R0102 | LD-C0082 | is_used_to_route | LD-C0022 | — |
| LD-R0103 | LD-C0082 | is_issued_by | LD-C0001 | — |
| LD-R0104 | LD-C0083 | is_held_by_and_points_to_another | LD-C0002 | — |
| LD-R0105 | LD-C0083 | may_inform_but_never_defines | LD-C0073 | — |
| LD-R0106 | LD-C0083 | decides_whether_a_client_is | LD-C0085 | — |
| LD-R0107 | LD-C0084 | is_the_provider_toward | LD-C0004 | — |
| LD-R0108 | LD-C0084 | is_party_to | LD-C0012 | — |
| LD-R0109 | LD-C0084 | provides | LD-C0052 | — |
| LD-R0110 | LD-C0084 | is_the_observing_entity_for | LD-C0039 | — |
| LD-R0111 | LD-C0085 | is_determined_through | LD-C0083 | — |
| LD-R0112 | LD-C0085 | may_be_recorded_in_house_or_client_accounts_of | LD-C0069 | — |
| LD-R0113 | LD-C0085 | is_flagged_for_elimination_in | LD-C0039 | — |
| LD-R0114 | LD-C0086 | is_held_together_with | LD-C0058 | — |
| LD-R0115 | LD-C0086 | clears_through_a_general | LD-C0007 | — |
| LD-R0116 | LD-C0086 | is_conferred_by | LD-C0059 | — |
| LD-R0117 | LD-C0087 | is_sponsored_by | LD-C0157 | — |
| LD-R0118 | LD-C0087 | is_admitted_under | LD-C0115 | — |
| LD-R0119 | LD-C0087 | normally_also_holds_toward_its_sponsor | LD-C0004 | — |
| LD-R0120 | LD-C0088 | classifies | LD-C0004 | — |
| LD-R0121 | LD-C0088 | is_assigned_by | LD-C0084 | — |
| LD-R0122 | LD-C0088 | is_defined_under | LD-C0067 | — |
| LD-R0123 | LD-C0089 | classifies | LD-C0002 | — |
| LD-R0124 | LD-C0089 | is_defined_under | LD-C0067 | — |
| LD-R0125 | LD-C0090 | is_held_for | LD-C0004 | — |
| LD-R0126 | LD-C0090 | is_mapped_to | LD-C0069 | — |
| LD-R0127 | LD-C0090 | is_targeted_by | LD-C0020 | — |
| LD-R0128 | LD-C0090 | records | LD-C0026 | — |
| LD-R0129 | LD-C0091 | operates | LD-C0009 | — |
| LD-R0130 | LD-C0091 | issues | LD-C0194 | — |
| LD-R0131 | LD-C0091 | issues | LD-C0175 | — |
| LD-R0132 | LD-C0092 | maintains | LD-C0213 | — |
| LD-R0133 | LD-C0092 | evidences | LD-C0049 | — |
| LD-R0134 | LD-C0092 | evidences | LD-C0029 | — |
| LD-R0135 | LD-C0093 | is_the_scheme_of | LD-C0082 | — |
| LD-R0136 | LD-C0093 | identifies_through_lei | LD-C0002 | — |
| LD-R0137 | LD-C0093 | provides_matching_keys_for | LD-C0205 | — |
| LD-R0138 | LD-C0094 | part_of | LD-C0009 | Level-2 structure (2026-11 domain review). |
| LD-R0139 | LD-C0094 | lists_contracts_of | LD-C0062 | — |
| LD-R0140 | LD-C0094 | can_have_its_own_fee_schedule | LD-C0032 | — |
| LD-R0141 | LD-C0094 | can_carry_its_own_regulatory_classification | LD-C0068 | — |
| LD-R0142 | LD-C0094 | can_have_its_own_calendar_or_sessions | LD-C0066 | — |
| LD-R0143 | LD-C0095 | has_leg | LD-C0014 | Each leg states its instrument, ratio and side. Corrected 2026-11-09 (was a strategy made of strategies). |
| LD-R0144 | LD-C0095 | is_executed_as_one_execution_per_leg | LD-C0017 | — |
| LD-R0145 | LD-C0095 | results_in_positions_in_its_legs | LD-C0026 | — |
| LD-R0146 | LD-C0095 | may_be_charged_per_leg_or_per_strategy_by_venue_rule | LD-C0036 | — |
| LD-R0147 | LD-C0096 | is_created_within_the_limits_of | LD-C0062 | — |
| LD-R0148 | LD-C0096 | may_have_its_own_eligibility_in | LD-C0051 | — |
| LD-R0149 | LD-C0096 | may_have_its_own_fees_under | LD-C0032 | — |
| LD-R0150 | LD-C0097 | part_of | LD-C0062 | Level-2 structure (2026-11 domain review). |
| LD-R0151 | LD-C0097 | drives_the_classification_of | LD-C0013 | — |
| LD-R0152 | LD-C0097 | can_itself_be_option_on_a_future | LD-C0014 | — |
| LD-R0153 | LD-C0097 | corporate_events_on_it_can_trigger | LD-C0099 | — |
| LD-R0154 | LD-C0097 | its_market_s_holidays_can_close_a_contract | LD-C0066 | — |
| LD-R0155 | LD-C0098 | part_of | LD-C0062 | Level-2 structure (2026-11 domain review). |
| LD-R0156 | LD-C0098 | is_resolved_against | LD-C0066 | — |
| LD-R0157 | LD-C0098 | produces_key_dates_of | LD-C0015 | — |
| LD-R0158 | LD-C0098 | gives_each_series_its_key_dates | LD-C0014 | — |
| LD-R0159 | LD-C0098 | is_changed_by_and_a_calendar_change_can_move_its_results | LD-C0064 | — |
| LD-R0160 | LD-C0099 | changes_or_creates | LD-C0014 | — |
| LD-R0161 | LD-C0099 | is_triggered_by_an_event_on | LD-C0097 | — |
| LD-R0162 | LD-C0099 | changes_the_terms_of_positions_in | LD-C0026 | — |
| LD-R0163 | LD-C0099 | is_announced_by | LD-C0197 | A market notice or clearing advisory announces the adjustment; the adjustment is not itself a rule change. Corrected 2026-11-09 (target was Rule Change). |
| LD-R0164 | LD-C0100 | part_of | LD-C0051 | Level-2 structure (2026-11 domain review). |
| LD-R0165 | LD-C0100 | maps_one_or_more_of | LD-C0062 | — |
| LD-R0166 | LD-C0100 | is_the_contract_in_which_positions_are_held | LD-C0026 | — |
| LD-R0167 | LD-C0100 | is_margined_under | LD-C0070 | — |
| LD-R0168 | LD-C0100 | is_listed_in | LD-C0101 | — |
| LD-R0169 | LD-C0101 | part_of | LD-C0051 | Level-2 structure (2026-11 domain review). |
| LD-R0170 | LD-C0101 | lists_as_eligible | LD-C0062 | — |
| LD-R0171 | LD-C0101 | lists_as_eligible_with_trade_term_ranges_otc | LD-C0013 | — |
| LD-R0172 | LD-C0101 | is_changed_by | LD-C0064 | — |
| LD-R0173 | LD-C0101 | is_relied_on_by_never_equal_to | LD-C0052 | — |
| LD-R0174 | LD-C0102 | part_of | LD-C0066 | Level-2 structure (2026-11 domain review). |
| LD-R0175 | LD-C0102 | assigns_trade_dates_of | LD-C0015 | — |
| LD-R0176 | LD-C0102 | is_defined_by | LD-C0009 | — |
| LD-R0177 | LD-C0102 | positions_cut_offs_relative_to | LD-C0065 | — |
| LD-R0178 | LD-C0102 | is_changed_by_hours_extensions | LD-C0064 | — |
| LD-R0179 | LD-C0103 | state_of | LD-C0014 | Level-2 structure (2026-11 domain review). |
| LD-R0180 | LD-C0103 | may_be_published_per_series_of | LD-C0100 | — |
| LD-R0181 | LD-C0103 | values_listed_positions_for | LD-C0045 | — |
| LD-R0182 | LD-C0103 | is_used_in_its_final_kind_by | LD-C0220 | — |
| LD-R0183 | LD-C0104 | part_of | LD-C0066 | Level-2 structure (2026-11 domain review). |
| LD-R0184 | LD-C0104 | frames | LD-C0065 | — |
| LD-R0185 | LD-C0104 | dates | LD-C0206 | — |
| LD-R0186 | LD-C0104 | dates | LD-C0161 | — |
| LD-R0187 | LD-C0104 | dates | LD-C0026 | — |
| LD-R0188 | LD-C0105 | part_of | LD-C0052 | Level-2 structure (2026-11 domain review). |
| LD-R0189 | LD-C0105 | is_priced_by_for_the_firm_s_own_client_charges | LD-C0177 | — |
| LD-R0190 | LD-C0106 | part_of | LD-C0052 | Level-2 structure (2026-11 domain review). |
| LD-R0191 | LD-C0106 | relies_on | LD-C0059 | — |
| LD-R0192 | LD-C0106 | covers_trading_on | LD-C0009 | — |
| LD-R0193 | LD-C0106 | covers_clearing_in | LD-C0051 | — |
| LD-R0194 | LD-C0106 | states_its_product_scope_by | LD-C0062 | — |
| LD-R0195 | LD-C0106 | is_available_through | LD-C0061 | — |
| LD-R0196 | LD-C0107 | applies_to | LD-C0052 | — |
| LD-R0197 | LD-C0107 | is_tested_against | LD-C0004 | — |
| LD-R0198 | LD-C0107 | may_require_a_stated_value_of | LD-C0068 | — |
| LD-R0199 | LD-C0108 | documents | LD-C0059 | — |
| LD-R0200 | LD-C0108 | is_distinct_from | LD-C0055 | — |
| LD-R0201 | LD-C0108 | is_distinct_from | LD-C0056 | — |
| LD-R0202 | LD-C0109 | step_in | LD-C0059 | Level-2 structure (2026-11 domain review). |
| LD-R0203 | LD-C0109 | must_satisfy | LD-C0110 | — |
| LD-R0204 | LD-C0109 | sets_up | LD-C0111 | — |
| LD-R0205 | LD-C0110 | must_be_met_for | LD-C0059 | — |
| LD-R0206 | LD-C0110 | may_require | LD-C0202 | — |
| LD-R0207 | LD-C0110 | may_implement | LD-C0190 | — |
| LD-R0208 | LD-C0110 | may_require | LD-C0172 | — |
| LD-R0209 | LD-C0111 | part_of | LD-C0059 | Level-2 structure (2026-11 domain review). |
| LD-R0210 | LD-C0111 | generates_cost_of_category_connectivity_and_market_data | LD-C0040 | — |
| LD-R0211 | LD-C0112 | is_granted_by_the_client_s | LD-C0058 | — |
| LD-R0212 | LD-C0112 | is_the_standing_permission_behind_orders_on_the_channels_direct_market_access_and_sponsored_access | LD-C0061 | — |
| LD-R0213 | LD-C0112 | is_subject_to_controls_set_as | LD-C0110 | — |
| LD-R0214 | LD-C0113 | is_intermediated_by_the_venue_member_role_of | LD-C0058 | — |
| LD-R0215 | LD-C0113 | lets_the_firm_act_as_the_client_s_executing_broker_while_another_party_is_the_venue_member_so_it_never_implies | LD-C0006 | — |
| LD-R0216 | LD-C0113 | gives_rise_to_brokerage_owed_to_the_intermediary | LD-C0035 | — |
| LD-R0217 | LD-C0114 | grants_clearing_access_to | LD-C0051 | — |
| LD-R0218 | LD-C0114 | is_intermediated_by_the_general_clearing_member_role_of | LD-C0007 | — |
| LD-R0219 | LD-C0114 | confers | LD-C0086 | — |
| LD-R0220 | LD-C0115 | grants_clearing_access_to | LD-C0051 | — |
| LD-R0221 | LD-C0115 | confers | LD-C0087 | — |
| LD-R0222 | LD-C0115 | may_open_in_the_participant_s_name_a | LD-C0069 | — |
| LD-R0223 | LD-C0115 | is_intermediated_by_the_sponsoring | LD-C0007 | — |
| LD-R0224 | LD-C0116 | grants_clearing_access_to | LD-C0051 | — |
| LD-R0225 | LD-C0116 | confers | LD-C0081 | — |
| LD-R0226 | LD-C0116 | is_documented_at_each_link_by_a | LD-C0056 | — |
| LD-R0227 | LD-C0116 | offers_account_options_governed_by | LD-C0011 | — |
| LD-R0228 | LD-C0117 | is_given_by | LD-C0004 | — |
| LD-R0229 | LD-C0117 | is_received_by | LD-C0006 | — |
| LD-R0230 | LD-C0117 | has_at_each_point_in_time_a | LD-C0061 | — |
| LD-R0231 | LD-C0117 | is_worked_through | LD-C0118 | — |
| LD-R0232 | LD-C0117 | is_filled_by | LD-C0121 | — |
| LD-R0233 | LD-C0118 | is_derived_from | LD-C0117 | — |
| LD-R0234 | LD-C0118 | is_entered_on_the_venue_by | LD-C0058 | — |
| LD-R0235 | LD-C0118 | is_submitted_to | LD-C0009 | — |
| LD-R0236 | LD-C0118 | is_filled_by | LD-C0120 | — |
| LD-R0237 | LD-C0118 | may_be_routed_through | LD-C0130 | — |
| LD-R0238 | LD-C0119 | step_in | LD-C0016 | Level-2 structure (2026-11 domain review). |
| LD-R0239 | LD-C0119 | may_apply | LD-C0138 | — |
| LD-R0240 | LD-C0119 | requires_for_direct_market_access_or_sponsored_access_orders_a_live | LD-C0112 | — |
| LD-R0241 | LD-C0120 | fills | LD-C0118 | — |
| LD-R0242 | LD-C0120 | occurs_on | LD-C0009 | — |
| LD-R0243 | LD-C0120 | gives_rise_to | LD-C0126 | — |
| LD-R0244 | LD-C0120 | can_give_rise_to | LD-C0036 | — |
| LD-R0245 | LD-C0121 | fills | LD-C0117 | — |
| LD-R0246 | LD-C0121 | reflects_one_or_more | LD-C0120 | — |
| LD-R0247 | LD-C0121 | may_be_priced_through | LD-C0021 | — |
| LD-R0248 | LD-C0121 | is_the_basis_of | LD-C0033 | — |
| LD-R0249 | LD-C0121 | is_split_by | LD-C0020 | — |
| LD-R0250 | LD-C0122 | is_registered_on | LD-C0009 | — |
| LD-R0251 | LD-C0122 | has_minimum_size_set_per | LD-C0062 | — |
| LD-R0252 | LD-C0122 | is_governed_by | LD-C0063 | — |
| LD-R0253 | LD-C0122 | can_be_given_up_like_any_other_execution | LD-C0022 | — |
| LD-R0254 | LD-C0123 | is_registered_on | LD-C0009 | — |
| LD-R0255 | LD-C0123 | is_governed_by | LD-C0063 | — |
| LD-R0256 | LD-C0123 | is_linked_to_the_trade_in_the_related_position_which_is_not_a_listed_trade | LD-C0018 | — |
| LD-R0257 | LD-C0124 | is_produced_with | LD-C0120 | — |
| LD-R0258 | LD-C0124 | is_in_the_leg | LD-C0014 | — |
| LD-R0259 | LD-C0124 | is_usually_allocated_per_leg_by | LD-C0020 | — |
| LD-R0260 | LD-C0125 | refers_to_the_original | LD-C0017 | — |
| LD-R0261 | LD-C0125 | is_governed_by_the_venue_s_error_trade_rules_in | LD-C0063 | — |
| LD-R0262 | LD-C0125 | may_raise | LD-C0030 | — |
| LD-R0263 | LD-C0126 | is_formed_by | LD-C0120 | — |
| LD-R0264 | LD-C0126 | is_succeeded_by | LD-C0143 | — |
| LD-R0265 | LD-C0126 | is_succeeded_by_under_the_principal_model | LD-C0144 | — |
| LD-R0266 | LD-C0126 | may_be_given_up_through | LD-C0022 | — |
| LD-R0267 | LD-C0127 | part_of | LD-C0021 | Level-2 structure (2026-11 domain review). |
| LD-R0268 | LD-C0127 | may_give_rise_to_a_settlement_obligation_settled_by_a_cash_movement | LD-C0028 | — |
| LD-R0269 | LD-C0128 | is_often_agreed_alongside | LD-C0055 | — |
| LD-R0270 | LD-C0128 | drives | LD-C0020 | — |
| LD-R0271 | LD-C0129 | part_of | LD-C0020 | Level-2 structure (2026-11 domain review). |
| LD-R0272 | LD-C0129 | targets | LD-C0010 | — |
| LD-R0273 | LD-C0129 | gives_rise_to_when_routed_to_another_clearing_member | LD-C0131 | — |
| LD-R0274 | LD-C0129 | must_be_completed_by | LD-C0065 | — |
| LD-R0275 | LD-C0130 | acts_for | LD-C0006 | — |
| LD-R0276 | LD-C0130 | is_admitted_to | LD-C0009 | — |
| LD-R0277 | LD-C0130 | is_the_intermediary_of | LD-C0113 | — |
| LD-R0278 | LD-C0130 | is_owed | LD-C0035 | — |
| LD-R0279 | LD-C0131 | part_of | LD-C0022 | Level-2 structure (2026-11 domain review). |
| LD-R0280 | LD-C0131 | is_created_from | LD-C0129 | — |
| LD-R0281 | LD-C0131 | carries_out_part_of | LD-C0060 | — |
| LD-R0282 | LD-C0131 | concerns_a_quantity_of | LD-C0018 | — |
| LD-R0283 | LD-C0131 | names | LD-C0135 | — |
| LD-R0284 | LD-C0131 | is_answered_by | LD-C0053 | — |
| LD-R0285 | LD-C0131 | is_completed_by | LD-C0139 | — |
| LD-R0286 | LD-C0132 | usually_relies_on | LD-C0138 | — |
| LD-R0287 | LD-C0132 | coincides_with | LD-C0023 | — |
| LD-R0288 | LD-C0133 | is_carried_meanwhile_by | LD-C0134 | — |
| LD-R0289 | LD-C0133 | must_finish_before | LD-C0140 | — |
| LD-R0290 | LD-C0133 | ends_with | LD-C0139 | — |
| LD-R0291 | LD-C0134 | clears_for | LD-C0006 | — |
| LD-R0292 | LD-C0134 | gives_up_in | LD-C0022 | — |
| LD-R0293 | LD-C0134 | holds_the_trade_in_until_registration_to_the_receiving_member | LD-C0069 | Per quantity: the giving member keeps each quantity in its CCP account until the CCP records it in the receiving member's account; a take-up decision alone does not move it. Corrected 2026-11-09 (was until take-up). |
| LD-R0294 | LD-C0135 | acts_for | LD-C0057 | — |
| LD-R0295 | LD-C0135 | decides | LD-C0053 | — |
| LD-R0296 | LD-C0135 | receives_the_trade_in | LD-C0069 | — |
| LD-R0297 | LD-C0136 | answers | LD-C0131 | — |
| LD-R0298 | LD-C0136 | may_be_applied_automatically_within | LD-C0138 | — |
| LD-R0299 | LD-C0136 | is_checked_against | LD-C0055 | — |
| LD-R0300 | LD-C0137 | answers | LD-C0141 | — |
| LD-R0301 | LD-C0137 | applies | LD-C0138 | — |
| LD-R0302 | LD-C0137 | precedes | LD-C0023 | — |
| LD-R0303 | LD-C0138 | may_be_referred_to_in | LD-C0055 | — |
| LD-R0304 | LD-C0138 | may_be_allowed_by | LD-C0056 | — |
| LD-R0305 | LD-C0138 | may_be_applied_by | LD-C0119 | — |
| LD-R0306 | LD-C0138 | is_applied_in | LD-C0136 | — |
| LD-R0307 | LD-C0138 | is_applied_in | LD-C0137 | — |
| LD-R0308 | LD-C0139 | step_in | LD-C0022 | Level-2 structure (2026-11 domain review). |
| LD-R0309 | LD-C0139 | records_the_quantity_in | LD-C0069 | — |
| LD-R0310 | LD-C0139 | changes | LD-C0026 | — |
| LD-R0311 | LD-C0140 | applies_to | LD-C0022 | — |
| LD-R0312 | LD-C0140 | is_set_against | LD-C0066 | — |
| LD-R0313 | LD-C0141 | concerns | LD-C0018 | — |
| LD-R0314 | LD-C0141 | targets | LD-C0051 | — |
| LD-R0315 | LD-C0141 | is_answered_by | LD-C0137 | — |
| LD-R0316 | LD-C0141 | leads_to | LD-C0023 | — |
| LD-R0317 | LD-C0142 | governs | LD-C0141 | — |
| LD-R0318 | LD-C0142 | is_the_otc_counterpart_of | LD-C0055 | — |
| LD-R0319 | LD-C0142 | works_alongside | LD-C0056 | — |
| LD-R0320 | LD-C0143 | is_created_by | LD-C0054 | — |
| LD-R0321 | LD-C0143 | is_recorded_in | LD-C0069 | — |
| LD-R0322 | LD-C0143 | is_governed_by_the_rules_of | LD-C0051 | — |
| LD-R0323 | LD-C0143 | is_mirrored_under_the_principal_model_by | LD-C0144 | — |
| LD-R0324 | LD-C0143 | makes_up | LD-C0026 | — |
| LD-R0325 | LD-C0144 | arises_under | LD-C0056 | — |
| LD-R0326 | LD-C0144 | mirrors | LD-C0143 | — |
| LD-R0327 | LD-C0144 | has_as_one_party | LD-C0057 | — |
| LD-R0328 | LD-C0144 | has_as_the_other_party | LD-C0004 | — |
| LD-R0329 | LD-C0145 | is_held_in_the_name_of | LD-C0007 | — |
| LD-R0330 | LD-C0145 | is_opened_within | LD-C0051 | — |
| LD-R0331 | LD-C0145 | may_contain | LD-C0149 | — |
| LD-R0332 | LD-C0146 | is_held_in_the_name_of | LD-C0007 | — |
| LD-R0333 | LD-C0146 | applies | LD-C0011 | — |
| LD-R0334 | LD-C0146 | contains_when_gross | LD-C0149 | — |
| LD-R0335 | LD-C0146 | is_mapped_from_the_clients_internal_accounts | LD-C0010 | — |
| LD-R0336 | LD-C0147 | is_held_in_the_name_of | LD-C0007 | — |
| LD-R0337 | LD-C0147 | is_opened_following | LD-C0150 | — |
| LD-R0338 | LD-C0147 | holds_collateral_attributed_to_one_client | LD-C0047 | — |
| LD-R0339 | LD-C0148 | is_held_in_the_name_of | LD-C0007 | — |
| LD-R0340 | LD-C0148 | results_from_an_indirect_clearing_access_arrangement | LD-C0059 | — |
| LD-R0341 | LD-C0149 | part_of | LD-C0069 | Level-2 structure (2026-11 domain review). |
| LD-R0342 | LD-C0149 | records | LD-C0026 | — |
| LD-R0343 | LD-C0149 | is_mapped_from_internal_client_accounts | LD-C0010 | — |
| LD-R0344 | LD-C0149 | receives_given_up_trades_designated_by_a_give_up_reference | LD-C0022 | — |
| LD-R0345 | LD-C0150 | part_of | LD-C0056 | Level-2 structure (2026-11 domain review). |
| LD-R0346 | LD-C0150 | selects_one_option_of | LD-C0011 | — |
| LD-R0347 | LD-C0150 | determines_the_kind_of | LD-C0069 | — |
| LD-R0348 | LD-C0150 | is_made_per | LD-C0051 | — |
| LD-R0349 | LD-C0150 | is_made_by | LD-C0004 | — |
| LD-R0350 | LD-C0151 | is_held_in | LD-C0014 | — |
| LD-R0351 | LD-C0151 | is_recorded_in | LD-C0149 | — |
| LD-R0352 | LD-C0151 | is_compared_in_position_reconciliation | LD-C0050 | — |
| LD-R0353 | LD-C0152 | is_made_of | LD-C0143 | — |
| LD-R0354 | LD-C0152 | is_recorded_in | LD-C0069 | — |
| LD-R0355 | LD-C0152 | may_be_included_in_a_margin_portfolio | LD-C0027 | — |
| LD-R0356 | LD-C0153 | moves_positions_from_and_to | LD-C0069 | — |
| LD-R0357 | LD-C0153 | changes | LD-C0026 | — |
| LD-R0358 | LD-C0153 | may_give_rise_to_a_transfer_fee | LD-C0031 | — |
| LD-R0359 | LD-C0153 | is_not | LD-C0022 | — |
| LD-R0360 | LD-C0154 | may_use | LD-C0172 | — |
| LD-R0361 | LD-C0154 | may_start | LD-C0155 | — |
| LD-R0362 | LD-C0155 | step_in | LD-C0154 | Level-2 structure (2026-11 domain review). |
| LD-R0363 | LD-C0155 | transfers_to | LD-C0156 | — |
| LD-R0364 | LD-C0155 | moves_the_content_of | LD-C0069 | — |
| LD-R0365 | LD-C0155 | moves_as_a_separate_leg | LD-C0047 | — |
| LD-R0366 | LD-C0155 | depends_on_the_segregation_applied_to | LD-C0011 | — |
| LD-R0367 | LD-C0156 | receives_positions_by | LD-C0155 | — |
| LD-R0368 | LD-C0156 | is_named_by | LD-C0004 | — |
| LD-R0369 | LD-C0156 | is_held_per | LD-C0051 | — |
| LD-R0370 | LD-C0157 | sponsors | LD-C0087 | — |
| LD-R0371 | LD-C0157 | acts_under | LD-C0115 | — |
| LD-R0372 | LD-C0157 | may_pay_for_the_participant | LD-C0172 | — |
| LD-R0373 | LD-C0158 | changes | LD-C0026 | — |
| LD-R0374 | LD-C0158 | applies_within | LD-C0069 | — |
| LD-R0375 | LD-C0158 | must_be_done_before | LD-C0065 | — |
| LD-R0376 | LD-C0159 | arises_under | LD-C0056 | — |
| LD-R0377 | LD-C0159 | ends | LD-C0144 | — |
| LD-R0378 | LD-C0159 | may_use | LD-C0047 | — |
| LD-R0379 | LD-C0160 | part_of | LD-C0070 | Level-2 structure (2026-11 domain review). |
| LD-R0380 | LD-C0160 | is_changed_by_a_rule_change | LD-C0064 | — |
| LD-R0381 | LD-C0160 | is_published_for_a_clearing_service | LD-C0051 | — |
| LD-R0382 | LD-C0160 | is_applied_in_a_margin_run | LD-C0161 | — |
| LD-R0383 | LD-C0161 | determines | LD-C0043 | A margin run states margin requirements as of its run time. Corrected 2026-11-09 (was step_in: a run is not a step of a measure). |
| LD-R0384 | LD-C0161 | applies | LD-C0070 | — |
| LD-R0385 | LD-C0161 | uses | LD-C0160 | — |
| LD-R0386 | LD-C0161 | may_lead_to | LD-C0046 | — |
| LD-R0387 | LD-C0161 | is_calculated_over | LD-C0164 | — |
| LD-R0388 | LD-C0162 | part_of | LD-C0043 | Level-2 structure (2026-11 domain review). |
| LD-R0389 | LD-C0162 | breaks_down | LD-C0044 | — |
| LD-R0390 | LD-C0163 | part_of | LD-C0070 | Level-2 structure (2026-11 domain review). |
| LD-R0391 | LD-C0163 | is_agreed_or_notified_under | LD-C0056 | — |
| LD-R0392 | LD-C0163 | applies_to | LD-C0004 | — |
| LD-R0393 | LD-C0164 | is_defined_within_or_across | LD-C0069 | — |
| LD-R0394 | LD-C0164 | contains | LD-C0026 | — |
| LD-R0395 | LD-C0164 | is_the_scope_of | LD-C0043 | — |
| LD-R0396 | LD-C0165 | part_of | LD-C0071 | Level-2 structure (2026-11 domain review). |
| LD-R0397 | LD-C0165 | may_be_set_in | LD-C0056 | — |
| LD-R0398 | LD-C0165 | names_the_deadline_as | LD-C0065 | — |
| LD-R0399 | LD-C0165 | governs | LD-C0046 | — |
| LD-R0400 | LD-C0166 | state_of | LD-C0043 | Level-2 structure (2026-11 domain review). |
| LD-R0401 | LD-C0166 | compares | LD-C0047 | — |
| LD-R0402 | LD-C0166 | may_give_rise_to | LD-C0046 | — |
| LD-R0403 | LD-C0166 | may_be_held_at | LD-C0069 | — |
| LD-R0404 | LD-C0167 | part_of | LD-C0072 | Level-2 structure (2026-11 domain review). |
| LD-R0405 | LD-C0167 | applies_to | LD-C0048 | — |
| LD-R0406 | LD-C0167 | gives_the_value_after_haircut_of | LD-C0047 | — |
| LD-R0407 | LD-C0167 | is_changed_by | LD-C0064 | — |
| LD-R0408 | LD-C0168 | part_of | LD-C0072 | Level-2 structure (2026-11 domain review). |
| LD-R0409 | LD-C0168 | applies_to | LD-C0048 | — |
| LD-R0410 | LD-C0168 | limits_the_value_of | LD-C0047 | — |
| LD-R0411 | LD-C0169 | step_in | LD-C0049 | Level-2 structure (2026-11 domain review). |
| LD-R0412 | LD-C0169 | is_made_under | LD-C0071 | — |
| LD-R0413 | LD-C0169 | may_respond_to | LD-C0046 | — |
| LD-R0414 | LD-C0170 | offsets_funding_effect_of | LD-C0045 | Never part of the variation margin amount; owed as a separate obligation even when paid together with it. Corrected 2026-11-09 (was part_of). |
| LD-R0415 | LD-C0170 | gives_rise_to | LD-C0028 | — |
| LD-R0416 | LD-C0170 | counts_in_only_if_the_management_reporting_basis_says_so | LD-C0187 | — |
| LD-R0417 | LD-C0171 | part_of | LD-C0071 | Level-2 structure (2026-11 domain review). |
| LD-R0418 | LD-C0171 | accrues_on | LD-C0047 | — |
| LD-R0419 | LD-C0171 | gives_rise_to | LD-C0028 | — |
| LD-R0420 | LD-C0171 | feeds | LD-C0187 | — |
| LD-R0421 | LD-C0172 | part_of | LD-C0051 | Level-2 structure (2026-11 domain review). |
| LD-R0422 | LD-C0172 | is_owed_by_the_holder_of | LD-C0007 | — |
| LD-R0423 | LD-C0172 | may_be_paid_by | LD-C0157 | — |
| LD-R0424 | LD-C0172 | may_be_required_by | LD-C0110 | — |
| LD-R0425 | LD-C0172 | is_covered_by | LD-C0047 | — |
| LD-R0426 | LD-C0172 | gives_rise_to_a_funding_cost_in | LD-C0040 | — |
| LD-R0427 | LD-C0173 | owes | LD-C0043 | — |
| LD-R0428 | LD-C0173 | faces | LD-C0174 | — |
| LD-R0429 | LD-C0174 | applies | LD-C0070 | — |
| LD-R0430 | LD-C0174 | issues | LD-C0046 | — |
| LD-R0431 | LD-C0175 | is_changed_by | LD-C0064 | — |
| LD-R0432 | LD-C0175 | applies_to | LD-C0009 | — |
| LD-R0433 | LD-C0175 | applies_to | LD-C0051 | — |
| LD-R0434 | LD-C0175 | applies_to | LD-C0062 | — |
| LD-R0435 | LD-C0175 | is_published_alongside | LD-C0063 | — |
| LD-R0436 | LD-C0176 | is_documented_in_or_under | LD-C0012 | — |
| LD-R0437 | LD-C0176 | is_agreed_for | LD-C0052 | — |
| LD-R0438 | LD-C0176 | is_agreed_with | LD-C0004 | — |
| LD-R0439 | LD-C0176 | may_be_agreed_at_the_level_of | LD-C0073 | — |
| LD-R0440 | LD-C0176 | may_set_brokerage_terms_together_with | LD-C0055 | — |
| LD-R0441 | LD-C0177 | part_of | LD-C0032 | Level-2 structure (2026-11 domain review). |
| LD-R0442 | LD-C0177 | determines_the_amount_of | LD-C0031 | — |
| LD-R0443 | LD-C0177 | may_be_tiered_by | LD-C0186 | — |
| LD-R0444 | LD-C0177 | may_be_changed_by | LD-C0064 | — |
| LD-R0445 | LD-C0178 | part_of | LD-C0032 | Level-2 structure (2026-11 domain review). |
| LD-R0446 | LD-C0178 | gives_rise_to | LD-C0182 | — |
| LD-R0447 | LD-C0178 | is_joined_by | LD-C0058 | — |
| LD-R0448 | LD-C0178 | is_introduced_or_changed_by | LD-C0064 | — |
| LD-R0449 | LD-C0179 | may_pass_on | LD-C0036 | — |
| LD-R0450 | LD-C0179 | may_pass_on | LD-C0037 | — |
| LD-R0451 | LD-C0179 | may_pass_on | LD-C0035 | — |
| LD-R0452 | LD-C0179 | may_pass_on | LD-C0181 | — |
| LD-R0453 | LD-C0179 | is_shown_gross_or_net_according_to | LD-C0188 | — |
| LD-R0454 | LD-C0180 | is_charged_for_with_service_kind_execute_and_clear | LD-C0052 | — |
| LD-R0455 | LD-C0180 | is_a_candidate_reading_of | LD-C0038 | — |
| LD-R0456 | LD-C0180 | is_split_according_to | LD-C0188 | — |
| LD-R0457 | LD-C0181 | is_owed_to_including_a_self_regulatory_organisation | LD-C0203 | — |
| LD-R0458 | LD-C0182 | is_owed_under | LD-C0178 | — |
| LD-R0459 | LD-C0182 | is_settled_by | LD-C0029 | — |
| LD-R0460 | LD-C0182 | is_netted_or_shown_gross_according_to | LD-C0188 | — |
| LD-R0461 | LD-C0183 | step_in | LD-C0031 | Level-2 structure (2026-11 domain review). |
| LD-R0462 | LD-C0183 | may_be_shown_on | LD-C0184 | — |
| LD-R0463 | LD-C0183 | may_resolve | LD-C0030 | — |
| LD-R0464 | LD-C0184 | step_in | LD-C0031 | Level-2 structure (2026-11 domain review). |
| LD-R0465 | LD-C0184 | may_be_issued_by | LD-C0185 | — |
| LD-R0466 | LD-C0184 | gives_rise_to | LD-C0028 | — |
| LD-R0467 | LD-C0184 | is_settled_by | LD-C0029 | — |
| LD-R0468 | LD-C0184 | is_checked_by_a_fee_reconciliation | LD-C0050 | — |
| LD-R0469 | LD-C0185 | collects_on_behalf_of_the_creditor | LD-C0031 | — |
| LD-R0470 | LD-C0185 | may_issue | LD-C0184 | — |
| LD-R0471 | LD-C0186 | may_set_the_tier_of | LD-C0177 | — |
| LD-R0472 | LD-C0186 | may_decide_eligibility_under | LD-C0178 | — |
| LD-R0473 | LD-C0186 | counts | LD-C0017 | — |
| LD-R0474 | LD-C0186 | counts | LD-C0023 | — |
| LD-R0475 | LD-C0187 | is_built_in_part_from | LD-C0171 | — |
| LD-R0476 | LD-C0187 | is_defined_by | LD-C0188 | — |
| LD-R0477 | LD-C0188 | part_of | LD-C0039 | Level-2 structure (2026-11 domain review). |
| LD-R0478 | LD-C0040 | is_measured_under | LD-C0188 | Corrected 2026-11-09 (direction was reversed). |
| LD-R0479 | LD-C0074 | is_measured_under | LD-C0188 | Corrected 2026-11-09 (direction was reversed). |
| LD-R0480 | LD-C0188 | rolls_revenue_up_to | LD-C0073 | — |
| LD-R0481 | LD-C0188 | sets_the_date_role_of | LD-C0015 | — |
| LD-R0482 | LD-C0189 | part_of | LD-C0074 | Level-2 structure (2026-11 domain review). |
| LD-R0483 | LD-C0189 | selects_categories_of | LD-C0040 | — |
| LD-R0484 | LD-C0189 | is_versioned_with | LD-C0188 | — |
| LD-R0485 | LD-C0190 | part_of | LD-C0067 | Level-2 structure (2026-11 domain review). |
| LD-R0486 | LD-C0190 | is_defined_in_one_or_more | LD-C0063 | — |
| LD-R0487 | LD-C0190 | applies_to_holders_of | LD-C0068 | — |
| LD-R0488 | LD-C0190 | is_held_by_parties_in | LD-C0003 | — |
| LD-R0489 | LD-C0190 | is_scoped_by | LD-C0192 | — |
| LD-R0490 | LD-C0190 | applies_through | LD-C0193 | — |
| LD-R0491 | LD-C0190 | can_be_relieved_by | LD-C0195 | — |
| LD-R0492 | LD-C0191 | covers_trades_in | LD-C0192 | — |
| LD-R0493 | LD-C0191 | applies_to_pairs_holding | LD-C0068 | — |
| LD-R0494 | LD-C0191 | is_met_through | LD-C0051 | — |
| LD-R0495 | LD-C0191 | applies_to | LD-C0018 | — |
| LD-R0496 | LD-C0191 | applies_through | LD-C0193 | — |
| LD-R0497 | LD-C0192 | part_of | LD-C0067 | Level-2 structure (2026-11 domain review). |
| LD-R0498 | LD-C0192 | is_defined_in | LD-C0063 | — |
| LD-R0499 | LD-C0192 | is_mapped_to_never_equal_to | LD-C0013 | — |
| LD-R0500 | LD-C0192 | is_the_value_of_product_level | LD-C0068 | — |
| LD-R0501 | LD-C0192 | sets_the_product_scope_of | LD-C0190 | — |
| LD-R0502 | LD-C0193 | part_of | LD-C0190 | Level-2 structure (2026-11 domain review). |
| LD-R0503 | LD-C0193 | can_also_stage | LD-C0064 | — |
| LD-R0504 | LD-C0194 | is_issued_by | LD-C0001 | — |
| LD-R0505 | LD-C0194 | governs | LD-C0051 | — |
| LD-R0506 | LD-C0194 | governs | LD-C0009 | — |
| LD-R0507 | LD-C0194 | is_changed_after | LD-C0199 | — |
| LD-R0508 | LD-C0195 | removes_or_defers | LD-C0190 | — |
| LD-R0509 | LD-C0195 | is_issued_by | LD-C0203 | — |
| LD-R0510 | LD-C0195 | can_depend_on | LD-C0068 | — |
| LD-R0511 | LD-C0196 | relates_two | LD-C0067 | — |
| LD-R0512 | LD-C0196 | is_a_condition_of | LD-C0202 | — |
| LD-R0513 | LD-C0196 | can_change_the_treatment_of_trades_on | LD-C0009 | — |
| LD-R0514 | LD-C0197 | announces | LD-C0064 | One notice can announce several rule changes and one change several notices. Corrected 2026-11-09 (was part_of). |
| LD-R0515 | LD-C0198 | step_in | LD-C0064 | Level-2 structure (2026-11 domain review). |
| LD-R0516 | LD-C0198 | is_opened_by | LD-C0197 | — |
| LD-R0517 | LD-C0198 | closes_on_a | LD-C0015 | — |
| LD-R0518 | LD-C0199 | step_in | LD-C0064 | Level-2 structure (2026-11 domain review). |
| LD-R0519 | LD-C0199 | is_decided_by | LD-C0203 | — |
| LD-R0520 | LD-C0199 | concerns_a_change_to | LD-C0194 | — |
| LD-R0521 | LD-C0200 | step_in | LD-C0064 | Level-2 structure (2026-11 domain review). |
| LD-R0522 | LD-C0200 | uses | LD-C0201 | — |
| LD-R0523 | LD-C0201 | part_of | LD-C0200 | Level-2 structure (2026-11 domain review). |
| LD-R0524 | LD-C0201 | is_a_reading_of | LD-C0063 | — |
| LD-R0525 | LD-C0202 | is_held_by | LD-C0002 | — |
| LD-R0526 | LD-C0202 | is_granted_under | LD-C0067 | — |
| LD-R0527 | LD-C0202 | is_granted_by | LD-C0203 | — |
| LD-R0528 | LD-C0202 | can_be_limited_to | LD-C0051 | — |
| LD-R0529 | LD-C0202 | can_depend_on | LD-C0196 | — |
| LD-R0530 | LD-C0203 | adopts_or_supervises | LD-C0067 | — |
| LD-R0531 | LD-C0203 | issues | LD-C0063 | — |
| LD-R0532 | LD-C0203 | grants | LD-C0202 | — |
| LD-R0533 | LD-C0203 | decides | LD-C0199 | — |
| LD-R0534 | LD-C0204 | is_defined_by | LD-C0190 | — |
| LD-R0535 | LD-C0204 | is_held_on | LD-C0017 | — |
| LD-R0536 | LD-C0204 | is_relied_on_by_delegated_reporting | LD-C0105 | — |
| LD-R0537 | LD-C0205 | is_compared_in | LD-C0050 | — |
| LD-R0538 | LD-C0205 | represents_for_example | LD-C0018 | — |
| LD-R0539 | LD-C0205 | represents_for_example | LD-C0026 | — |
| LD-R0540 | LD-C0205 | has_as_a_kind | LD-C0206 | — |
| LD-R0541 | LD-C0206 | is_issued_for | LD-C0051 | — |
| LD-R0542 | LD-C0206 | covers | LD-C0069 | — |
| LD-R0543 | LD-C0206 | is_the_counterpart_record_in | LD-C0050 | — |
| LD-R0544 | LD-C0206 | is_compared_in | LD-C0208 | — |
| LD-R0545 | LD-C0207 | part_of | LD-C0050 | Level-2 structure (2026-11 domain review). |
| LD-R0546 | LD-C0207 | concerns_two_or_more | LD-C0205 | — |
| LD-R0547 | LD-C0207 | may_raise | LD-C0030 | — |
| LD-R0548 | LD-C0207 | may_be_handled_in | LD-C0209 | — |
| LD-R0549 | LD-C0208 | uses | LD-C0206 | — |
| LD-R0550 | LD-C0208 | compares | LD-C0026 | — |
| LD-R0551 | LD-C0208 | is_keyed_by | LD-C0069 | — |
| LD-R0552 | LD-C0208 | produces | LD-C0207 | — |
| LD-R0553 | LD-C0209 | handles | LD-C0030 | One case can handle several exceptions. Corrected 2026-11-09 (was part_of). |
| LD-R0554 | LD-C0209 | may_concern | LD-C0207 | — |
| LD-R0555 | LD-C0209 | may_concern | LD-C0022 | — |
| LD-R0556 | LD-C0210 | state_of | LD-C0028 | Level-2 structure (2026-11 domain review). |
| LD-R0557 | LD-C0210 | is_assessed_against | LD-C0214 | — |
| LD-R0558 | LD-C0210 | may_raise | LD-C0030 | — |
| LD-R0559 | LD-C0211 | is_settled_by | LD-C0029 | — |
| LD-R0560 | LD-C0211 | is_stated_in | LD-C0206 | — |
| LD-R0561 | LD-C0212 | step_in | LD-C0028 | Level-2 structure (2026-11 domain review). |
| LD-R0562 | LD-C0212 | carries_out_for_cash_collateral | LD-C0169 | — |
| LD-R0563 | LD-C0213 | is_debited_or_credited_by | LD-C0029 | — |
| LD-R0564 | LD-C0213 | settles_obligations_of | LD-C0069 | — |
| LD-R0565 | LD-C0213 | is_named_in | LD-C0212 | — |
| LD-R0566 | LD-C0214 | applies_to | LD-C0028 | — |
| LD-R0567 | LD-C0214 | is_set_for_the_obligation_created_by | LD-C0046 | — |
| LD-R0568 | LD-C0214 | is_read_against | LD-C0066 | — |
| LD-R0569 | LD-C0215 | may_be_set_in | LD-C0056 | — |
| LD-R0570 | LD-C0215 | may_apply_to | LD-C0060 | — |
| LD-R0571 | LD-C0215 | may_apply_to | LD-C0218 | — |
| LD-R0572 | LD-C0216 | ends | LD-C0014 | — |
| LD-R0573 | LD-C0216 | closes | LD-C0026 | — |
| LD-R0574 | LD-C0216 | leads_to | LD-C0220 | — |
| LD-R0575 | LD-C0216 | may_lead_to | LD-C0217 | — |
| LD-R0576 | LD-C0217 | reduces_the_long | LD-C0026 | — |
| LD-R0577 | LD-C0217 | leads_to | LD-C0219 | — |
| LD-R0578 | LD-C0217 | is_requested_by | LD-C0218 | — |
| LD-R0579 | LD-C0217 | creates | LD-C0028 | — |
| LD-R0580 | LD-C0218 | step_in | LD-C0217 | Level-2 structure (2026-11 domain review). |
| LD-R0581 | LD-C0218 | must_arrive_before | LD-C0065 | — |
| LD-R0582 | LD-C0218 | may_be_subject_to | LD-C0215 | — |
| LD-R0583 | LD-C0219 | follows | LD-C0217 | — |
| LD-R0584 | LD-C0219 | reduces_the_short | LD-C0026 | — |
| LD-R0585 | LD-C0219 | creates | LD-C0028 | — |
| LD-R0586 | LD-C0220 | uses_the_final_kind_of | LD-C0103 | — |
| LD-R0587 | LD-C0221 | step_in | LD-C0220 | Level-2 structure (2026-11 domain review). |
| LD-R0588 | LD-C0221 | must_arrive_before | LD-C0065 | — |
| LD-R0589 | LD-C0221 | is_governed_by | LD-C0062 | — |
| LD-R0590 | LD-C0222 | changes_or_ends | LD-C0018 | — |
| LD-R0591 | LD-C0222 | may_change | LD-C0026 | — |
| LD-R0592 | LD-C0222 | may_raise | LD-C0030 | — |
| LD-R0593 | LD-C0065 | set_by | LD-C0063 / LD-C0012 | A cut-off is set by a rule provision or by a term of an agreement (sponsor decision 2026-11-01); only rule-set cut-offs follow the rule change lifecycle. |
| LD-R0594 | LD-C0223 | part_of | LD-C0225 | With the cash balance, gives total equity. |
| LD-R0595 | LD-C0224 | part_of | LD-C0225 | — |
| LD-R0596 | LD-C0166 | may_be_stated_against | LD-C0225 | Where the client agreement margins on account equity (mainly US futures), account equity is the held side compared with the requirement. |
| LD-R0597 | LD-C0223 | is_derived_from | LD-C0230 | Listed futures and futures-style options. |
| LD-R0598 | LD-C0230 | values | LD-C0026 | — |
| LD-R0599 | LD-C0230 | uses | LD-C0103 | Listed positions; cleared OTC positions are valued by the CCP's own valuation, not by a settlement price. |
| LD-R0600 | LD-C0045 | is_based_on | LD-C0230 | — |
| LD-R0601 | LD-C0226 | gives_rise_to | LD-C0028 | Premium-style options; futures-style options carry no upfront premium. |
| LD-R0602 | LD-C0226 | is_owed_on | LD-C0018 | The option trade. |
| LD-R0603 | LD-C0205 | has_as_a_kind | LD-C0227 | — |
| LD-R0604 | LD-C0227 | is_issued_by | LD-C0005 | Clearing or executing broker, to its client. |
| LD-R0605 | LD-C0227 | states | LD-C0225 | Also states the cash balance, open trade equity, margin requirement and excess or shortfall. |
| LD-R0606 | LD-C0228 | confirms | LD-C0121 | One execution, or the allocations made from it. |
| LD-R0607 | LD-C0228 | is_issued_by | LD-C0005 | — |
| LD-R0608 | LD-C0229 | set_by | LD-C0063 | A regulator's or a venue's rule. |
| LD-R0609 | LD-C0229 | applies_to | LD-C0026 | Positions aggregated by holder or controller across accounts and firms, as the rule states. |
| LD-R0610 | LD-C0229 | is_distinct_from | LD-C0138 | — |
