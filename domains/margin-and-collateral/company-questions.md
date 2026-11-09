# Margin and collateral: questions for our firm

These questions capture how **our firm** works in this domain, so the ontology can be tailored to it. The answers are firm-specific: record them in the internal workspace, **never in this repository**. Ask them in a meeting with the people named; several questions are shared with other domains and are best answered in a joint session.

## Priority 1: needed for the pilot agents

### 1. When someone asks 'what margin is required for this client?', which figure do your teams mean by default: what the CCP requires on the client's account, or what you require from the client? Does the answer differ by desk or product?

- **Why it matters:** Sets the default tier an agent may assume, or confirms that it must always ask.
- **How to answer:** Default tier per team or product, or 'no default, always ask'.
- **Concepts affected:** Margin Requirement, Margin Provider, Margin Taker
- **Who answers:** Collateral Manager with Risk
<sub>question q01</sub>

### 2. For each reference CCP and clearing service, how do you set client initial margin: copy the CCP figure, apply a multiplier or add-on, or run your own model; where a regime or CCP sets a minimum client margin, how is it applied; and which grouping of clients does the risk function use for uplifts (ownership, credit or another group)? Who decides?

- **Why it matters:** Gives the firm values of the member-to-client methodology and the Client Margin Uplift.
- **How to answer:** Table: clearing service, method (replication, multiplier, add-on, own model), level at which it is set, approving role.
- **Concepts affected:** Margin Methodology, Client Margin Uplift, Initial Margin Requirement
- **Who answers:** Risk with Collateral Manager
<sub>question q02</sub>

### 3. When a CCP makes an intraday call on your client accounts, do you pass it on to clients? To all clients or some, on the same day or later, and with what deadline?

- **Why it matters:** Decides whether Intraday Margin Call exists at the member-to-client tier in your firm.
- **How to answer:** Per clearing service: passed on yes or no; client scope; timing; deadline.
- **Concepts affected:** Intraday Margin Call, Margin Call Terms
- **Who answers:** Collateral Manager
<sub>question q03</sub>

### 4. Which client-level margin call deadlines must an operations agent know, in which time zone and business calendar, and what happens when a client misses one? (CCP payment deadlines are asked in the post-trade questions.)

- **Why it matters:** Gives the deadlines and consequences inside Margin Call Terms and the cut-offs operations track.
- **How to answer:** Table: tier, clearing service or client group, deadline, calendar and time zone, consequence and escalation.
- **Concepts affected:** Margin Call Terms, Margin Call, Margin Call Status
- **Who answers:** ETD post-trade operations lead with Collateral Manager
<sub>question q04</sub>

### 5. Which statuses do you track for a margin call, at CCP level and at client level? Can a client dispute a call, and how is a partly met call handled?

- **Why it matters:** Sets the harmonised values of Margin Call Status and whether 'disputed' applies.
- **How to answer:** List of native statuses with meaning; yes or no on disputes; rule for partly met calls.
- **Concepts affected:** Margin Call Status, Margin Call
- **Who answers:** ETD post-trade operations lead
<sub>question q05</sub>

### 6. Where does client excess collateral sit: posted to the CCP in the client's account, or retained by you? Answer per regime (EU, UK, US) and account kind, and say whether it is a client choice where the regime allows one. (Answered by the Collateral Manager with Legal.)

- **Why it matters:** Fixes where Margin Excess or Shortfall is held and how returns are modelled.
- **How to answer:** Table: region, account type, where excess sits, return timing.
- **Concepts affected:** Margin Excess or Shortfall, Collateral, Collateral Instruction
- **Who answers:** Collateral Manager with Legal
- **Joint question:** also covers what Clearing: services, accounts and client clearing needed to ask.
<sub>question q06</sub>

### 7. In a net omnibus client account, do you calculate a margin requirement per client, and how do you explain the difference between the sum of client figures and what the CCP calls?

- **Why it matters:** Confirms that a client-level figure exists only in your own calculation and how it relates to the CCP figure.
- **How to answer:** Yes or no per clearing service; short description of how differences are explained.
- **Concepts affected:** Margin Requirement, Margin Portfolio
- **Who answers:** Risk
<sub>question q07</sub>

### 8. When your teams say 'margin', 'margin held', 'margin posted' or 'margin balance', which of these mean a requirement and which mean collateral? Are there other words in daily use?

- **Why it matters:** Sets aliases with their scope so agents resolve everyday words correctly.
- **How to answer:** List of terms with meaning and the teams that use them (internal terms stay outside the repository).
- **Concepts affected:** Margin Requirement, Collateral
- **Who answers:** Collateral Manager
<sub>question q08</sub>

### 9. Do you pay or charge interest on clients' cash collateral? On what basis (benchmark rate, spread, by currency, per client or account type), is it passed on from the CCP rate, and how are negative rates treated?

- **Why it matters:** Gives the terms behind Cash Collateral Interest and supports the collateral income part of open question 9.
- **How to answer:** Per currency and client group: paid or charged, rate basis, negative-rate treatment, owning team.
- **Concepts affected:** Cash Collateral Interest, Collateral Arrangement
- **Who answers:** Collateral Manager with Business Finance
- **Joint question:** also covers what Fees, revenue and contribution needed to ask.
<sub>question q09</sub>

## Priority 2: needed before go-live

### 10. Do you pass price alignment amounts received from or paid to CCPs on to clients in full, net, or not at all?

- **Why it matters:** Decides whether Price Alignment Amount exists at the client tier and how it relates to collateral income.
- **How to answer:** Per clearing service: full, net or not passed on.
- **Concepts affected:** Price Alignment Amount
- **Who answers:** OTC Clearing product owner with Collateral Manager
<sub>question q10</sub>

### 11. For your OTC clearing services, which variation margin treatment applies to which account types today, and how is it treated in your internal reporting?

- **Why it matters:** Gives the firm view of settled-to-market versus collateralised-to-market per service and account type.
- **How to answer:** Table: clearing service, account type, treatment, effective date if known, internal reporting treatment.
- **Concepts affected:** Variation Margin Requirement, Price Alignment Amount
- **Who answers:** OTC Clearing product owner with Legal and Finance
<sub>question q11</sub>

### 12. Which kinds of collateral do you accept from clients, and do you apply your own haircuts or limits that are stricter than the CCP's?

- **Why it matters:** Decides whether a client-tier eligibility schedule exists and how it differs from the CCP's.
- **How to answer:** Asset categories accepted; own haircuts yes or no; own limits yes or no; by client group if different.
- **Concepts affected:** Collateral Eligibility Schedule, Collateral Haircut, Concentration Limit
- **Who answers:** Collateral Manager with Risk
<sub>question q12</sub>

### 13. Under which legal form do clients provide collateral to you (title transfer or security interest), by region and service? Do you have a right to reuse client assets, and do you use it?

- **Why it matters:** Gives the legal form and right of use per arrangement.
- **How to answer:** Table: region, service, legal form, right of use yes or no.
- **Concepts affected:** Collateral Arrangement, Collateral
- **Who answers:** Legal
<sub>question q13</sub>

### 14. Which margin components do your client statements show (base initial margin, add-ons, premium margin, delivery margin, variation margin)? Do you show CCP add-ons separately from your own uplift?

- **Why it matters:** Sets the component values used at the client tier and keeps CCP add-ons apart from the broker uplift.
- **How to answer:** List of components shown per statement type.
- **Concepts affected:** Margin Requirement Component, Margin Add-on, Client Margin Uplift
- **Who answers:** Collateral Manager with Client service
<sub>question q14</sub>

### 15. Do you pre-fund client margin at the CCP before the client pays, or cover a client shortfall with your own resources? In which cases, and is this tracked as a cost?

- **Why it matters:** Tells whether a funding concept is needed beside margin and how it feeds cost and contribution.
- **How to answer:** Yes or no per region and service; cases; whether costed and where.
- **Concepts affected:** Margin Excess or Shortfall, Margin Call
- **Who answers:** Collateral Manager with Treasury
<sub>question q15</sub>

### 16. Do any clients have unsecured margin thresholds or credit lines, so that a shortfall below a level is not called? Which client types?

- **Why it matters:** Gives the threshold values in Margin Call Terms and explains shortfalls without calls.
- **How to answer:** Yes or no; client types; who approves.
- **Concepts affected:** Margin Call Terms, Margin Excess or Shortfall
- **Who answers:** Risk
<sub>question q17</sub>

### 17. Do you benefit from cross-margining at any reference CCP (across products, services or CCPs), and do you offer clients portfolio margining across products?

- **Why it matters:** Gives the firm values of Margin Portfolio and whether client margin reflects offsets.
- **How to answer:** Per CCP: cross-margining used yes or no and scope; client offer yes or no.
- **Concepts affected:** Margin Portfolio
- **Who answers:** Risk with ETD and OTC Clearing product owners
<sub>question q18</sub>

### 18. In which currencies do you call clients, and how do you treat a requirement in one currency covered by cash or securities in another?

- **Why it matters:** Gives the currency basis of client requirements and calls and the use of currency mismatch haircuts.
- **How to answer:** Call currencies per client group; conversion rule; currency haircut yes or no.
- **Concepts affected:** Margin Call Terms, Collateral Haircut, Margin Requirement
- **Who answers:** Collateral Manager
<sub>question q20</sub>

### 19. While a give-up is pending and you carry the trade as giving clearing member, who bears or is called for the margin, and is it recharged to the executing broker or client?

<sub>question q24</sub>

### 20. On client statements, how is account equity built: is variation margin settled each day shown in the cash balance or kept in open trade equity, and which components (cash, open trade equity, option value, securities) count toward the margin excess or deficit?

- **Why it matters:** Sets what an agent adds up when it explains an excess or deficit, and what 'equity' means on a statement.
- **How to answer:** Statement layout per regime (US, EU and UK); components counted toward the excess; whether open trade equity can be withdrawn.
- **Concepts affected:** Open Trade Equity, Account Cash Balance, Account Equity, Margin Excess or Shortfall
- **Who answers:** Collateral Manager with the ETD post-trade operations lead
<sub>question q25</sub>

### 21. Do you apply a maintenance level below the initial margin requirement for some clients or regimes (for example US futures), and when equity falls below it, does the call restore the initial level?

- **Why it matters:** Confirms the proposed answer on 'margin' and 'initial margin' (two call trigger levels of one requirement) and the trigger an agent must know.
- **How to answer:** Regimes and client types concerned; trigger level; level restored by the call.
- **Concepts affected:** Margin Call Terms, Margin Requirement, Account Equity
- **Who answers:** Collateral Manager with Risk
<sub>question q26</sub>

## Priority 3: later

### 22. Do you hold client and CCP collateral through custodians, settlement systems or triparty agents, by category, and is a pledge recorded as a movement between accounts?

- **Why it matters:** Decides how Collateral Movement and Collateral Instruction are recorded for pledged assets.
- **How to answer:** Categories of holding location per tier (no provider names in the repository); pledge recorded as movement yes or no.
- **Concepts affected:** Collateral Movement, Collateral Instruction, Collateral
- **Who answers:** Collateral Manager with Operations
<sub>question q21</sub>

### 23. For physically delivered futures, do you call clients for delivery margin around expiry, and from when?

- **Why it matters:** Confirms whether delivery margin is a component used at the client tier.
- **How to answer:** Yes or no per product family; start point relative to expiry.
- **Concepts affected:** Margin Requirement Component
- **Who answers:** ETD Clearing product owner
<sub>question q23</sub>

### 24. For cleared OTC positions, which valuation do you show clients: the CCP's or your own, and how do you explain a difference?

- **Why it matters:** Tells an agent which valuation party to state when a client asks what a position is worth.
- **How to answer:** Valuation party per product; how differences are reported.
- **Concepts affected:** Position Valuation, Variation Margin Requirement
- **Who answers:** OTC Clearing product owner with the Collateral Manager
<sub>question q27</sub>
