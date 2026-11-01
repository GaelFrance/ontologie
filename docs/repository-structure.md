# Repository structure

This is the exact Markdown-first structure, updated after the 2026-11 level-2 domain review. Empty future schemas and metric implementations are deliberately deferred; machine-readable exports are generated from the Markdown, not stored as canonical files.

```text
.claude/skills/<domain>-expert/SKILL.md     one expert skill per domain (10)
.github/pull_request_template.md
CHANGELOG.md
CONTRIBUTING.md
README.md
domains/README.md                           generated index of domains
domains/<domain>/README.md                  generated domain page
domains/<domain>/overview.md                hand-written introduction
domains/<domain>/concepts.md                generated concept cards
domains/<domain>/review.md                  generated review sheet
domains/<domain>/company-questions.md       hand-written questions for the firm
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
governance/reviews/2026-11-classification-review/01-ontology-lead.md … ARBITRATION.md
governance/reviews/2026-11-level2-domain-review/SUPERVISION.md
governance/review-domains.md
glossary.md                                 generated A-to-Z of all concepts
governance/sources.md
mappings/README.md
mappings/templates/mapping-template.md
ontology/README.md
ontology/concept-annotations.md
ontology/foundation.md
relationships/relationships.md
semantic-layer/README.md
taxonomies/README.md
templates/concept-template.md
tools/build_domain_views.py                 builds domains/ and glossary.md from the registers
```

Concept cards are generated per domain (`domains/<domain>/concepts.md`) from the registers; there are no hand-written per-concept files, so a meaning is written once. `ontology/foundation.md` stays the single index of IDs because the agent hub reads it. If a later YAML migration is approved, retain IDs, add schemas and validation, and generate readable documentation from the canonical data. Mappings remain methodology and templates until actual schemas are provided.
