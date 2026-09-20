# Governance

Status: Draft

## Proposed responsibilities

| Responsibility | Suggested role |
|---|---|
| Scope and phase approval | Business / Product sponsor |
| Execution meanings | Execution Product owner with Operations |
| ETD Clearing meanings | ETD Clearing Product owner with Operations |
| OTC Clearing meanings | OTC Clearing Product owner with Operations |
| Fees, revenue, costs and recognition | Finance with relevant Product owner |
| Margin, collateral and risk aggregation | Risk / Collateral subject-matter owner |
| Legal effect and regulatory applicability | Legal / Compliance |
| IDs, consistency, traceability and release process | Semantic / Data steward |

These are suggested responsibilities, not assigned people or completed approvals.

## Review status

- **Draft:** proposal, including unresolved issues.
- **Reviewed:** designated reviewers have assessed the proposal; record findings and remaining conditions.
- **Approved:** accountable business owner explicitly accepts the definition and scope; record approver, date and decision evidence.

Technical checks, a Git commit or sponsor approval to create files do not constitute semantic approval. Deprecation is separate from review status and must identify replacements where relevant.

## Changes and releases

Use a focused branch and reviewable change when a base branch exists. Include changed IDs, rationale, affected concepts, compatibility implications and business review needs. Do not silently change a meaning or reuse an identifier. Preserve published versions; breaking semantic changes require an explicit migration note. Establish formal version numbering when the first approved release is made.

## Sensitivity

Concept definitions may be shareable while examples, internal pricing, client names, positions and source mappings are restricted. Use synthetic examples. Establish repository visibility and access policy before introducing confidential material. A sensitivity annotation is metadata, not enforcement of source-system permissions.

## Phase gate

Stop after Phase 1. Request explicit review of architecture, catalogue, relationships and ambiguity register. No domain expansion, detailed taxonomies, resolved query demonstrations or physical mappings until their phase is authorised.
