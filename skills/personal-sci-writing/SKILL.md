---
name: personal-sci-writing
description: Draft, rewrite, or review English SCI manuscript prose in the author's personal style, emphasizing Abstracts, Introduction contribution logic, impersonal voice, and configurable lexical restrictions. Also update the style profile from newly authorized papers. Use for personal-style manuscript work rather than generic translation or literature retrieval.
---

# Personal SCI Writing

Preserve scientific content and apply the personal rhetorical profile. This public distribution contains structural templates and preferences. Private source papers and original quotations are not included.

## Hard constraints

- Read [language-rules.json](language-rules.json) every invocation. Explicit user rules override historical usage and other writing defaults.
- In new or rewritten English manuscript prose, exclude the configured exact lexical forms. Initial bans are `which`, `while`, `i.e.`, `namely`, `due to`, `associated with`, `corresponds`, `we`, `our`, `us`, and the semicolon. Match case-insensitively at lexical boundaries. Do not extend a ban to every inflection without instruction.
- Prefer grammatical passives and clear nonhuman subjects. Active subjects such as `This paper`, `The proposed method`, and `The results` are allowed.
- Preserve equations, variables, quantifiers, assumptions, inequalities, units, data, citation identities and guarantee strength. Necessary and sufficient conditions are distinct. A candidate strategy does not establish global optimality.
- Preserve quoted evidence, proper names, reference titles and mathematics. Identify conflicts rather than silently editing protected material.
- Do not create results, citations or novelty claims. Every literature comparison needs actual support for the new manuscript.

## Route by task

Select Writing, Rewriting, Review or Learning Mode and identify the target section.

- Abstract: [references/abstract.md](references/abstract.md).
- Introduction, literature, gaps and contributions: [references/introduction.md](references/introduction.md).
- Models, methods, theory, results and conclusions: [references/sections.md](references/sections.md).
- Lexical rewriting: [references/language.md](references/language.md). Search [references/phrase-bank.json](references/phrase-bank.json) by function.
- Profile provenance and boundaries: [references/style-profile.md](references/style-profile.md).
- New authorized papers: [references/learning.md](references/learning.md).
- Running checks and handling protected material: [references/usage.md](references/usage.md).

## Workflow

1. Extract supplied facts and claim boundaries. Identify missing information before making a substantive claim.
2. Choose an appropriate section pattern. Abstract length is flexible. Group literature by technical issue and prefer concrete contribution-first comparisons.
3. Draft or rewrite using templates as structural guidance. Keep citations attached to the same claims and preserve all technical qualifiers.
4. Check against the source facts. Resolve lexical conflicts by restructuring clauses instead of substituting arbitrary synonyms.
5. Run `python <skill-dir>/scripts/style_lint.py <manuscript> --format json`. Fix hard violations and rerun. Treat length and repetition as advisory.
6. Independently review voice, technical meaning, gap-to-contribution alignment, novelty scope and citation support. The linter cannot establish these properties.

Writing/Rewriting Mode returns clean prose with any unresolved factual dependency identified. Review Mode returns anchored findings and suggested edits. Learning Mode preserves old evidence and hard rules, and produces a proposed change report before activating evidence-based changes. Never return unfilled template slots as finished manuscript text.
