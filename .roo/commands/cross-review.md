---
description: Cross-review several domains (expert per domain, cross-check, supervisor)
argument-hint: <domain folder names, or all>
mode: orchestrator
---

Run a cross-review of the domains I name after this command ("all" means the eleven domains listed in AGENTS.md), following "Cross-review" in AGENTS.md:
1. For each domain, one at a time, start a subtask in the "Domain reviewer" mode: "Review the domain <domain> following .opencode/agents/domain-reviewer.md".
2. Then a subtask in the "Domain reviewer" mode: "Cross-check today's review notes following .opencode/agents/cross-checker.md".
3. Then a subtask in the "Domain reviewer" mode: "Consolidate the review following .opencode/agents/review-supervisor.md".
4. Show me the path and summary of the decision list. Apply nothing.
