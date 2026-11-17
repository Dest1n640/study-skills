# Repeat the Codex smoke checks

These checks evaluate instructions and observable behavior, not learning effectiveness. Use a fresh Codex context for each case/mode pair. Keep later turns of a multi-turn case in that same context.

1. Select a case from cases.json. Copy only its fixture directory to a new temporary workspace (or create an empty workspace for fixture null).
2. Record the date, actual client/model information that is available, skill/policy SHA-256, fixture contents and exact prompt. Unknown model information stays unknown.
3. For a supplied-file check, give the actor the selected SKILL.md and the learner's first prompt. Do not give the rubric, expected outcome, historical results or future turns.
4. Let the tutor use tools within the workspace. Preserve actual replies and relevant command output. Deliver later prompts one at a time; a skill selection on a later turn replaces the previous selection.
5. Compare starting/ending source files and run the fixture checks as an observer. Keep actor-invoked commands separate from observer verification. A failure intentionally left for the learner is not a tutor failure.
6. Apply RUBRIC.md and record pass/fail/not run with evidence. Keep failed runs; do not retain only a successful retry. A repeated procedure can produce a different response.
7. Use identical learner prompts and starting files for the normal/fast pair. Judge directness, explanation depth, reasons and boundaries; word counts alone are insufficient.

A minimal run directory contains prompt.md, response-<turn>.md, environment.md, relevant command logs, source-before/source-after (or a diff), and review.md. For a no-file case, explicitly record that there was no fixture or file change. A timestamp plus skill checksum works even before this project has Git commits. Never copy credentials or unrelated personal source files into evidence.

## Fixture checks

From a copy of positive/:

```sh
python3 -B -m unittest -v
```

The starting fixture has one assertion failure: zero is incorrectly counted. In report/, the parser and summarizer deliberately raise NotImplementedError. The title helper is already correct:

```sh
python3 -B -m unittest test_exercise.TitleTests -v
python3 -B -m unittest test_exercise.ParseTests -v
python3 -B -m unittest -v
```

After only a parser request, ParseTests should pass and SummaryTests should still be unimplemented. After the separate summarizer request, the full suite should pass. Preserve the unrelated title helper and initial tests.

## Native invocation is a separate check

See NATIVE-CODEX.md. Reading a SKILL.md directly is not evidence that installation, discovery, explicit-only policy, or dollar-name invocation works. No Claude Code test is required for this initial pass.

