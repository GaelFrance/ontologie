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
| `.roomodes`, `.roo/rules/` | Roo Code | Two modes, "Ontology Lead" and "Domain reviewer", and a rule that points to `AGENTS.md` |
| `tools/next_ids.py` | Both | Prints the next free concept, relationship and ambiguity IDs, so the agent never guesses one |

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
| Rebuild and check | `/check` | "Ontology Lead" mode: "Run the checks" |

Then review the diff yourself, commit on a branch and open the pull request in the firm's repository service. The agent should never push to the main branch.

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
