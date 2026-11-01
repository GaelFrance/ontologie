# Instruments, venues and calendars: questions for our firm

These questions capture how **our firm** works in this domain, so the ontology can be tailored to it. The answers are firm-specific: record them in the internal workspace, **never in this repository**. Ask them in a meeting with the people named; several questions are shared with other domains and are best answered in a joint session.

## Priority 1: needed for the pilot agents

### 1. For one listed future and one listed option, which levels does your reference data hold: product family, venue contract, series, strategy, CCP contract? Which level do trading, clearing and finance each work at?

- **Why it matters:** Confirms the chain product family, contract specification, instrument and tells us whether Clearing Contract and Listed Strategy need to be first-class for the pilot.
- **How to answer:** Table: level by function (trading, clearing operations, finance), yes or no, with the usual name each team gives it.
- **Concepts affected:** Product Family, Contract Specification, Instrument, Clearing Contract, Listed Strategy
- **Who answers:** Reference & Client Data lead
<sub>question q01</sub>

### 2. Which identifiers do your teams use to recognise a listed contract and a series in each function (venue product code plus expiry, ISIN, CCP product code, a vendor symbol, an internal code)? Which one is treated as the master key?

- **Why it matters:** Sets the identifier schemes the internal layer must cross-reference and the key the agents use to match records.
- **How to answer:** List per function: scheme used, whether it is the master key, and any known gaps (for example series without ISIN).
- **Concepts affected:** Identifier Scheme, Instrument, Contract Specification
- **Who answers:** Reference & Client Data lead
<sub>question q02</sub>

### 3. Do your clients trade venue-listed strategies, are any of them user-defined, on which venues, and do your reference data hold the strategy as well as its legs?

- **Why it matters:** Decides whether Listed Strategy and Strategy Leg are needed in the pilot and at which level give-up, fees and revenue operate.
- **How to answer:** Yes or no per venue; for each function (booking, give-up, fees, reporting): strategy level or leg level.
- **Concepts affected:** Listed Strategy, Strategy Leg, Instrument
- **Who answers:** Listed Execution product owner
<sub>question q06</sub>

### 4. Which product hierarchy exists in your reference data (asset class lists, an industry taxonomy, CFI, an internal hierarchy), how many levels does it have, and who maintains it? (Which level revenue reporting uses is asked in the fees questions.)

- **Why it matters:** Determines the Product Family levels the internal layer must carry and the level at which revenue by product can be answered.
- **How to answer:** Name of the classification by function (no internal system names), number of levels, one synthetic example path.
- **Concepts affected:** Product Family, OTC Product Definition
- **Who answers:** Revenue domain owner
<sub>question q08</sub>

### 5. Which calendars do you maintain or subscribe to (venue, contract-specific, CCP, payment system per currency, your own office locations), which do you maintain yourselves, and which of them decide client deadlines, firm cut-offs and settlement deadlines?

- **Why it matters:** Seeds the calendar scopes an agent may cite and which calendar governs a cut-off by default.
- **How to answer:** Table: calendar scope, maintained or bought in, used for which processes.
- **Concepts affected:** Business Calendar, Calendar Day, Cut-off
- **Who answers:** ETD post-trade operations lead
- **Joint question:** also covers what Post-trade operations needed to ask.
<sub>question q10</sub>

### 6. For evening and overnight sessions, which business date does each use carry: books, client confirmations, client statements, operations, management revenue (venue trade date, CCP clearing date, or the booking office's local date)? Do offices in different regions use different booking dates for the same trade?

- **Why it matters:** Sets the firm-specific date role used in booking and revenue, beside the sponsor's default of the CCP clearing date for operational questions.
- **How to answer:** One choice per use (booking, client statements, management revenue), with any regional exceptions.
- **Concepts affected:** Business Date, Date Role, Trading Session
- **Who answers:** ETD post-trade operations lead
- **Joint question:** also covers what Listed derivatives execution, Post-trade operations needed to ask.
<sub>question q11</sub>

### 7. When you decide whether you can onboard a client for a contract at a CCP, at which level do you check the CCP's eligibility: product family, contract, series, or OTC product with trade-term ranges? Where is that eligibility recorded?

- **Why it matters:** Sets the grain the market onboarding agent uses and keeps CCP eligibility separate from the firm's offering.
- **How to answer:** Level by business line (listed, OTC); recorded where (by role); refresh frequency.
- **Concepts affected:** Clearing Eligibility Schedule, Contract Specification, OTC Product Definition
- **Who answers:** ETD and OTC Clearing product owners
<sub>question q18</sub>

## Priority 2: needed before go-live

### 8. Who owns instrument, venue and calendar reference data in the firm, and is there one authoritative source or one per function or region?

- **Why it matters:** Decides who approves internal-layer values for this domain and which source an agent cites when sources disagree.
- **How to answer:** Owner role per data set (instruments, venues, calendars), authoritative source by role (not system name), regional split if any.
- **Concepts affected:** Instrument, Trading Venue, Business Calendar, Identifier Scheme
- **Who answers:** Reference & Client Data lead
<sub>question q03</sub>

### 9. Do your clients use flexible or custom-terms series, and on which venues? How quickly must such a series be available in your records after the venue creates it?

- **Why it matters:** Decides whether Flexible Series needs its own rules and whether intraday creation of instruments must be handled.
- **How to answer:** Yes or no per venue; expected availability (same minute, same hour, next day).
- **Concepts affected:** Flexible Series, Instrument
- **Who answers:** ETD post-trade operations lead
<sub>question q07</sub>

### 10. For cleared OTC derivatives, at which level do your teams identify the product: the UPI, an industry taxonomy level, the CCP's product code, or an internal product type? Do you hold OTC ISINs?

- **Why it matters:** Confirms the narrowed Instrument meaning for OTC and whether OTC Product Definition is the working level for eligibility and onboarding.
- **How to answer:** Level used by function (onboarding, clearing operations, reporting); OTC ISIN use yes or no and for which purpose.
- **Concepts affected:** OTC Product Definition, Instrument, Identifier Scheme
- **Who answers:** OTC Clearing product owner
<sub>question q09</sub>

### 11. Are there days when your own offices are closed but venues and CCPs are open (or the reverse), and how are deadlines handled on those days?

- **Why it matters:** Decides whether a firm-location calendar must be combined with venue and CCP calendars when an agent states a deadline.
- **How to answer:** Yes or no; list of affected processes; handling rule in words.
- **Concepts affected:** Business Calendar, Calendar Day, Cut-off
- **Who answers:** ETD post-trade operations lead
<sub>question q13</sub>

### 12. For reference data only: do contract, series, calendar and session changes reach you through vendor files, venue and CCP notices, or both, and how quickly must they be reflected in your records?

- **Why it matters:** Defines the source and timeliness behind change-impact answers and the as-of date an agent may state for reference data.
- **How to answer:** Channel per change type (new contract, specification change, holiday, trading hours, delisting), reviewer role, target lead time.
- **Concepts affected:** Contract Specification, Business Calendar, Trading Session, Listing Status
- **Who answers:** Reference & Client Data lead
<sub>question q15</sub>

### 13. Do you trade or clear single-stock or other derivatives that are adjusted after corporate events? Who is told about an adjustment, and are adjusted series kept apart from standard series in client reporting?

- **Why it matters:** Decides whether Contract Adjustment is needed for the pilot change-impact agent and how adjusted series are identified.
- **How to answer:** Yes or no per venue; roles notified; reporting treatment in words.
- **Concepts affected:** Contract Adjustment, Instrument, Underlying
- **Who answers:** ETD Clearing product owner
<sub>question q16</sub>

### 14. Do you have contracts that are listed on more than one venue or cleared at a CCP outside the listing venue's group? If so, do you hold positions by venue contract or by CCP contract?

- **Why it matters:** Confirms the need for Clearing Contract and how positions and fees are keyed for fungible contracts.
- **How to answer:** List of cases (synthetic description acceptable); position key used; fee key used.
- **Concepts affected:** Clearing Contract, Contract Specification
- **Who answers:** ETD Clearing product owner
<sub>question q17</sub>

### 15. Which source is authoritative for daily and final settlement prices in your processes, the venue or the CCP, and what happens when a price is corrected after publication?

- **Why it matters:** Determines the publisher an agent cites for settlement prices and how corrections are treated in answers.
- **How to answer:** Source per use (margin, client statements, valuation); correction handling in words.
- **Concepts affected:** Settlement Price
- **Who answers:** ETD post-trade operations lead
<sub>question q19</sub>

### 16. What do your teams mean when they say 'product', 'contract', 'instrument' and 'exchange' in day-to-day work? Give a typical sentence for each from sales, operations and finance.

- **Why it matters:** Captures firm usage of ambiguous words so that agents ask the right clarifying question; answers stay in the internal layer.
- **How to answer:** Short sentences per team, internal terms allowed in the internal reply only.
- **Concepts affected:** Product Family, Contract Specification, Instrument, Trading Venue
- **Who answers:** Reference & Client Data lead
<sub>question q22</sub>
