## Why

Learners need to know where existing code fails and how to investigate a fix they will implement themselves. An educational review gives them evidence and a usable next step for code they wrote, received from an agent, or inherited.

## What Changes

- **Confirmed** — Add an explicitly selected `study-review` skill. Review the requested scope when provided, otherwise review the current changes or the entire available project when there are no changes.
- **Confirmed** — Review correctness, readability, architecture, and performance by default. Explain a bug's location and cause directly, show a concrete counterexample, and give a hint toward the fix.
- **Confirmed** — Keep implementation and tests under learner authorship in review. A request for a ready fix gets a more specific hint. The learner explicitly selects a mode that permits implementation to get a ready fix.
- **Proposed defaults** — Ship one review variant, order findings by impact, and report the limits of the actual review. Follow the existing bilingual documentation and Codex evaluation practices.

## Capabilities

### New Capabilities

- `educational-code-review` — Select a review scope, ground and prioritize findings, and guide learner-authored repairs.

### Modified Capabilities

- `study-modes` — Define explicit selection and persistence for the educational review mode.
- `distribution-validation` — Include the review skill in individual and full product installation selections.

## Impact

- `skills/study-review/` gains the standalone skill, client metadata, and MIT license.
- `README.md`, `README.ru.md`, and `evaluation/` gain review usage, installation, and repeatable behavior checks.
- `add-study-trace` has a separate walkthrough contract. Both changes touch full installation selection, which needs reconciliation when the second delta is synced or archived.
