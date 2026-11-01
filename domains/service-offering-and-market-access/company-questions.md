# Service offering and market access: questions for our firm

These questions capture how **our firm** works in this domain, so the ontology can be tailored to it. The answers are firm-specific: record them in the internal workspace, **never in this repository**. Ask them in a meeting with the people named; several questions are shared with other domains and are best answered in a joint session.

## Priority 1: needed for the pilot agents

### 1. How do you name and divide your service offerings today: one per service kind, or also split by region, asset class, venue or clearing house, or client segment?

- **Why it matters:** Sets what counts as one Service Offering, which is the key for revenue per service and for onboarding answers.
- **How to answer:** Short description of the dimensions used, with one synthetic example of each offering level.
- **Concepts affected:** Service Offering, Service Kind, Offering Coverage Line
- **Who answers:** Product development lead
<sub>question q01</sub>

### 2. Please fill one access-route table: one row per venue or venue segment and per clearing service you use, with columns: execution or clearing; access model (own membership, third-party member, non-clearing member, client, sponsored, none); membership category in the rulebook's own words; intermediary, if any; holding legal entity or branch (by role); status; for listed clearing, whether you act as giving member, receiving member or both; and where this record is kept and who maintains it.

- **Why it matters:** Gives the first internal instances of Market Access Arrangement, needed before any onboarding or coverage answer.
- **How to answer:** Table: venue or clearing service, access model, membership category or intermediary type, status. Internal only.
- **Concepts affected:** Market Access Arrangement, Access Status, Non-Clearing Member Arrangement, Third-Party Execution Arrangement
- **Who answers:** ETD Clearing product owner and Listed Execution product owner
- **Joint question:** also covers what Clearing: give-up and acceptance, Clearing: services, accounts and client clearing, Instruments, venues and calendars, Listed derivatives execution, Parties, roles, clients and accounts needed to ask.
<sub>question q07</sub>

### 3. When you execute on a venue where you are not a member, how do you choose the third-party executing member, and does the client know who it is? (How its brokerage is recorded is asked in the fees questions.)

- **Why it matters:** Defines the Third-Party Execution Arrangement's intermediary rules and how its cost reaches revenue and contribution.
- **How to answer:** Short answers: selection rule; disclosed to client yes or no; recharged, absorbed or depends.
- **Concepts affected:** Third-Party Execution Arrangement, Market Access Arrangement
- **Who answers:** Listed Execution product owner
<sub>question q09</sub>

### 4. At which CCPs, today or as a plan, do you: (a) clear for clients that clear for their own clients (indirect clearing), and do you know those underlying clients by name or only as an omnibus; (b) act as sponsor or clearing agent under a sponsored or direct-client model, or have entities that are sponsored participants themselves; (c) clear for venue members that are not clearing members, and are they kept as ordinary clients in your client data; (d) clear through another clearing member?

- **Why it matters:** Determines whether Indirect Clearing Arrangement and Non-Clearing Member Arrangement have firm instances, and answers 'how can we offer clearing where we are not a member'.
- **How to answer:** Per CCP: yes or no; if yes, route (non-clearing member, client, other) and whether clients are cleared indirectly.
- **Concepts affected:** Indirect Clearing Arrangement, Non-Clearing Member Arrangement, Offering Coverage Line
- **Who answers:** ETD Clearing product owner
- **Joint question:** also covers what Clearing: services, accounts and client clearing, Parties, roles, clients and accounts needed to ask.
<sub>question q10</sub>

### 5. When the firm decides to offer execution or clearing on a new venue or CCP, what are the internal stages and approvals (business case, risk, legal, operations readiness, testing, go-live), and who approves each?

- **Why it matters:** Gives the firm-specific steps of Access Onboarding beyond what the venue or CCP requires, used by the onboarding assistant.
- **How to answer:** Ordered list of stages with the approving role for each.
- **Concepts affected:** Access Onboarding, Access Status
- **Who answers:** Product development lead
<sub>question q12</sub>

### 6. What conditions must a client meet before you offer it a given service (for example client type, regulatory classification, jurisdiction, credit approval, documents signed, testing for electronic access)?

- **Why it matters:** Provides the Offering Eligibility Criterion values that decide 'can we onboard Client A for contract Y at CCP Z'.
- **How to answer:** List of conditions per service kind, each marked mandatory or case by case, with the approving role.
- **Concepts affected:** Offering Eligibility Criterion, Service Offering
- **Who answers:** Product development lead with Credit Risk and Compliance
<sub>question q13</sub>

### 7. When people in the firm say 'we cover market X', what do they mean: a membership exists, an access route is live, an offering is active there, or at least one client is live?

- **Why it matters:** Fixes the firm's reading of 'covered' so agents never answer it from a membership list.
- **How to answer:** Pick one or describe; give the condition that must hold.
- **Concepts affected:** Offering Coverage Line, Access Status, Market Access Arrangement
- **Who answers:** Product development lead
<sub>question q14</sub>

### 8. For each access route, which documents does Legal consider necessary, and are any master documents shared across several venues or CCPs? (Give-up agreements are asked in the give-up questions.)

- **Why it matters:** Answers Legal's question on whether an access arrangement is one agreement or a set, and fills Access Agreement values.
- **How to answer:** Per access model: list of document types; note shared master documents.
- **Concepts affected:** Access Agreement, Market Access Arrangement, Client Clearing Agreement, Give-up Agreement
- **Who answers:** Legal
<sub>question q16</sub>

## Priority 2: needed before go-live

### 9. Which related post-trade services do you sell on their own, and which only inside execution or clearing services (for example average pricing, handling of trades given in, delegated reporting, exercise and delivery handling)?

- **Why it matters:** Decides whether a 'related post-trade service' is a Service Kind value or a Service Component, and whether it has its own revenue line.
- **How to answer:** List of services, each marked: sold alone, bundled, or both; priced separately or not.
- **Concepts affected:** Service Kind, Service Component
- **Who answers:** Product development lead
<sub>question q03</sub>

### 10. Which connectivity models do you use to reach venues and CCPs (direct, through a vendor or service bureau, through another member), and do clients with electronic access use their own connection or yours?

- **Why it matters:** Sets the Connectivity Route values in use and links connectivity costs to access routes.
- **How to answer:** Per venue or CCP group: connectivity model; for client electronic access: own, firm's, both.
- **Concepts affected:** Connectivity Route, Direct Electronic Access Arrangement
- **Who answers:** Listed Execution product owner with technology lead
<sub>question q15</sub>

### 11. Are any service kinds unavailable, or offered under materially different terms, in one of your regions (EU, UK, US, Asia-Pacific)?

- **Why it matters:** Shows whether offerings are regional variants and which regimes each coverage line falls under.
- **How to answer:** Matrix: service kind by region, marked offered, not offered, or offered from another region's entity.
- **Concepts affected:** Service Offering, Offering Coverage Line
- **Who answers:** Product development lead with Regulatory Affairs
<sub>question q19</sub>

### 12. How do you state the product scope of an offering: by asset class, by product family, by list of contracts, or by 'all contracts eligible at the CCP'?

- **Why it matters:** Decides the level at which coverage lines name their scope and prevents scope from being inferred from CCP eligibility.
- **How to answer:** One of the listed options, or a combination, with a synthetic example.
- **Concepts affected:** Offering Coverage Line, Service Offering
- **Who answers:** Product development lead
<sub>question q22</sub>

### 13. Which access requirements are hardest or slowest to meet when you add a venue or CCP (for example capital, default fund, local registration, testing, staff qualification)?

- **Why it matters:** Prioritises which Access Requirement categories the onboarding assistant must describe in detail first.
- **How to answer:** Ranked list of up to five requirement categories, with typical lead time in weeks.
- **Concepts affected:** Access Requirement, Access Onboarding
- **Who answers:** Product development lead
<sub>question q23</sub>

### 14. For OTC derivatives, do you clear trades your clients execute with other dealers or on OTC trading venues (MTFs, OTFs, swap execution facilities), and do you provide or arrange access to those venues?

<sub>question q24</sub>

### 15. Do any clients ask you to provide clearing at an EU CCP to meet an active account requirement, and does this shape your offering?

<sub>question q25</sub>

## Priority 3: later

### 16. When a venue or CCP access route is suspended, restricted or terminated, what happens to the offering and to clients relying on it (notice periods, move to another route, client transfer)?

- **Why it matters:** Defines the transitions of Access Status and their effect on coverage lines, needed for change-impact answers.
- **How to answer:** Short description per case: suspension, restriction, termination.
- **Concepts affected:** Access Status, Offering Coverage Line, Market Access Arrangement
- **Who answers:** Product development lead with ETD post-trade operations lead
<sub>question q20</sub>

### 17. Do any of your clients with electronic access pass that access on to their own clients, and do you allow it?

- **Why it matters:** Determines whether a chained direct electronic access arrangement must be modelled.
- **How to answer:** Allowed, not allowed, or case by case with the approving role.
- **Concepts affected:** Direct Electronic Access Arrangement
- **Who answers:** Listed Execution product owner with Compliance
<sub>question q21</sub>
