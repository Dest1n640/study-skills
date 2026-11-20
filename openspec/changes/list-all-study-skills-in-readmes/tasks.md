## 1. README skill tables

- [ ] 1.1 Verify the table at the top of `README.md` and `README.ru.md` against the names in `skills/*/SKILL.md`. Correct any discrepancies in place. Confirm both two-column tables have exactly one row per product skill in the same order and that each localized description agrees with the skill's behavior.
- [ ] 1.2 Confirm each README introduction states the correct skill count and each full-set installation command selects exactly the names in the table. Verify the documented invocation examples for `study-review` and `study-trace`, the local Markdown links, and `git diff --check -- README.md README.ru.md`.

Planning note. Both READMEs already have working-copy edits from the review and trace changes. Preserve those edits and reuse the existing tables where they meet the checks. This documentation change uses `skip_specs: true`. The conditional design artifact is omitted because the change concerns only the contents of two Markdown tables and associated documentation consistency.
