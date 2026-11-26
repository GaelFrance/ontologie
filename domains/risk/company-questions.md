# Risk: questions for our firm

These questions capture how **our firm** works in this domain, so the ontology can be tailored to it. Record the answers in this domain's [expert workbook](questions-for-experts.xlsx) in this repository; the Ontology Lead turns them into changes, and definitions stay generic. Ask them in a meeting with the people named; several questions are shared with other domains and are best answered in a joint session. Each question names its area: the clients we clear, execution, or CCPs.

## Priority 1: needed for the pilot agents

### 1. (The clients we clear) Which limits does the risk function set on a client before we clear for it (trade quantity, notional, margin, exposure, stress loss), at which level (client, group of clients defined for risk purposes, account, product, clearing service), and which of them are checked automatically at take-up or submission?

- **Why it matters:** Gives the kinds of Risk Limit in use and tells the give-up agent which limit decides automatic acceptance.
- **How to answer:** Table: limit kind, level, basis, checked pre-trade yes or no, checked at take-up yes or no, owner.
- **Concepts affected:** Risk Limit, Clearing Limit, Clearing Member Acceptance
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
- **Concepts affected:** Client Clearing Exposure, Risk Exposure
- **Who answers:** Risk with Collateral Manager
<sub>question q03</sub>

### 4. (Execution) Which pre-trade limits apply to each channel (care, broker algorithm, direct electronic access, sponsored access), who sets them (executing desk, clearing risk, Compliance, the venue) and who may activate a kill switch?

- **Why it matters:** Gives the values of Pre-trade Limit per channel and the parties allowed to trigger a Kill Switch Activation.
- **How to answer:** Table: channel, limit kind, setting role, kill switch authority.
- **Concepts affected:** Risk Limit, Pre-trade Control Check
- **Who answers:** Listed Execution product owner with Risk and Compliance
<sub>question q04</sub>

### 5. (CCPs) For each reference CCP, which resources of ours stand at risk (house margin, default fund contribution, assessment commitment, guarantees to clients), and how often does the risk function review the CCP?

- **Why it matters:** Gives the components of CCP Exposure the firm follows and the cycle of the CCP Risk Assessment.
- **How to answer:** Table: CCP and clearing service, components counted, review frequency, approving role.
- **Concepts affected:** CCP Exposure, CCP Risk Assessment, Default Fund Contribution, Default Fund Assessment
- **Who answers:** Risk with ETD Clearing product owner and OTC Clearing product owner
<sub>question q05</sub>

### 6. (The clients we clear) Which group of clients does the risk function use for risk purposes (legal group, connected clients, fund manager and its funds), and does it ever equal the commercial group?

- **Why it matters:** Fills Client Risk Group and tells agents never to read it as the Commercial Group.
- **How to answer:** Grouping bases used, who sets membership, how often it is reviewed, and cases where it equals the commercial group.
- **Concepts affected:** Client Risk Group, Client Clearing Exposure
- **Who answers:** Risk with Reference & Client Data
<sub>question q13</sub>

### 7. (The clients we clear) Do you record a warning level reached as a breach? Do you distinguish breaches caused by new business from those caused by market moves? After a breach, do you run an ad hoc margin call, raise the client margin uplift, or both?

- **Why it matters:** Confirms what a Limit Breach records and the route from a breach to a Margin Call. Extends question q02.
- **How to answer:** Yes or no for each point, with the deciding role.
- **Concepts affected:** Limit Breach, Margin Call
- **Who answers:** Risk with the Collateral Manager
<sub>question q14</sub>

### 8. (The clients we clear) When exposure is measured after collateral, is client collateral valued with the margin eligibility haircuts or with risk's own haircuts? Is client excess, held by us or passed to the CCP, counted?

- **Why it matters:** Gives the valuation basis an agent must state for Client Clearing Exposure after collateral.
- **How to answer:** Haircut basis used; client excess counted yes or no, where it is held.
- **Concepts affected:** Client Clearing Exposure
- **Who answers:** Risk with the Collateral Manager
<sub>question q15</sub>

### 9. (The clients we clear) Is the clearing limit the same limit as the client credit limit, or a separate limit with a separate owner? Are clearing limits set only through the client credit assessment, or also at the desk's request?

- **Why it matters:** Tells the give-up agent which limit decides acceptance and who owns it.
- **How to answer:** Same or separate limit; owner of each; who may request a clearing limit.
- **Concepts affected:** Clearing Limit, Risk Limit
- **Who answers:** Risk with the ETD Clearing product owner
<sub>question q16</sub>

### 10. (The clients we clear) Does the utilisation of our clearing limit count give-up lines pending take-up? Between acceptance on a give-up facility and registration at the CCP, do we treat the quantity as ours or as the giving member's, for limits and exposure?

- **Why it matters:** Sets what Limit Utilisation counts at take-up and where Unaccepted Give-up Exposure ends for the firm.
- **How to answer:** Yes or no for pending lines; ours or the giving member's between acceptance and registration, for limits and for exposure.
- **Concepts affected:** Limit Utilisation, Unaccepted Give-up Exposure
- **Who answers:** Risk with the ETD post-trade operations lead
<sub>question q17</sub>

### 11. (Execution) For each channel, which pre-trade limits do we set ourselves, and which checks do we rely on the venue's or the clearing member's tools to apply? As clearing broker, do we set limits on venue platforms for clients or non-clearing members we clear for? Who may activate a kill switch, at which scope, and who may lift it?

- **Why it matters:** Separates the firm's own pre-trade limits from venue rule provisions in each check, and gives the kill switch practice. Extends question q04.
- **How to answer:** Table: channel, limit kind, setting party, applying party; kill switch authority, scope and who lifts it.
- **Concepts affected:** Risk Limit, Pre-trade Control Check
- **Who answers:** Listed Execution product owner with Risk
<sub>question q22</sub>

### 12. (CCPs) For each reference CCP, does our CCP exposure count house position replacement, amounts the CCP owes us, client trades and client collateral under the principal model? For which CCPs and account types is the collateral we post protected from the CCP's insolvency? Which events trigger an early CCP review?

- **Why it matters:** Gives the components of CCP Exposure the firm follows and the triggers of a CCP Risk Assessment. Extends question q05.
- **How to answer:** Table: CCP and clearing service, components counted, protection per account type (as assessed by Legal), trigger events.
- **Concepts affected:** CCP Exposure, CCP Risk Assessment
- **Who answers:** Risk with the Collateral Manager and Legal
<sub>question q26</sub>

## Priority 2: needed before go-live

### 13. (The clients we clear) How is a client assessed before onboarding and reviewed afterwards: who performs the assessment, which rating scale is used, how often is a client reviewed, and which events trigger an early review?

- **Why it matters:** Gives the steps and outcomes of Client Credit Assessment and the use of Client Risk Rating.
- **How to answer:** Steps, approving roles, review frequency by rating, trigger events.
- **Concepts affected:** Client Credit Assessment, Client Risk Group
- **Who answers:** Risk
<sub>question q06</sub>

### 14. (The clients we clear) Which forms of credit support do you accept from clients beyond collateral (parent guarantee, letter of credit, other), and do they change limits or margin?

- **Why it matters:** Confirms Credit Support Arrangement and its effect on Client Clearing Exposure.
- **How to answer:** List of forms accepted, effect on limit or margin, approving role.
- **Concepts affected:** Third-party Credit Support, Client Clearing Exposure
- **Who answers:** Risk with Legal
<sub>question q07</sub>

### 15. (The clients we clear) After a client default, which steps do you follow, in which order, and who decides each one (stop new business, hedge, close out, transfer, apply collateral, claim the shortfall)? Does it differ between listed and OTC clearing?

- **Why it matters:** Gives the steps of Client Default Management.
- **How to answer:** Ordered steps per clearing type, deciding role, usual time frame.
- **Concepts affected:** Client Default
- **Who answers:** Risk with Legal and ETD Clearing product owner
<sub>question q08</sub>

### 16. (Execution) How are execution errors handled: who decides whether an error is the firm's or the client's, when is a venue asked to cancel or adjust a trade, and in which account is an error position held and closed?

- **Why it matters:** Gives the resolutions of Execution Error and how Error Position is kept apart from client business and revenue.
- **How to answer:** Steps, deciding roles, account used, time allowed to close the position.
- **Concepts affected:** Execution Correction, Error Position
- **Who answers:** Listed Execution product owner with ETD post-trade operations lead
<sub>question q09</sub>

### 17. (Execution) Which trades executed for clients most often stay with the giving side because take-up is late, rejected or lapsed, and how is that risk followed until the CCP registers them to the clearing broker's account?

- **Why it matters:** Confirms Unaccepted Give-up Exposure and who follows it.
- **How to answer:** Typical causes, following role, escalation and time frame.
- **Concepts affected:** Unaccepted Give-up Exposure, Clearing Member Acceptance
- **Who answers:** ETD post-trade operations lead with Risk
<sub>question q10</sub>

### 18. (CCPs) Do you take part in the default management groups of the reference CCPs, and can our clients bid in a CCP's default auctions through us?

- **Why it matters:** Gives the firm's role in the auction step of a Clearing Member Default. The public rules on bidding are asked separately, once, from the rulebooks.
- **How to answer:** Per CCP and clearing service: participation in the default management group yes or no; clients may bid through us yes or no.
- **Concepts affected:** Clearing Member Default, Default Fund Contribution
- **Who answers:** Risk with ETD Clearing product owner and OTC Clearing product owner
<sub>question q11</sub>

### 19. (The clients we clear) Do you accept guarantees or letters of credit as margin cover counted in excess or shortfall, or only as credit support that reduces exposure or raises a limit?

- **Why it matters:** Sets the boundary between Third-party Credit Support and collateral. Extends question q07.
- **How to answer:** Per form of support: margin cover, credit support, or both; approving role.
- **Concepts affected:** Third-party Credit Support
- **Who answers:** Risk with Legal and the Collateral Manager
<sub>question q18</sub>

### 20. (The clients we clear) Does the firm act as sponsoring clearing member? If so, is its exposure to a sponsored participant treated as a client clearing exposure, and who bears assessments?

- **Why it matters:** Tells whether Client Clearing Exposure and Default Fund Assessment must cover sponsored participants.
- **How to answer:** Yes or no per CCP; treatment of the exposure; who bears assessments.
- **Concepts affected:** Client Clearing Exposure, Default Fund Assessment
- **Who answers:** Risk with the ETD Clearing and OTC Clearing product owners and Legal
<sub>question q19</sub>

### 21. (The clients we clear) Do we clear for clients that clear for indirect clients, and which procedure applies to the indirect clients when such a client defaults?

- **Why it matters:** Confirms the indirect-client part of Client Default and of Client Clearing Exposure.
- **How to answer:** Yes or no per clearing service; the procedure followed for the indirect clients.
- **Concepts affected:** Client Default, Client Clearing Exposure
- **Who answers:** Legal with Risk
<sub>question q20</sub>

### 22. (The clients we clear) Does the client credit assessment use the client's regulatory classifications as inputs, and who supplies them?

- **Why it matters:** Tells whether a Client Credit Assessment reads regulatory classifications, which it does not determine.
- **How to answer:** Classifications used, supplying team.
- **Concepts affected:** Client Credit Assessment
- **Who answers:** Risk with Compliance
<sub>question q21</sub>

### 23. (Execution) Where does an error position go when the error is made by a direct electronic access client, by a third-party executing member, or at the clearing broker (allocation or booking)? What happens to a gain on an error position?

- **Why it matters:** Confirms who holds an Error Position and the responsible parties recorded on Execution Correction. Extends question q09.
- **How to answer:** Per case: account used, responsible party, treatment of a gain.
- **Concepts affected:** Error Position, Execution Correction
- **Who answers:** Listed Execution product owner with the ETD post-trade operations lead
<sub>question q23</sub>

### 24. (Execution) On which side does the firm carry unaccepted give-up exposure: as giving clearing member, as executing broker using another clearing member, or both? Who follows it until registration? Is it followed per client, per executing broker or per receiving member? Does it include quantity not yet allocated?

- **Why it matters:** Gives the observing party of Unaccepted Give-up Exposure and informs whether unallocated quantity should be covered. Extends question q10.
- **How to answer:** Side or sides; following role; level of follow-up; unallocated quantity included yes or no.
- **Concepts affected:** Unaccepted Give-up Exposure
- **Who answers:** ETD post-trade operations lead with Risk
<sub>question q24</sub>

### 25. (Execution) Which firm risk limits exist because a rule requires a control, and is that link recorded? Are pre-trade position caps used to keep clients within regulator or venue position limits?

- **Why it matters:** Keeps a Risk Limit required by a rule apart from the rule itself and from a Position Limit.
- **How to answer:** List of limits with the rule that requires them; recorded yes or no; position caps used yes or no.
- **Concepts affected:** Risk Limit, Position Limit
- **Who answers:** Risk with Compliance
<sub>question q25</sub>

### 26. (CCPs) From each reference CCP's rulebook, with its version: are members required to bid in default auctions, does the CCP juniorise the default fund contribution of members that bid poorly, and may clients bid through a member?

- **Why it matters:** Public part of question q11: rulebook facts for the auction step of a Clearing Member Default, answered once.
- **How to answer:** Per CCP and clearing service: mandatory bidding, juniorisation, client bidding, rulebook version.
- **Concepts affected:** Clearing Member Default, Default Fund Contribution
- **Who answers:** Legal, once from the rulebooks
<sub>question q28</sub>

## Priority 3: later

### 27. (CCPs) How do our client clearing agreements pass on to clients the assessments, variation margin gains haircutting and tear-up of the reference CCPs, and how are clients told about them?

- **Why it matters:** Confirms whether CCP Loss Allocation must be traced to client accounts. Which tools a CCP can apply to client accounts is asked separately, once, from the rulebooks.
- **How to answer:** Per CCP and client clearing legal model: tool, passed on to clients yes or no, contractual basis, how clients are told.
- **Concepts affected:** CCP Loss Allocation, Default Waterfall
- **Who answers:** Legal with Risk
<sub>question q12</sub>

### 28. (CCPs) Do you treat a replenishment of our default fund contribution after a default as an assessment, for exposure and for funding cost?

- **Why it matters:** Keeps Default Fund Assessment apart from the replenishment of a Default Fund Contribution in the firm's figures.
- **How to answer:** Yes or no for exposure; yes or no for funding cost.
- **Concepts affected:** Default Fund Assessment, Default Fund Contribution
- **Who answers:** Risk with the Collateral Manager
<sub>question q27</sub>

### 29. (CCPs) From each reference CCP's rulebook, with its version: which loss allocation tools can the CCP apply to client accounts (for example variation margin gains haircutting or tear-up)?

- **Why it matters:** Public part of question q12: which CCP Loss Allocation tools can reach client accounts, answered once.
- **How to answer:** Per CCP and clearing service: tools that can reach client accounts, rulebook version.
- **Concepts affected:** CCP Loss Allocation, Default Waterfall
- **Who answers:** Legal, once from the rulebooks
<sub>question q29</sub>
