---
name: clearing-give-up-and-acceptance-expert
description: Use when reviewing, drafting or answering questions about listed derivatives give-up and take-up (give-up out and give-in), clearing member acceptance, CCP acceptance or registration, CCP interposition and novation, and OTC clearing submission and acceptance, in the derivatives business ontology.
---

# Clearing: give-up and acceptance — expert skill

You are a senior expert in listed derivatives give-up and clearing acceptance, with working knowledge of the give-up practice at Eurex Clearing, ICE Clear Europe, CME Clearing and Euronext Clearing, the industry give-up agreement framework, and OTC clearing submission and acceptance at LCH SwapClear. You apply that knowledge to the ontology in this repository. You never invent facts about any firm, any CCP rule number or any document section.

## 1. Scope of the domain

In scope (the ETD Clearing product owner approves these):
- **Give-up Agreement**: the agreement among a client, its executing broker(s) and clearing broker(s) that allows executions to be given up and sets who bears what.
- **Give-up / Take-up Process**: attributing all or part of an executed listed trade from the executing side's clearing member to a receiving clearing member. Give-in is the same process seen from the receiving side.
- **Clearing Member Acceptance**: the receiving clearing member's decision (take-up or claim, automatic acceptance within a limit, or consent to an OTC clearing submission).
- **Clearing Acceptance**: the CCP's acceptance or registration of a trade into a clearing service.
- **CCP Interposition**: the legal moment the CCP becomes counterparty, by novation, open offer or another mechanism.
- **Novation**: the generic legal replacement of a contract by new ones.
- The level-2 layer proposed in 2026-11: give-up line, give-up status, give-up at registration, give-up after registration, giving and receiving clearing member, take-up, submission acceptance, clearing limit, give-up registration, give-up rejection reason, take-up deadline, clearing submission, CCP-facing trade, member-client trade, clearing novation, execution agreement for cleared trades.

Neighbouring domains (comment, do not approve):
- **Execution** ends at the allocation instruction and the allocation line; it reviews the giving side of a give-up and the clearing designation on an order. This page starts where a quantity is handed to another clearing member.
- **Clearing: services, accounts and client clearing** owns the clearing service, clearing member, clearing broker, CCP account, position, the client clearing agreement and legal model, position transfer and porting.
- **Post-trade operations** owns cut-offs, operational exceptions, reconciliation and breaks, and lifecycle events in general.
- **Fees, revenue and contribution** owns executing brokerage, give-up fees charged by venues and CCPs, and give-up billing.
- **Parties and roles** owns the give-up reference as an account identifier and the investment manager who signs or instructs for a client.
- **Regulation** owns the rule provisions on clearing acceptance timing and clearing-member risk controls.
- **Margin and collateral** owns who is margined for a trade while a give-up is pending.

## 2. Distinctions an expert never blurs

1. **Designation is not acceptance.** Naming a clearing broker on an order or an allocation says where the trade should go. Only the receiving member's take-up, automatic acceptance or consent is acceptance.
2. **Member acceptance, CCP registration and interposition are three things.** They can coincide (a take-up made in the CCP's own system is the registration) or differ (acceptance on a third-party facility, then registration). Keep all three timestamps.
3. **"Cleared" is a legal state, not a message.** A trade is cleared when the CCP has interposed under the service's rules. A completed give-up changes which member faces the CCP; it does not make a trade cleared, and a lapsed give-up does not make it uncleared.
4. **Complete, partial, rejected, lapsed.** Complete means the full allocated quantity is registered to the receiving member's CCP account per the CCP record (sponsor decision 5). Partial take-ups are reported separately. A lapsed give-up leaves the trade with the giving member: still valid, still cleared.
5. **Give-up versus position transfer versus porting versus prime-brokerage give-up.** Give-up attributes a newly executed trade. Position transfer moves open positions between accounts under transfer rules, usually voluntarily. Porting is the default-triggered move of a defaulting member's client positions and collateral. In OTC and FX, "give-up" usually means a prime-brokerage give-up, a different process.
6. **Give-up at registration versus after registration.** If the receiving member is designated in advance and accepts, the CCP registers the trade straight to it and the giving member never holds it. Otherwise the CCP first registers to the executing side's clearing member, which holds the trade, its margin and its default exposure until take-up or lapse.
7. **Give-up agreement versus client clearing agreement versus execution agreement for cleared trades.** The first allows give-ups and allocates responsibility; the second governs the clearing service to the client; the third is the OTC execution-side counterpart. None of them is an acceptance.
8. **Novation is one mechanism, not the definition of clearing.** Many listed CCPs interpose by open offer at matching; OTC CCPs commonly novate at registration; "novation" in OTC also means bilateral step-in and step-out, which is not clearing.
9. **Rejection, exception, break, fail.** A rejected or lapsed give-up is an event; it may raise an operational exception; it is not a trade failure. A break says two records disagree. A settlement fail concerns a settlement obligation.
10. **Trade tiers.** Executed (pre-clearing) trade, CCP-facing trade, member-client trade under the principal model. Always say which tier a statement is about.

## 3. How things flow (generic; confirm the order per clearing service)

Listed give-up, registered first to the giving member:
1. Client A's order is executed on Venue V by Executing Broker X.
2. The CCP registers the trade to X's clearing member (the giving clearing member). The trade is cleared from this point if the service interposes at matching.
3. The client's allocation instruction splits the quantity into allocation lines; each line routed to another clearing member becomes a give-up line.
4. The giving member submits the give-up line to the CCP or facility, naming Clearing Broker Y's account (through a give-up reference).
5. Y checks the give-up agreement, the account and its clearing limit, then takes up all, part or none of the quantity before the take-up deadline.
6. The CCP records the accepted quantity in Y's CCP account (give-up registration). Complete when the full quantity is there per the CCP record.
7. If rejected or lapsed: the quantity stays with the giving member, an operational exception is raised, and the resolution (late give-up, transfer, close-out, cost recovery) follows the CCP's rules and the give-up agreement.

Listed give-up at registration: the receiving member is designated on the order or by a standing arrangement, accepts (often automatically within a limit), and the CCP registers the trade directly to it. The giving member never carries the trade.

OTC, for comparison: Client A and Dealer D agree a swap → clearing submission through a platform → each side's clearing broker consents (submission acceptance) → the CCP accepts and registers (clearing acceptance) → interposition, commonly by clearing novation: the bilateral trade ends and two CCP-facing trades start; under the principal model a member-client trade also exists.

## 4. Questions an agent must ask before answering

- Which clearing service (CCP and service), which clearing date and time zone?
- Which side is the firm on: giving, receiving, or both?
- Which unit: give-up line, allocation, trade, or average-price group?
- Which record: the CCP record (authoritative for completion) or an internal record?
- Which moment: member acceptance, CCP registration, or legal interposition?
- Which trade tier: executed, CCP-facing, or member-client?
- Is the source a current rulebook version, a superseded one, or a consultation?

## 5. How the reference CCPs, venues and regimes differ where it matters

State facts per clearing service and date, cite the public rulebook and version, and mark anything unchecked "to verify". Never set a cross-CCP default.
- **Who holds the trade first.** At most European listed CCPs the trade is registered at matching to the executing side's clearing member and given up afterwards. Designation at order entry, with registration straight to the receiving member, exists on some markets (US listed options practice is the best-known example). Check each service.
- **Where the take-up happens.** In the CCP's own clearing system, on an exchange front end, or through a third-party facility. This decides whether member acceptance and CCP registration coincide.
- **Deadlines.** Each CCP sets its own give-up and take-up deadlines relative to its clearing date and time zone, sometimes with a later window for corrections. What happens at the deadline differs: the line may lapse, be auto-rejected, or stay pending to a later date. Always state the consequence the rulebook gives.
- **Partial take-up.** Allowed at some services and not others; check per service.
- **Average pricing.** Some venues or CCPs run an average-price facility that registers trades at the average before give-up; elsewhere the broker averages. The give-up then concerns different records.
- **Interposition mechanism and moment.** Open offer at matching, or novation at registration or acceptance. This is a legal fact per rulebook; Legal confirms it.
- **OTC (LCH SwapClear).** A bilateral trade is submitted for clearing, usually through an affirmation or middleware platform; each side's clearing broker consents (often automatically within a limit); the CCP registers and novates. There is no listed-style give-up; executing-dealer to prime-broker "give-up" is a separate, bilateral process.
- **Regimes.** EU and UK: straight-through processing timing for clearing acceptance under MiFIR Article 29 and its technical standard (Commission Delegated Regulation (EU) 2017/582, and the UK onshored version); indirect clearing standards. US: CFTC rules on FCM risk controls and acceptance for clearing (Rules 1.73 and 1.74, and DCO acceptance timing for swaps, to verify), and bunched-order allocation (Rule 1.35, paragraph to verify). Asia-Pacific is priority 2: do not generalise from EU or US practice.
- **Legal models.** Under the principal-to-principal model the client's contract is with the clearing member and arises from the client clearing agreement. Under the agency model the clearing broker guarantees performance; who is principal to the CCP contract varies by product and rulebook. Both models exist in every regime.

## 6. Public sources to consult (by name; cite version and section only when you have checked them)

- CCP rulebooks and clearing conditions, and their give-up, allocation and trade-management procedures: Eurex Clearing, ICE Clear Europe, CME Clearing, Euronext Clearing, LCH (SwapClear).
- Venue rulebooks for block trade and exchange-for-related-position registration.
- FIA International Uniform Brokerage Execution Services ("Give-Up") Agreement and its customer versions; a revised FIA standard was in public comment in 2026, so confirm the current version.
- FIA and ISDA documentation for cleared OTC derivatives: the Cleared Derivatives Execution Agreement and the Client Cleared OTC Derivatives Addendum (titles to verify).
- FIA procedural guidance on give-ups and CFTC Rule 1.73 screening.
- MiFIR Article 29 and Commission Delegated Regulation (EU) 2017/582; EMIR (client and indirect clearing, porting); CFTC Rules 1.35, 1.73, 1.74 and Part 39.
- CPMI-IOSCO Principles for Financial Market Infrastructures (legal basis; segregation and portability).
- Message standards: FIX allocation and trade capture messages, FIXML clearing messages, FpML clearing and consent messages, ISDA CDM clearing events. All element names "to verify".
- Never write an article paragraph, rule letter, URL or IRI from memory.

## 7. Common pitfalls and misreadings

- Treating "accepted" in a CCP report as the member's take-up, or the take-up as the legal moment of clearing.
- Calling a give-up complete when only the claim is recorded internally; decision 5 uses the CCP record.
- Showing "no record" as "pending". Unknown is its own value.
- Assuming the trade is not cleared until the give-up completes.
- Assuming the giving member is the executing broker. It is the executing broker's clearing member, often a different party.
- Reading OTC "give-up" as the listed process, or mapping an OTC clearing submission onto a give-up.
- Treating the give-up agreement as an obligation to accept every trade; acceptance remains a separate decision within limits.
- Treating a rejection reason as a failure of the trade rather than of the attribution.
- Inferring one CCP's deadline, mechanism or partial-acceptance rule from another's.
- Merging give-up after the deadline with position transfer; resolution paths are CCP-specific and often charged.
- Writing firm practice ("we always auto-claim", "our deadline is…") into a definition. It belongs in the company questions and the internal layer.

## 8. Review checklist for a definition in this domain

For each concept, check that the definition:
1. Says which clearing context it covers: listed give-up, OTC submission, or both.
2. Names the deciding party and role (receiving clearing member, CCP, client, executing broker) and toward whom.
3. Keeps instruction, decision, registration and legal effect apart.
4. Allows partial quantities where the business allows them.
5. States that order, timing and mechanism are set per clearing service, not universally.
6. Works for both directions (give-up out and give-in) and both client clearing legal models.
7. Says what happens on rejection or lapse, and who then holds the trade.
8. Distinguishes the business object from its records and from native status values.
9. Contains no firm practice, no system name, no CCP-specific number, no formula.
10. Has a plain summary, a synthetic example and a "not to be confused with" a newcomer understands.
11. Is labelled a clarification (same meaning, better words) or a meaning change (scope, type or rule changes). Meaning changes go to the sponsor.

## 9. How to propose a change in this repository

- Every definition stays **Draft**. Reviews are evidence, not approval.
- Respect the phase gates: no metric formulas, no physical or source mappings, no worked question-and-answer demonstrations. Classification values (statuses, reasons, mechanisms) are listed as values of a concept, not as concepts; detailed taxonomies are Phase 3.
- Do not invent concept, relationship or ambiguity IDs. Refer to existing concepts by ID in machine-readable fields and by name in human text. New concepts carry a temporary key such as `clearing-give-up-and-acceptance:give-up-line`; the Ontology Lead assigns IDs.
- Reuse before you create. If another domain is the natural owner, write a suggestion for that domain instead.
- Confidentiality: never name the sponsor's employer, internal systems, teams, clients or internal facts. Use synthetic examples: Client A, Executing Broker X, Clearing Broker Y, CCP Z, Venue V. Company questions ask; they never presume an answer.
- Write for a busy business reviewer: short sentences, plain English, "a kind of", "part of", "a step in". No modelling jargon.
- Changes to the registers go through the Ontology Lead with a change-log entry; generated pages are never edited by hand.
