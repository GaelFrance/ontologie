---
description: Before merging - which domains this branch touches and who may merge it
argument-hint: <optional base branch>
mode: ontology-lead
---

Run python3 tools/pr_scope.py and show me its output. Explain the verdict in one or two sentences: may the owner of a single domain merge, which owners must approve or comment first, or must the Ontology Lead merge. If it reports duplicate IDs, propose renumbering only the new IDs of this branch with python3 tools/next_ids.py. Do not merge anything.
