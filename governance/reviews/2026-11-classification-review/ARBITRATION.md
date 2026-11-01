# Classification review — arbitration

Date: 2026-11-01. Requested by the sponsor. Three AI expert reviews of the review-domain classification ([`review-domains.md`](../../review-domains.md)): [01 Ontology Lead](01-ontology-lead.md), [02 ETD and OTC clearing](02-clearing.md), [03 ETD execution](03-execution.md). AI reviews are evidence, not approval (governance principle 6). The result is Draft and goes to the named owners like any other change.

## Adopted

| Point | Source | Applied as |
|---|---|---|
| Each concept has exactly one primary domain (its owner approves it); other domains only show it for comment | 01 | Two columns, Primary concepts and Also shown; `--check` fails unless each concept has exactly one primary |
| Split Clearing by business function, not by ETD versus OTC (OTC-specific concepts are still backlog) | 01, 02 | "Clearing: give-up and acceptance" (wave 1 pack for AG-004) and "Clearing: services, accounts and client clearing" |
| Clearing Member and CCP visible to clearing reviewers | 02 | Primary on the clearing services page, shown on Parties |
| New domain "Service offering and market access" for Service Offering and Market Access Arrangement | 01 | Owner: product development lead (sponsor or delegate), added to the governance proposal. Fallback if the sponsor wants fewer pages: Service Offering to Fees, Market Access Arrangement to Execution |
| Rename "Products and reference data" to "Instruments, venues and calendars" ("product" is ambiguous, LD-A0021) | 01 | Applied |
| Executing Broker and Trading Venue Member approved by the Listed Execution product owner | 01, 03 | Primary on the execution page |
| Execution page shows give-up, give-up agreement, executing brokerage, venue fees and service offering; it ends where clearing takes over | 03 | Also shown, with a scope note stating the boundary concept by concept |
| Portfolio belongs with margin | 02 | Primary on the margin page (01 had it on clearing services) |
| Cut-off approved by operations; Account by Reference & Client Data | 01 | Applied |
| Reviewer roles completed where the answer differs | 01, 02, 03 | OTC Clearing product owner on Parties, Instruments, Margin, Fees, Regulation, Post-trade and give-up; Revenue domain owner on Execution; Listed Execution product owner on Regulation; Compliance on Parties; Collateral Manager on clearing services and post-trade; ETD Clearing product owner on Instruments, Margin and Post-trade. Business Finance moved from Margin to Fees (collateral revenue is reviewed there) |
| One question per reviewer role, concrete walk-through, ETD and OTC asked separately; open questions 4, 9, 10, 11 placed on the page that answers them | 01, 02, 03 | Table "Questions by reviewer role" |
| Generic sequence line on process pages, scope note, review wave and pilot use cases, backlog items the domain may need, verdict column | 01, 02, 03 | Table "Page content" and generator |
| Ambiguities in full only where their concepts are approved; one line with a link elsewhere | 01 | Generator |
| Remove the "En bref (FR)" blocks from generated pages | 01, 02 | Applied, consistent with the removal of French labels |

## Not adopted, or deferred

| Point | Source | Reason |
|---|---|---|
| Worked synthetic examples with outcomes (for example 60 of 100 lots taken up) | 02, 03 | Close to a query-resolution demonstration, deferred to Phase 4 by the phase-1 approval. Sequences name concepts only |
| Sub-sections of the execution page, each with a co-reviewer | 03 | Covered by per-role questions and the primary / also-shown split; revisit if the page proves too long |
| ETD / OTC markers per concept | 02 | Needs a governed scope attribute on each concept; to add with the next catalogue release |
| A separate OTC clearing page | 02 | Reconsider when Clearing Submission, Porting and Compression are promoted |

## Definition issues for the owners (not changed here)

Changing a definition needs owner review. These go into the first review packs.

| Concept | Issue | Source | Page |
|---|---|---|---|
| LD-C0006 Executing Broker | Thin and near-circular; the client-facing meaning lives only in its usage note | 01, 03 | Execution |
| LD-C0017 Execution | "Fulfilling all or part of a trading instruction" fits a negotiated block or EFRP poorly; "trading instruction" is not the catalogue term Order | 03 | Execution |
| LD-C0020 Allocation | Still says the instruction is a "later specialisation", but LD-C0060 now exists | 03 | Execution |
| LD-C0060 Allocation Instruction | Standing instructions held by the broker are neither covered nor excluded | 03 | Execution |
| LD-C0059 / LD-C0061 | DMA and sponsored access appear both as access models and as handling channels; "sponsored" also names a CCP sponsored clearing model | 02, 03 | Service offering |
| LD-C0059 Market Access Arrangement | Said to be documented by agreements, yet it is a kind of Agreement | 01 | Service offering |
| LD-C0069 CCP Account | "In a clearing member's name" may not fit sponsored or direct-client accounts | 02 | Clearing services |
| LD-C0053 Clearing Member Acceptance | ETD wording only; the OTC limit check on submission is not named | 02 | Give-up |
| LD-C0022 Give-up / Take-up Process | Check that "executed" covers trades registered off-book (block, EFRP) | 02 | Give-up |
| LD-R0026 membership category | Exists only as a qualifier; needs a governed vocabulary | 02 | Clearing services |
| LD-C0027 Portfolio | Generic enough to overlap Account and Position; could be parked like LD-C0019 | 01 | Margin |
| LD-C0041, LD-C0042 | "Under a defined semantic contract" is jargon for a business reviewer | 01 | Fees |
| LD-C0004 Client | Could point to Commercial Group (LD-C0073) | 01 | Parties |
