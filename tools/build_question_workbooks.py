"""Build one Excel workbook of questions for the experts of each domain.

Writes domains/<page>/questions-for-experts.xlsx from the same sources as the
domain pages: the questions for our firm (company-questions.md), the questions
put to each reviewer role and the open questions on meaning
(governance/review-domains.md, governance/ambiguity-register.md).

The workbooks in the repository stay blank. Answers are firm-specific: they are
written in a copy kept inside the firm and never committed.

Usage: python3 tools/build_question_workbooks.py   (needs openpyxl)
"""
import datetime
import os
import re
import sys
import zipfile

from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import build_domain_views as bdv  # noqa: E402

FILE = "questions-for-experts.xlsx"
NAVY, TEAL, INPUT, BORDER = "14213D", "1F6F8B", "FFF2CC", "D9D9D9"
FONT = "Arial"
STAMP = datetime.datetime(2026, 11, 1)  # fixed, so an unchanged workbook rebuilds identically
SIDE = Side(style="thin", color=BORDER)
BOX = Border(left=SIDE, right=SIDE, top=SIDE, bottom=SIDE)
WRAP = Alignment(wrap_text=True, vertical="top")


def plain(text):
    if not text:
        return ""
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"(?<!\w)\*([^*]+)\*(?!\w)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    return text.replace("⚠️", "").strip()


def font(**kw):
    kw.setdefault("size", 10)
    return Font(name=FONT, **kw)


def title(ws, text, sub):
    ws["A1"], ws["A2"] = text, sub
    ws["A1"].font = font(bold=True, size=14, color=NAVY)
    ws["A2"].font = font(italic=True, color="595959")


def header(ws, row, cols):
    for j, (name, width) in enumerate(cols, 1):
        cell = ws.cell(row=row, column=j, value=name)
        cell.font = font(bold=True, color="FFFFFF")
        cell.fill = PatternFill("solid", fgColor=NAVY)
        cell.alignment = Alignment(wrap_text=True, vertical="center")
        cell.border = BOX
        ws.column_dimensions[get_column_letter(j)].width = width
    ws.row_dimensions[row].height = 30


def table(ws, start, values, inputs, ref_col):
    for k, vals in enumerate(values):
        r = start + k
        lines = 1
        for j, v in enumerate(vals, 1):
            cell = ws.cell(row=r, column=j, value=v)
            cell.font = font(color="808080" if j == ref_col else "000000")
            cell.alignment, cell.border = WRAP, BOX
            if j in inputs:
                cell.fill = PatternFill("solid", fgColor=INPUT)
            width = ws.column_dimensions[get_column_letter(j)].width or 10
            lines = max(lines, int(len(str(v or "")) / width) + 1)
        ws.row_dimensions[r].height = min(409, max(30, 13 * lines))
    return start + len(values) - 1


def dropdown(ws, options, col, first, last, prompt):
    dv = DataValidation(type="list", formula1='"' + ",".join(options) + '"', allow_blank=True)
    dv.promptTitle, dv.prompt, dv.showInputMessage = "Choose one", prompt, True
    dv.errorTitle, dv.error, dv.showErrorMessage = "Not in the list", "Pick a value from the list.", True
    ws.add_data_validation(dv)
    dv.add(f"{col}{first}:{col}{last}")


def firm_questions(page):
    text = bdv.read(f"domains/{page}/company-questions.md")
    prio, out = None, []
    for block in re.split(r"\n(?=## |### )", text):
        m = re.match(r"## Priority (\d)", block)
        if m:
            prio = int(m.group(1))
            continue
        m = re.match(r"### (\d+)\. (.+)", block)
        if not m:
            continue
        f = dict(re.findall(r"- \*\*([^:*]+):\*\* (.+)", block))
        ref = re.search(r"question (q\d+)", block)
        out.append([int(m.group(1)), prio, plain(m.group(2)), plain(f.get("Why it matters")),
                    plain(f.get("How to answer")), plain(f.get("Concepts affected")),
                    plain(f.get("Who answers")), plain(f.get("Joint question")),
                    None, None, None, ref.group(1) if ref else ""])
    return out


def build(ctx, dom):
    page = dom["Page"]
    pset = {i for i in dom["primary"] if i in ctx.c}
    wb = Workbook()
    wb.properties.creator = "tools/build_question_workbooks.py"
    wb.properties.created = wb.properties.modified = STAMP
    wb.calculation.fullCalcOnLoad = True  # Excel computes the summary on opening

    # Start here
    ws = wb.active
    ws.title = "Start here"
    ws.sheet_view.showGridLines = False
    ws.column_dimensions["A"].width, ws.column_dimensions["B"].width = 30, 100
    title(ws, f"{dom['Domain']}: questions for the domain experts",
          "Business ontology · interview guide generated from the repository")
    r = 4

    def line(label, text, bold=True, fill=False):
        nonlocal r
        a = ws.cell(row=r, column=1, value=label)
        a.font, a.alignment = font(bold=bold), WRAP
        b = ws.cell(row=r, column=2, value=text)
        b.font, b.alignment = font(), WRAP
        if fill:
            b.fill, b.border = PatternFill("solid", fgColor=INPUT), BOX
        ws.row_dimensions[r].height = max(15, 14 * (len(text or "") // 110 + 1))
        r += 1

    def section(text):
        nonlocal r
        r += 1
        ws.cell(row=r, column=1, value=text).font = font(bold=True, size=12, color=TEAL)
        r += 1

    line("Domain owner", dom["Owner role"])
    line("Reviewers", dom["Reviewer roles"])
    line("Review wave", dom["Wave"])
    for label in ("Interviewer", "Expert (name and role)", "Date of the session"):
        line(label, None, fill=True)
    section("How to use this workbook")
    line("Purpose", "Ask the domain's experts how our firm works, so the ontology can be tailored to it. "
         "Start with priority 1: those answers are needed for the pilot agents.")
    line("Keep it inside the firm", "This file in the repository stays blank. Save a copy inside the firm before "
         "filling it in. Answers are firm-specific: they go to the internal records, never into the repository.")
    line("Yellow cells", "Only the yellow cells are filled in. Everything else comes from the ontology.")
    line("Sheet 1", "Questions for our firm: answer, set a status, note any follow-up.")
    line("Sheet 2", "Questions put to each role during the review: notes from the session.")
    line("Sheet 3", "Words with several meanings: does the expert agree with the proposed answer? If not, what is the rule in practice?")
    line("Summary", "Counts what has been asked and answered.")
    section("Example of a filled row (sheet 1, invented)")
    line("Question", "Which give-up statuses do your teams use day to day?")
    line("Answer", "Pending, claimed, rejected, lapsed; 'claimed' means accepted in full.", bold=False)
    line("Status", "Answered", bold=False)
    line("Follow-up", "Check whether partial claims are used at any CCP.", bold=False)

    # 1 Questions for our firm
    ws1 = wb.create_sheet("1 Questions for our firm")
    title(ws1, "1. Questions for our firm", "Fill in a copy kept inside the firm, never the file in the repository.")
    header(ws1, 4, [("#", 5), ("Priority", 8), ("Question", 55), ("Why it matters", 40), ("How to answer", 35),
                    ("Concepts affected", 25), ("Who answers", 22), ("Shared with other domains", 25),
                    ("Answer", 50), ("Status", 13), ("Follow-up", 30), ("Ref", 8)])
    fq = firm_questions(page)
    last1 = max(5, table(ws1, 5, fq, {9, 10, 11}, ref_col=12))
    dropdown(ws1, ["Not asked", "Answered", "Partly answered", "Follow-up needed", "Not applicable"], "J", 5, last1,
             "Where this question stands.")
    ws1.freeze_panes = "D5"
    ws1.auto_filter.ref = f"A4:L{last1}"

    # 2 Questions by role
    ws2 = wb.create_sheet("2 Questions by role")
    title(ws2, "2. Questions put to each role", "From the domain's review sheet.")
    header(ws2, 4, [("#", 5), ("Role", 28), ("Question", 90), ("Notes from the session", 60)])
    rq = [[n, q["Role"], plain(ctx.human(q["Question"])), None]
          for n, q in enumerate(ctx.d["questions"].get(page, []), 1)]
    table(ws2, 5, rq, {4}, ref_col=None)
    ws2.freeze_panes = "C5"

    # 3 Meaning to confirm
    ws3 = wb.create_sheet("3 Meaning to confirm")
    title(ws3, "3. Words with several meanings", "A proposed answer is not a decision until the domain owner confirms it.")
    header(ws3, 4, [("#", 5), ("Word or issue", 22), ("To decide", 40), ("Proposed answer", 70),
                    ("Expert's view", 13), ("Rule in practice, or comment", 45), ("Ref", 10)])
    open_q = [a for a in ctx.d["amb"] if not a["Status"].startswith("Decided")
              and set(re.findall(bdv.CID, a.get("Affected IDs", ""))) & pset]
    mq = [[n, a["Term / issue"], plain(ctx.human(a["Required distinction or decision"])),
           plain(ctx.human(ctx.d["answers"].get(a["ID"], ""))), None, None, a["ID"]]
          for n, a in enumerate(open_q, 1)]
    last3 = max(5, table(ws3, 5, mq, {5, 6}, ref_col=7))
    dropdown(ws3, ["Agree", "Disagree", "Unsure"], "E", 5, last3, "Does the expert agree with the proposed answer?")
    ws3.freeze_panes = "C5"

    # Summary
    ws4 = wb.create_sheet("Summary")
    ws4.sheet_view.showGridLines = False
    title(ws4, "Summary", "Calculated from the entries in sheets 1 and 3.")
    header(ws4, 4, [("Item", 50), ("Count", 12)])
    s1, s3 = "'1 Questions for our firm'", "'3 Meaning to confirm'"
    items = [
        ("Questions for our firm", f"=COUNTA({s1}!C5:C{last1})"),
        ("Priority 1 questions", f"=COUNTIF({s1}!B5:B{last1},1)"),
        ("Answered", f'=COUNTIF({s1}!J5:J{last1},"Answered")'),
        ("Partly answered or follow-up needed",
         f'=COUNTIF({s1}!J5:J{last1},"Partly answered")+COUNTIF({s1}!J5:J{last1},"Follow-up needed")'),
        ("Priority 1 not yet answered",
         f'=COUNTIF({s1}!B5:B{last1},1)-COUNTIFS({s1}!B5:B{last1},1,{s1}!J5:J{last1},"Answered")'
         f'-COUNTIFS({s1}!B5:B{last1},1,{s1}!J5:J{last1},"Not applicable")'),
        ("Meanings to confirm", f"=COUNTA({s3}!B5:B{last3})"),
        ("Meanings where the expert disagrees", f'=COUNTIF({s3}!E5:E{last3},"Disagree")'),
    ]
    for k, (label, formula) in enumerate(items):
        for j, v in enumerate((label, formula), 1):
            c = ws4.cell(row=5 + k, column=j, value=v)
            c.font, c.border, c.alignment = font(), BOX, WRAP

    wb.active = 0
    path = os.path.join(ROOT, "domains", page, FILE)
    wb.save(path)
    freeze(path)
    return path, len(fq), len(rq), len(mq)


def freeze(path):
    """openpyxl stamps the save time; rewrite it, and the zip dates, so an unchanged workbook is byte-identical."""
    with zipfile.ZipFile(path) as z:
        parts = [(i, z.read(i.filename)) for i in z.infolist()]
    stamp = STAMP.strftime("%Y-%m-%dT%H:%M:%SZ")
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
        for info, data in parts:
            if info.filename == "docProps/core.xml":
                data = re.sub(rb"(<dcterms:modified[^>]*>)[^<]*", rb"\g<1>" + stamp.encode(), data)
            info.date_time = STAMP.timetuple()[:6]
            z.writestr(info, data)


def main():
    os.chdir(ROOT)
    ctx = bdv.Ctx(bdv.load())
    total = 0
    for dom in ctx.d["domains"]:
        path, nf, nr, nm = build(ctx, dom)
        total += nf
        print(f"{os.path.relpath(path, ROOT)}: {nf} firm questions, {nr} role questions, {nm} meanings to confirm")
    print(f"{total} firm questions in total")


if __name__ == "__main__":
    main()
