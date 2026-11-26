# Contributor guide

Status: Draft, 2026-11-25

Who does what on the ontology, and how to do it with **OpenCode** (terminal) or **VS Code with Roo Code**. Both use the firm's Qwen model and the same rules, skills and tools; pick the one you are comfortable with. Setup of the tools: [working with AI agents](working-with-ai-agents.md). Rules for merging: [governance, who merges](governance.md#who-merges).

## The roles at a glance

| Role | Who | Expected of them | Time |
|---|---|---|---|
| **Ontology Lead** | One person | Keeps the whole consistent: tools, agent setup, domain classification, releases; reads the weekly report; arbitrates with the sponsor | A few hours a week |
| **Domain owner** | One per domain (a person may own several) | Approves meanings in the domain; reviews and merges pull requests; makes sure the workbook gets answered; asks the other owners when a change crosses domains | 1 to 2 hours a week |
| **Domain expert** | Two or three per domain | Answers the questions for our firm; reviews the domain's definitions; proposes changes | When asked; a session is 45 minutes to 2 hours |
| **Sponsor** | Business sponsor | Arbitrates meaning changes across domains and open questions | On request |

Nothing anyone merges approves a meaning by itself: approvals are recorded explicitly in the decision log (see [governance](governance.md)).

## Everyone: set up your computer (once, about 30 minutes)

1. Install **Git**, **Python 3**, and **OpenCode** or **VS Code with the Roo Code extension**, through the firm's usual software channel.
2. Connect the tool to the Qwen model: [working with AI agents](working-with-ai-agents.md), sections "Set up OpenCode with Qwen" or "Set up Roo Code with Qwen".
3. Copy the repository and prepare it:

```bash
git clone <repository address>
cd ontologie
python3 -m pip install openpyxl
python3 tools/setup_computer.py
```

   `setup_computer.py` is essential: it lets Git merge the domain workbook answer by answer when two people worked on it at the same time.

4. Check it works. In OpenCode, run `opencode` in the folder; in VS Code, open the folder and the Roo Code panel. Then type `/ask what is a give-up line?`. The answer should name *Give-up Line (LD-C0131)*.

**Where to type commands.** In OpenCode, type the slash commands in the OpenCode prompt and Git commands in a terminal. In VS Code, type the slash commands in the Roo Code panel; for Git, use the Source Control panel (left bar) or the terminal (menu Terminal, New Terminal). Each Roo Code command switches to the right mode by itself ("Ask", "Domain expert", "Domain reviewer", "Ontology Lead" or "Orchestrator").

**Every piece of work follows the same cycle:**

1. Start from the latest version on a new branch: `git checkout main`, `git pull`, `git checkout -b <short-topic>`. In VS Code: the branch name at the bottom left, then "Create new branch".
2. Do the work (below, by role).
3. `/check` rebuilds the pages and runs the checks. Fix anything it reports.
4. Commit and send: `git add -A`, `git commit -m "<what changed>"`, `git pull origin main`, `git push -u origin <short-topic>`. In VS Code: Source Control panel, message, Commit, then Sync.
5. Open a pull request in the repository service, with the domain owner as reviewer.

## Domain expert

**Expected:** answer the questions for our firm in your domain's workbook, honestly and with your initials; review your domain's definitions when asked; propose corrections. You never need to edit the registers yourself unless you want to.

### Answer the questions for our firm

The workbook is `domains/<your domain>/questions-for-experts.xlsx`, **shared by the experts of your domain**.

1. Get the latest version just before you start (step 1 of the cycle; a branch like `answers-<initials>-<date>`).
2. Open the workbook in Excel and fill in only the yellow cells. Sheet 1: answer, status, follow-up and **your initials in "Answered by"**. Sheet 3: your view and **your initials in "Expert"**. If you disagree with an answer already there, add yours after it, starting with your initials; do not replace it.
3. Need help? `/prepare-answers <your domain> questions 3 and 5`: the agent explains each question, asks how our firm does it, and drafts an answer you paste into Excel. It never writes in the workbook.
4. Save, close Excel and **send your work straight away** (step 4 of the cycle), so others work on the latest version. Open the pull request for your domain owner.

**If Git reports a conflict on the workbook:** answers to different questions merge by themselves. If you and another expert changed the same cell, the cell keeps both versions marked **CONFLICT** and the merge stops. Open the workbook, search for `CONFLICT`, keep the right text (or both, each with initials), save, then `git add`, `git commit`, `git push`. If the pull request page shows a conflict, run `git pull origin main` on your branch and do the same: the repository service cannot merge Excel files itself.

### Review your domain and propose changes

| Task | OpenCode or Roo Code panel |
|---|---|
| Ask about a concept | `/ask what is the difference between a give-up and an allocation?` |
| Expert review of your domain | `/review-domain <your domain>`: notes in `.review-notes/` |
| Propose a change | On a branch: `/apply-change <the change>`, then `/check`, then the cycle |

Change only concepts whose primary domain is yours; for other concepts, write a comment in the pull request for their owner.

## Domain owner

**Expected:** keep your domain moving. Concretely, every week:

1. **Review and merge pull requests on your domain**, the answer ones quickly so experts keep working on the latest workbook. Before merging, on the branch:
   - `/scope` (or `python3 tools/pr_scope.py`): which domains the branch touches, whose approval is needed, shared files changed, and duplicate new IDs to fix first.
   - `/read-answers <domain>` for a workbook change: what was answered, unsigned answers, cells left in CONFLICT.
   - `/check` must pass.
   - Then merge in the repository service. A pull request that also touches another domain needs that domain's owner's approval first; then you may merge it.
2. **Turn answers into improvements.** `/read-answers <domain>` proposes the clarifications, meaning changes and new concepts the answers suggest. Apply what you accept with `/apply-change` on a branch; meaning changes that affect other domains go to their owners, and to the sponsor if owners disagree.
3. **Review from time to time:** `/cross-review <your domain> <neighbouring domain>` runs an expert per domain, a cross-check and a supervisor, and writes a decision list in `.review-notes/`. Apply nothing until you have read it.
4. **Approve meanings** when you are ready: tell the Ontology Lead which definitions you approve; the approval is recorded in the decision log.

## Ontology Lead

**Expected:** keep the whole consistent without being a bottleneck.

1. **Every week**, run `/weekly-report` (or `python3 tools/weekly_report.py`), read it, share it with the owners, and commit it in `reports/weekly/` through a pull request. Look at the "Shared files changed" section: tools, agent setup and classification changed by others.
2. **Maintain the tools and the agent setup** (`AGENTS.md`, `.agents/skills/`, `.opencode/`, `.roo*`): when the model gets something wrong repeatedly, add one plain sentence to `AGENTS.md` or to the domain skill. See the [maintenance guide](maintenance-guide.md).
3. **Keep the lists current**: owners and experts in `governance/experts.md`, owner and reviewer roles in `governance/review-domains.md`.
4. **Record decisions** with the sponsor in `governance/decision-log.md`, and releases in `CHANGELOG.md`.
5. **Onboard** new owners and experts with this guide.

## Commands, side by side

The same commands exist in OpenCode and in Roo Code.

| Command | What it does | Who uses it |
|---|---|---|
| `/ask <question>` | Answers from the ontology, naming concepts and IDs | Everyone |
| `/prepare-answers <domain> <questions>` | Helps draft answers to paste into the workbook | Experts |
| `/review-domain <domain>` | Expert review of one domain, notes in `.review-notes/` | Experts, owners |
| `/cross-review <domains or all>` | Expert per domain, cross-check, supervisor, decision list | Owners, Lead |
| `/read-answers <domain>` | Workbook answers as a page, with the changes they suggest | Owners, Lead |
| `/apply-change <changes>` | Applies agreed changes, rebuilds, checks, adds a change-log line | Experts, owners, Lead |
| `/new-firm-questions <domain> <topic>` | Adds questions for our firm and rebuilds the workbook | Owners, Lead |
| `/scope` | Before a merge: domains touched, approvals needed, shared files, duplicate IDs | Owners |
| `/check` | Rebuilds the pages and runs the checks | Everyone |
| `/weekly-report` | Writes the weekly report of merged changes | Lead |

## Good to know

- How our firm works goes into the workbook; definitions stay generic. Never put client names, internal system names or internal figures in a definition.
- Never edit the generated pages (`concepts.md`, `review.md`, the domain `README.md`, `domains/README.md`, `glossary.md`); `/check` rebuilds them.
- If the agent invents something or ignores a rule, tell the Ontology Lead: it usually needs one sentence in `AGENTS.md`.
