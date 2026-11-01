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

## Decisions and open questions

Record business-owner decisions in the [decision log](../governance/decision-log.md) with date and evidence; keep questions that only the owner can answer in [open questions](../governance/open-questions-for-owner.md). An ambiguity entry may carry a proposed answer, but stays Open until a recorded decision resolves it.

## Proposed operating model

A governance model with bodies, a reviewer list, a RACI and the review workflow is proposed in [governance model proposal](../governance/governance-model-proposal.md), pending sponsor decision.

## Phase gate

The sponsor approved the Phase 1 foundation on 2026-09-20; see the [decision record](../governance/phase-1-review.md). Phase 2 may develop the concepts in the agreed order. This does not approve individual definitions, metric formulas, detailed taxonomies, resolved query demonstrations or physical mappings. Preserve subsequent phase gates.
