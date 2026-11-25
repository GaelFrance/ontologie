---
description: Draft new questions for our firm in one domain, then rebuild the expert workbook
---

Draft questions for our firm in the domain `$1` about: $ARGUMENTS

Load the `$1-expert` skill and read `domains/$1/company-questions.md`. Add new questions in the same format and numbering style, without repeating existing ones and without stating any firm fact as known. Then run `python3 tools/build_question_workbooks.py`, (it keeps the answers already entered and stops if one would be lost: tell me, never use `--force` unless I ask), run the checks in `AGENTS.md`, and add a change-log bullet.
