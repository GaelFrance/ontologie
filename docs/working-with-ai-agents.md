# Working on the ontology with AI agents

Status: Draft, 2026-11-25

This page explains how to maintain this repository with an AI coding agent: **OpenCode** in a terminal, or **Roo Code** in VS Code, both connected to a **Qwen** model served by an OpenAI-compatible endpoint. The agent never approves a meaning: everything it produces is a Draft proposal for the Ontology Lead and the domain owners.

## What the repository gives the agent

| File or folder | Read by | What it does |
|---|---|---|
| `AGENTS.md` | OpenCode, Roo Code | Rules that must never be broken and step-by-step procedures for the usual tasks |
| `.agents/skills/<domain>-expert/SKILL.md` | OpenCode, Roo Code | One expert per domain: scope, distinctions, venue and regime differences, pitfalls, review checklist |
| `.opencode/agents/` | OpenCode | Three reviewers that run in their own context: `domain-reviewer`, `cross-checker`, `review-supervisor` |
| `.opencode/commands/` | OpenCode | Ready-made tasks, typed as `/name` (table below) |
| `.roomodes`, `.roo/rules/`, `.roo/commands/` | Roo Code | Three modes ("Ontology Lead", "Domain expert", "Domain reviewer"), a rule that points to `AGENTS.md`, and the same slash commands as OpenCode, each switching to the right mode |
| `tools/pr_scope.py` | Both | Before a merge: which domains a branch touches and who may merge it |
| `tools/next_ids.py` | Both | Prints the next free concept, relationship and ambiguity IDs, so the agent never guesses one |
| `tools/read_answers.py` | Both | Turns a domain's Excel workbook into a page the agent can read |
| `tools/merge_answers.py`, `tools/setup_computer.py` | Git | Merge two versions of a shared workbook answer by answer; register that merge once per computer |

Review notes are written to `.review-notes/`, which is not committed. Decisions go into the registers and the decision log once a person has taken them.

## Set up OpenCode with Qwen

1. Install OpenCode by following its documentation (opencode.ai/docs). If the firm's network blocks the installer, ask the team that packages developer tools.
2. Get from the team that hosts the model: the endpoint URL (ending in `/v1`), the model name as the endpoint knows it, and an API key if one is needed. Ask them to confirm that **tool calling is enabled** for that model on the server: without it the agent can chat but cannot read files or run the checks.
3. Put the connection in your personal configuration, never in the repository: `~/.config/opencode/opencode.json`. Current OpenCode (version 2):

```json
{
  "$schema": "https://opencode.ai/config.json",
  "providers": {
    "firm-llm": {
      "name": "Firm LLM",
      "env": ["FIRM_LLM_API_KEY"],
      "package": "@opencode/ai/providers/openai-compatible",
      "settings": { "baseURL": "https://llm.example.internal/v1" },
      "models": { "qwen-coder": { "name": "Qwen coder" } }
    }
  },
  "model": "firm-llm/qwen-coder"
}
```

   Replace the URL and the model name with the ones you were given; set the key in the environment variable `FIRM_LLM_API_KEY`. With an older OpenCode (version 1) the same block is written `"provider"` (singular), `"npm": "@ai-sdk/openai-compatible"` and `"options": { "baseURL": "…", "apiKey": "{env:FIRM_LLM_API_KEY}" }`. Check the provider page of the documentation for the version you have.
4. Open a terminal in the repository folder and run `opencode`. Ask "Which skills and agents do you see?": it should list the ten `*-expert` skills and the three reviewers.

## Set up Roo Code with Qwen

1. Install the Roo Code extension in VS Code.
2. In its settings, add an API configuration of type "OpenAI Compatible" with the same URL, key and model name.
3. Open the repository folder. Roo Code reads `.roomodes` (two project modes appear in the mode list), `.roo/rules/` and the skills in `.agents/skills/`.

## Daily use

| Task | OpenCode | Roo Code |
|---|---|---|
| Answer a business question | `/ask what is a give-up line?` | Ask in the "Ask" mode |
| Review one domain | `/review-domain execution` | "Domain reviewer" mode: "Review the execution domain" |
| Cross-review (expert per domain, cross-check, supervisor) | `/cross-review execution clearing-give-up-and-acceptance` or `/cross-review all` | "Orchestrator" mode: "Cross-review execution and clearing-give-up-and-acceptance following AGENTS.md", which hands each domain to the "Domain reviewer" mode |
| Apply what you decided | `/apply-change items 1, 3 and 4 of .review-notes/2026-11-26-decisions.md` | "Ontology Lead" mode, same sentence |
| Add questions for the firm | `/new-firm-questions margin-and-collateral intraday calls` | "Ontology Lead" mode |
| Read the experts' answers and see what they change | `/read-answers execution` | "Ontology Lead" mode: "Read the execution answers following AGENTS.md" |
| Help an expert prepare answers (the expert types them in Excel) | `/prepare-answers execution questions 3 and 5` | "Domain expert" mode |
| Rebuild and check | `/check` | "Ontology Lead" mode: "Run the checks" |

Then review the diff yourself, commit on a branch and open the pull request in the firm's repository service. The agent should never push to the main branch.

Roo Code has the same slash commands (`/ask`, `/review-domain`, `/cross-review`, `/apply-change`, `/read-answers`, `/prepare-answers`, `/check`, `/scope`); type the arguments after the command, as in OpenCode. Each command switches to the right mode by itself.

## OpenCode or Roo Code?

Both use the same model, the same rules (`AGENTS.md`), the same expert skills and the same tools, so the content they produce should be equivalent; the model matters far more than the tool. The differences are in daily use:

| | OpenCode | Roo Code |
|---|---|---|
| Where | Terminal | VS Code side panel |
| Best for | The Ontology Lead and anyone at ease with a terminal | Domain experts and owners: files, diffs and Git in one window, each edit shown for approval |
| Cross-review | Reviewer subagents, each in its own context | The Orchestrator hands each domain to a subtask in the "Domain reviewer" mode |
| Limiting what the agent may edit | By instructions in `AGENTS.md` | Also enforced per mode: the reviewer mode can only write review notes |
| Cost in context | Lighter system prompt | Heavier system prompt; with a small context window, keep tasks shorter |

A team can mix both: nothing in the repository depends on which one a person uses.

## Working with several experts

Each domain has one owner and two or three experts, each on their own computer; the experts' guide is [the guide for domain experts](expert-guide.md). Domain owners merge what stays within their domain, so the Ontology Lead is not a bottleneck (rules in [who merges](governance.md#who-merges)). As Ontology Lead:

1. **Protect the main branch** in the repository service: changes only through pull requests, at least one approval, and merge allowed for the domain owners and you. Give the experts write access so they can push their own branches. The service cannot check which domain a pull request touches, so owners run `python3 tools/pr_scope.py` (or `/scope` in OpenCode) before merging: it says whether they may merge or must pass the pull request to you.
2. **List owners and experts** in [`governance/experts.md`](../governance/experts.md). Add the owner of each domain as default reviewer of pull requests on it.
3. **Give each expert** the repository address, the Qwen settings and the expert guide. Each one runs `python3 tools/setup_computer.py` once after cloning, and so do you: it lets Git merge the shared workbooks answer by answer. The repository service's own merge button cannot do that, so a pull request on a workbook that changed meanwhile shows a conflict; the expert then runs `git pull origin main` on their branch, which merges the answers locally, and pushes again.
4. **Owners merge answer pull requests quickly**, so that experts keep working on the latest workbook. Before merging, `/read-answers <domain>` on the branch shows what changed, answers without initials and cells marked CONFLICT.
5. **Owners turn answers into changes** in their domain: `/read-answers <domain>`, then `/apply-change` for what they accept; changes that cross domains come to you.

## Getting good results from a smaller model

The workflow was built with a very large model. Qwen models served in-house usually have a smaller context and are less reliable over long multi-step tasks, so:

- **One domain at a time.** Run a cross-review of two or three related domains rather than all ten at once; `/cross-review` runs the reviewers one after the other for that reason.
- **Short tasks with a clear end.** "Review execution", then "cross-check", then "consolidate" works better than one long instruction.
- **Always run `/check` and read the diff.** The checks catch broken tables and stale pages; they do not catch a wrong meaning.
- **Ask for the plan first** on any change touching several registers ("list the edits you will make, do not edit yet").
- **Start a new session** when an answer starts to drift; the context is then clean and `AGENTS.md` is re-read.
- If the model ignores a rule, add one plain sentence to `AGENTS.md` rather than repeating it in every request.

## Safety net

- Generated pages are rebuilt from the registers, so a broken generated page is fixed by running the build, never by hand.
- `tools/build_question_workbooks.py` keeps the answers experts entered in each `questions-for-experts.xlsx`. If an answer no longer matches any question it stops and writes nothing; move the answer by hand (`--force` drops it).
- Git history keeps every earlier state: revert a bad commit rather than repairing it by hand.
