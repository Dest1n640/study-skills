# Native Codex invocation checklist

## Consolidated hint and guide

- [x] Non-interactive CLI loaded the installed `study-hint` and presented the text pace menu.
- [x] The same session resumed the pending request, carried the selected pace into a follow-up, and accepted an explicit pace change.
- [x] The same session loaded `study-guide` after explicit selection and preserved the fixture under the existing read-only permissions.
- [ ] Interactive discovery and the button menu.
- [ ] Ending study mode and a native switch that also changes the client's permission policy.

[Run evidence](runs/2026-11-21-consolidated-tutoring/README.md) identifies the native injection events, exact prompts, and observed changes.

## Historical pace-specific skills

Status: partial; see [native results](runs/2026-11-17/native-codex/README.md). Supplied-file evaluations do not satisfy this checklist.

Use an isolated project where only the four product modes have been installed. Record Codex/Skills CLI versions, the installed file set and policy-file contents.

- [ ] A fresh conversation with no study selection does not implicitly activate a study mode.
- [x] $study-hint-normal is discovered and actually invoked. (Invocation only; see behavior results.)
- [x] $study-hint-fast is discovered and actually invoked. (Invocation only; see behavior results.)
- [x] $study-guide-normal is discovered and actually invoked. (Invocation only; see behavior results.)
- [ ] $study-guide-fast is discovered and actually invoked.
- [ ] Explicit selection switches hint to guide and guide back to hint.
- [ ] Explicitly ending study mode removes its preference.

For each check retain the exact request, relevant client events (including a skill-load event when available), actual reply and observed file changes. Do not infer discovery just from the assistant saying it used a mode.

If the available interface cannot exercise a check, leave it not run with a reason. Installation file checks can pass independently. Do not change global agent settings or claim Claude Code coverage.


The invocation checklist above records the historical 17 November checks. The permission-bound hint workflow approved on 18 November is evaluated separately under runs/2026-11-18-hint-regression/. Full interactive resume/switching remains unverified.

## Study review on 19 November 2026

- [x] A one-skill Codex project explicitly loaded `study-review` and reviewed the sample with its files preserved.
- [x] In a writable Codex session, review stayed active through requests for ready code and a file edit, and the fixture remained unchanged.
- [x] In that same session, explicit `study-guide-fast` replaced review and only the requested comparison changed.

This sequence used non-interactive CLI resume. The [review run records](runs/2026-11-19-study-review/README.md) identify both native skill injections and the per-turn source snapshots.

## Study trace on 19 November 2026

- [x] A one-skill Codex project explicitly loaded `study-trace` and traced its principal route.
- [x] A fresh session with the full selection produced no skill injection for the plain first request.
- [x] Explicit `study-hint-fast` and `study-trace` selections loaded on their respective turns in the same read-only session. The requested repair preserved the source and tests.

The [trace run records](runs/2026-11-19-study-trace/README.md) contain the per-turn client settings, skill injections, commands, and file snapshots.
