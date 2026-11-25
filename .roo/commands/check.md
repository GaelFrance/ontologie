---
description: Rebuild the generated pages and run the repository checks
mode: ontology-lead
---

Run python3 tools/build_domain_views.py, then python3 tools/build_domain_views.py --check, then git status --short, and show me the output. If the check fails, explain each failure in one line and propose the fix to the registers (never to a generated file). Do not commit.
