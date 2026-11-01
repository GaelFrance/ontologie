# Parties, roles, clients and accounts: questions for our firm

These questions capture how **our firm** works in this domain, so the ontology can be tailored to it. The answers are firm-specific: record them in the internal workspace, **never in this repository**. Ask them in a meeting with the people named; several questions are shared with other domains and are best answered in a joint session.

## Priority 1: needed for the pilot agents

### 1. For each service kind (execution-only, clearing-only, execute-and-clear) and region, which of your legal entities (by role, not name) contracts with the client, executes, acts as clearing member (including the giving clearing member when you execute but do not clear), and books the revenue? Can one client contract with more than one entity for the same service, and can one offering be delivered by several entities?

- **Why it matters:** Fixes the Contracting Entity values and the observing entity for revenue; decides whether one client can have parallel relationships.
- **How to answer:** Table: service, region or CCP, contracting legal entity; yes or no with examples for parallel relationships.
- **Concepts affected:** Contracting Entity, Client, Legal Entity
- **Who answers:** Legal with Reference & Client Data
- **Joint question:** also covers what Clearing: give-up and acceptance, Clearing: services, accounts and client clearing, Listed derivatives execution, Service offering and market access needed to ask.
<sub>question q01</sub>

### 2. What is the lowest level at which you record a client: legal entity, sub-fund, branch, natural person, or something else? Is it the same level for execution and for clearing?

- **Why it matters:** Defines what 'Client' means in the firm's data and how many client records one legal entity can produce.
- **How to answer:** Chosen level per service, with any exceptions.
- **Concepts affected:** Client, Party, Investment Fund, Natural Person
- **Who answers:** Reference & Client Data
<sub>question q03</sub>

### 3. How many client groupings do you maintain (for example sales coverage, credit, revenue reporting)? Who maintains each one, can a client belong to more than one, and is any of them based on legal ownership?

- **Why it matters:** Decides whether Commercial Group is one hierarchy or several named ones, and keeps it apart from the ownership group.
- **How to answer:** List of groupings with purpose, owner, update frequency, ownership-based yes or no.
- **Concepts affected:** Commercial Group, Parent Entity
- **Who answers:** Reference & Client Data with business management
<sub>question q04</sub>

### 4. When an investment manager trades for many funds, who is your contractual client for listed derivatives and for OTC clearing: each fund, the manager, or both? Who signs the agreements?

- **Why it matters:** Sets the client and the revenue attribution target for the largest client segment.
- **How to answer:** Fund, manager or both, per service; signatory.
- **Concepts affected:** Client, Investment Fund, Investment Manager, Commercial Group
- **Who answers:** Legal with ETD and OTC Clearing product owners
<sub>question q05</sub>

### 5. Which identifiers do you hold for parties and accounts (LEI, internal party code, CCP account numbers, give-up references per venue, executing broker codes)? Which one is the master key for a party and for an account?

- **Why it matters:** Decides which Account Identifier and party identifier values must be supported and how agents match records.
- **How to answer:** List of identifier kinds with issuer, scope and whether master.
- **Concepts affected:** Account Identifier, Legal Entity Identifier, Party
- **Who answers:** Reference & Client Data
<sub>question q08</sub>

### 6. Which client relationship statuses do you use, per contracting entity and per service, and which status blocks new trading, new accounts or clearing? When is a client considered onboarded for a given service at a given CCP?

- **Why it matters:** Sets the values and attachment level of Client Relationship Status, needed to answer onboarding questions.
- **How to answer:** List of statuses with effect and level.
- **Concepts affected:** Client Relationship Status, Client
- **Who answers:** Reference & Client Data with Compliance
<sub>question q09</sub>

### 7. Which of your affiliates are clients of your execution or clearing entities? At each reference CCP, are they cleared in house or client accounts, and how are they flagged for revenue elimination?

- **Why it matters:** Defines Intra-group Client in practice and its effect on account type and revenue views.
- **How to answer:** Per CCP: house or client; flagging method; elimination owner.
- **Concepts affected:** Intra-group Client, Parent Entity, Client Account
- **Who answers:** ETD Clearing product owner with Business Finance
- **Joint question:** also covers what Clearing: services, accounts and client clearing needed to ask.
<sub>question q10</sub>

## Priority 2: needed before go-live

### 8. Is MiFID client categorisation done per legal entity of the client, per contracting entity, or per service? Do you allow clients to opt up or down, and does the UK use the same process?

- **Why it matters:** Sets the attachment level and basis values of Client Regulatory Category.
- **How to answer:** Level of categorisation, opt-up and opt-down yes or no, UK same or different.
- **Concepts affected:** Client Regulatory Category, Contracting Entity
- **Who answers:** Compliance
<sub>question q12</sub>

### 9. Which entity-level statuses do you record for clients (EU and UK counterparty category and clearing-threshold status per asset class, US eligible contract participant, US person), from which source (self-declaration, data vendor, own assessment), how often are they refreshed, and which of them decide whether a client is in scope of an obligation?

- **Why it matters:** Sets the values, basis and freshness of Counterparty Regulatory Status.
- **How to answer:** List of statuses with source and refresh frequency.
- **Concepts affected:** Counterparty Regulatory Status, Legal Entity
- **Who answers:** Compliance with Regulatory Affairs
- **Joint question:** also covers what Regulation and rule changes needed to ask.
<sub>question q13</sub>

### 10. In which capacities do your entities execute for clients (agency, riskless principal, principal), per product, region and handling channel? Is capacity fixed in the client agreement or decided per order?

- **Why it matters:** Sets the firm values of Trading Capacity and where it is recorded.
- **How to answer:** Table: entity, product, capacities used; per agreement or per order.
- **Concepts affected:** Trading Capacity, Broker
- **Who answers:** Listed Execution product owner with Compliance
- **Joint question:** also covers what Listed derivatives execution needed to ask.
<sub>question q17</sub>

### 11. Who can instruct you for a client, including orders and allocation instructions (authorised traders, investment managers, introducing brokers or introducers, the broker on the client's behalf), and how are those authorities recorded and checked?

- **Why it matters:** Sets the values and required context of Authorised Representative and Investment Manager.
- **How to answer:** List of representative kinds; where authority is recorded; checks applied.
- **Concepts affected:** Authorised Representative, Investment Manager, Natural Person
- **Who answers:** Reference & Client Data with Listed Execution product owner
- **Joint question:** also covers what Listed derivatives execution needed to ask.
<sub>question q18</sub>

### 12. What is your rule when a client's LEI lapses or is missing: no new trades, trades allowed with escalation, or no impact? Do you record LEIs for branches and for each sub-fund?

- **Why it matters:** Sets the business rules carried by Legal Entity Identifier status and the expected coverage of LEIs.
- **How to answer:** Rule per service; yes or no for branches and sub-funds.
- **Concepts affected:** Legal Entity Identifier, Branch, Investment Fund
- **Who answers:** Reference & Client Data with Compliance
<sub>question q20</sub>

### 13. Which client segmentation do you use for sales and revenue reporting, who assigns a client to a segment, and can a client change segment over time?

- **Why it matters:** Provides the firm values for the client segment axis used by Service Offering and revenue views.
- **How to answer:** List of segments; assigning role; change rule.
- **Concepts affected:** Client, Commercial Group
- **Who answers:** Business management with Reference & Client Data
- **Joint question:** also covers what Service offering and market access needed to ask.
<sub>question q21</sub>

### 14. Are your internal desks or business lines ever recorded as counterparties or clients of each other (for example for internal recharges)?

- **Why it matters:** Tests the proposed exclusion of internal teams from Party and the meaning of 'internal client'.
- **How to answer:** Yes or no; examples of use.
- **Concepts affected:** Party, Intra-group Client, Client
- **Who answers:** Business Finance
<sub>question q22</sub>

### 15. For clients whose trades you give up to other clearing brokers, do you record each client's clearing brokers and the give-up references of its accounts there; who maintains them and how are changes dated?

<sub>question q24</sub>

## Priority 3: later

### 16. Do you accept business through introducing brokers or other introducers? Are they recorded as parties, and does their remuneration depend on the clients they introduce?

- **Why it matters:** Decides whether an Introducing Broker role must be promoted from a value to its own concept, and its link to fees.
- **How to answer:** Yes or no; recorded as party yes or no; remuneration basis in words.
- **Concepts affected:** Authorised Representative, Broker, Client
- **Who answers:** Listed Execution and ETD Clearing product owners
<sub>question q19</sub>

### 17. Do you have individual (natural person) clients for listed or cleared derivatives, directly or through another entity of your group?

- **Why it matters:** Decides whether Natural Person as a client needs its own rules (retail protection, personal data) in the pilot.
- **How to answer:** Yes or no; channel; regions.
- **Concepts affected:** Natural Person, Client Regulatory Category
- **Who answers:** Compliance
<sub>question q23</sub>
