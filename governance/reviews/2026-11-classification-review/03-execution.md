# Execution domain: review of the classification

Reviewer viewpoint: listed derivatives execution (care, DMA, algo, sponsored access, venue membership and third-party execution, block/EFRP, average pricing, allocation, giving-side give-up, execution fees and brokerage). Source read: `governance/review-domains.md`, `domains/execution.md`, `ontology/foundation.md`, `relationships/relationships.md`, `governance/ambiguity-register.md`, `ontology/concept-annotations.md`, `governance/decision-log.md`, `governance/governance-model-proposal.md`, ARBITRATION.md §6, review 01, hub UC-003 and UC-004.

## 1. Verdict

The Execution domain is the right business cut and needs no split into separate pages. It does miss what an execution desk actually owns: the executing broker role, the venue, the giving side of the give-up and the give-up agreement, executing brokerage and venue fees, and the service offering.
Execution is the most hand-off-heavy domain: allocation, average pricing and give-up cross into clearing. So the page should be ordered by lifecycle stage, with the co-reviewer named on each section, and should end at the clearing boundary.
The reviewer question is too broad for a busy expert. Replace it with six checks, one per decision the desk really makes.

## 2. Proposed rows for `governance/review-domains.md`

Bold marks what changed.

| Domain | Page | Owner role | Reviewer roles | Concept IDs | What the reviewer is asked |
|---|---|---|---|---|---|
| Listed derivatives execution | execution | Listed Execution product owner | ETD post-trade operations lead; Compliance; **ETD Clearing product owner (give-up hand-off section only)**; **Revenue domain owner (execution economics section only)** | **LD-C0006, LD-C0009,** LD-C0016 to LD-C0021, **LD-C0022,** LD-C0033, **LD-C0035, LD-C0036,** LD-C0041, **LD-C0052, LD-C0055,** LD-C0058 to LD-C0061 | **(1) Access: for each venue, can you tell the client-facing executing broker (LD-C0006) from the venue member that enters the order (LD-C0058), including third-party execution where the firm is not a member? Is the list of access models in LD-C0059 complete for execution, and is the line between the DEA permission (an access model) and the channel of a given order (LD-C0061) clear? (2) Channel: are care, broker algorithm, DMA and sponsored access the full list of values for the revenue split? Is a block or EFRP traded by voice an execution method rather than a channel? (3) Identity: for one client order worked as child orders and filled several times, do Order, Execution and Trade give the records and counts your desk and middle office use, and which of them do you call "fill" and "trade"? (4) Averaging and allocation: who averages (venue or CCP facility, or broker), what is eligible, how are rounding residuals handled, and can an allocation instruction be standing, pre-trade or post-trade and amended until the cut-off? (5) Hand-off: is the rule "an allocation to an account carried by another clearing member starts a give-up, otherwise it is internal" right in both directions, and what does the giving side still own until take-up or lapse? (6) Economics: can you separate the client execution fee, executing brokerage (received as executing broker, or paid as clearing broker and recharged) and the venue fee by creditor and charge basis (per side, round turn, ticket)?** |
| Parties, roles and clients | parties-and-roles | Reference & Client Data | Legal; ETD Clearing product owner; **Listed Execution product owner (approves LD-C0005, LD-C0006, LD-C0058)** | unchanged | unchanged, plus: **"Executing broker, venue member, regulatory executing entity and giving clearing member can be four different parties for one execution (LD-A0035): can your data tell them apart?"** |
| Products, instruments and reference data | products-and-reference-data | Reference & Client Data | ETD post-trade operations lead; Listed Execution product owner | unchanged | unchanged, plus: **"Is a listed strategy (spread, options combination) an instrument with legs whose execution yields leg executions? Are the trade dates of evening and overnight sessions assigned by the venue calendar (LD-C0066)?"** |
| Fees, revenue and contribution | fees-revenue-and-contribution | Revenue domain owner | Collateral Manager (collateral revenue); Business Finance; Listed Execution and ETD Clearing product owners | LD-C0031 to LD-C0042, LD-C0052, **LD-C0061,** LD-C0073, LD-C0074 | unchanged, plus: **"Is execution revenue split by handling channel (sponsor decision 2), and is executing brokerage counted once when it is paid by the clearing broker and recharged to the client (LD-R0080)?"** |

Why each change was made:

- **LD-C0006 Executing Broker** belongs at the centre of execution. Today it appears only on the Parties page, so its usage note (client-facing, not the venue member) is invisible to the execution owner. The Listed Execution product owner should approve its meaning.
- **LD-C0009 Trading Venue**: an execution `occurs_on` a venue (LD-R0006), and a block or EFRP is registered there under venue rules. The concept stays on the Products page as reference data.
- **LD-C0022 Give-up / Take-up Process and LD-C0055 Give-up Agreement**: the arbitration keeps LD-C0022 Common because "the executing side is party to it", and the executing broker is a party to LD-C0055. With execution-only service (give-up out) in the sponsor's mix, the execution desk owns submission, designation at order entry and lapsed trades that stay with the giving member. Clearing remains the owner domain; Execution co-reviews the giving side.
- **LD-C0035 and LD-C0036**: executing brokerage is the execution revenue of an execution-only business. Venue fees decide all-in versus fees-plus pricing. LD-A0001 is already on the page, but two of its three concepts are not.
- **LD-C0052 Service Offering** carries execution-only, execute-and-clear and the handling channel: it is the execution product.
- **LD-C0061 on the Fees page**: it is required context for LD-C0041, so the Revenue owner must see it.
- **LD-C0019 Transaction stays** but is labelled "blocked, review only the alias rule of LD-A0008 (the MiFIR 'transaction' is not this concept)".

**Execution versus clearing** (to be stated at the top of the page):

| Concept | Owner domain | Execution reviews |
|---|---|---|
| Order, Execution, Order Handling Channel, Average Price Group, Allocation, Allocation Instruction | Execution | everything |
| Trade | shared | the pre-clearing tier only (LD-A0025); CCP-facing and member–client tiers are Clearing |
| Market Access Arrangement | shared | access to venues; access to clearing services is Clearing |
| Give-up / Take-up, Give-up Agreement | Clearing | the giving side and the terms that bind the executing broker |
| Clearing Member Acceptance, Clearing Acceptance, CCP Interposition | Clearing | nothing; show them as "after this point" |

**Sub-domains:** no separate pages. Split the page into five sections, each naming its co-reviewer, so a busy reviewer reads only their own part:

| Section | Concepts | Co-reviewer |
|---|---|---|
| A. Market access and roles | LD-C0006, LD-C0009, LD-C0052, LD-C0058, LD-C0059 | Compliance (DEA controls) |
| B. Order to execution | LD-C0016, LD-C0017, LD-C0061 | Compliance |
| C. Execution to allocation | LD-C0018, LD-C0019, LD-C0020, LD-C0021, LD-C0060 | ETD post-trade operations lead |
| D. Hand-off to clearing | LD-C0022, LD-C0055 | ETD Clearing product owner |
| E. Execution economics | LD-C0033, LD-C0035, LD-C0036, LD-C0041 | Revenue domain owner |

This could live as a small "sections" table in `review-domains.md` that the generator reads.

**Outside my rows:**

- Add LD-C0020 and LD-C0060 to Post-trade operations, because allocation cut-offs and breaks are operational.
- Add the Listed Execution product owner as a reviewer of Regulation and rule changes, because venue rule changes (block thresholds, EFRP rules, DEA and algo controls) are among the most frequent circulars.

## 3. Additions to the execution page

1. **Lifecycle sequence** (one line, with the concept at each step): client order (LD-C0016, channel LD-C0061) → child and venue orders → venue executions by matching, or block/EFRP registration (LD-C0017 at LD-C0009, execution method taxonomy) → client-facing executions → average price group (LD-C0021) → allocation instruction (LD-C0060, cut-off LD-C0065) → allocations (LD-C0020) → internal, or give-up submitted (LD-C0022 under LD-C0055) → **clearing domain starts**: member take-up (LD-C0053), CCP acceptance (LD-C0023), interposition (LD-C0054) → charges (LD-C0033, LD-C0035, LD-C0036).

2. **Worked synthetic example.** Label it "illustrative; not an expected answer". It uses no amounts, so it is not a resolution demonstration.
   - A synthetic investment manager places a care order to buy 300 lots of a synthetic index future on "Venue X".
   - The desk passes the order to a broker algorithm: the channel changes over time (LD-R0046).
   - The algorithm sends 3 child orders and gets 7 venue executions.
   - The client asks for an average price: 1 average price group, with a possible rounding residual.
   - The allocation instruction splits the quantity: 100 lots to an account cleared in-house (an internal allocation) and 200 lots to an account cleared by "Clearing Broker Y" (a give-up).
   - Y takes up 150 lots by the cut-off. The other 50 lapse and stay with the giving member: partial and lapsed per LD-A0010.
   - Charges: a client execution fee on 300 lots; executing brokerage on the 200 given-up lots, billed to Y and possibly recharged to the client (LD-R0080); a venue fee whose debtor is set by venue rules.
   - Point to make on the page: the records are 1 order, 3 child orders, 7 executions, 1 average price group, 2 allocations and 1 give-up line. Record the lineage, not the counts.

3. **"Not yet in the catalogue" box**, taken from ARBITRATION §6:
   - Execution Method (block, EFRP; taxonomy axis now)
   - the Order `derived_from` (parent and child) and `submitted_to` relationships
   - the trading capacity axis
   - Fee Rebate (venue liquidity-provider rebates)
   - Activity Volume
   - Regulatory Report (transaction reporting)
   - Identifier Scheme (venue trade IDs)
   - the pending ambiguities on block trade, on DMA, DEA and algorithm, on trade identifiers, and on rebate, discount and waiver.

   Ask the reviewer: "does any decision you need now require one of these?"

4. **Scope note:** the execution of OTC derivatives on swap execution facilities, MTFs and OTFs is in no domain today. Say so explicitly, so that it is not assumed to be covered here.

## 4. Definition issues (to send to the definition owners, not changed here)

- **LD-C0020 Allocation** still says "instruction and completed event are later specialisations". The instruction now exists as LD-C0060, an Instruction that is not a specialisation of this Process. The definition text is stale.
- **LD-C0006 Executing Broker** ("the party providing the execution service concerned") is close to circular. The client-facing meaning lives only in its usage note.
- **LD-C0017 Execution** ("fulfilling all or part of a trading instruction") fits a negotiated block or EFRP registered on a venue poorly, and "trading instruction" is not the catalogue term Order.
- **LD-C0059 and LD-C0061 overlap on DMA and sponsored access:** the first holds them as access models, the second as handling channels. One sentence on the boundary is needed (the permission versus how a given order was routed).
- **LD-C0060 Allocation Instruction** names only the client or its investment manager as the source. Standing allocation instructions held by the broker should be covered or excluded explicitly.
