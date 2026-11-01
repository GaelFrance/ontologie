# Listed derivatives execution: questions for our firm

These questions capture how **our firm** works in this domain, so the ontology can be tailored to it. The answers are firm-specific: record them in the internal workspace, **never in this repository**. Ask them in a meeting with the people named; several questions are shared with other domains and are best answered in a joint session.

## Priority 1: needed for the pilot agents

### 1. Which handling channels do you offer for listed derivatives, per service kind, region and venue, and are there any beyond care, broker algorithm, direct market access and sponsored access? Is sponsored access offered at all?

- **Why it matters:** Sets the values of the handling channel used for revenue per channel; a channel outside the four would be a meaning change.
- **How to answer:** Table: channel name used internally, short description, regions and venues where offered.
- **Concepts affected:** Order Handling Channel, Client Order, Execution Revenue
- **Who answers:** Listed Execution product owner
- **Joint question:** also covers what Service offering and market access needed to ask.
<sub>question q01</sub>

### 2. When an order changes channel while it is worked (for example care passed to an algorithm), which channel does revenue use: the channel at receipt, the last channel, or a split by quantity executed in each? (Answered with the Revenue domain owner.)

- **Why it matters:** Decides whether channel is held on the client order or on each child order and execution for revenue attribution.
- **How to answer:** One of: at receipt / last / split by quantity / other (describe).
- **Concepts affected:** Order Handling Channel, Client Order, Child Order, Execution Revenue
- **Who answers:** Revenue domain owner with Listed Execution product owner
- **Joint question:** also covers what Fees, revenue and contribution needed to ask.
<sub>question q02</sub>

### 3. Which records do your desk, middle office and operations teams call 'order', 'fill', 'execution' and 'trade'?

- **Why it matters:** Feeds the internal alias table so that agents resolve each team's words to venue execution, client execution, executed trade or allocation line.
- **How to answer:** Table: team, word used, which record it means (client order, child order, venue fill, client fill, allocation line, CCP trade).
- **Concepts affected:** Client Order, Child Order, Venue Execution, Client Execution, Executed Trade, Allocation Line
- **Who answers:** Listed Execution product owner with ETD post-trade operations lead
<sub>question q03</sub>

### 4. Who performs average pricing for your clients on each venue or CCP: the venue or CCP facility, your own systems, or both, and for which client segments?

- **Why it matters:** Decides which records carry the average price (CCP record or client-facing only) and therefore what the give-up agent and revenue agent see.
- **How to answer:** Table: venue or CCP, averaging performer, client segments eligible.
- **Concepts affected:** Average Price Group, Average Pricing Method, Client Execution
- **Who answers:** ETD post-trade operations lead
<sub>question q09</sub>

### 5. Which forms of allocation instruction do you accept: standing instructions, designation on the order, instructions after execution; and through which means (electronic message, allocation platform, other)?

- **Why it matters:** Confirms the proposed meaning change to include standing instructions and sets which kinds of allocation instruction are needed.
- **How to answer:** Checklist of forms accepted, with the means used for each.
- **Concepts affected:** Allocation Instruction, Standing Allocation Instruction, Clearing Designation
- **Who answers:** ETD post-trade operations lead
<sub>question q11</sub>

### 6. When a client misses your allocation deadline, what happens: a default account, the give-up is refused, a late give-up, or a charge? (The deadlines themselves are asked in the firm cut-off inventory.)

- **Why it matters:** Gives the firm cut-off and its consequence that the give-up agent must state beside the public cut-off.
- **How to answer:** Per CCP or venue: firm deadline relative to the public cut-off, consequence of missing it.
- **Concepts affected:** Allocation Instruction, Allocation Line, Cut-off
- **Who answers:** ETD post-trade operations lead
<sub>question q13</sub>

### 7. For a give-up to another clearing broker, at which step does the execution desk hand over to clearing operations, and which team owns each later step (give-up submission, take-up, rejection follow-up, agreement set-up)?

- **Why it matters:** Fixes the boundary between this page and the give-up page and who an agent should name as owner of a lapsed trade.
- **How to answer:** Name of the hand-over step and owning role for each outcome (rejected, lapsed, partially taken up).
- **Concepts affected:** Allocation Line, Clearing Designation, Give-up / Take-up Process
- **Who answers:** Listed Execution product owner with ETD Clearing product owner
- **Joint question:** also covers what Clearing: give-up and acceptance needed to ask.
<sub>question q15</sub>

## Priority 2: needed before go-live

### 8. Which negotiated trade types do you arrange (block trades, exchanges for physical, for swap, options for options, other venue types), on which venues, and who negotiates them (desk, client directly, both)?

- **Why it matters:** Sets which execution method values and kinds are needed for the pilot and which venue rule changes the change-impact agent must watch.
- **How to answer:** Table: venue, negotiated trade type, offered yes or no, negotiated by.
- **Concepts affected:** Execution Method, Block Trade, Exchange for Related Position
- **Who answers:** Listed Execution product owner
<sub>question q07</sub>

### 9. At which level do you allocate (each venue execution, each client execution, each average price group or the whole order), are partial allocations allowed before the order is complete, and at which unit do your teams track give-up progress (allocation line, give-up line, trade)?

- **Why it matters:** Decides what an allocation line points to and how lineage from fill to give-up is recorded.
- **How to answer:** One of the levels per channel or client type; partial allocation yes or no.
- **Concepts affected:** Allocation, Allocation Line, Average Price Group
- **Who answers:** ETD post-trade operations lead
- **Joint question:** also covers what Clearing: give-up and acceptance needed to ask.
<sub>question q14</sub>

### 10. When clients trade listed strategies, do you allocate, give up and report per leg or per strategy; do block trades, exchanges for related positions and strategy legs follow the same give-up steps and deadlines as on-book executions; and does this differ by venue?

- **Why it matters:** Decides whether allocation lines point to strategy leg executions.
- **How to answer:** Per leg / per strategy / depends (by venue).
- **Concepts affected:** Strategy Leg Execution, Allocation Line
- **Who answers:** ETD post-trade operations lead
- **Joint question:** also covers what Clearing: give-up and acceptance needed to ask.
<sub>question q16</sub>

### 11. Which pre-trade controls apply to each channel, and who sets each limit (execution desk, clearing credit risk, Compliance)?

- **Why it matters:** Sets who owns the pre-trade control check and links rule changes on direct electronic access to the right control.
- **How to answer:** Table: channel, control kind, who sets the limit.
- **Concepts affected:** Pre-trade Control Check, Order Handling Channel, Order Status
- **Who answers:** Compliance with Listed Execution product owner
<sub>question q17</sub>

### 12. Is the handling channel recorded on each client order and child order in your records today, and is the client's own use of an algorithm recorded separately?

- **Why it matters:** Tells whether revenue per channel can be answered from records or needs a derivation rule later.
- **How to answer:** Yes, partly or no for each of: channel on client order, channel on child order, client algorithm flag.
- **Concepts affected:** Order Handling Channel, Client Order, Child Order
- **Who answers:** Listed Execution product owner
<sub>question q21</sub>

## Priority 3: later

### 13. For exchanges for related positions, does the firm also provide the related position (cash bond, OTC swap, OTC option), and from which business?

- **Why it matters:** Decides whether the related leg must be linked to another domain's trade and which owner reviews it.
- **How to answer:** Per related-position type: provided by the firm yes or no, business that provides it (generic).
- **Concepts affected:** Exchange for Related Position, Trade
- **Who answers:** Listed Execution product owner
<sub>question q08</sub>

### 14. Do you cross or match client orders against each other or against the firm on a venue (cross or committed orders), and how are those executions recorded?

- **Why it matters:** Decides whether the cross value of execution method is needed and how capacity is shown on each side.
- **How to answer:** Yes or no per venue; capacity on each side; method name used.
- **Concepts affected:** Execution Method, Venue Execution, Trading Capacity
- **Who answers:** Listed Execution product owner with Compliance
<sub>question q20</sub>

### 15. Which order statuses must be shown to clients or operations, and do you use any status beyond working, partly filled, filled, cancelled, rejected and expired?

- **Why it matters:** Sets the values of order status that the operations agent must recognise.
- **How to answer:** List of status names with a one-line meaning each.
- **Concepts affected:** Order Status
- **Who answers:** ETD post-trade operations lead
<sub>question q22</sub>
