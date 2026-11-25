---
description: Write the weekly report of changes merged into the main branch
argument-hint: <optional --days N or --since YYYY-MM-DD>
mode: ontology-lead
---

Run git fetch origin, then python3 tools/weekly_report.py (add the options I give after this command, if any; default is the last 7 days), and read the report it writes in reports/weekly/. Give me a summary of five lines at most: what was merged, concepts added or changed per domain, answers progress, and any shared files changed (tools, agent setup, classification) that I should look at. Do not commit.
