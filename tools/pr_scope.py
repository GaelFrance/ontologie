#!/usr/bin/env python3
"""Say who must approve and who may merge the changes of a branch.

Compares the current branch with the main branch and lists:
- the domains touched: through their folder, or through concept IDs on changed
  lines of the registers (the concept's primary domain; domains where it is
  "also shown" are listed for comment);
- the files only the Ontology Lead changes (tools, agent setup, domain
  classification, decision log, list of experts and owners, documentation).

Rule (docs/governance.md): if exactly one domain is touched and no Ontology Lead
file, that domain's owner may merge; otherwise every listed owner approves and
the Ontology Lead merges.

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


def main(argv):
    os.chdir(ROOT)
    base = base_ref(argv)
    since = git("merge-base", base, "HEAD").strip()
    files = [f for f in git("diff", "--name-only", since).splitlines() if f]
    data = bdv.load()
    primary, shown = {}, {}
    owner = {}
    for dom in data["domains"]:
        owner[dom["Page"]] = dom["Owner role"]
        for c in dom["primary"]:
            primary[c] = dom["Page"]
        for c in dom["shown"]:
            shown.setdefault(c, set()).add(dom["Page"])

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
            diff = git("diff", "--unified=0", since, "--", f)
            ids = set()
            for line in diff.splitlines():
                if line[:1] in "+-" and not line.startswith(("+++", "---")):
                    ids |= set(re.findall(bdv.CID, line))
            for c in sorted(ids):
                if c in primary:
                    touched.setdefault(primary[c], set()).add(f"{f} ({c})")
                    comment |= shown.get(c, set())
                else:
                    unknown.append(f"{f} ({c} has no primary domain yet)")
            continue
        lead.append(f)

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
    comment -= set(touched)
    if comment:
        print("\nAlso shown in, owners to comment: " + ", ".join(sorted(comment)))
    if lead or unknown:
        print("\nOntology Lead files or decisions:")
        for f in lead + unknown:
            print(f"  {f}")
    print()
    if len(touched) == 1 and not lead and not unknown:
        page = next(iter(touched))
        extra = " after the owners listed for comment have commented" if comment else ""
        print(f"Verdict: the owner of {page} may approve and merge{extra}.")
    elif not touched and not lead and not unknown:
        print("Verdict: only the change log changed; any domain owner may merge.")
    else:
        names = ", ".join(sorted(touched)) or "none"
        print(f"Verdict: owners of {names} approve; the Ontology Lead merges.")
    return 1 if dup else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
