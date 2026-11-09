# Clearing: services, accounts and client clearing: questions for our firm

These questions capture how **our firm** works in this domain, so the ontology can be tailored to it. The answers are firm-specific: record them in the internal workspace, **never in this repository**. Ask them in a meeting with the people named; several questions are shared with other domains and are best answered in a joint session.

## Priority 1: needed for the pilot agents

### 1. For each regime and clearing service, which client clearing legal model do you use: principal-to-principal, agency, or both? Does it differ between listed and OTC?

- **Why it matters:** Decides whether a client back-to-back trade exists and how trade lineage and client positions are described (sponsor decision 11 keeps the answer internal).
- **How to answer:** Table: regime, clearing service, listed or OTC, legal model, confirmed by Legal yes or no.
- **Concepts affected:** Client Clearing Legal Model, Client Back-to-Back Trade, Client Clearing Agreement
- **Who answers:** Legal with ETD and OTC Clearing product owners
<sub>question q03</sub>

### 2. Which CCP account kinds do you hold or offer at each clearing service (house, net omnibus, gross omnibus, individually segregated, indirect basic or gross omnibus, sponsored participant), and which is the default for a new client?

- **Why it matters:** Sets the values the market onboarding agent can propose and the account a trade lands in by default.
- **How to answer:** Table: clearing service, account kinds held, account kinds offered to clients, default kind.
- **Concepts affected:** CCP Account, Client Omnibus Account, Individually Segregated Client Account, Indirect Client Account, House Account
- **Who answers:** ETD Clearing product owner
<sub>question q04</sub>

### 3. How is a client's segregation election captured, dated and changed: per CCP, per clearing service or per legal entity, and which document records the disclosure it was based on?

- **Why it matters:** Defines the grain and the evidence of Segregation Election, and how an agent can tell which clients a change of account type affects.
- **How to answer:** Short description: grain, who records it, document name (generic), how a change is dated.
- **Concepts affected:** Segregation Election, Client Clearing Agreement
- **Who answers:** Reference & Client Data with Legal
<sub>question q05</sub>

### 4. How many account levels do you keep between the CCP account and the client (for example client master account, sub-accounts, execution accounts); what does each team call each level; how are client accounts mapped to CCP accounts at each reference CCP (one to one, many to one, one to several); and who maintains the mapping and how are changes dated? (Answered by Reference and Client Data with the ETD post-trade operations lead.)

- **Why it matters:** Confirms the three-level account structure, the place of the CCP Position Account and the internal aliases agents must recognise (the names stay in the internal layer).
- **How to answer:** Diagram or list of levels from CCP to client sub-account, with the usual name per team and the owner of the mapping.
- **Concepts affected:** CCP Account, CCP Position Account, Account, Client Account
- **Who answers:** Reference & Client Data lead with ETD post-trade operations lead
- **Joint question:** also covers what Parties, roles, clients and accounts needed to ask.
<sub>question q06</sub>

### 5. When someone asks for 'the client's positions at CCP Z', what should the default answer be: the CCP's figures, your internal figures, or both labelled? Gross or net? At which cycle of the clearing date?

- **Why it matters:** Sets the default basis and source for Position (the open question on positions asks for a firm decision).
- **How to answer:** Choice of source (CCP, internal, both), basis (gross, net, both) and cycle (end of day, intraday).
- **Concepts affected:** Position, Listed Position, Cleared OTC Position
- **Who answers:** ETD post-trade operations lead with ETD Clearing product owner
<sub>question q11</sub>

### 6. If any of your entities is registered as a futures commission merchant, which US customer account classes does it maintain (futures, foreign futures, cleared swaps), and at which derivatives clearing organisations?

- **Why it matters:** Seeds the US values of Client Omnibus Account and the segregation rules agents must apply in the US.
- **How to answer:** Table: account class, DCO, yes or no.
- **Concepts affected:** Client Omnibus Account, Segregation Model, CCP Account
- **Who answers:** ETD Clearing product owner with OTC Clearing product owner
<sub>question q17</sub>

### 7. Which words do your teams use for 'clearing member', 'clearing broker', 'CCP account', 'omnibus' and 'position', and do they mean something different in any team?

- **Why it matters:** Lets the internal layer carry the firm's aliases and flags words that must be treated as ambiguous; the words themselves never go into the repository.
- **How to answer:** Table: our word, team, meaning in that team (by ontology concept name).
- **Concepts affected:** Clearing Member, Clearing Broker, CCP Account, Client Omnibus Account, Position
- **Who answers:** Reference & Client Data lead
<sub>question q19</sub>

## Priority 2: needed before go-live

### 8. Which position transfers do you handle (client moving in, client moving out, account corrections, member restructuring), and who approves them? (Charges are asked in the fees questions.)

- **Why it matters:** Scopes Position Transfer, its triggers and the related fee events.
- **How to answer:** Table: trigger, approver role, charged yes or no, typical frequency (low, medium, high).
- **Concepts affected:** Position Transfer, Fee Charge
- **Who answers:** ETD post-trade operations lead with ETD Clearing product owner
<sub>question q13</sub>

### 9. Do clients name back-up clearing members, do you act as back-up for other members' clients, and do you track for each client whether its positions are portable?

- **Why it matters:** Decides whether Back-up Clearing Member and Porting are needed before the next release (reviewer question on this page).
- **How to answer:** Yes or no for each part; if tracked, at which grain (client, CCP, account).
- **Concepts affected:** Back-up Clearing Member, Porting, Segregation Election
- **Who answers:** ETD Clearing product owner with Legal
<sub>question q14</sub>

### 10. Does one client clearing agreement cover a client's listed and OTC clearing, or are they separate? Which public documentation families do you use per regime (for example an industry addendum or a customer agreement)?

- **Why it matters:** Shapes the Client Clearing Agreement as one agreement or several, and which terms an agent can look for in each.
- **How to answer:** Per regime: one or separate agreements; documentation family by generic name; who holds the signed versions.
- **Concepts affected:** Client Clearing Agreement, Agreement
- **Who answers:** Legal
<sub>question q15</sub>

### 11. When a client is cleared at a CCP where you are already a member, what steps are needed to open its account and how long do they usually take? Who requests the account at the CCP?

- **Why it matters:** Gives the market onboarding agent the account-opening part of 'what it takes', without needing internal systems.
- **How to answer:** Ordered list of steps with owner role and usual lead time range.
- **Concepts affected:** CCP Account, Client Clearing Agreement, Segregation Election
- **Who answers:** Client onboarding lead with ETD Clearing product owner
<sub>question q18</sub>

### 12. Which position adjustments do you make at each CCP (closing long against short in gross accounts, open and close corrections, others), who sends the open and close instructions (operations, the client, an automatic rule), and by when?

- **Why it matters:** Defines the Position Adjustment values in use and explains position changes without trades.
- **How to answer:** Table: CCP, adjustment type, requested by (client or firm), deadline.
- **Concepts affected:** Position Adjustment, Position Reconciliation
- **Who answers:** ETD post-trade operations lead
<sub>question q17</sub>

### 13. Under which events do you treat a client as in default toward you, and which remedies (close-out, transfer, hedge) do you use, per regime and client clearing legal model? (Answered by Legal with credit risk.)

<sub>question q22</sub>

### 14. How are client money and segregated funds held and checked per regime (for example US segregated and secured amounts, UK client money), and do you add your own funds as a buffer?

- **Why it matters:** Decides whether the ontology needs a client funds requirement concept (now in 'Not yet in the catalogue').
- **How to answer:** Regimes concerned; daily check yes or no; buffer of own funds yes or no.
- **Concepts affected:** Segregation Model, Client Account
- **Who answers:** ETD Clearing product owner with Legal and the Collateral Manager
<sub>question q23</sub>
