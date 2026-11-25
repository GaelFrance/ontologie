---
description: Rebuild the generated pages and run the repository checks
---

Run these commands in order and show me their output:

1. `python3 tools/build_domain_views.py`
2. `python3 tools/build_domain_views.py --check`
3. `git status --short`

If the check fails, explain each failure in one line and propose the fix to the registers (never to a generated file). Do not commit.
