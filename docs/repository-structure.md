# Repository structure

This is the exact Markdown-first structure, updated after the 2026-11 expert review. Empty future schemas and metric implementations are deliberately deferred; machine-readable exports are generated from the Markdown, not stored as canonical files.

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
governance/decision-log.md
governance/open-questions-for-owner.md
governance/phase-1-review.md
governance/reviews/2026-11-expert-review/01-execution.md … 08-ontology-engineering.md
governance/reviews/2026-11-expert-review/ARBITRATION.md
governance/sources.md
mappings/README.md
mappings/templates/mapping-template.md
ontology/common/README.md
ontology/concept-annotations.md
ontology/etd-clearing/README.md
ontology/execution/README.md
ontology/foundation.md
ontology/otc-clearing/README.md
relationships/relationships.md
semantic-layer/README.md
taxonomies/README.md
templates/concept-template.md
```

Detailed concept files will use `<module>/LD-Cnnnn.md`; when they exist, the content of `ontology/concept-annotations.md` moves into them. `ontology/foundation.md` stays the single index of IDs because the agent hub reads it. If a later YAML migration is approved, retain IDs, add schemas and validation, and generate readable documentation from the canonical data. Mappings remain methodology and templates until actual schemas are provided.
