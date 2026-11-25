---
description: Help a domain expert prepare answers to the questions for our firm (the expert types them in Excel)
---

I am a domain expert for `$1`. Help me answer the open questions for our firm: $ARGUMENTS

1. Run `python3 tools/read_answers.py $1` and read `.review-notes/answers/$1.md` to see which questions are still open (priority 1 first).
2. Load the `$1-expert` skill. For each question I pick, explain in two or three sentences what it asks and why it matters, then ask me how our firm does it.
3. Turn what I tell you into a short answer I can paste into the "Answer" column of `domains/$1/questions-for-experts.xlsx`. Never write into the workbook yourself, and never invent a firm fact.
4. At the end, remind me to write my initials in "Answered by", save, and send the file back right away (`docs/contributor-guide.md`).
