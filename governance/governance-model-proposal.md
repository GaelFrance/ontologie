# Governance model and reviewer list — proposal

Status: Proposal for sponsor decision (requested 2026-11-01). Roles only; no person is named or assigned here. The sponsor arbitrates until reviewers are named.

## 1. Principles

1. **The business owns meaning.** Each concept has one accountable domain owner; tooling, the Ontology Lead and AI agents never approve a meaning.
2. **Review in plain language.** Reviewers read Markdown pages or an exported document, and comment in words. The Ontology Lead turns comments into changes. Nobody is asked to read YAML, JSON or Git diffs.
3. **Light by default, strict on meaning.** Typos and links need no business review; a new concept, a meaning change or a decided ambiguity always does.
4. **Silence is not approval.** A missed deadline escalates to the sponsor; it never counts as consent.
5. **Public layer only.** The repository holds industry meanings. Firm-specific facts (offered services, legal models, clients, prices, systems) live in an internal layer under the bank's own controls.
6. **AI can propose, never decide.** Reviews produced by AI agents are evidence, labelled as such, and go through the same human review.

## 2. Bodies and roles

| Role | Accountable for | Typical profile | Time needed |
|---|---|---|---|
| **Sponsor / arbiter** | Scope, priorities, phase gates, cross-domain conflicts, final say when owners disagree | Head of Product Development, execution & clearing | 1 h / month + escalations |
| **Ontology board** | Monthly review of open questions, conflicts and the release plan | Sponsor, domain owners, Ontology Lead; others by agenda | 45 min / month |
| **Ontology Lead** | IDs, consistency, change log, releases, checks, turning comments into changes, preparing review packs | Data architect or business analyst with modelling skills | 1–2 days / week in Phase 2 |
| **Domain owner** (one per module or cross-cutting domain) | Approves meanings in their domain | Product owner of the module; for the Revenue domain, the Revenue owner | 2 h / month |
| **Subject reviewer** | Reviews concepts touching their subject; recommends, does not approve | Expert from the functions below | On request, per review pack |
| **Agent owner** (one per pilot agent) | States what the agent must answer; validates evaluation questions and expected answers | Business user of the agent | 2 h / month |

## 3. Reviewer list to name

Ordered by need for the pilot agents. Wave 1 is required before any definition can move from Draft to Reviewed for AG-004 (give-up and clearing acceptance) and AG-002 (change impact).

| # | Reviewer role | Subjects | Concepts (examples) | Wave |
|---|---|---|---|---|
| 1 | Ontology Lead | All: structure, IDs, consistency | All | 1 |
| 2 | ETD Clearing product owner (domain owner) | Give-up/take-up, clearing acceptance, CCP accounts, positions | LD-C0022, LD-C0023, LD-C0053, LD-C0026 | 1 |
| 3 | ETD post-trade operations lead | Give-up workflows, cut-offs, reconciliations, breaks | LD-C0030, LD-C0050, LD-C0065 | 1 |
| 4 | Regulatory Affairs | Regimes, rule changes, consultations, regulatory classifications | LD-C0063, LD-C0064, LD-C0067, LD-C0068 | 1 |
| 5 | Legal | Legal effect of clearing, interposition, client clearing models, agreements | LD-C0024, LD-C0054, LD-C0012 | 1 |
| 6 | Listed Execution product owner (domain owner) | Orders, executions, handling channel, average pricing, venue access | LD-C0016, LD-C0017, LD-C0021, LD-C0061 | 2 |
| 7 | **Revenue domain owner** (domain owner, sponsor decision 2026-11-01) | Management revenue, fees, pricing form, pass-through, charge basis, contribution after costs; answers open questions 9 and 10 | LD-C0031 to LD-C0042, LD-C0074 | 2 |
| 7a | Collateral Manager, as owner of the **collateral revenue** sub-domain | Interest margin on client cash, price alignment, fees on non-cash collateral, and whether they count in clearing revenue | LD-C0042, LD-C0047, LD-C0048 | 2 |
| 7b | Business Finance / Product Control (subject reviewer) | Consistency with management reporting | LD-C0039 to LD-C0042, LD-C0074 | 2 |
| 8 | Margin & Collateral (Collateral Manager, with Risk) | Margin, collateral, default fund, segregation; answers open question 11 | LD-C0043 to LD-C0049, LD-C0011 | 2 |
| 9 | Compliance | Best execution, reporting, client classification, conduct | Regulatory concepts, LD-C0004 | 2 |
| 10 | OTC Clearing product owner (domain owner) | OTC submission, CCP registration, porting, compression | OTC concepts, LD-C0014, LD-C0018 | 3 |
| 11 | Reference & Client Data | Identifiers, instruments, accounts, client hierarchies | LD-C0002, LD-C0010, LD-C0014, LD-C0062 | 3 |
| 12 | Agent owners (AG-004, AG-002, then AG-003, AG-005) | Evaluation questions, expected answers, usefulness | Hub use cases | 1 for AG-004 and AG-002 |
| 13 | Information Security / Data Protection (consulted) | Confidentiality, public/internal boundary, repository access | Governance, sensitivity rules | Once, before the first release |

Business management takes part with Regulatory Affairs, Legal and Compliance in reviewing consultations and readings marked "interpretation required" (decision 9 of the [decision log](decision-log.md)).

## 4. Who does what (RACI)

R = does the work, A = accountable (one per line), C = consulted, I = informed.

| Activity | Sponsor | Board | Ontology Lead | Domain owner | Subject reviewers | Agent owners |
|---|---|---|---|---|---|---|
| Propose a concept or change | I | I | R | C | C | C |
| Technical checks (IDs, links, hub check) | | | A/R | | | |
| Review a meaning | I | | R | C | R | C |
| Approve a meaning in one module | I | I | C | A | C | I |
| Approve a cross-module meaning or conflict | A | R | C | C | C | I |
| Decide an ambiguity | A for scope, else domain owner | C | R | A/R | C | C |
| Validate evaluation questions and expected answers | I | | C | C | C | A/R |
| Release and version | A | I | R | I | I | I |

## 5. Workflow

1. **Propose.** Anyone (including an AI agent) opens a change with affected IDs, rationale and sources. The Ontology Lead checks structure and runs the automatic checks.
2. **Review pack.** For each batch the Ontology Lead produces a readable pack: concept, old and new wording, why, examples, questions. Reviewers can answer in the pack, by e-mail or in a meeting; GitHub is optional.
3. **Reviewed.** Subject reviewers give comments within 10 business days. The Ontology Lead records findings; status becomes Reviewed with remaining conditions.
4. **Approved.** The domain owner approves (or the sponsor, across modules). Record approver role, date and evidence in the decision log.
5. **Release.** Quarterly, or ad hoc for regulatory urgency: tag a version, publish the change log, move the hub's ontology pin, re-run evaluation sets.

| Change type | Business review | Approval |
|---|---|---|
| Typo, link, formatting | None | Ontology Lead |
| New alias, French label, example | Subject reviewer informed | Ontology Lead |
| New concept or relationship | Subject reviewers | Domain owner |
| Meaning change or retype | Subject reviewers + affected agent owners | Domain owner, sponsor if cross-module |
| Ambiguity decision | Subject reviewers | Domain owner, or sponsor for scope |
| Deprecation | Agent owners | Domain owner + Ontology Lead |

## 6. Cadence and escalation

- Monthly board (45 minutes): open questions, conflicts, release content.
- Review deadline: 10 business days; after that the Ontology Lead escalates to the sponsor, who decides or extends.
- Disagreement between two domain owners goes to the board; if unresolved, the sponsor decides and the decision log records it.

## 7. Immediate next steps

1. Sponsor names wave 1 reviewers (rows 1–5 and the agent owners for AG-004 and AG-002).
2. Ontology Lead prepares the first review pack: the AG-004 core (give-up, clearing acceptance, CCP interposition, clearing service, cut-off) and the six meaning changes accepted as Draft on 2026-11-01.
3. First board session to fix the release cadence and confirm this model.
