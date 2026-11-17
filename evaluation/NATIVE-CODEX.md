# Native Codex invocation checklist

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

