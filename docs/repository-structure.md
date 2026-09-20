# Repository structure

This is the exact Phase 1 Markdown-first structure. Empty future schemas, metric implementations and YAML taxonomy files are deliberately deferred.

```text
.github/pull_request_template.md
CHANGELOG.md
CONTRIBUTING.md
README.md
docs/architecture.md
docs/governance.md
docs/modelling-guidelines.md
docs/principles.md
docs/repository-structure.md
docs/scope.md
examples/natural-language-queries.md
governance/ambiguity-register.md
governance/phase-1-review.md
governance/sources.md
mappings/README.md
mappings/templates/mapping-template.md
ontology/common/README.md
ontology/etd-clearing/README.md
ontology/execution/README.md
ontology/foundation.md
ontology/otc-clearing/README.md
relationships/relationships.md
semantic-layer/README.md
taxonomies/README.md
templates/concept-template.md
```

After Phase 1 approval, detailed concept files will use `<module>/LD-Cnnnn.md`. If a later YAML migration is approved, retain IDs, add schemas and validation, and generate readable documentation from the canonical data. Mappings remain methodology and templates until actual schemas are provided.
