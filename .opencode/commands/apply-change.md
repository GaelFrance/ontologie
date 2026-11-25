---
description: Apply agreed ontology changes (new concept, clarification, meaning change already decided)
---

Apply these agreed changes: $ARGUMENTS

Follow "Apply an agreed change" in `AGENTS.md` exactly:
1. Restate the list of changes and whether each is a clarification, a decided meaning change or a new concept. If anything is unclear, ask before editing.
2. For new IDs run `python3 tools/next_ids.py --count N`.
3. Edit only the registers and hand-written pages; keep every table parseable.
4. Run `python3 tools/build_domain_views.py` then `python3 tools/build_domain_views.py --check`, and fix failures.
5. Add one bullet to `CHANGELOG.md` under "Unreleased".
6. Show me `git diff --stat` and propose a commit message naming the IDs. Commit only when I confirm, on a branch, never on the main branch.
