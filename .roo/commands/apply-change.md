---
description: Apply agreed ontology changes
argument-hint: <changes, or items of a decision list>
mode: ontology-lead
---

Apply the agreed changes I describe after this command, following "Apply an agreed change" in AGENTS.md exactly: restate the changes and ask if anything is unclear; get new IDs only from python3 tools/next_ids.py; edit only registers and hand-written pages; rebuild and run the checks; add a CHANGELOG.md bullet; run python3 tools/pr_scope.py; show me git diff --stat and propose a commit message naming the IDs. Commit only when I confirm, on a branch, never on the main branch.
