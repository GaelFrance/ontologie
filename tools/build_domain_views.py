#!/usr/bin/env python3
"""Build the human-readable domain folders from the canonical registers.

Canonical sources (never edited by this script):
  ontology/foundation.md            concept catalogue (all levels)
  ontology/concept-annotations.md   kinds, summaries, examples, aliases, notes, values
  relationships/relationships.md    connections between concepts
  governance/ambiguity-register.md  open questions on meaning, with proposed answers
  governance/decision-log.md        decisions taken
  governance/review-domains.md      domains, owners, reviewers, questions per role
  domains/<page>/overview.md        hand-written introduction to each domain
  domains/<page>/company-questions.md  hand-written questions for the firm

Generated (do not edit by hand):
  domains/README.md, domains/<page>/README.md, domains/<page>/concepts.md,
  domains/<page>/review.md, glossary.md

Usage: python3 tools/build_domain_views.py [--check]
  --check  exit 1 if a generated file is out of date, or if a concept does not have
           exactly one primary domain.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "domains"
ID = r"LD-[CRA]\d{4}"
CID = r"LD-C\d{4}"
MEANING_CHANGED = {"LD-C0003", "LD-C0013", "LD-C0014", "LD-C0022", "LD-C0023", "LD-C0047"}
CANONICAL_IN_DOMAIN = {"overview.md", "company-questions.md"}
GENERATED_IN_DOMAIN = {"README.md", "concepts.md", "review.md"}
EMPTY = (None, "", "—", "-")
STRUCTURE = {"part_of", "step_in", "state_of"}
PILOTS = {"UC-001": "the change-impact use case", "UC-002": "the market-onboarding use case",
          "UC-003": "the give-up use case", "UC-004": "the management-revenue use case",
          "UC-005": "the strategic-intelligence use case", "UC-006": "the operational-status use case",
          "AG-001": "the intelligence publisher agent", "AG-002": "the change-impact agent",
          "AG-003": "the onboarding agent", "AG-004": "the give-up and clearing acceptance agent",
          "AG-005": "the business-performance agent", "AG-006": "the operations agent"}


# --------------------------------------------------------------------------- reading

def cells(line):
    line = line.strip()
    if not line.startswith("|"):
        return None
    parts = re.split(r"(?<!\\)\|", line.strip("|"))
    return [p.strip().replace("\\|", "|") for p in parts]


def tables(text):
    """Yield (header, rows) for every Markdown table in text."""
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        head = cells(lines[i])
        if head and i + 1 < len(lines) and re.match(r"^\|[\s:|-]+\|$", lines[i + 1].strip()):
            rows = []
            i += 2
            while i < len(lines) and cells(lines[i]) is not None:
                rows.append(dict(zip(head, cells(lines[i]))))
                i += 1
            yield head, rows
        else:
            i += 1


def expand(spec):
    """Expand 'LD-C0001, LD-C0003 to LD-C0005' into an ordered list of IDs."""
    ids = []
    for part in re.split(r",\s*", spec or ""):
        part = part.strip()
        m = re.match(r"LD-C(\d{4}) to LD-C(\d{4})$", part)
        if m:
            ids += [f"LD-C{n:04d}" for n in range(int(m.group(1)), int(m.group(2)) + 1)]
        elif re.match(r"^LD-C\d{4}$", part):
            ids.append(part)
    return ids


def read(path):
    p = ROOT / path
    return p.read_text(encoding="utf-8") if p.exists() else ""


def first_id(text):
    m = re.search(CID, text or "")
    return m.group(0) if m else None


def load():
    d = {"concepts": {}, "rels": [], "amb": [], "answers": {}, "notes": {}, "context": {}, "aliases": [],
         "decisions": [], "domains": [], "content": {}, "questions": {}, "parents": {}, "summary": {},
         "values": {}, "flags": {}}
    for head, rows in tables(read("ontology/foundation.md")):
        if "Working business definition" in head:
            for r in rows:
                r.setdefault("Level", "1")
                d["concepts"][r["ID"]] = r
    for head, rows in tables(read("relationships/relationships.md")):
        if "Relation" in head:
            d["rels"] += rows
    amb = read("governance/ambiguity-register.md")
    for head, rows in tables(amb):
        if "Affected IDs" in head:
            d["amb"] += rows
    for m in re.finditer(r"^### (LD-A\d{4})[^\n]*\n(.*?)(?=^### |^## |\Z)", amb, re.M | re.S):
        d["answers"][m.group(1)] = " ".join(m.group(2).split())
    for head, rows in tables(read("ontology/concept-annotations.md")):
        if head[:2] == ["Concept", "Note"]:
            for r in rows:
                d["notes"][first_id(r["Concept"])] = r["Note"]
        elif "Required context" in head:
            for r in rows:
                for c in re.findall(CID, r["Concept"]):
                    d["context"][c] = r["Required context"]
        elif "Resolves to" in head:
            d["aliases"] += rows
        elif head[:2] == ["Child", "Parent"]:
            for r in rows:
                child = first_id(r["Child"])
                link = r.get("Link", "kind of") or "kind of"
                for p in re.findall(CID, r["Parent"]):
                    d["parents"].setdefault(child, []).append((p, link))
        elif "In short" in head:
            for r in rows:
                d["summary"][first_id(r["Concept"])] = r
        elif head[:2] == ["Concept", "Values (draft)"]:
            for r in rows:
                d["values"][first_id(r["Concept"])] = r["Values (draft)"]
        elif "Flag" in head:
            for r in rows:
                d["flags"][first_id(r["Concept"])] = r
    for r in d["rels"]:
        if r.get("Relation") in STRUCTURE:
            src, tgt = first_id(r.get("Source concept")), first_id(r.get("Target concept"))
            if src and tgt:
                d["parents"].setdefault(src, []).append((tgt, r["Relation"].replace("_", " ")))
    for head, rows in tables(read("governance/decision-log.md")):
        if "Affected IDs" in head:
            d["decisions"] += rows
    for head, rows in tables(read("governance/review-domains.md")):
        if "Primary concepts" in head:
            for r in rows:
                r["primary"] = expand(r["Primary concepts"])
                r["shown"] = expand(r.get("Also shown", ""))
                d["domains"].append(r)
        elif "Sequence" in head:
            for r in rows:
                d["content"][r["Page"]] = r
        elif "Question" in head and "Role" in head:
            for r in rows:
                d["questions"].setdefault(r["Page"], []).append(r)
    return d


# --------------------------------------------------------------------------- helpers

def slug(text):
    """GitHub heading anchor."""
    s = text.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s)
    return s.replace(" ", "-")


class Ctx:
    def __init__(self, data):
        self.d = data
        self.c = data["concepts"]
        self.owner = {}
        for dom in data["domains"]:
            for i in dom["primary"]:
                self.owner.setdefault(i, dom)
        self.children = {}
        for child, ps in data["parents"].items():
            for p, link in ps:
                self.children.setdefault(p, []).append((child, link))
        self.amb_term = {a["ID"]: a["Term / issue"] for a in data["amb"]}

    def name(self, i):
        return self.c[i]["Canonical English name"] if i in self.c else i

    def link(self, i, here=None):
        """Markdown link to a concept card, relative to domains/<here>/."""
        if i not in self.c:
            return i
        dom = self.owner.get(i)
        if not dom:
            return self.name(i)
        anchor = slug(self.name(i))
        if here is not None and dom["Page"] == here:
            return f"[{self.name(i)}](#{anchor})"
        prefix = "../" if here is not None else "domains/"
        return f"[{self.name(i)}]({prefix}{dom['Page']}/concepts.md#{anchor})"

    def human(self, text, here=None, links=False):
        """Replace IDs in free text by concept names; keep the text readable."""
        if not text:
            return text
        def name_or_link(i):
            return self.link(i, here) if links else self.name(i)
        for i in set(re.findall(CID, text)):
            if i in self.c:
                text = re.sub(re.escape(self.name(i)) + r"\s*\(" + i + r"\)",
                              lambda m, i=i: name_or_link(i), text, flags=re.I)
        def paren(m):
            ids = re.findall(CID, m.group(0))
            before = m.string[max(0, m.start() - 60):m.start()]
            if all(self.name(i).lower() in before.lower() for i in ids if i in self.c):
                return ""
            return " (" + ", ".join(name_or_link(i) for i in ids) + ")"
        text = re.sub(r"\s*\((?:see )?(?:LD-C\d{4}(?:,\s*|\s+and\s+|\s*/\s*)?)+\)", paren, text)
        text = re.sub(CID, lambda m: name_or_link(m.group(0)), text)
        text = re.sub(r"LD-A\d{4}", lambda m: f"the open question “{self.amb_term.get(m.group(0), m.group(0))}”", text)
        text = re.sub(r"\s*\(?LD-R\d{4}\)?", "", text)
        text = re.sub(r"\b(UC-00\d) / (AG-00\d)\b", lambda m: PILOTS[m.group(2)], text)
        text = re.sub(r"\b(?:UC|AG)-00\d\b", lambda m: PILOTS.get(m.group(0), m.group(0)), text)
        return text

    def summary(self, i, field):
        r = self.d["summary"].get(i, {})
        v = r.get(field, "")
        return "" if v in EMPTY else v


# --------------------------------------------------------------------------- pages

def concept_card(ctx, i, page):
    c = ctx.c[i]
    name = c["Canonical English name"]
    out = [f"### {name}", ""]
    short = ctx.summary(i, "In short")
    if short:
        out += [f"*{ctx.human(short)}*", ""]
    flag = " — *meaning changed in 2026-11, accepted as Draft*" if i in MEANING_CHANGED else ""
    out += [f"**Definition.** {ctx.human(c['Working business definition'], page, links=True)}{flag}", ""]
    for field, label in (("Example", "Example"), ("Not to be confused with", "Not to be confused with")):
        v = ctx.summary(i, field)
        if v:
            out += [f"**{label}.** {ctx.human(v, page, links=True)}", ""]
    ps = ctx.d["parents"].get(i, [])
    if ps:
        groups = {}
        for p, link in ps:
            groups.setdefault(link, []).append(ctx.link(p, page))
        out += [" · ".join(f"**{k.capitalize()}:** {', '.join(v)}" for k, v in groups.items()), ""]
    kids = ctx.children.get(i, [])
    if kids:
        out += ["**Breaks down into:** " + ", ".join(f"{ctx.link(k, page)} ({link})" for k, link in kids), ""]
    if i in ctx.d["values"]:
        out += [f"**Values (draft list):** {ctx.d['values'][i]}", ""]
    al = [a for a in ctx.d["aliases"] if i in re.findall(CID, a.get("Resolves to", ""))]
    if al:
        words = [f"“{a['Alias']}” ({a['Scope']})" if a.get("Scope") not in EMPTY else f"“{a['Alias']}”" for a in al]
        out += ["**Words people use:** " + "; ".join(words), ""]
    if i in ctx.d["notes"]:
        out += [f"**Note.** {ctx.human(ctx.d['notes'][i], page, links=True)}", ""]
    if i in ctx.d["context"]:
        out += [f"**Before using it, know:** {ctx.human(ctx.d['context'][i])}", ""]
    if i in ctx.d["flags"]:
        out += [f"**Caution.** {ctx.human(ctx.d['flags'][i].get('Behaviour expected from agents', ''))}", ""]
    rl = [r for r in ctx.d["rels"] if r.get("Source concept") == i or r.get("Target concept") == i]
    rl = [r for r in rl if r.get("Relation") not in {"is_a"} | STRUCTURE]
    if rl:
        out += ["**Connected to:**", ""]
        outgoing = {o for r in rl if r.get("Source concept") == i for o in re.findall(CID, r.get("Target concept", ""))}
        for r in rl:
            rel = r["Relation"].replace("_", " ")
            src, tgt = r.get("Source concept"), r.get("Target concept")
            other_ids = re.findall(CID, tgt if src == i else src)
            if src != i and set(other_ids) <= outgoing:
                continue
            others = ", ".join(ctx.link(o, page) for o in other_ids) or ctx.human(tgt if src == i else src)
            phrase = f"*{rel}* {others}" if src == i else f"{others} *{rel}* {name}"
            cond = ctx.human(r.get("Meaning and conditions", ""))
            out.append(f"- {phrase}" + (f" — {cond}" if cond not in EMPTY else ""))
        out.append("")
    am = [a for a in ctx.d["amb"] if i in re.findall(CID, a.get("Affected IDs", ""))]
    if am:
        out += ["**Open questions on its meaning:** " + "; ".join(
            f"“{a['Term / issue']}” ({a['Status'].lower()})" for a in am) + " — see the [review sheet](review.md).", ""]
    owner = ctx.owner.get(i)
    level = c.get("Level", "1")
    out += [f"<sub>{c['Proposed type']} · level {level} · Draft · reference {i}"
            + (f" · approved by the {owner['Owner role']}" if owner else "") + "</sub>", ""]
    return out


def tree_lines(ctx, ids, page, depth=0, seen=None):
    seen = seen if seen is not None else set()
    out = []
    for i in ids:
        if i in seen or i not in ctx.c:
            continue
        seen.add(i)
        short = ctx.summary(i, "In short")
        out.append("  " * depth + f"- **{ctx.link(i, page)}**" + (f" — {ctx.human(short)}" if short else ""))
        kids = [k for k, _ in ctx.children.get(i, []) if ctx.owner.get(k) is ctx.owner.get(i)]
        out += tree_lines(ctx, kids, page, depth + 1, seen)
    return out


def roots(ctx, ids):
    """Concepts of a domain whose parent is not in the same domain, in domain order."""
    s = set(ids)
    return [i for i in ids if not any(p in s for p, _ in ctx.d["parents"].get(i, []))]


def render_readme(ctx, dom):
    page = dom["Page"]
    content = ctx.d["content"].get(page, {})
    ov = read(f"domains/{page}/overview.md")
    paras = [p for p in ov.split("\n\n") if p.strip() and not p.lstrip().startswith("#")]
    intro = paras[0].strip() if paras else ""
    n_q = len(re.findall(r"^### ", read(f"domains/{page}/company-questions.md"), re.M))
    out = [f"# {dom['Domain']}", "",
           "> Generated by `tools/build_domain_views.py`; edit `overview.md`, `company-questions.md` or the registers instead.", ""]
    if intro:
        out += [intro, ""]
    out += ["| Read | What you will find |", "|---|---|"]
    if ov:
        out.append("| [Overview](overview.md) | The domain in plain words: what it covers, how it works, what to keep apart |")
    out.append(f"| [Concepts](concepts.md) | {len(dom['primary'])} concepts, each with a definition, an example and what not to confuse it with |")
    out.append("| [Review sheet](review.md) | What each reviewer is asked, open questions on meaning, decisions already taken |")
    if n_q:
        out.append(f"| [Questions for our firm](company-questions.md) | {n_q} questions that capture how our firm works in this domain |")
    out += ["", f"**Owner:** {dom['Owner role']}  ", f"**Reviewers:** {dom['Reviewer roles']}  ",
            f"**Review wave:** {dom['Wave']}", ""]
    if content.get("Why it matters") not in EMPTY:
        out += [f"**Why it matters:** {ctx.human(content['Why it matters'])}", ""]
    if content.get("Sequence") not in EMPTY:
        out += ["## How it flows", "", ctx.human(content["Sequence"], page, links=True).replace("](#", "](concepts.md#"), ""]
    out += ["## Concepts at a glance", ""]
    out += [l.replace("](#", "](concepts.md#") for l in tree_lines(ctx, roots(ctx, dom["primary"]), page)]
    if dom["shown"]:
        out += ["", "Also relevant here, owned by another domain: "
                + ", ".join(ctx.link(i, page) for i in dom["shown"] if i in ctx.c) + "."]
    out.append("")
    return "\n".join(out)


def render_concepts(ctx, dom):
    page = dom["Page"]
    out = [f"# {dom['Domain']} — concepts", "",
           "> Generated by `tools/build_domain_views.py` from the registers. Every definition is Draft. "
           "To propose a change, tell the domain owner or the Ontology Lead; you do not need GitHub.", "",
           "Concepts are grouped by family: a broad concept first, then the kinds or parts it breaks down into.", ""]
    order, seen = [], set()
    def walk(i):
        if i in seen or i not in ctx.c:
            return
        seen.add(i)
        order.append(i)
        for k, _ in ctx.children.get(i, []):
            if ctx.owner.get(k) is dom:
                walk(k)
    for r in roots(ctx, dom["primary"]):
        walk(r)
    for i in dom["primary"]:
        walk(i)
    out += ["**Contents:** " + " · ".join(f"[{ctx.name(i)}](#{slug(ctx.name(i))})" for i in order), ""]
    for i in order:
        out += concept_card(ctx, i, page)
    return "\n".join(out)


def render_review(ctx, dom):
    page = dom["Page"]
    primary = [i for i in dom["primary"] if i in ctx.c]
    shown = [i for i in dom["shown"] if i in ctx.c]
    pset, allset = set(primary), set(primary) | set(shown)
    content = ctx.d["content"].get(page, {})
    out = [f"# {dom['Domain']} — review sheet", "",
           "> Generated by `tools/build_domain_views.py`. Reviewers answer in plain language, in writing or in a meeting; GitHub is optional.", "",
           f"**Owner (approves the concepts in section 1):** {dom['Owner role']}  ",
           f"**Reviewers:** {dom['Reviewer roles']}  ",
           f"**Review wave:** {dom['Wave']}  ",
           f"**Concepts:** {len(primary)} to approve, {len(shown)} shown for context, all Draft", ""]
    if content.get("Scope note") not in EMPTY:
        out += [f"**Scope:** {ctx.human(content['Scope note'])}", ""]
    out += ["## What you are asked to review", ""]
    for q in ctx.d["questions"].get(page, []):
        out.append(f"- **{q['Role']}:** {ctx.human(q['Question'])}")
    out += ["- **Everyone:** for each concept in section 1, is the definition **correct**, **complete** and "
            "**worded the way your teams use it**? Write *OK*, *Change* (say what) or *Unsure*. "
            "Is a concept your area relies on **missing**, or one **unnecessary**? The [concept cards](concepts.md) give examples.",
            "- **Everyone:** for each open question in section 3, do you **agree with the proposed answer**? If not, what is the rule in practice?",
            "- How *our* firm works goes in the [questions for our firm](company-questions.md), never in the definitions. "
            "Mention internal terms or system names only in your reply, never in this repository.", "",
            "## 1. Concepts you approve", "", "| Concept | Definition | Your verdict |", "|---|---|---|"]
    for i in primary:
        c = ctx.c[i]
        flag = " ⚠️ *meaning changed 2026-11*" if i in MEANING_CHANGED else ""
        lvl = " *(level 2)*" if c.get("Level", "1") == "2" else ""
        out.append(f"| **{ctx.link(i, page).replace('](#', '](concepts.md#')}**{lvl} | {ctx.human(c['Working business definition'])}{flag} | |")
    if shown:
        out += ["", "## 2. Concepts owned elsewhere: check them from your angle", "",
                "| Concept | Approved in | Definition | Your comment |", "|---|---|---|---|"]
        for i in shown:
            o = ctx.owner.get(i)
            where = f"[{o['Domain']}](../{o['Page']}/review.md)" if o else "—"
            out.append(f"| **{ctx.link(i, page)}** | {where} | {ctx.human(ctx.c[i]['Working business definition'])} | |")
    full = [a for a in ctx.d["amb"] if set(re.findall(CID, a.get("Affected IDs", ""))) & pset]
    brief = [a for a in ctx.d["amb"] if a not in full and set(re.findall(CID, a.get("Affected IDs", ""))) & allset]
    if full or brief:
        out += ["", "## 3. Open questions on meaning", "",
                "A proposed answer comes from the expert review; it is **not a decision** until the owner confirms it.", ""]
        for a in full:
            out += [f"### {a['Term / issue']} ({a['Status']})", "",
                    f"**To decide:** {ctx.human(a['Required distinction or decision'])}", "",
                    f"**Proposed answer:** {ctx.human(ctx.d['answers'].get(a['ID'], '—'))}", "",
                    f"<sub>reference {a['ID']}</sub>", ""]
        if brief:
            out += ["Also touching this domain, answered elsewhere:", ""]
            for a in brief:
                pages = {}
                for i in re.findall(CID, a.get("Affected IDs", "")):
                    o = ctx.owner.get(i)
                    if o:
                        pages[o["Page"]] = o
                out.append(f"- “{a['Term / issue']}” ({a['Status'].lower()}): see "
                           + ", ".join(f"[{p['Domain']}](../{k}/review.md)" for k, p in sorted(pages.items())))
            out.append("")
    keys = pset | {a["ID"] for a in full}
    dc = [x for x in ctx.d["decisions"] if set(re.findall(ID, x.get("Affected IDs", ""))) & keys]
    if dc:
        out += ["## 4. Decisions already taken", "", "| Decision | What it means for the ontology |", "|---|---|"]
        for x in dc:
            out.append(f"| **{x['Point']}** — {ctx.human(x['Decision'])} | {ctx.human(x['Consequence in the ontology'])} |")
        out.append("")
    if content.get("Not yet in the catalogue") not in EMPTY:
        out += ["## 5. Not yet in the catalogue", "",
                "These items are in the backlog. **Does a decision you need now depend on one of them?**", ""]
        out += [f"- {b.strip()}" for b in content["Not yet in the catalogue"].split(";")]
        out.append("")
    return "\n".join(out)


def render_glossary(ctx):
    out = ["# Glossary", "",
           "> Generated by `tools/build_domain_views.py`. Every concept of the ontology, A to Z, with the domain that owns it.", ""]
    names = sorted(ctx.c, key=lambda i: ctx.name(i).lower())
    letter = None
    for i in names:
        n = ctx.name(i)
        if n[0].upper() != letter:
            letter = n[0].upper()
            out += ["", f"## {letter}", ""]
        o = ctx.owner.get(i)
        short = ctx.summary(i, "In short") or ctx.human(ctx.c[i]["Working business definition"])
        out.append(f"- **{ctx.link(i)}** — {ctx.human(short)}" + (f" *({o['Domain']})*" if o else ""))
    al = sorted(ctx.d["aliases"], key=lambda a: a["Alias"].lower())
    if al:
        out += ["", "## Words people use", "", "Informal words and abbreviations, and the concept they point to.", ""]
        for a in al:
            targets = ", ".join(ctx.link(i) for i in re.findall(CID, a.get("Resolves to", ""))) or ctx.human(a.get("Resolves to", ""))
            scope = f" ({a['Scope']})" if a.get("Scope") not in EMPTY else ""
            out.append(f"- “{a['Alias']}”{scope} → {targets}")
    out.append("")
    return "\n".join(out)


def render_index(ctx):
    out = ["# Domains", "",
           "> Generated by `tools/build_domain_views.py`. Do not edit by hand.", "",
           "The ontology is organised in ten business domains. Each domain has a folder with an overview in plain words, "
           "concept cards, a review sheet for its reviewers and the questions that capture how our firm works.", "",
           "| Domain | Owner | Review wave | Concepts |", "|---|---|---|---|"]
    for dom in ctx.d["domains"]:
        out.append(f"| [{dom['Domain']}]({dom['Page']}/README.md) | {dom['Owner role']} | {dom['Wave']} | {len(dom['primary'])} |")
    out += ["", f"Each of the {len(ctx.c)} concepts belongs to exactly one domain, whose owner approves it. "
            "A concept can also appear on other domains' review sheets for comment. "
            "The [glossary](../glossary.md) lists every concept A to Z.", ""]
    return "\n".join(out)


# --------------------------------------------------------------------------- main

def build():
    data = load()
    ctx = Ctx(data)
    errors, count = [], {}
    for dom in data["domains"]:
        for i in dom["primary"]:
            count[i] = count.get(i, 0) + 1
        both = set(dom["primary"]) & set(dom["shown"])
        if both:
            errors.append(f"{dom['Page']}: both primary and also shown: {', '.join(sorted(both))}")
    missing = sorted(set(ctx.c) - set(count))
    multiple = sorted(i for i, n in count.items() if n > 1)
    used = set(count).union(*(set(dom["shown"]) for dom in data["domains"]))
    unknown = sorted(used - set(ctx.c))
    for p in sorted((set(data["content"]) | set(data["questions"])) - {dom["Page"] for dom in data["domains"]}):
        errors.append(f"page content or questions for an unknown page: {p}")
    if missing:
        errors.append(f"concepts without a primary domain: {', '.join(missing)}")
    if multiple:
        errors.append(f"concepts with more than one primary domain: {', '.join(multiple)}")
    if unknown:
        errors.append(f"domain IDs not in the catalogue: {', '.join(unknown)}")
    files = {"domains/README.md": render_index(ctx), "glossary.md": render_glossary(ctx)}
    for dom in data["domains"]:
        p = dom["Page"]
        files[f"domains/{p}/README.md"] = render_readme(ctx, dom)
        files[f"domains/{p}/concepts.md"] = render_concepts(ctx, dom)
        files[f"domains/{p}/review.md"] = render_review(ctx, dom)
    return files, errors, data


def stale(files, data):
    """Generated files that exist on disk but are no longer produced."""
    pages = {dom["Page"] for dom in data["domains"]}
    out = [p for p in OUT.glob("*.md") if p.name != "README.md"]
    for d in OUT.iterdir() if OUT.exists() else []:
        if d.is_dir():
            for f in d.glob("*.md"):
                if f.name in GENERATED_IN_DOMAIN and (d.name not in pages):
                    out.append(f)
    return out


def main():
    files, errors, data = build()
    if "--check" in sys.argv:
        for f, text in files.items():
            p = ROOT / f
            if not p.exists() or p.read_text(encoding="utf-8") != text:
                errors.append(f"{f} is out of date; run tools/build_domain_views.py")
        for p in stale(files, data):
            errors.append(f"{p.relative_to(ROOT)} is no longer generated; delete it")
        for e in errors:
            print("ERROR", e)
        sys.exit(1 if errors else 0)
    for p in stale(files, data):
        p.unlink()
    for f, text in files.items():
        p = ROOT / f
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text, encoding="utf-8")
    for e in errors:
        print("ERROR", e)
    print(f"{len(files)} files written ({len(data['domains'])} domains, glossary, index)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
