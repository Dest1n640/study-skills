# Study skills

[Русское описание](README.ru.md)

Four explicitly selected programming-learning skills for learners at any experience level. Learn how to choose an approach and implement it with help that fits the current obstacle.

| Skill | How it helps |
| --- | --- |
| `study-hint-normal` | Asks about your idea and offers gradual hints. You write the assignment code. |
| `study-hint-fast` | Gives direct, compact hints. You write the assignment code. |
| `study-guide-normal` | Explains approaches and implements concrete parts you request. |
| `study-guide-fast` | Helps implement requested parts with concise explanations. |

Hint allows pseudocode for the current step, syntax examples, and materially different small examples. It does not provide or edit the target implementation. Guide first turns "do the whole assignment" into a plan. You may request specific parts in sequence, so it may eventually write all the code. Guide checks your understanding only when you ask.

All modes read relevant project files and run available existing checks. They compare applicable approaches, explain why a method fits, and adapt explanation depth from the conversation. Tutors respond in your language. Fast changes explanation length and directness, not authorship permissions.

## Install

This is a local draft, not a published package. After publication, replace `OWNER/REPO` with the actual GitHub repository:

```sh
npx skills add OWNER/REPO --agent codex --skill study-hint-normal study-hint-fast study-guide-normal study-guide-fast
```

The [Skills CLI](https://github.com/vercel-labs/skills) selects only the four product skills with this command. To choose another supported client, change the agent selection. Use its current prerequisites and supported-agent list. No custom installer is included.

The shorter interactive alternative is `npx skills add OWNER/REPO`: select only the four `study-*` names. This repository also contains `openspec-*` development helpers; do not select those for tutoring or use `--all` to install the product.

For local installation from this checkout:

```sh
npx skills add . --agent codex --skill study-hint-normal study-hint-fast study-guide-normal study-guide-fast
```

The explicit four-skill selection was tested locally with Codex in an isolated project; remote installation remains untested. Restart or refresh skill discovery as required by your agent. See [results](evaluation/RESULTS.md) for a native hint-mode failure.

## Use

Codex examples:

```text
$study-hint-normal Help me understand why my sliding window fails on repeated characters.
$study-guide-normal Explain the viable approaches. Then help me implement the parser part.
$study-hint-fast I am stuck on the loop invariant. Give me a direct hint.
$study-guide-fast Implement only the validation helper and explain the important decisions.
```

Claude Code uses slash invocations, for example `/study-hint-normal`. It has not been tested. Explicit-only selection is configured with `agents/openai.yaml` for Codex and `disable-model-invocation: true` for Claude Code. Other agents may interpret these extensions differently.

Choose another study skill explicitly to change mode, or say that you are ending study mode.

## Scope and status

The files use the open [Agent Skills format](https://agentskills.io/specification). Codex is the initial behavioral evaluation target; see [evaluation scenarios](evaluation/SCENARIOS.md) and [results](evaluation/RESULTS.md). Claude Code and other clients are not behaviorally tested or installation-certified.

These are instructions for an assistant, not a technical barrier. Passing program tests does not prove that the learner understands. No quizzes, learning profiles, XP, persistent progress tracking, or spaced-repetition scheduler are required. Original project materials are licensed under MIT.

## Inspiration

Independently written instructions informed by examining [TuTor](https://github.com/kevinnio/tutor), [programming-tutor](https://github.com/cdmorozov/claude-tutors), [Think Before Code](https://github.com/Far-200/think-before-code), and [ai-socratic-tutor](https://github.com/bstellato/ai-teaching-skills). Their implementations and licenses remain separate. No third-party tutoring skill text is bundled. OpenSpec development-helper notices are retained separately.


## Protected hint sessions in Codex

For work on assignment files, start a read-only session and then explicitly select a hint skill:

```sh
codex --cd /path/to/project --sandbox read-only --ask-for-approval never
```

```text
$study-hint-normal
```

Both hint modes use the same launch settings. A SKILL.md cannot change client permissions. Without the client restriction, hint is only a behavioral instruction and has been observed editing files. Read-only does not enforce what code appears in chat.

To keep the chat while moving to guide, exit using `/quit`, then resume that session with its ID (replace SESSION_ID and the project path):

```sh
codex resume SESSION_ID --cd /path/to/project --sandbox workspace-write --ask-for-approval on-request
```

Then explicitly select `$study-guide-normal` or `$study-guide-fast`. To return to protected hint, quit and resume the same ID with `--sandbox read-only --ask-for-approval never`, then select a hint skill. Changing the skill alone does not change permissions. The CLI flags were checked locally; the full interactive resume sequence has not been exercised.

## License

[MIT](LICENSE), Copyright (c) 2026 Dest1n640. Each product skill includes its own LICENSE copy for independent installation. Upstream development-helper notices are retained in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md); external materials retain their own terms.
