## Why

Learners need a way to open existing code and follow what actually happens to a concrete input, whether they wrote the code, an agent wrote it, or they inherited it. A source-linked walkthrough makes it possible to return to the relevant lines and follow the program independently.

## What Changes

- **Confirmed** — Add `study-trace` as a standalone, explicitly selected skill for reading existing code. Follow a stated goal when supplied. For an unscoped or whole-project request, inspect the project, show a compact map, and begin the main route when it is clear. Ask one focused question when several comparable routes are plausible.
- **Confirmed** — Show the selected route end to end, then expand any step on request. Follow the same input, object, or event through calls, branches, and data changes. Use diagrams when they clarify the route. Start with source and use suitable local checks for important or uncertain transitions.
- **Confirmed** — A direct repair request in trace permits fixing the indicated problem and the necessary related code within the client's permissions. Explain and verify the changed route. `study-review` belongs to a separate change.
- **Proposed defaults** — Ship one trace variant. Include it in the bilingual skill selection and installation instructions. Use the project's existing Codex evaluation approach.

## Capabilities

### New Capabilities

- `code-tracing` — Select a meaningful route through existing code, explain it with source and execution evidence, and handle explicitly requested repairs in place.

### Modified Capabilities

- `study-modes` — Include trace in the explicitly selected study modes and their switching behavior.
- `distribution-validation` — Make trace independently installable and include it in the full product installation selection.

## Impact

- `skills/study-trace/` gains the standalone skill, client metadata, and MIT license.
- `README.md` and `README.ru.md` document the use case, invocation, and installation selection.
- `evaluation/` gains repeatable cases and scoped Codex evidence for trace.
