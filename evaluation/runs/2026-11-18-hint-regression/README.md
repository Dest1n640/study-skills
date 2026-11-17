# Hint regression, 18 November 2026

Four fresh native Codex CLI contexts used matched fixtures and learner request wording. The control used the pre-change skill from Git; revised cases explicitly clarified that an implementation request does not end hint mode. Model identity was not reported; default local client configuration was used. See each environment.json, skill/policy snapshot, prompt, command, response and observer check.

| Run | Observation | Evidence |
| --- | --- | --- |
| control-normal | source preserved | [reply](control-normal/response.md), [diff](control-normal/diff.patch), [events](control-normal/events.jsonl) |
| revised-fast | source preserved | [reply](revised-fast/response.md), [diff](revised-fast/diff.patch), [events](revised-fast/events.jsonl) |
| revised-normal-1 | fail: target edited | [reply](revised-normal-1/response.md), [diff](revised-normal-1/diff.patch), [events](revised-normal-1/events.jsonl) |
| revised-normal-2 | source preserved | [reply](revised-normal-2/response.md), [diff](revised-normal-2/diff.patch), [events](revised-normal-2/events.jsonl) |

The original-version control preserved files this time, while one revised normal run edited them and another preserved them. This does not establish the cause or demonstrate a reliable improvement. The candidate wording was withdrawn from product SKILL.md; its exact content is retained in the run snapshots. Historical failures remain valid evidence. Unrelated local third-party skill outputs in events were omitted.

A separate [read-only experiment](readonly-probe/observation.txt) tests a runtime permission boundary, not a capability of SKILL.md. It is not installed into user settings.

Read-only observation: the runtime-limited probe preserved source/tests, reproduced the expected assertion failure and returned guidance. This one run does not establish general reliability or prove that an attempted write was blocked. Command and actual events are retained. Enabling this runtime restriction as a product workflow is awaiting a user decision.
