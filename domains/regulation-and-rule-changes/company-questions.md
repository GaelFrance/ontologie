# Regulation and rule changes: questions for our firm

These questions capture how **our firm** works in this domain, so the ontology can be tailored to it. The answers are firm-specific: record them in the internal workspace, **never in this repository**. Ask them in a meeting with the people named; several questions are shared with other domains and are best answered in a joint session.

## Priority 1: needed for the pilot agents

### 1. Which of the firm's legal entities (described by role, not name) hold which licences, registrations or recognitions (including any futures commission merchant or swap dealer registration), in which jurisdictions, and for which activities?

- **Why it matters:** Obligations attach to legal entities and their authorisations; without this the change-impact agent cannot say whose duty a new rule creates.
- **How to answer:** Table: entity role x regime x authorisation x activity scope x since; 'unknown' allowed.
- **Concepts affected:** Regulatory Authorisation, Regulatory Classification, Regulatory Obligation
- **Who answers:** Regulatory Affairs with Legal
<sub>question q01</sub>

### 2. Please give one table of published changes by kind (contract and calendar, cut-off, margin model or parameters, eligible collateral, fees, clearing-service rules such as account types and default rules, regulation): which publishers you monitor for each, which one is authoritative when they disagree, who assesses it, and which changes trigger a client communication.

- **Why it matters:** Sets the sources of Change Notices and the evidence an agent must cite.
- **How to answer:** List of publisher types with frequency and authoritative flag.
- **Concepts affected:** Change Notice, Rule Change
- **Who answers:** Regulatory Affairs
- **Joint question:** also covers what Clearing: services, accounts and client clearing, Margin and collateral needed to ask.
<sub>question q02</sub>

### 3. When a single circular announces several changes, does the team record one item per circular, one per change, or one per affected obligation or process?

- **Why it matters:** Decides the unit of a Rule Change in the firm's records and how the internal layer maps to the ontology.
- **How to answer:** One of: per notice, per change, per affected object; with an example in words.
- **Concepts affected:** Rule Change, Change Notice, Change Impact Assessment
- **Who answers:** Regulatory Affairs
<sub>question q03</sub>

### 4. Which criticality or triage levels does the team use for a new change, what decides the level, and who decides to act, plan, monitor or ignore?

- **Why it matters:** Gives the values and owners of the decision in a Change Impact Assessment and the priority input of the change-impact agent.
- **How to answer:** Ordered list of levels with criteria and deciding role.
- **Concepts affected:** Change Impact Assessment
- **Who answers:** Regulatory Affairs with business management
<sub>question q04</sub>

### 5. Which dates does the team track for each change (publication, consultation close, entry into force, application, phase-in, internal readiness date), and which date drives planning?

- **Why it matters:** Sets the date roles a Rule Change must carry and the default date an agent states.
- **How to answer:** Checklist of date roles; name the planning date.
- **Concepts affected:** Rule Change, Phase-in Step, Consultation
- **Who answers:** Regulatory Affairs
<sub>question q05</sub>

### 6. How does the team record a CCP or exchange change announced 'subject to regulatory approval' or self-certified, and when is it treated as final?

- **Why it matters:** Decides the status values and the Rule Change Approval step the agent must report.
- **How to answer:** Free text with the status used at each stage.
- **Concepts affected:** Rule Change Approval, Rule Change
- **Who answers:** Regulatory Affairs with ETD Clearing product owner
<sub>question q06</sub>

### 7. Which regulatory obligations should the first change-impact agent cover: clearing, trading on venue, active account, reporting, segregation offer and disclosure, fair commercial terms, position limits, best execution, direct electronic access and algorithm controls, client information duties, others?

- **Why it matters:** Selects the Regulatory Obligation values seeded first.
- **How to answer:** Tick list with priority 1 to 3 each.
- **Concepts affected:** Regulatory Obligation, Clearing Obligation
- **Who answers:** Regulatory Affairs with Compliance
<sub>question q07</sub>

### 8. Which impact dimensions and confidence scale does the team use when assessing a change (legal, operational, technology, client documents, client communication, revenue or cost, capital)?

- **Why it matters:** Sets the impact types and confidence values of a Change Impact Assessment.
- **How to answer:** List of dimensions and the scale used.
- **Concepts affected:** Change Impact Assessment
- **Who answers:** Regulatory Affairs
<sub>question q09</sub>

### 9. Which venue rule areas matter most to the listed execution desk when they change (block thresholds and reporting delays, exchange-for-related-position rules, error trade policy, direct electronic access and algorithm controls, order-to-trade limits, position limits and accountability)?

- **Why it matters:** Targets the venue Rulebook provisions and affected execution concepts the agent must watch.
- **How to answer:** Ranked list.
- **Concepts affected:** Rulebook, Rule Change, Rule Provision
- **Who answers:** Listed Execution product owner
<sub>question q10</sub>

### 10. Which cross-border decisions does the business rely on (equivalence, recognition of third-country CCPs, substituted compliance, exemptions from registration), and who watches their expiry?

- **Why it matters:** Identifies Equivalence Decisions and Regulatory Authorisations whose change or expiry is high impact.
- **How to answer:** List of decision types with dependent activity and monitoring role.
- **Concepts affected:** Equivalence Decision, Regulatory Authorisation
- **Who answers:** Regulatory Affairs with Legal
<sub>question q12</sub>

## Priority 2: needed before go-live

### 11. Which Asia-Pacific jurisdictions should be prepared after the EU, UK and US, in which order, and for each: which venues and calendars, which CCPs and account structures or legal models, whether give-ups follow a different practice, and which regulatory frameworks apply? (Answered by the product development lead with Regulatory Affairs.)

- **Why it matters:** Seeds priority-2 Regulatory Regime instances (sponsor decision 8 left them to be scoped).
- **How to answer:** Ordered list of jurisdictions with the activity (execution, clearing) concerned.
- **Concepts affected:** Regulatory Regime
- **Who answers:** Regulatory Affairs with business management
- **Joint question:** also covers what Clearing: give-up and acceptance, Clearing: services, accounts and client clearing, Instruments, venues and calendars needed to ask.
<sub>question q11</sub>

### 12. Does the business rely on any regulatory relief (no-action relief, exemptions, transitional measures, forbearance), and is each tracked with its conditions and expiry?

- **Why it matters:** Relief changes who must comply and when; its expiry is itself a change to watch.
- **How to answer:** Yes or no per relief type; tracking practice in words.
- **Concepts affected:** Regulatory Relief
- **Who answers:** Compliance with Legal
<sub>question q13</sub>

### 13. Who signs off a reading marked 'interpretation required' in practice, beyond Regulatory Affairs and business management with Legal and Compliance as already decided; what turnaround is expected, what is recorded, and when is external counsel used?

- **Why it matters:** Sets the status, author kinds and sign-off record of a Regulatory Interpretation.
- **How to answer:** Process description in a few lines.
- **Concepts affected:** Regulatory Interpretation, Change Impact Assessment
- **Who answers:** Regulatory Affairs with Legal and Compliance
<sub>question q14</sub>

### 14. Does the firm respond to consultations directly, through industry associations, or both, and is the decision to respond tracked against the consultation?

- **Why it matters:** Decides whether a Consultation needs a response status and owner.
- **How to answer:** One of: direct, associations, both, none; tracking yes or no.
- **Concepts affected:** Consultation
- **Who answers:** Regulatory Affairs
<sub>question q15</sub>

### 15. To which internal objects must every assessed change be traceable: service offerings, client agreements and templates, procedures, controls, systems (by role), client communications?

- **Why it matters:** Defines the internal-layer targets of the 'affects' link beyond the public concepts.
- **How to answer:** Tick list.
- **Concepts affected:** Change Impact Assessment, Rule Change
- **Who answers:** Regulatory Affairs with business management
<sub>question q16</sub>

### 16. Which of the firm's own procedures and policies should be recorded as rule provisions in the internal layer (cut-off policies, client limits, onboarding criteria, give-up acceptance rules), and who owns them?

- **Why it matters:** Rule Provision includes firm procedures; their kinds and owners must be known before the internal layer is built.
- **How to answer:** List of procedure kinds with owner roles.
- **Concepts affected:** Rule Provision, Rulebook
- **Who answers:** Compliance with product owners
<sub>question q17</sub>

### 17. For audits, supervisory requests and client disputes, which objects need 'as known at' history (rule changes, classifications, reference data and contract versions, statuses and reports, cut-offs), and how far back? (Answered by Compliance.)

- **Why it matters:** Decides whether record time must be kept and queried (open firm decision in the time convention).
- **How to answer:** Yes or no; retention period.
- **Concepts affected:** Regulatory Classification, Rule Change
- **Who answers:** Compliance
- **Joint question:** also covers what Instruments, venues and calendars, Post-trade operations needed to ask.
<sub>question q18</sub>

### 18. For OTC clearing, which clearing obligation classes, counterparty categories and transitional points matter most to the business, and are any clients relying on intragroup or other exemptions?

- **Why it matters:** Prioritises Clearing Obligation and Regulated Product Class content and the exemptions the agent must ask about.
- **How to answer:** Ranked list of classes and categories; yes or no on exemptions (no client names).
- **Concepts affected:** Clearing Obligation, Regulated Product Class, Phase-in Step
- **Who answers:** OTC Clearing product owner with Compliance
<sub>question q19</sub>

### 19. Which client-facing duties tied to regulation does the firm perform as clearing or execution provider (informing clients of new obligations, segregation and cost disclosures, publishing fair commercial terms), and who owns each?

- **Why it matters:** Identifies provider-side Regulatory Obligations that a rule change can trigger on the firm itself.
- **How to answer:** List of duties with owner role.
- **Concepts affected:** Regulatory Obligation
- **Who answers:** Compliance with Legal
<sub>question q20</sub>

### 20. Do any of the firm's entities operate through branches in the EU, UK or US, and which regimes attach duties or authorisations to those branches? (Ask in the same session as the access-route table.)

- **Why it matters:** Decides whether Regulatory Authorisation and Classification attach to branches as well as legal entities.
- **How to answer:** Yes or no; regime list (no entity names).
- **Concepts affected:** Regulatory Authorisation, Regulatory Classification
- **Who answers:** Legal
<sub>question q21</sub>

### 21. For each region where clients are located, on what regulatory basis do you serve them (local licence, branch, cross-border exemption or relief, client-initiated business), and who tracks its conditions?

<sub>question q25</sub>

## Priority 3: later

### 22. Should prudential consequences of a change (qualifying CCP status, default fund and CCP exposure treatment, leverage) be part of change impact, and who owns that view?

- **Why it matters:** Decides whether capital impact is an impact type and whether qualifying status must be tracked here.
- **How to answer:** Yes or no; owner role.
- **Concepts affected:** Change Impact Assessment, Regulatory Authorisation
- **Who answers:** Business management with Finance
<sub>question q22</sub>

### 23. Under which reporting regimes does the firm report listed and OTC derivatives activity, and does it offer delegated reporting to clients?

- **Why it matters:** Decides when Regulatory Report should leave the backlog and which reporting obligations to seed.
- **How to answer:** Tick list of regimes; yes or no on delegated reporting.
- **Concepts affected:** Regulatory Obligation
- **Who answers:** Compliance (regulatory reporting)
<sub>question q23</sub>

### 24. Must the team handle official publications in languages other than English, and which version is authoritative for the firm?

- **Why it matters:** Affects Change Notice language and the evidence an agent cites.
- **How to answer:** List of languages; authoritative-language rule.
- **Concepts affected:** Change Notice, Rule Provision
- **Who answers:** Regulatory Affairs
<sub>question q24</sub>
