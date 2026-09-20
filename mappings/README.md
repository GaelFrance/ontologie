# Physical mappings — deferred

No physical mapping exists in this foundation. Mapping starts only when the user supplies actual source schemas and authorises Phase 5.

## Method

1. Identify source system ownership, schema version and permitted access.
2. Identify target concept IDs and their approved context.
3. Establish grain, identifiers, keys, cardinality and temporal semantics.
4. Document actual fields, transformations, code translations, units and sign conversion.
5. Test completeness, duplicates, reconciliation, reversals and lineage with authorised data.
6. Record coverage gaps, owner review and effective dates.

A shared field name is not evidence of shared business meaning. An API or MCP adapter exposes a mapping; it does not define the concept.

Use the [mapping template](templates/mapping-template.md) only after real schemas are supplied. No application, table, column, API or MCP resource is assumed.
