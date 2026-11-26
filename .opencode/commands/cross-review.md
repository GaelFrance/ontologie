---
description: Cross-review several domains (expert per domain, cross-check, supervisor). Give domain folder names, or "all".
---

Run a cross-review of these domains: $ARGUMENTS ("all" means the eleven domains listed in `AGENTS.md`).

1. For each domain, use the domain-reviewer subagent with that domain name. Run them one at a time if the model's context is small; each writes its own notes file in `.review-notes/`.
2. Then use the cross-checker subagent on today's notes.
3. Then use the review-supervisor subagent to produce the decision list.
4. Show me the decision list path and its summary. Apply nothing until I say which items to apply.
