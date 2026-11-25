# Guide for domain experts

Status: Draft, 2026-11-25

You are one of the two or three experts of a business domain. You can ask the ontology questions, answer the questions for our firm in your domain's workbook, and propose changes to your domain. Nothing you write approves a meaning: the Ontology Lead turns answers and proposals into changes, and the domain owner approves them.

## 1. Set up your computer (once, about 30 minutes)

1. Install **Git**, **Python 3** and either **OpenCode** (terminal) or **VS Code with the Roo Code extension**, through the firm's usual software channel.
2. Connect OpenCode or Roo Code to the firm's Qwen model: follow "Set up OpenCode with Qwen" or "Set up Roo Code with Qwen" in [working with AI agents](working-with-ai-agents.md). The Ontology Lead can give you the settings.
3. Copy the repository to your computer and prepare it:

```bash
git clone <repository address given by the Ontology Lead>
cd ontologie
python3 -m pip install openpyxl
python3 tools/setup_computer.py
```

   The last command is essential: it lets Git merge the workbook answer by answer when two experts worked on it at the same time. Without it, Git cannot merge an Excel file.

## 2. Ask the ontology a question

Open OpenCode in the `ontologie` folder (or open the folder in VS Code and choose the "Domain expert" mode in Roo Code) and ask, for example:

- `/ask what is the difference between a give-up and an allocation?`
- "Which concepts of my domain are still unclear?"

The answer names concepts first, with their ID in brackets (for example *Give-up Line (LD-C0131)*).

## 3. Answer the questions for our firm

Your domain's workbook is `domains/<your domain>/questions-for-experts.xlsx`. It is **shared by the experts of your domain**, so follow this routine every time:

1. **Get the latest version just before you start:**
   ```bash
   git checkout main
   git pull
   git checkout -b answers-<your initials>-<date>
   ```
2. **Open the workbook in Excel.** Fill in only the yellow cells. On sheet 1 write the answer, the status and any follow-up, and **your initials in "Answered by"**. On sheet 3 give your view and **your initials in "Expert"**.
   - If another expert already answered and you disagree, do not replace their answer: add yours after it, starting with your initials ("CD: in practice …").
   - Need help with a question? Ask the agent: `/prepare-answers <your domain> questions 3 and 5`. It explains the question and drafts an answer that you paste into Excel. It never writes in the workbook.
3. **Save, close Excel and send your work straight away** (do not keep it for days, so that others work on the latest version):
   ```bash
   git add domains/<your domain>/questions-for-experts.xlsx
   git commit -m "Answers <your domain>, <your initials>"
   git pull origin main
   git push -u origin answers-<your initials>-<date>
   ```
4. **Open a pull request** in the repository service for the Ontology Lead.

### If Git reports a conflict on the workbook

`git pull origin main` merges your answers with those another expert sent meanwhile. Answers to different questions merge by themselves. If you and the other expert changed the same cell, the cell keeps both versions, marked **CONFLICT**, and Git says the merge failed. Then:

1. Open the workbook in Excel and search for `CONFLICT`. Keep the right text (or both, each with its initials) and remove the marker.
2. Save, then `git add domains/<your domain>/questions-for-experts.xlsx`, `git commit`, `git push`.

If the pull request page says the branch has conflicts, do the same: `git pull origin main` on your branch, resolve, push. The repository service cannot merge Excel files itself.

## 4. Propose a change to your domain

On a new branch (`git checkout -b proposal-<topic>`):

- `/review-domain <your domain>` for an expert review of the domain, or `/read-answers <your domain>` to see what the answers suggest changing.
- `/apply-change …` with the change you propose. Change only concepts of your own domain; for others, write a comment in the pull request.
- `/check`, then commit, push and open a pull request. The Ontology Lead reviews and merges.

## 5. Good to know

- Never write firm facts into a definition: how our firm works goes into the workbook; definitions stay generic.
- Never edit the generated pages (`concepts.md`, `review.md`, the domain `README.md`, `glossary.md`); they are rebuilt.
- If the agent's answer looks wrong or invents something, say so to the Ontology Lead; it may need a rule in `AGENTS.md`.
