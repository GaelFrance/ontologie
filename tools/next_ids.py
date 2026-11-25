#!/usr/bin/env python3
"""Print the next free concept, relationship and ambiguity IDs.

IDs are never reused, so the next free ID is one above the highest ID that
appears anywhere in the repository's Markdown files (registers, decision log,
change log, generated pages), including retired ones.

Usage: python3 tools/next_ids.py [--count N]
  --count N  list the next N free IDs of each kind (default 1).
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KINDS = {"C": "concept", "R": "relationship", "A": "ambiguity"}


def highest():
    top = {k: 0 for k in KINDS}
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        for kind, num in re.findall(r"LD-([CRA])(\d{4})", path.read_text(encoding="utf-8")):
            top[kind] = max(top[kind], int(num))
    return top


def main(argv):
    count = 1
    if "--count" in argv:
        count = int(argv[argv.index("--count") + 1])
    top = highest()
    for kind, label in KINDS.items():
        ids = ", ".join(f"LD-{kind}{top[kind] + n:04d}" for n in range(1, count + 1))
        print(f"{label:<13} highest LD-{kind}{top[kind]:04d}  next {ids}")


if __name__ == "__main__":
    main(sys.argv[1:])
