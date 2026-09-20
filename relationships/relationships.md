# Major relationships

Status: Draft. All concept IDs refer to the [foundation catalogue](../ontology/foundation.md).

These are logical relation proposals, not database foreign keys. Source/target alternatives are not equivalence assertions. Cardinalities remain unapproved unless stated as qualified examples. Inverse labels, full constraints and contextual relation objects will be defined in Phase 2.

| ID | Source concept | Relation | Target concept | Meaning and conditions |
|---|---|---|---|---|
| LD-R0001 | LD-C0001 | has_role | LD-C0003 | Use a contextual, time-bounded role assignment; not an unqualified permanent property. |
| LD-R0002 | LD-C0003 | governed_by | LD-C0012 | Applicable to the role assignment where a governing agreement exists. |
| LD-R0003 | LD-C0004 | submits | LD-C0016 | Distinguish contractual client, representative and technical sender. |
| LD-R0004 | LD-C0016 | fulfilled_by | LD-C0017 | An order can have zero or multiple fills; cancellations and partial execution matter. |
| LD-R0005 | LD-C0017 | contributes_to | LD-C0018 | Do not assume a universal one-to-one fill/trade representation. |
| LD-R0006 | LD-C0017 | occurs_on | LD-C0009 | When applicable; distinguish execution from reporting or registration on a venue. |
| LD-R0007 | LD-C0020 | allocates | LD-C0017 / LD-C0018 | State allocated quantity, source object and process scope. |
| LD-R0008 | LD-C0020 | targets | LD-C0010 | Target account does not by itself establish legal ownership. |
| LD-R0009 | LD-C0021 | groups | LD-C0017 / LD-C0018 | Eligibility, weighting, rounding and resulting records depend on context. |
| LD-R0010 | LD-C0022 | concerns | LD-C0018 | Carry quantity, counterparties and lifecycle history. |
| LD-R0011 | LD-C0022 | receiving_member | LD-C0007 | An intended recipient is not proof of acceptance. |
| LD-R0012 | LD-C0023 | concerns | LD-C0018 | Specify service, acceptance criteria and time. |
| LD-R0013 | LD-C0023 | accepted_by | LD-C0008 | Identify CCP service and receiving member; do not infer a universal legal effect. |
| LD-R0014 | LD-C0024 | transforms | LD-C0018 | Preserve predecessor and successor obligations/trades with directional lineage. |
| LD-R0015 | LD-C0026 | recorded_in | LD-C0010 | Recording does not assert beneficial ownership. |
| LD-R0016 | LD-C0026 | included_in | LD-C0027 | Membership is purpose-specific and time-bound. |
| LD-R0017 | LD-C0043 | assessed_for | LD-C0027 / LD-C0010 | Include risk scope, relationship, model and as-of time; not individual-position causality. |
| LD-R0018 | LD-C0046 | requests_satisfaction_of | LD-C0043 | Requirement, demand and remaining shortfall are different objects. |
| LD-R0019 | LD-C0049 | moves | LD-C0047 | Identify pledgor/recipient, arrangement and committed quantity. |
| LD-R0020 | LD-C0029 | settles | LD-C0028 | May be partial; net payment may cover several obligations. |
| LD-R0021 | LD-C0031 | has_debtor | LD-C0001 | Debtor may differ from actual payer. |
| LD-R0022 | LD-C0031 | has_creditor | LD-C0001 | Creditor may differ from collector or ultimate beneficiary. |
| LD-R0023 | LD-C0031 | calculated_under | LD-C0032 | Use the applicable tariff version and conditions; calculation is not recognition. |
| LD-R0024 | LD-C0050 | identifies | LD-C0030 | A reconciliation break does not prove underlying trade failure. |

A future collateral-to-obligation relation must distinguish secured obligations, arrangements and valuation. The generic Obligation type is present in the model, but a standalone general Obligation concept is not yet defined in the catalogue. Do not invent an unresolved target concept ID.
