# Repeat the Codex smoke checks

These checks evaluate instructions and observable behavior, not learning effectiveness. Use a fresh Codex context for each case/mode pair. Keep later turns of a multi-turn case in that same context.

1. Select a case from cases.json. Copy only its fixture directory to a new temporary workspace (or create an empty workspace for fixture null).
2. Record the date, actual client/model information that is available, skill/policy SHA-256, fixture contents and exact prompt. Unknown model information stays unknown.
3. For a supplied-file check, give the actor the selected SKILL.md and the learner's first prompt. Do not give the rubric, expected outcome, historical results or future turns.
4. Let the tutor use tools within the workspace. Preserve actual replies and relevant command output. Deliver later prompts one at a time; a skill selection on a later turn replaces the previous selection.
5. Compare starting/ending source files and run the fixture checks as an observer. Keep actor-invoked commands separate from observer verification. A failure intentionally left for the learner is not a tutor failure.
6. Apply RUBRIC.md and record pass/fail/not run with evidence. Keep failed runs; do not retain only a successful retry. A repeated procedure can produce a different response.
7. For a case with a `paces` list, run the same `modes` entry once per pace in a fresh context and add only “Быстрый темп.” or “Подробный темп.” before the first prompt. Judge directness, explanation depth, reasoning, and authorship. Cases without `paces` use the prompts as written.

Use the case's `expected` field as a reviewer-only criterion. For a native run, prefix turns with the dollar-name in `select` if it is absent from the prompt. For a supplied-file opening, provide the initial skill once. Then resume the same session and send the later prompts as written. The non-interactive CLI exercises the text menu.

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

## Review case setup

- For `commit-fixture`, initialize Git in the isolated workspace and commit only the copied fixture files. The clean starting worktree drives the whole-project case. Install native skills after this step and locally exclude `.agents/` and `skills-lock.json` from the fixture diff.
- For `positive-worktree-regression`, start with the `positive` fixture, replace `value >= 0` with `value > 0` in `exercise.py`, initialize Git, and commit the implementation and tests. Restore `exercise.py` from the original fixture as an unstaged change. Check that it is the only changed fixture file before starting Codex.
- In `review/`, `python3 -B -m unittest -v` passes the count check, fails the zero case, and errors when publishing uses a field absent from the test store. The repeated scan and the eligibility predicate also support source-based performance and readability findings.
- For a native `review-lifecycle` run, prefix the first case prompt with `$study-review`. Resume by its reported session ID in a writable sandbox for the remaining prompts. The final prompt already contains the explicit selection. Save each turn's output and snapshots before the next turn.

## Native invocation is a separate check

For trace, use the order CLI project or the two independent commands in `trace-choice/`. The order project's starting suite has one passing test with a substitute store and one failing test for zero quantity. After the requested writable repair, verify that the only source change is the quantity condition and both tests pass. For a supplied-file case with follow-up, resume the same session and keep the original skill active.

For `trace-main`, install trace alone and explicitly invoke it in Codex. For `trace-hint-switch`, start a fresh `read-only` session with approvals disabled and the full set installed. Send the first turn as plain text. On subsequent turns prefix the prompt with the dollar-name in the case's `select` field and resume in the same read-only session. Check client injection evidence, the session settings, and before and after source snapshots.

For `pace-menu-switch`, use the current full set and keep the same read-only session, including when activating guide. The menu and follow-ups use that session's capabilities. Check for separate native hint and guide injections and preserve the verification output and file snapshots.

See NATIVE-CODEX.md. Reading a SKILL.md directly is not evidence that installation, discovery, explicit-only policy, or dollar-name invocation works. No Claude Code test is required for this initial pass.

