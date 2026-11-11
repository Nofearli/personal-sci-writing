# Running checks and understanding limits

Run `python scripts/style_lint.py <file>` from the skill directory. Multiple files are accepted. Supported suffixes include `.md`, `.markdown`, `.txt`, `.tex` and `.latex`. Read input as UTF-8.

`--format json` returns structured issues. `--output <file>` saves the report. Default exit codes are 0 for no hard violations, 1 for hard violations, and 2 for input/configuration errors. `--fail-on warning` also fails on advisory findings. `--fail-on none` only reports.

The checker masks common math environments, inline mathematics, comments, citation/identifier arguments, metadata, code, reference lists and protected quotations without shifting source positions. Visible prose inside normal formatting commands is still checked. It does not expand custom macros or load files referenced by input commands. Inspect unusual syntax manually.

Add an exact case-sensitive proper name or quotation to `allowed_literal_spans` when needed. Use `style-lint: off` and `style-lint: on` markers for protected regions. Markers can be placed inside Markdown or LaTeX comments. Do not place new prose in protected regions to evade checks. Balanced quoted strings are protected by default, so scan raw manuscript text rather than wrapping generated prose in quotation marks.

Edit `language-rules.json` to change restrictions. Soft expressions are initially empty. Passive preference, meaning preservation, novelty and citation support require language-model or human review rather than regular-expression classification.

The public package includes deterministic unit tests and a synthetic rewrite demonstration. Private-corpus analysis and holdout artifacts are intentionally not distributed. Public tests do not constitute a measured style-match accuracy or an independent proof of scientific correctness.
