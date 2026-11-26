#!/usr/bin/env python3
"""Merge two versions of a questions-for-experts.xlsx workbook, answer by answer.

Git cannot merge Excel files: when two experts change the same domain workbook on
their own computers, the second one to send their work gets a conflict. This
script merges the cells experts fill in (answer, status, follow-up, answered by,
session notes, expert's view and comment, and the cover sheet), using the common
earlier version to see who changed what:

- a cell changed on one side only takes that change;
- a cell changed on both sides to different values keeps both, marked
  "CONFLICT", and the script exits with status 1 so that the person resolves it
  in Excel (search for CONFLICT) before committing.

Git runs it by itself once each computer has registered it (once per clone):
  git config merge.expert-answers.name "Merge expert answers in Excel workbooks"
  git config merge.expert-answers.driver "python3 tools/merge_answers.py %O %A %B"
The .gitattributes file already routes domains/*/questions-for-experts.xlsx to it.

It can also be run by hand:
  python3 tools/merge_answers.py BASE.xlsx OURS.xlsx THEIRS.xlsx
which writes the merged workbook over OURS.xlsx.
"""
import os
import shutil
import sys
import tempfile

from openpyxl import load_workbook

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_question_workbooks import CARRY, START_INPUTS, previous_entries, row_key  # noqa: E402

MARK = "CONFLICT"


def flatten(entries):
    """{(sheet, key, col): value} from previous_entries() output."""
    flat = {}
    for sheet, rows in entries.items():
        if sheet == "Start here":
            for label, value in rows.items():
                flat[(sheet, label, 2)] = value
            continue
        for key, cols in rows.items():
            for col, value in cols.items():
                flat[(sheet, key, col)] = value
    return flat


def merge(base, ours, theirs):
    """Return (merged cells, list of conflicts)."""
    merged, conflicts = {}, []
    for cell in set(base) | set(ours) | set(theirs):
        b, o, t = base.get(cell), ours.get(cell), theirs.get(cell)
        if o == t or t == b:
            value = o
        elif o == b:
            value = t
        else:
            value = f"{MARK} - this version: {o if o is not None else '(empty)'} | " \
                    f"other version: {t if t is not None else '(empty)'}"
            conflicts.append(cell)
        merged[cell] = value
    return merged, conflicts


def write(path, merged):
    """Write merged input cells into the workbook at path; return cells that found no row."""
    wb = load_workbook(path)
    placed = set()
    if "Start here" in wb.sheetnames:
        for row in wb["Start here"].iter_rows(min_col=1, max_col=2):
            cell = ("Start here", row[0].value, 2)
            if row[0].value in START_INPUTS:
                row[1].value = merged.get(cell)
                placed.add(cell)
    for sheet, (_, inputs) in CARRY.items():
        if sheet not in wb.sheetnames:
            continue
        ws = wb[sheet]
        for r in range(5, ws.max_row + 1):
            vals = [ws.cell(row=r, column=c).value for c in range(1, 15)]
            if vals[0] is None:
                continue
            key = row_key(sheet, vals)
            for col in inputs:
                cell = (sheet, key, col)
                ws.cell(row=r, column=col).value = merged.get(cell)
                placed.add(cell)
    wb.save(path)
    return [c for c, v in merged.items() if c not in placed and v not in (None, "")]


def main(argv):
    if len(argv) != 3:
        raise SystemExit(__doc__)
    base_path, ours_path, theirs_path = argv
    # Git hands over temporary files without the .xlsx extension that openpyxl requires.
    with tempfile.TemporaryDirectory() as tmp:
        copies = []
        for name, path in (("base", base_path), ("ours", ours_path), ("theirs", theirs_path)):
            copy = os.path.join(tmp, name + ".xlsx")
            shutil.copyfile(path, copy)
            copies.append(copy)
        base = flatten(previous_entries(copies[0])) if os.path.getsize(copies[0]) else {}
        ours = flatten(previous_entries(copies[1]))
        theirs = flatten(previous_entries(copies[2]))
        merged, conflicts = merge(base, ours, theirs)
        lost = write(copies[1], merged)
        shutil.copyfile(copies[1], ours_path)
    for sheet, key, col in conflicts:
        where = key if isinstance(key, str) else " / ".join(key)
        print(f"{MARK}: sheet '{sheet}', question {where}, column {col}: both versions changed it", file=sys.stderr)
    for sheet, key, col in lost:
        where = key if isinstance(key, str) else " / ".join(key)
        print(f"Not placed: sheet '{sheet}', question {where}: the question is missing from this version; "
              f"value to copy by hand: {merged[(sheet, key, col)]}", file=sys.stderr)
    if conflicts or lost:
        print("Open the workbook in Excel, resolve the cells marked CONFLICT, save, then commit.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
