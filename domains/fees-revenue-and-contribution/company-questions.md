# Fees, revenue and contribution: questions for our firm

These questions capture how **our firm** works in this domain, so the ontology can be tailored to it. The answers are firm-specific: record them in the internal workspace, **never in this repository**. Ask them in a meeting with the people named; several questions are shared with other domains and are best answered in a joint session.

## Priority 1: needed for the pilot agents

### 1. For each service (execution-only, clearing-only, execute-and-clear) and region, do you price clients all-in, fees-plus, or both, and how is the choice recorded per client?

- **Why it matters:** Decides how client fees relate to venue and CCP fees and whether a fee can be compared with a tariff; sets the values of pricing form on client pricing terms.
- **How to answer:** Table per service and region: all-in, fees-plus or both; where the choice is recorded (agreement, fee letter, pricing record).
- **Concepts affected:** Client Pricing Terms, Client Execution Fee, Client Clearing Fee, Pass-through Charge
- **Who answers:** Revenue domain owner
<sub>question q01</sub>

### 2. In which units are client rates quoted and stored: per contract side, per round turn, per ticket, per notional, per percentage of premium, or fixed periodic amounts? Does it differ for listed and OTC?

- **Why it matters:** Sets the charge basis values the agents must expect and whether rates can be compared across clients.
- **How to answer:** List of units per service and asset class, with the unit used as the stored reference.
- **Concepts affected:** Charge Basis, Fee Rate, Client Pricing Terms
- **Who answers:** Revenue domain owner
<sub>question q02</sub>

### 3. In management reporting, are venue, CCP and regulatory fees passed on to clients shown gross (in revenue and in cost) or net? Is the same rule used for every service and region?

- **Why it matters:** Fixes the gross or net rule of the management reporting basis; without it revenue figures are not comparable.
- **How to answer:** Choice per service: gross, net, or both shown; any exceptions.
- **Concepts affected:** Management Reporting Basis, Pass-through Charge, Revenue, Execution Revenue, Clearing Revenue
- **Who answers:** Business Finance
<sub>question q03</sub>

### 4. Do you charge bundled execute-and-clear rates? If so, how is the rate split between execution and clearing revenue, and who owns the split rule?

- **Why it matters:** Revenue is attributed per service (sponsor decision); a bundled fee cannot feed execution or clearing revenue without a split rule.
- **How to answer:** Yes or no; description of the split rule (fixed proportion, notional clearing rate, other) and its owner. No amounts needed.
- **Concepts affected:** Bundled Execution and Clearing Fee, Management Reporting Basis, Execution Revenue, Clearing Revenue
- **Who answers:** Revenue domain owner
- **Joint question:** also covers what Service offering and market access needed to ask.
<sub>question q04</sub>

### 5. When you act as executing broker on trades given up to another clearing broker, how is your executing brokerage billed and collected: from the client, from the clearing broker, or through an industry give-up payment service?

- **Why it matters:** Sets the debtor, payer and collector of brokerage received, and when it counts as earned.
- **How to answer:** Per region or client type: billed to whom, collected how, typical delay.
- **Concepts affected:** Executing Broker Brokerage Charge, Fee Collector, Execution Revenue
- **Who answers:** Listed Execution product owner
<sub>question q05</sub>

### 6. When you act as clearing broker for given-in trades, do you pay other executing brokers' brokerage on clients' behalf and recharge it? Is that recharge shown in your revenue, your cost, or neither?

- **Why it matters:** Avoids counting executing brokerage twice and decides how a recharge appears in revenue.
- **How to answer:** Yes or no per region; treatment in management reporting (revenue and cost, net, or outside).
- **Concepts affected:** Executing Broker Brokerage Charge, Pass-through Charge, Clearing Revenue, Cost
- **Who answers:** ETD Clearing product owner
<sub>question q06</sub>

### 7. Where you use a third-party executing member or a third-party clearing member, how are their fees recorded: recharged to the client, absorbed as cost, and attributed to which client and service?

- **Why it matters:** Third-party execution is in scope; these fees are a main candidate for the first cost perimeter.
- **How to answer:** Per access route: recharged or absorbed; attribution level (client, service, venue).
- **Concepts affected:** Pass-through Charge, Cost, Cost Perimeter, Executing Broker Brokerage Charge
- **Who answers:** Business Finance
<sub>question q07</sub>

### 8. Which date decides the period of management revenue (trade date, CCP clearing date, invoice date or cash receipt), how is period-end assigned for trades in late sessions, and how are month-end accruals and later invoice differences handled?

- **Why it matters:** The ontology's operational default is the CCP clearing date; finance may use another date role, which every revenue answer must then state.
- **How to answer:** Date role used for revenue and for cost; accrual and true-up practice in one or two sentences.
- **Concepts affected:** Management Reporting Basis, Revenue, Fee Charge, Fee Adjustment
- **Who answers:** Business Finance
<sub>question q08</sub>

### 9. Is management revenue reported per booking entity, consolidated, or both, and how are revenues from affiliates eliminated? (Which entity books what is asked in the legal-entity question.)

- **Why it matters:** Defines the observing entity and elimination rule that every revenue and contribution answer requires.
- **How to answer:** List of entity types (not names in the repository), reporting levels, elimination yes or no.
- **Concepts affected:** Management Reporting Basis, Revenue, Contribution
- **Who answers:** Business Finance
<sub>question q09</sub>

### 10. Revenue is attributed to the contractual client (decided). Which reporting dimensions and roll-ups do business reviews need above it: commercial group, the investment manager's group of funds, ownership group; service offering or another unit (desk, business line, product group) to be mapped to it; product classification level; venue, segment, venue operator or exchange group; clearing service; channel; region; and at which of these levels must contribution be produced?

- **Why it matters:** Fixes the attribution target and roll-up; funds managed by one manager are a common source of disagreement.
- **How to answer:** Ordered list of levels used in reviews, with the default one.
- **Concepts affected:** Revenue, Contribution, Management Reporting Basis
- **Who answers:** Revenue domain owner
- **Joint question:** also covers what Instruments, venues and calendars, Service offering and market access needed to ask.
<sub>question q10</sub>

### 11. Which income streams come from client collateral (income on client cash, fees on non-cash collateral, collateral transformation, price alignment amounts not passed on), and are they reported inside clearing revenue, separately, or both? (Answered by the Collateral Manager with Business Finance.)

- **Why it matters:** Decides the content and owner of collateral revenue and whether clearing revenue may ever include it.
- **How to answer:** List of streams; reporting treatment for each; owner.
- **Concepts affected:** Collateral Revenue, Cash Collateral Interest, Clearing Revenue
- **Who answers:** Collateral Manager
<sub>question q11</sub>

### 12. For the first contribution measure, which cost categories should be deducted from revenue? Candidates: venue and CCP fees not recharged, third-party brokerage, third-party clearing, connectivity and market data, funding and collateral, default fund funding, introducer or fee-sharing payments, attributed shared cost.

- **Why it matters:** Sets the first cost perimeter (open question 10); no contribution can be stated without it.
- **How to answer:** Confirm or amend the list of categories; anything to exclude explicitly.
- **Concepts affected:** Cost Perimeter, Cost, Contribution
- **Who answers:** Revenue domain owner
<sub>question q13</sub>

## Priority 2: needed before go-live

### 13. Are CCP membership fees, default fund contributions, the cost of posting house margin, connectivity and market data costs attributed to clients, services, venues or CCPs for management reporting, or kept central? (Answered by the Revenue domain owner with the Collateral Manager.)

- **Why it matters:** Decides whether these categories can ever enter a cost perimeter and at which level.
- **How to answer:** Per category: attributed (to what) or central.
- **Concepts affected:** Cost, Cost Perimeter, Contribution
- **Who answers:** Business Finance
- **Joint question:** also covers what Margin and collateral needed to ask.
<sub>question q14</sub>

### 14. In which venue or CCP incentive programmes does the firm take part (as member or market maker)? Are the rebates netted against exchange fees, passed on to clients, or kept?

- **Why it matters:** Decides rebate presentation and whether a rebate is revenue, a cost reduction or a pass-through.
- **How to answer:** Programme types (no names needed) and treatment per type: netted, passed on, kept.
- **Concepts affected:** Fee Incentive Programme, Fee Rebate, Management Reporting Basis
- **Who answers:** Listed Execution product owner
<sub>question q15</sub>

### 15. Which client discounts, volume tiers, minimum fees, caps, waivers and client rebates do you use, and are they recorded as a reduced rate, a separate credit or a later adjustment?

- **Why it matters:** Separates discount, rebate, waiver and adjustment as recorded, so that agents do not mix them.
- **How to answer:** List of mechanisms used and how each is recorded.
- **Concepts affected:** Client Pricing Terms, Fee Rebate, Fee Adjustment
- **Who answers:** Revenue domain owner
<sub>question q16</sub>

### 16. How are clients billed: fees debited daily on the statement, monthly invoices, or both? In which currency, and which fees are invoiced rather than debited?

- **Why it matters:** Sets the billing stages and the fee invoice values an operations or revenue agent will meet.
- **How to answer:** Per service: billing method, frequency, currency rule.
- **Concepts affected:** Fee Invoice, Fee Charge, Fee Adjustment
- **Who answers:** ETD post-trade operations lead
<sub>question q17</sub>

### 17. How do you receive and check bills from venues, CCPs and other brokers: which bills combine several creditors or service natures, and who decomposes them?

- **Why it matters:** Bundled bills must be decomposed by service nature and creditor before exchange or CCP fees can be reported.
- **How to answer:** For each bill type: issuer kind, creditors included, service natures included, who decomposes.
- **Concepts affected:** Fee Invoice, Fee Collector, Exchange Fee Charge, CCP Fee Charge
- **Who answers:** Business Finance
<sub>question q18</sub>

### 18. For OTC client clearing, which fee structures do you use: per-ticket registration, periodic maintenance on open trades or notional, fixed annual packages, minimum fees? Do CCP tariff choices affect client pricing?

- **Why it matters:** Checks that client clearing fee and CCP fee cover OTC structures as well as per-lot listed fees.
- **How to answer:** List of structures used; link to CCP tariff choice yes or no.
- **Concepts affected:** Client Clearing Fee, CCP Fee Charge, Charge Basis, Client Pricing Terms
- **Who answers:** OTC Clearing product owner
<sub>question q19</sub>

### 19. For which events and services do you charge clients your own fee, beyond passing on venue, CCP and regulatory fees: give-up, give-in, position transfer, exercise, delivery, late or failed steps (including passing on CCP late give-up fees and late payment interest), exception handling, strategies versus legs, holding non-cash collateral or recharging CCP collateral fees?

- **Why it matters:** Sets the chargeable events of client fees beyond execution and clearing per lot.
- **How to answer:** List of events charged by the firm; per event: own fee, pass-through, or both.
- **Concepts affected:** Client Clearing Fee, Client Execution Fee, Pass-through Charge
- **Who answers:** ETD Clearing product owner
- **Joint question:** also covers what Margin and collateral, Post-trade operations needed to ask.
<sub>question q20</sub>

### 20. When an average price is rounded, what happens to the residual (kept by the firm, passed to the client, settled as a cash adjustment, or avoided by carrying more decimals), and is it shown in management revenue, and where? (Answered by Business Finance with the ETD post-trade operations lead.)

- **Why it matters:** Open question 4: residuals must not be mixed with fees; their treatment decides whether they appear in revenue.
- **How to answer:** One of: firm revenue or cost; client; reported separately; not tracked.
- **Concepts affected:** Revenue, Execution Revenue, Management Reporting Basis
- **Who answers:** Business Finance
- **Joint question:** also covers what Listed derivatives execution needed to ask.
<sub>question q21</sub>

### 21. In which unit and counting basis is volume reported to management (contract sides or round turns; single or double counted; executed or cleared)?

- **Why it matters:** Ensures volume-tiered rates and volume figures are read in the same unit.
- **How to answer:** Unit, counting basis and stage per report.
- **Concepts affected:** Activity Volume, Charge Basis
- **Who answers:** Revenue domain owner
<sub>question q23</sub>

### 22. Which reporting currency and conversion rule are used for management revenue and cost (daily rate, month-end rate, budget rate)?

- **Why it matters:** Currency is mandatory context; a mixed-currency total is refused without a rule.
- **How to answer:** Reporting currency per level; conversion rule.
- **Concepts affected:** Management Reporting Basis, Revenue, Cost
- **Who answers:** Business Finance
<sub>question q24</sub>

### 23. Do you share client fees with introducers or other parties, or split revenue internally between desks, regions or entities (for example revenue sharing or sales credits), and is the share shown as cost, as reduced revenue, or not at all?

<sub>question q26</sub>

### 24. Do your clearing charges differ by segregation level or account kind (omnibus, individually segregated, indirect), and where are those prices stated?

<sub>question q27</sub>
