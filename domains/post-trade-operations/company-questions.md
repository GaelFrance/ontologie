# Post-trade operations: questions for our firm

These questions capture how **our firm** works in this domain, so the ontology can be tailored to it. The answers are firm-specific: record them in the internal workspace, **never in this repository**. Ask them in a meeting with the people named; several questions are shared with other domains and are best answered in a joint session.

## Priority 1: needed for the pilot agents

### 1. For each CCP and venue you work with, which market cut-offs do your operations teams actually work to (give-up and take-up, allocation, exercise and abandonment, delivery notices, margin and cash settlement, position adjustments)?

- **Why it matters:** Seeds the Cut-off instances the operations agent must know, per clearing service, with their calendar and consequence.
- **How to answer:** Table: CCP or venue, process step, cut-off as published (local time and calendar, or period after an event), consequence if missed.
- **Concepts affected:** Cut-off, Settlement Deadline, Exercise Instruction, Delivery Notice
- **Who answers:** ETD post-trade operations lead
<sub>question q01</sub>

### 2. Please give one inventory of the earlier deadlines your firm sets for clients and internal teams ahead of each market cut-off (allocation, give-up, take-up, exercise and abandonment instructions, closing or rolling physically delivered positions before notice or delivery, payment): for each, the market cut-off it protects, where it is stated (client agreement, client service guide, internal procedure), what happens when it is missed, who sets and changes it, and how changes are announced to operations and clients.

- **Why it matters:** Defines the Firm Cut-off instances and whether they come from agreements or procedures, which supports the Cut-off meaning change.
- **How to answer:** Table: process step, market cut-off it protects, firm cut-off, who it binds, where stated, consequence for the client.
- **Concepts affected:** Firm Cut-off, Cut-off
- **Who answers:** ETD post-trade operations lead with Client service
- **Joint question:** also covers what Clearing: give-up and acceptance, Instruments, venues and calendars needed to ask.
<sub>question q02</sub>

### 3. For status questions on margin, cash, collateral and fees, which record does your firm treat as the reference when its own books and the CCP or another party disagree? (The default answer for positions is asked in the clearing questions.)

- **Why it matters:** Tells the agent which Source Record is authoritative per question, instead of assuming.
- **How to answer:** Table: question type, reference source (by role, e.g. CCP report, clearing back-office books, settlement bank statement), rule or policy behind it.
- **Concepts affected:** Source Record, CCP Report, Reconciliation
- **Who answers:** ETD post-trade operations lead
<sub>question q03</sub>

### 4. Which kinds of records does your firm hold for trades, positions and payments, by function (front office, middle office, clearing back office, finance), and is there a book of record for each object; if so, which?

- **Why it matters:** Lets the internal layer name the sources an answer can cite, without naming systems in the public ontology.
- **How to answer:** Table: business object, sources by function (no system names here), book of record yes or no.
- **Concepts affected:** Source Record
- **Who answers:** Head of operations data or ETD post-trade operations lead
<sub>question q04</sub>

### 5. Which reconciliations do you run (trade, give-up, position, cash, margin, collateral, fee), against whom (CCP, executing broker, other clearing broker, client, settlement bank), and how often (intraday, end of day, start of day)?

- **Why it matters:** Sets the reconciliation types and cycles the agent can report on and the counterpart record in each.
- **How to answer:** Table: reconciliation type, counterpart source, frequency and cycle, tier.
- **Concepts affected:** Reconciliation, Position Reconciliation, CCP Report
- **Who answers:** ETD post-trade operations lead
<sub>question q05</sub>

### 6. At what level do you reconcile positions with each CCP: per CCP account only, or also per client inside an omnibus account; gross long and short or net; per clearing date or per cycle?

- **Why it matters:** Fixes the key of Position Reconciliation for each account type, which differs between house, omnibus and segregated accounts.
- **How to answer:** Per account type: level (CCP account, client, sub-account), basis (gross, net), timing (date, cycle).
- **Concepts affected:** Position Reconciliation, Reconciliation Break
- **Who answers:** ETD Clearing product owner with operations
<sub>question q06</sub>

### 7. Which events automatically raise an operational exception in your process (for example a rejected or lapsed give-up, a missed cut-off, an unmatched allocation, an unpaid margin call, a failed exercise instruction, a CCP report correction)?

- **Why it matters:** Lists the triggers the agent should report as exceptions rather than as plain statuses.
- **How to answer:** List of trigger events, with the business object they are raised against.
- **Concepts affected:** Operational Exception, Exception Case
- **Who answers:** ETD post-trade operations lead
<sub>question q08</sub>

### 8. For each CCP and currency, how does your firm settle cash with the CCP: directly in the payment system or through a settlement bank, in which settlement cycles, and with one net amount per currency or separate amounts by purpose?

- **Why it matters:** Defines the Netted Settlement Obligation, Settlement Account and Settlement Deadline instances per CCP.
- **How to answer:** Table: CCP, currency, route (direct or settlement bank, by role), cycles per day, netting (net or by purpose).
- **Concepts affected:** Netted Settlement Obligation, Settlement Account, Settlement Deadline, Payment Instruction
- **Who answers:** Treasury or cash operations lead
<sub>question q10</sub>

### 9. How do clients settle with your firm: by payment, by debit or credit to their cash account in your books, or both; and are variation margin, premium, fees and interest netted on the client statement?

- **Why it matters:** Decides whether a client-tier Cash Movement is an external payment or a booking, and how client obligations are netted.
- **How to answer:** Per client type or service: settlement method, netting rule, statement frequency.
- **Concepts affected:** Cash Movement, Netted Settlement Obligation, Settlement Obligation
- **Who answers:** ETD post-trade operations lead with Client service
<sub>question q11</sub>

### 10. For listed options, how does your firm handle expiry operationally: do you rely on the CCP's automatic exercise, how do clients send exercise or contrary instructions, and how are they checked? (The deadlines are asked in the firm cut-off inventory.)

- **Why it matters:** Defines Exercise and Exercise Instruction practice and the Firm Cut-offs around expiry.
- **How to answer:** In words per CCP or product group; deadlines as stated in client documentation.
- **Concepts affected:** Exercise, Exercise Instruction, Expiry, Firm Cut-off
- **Who answers:** ETD post-trade operations lead
<sub>question q14</sub>

### 11. Which lifecycle events must an operations agent cover first: trades and give-ups, transfers, adjustments, exercise and assignment, expiry and delivery, OTC terminations and compression?

- **Why it matters:** Sets the order in which level-2 lifecycle events are completed and loaded in the internal layer.
- **How to answer:** Ranked list, with the reason for the top three.
- **Concepts affected:** Lifecycle Event, Expiry, Exercise, Assignment, Position Adjustment, Trade Amendment
- **Who answers:** ETD post-trade operations lead with OTC Clearing product owner
<sub>question q19</sub>

## Priority 2: needed before go-live

### 12. How do you classify reconciliation breaks (categories, materiality thresholds, ageing buckets), and when does a break become an exception that must be escalated?

- **Why it matters:** Decides the break values and the rule that turns a break into an Operational Exception.
- **How to answer:** List of categories; thresholds by type; ageing buckets; escalation rule in words.
- **Concepts affected:** Reconciliation Break, Operational Exception
- **Who answers:** ETD post-trade operations lead
<sub>question q07</sub>

### 13. How are exceptions handled as cases: which handling states, priority levels and target resolution times do you use, and can one case group several exceptions?

- **Why it matters:** Sets the values of Exception Case and what 'open since' and 'overdue' mean for the agent.
- **How to answer:** List of states; priority scale; target times per priority; grouping rule yes or no.
- **Concepts affected:** Exception Case
- **Who answers:** ETD post-trade operations lead
<sub>question q09</sub>

### 14. What evidence does your firm accept that a cash movement has happened and is final (payment system confirmation, settlement bank statement, CCP confirmation, internal booking)?

- **Why it matters:** Sets which source makes a Cash Movement 'settled' for the agent.
- **How to answer:** Per route: evidence type and when it arrives (same day, next day).
- **Concepts affected:** Cash Movement, Source Record
- **Who answers:** Treasury or cash operations lead
<sub>question q12</sub>

### 15. How do you define a settlement fail toward clients and toward CCPs for obligations other than margin calls, and what follows (late interest, charges, close-out rights, default procedures)?

- **Why it matters:** Fixes the Settlement Fail values and its consequences, kept apart from default handling.
- **How to answer:** In words per tier; consequences listed in order.
- **Concepts affected:** Settlement Fail, Settlement Deadline
- **Who answers:** ETD post-trade operations lead with Legal
<sub>question q13</sub>

### 16. How does your firm allocate assignments received from a CCP to its clients' short positions (random, pro rata, other), and is the method the same for every CCP and account type?

- **Why it matters:** Gives the member-to-client values of Assignment, which the firm chooses and may have to disclose.
- **How to answer:** Method per CCP and account type; where it is disclosed to clients.
- **Concepts affected:** Assignment
- **Who answers:** ETD post-trade operations lead with Compliance
<sub>question q15</sub>

### 17. Do you or your clients take or make physical delivery on any listed contracts; if not, how do you make sure positions are closed before the notice or delivery period? (The deadlines are asked in the firm cut-off inventory.)

- **Why it matters:** Decides whether Delivery Notice and physical Final Settlement are in scope for the pilot and which deadlines apply.
- **How to answer:** Yes or no per product group; if yes, delivery route by role; if no, the close-out rule and its deadline.
- **Concepts affected:** Final Settlement, Delivery Notice, Expiry
- **Who answers:** ETD post-trade operations lead
<sub>question q16</sub>

### 18. Which changes to registered trades does your firm allow (non-economic corrections of account or client reference, OTC economic changes, partial termination), and when a venue cancels or corrects a trade or a client fill must be corrected, do you cancel and rebook or amend; how are allocations and give-ups already made handled?

- **Why it matters:** Sets the Trade Amendment values and whether lineage is kept by successor trades.
- **How to answer:** List of change types with method (amend, cancel and rebook, successor trade) and approval needed.
- **Concepts affected:** Trade Amendment, Lifecycle Event
- **Who answers:** ETD post-trade operations lead with ETD Clearing product owner
- **Joint question:** also covers what Listed derivatives execution needed to ask.
<sub>question q18</sub>

## Priority 3: later

### 19. For cleared OTC trades, which lifecycle events and payments does your operations team handle (resets, coupon payments, partial terminations, compression), and are they in the first pilot scope?

- **Why it matters:** Decides whether OTC lifecycle values of Trade Amendment and OTC settlement obligations are needed now.
- **How to answer:** List of events with yes or no for the pilot.
- **Concepts affected:** Trade Amendment, Settlement Obligation, Lifecycle Event
- **Who answers:** OTC Clearing product owner
<sub>question q25</sub>
