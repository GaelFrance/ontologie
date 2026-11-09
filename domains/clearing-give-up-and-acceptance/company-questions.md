# Clearing: give-up and acceptance: questions for our firm

These questions capture how **our firm** works in this domain, so the ontology can be tailored to it. The answers are firm-specific: record them in the internal workspace, **never in this repository**. Ask them in a meeting with the people named; several questions are shared with other domains and are best answered in a joint session.

## Priority 1: needed for the pilot agents

### 1. On which markets is the receiving clearing member designated at order entry so the CCP registers trades straight to it, and on which is the trade registered first to the executing side and given up later?

- **Why it matters:** Decides which kind of give-up applies per market, and who holds the obligation between execution and acceptance.
- **How to answer:** Per market: at registration, after registration, both.
- **Concepts affected:** Give-up at Registration, Give-up after Registration
- **Who answers:** ETD post-trade operations lead
<sub>question q03</sub>

### 2. As receiving member, how does your firm take up give-ins at each CCP: manual claim, automatic claim by rule, automatic within a clearing limit, or a mix?

- **Why it matters:** Fixes the values of Take-up used internally and whether member acceptance and registration times will differ.
- **How to answer:** Per CCP: manual, automatic by rule, automatic within limit; share of each if known.
- **Concepts affected:** Take-up, Clearing Limit, Clearing Member Acceptance
- **Who answers:** ETD post-trade operations lead
<sub>question q04</sub>

### 3. Where are give-ups claimed: in each CCP's own system, on an exchange front end, or through a third-party give-up facility?

- **Why it matters:** If acceptance happens outside the CCP, the member acceptance time and the CCP registration time differ and both must be kept (decision 5).
- **How to answer:** Per CCP: facility type (CCP, exchange, third party); no system names needed.
- **Concepts affected:** Take-up, Give-up Registration
- **Who answers:** ETD post-trade operations lead
<sub>question q05</sub>

### 4. Who sets clearing limits for give-in clients and executing brokers, at what level (client, account, executing broker, product), on what basis, and how is a breach handled? Do you restrict which executing brokers may give trades in to you, per client, per venue or firm-wide?

- **Why it matters:** Gives Clearing Limit its scope and basis values and tells agents when automatic acceptance applies.
- **How to answer:** Short description per level; basis (lots, notional, risk); breach route (refer, reject).
- **Concepts affected:** Clearing Limit, Take-up, Submission Acceptance
- **Who answers:** Head of clearing risk or credit
- **Joint question:** also covers what Service offering and market access needed to ask.
<sub>question q06</sub>

### 5. Which give-up statuses do your teams use day to day, and how do they map to the receiving member's decision (pending, accepted in full, accepted in part, rejected, lapsed, unknown) and to the CCP registration status (not registered, registered in part, registered in full, reversed), plus cancelled?

- **Why it matters:** Builds the mapping from native statuses to the harmonised values, kept in the internal layer.
- **How to answer:** Two-column table: your status name, harmonised value (or 'no equivalent').
- **Concepts affected:** Give-up Status
- **Who answers:** ETD post-trade operations lead
<sub>question q08</sub>

### 6. For each reference CCP, does Legal hold a confirmed view of the interposition mechanism and its legal moment, and which timestamp does your firm use as 'cleared' in client and internal reporting?

- **Why it matters:** Separates the legal moment from the message time for each clearing service; agents must state which one they use.
- **How to answer:** Per CCP: mechanism, moment, confirmed (yes or no); timestamp used.
- **Concepts affected:** CCP Interposition, Clearing Novation, Clearing Acceptance
- **Who answers:** Legal
<sub>question q20</sub>

### 7. When a give-up line has been taken up but the CCP has not yet registered it, how long does that gap usually last at each CCP, and do your internal records show the line as accepted or as complete meanwhile?

- **Why it matters:** The ontology keeps the receiving member's decision and the CCP registration as two statuses (decision 5); agents must know when they diverge and which one internal screens show.
- **How to answer:** Per CCP: usual delay between take-up and registration; status shown internally during that gap.
- **Concepts affected:** Give-up Line, Take-up, Give-up Registration
- **Who answers:** ETD post-trade operations lead
<sub>question q23</sub>

### 8. When a CCP reverses or corrects a give-up registration, how does your firm learn of it, and which record is then treated as current?

- **Why it matters:** The registered quantity counts only valid CCP records, net of reversals and corrections; agents must not count a corrected registration twice.
- **How to answer:** Per CCP: how reversals and corrections reach you; which record wins; how often it happens.
- **Concepts affected:** Give-up Line, Give-up Registration
- **Who answers:** ETD post-trade operations lead
<sub>question q24</sub>

### 9. When only part of a give-up line is taken up, what happens to the remaining quantity: does it stay with the giving member, is a new line sent, or is it handled as a break?

- **Why it matters:** Fixes the values of the remaining-quantity disposition on the give-up line.
- **How to answer:** Per CCP or per giving side: the usual handling and who decides it.
- **Concepts affected:** Give-up Line, Giving Clearing Member
- **Who answers:** ETD post-trade operations lead
<sub>question q25</sub>

## Priority 2: needed before go-live

### 10. Does your firm ever accept only part of a give-up line, and under what conditions?

- **Why it matters:** Decides whether 'accepted in part' is a live value for the firm and how partial completion is reported.
- **How to answer:** Yes or no per CCP; typical conditions.
- **Concepts affected:** Give-up Status, Take-up
- **Who answers:** ETD post-trade operations lead
<sub>question q09</sub>

### 11. Which reasons does your firm record when it rejects a give-in or a clearing submission, and are they standardised across markets?

- **Why it matters:** Seeds the firm's mapping to the Give-up Rejection Reason values and supports failure analysis.
- **How to answer:** List of reasons in use; whether one list or per market.
- **Concepts affected:** Give-up Rejection Reason
- **Who answers:** ETD post-trade operations lead
<sub>question q10</sub>

### 12. As giving side, when a give-up is rejected or lapses, what does your firm normally do: re-submit, late give-up, position transfer, close-out with cost recovery, or keep the position for the client?

- **Why it matters:** Describes the firm's resolution paths after failure, which an evaluation question asks about, without putting firm practice in definitions.
- **How to answer:** Ranked list of paths with the role that decides.
- **Concepts affected:** Give-up after Registration, Give-up Status, Operational Exception
- **Who answers:** ETD Clearing product owner
<sub>question q12</sub>

### 13. As receiving side, what does your firm do with a give-in it cannot accept by the deadline: reject explicitly, let it lapse, or take it up and correct later?

- **Why it matters:** Tells agents whether a lapse at the firm is a choice or an accident, and how status should be read.
- **How to answer:** Choice per situation (no agreement, limit breach, unknown account).
- **Concepts affected:** Take-up, Give-up Status, Give-up Rejection Reason
- **Who answers:** ETD post-trade operations lead
<sub>question q13</sub>

### 14. Does your firm sign give-up agreements on the industry standard form, on bespoke terms, or both, and are they managed on an electronic agreement platform?

- **Why it matters:** Tells whether Give-up Agreement terms can be read from a standard template and how agreement coverage can be checked.
- **How to answer:** Share standard versus bespoke; platform used (yes or no, no names needed).
- **Concepts affected:** Give-up Agreement
- **Who answers:** Legal
<sub>question q14</sub>

### 15. Do your give-up agreements usually set acceptance limits, and do they say who bears a trade the clearing broker does not take up?

- **Why it matters:** Checks the proposed clarification that the agreement permits but does not oblige acceptance, and how responsibility is allocated.
- **How to answer:** Yes, no or varies, for each of: limits, responsibility for trades not taken up.
- **Concepts affected:** Give-up Agreement, Clearing Limit
- **Who answers:** Legal
<sub>question q15</sub>

### 16. When trades are average-priced, are give-ups made at the average price through a venue or CCP facility, and does this vary by CCP? (Who performs the averaging is asked in the execution questions.)

- **Why it matters:** Tells agents which records a give-up concerns when averaging is involved (an evaluation question).
- **How to answer:** Per CCP: facility, broker, both.
- **Concepts affected:** Give-up Line, Average Price Group
- **Who answers:** ETD post-trade operations lead
<sub>question q16</sub>

### 17. For OTC trades cleared at LCH SwapClear or other OTC CCPs, does your firm act as clearing broker, executing dealer, or both, and how is its consent to a clearing submission given?

- **Why it matters:** Fixes the OTC roles the ontology must support and the values of Submission Acceptance.
- **How to answer:** Per CCP: roles; consent manual, automatic within limit, or mixed.
- **Concepts affected:** Clearing Submission, Submission Acceptance, Clearing Limit
- **Who answers:** OTC Clearing product owner
<sub>question q18</sub>

### 18. Under the principal-to-principal model, does your firm keep the client back-to-back trade as its own record with its own identifier, separate from the CCP-facing trade?

- **Why it matters:** Decides whether agents can answer questions at the member-client tier or only at the CCP-facing tier.
- **How to answer:** Yes or no per regime; how the two are linked.
- **Concepts affected:** Member-Client Trade, CCP-facing Trade
- **Who answers:** OTC Clearing product owner
<sub>question q21</sub>

### 19. In markets where you clear through another clearing member, do you still accept give-ins or clearing submissions as clearing broker for your clients?

- **Why it matters:** Tells whether the receiving clearing member and the clearing broker can differ for the firm, which affects who decides acceptance.
- **How to answer:** Per market: yes or no; the receiving member's relationship to the firm.
- **Concepts affected:** Receiving Clearing Member, Clearing Member Acceptance
- **Who answers:** ETD Clearing product owner
<sub>question q22</sub>

## Priority 3: later

### 20. Does your firm also perform OTC or FX prime-brokerage 'give-ups', and are they handled by the same teams or systems as listed give-ups?

- **Why it matters:** Prevents agents from mixing prime-brokerage give-up with the listed process; decides whether a separate concept is needed later.
- **How to answer:** Yes or no; same team or different team.
- **Concepts affected:** Give-up / Take-up Process
- **Who answers:** OTC Clearing product owner
<sub>question q19</sub>
