---
description: Help me prepare answers to the questions for our firm (I type them in Excel)
argument-hint: <domain> <which questions>
mode: domain-expert
---

I am a domain expert for the domain I name after this command. Run python3 tools/read_answers.py <domain> and read .review-notes/answers/<domain>.md to see the open questions (priority 1 first). Load the <domain>-expert skill. For each question I pick, explain in two or three sentences what it asks and why it matters, ask me how our firm does it, and turn my reply into a short answer I can paste into the Answer column of domains/<domain>/questions-for-experts.xlsx. Never write into the workbook and never invent a firm fact. At the end remind me to add my initials in "Answered by", save, and send the file right away (docs/contributor-guide.md).
