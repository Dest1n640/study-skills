# Study trace evaluation on 19 November 2026

The [tested skill](skill.md) and [Codex policy](policy.yaml) match the checkout. Skills CLI 1.9.0 installed trace alone and the six-skill product set in separate isolated Codex projects. Both selections matched the source bytes for skill, policy, and license. [Installation record](installation.json)

Codex CLI 0.169.1 ran five [cases](../../cases.json) across nine turns. Each run record retains the exact prompts and commands, session settings, tool observations, and file snapshots. The fixture's starting failure for zero quantity is intentional.

| Case | Result | Evidence |
| --- | --- | --- |
| Native trace alone | Pass. The client loaded the installed skill. The first answer mapped the project, diagrammed its main route, and followed `A7 2` across argument parsing, pricing, storage, and the CLI result. The fixture stayed unchanged. | [Answer](trace-main/response-1.md) · [Run](trace-main/run.json) |
| Comparable routes | Pass. The supplied skill inspected the two commands and asked one focused choice between them. | [Answer](trace-choice/response-1.md) · [Run](trace-choice/run.json) |
| Named route and follow-up | Pass. The supplied skill traced `A7 2`, linked significant transitions, and distinguished observed assertions about the stub response from the source-derived payload. The follow-up expanded the storage call for the same input. | [Route](trace-explicit/response-1.md) · [Follow-up](trace-explicit/response-2.md) · [Run](trace-explicit/run.json) |
| Writable repair | Pass. The supplied skill first traced the unexpected `201` for zero without changing files. A direct repair request changed only the quantity condition in `orders.py`. Both tests passed. The answer explained the early `422` before storage, and an independent CLI run also checked that positive orders still work. | [Before](trace-repair/response-1.md) · [After](trace-repair/response-2.md) · [Run](trace-repair/run.json) |
| Explicit switch in read-only Codex | Pass. The first plain request produced a walkthrough without a native skill injection. The client injected hint on turn 2 and trace on turn 3 in the same read-only session. The final reply reported the permission limit and checked the proposed condition in memory. The file snapshots and Git status stayed unchanged. | [Plain request](trace-hint-switch/response-1.md) · [Hint](trace-hint-switch/response-2.md) · [Trace](trace-hint-switch/response-3.md) · [Run](trace-hint-switch/run.json) |

Native injection evidence is extracted from the client session records and checked against the exact installed files. Supplied-file runs load the tested instructions by path. The checks cover these cases in Codex. Publication of this revision, remote installation, other-client behavior, and learning outcomes remain unverified.
