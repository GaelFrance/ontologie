# Governance and contributing

Status: Draft

## Who decides

Domain owners approve meanings in their domain; the sponsor arbitrates across domains; the Ontology Lead maintains IDs, consistency, traceability and releases. Owners and reviewers per domain are in [review domains](../governance/review-domains.md); the full operating model (bodies, reviewer list, RACI, workflow) is in the [governance model proposal](../governance/governance-model-proposal.md), pending sponsor decision. Decisions are recorded with date and evidence in the [decision log](../governance/decision-log.md); questions only the business can answer are in [open questions](../governance/open-questions-for-owner.md). An ambiguity entry may carry a proposed answer but stays Open until a recorded decision resolves it.

## Review status

- **Draft:** proposal, including unresolved issues. Every concept is Draft today.
- **Reviewed:** designated reviewers have assessed it; findings and remaining conditions recorded.
- **Approved:** the accountable owner explicitly accepts the definition and scope; approver, date and evidence recorded.

A passing check, a Git commit or AI review work never constitutes semantic approval. Deprecation is separate from review status and names the replacement where relevant.

## Making a change

1. Name the concept, relationship or ambiguity ID affected, and the business problem and context.
2. Check for an existing shared concept before adding one.
3. Keep IDs stable: never reuse or renumber one. Do not silently change a meaning; a breaking change needs a migration note.
4. Record sources and unresolved questions; do not invent approval.
5. Edit the registers, then run `python3 tools/build_domain_views.py` (and `--check`) and, if firm questions changed, `python3 tools/build_question_workbooks.py`.
6. Record the change in the [change log](../CHANGELOG.md) and get review from the relevant owner and the Ontology Lead.

Keep register tables parseable: no `|` inside a cell, no temporary `NEW-` IDs, columns appended only after checking the hub reader (see the [modelling guidelines](modelling-guidelines.md#authoring)).

## Content rules

English only. Business meanings only: no firm-specific facts, client names, internal system names, internal pricing, positions or source mappings; examples are synthetic. Answers to the questions for our firm stay in a copy kept inside the firm. A sensitivity annotation is metadata, not enforcement of source-system permissions.
