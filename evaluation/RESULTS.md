# Evaluation results

Date: 2026-11-17. These are small Codex-agent smoke tests, not a study of learning effectiveness.

## Method

Fresh independent Codex agents read a selected SKILL.md and responded to a learner request. File-based cases used isolated temporary Python projects. The coordinator inspected responses and resulting files. This tests instruction behavior when the skill is supplied directly; it does not test native discovery or installation.

## Observed behavior

| Mode and request | Observation |
| --- | --- |
| hint-normal: fix a function that counts zero as positive | Read code and existing test, reproduced the failure, explained the comparison; implementation stayed unchanged and no replacement code was supplied. |
| hint-fast: no starting idea, deadline, request for full longest-unique-substring pseudocode | Compared baseline and sliding-window approaches, gave an input trace and current-step pseudocode; did not supply full pseudocode or target code. |
| guide-fast: implement only a comma-separated integer parser | Implemented the parser and explained split/int behavior; all 3 existing tests passed. The separate report function remained unimplemented. No comprehension quiz. |
| guide-normal: do the whole expense-analysis assignment | Compared aggregation choices and proposed a plan without creating files or implementing the whole assignment. No comprehension quiz. |

Initial hint-normal and guide-normal replies unnecessarily quoted internal skill rules. The instructions were tightened to use ordinary teaching language. A focused hint follow-up and a fresh guide-normal run then avoided internal-rule quotations while preserving their boundaries.

Five independent agent sessions and one follow-up response were used. This is limited evidence. Switching modes, experienced learners across different languages, analogous-example boundaries, tool failures, browser use, and normal-versus-fast on identical prompts remain untested.

## Metadata

All four files parse as YAML with matching folder/name values and Claude explicit-only settings. All four Codex agents/openai.yaml files parse and set allow_implicit_invocation to false. README local links resolve.

The bundled skill-creator quick_validate.py does not recognize Claude's disable-model-invocation extension. Its core validation passed on temporary copies with only that extension removed. The actual skill files retain the extension, checked separately as a YAML boolean. This is not a claim that the unmodified bundled validator accepted the original files.

At the time of the historical tests above, no installation, native Codex skill-discovery test, Claude Code run, other-agent run, GitHub publication, or educational-effectiveness study had been performed. A release license has not yet been selected.

## Subsequent checks on 2026-11-17

Eight supplied-file Codex smoke runs, including multi-turn cases, retain prompts, responses, file snapshots and checks under [runs/2026-11-17](runs/2026-11-17/PAIR-COMPARISON.md). The matched normal/fast comparison and its limits are documented there. These checks are not proof of reliable future behavior.

[Local installation](runs/2026-11-17/installation/verification.txt) with Skills CLI 1.9.0 selected exactly the four product skills in an isolated project; the CLI found ten skills in the source. Remote GitHub installation is not tested.

Native Codex revealed a material failure: two `study-hint-normal` invocations edited the learner's source; the first was observed reading its rule. See [response](runs/2026-11-17/native-codex/study-hint-normal-response.md) and [events](runs/2026-11-17/native-codex/study-hint-normal-events.jsonl). `study-hint-fast` preserved the file in its run, but quoted an internal rule despite the instruction to avoid it. The same change's [task list](../openspec/changes/close-contract-and-evaluation-gaps/tasks.md) tracks the unresolved correction and follow-up. Native switching and ending study mode remain unverified.

Claude Code, publication, remote installation, and educational effectiveness remain untested.


## 18 November 2026: attempted hint correction

[Controlled native checks](runs/2026-11-18-hint-regression/README.md) tested an explicit hint-contract clarification. The original control preserved the source; one of two revised normal runs edited it, the other preserved it. Revised fast preserved it. The candidate wording was withdrawn from the product because improvement was not demonstrated. The cause of the intermittent violation remains unconfirmed.

A separate read-only runtime probe preserved the fixture and gave guidance. It is not automatically enabled by SKILL.md and does not enforce chat-output boundaries. A change to the product launch workflow requires a user decision; task 4.1 remains open.
