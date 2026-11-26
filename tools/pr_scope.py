#!/usr/bin/env python3
"""Say who must approve and who may merge the changes of a branch.

Compares the current branch with the main branch and lists:
- the domains touched: through their folder, or through concept IDs on changed
  lines of the registers (the concept's primary domain; domains where it is
  "also shown" are listed for comment);
- shared files (tools, agent setup, domain classification, decision log, list
  of owners and experts, documentation).

Rule (docs/governance.md, "Who merges"): domain owners merge. If one domain is
touched, its owner approves and merges; if several are, each owner concerned
approves first and then any of them merges. Shared files (tools, agent setup,
classification, documentation) are flagged so the weekly report shows them to
the Ontology Lead.

Usage: python3 tools/pr_scope.py [BASE]    BASE defaults to origin/main, then main
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import build_domain_views as bdv  # noqa: E402

REGISTERS = ("ontology/foundation.md", "ontology/concept-annotations.md", "relationships/relationships.md",
             "governance/ambiguity-register.md", "governance/open-questions-for-owner.md")
GENERATED = re.compile(r"^(glossary\.md|domains/README\.md|domains/[^/]+/(README|concepts|review)\.md)$")
LEAD_ONLY = re.compile(r"^(tools/|\.agents/|\.opencode/|\.roo|\.gitattributes|\.gitignore|AGENTS\.md|README\.md"
                       r"|docs/|governance/(review-domains|decision-log|experts|governance-model-proposal)\.md)")
ANYONE = {"CHANGELOG.md"}


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, check=True, capture_output=True, text=True).stdout


def duplicate_ids():
    """IDs that start more than one row of the catalogue, relationships or ambiguity register."""
    seen, dup = set(), []
    for path in ("ontology/foundation.md", "relationships/relationships.md", "governance/ambiguity-register.md"):
        for m in re.finditer(r"^\| (LD-[CRA]\d{4}) \|", bdv.read(path), re.M):
            if m.group(1) in seen:
                dup.append(m.group(1))
            seen.add(m.group(1))
    return dup


def base_ref(argv):
    for ref in argv[:1] or ["origin/main", "main"]:
        if subprocess.run(["git", "rev-parse", "--verify", "-q", ref], cwd=ROOT, capture_output=True).returncode == 0:
            return ref
    raise SystemExit("No base branch found; pass it, for example: python3 tools/pr_scope.py main")


def domain_maps(data):
    primary, shown, owner = {}, {}, {}
    for dom in data["domains"]:
        owner[dom["Page"]] = dom["Owner role"]
        for c in dom["primary"]:
            primary[c] = dom["Page"]
        for c in dom["shown"]:
            shown.setdefault(c, set()).add(dom["Page"])
    return primary, shown, owner


def classify(since, until=None, data=None):
    """Sort the changes between two commits by domain.

    Returns (files, touched {domain: set of where}, comment {domain}, lead [files], unknown [notes])."""
    span = [since] + ([until] if until else [])
    files = [f for f in git("diff", "--name-only", *span).splitlines() if f]
    primary, shown, _ = domain_maps(data or bdv.load())
    touched, comment, lead, unknown = {}, set(), [], []
    for f in files:
        if f in ANYONE or GENERATED.match(f):
            continue
        if LEAD_ONLY.match(f):
            lead.append(f)
            continue
        m = re.match(r"domains/([^/]+)/", f)
        if m:
            touched.setdefault(m.group(1), set()).add(f)
            continue
        if f in REGISTERS:
            ids = set()
            for line in git("diff", "--unified=0", *span, "--", f).splitlines():
                if line[:1] in "+-" and not line.startswith(("+++", "---")):
                    ids |= set(re.findall(bdv.CID, line))
            for c in sorted(ids):
                if c in primary:
                    touched.setdefault(primary[c], set()).add(f"{f} ({c})")
                    comment |= shown.get(c, set())
                else:
                    unknown.append(f"{f} ({c}: new concept, no primary domain yet)")
            continue
        lead.append(f)
    return files, touched, comment - set(touched), lead, unknown


def main(argv):
    os.chdir(ROOT)
    base = base_ref(argv)
    since = git("merge-base", base, "HEAD").strip()
    data = bdv.load()
    _, _, owner = domain_maps(data)
    files, touched, comment, lead, unknown = classify(since, data=data)
    dup = duplicate_ids()
    print(f"Changes on this branch since {base}: {len(files)} file(s)\n")
    if dup:
        print("STOP: these IDs are used by more than one row; renumber the new ones with tools/next_ids.py "
              "before merging: " + ", ".join(dup) + "\n")
    if not files:
        return 1 if dup else 0
    for page, where in sorted(touched.items()):
        print(f"Domain {page} (owner: {owner.get(page, 'unknown')}):")
        for w in sorted(where):
            print(f"  {w}")
    if comment:
        print("\nAlso shown in, owners to comment: " + ", ".join(sorted(comment)))
    if unknown:
        print("\nNew concepts (each needs a primary domain in governance/review-domains.md):")
        for f in unknown:
            print(f"  {f}")
    if lead:
        print("\nShared files (tools, agent setup, classification, documentation):")
        for f in lead:
            print(f"  {f}")
    print()
    if len(touched) <= 1 and not comment:
        who = f"the owner of {next(iter(touched))}" if touched else "any domain owner"
        print(f"Verdict: {who} may approve and merge.")
    else:
        names = sorted(set(touched) | comment)
        print(f"Verdict: the owners of {', '.join(names)} approve; then any of them merges.")
    if lead:
        print("Shared files changed: say so in the pull request; the weekly report lists them for the Ontology Lead.")
    return 1 if dup else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
