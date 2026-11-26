---
description: Draft new questions for our firm in one domain
argument-hint: <domain> <topic>
mode: ontology-lead
---

Draft new questions for our firm in the domain and on the topic I give after this command. Load the <domain>-expert skill and read domains/<domain>/company-questions.md; add questions in the same format without repeating existing ones and without stating any firm fact as known. Then run python3 tools/build_question_workbooks.py (it keeps entered answers and stops if one would be lost: tell me, never use --force unless I ask), run the checks in AGENTS.md and add a change-log bullet.
