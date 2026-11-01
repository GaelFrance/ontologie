# Registers

These files are the single source of truth behind the human pages in [`domains/`](../domains/README.md). They are written as Markdown tables so that tools can read them and people can still check them. Reviewers do not need to open them: the domain pages show the same content, by name.

| Register | Holds |
|---|---|
| [`foundation.md`](foundation.md) | The catalogue: one row per concept with its reference, name, type and definition. Level 1 = foundation, level 2 = the more detailed concepts of the 2026-11 domain review |
| [`concept-annotations.md`](concept-annotations.md) | Kinds of concepts, plain-language summaries and examples, words people use, usage notes, required context, value lists, priorities and standard alignments to verify |
| [`../relationships/relationships.md`](../relationships/relationships.md) | How concepts connect (including "part of", "step in" and "state of") |
| [`../governance/ambiguity-register.md`](../governance/ambiguity-register.md) | Open questions on meaning, with proposed answers |
| [`../governance/review-domains.md`](../governance/review-domains.md) | Which domain owns each concept, who reviews it, and what reviewers are asked |
| [`../governance/decision-log.md`](../governance/decision-log.md) | Decisions taken by the sponsor |

After any change to a register, run `python3 tools/build_domain_views.py` to regenerate the domain pages and the glossary, and `python3 tools/build_domain_views.py --check` before proposing the change. References (`LD-C`, `LD-R`, `LD-A`) are permanent: never reuse or renumber one.
