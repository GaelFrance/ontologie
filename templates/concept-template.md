# Concept template

Template only. Full concept completion is Phase 2 work. Field names and the key names in backticks are fixed so that a later YAML migration can map them one to one.

Replace guidance with content. Use `To validate — question` or `Not applicable — reason` explicitly.

| Field | Guidance |
|---|---|
| Unique ID | Immutable LD-C identifier. |
| Canonical English name | One preferred name. |
| Business definition | Meaning independent of a system. |
| Owning domain / applicable domains | Stewardship versus reuse. |
| Subdomain | Business capability or family. |
| Concept type | Choose an explicit proposed type. |
| French label (`label_fr`) | Secondary label; English remains canonical. |
| Synonyms / alternative terminology (`aliases`) | Mark exact, contextual or ambiguous; include scope and language. |
| Common abbreviations | Expansion and scope. |
| Related concepts | Concept IDs and nature of relatedness. |
| Parent concepts (`parents`) | IDs and justified is_a relationship. |
| Identity criteria and identifier schemes (`identity`) | What makes two records the same object; applicable identifier schemes and their uniqueness scope. |
| Temporal pattern (`temporal_pattern`) | Point event, interval-valid, snapshot or timeless; whether valid and record time are both needed. |
| Required context (`required_context`) | Qualifiers an agent must obtain before answering. |
| Resolution (`resolution`) | Normal, or blocked-pending-decision with the candidate concepts. |
| Child concepts | Derived view of approved parent references. |
| Relationships | Relationship IDs and relevant qualifiers. |
| Business rules | Scope, condition, effect and evidence. |
| Calculation / derivation | Formula or Not applicable; no invented formula. |
| Unit / currency | Quantity kind and currency role. |
| Direction / sign convention | Economic direction and observing party. |
| Business perspective / context | Required qualifiers and applicability. |
| Examples | Synthetic, domain-relevant examples. |
| Counterexamples / exclusions | What the concept does not mean. |
| Ambiguities | Open distinctions and register IDs. |
| Sensitivity / governance | Definition sensitivity and underlying-data considerations. |
| Suggested owner / steward | Roles until people are assigned. |
| Status | Draft / Reviewed / Approved. |
| Standard alignments (`alignments`) | Standard, module and concept with match kind (exact, close, broad, narrow, related); `verified: false` until checked; no IRI from memory. |
| Competency questions served | Evaluation or competency question IDs. |
| Sources and decisions | Evidence with version/section and decision references. |
| Version / effective period | Definition version and applicability dates. |
| Validation questions | Unresolved questions, reviewer and outcome. |
