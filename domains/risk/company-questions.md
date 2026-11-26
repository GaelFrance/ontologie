# Risk: questions for our firm

These questions capture how **our firm** works in this domain, so the ontology can be tailored to it. Record the answers in this domain's [expert workbook](questions-for-experts.xlsx) in this repository; the Ontology Lead turns them into changes, and definitions stay generic. Ask them in a meeting with the people named; several questions are shared with other domains and are best answered in a joint session. Each question names its area: the clients we clear, execution, or CCPs.

## Priority 1: needed for the pilot agents

### 1. (The clients we clear) Which limits does the risk function set on a client before we clear for it (trade quantity, notional, margin, exposure, stress loss), at which level (client, group of clients defined for risk purposes, account, product, clearing service), and which of them are checked automatically at take-up or submission?

- **Why it matters:** Gives the kinds of Risk Limit in use and tells the give-up agent which limit decides automatic acceptance.
- **How to answer:** Table: limit kind, level, basis, checked pre-trade yes or no, checked at take-up yes or no, owner.
- **Concepts affected:** Risk Limit, Clearing Limit, Pre-trade Limit, Clearing Member Acceptance
- **Who answers:** Risk with ETD Clearing product owner
<sub>question q01</sub>

### 2. (The clients we clear) When a client's limit is exceeded, what happens: who is told, which actions are possible (warning, referral, temporary increase, margin call, block of new trades) and who decides each one?

- **Why it matters:** Gives the actions and statuses of a Limit Breach.
- **How to answer:** Table: limit kind, warning level yes or no, action, deciding role, time allowed.
- **Concepts affected:** Limit Breach, Limit Utilisation, Margin Call
- **Who answers:** Risk
<sub>question q02</sub>

### 3. (The clients we clear) When someone asks "what is our exposure to client A", which figure do your teams mean by default: before or after collateral, current or under stress, one clearing service or all, the client alone or its group?

- **Why it matters:** Sets the default an agent may assume for Client Clearing Exposure, or confirms that it must always ask.
- **How to answer:** Default per team, or "no default, always ask".
- **Concepts affected:** Client Clearing Exposure, Stress Loss, Risk Exposure
- **Who answers:** Risk with Collateral Manager
<sub>question q03</sub>

### 4. (Execution) Which pre-trade limits apply to each channel (care, broker algorithm, direct electronic access, sponsored access), who sets them (executing desk, clearing risk, Compliance, the venue) and who may activate a kill switch?

- **Why it matters:** Gives the values of Pre-trade Limit per channel and the parties allowed to trigger a Kill Switch Activation.
- **How to answer:** Table: channel, limit kind, setting role, kill switch authority.
- **Concepts affected:** Pre-trade Limit, Pre-trade Control Check, Kill Switch Activation
- **Who answers:** Listed Execution product owner with Risk and Compliance
<sub>question q04</sub>

### 5. (CCPs) For each reference CCP, which resources of ours stand at risk (house margin, default fund contribution, assessment commitment, guarantees to clients), and how often does the risk function review the CCP?

- **Why it matters:** Gives the components of CCP Exposure the firm follows and the cycle of the CCP Risk Assessment.
- **How to answer:** Table: CCP and clearing service, components counted, review frequency, approving role.
- **Concepts affected:** CCP Exposure, CCP Risk Assessment, Default Fund Contribution, Default Fund Assessment
- **Who answers:** Risk with ETD Clearing product owner and OTC Clearing product owner
<sub>question q05</sub>

## Priority 2: needed before go-live

### 6. (The clients we clear) How is a client assessed before onboarding and reviewed afterwards: who performs the assessment, which rating scale is used, how often is a client reviewed, and which events trigger an early review?

- **Why it matters:** Gives the steps and outcomes of Client Credit Assessment and the use of Client Risk Rating.
- **How to answer:** Steps, approving roles, review frequency by rating, trigger events.
- **Concepts affected:** Client Credit Assessment, Client Risk Rating
- **Who answers:** Risk
<sub>question q06</sub>

### 7. (The clients we clear) Which forms of credit support do you accept from clients beyond collateral (parent guarantee, letter of credit, other), and do they change limits or margin?

- **Why it matters:** Confirms Credit Support Arrangement and its effect on Client Clearing Exposure.
- **How to answer:** List of forms accepted, effect on limit or margin, approving role.
- **Concepts affected:** Credit Support Arrangement, Client Clearing Exposure
- **Who answers:** Risk with Legal
<sub>question q07</sub>

### 8. (The clients we clear) After a client default, which steps do you follow, in which order, and who decides each one (stop new business, hedge, close out, transfer, apply collateral, claim the shortfall)? Does it differ between listed and OTC clearing?

- **Why it matters:** Gives the steps of Client Default Management.
- **How to answer:** Ordered steps per clearing type, deciding role, usual time frame.
- **Concepts affected:** Client Default Management, Client Default
- **Who answers:** Risk with Legal and ETD Clearing product owner
<sub>question q08</sub>

### 9. (Execution) How are execution errors handled: who decides whether an error is the firm's or the client's, when is a venue asked to cancel or adjust a trade, and in which account is an error position held and closed?

- **Why it matters:** Gives the resolutions of Execution Error and how Error Position is kept apart from client business and revenue.
- **How to answer:** Steps, deciding roles, account used, time allowed to close the position.
- **Concepts affected:** Execution Error, Error Position
- **Who answers:** Listed Execution product owner with ETD post-trade operations lead
<sub>question q09</sub>

### 10. (Execution) Which trades executed for clients most often stay with the giving side because take-up is late, rejected or lapsed, and how is that risk followed until the clearing broker accepts them?

- **Why it matters:** Confirms Unaccepted Give-up Exposure and who follows it.
- **How to answer:** Typical causes, following role, escalation and time frame.
- **Concepts affected:** Unaccepted Give-up Exposure, Clearing Member Acceptance
- **Who answers:** ETD post-trade operations lead with Risk
<sub>question q10</sub>

### 11. (CCPs) Do you take part in CCP default management (default management groups, auctions)? For each reference CCP, are you required to bid in auctions, and what happens to your default fund contribution if you bid poorly?

- **Why it matters:** Gives the firm's role in a Default Management Auction.
- **How to answer:** Per CCP: participation, obligation to bid, consequence.
- **Concepts affected:** Default Management Auction, Default Fund Contribution
- **Who answers:** Risk with ETD Clearing product owner and OTC Clearing product owner
<sub>question q11</sub>

## Priority 3: later

### 12. (CCPs) Which loss allocation tools of the reference CCPs could reach our clients (for example variation margin gains haircutting or tear-up), and how are clients told about them?

- **Why it matters:** Confirms whether CCP Loss Allocation must be traced to client accounts.
- **How to answer:** Per CCP: tools, whether passed on to clients, contractual basis.
- **Concepts affected:** CCP Loss Allocation, Default Waterfall
- **Who answers:** Legal with Risk
<sub>question q12</sub>
