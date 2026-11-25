---
description: Read the experts' answers of a domain from its Excel workbook and propose what they change
---

Read the experts' answers for the domain `$1`.

1. Run `python3 tools/read_answers.py $1` and read `.review-notes/answers/$1.md`.
2. Follow "Read and use the experts' answers" in `AGENTS.md`: summarise the answers, list what is unanswered (priority 1 first), unsigned, disputed or marked CONFLICT, and propose the clarifications, meaning changes, new concepts or ambiguity updates the answers suggest.
3. Write the result to `.review-notes/<today yyyy-mm-dd>-$1-answers.md` and show me a short summary. Do not edit the registers or the workbook.
