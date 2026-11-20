# Study skills

[Русское описание](README.ru.md)

Six explicitly selected programming-learning skills for learners at any experience level. Choose help with an approach, implementation, review, or walkthrough.

| Skill | How it helps |
| --- | --- |
| `study-hint-normal` | Asks about your idea and offers gradual hints. You write the assignment code. |
| `study-hint-fast` | Gives direct, compact hints. You write the assignment code. |
| `study-guide-normal` | Explains approaches and implements concrete parts you request. |
| `study-guide-fast` | Helps implement requested parts with concise explanations. |
| `study-review` | Reviews existing code, explains findings with evidence, and gives hints for fixes you make yourself. |
| `study-trace` | Follows one concrete input through existing code, with source locations and a diagram when it clarifies the route. |

Hint allows pseudocode for the current step, syntax examples, and materially different small examples. It does not provide or edit the target implementation. Guide first turns "do the whole assignment" into a plan. You may request specific parts in sequence, so it may eventually write all the code. Guide checks your understanding only when you ask.

Review looks at correctness, readability, architecture, and performance. It uses the scope you name, or reviews current changes when you leave the scope open. With no changes, it reviews the whole available project. For example, it can point to a predicate that counts zero as positive, show the failing input, and suggest checking how the boundary value enters the count. Asking for a ready fix gives you a more specific hint. Choose an implementation mode explicitly when you want it to write the fix.

Trace follows the behavior you name or starts with a compact project map and a clear main route. In the [order exercise](evaluation/fixtures/trace/README.md), it can follow `A7 2` from argument parsing in `cli.py`, through pricing in `orders.py`, to a stored order and a total of `300`. Ask to zoom in on any step. Trace checks important transitions locally when possible and says what the run observed. A walkthrough leaves the code and tests as they are. Trace applies a scoped repair when you ask for one and the session permits writes.

All modes read relevant project files, run suitable available checks, and respond in your language. Hint and guide compare applicable approaches and adapt their explanations. Their fast variants give shorter, more direct help with the same authorship rules.

## Install

Requires [Node.js 22.20 or later](https://github.com/vercel-labs/skills#install-a-skill). Run these commands from your programming project directory; skills are installed to that project by default.

Install one skill from [Dest1n640/study-skills](https://github.com/Dest1n640/study-skills) for Codex:

```sh
npx skills add Dest1n640/study-skills --agent codex --skill study-hint-normal --yes
```

Install the full set for Codex once this revision is published:

```sh
npx skills add Dest1n640/study-skills --agent codex \
  --skill study-hint-normal study-hint-fast study-guide-normal study-guide-fast study-review study-trace \
  --yes
```

These commands use the [Skills CLI](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#skills-add); `--yes` skips installer confirmation prompts. To install for Claude Code, replace `--agent codex` with `--agent claude-code`. To install a different single mode, replace `study-hint-normal` with its name from the table above.

The interactive alternative is `npx skills add Dest1n640/study-skills`. Choose your agent and the available `study-*` skills you want to use. Explicit selection keeps the `openspec-*` development helpers out of the tutoring install.

For local installation from this checkout:

```sh
npx skills add . --agent codex --skill study-review
npx skills add . --agent codex --skill study-trace
npx skills add . --agent codex --skill study-hint-normal study-hint-fast study-guide-normal study-guide-fast study-review study-trace
```

See [evaluation results](evaluation/RESULTS.md) for local Codex installation and behavior checks. Remote installation of this revision remains unverified. Restart or refresh skill discovery as required by your agent.

## Use

Codex examples:

```text
$study-hint-normal Help me understand why my sliding window fails on repeated characters.
$study-guide-normal Explain the viable approaches. Then help me implement the parser part.
$study-hint-fast I am stuck on the loop invariant. Give me a direct hint.
$study-guide-fast Implement only the validation helper and explain the important decisions.
$study-review Review my parser changes and give me hints for addressing the findings.
$study-trace Follow the arguments A7 2 from the CLI through order submission.
```

Claude Code uses slash invocations, for example `/study-trace`. It has not been tested. Explicit-only selection is configured with `agents/openai.yaml` for Codex and `disable-model-invocation: true` for Claude Code. Other agents may interpret these extensions differently.

Choose another study skill explicitly to change mode, or say that you are ending study mode.

## Scope and status

The files use the open [Agent Skills format](https://agentskills.io/specification). Codex is the initial behavioral evaluation target; see [evaluation scenarios](evaluation/SCENARIOS.md) and [results](evaluation/RESULTS.md). Claude Code and other clients are not behaviorally tested or installation-certified.

These are instructions for an assistant, not a technical barrier. Passing program tests does not prove that the learner understands. No quizzes, learning profiles, XP, persistent progress tracking, or spaced-repetition scheduler are required. Original project materials are licensed under MIT.

## Inspiration

Independently written instructions informed by examining [TuTor](https://github.com/kevinnio/tutor), [programming-tutor](https://github.com/cdmorozov/claude-tutors), [Think Before Code](https://github.com/Far-200/think-before-code), and [ai-socratic-tutor](https://github.com/bstellato/ai-teaching-skills). Their implementations and licenses remain separate. No third-party tutoring skill text is bundled. OpenSpec development-helper notices are retained separately.

## License

[MIT](LICENSE), Copyright (c) 2026 Dest1n640. Each product skill includes its own LICENSE copy for independent installation. Upstream development-helper notices are retained in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md); external materials retain their own terms.
