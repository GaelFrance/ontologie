#!/usr/bin/env python3
"""One-time setup of a clone of this repository on a new computer.

Registers the Git merge driver that merges the shared expert workbooks answer by
answer (tools/merge_answers.py; see .gitattributes), and checks that openpyxl is
installed. Run it once, from the repository folder, after cloning:

  python3 tools/setup_computer.py
"""
import subprocess
import sys


def git(*args):
    subprocess.run(["git", *args], check=True)


def main():
    git("config", "merge.expert-answers.name", "Merge expert answers in Excel workbooks")
    git("config", "merge.expert-answers.driver", f'"{sys.executable.replace(chr(92), "/")}" tools/merge_answers.py %O %A %B')
    print("Registered the merge driver for the expert workbooks.")
    try:
        import openpyxl  # noqa: F401
        print("openpyxl is installed.")
    except ImportError:
        print("openpyxl is missing: run  python3 -m pip install openpyxl")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
