# Supervision of the level-2 domain reviews

Date: 2026-11-01. Status: draft for the Ontology Lead and the sponsor. The detailed decisions are in `consolidation.json` in this folder.

## What was produced

Ten domain experts each reviewed their page, proposed level-2 concepts, wrote plain summaries and examples, and drafted questions about the firm. They then cross-checked each other's work for duplicates, conflicts, wrong owners, readability and confidentiality. I weighed every issue and arbitrated.

| | Proposed | After supervision |
|---|---|---|
| Level-2 concepts | 170 | 143 accepted, 4 merged, 23 turned into values; 5 supervisor additions. Total: 148 |
| Level-1 reviews | 70 clarify or change | 57 clarifications accepted, 13 meaning changes sent to the sponsor |
| Company questions | 232 | 183 kept or reworded (8 new), 57 merged into joint questions |

Each domain now has 12 to 18 level-2 concepts, as the brief asked.

## Main arbitration choices

**One owner and one name for each concept.**
- The trades created by clearing belong to the clearing services and accounts page. The client-side trade is called **Client Back-to-Back Trade**, because the name also fits the tier between a client and its indirect client. "Member-client trade" stays as an alias.
- **Cash Collateral Interest** belongs to the margin page. The fees page keeps Collateral Revenue and refers to it.

**One rule for trade identity.** These events end a CCP-facing trade and create a linked successor: a give-up registration, a transfer, porting, an economic change, compression and close-out. Only a correction that changes no economic term is recorded on the same trade.

**Corrections are split by origin, not by time.**
- An Execution Correction comes from the venue's error-trade rules or the broker's correction to its client, even after clearing.
- A Trade Amendment is made under the clearing service's rules or by agreement of the parties.
- A move to another account or clearing member is a Position Transfer or a give-up step.

**Roles are roles.**
- Giving, receiving, back-up and sponsoring clearing members become kinds of Party Role, held toward identified parties. A firm can be giving on one line and receiving on the next.
- Margin Provider and Margin Taker follow from the clearing roles at a tier.
- The parties page will show one "all roles" table.

**Statuses are values, not concepts.**
- Order, give-up, margin call, access, listing and client relationship statuses become value lists on their objects. A named source record asserts each status, and the source's own status is kept beside it.
- Settlement Fail stays a concept: each fail has its own amount, age and ending.
- A margin call is a demand, not a settlement obligation, so an unmet cash call is counted once.

**Earlier decisions are respected.** Clearing Tier, Execution Method, Date Role, Trading Capacity, Membership Category, Service Kind and Client Clearing Legal Model are already lists of values. They are not proposed again as concepts. The values the experts asked for are added to those lists instead.

**Supervisor additions** for gaps several pages needed but no page proposed:
- **Processing Window**: a named period of a clearing day.
- **Market Operator**: the company that runs a venue.
- **Settlement or Custody Agent**: settlement bank, custodian or triparty agent.
- **Regulatory Reporting Role**: for example the executing entity named in a transaction report.
- **Client Default**: a broker declares its own client in default.

**Other placements.**
- **Clearing Limit** has one owner, the give-up page. It applies before execution and at acceptance. It is not a rule provision.
- **Identifier Scheme** covers party, account, order, execution and give-up codes. The Legal Entity Identifier becomes one of its values.
- **Position Adjustment** moves next to Position Transfer.
- Positions are keyed by the series of the clearing contract.
- Revenue "per service" means the firm's Service Offering, not the CCP's clearing service.

## What was rejected

These 23 proposals became values, because none had an identity or rules beyond its parent:
- the six statuses and the seven value lists above;
- Clearing Novation, Average Pricing Method, Clearing Designation, Charge Basis, OTC Product Definition, Calendar Day;
- Margin Add-on, Intraday Margin Call, Give-up Rejection Reason, Legal Entity Identifier.

Strategy Leg merged into Listed Strategy. Portfolio Compression, OTC block allocation and bilateral step-in or step-out stay in the backlog, because they are outside the listed pilot.

## Cross-domain conflicts on questions

The same people were being asked the same thing on up to six pages. Each topic below is now one joint question, owned by the page in brackets:
- legal-entity matrix (parties)
- access-route table (service offering)
- indirect, sponsored and non-clearing-member clearing (service offering)
- account levels and mapping (clearing services)
- firm cut-off inventory (post-trade)
- dates for evening and overnight sessions (instruments)
- intake of published changes (regulation)
- "as known at" history (regulation)
- Asia-Pacific scoping (regulation)
- events the firm charges for (fees)
- revenue dimensions (fees)

The eight new questions cover:
- the clearing brokers and give-up references recorded for each client
- margin on give-ups not yet taken up
- OTC trades executed elsewhere
- active-account demand
- the regulatory basis for serving clients abroad
- fee sharing
- pricing by segregation level
- client default

## Quality concerns

- **IDs in text.** Definitions contained concept IDs; they are removed. Overview pages and question rationales still cite agent and evaluation IDs and must be rewritten in words.
- **Blocked word.** "Transaction" is blocked as ambiguous; it is replaced by "trade" in definitions.
- **Types.** "Amount" and "Status" are not catalogue types. They are retyped as Obligation, Measure or State.
- **Statements about the firm.** Some examples and questions stated facts about the firm ("the firm is a member…", "another part of the bank"). They now use synthetic parties or neutral wording.
- **Practice stated as fact.** Two overview statements need rewording when the pages are regenerated: "a missed call is a default event" and "at most European CCPs…".
- **Regime-specific rules.** Some rules were written as if universal: segregation election, excess collateral, the clearing obligation and client margin minimums. They are now marked per regime and "to verify".
- **Generator bug.** The page generator shows only the first kind of a concept, so it hides Clearing Revenue and Collateral Revenue.
- **Early promotions.** Some backlog items were promoted before their trigger was met. They are flagged for the sponsor.

## Points only the sponsor can decide

1. **Meaning changes.** Approve or reject the 13 level-1 meaning changes:
   - Party, Broker, Trading Venue, Allocation, Allocation Instruction, Position, Commission
   - Variation Margin Requirement, Market Access Arrangement, Rule Change, Cut-off, Regulatory Classification, CCP Account

   Three new deadline concepts (Settlement Deadline, Firm Cut-off, Take-up Deadline) depend on the Cut-off change. Standing Allocation Instruction depends on the Allocation Instruction change.
2. **Cut-off.** Should a cut-off be "set by" either a rule or an agreement term, instead of always being a rule (recommended)? Decide with Regulatory Affairs.
3. **Third-party execution.** Should it also cover a member that does not use its own membership? Today it does not, in line with decision 3.
4. **Backlog triggers.** Waive or keep them for Cash Collateral Interest and for the seven new level-1 concepts.
5. **Late charges.** Should Fee Charge widen to cover late and penalty charges? This would be a meaning change.
6. **OTC execution on venues.** Extend the execution page to cover it later, or exclude it from the listed pilot.
7. **Joint sessions.** Confirm that the merged company questions will be answered in joint sessions.
