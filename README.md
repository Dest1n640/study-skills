# Study skills

[Русское описание](README.ru.md)

Four explicitly selected programming-learning skills for learners at any experience level. Choose help with an approach, implementation, review, or walkthrough.

| Skill | How it helps |
| --- | --- |
| `study-hint` | Gives hints at your chosen pace. You write the assignment code and tests. |
| `study-guide` | Explains approaches and implements concrete parts you request at your chosen pace. |
| `study-review` | Reviews existing code, explains findings with evidence, and gives hints for fixes you make yourself. |
| `study-trace` | Follows one concrete input through existing code, with source locations and a diagram when it clarifies the route. |

Hint allows pseudocode for the current step, syntax examples, and materially different small examples. It does not provide or edit the target implementation. Guide first turns "do the whole assignment" into a plan. You may request specific parts in sequence, so it may eventually write all the code. Guide checks your understanding only when you ask.

Review looks at correctness, readability, architecture, and performance. It uses the scope you name, or reviews current changes when you leave the scope open. With no changes, it reviews the whole available project. For example, it can point to a predicate that counts zero as positive, show the failing input, and suggest checking how the boundary value enters the count. Asking for a ready fix gives you a more specific hint. Choose an implementation mode explicitly when you want it to write the fix.

Trace follows the behavior you name or starts with a compact project map and a clear main route. In the [order exercise](evaluation/fixtures/trace/README.md), it can follow `A7 2` from argument parsing in `cli.py`, through pricing in `orders.py`, to a stored order and a total of `300`. Ask to zoom in on any step. Trace checks important transitions locally when possible and says what the run observed. A walkthrough leaves the code and tests as they are. Trace applies a scoped repair when you ask for one and the session permits writes.

All modes read relevant project files, run suitable available checks, and respond in your language. Hint and guide focus on the code you are working on and explain how the task requirements affect the choice of tools, algorithms, data structures, and patterns. They compare viable approaches and use an example, pseudocode, or a flowchart to clarify difficult steps.

## Install

Requires [Node.js 22.20 or later](https://github.com/vercel-labs/skills#install-a-skill). Run these commands from your programming project directory; skills are installed to that project by default.

Install one skill from [Dest1n640/study-skills](https://github.com/Dest1n640/study-skills) for Codex once this revision is published:

```sh
npx skills add Dest1n640/study-skills --agent codex --skill study-hint --yes
```

Install the full set for Codex once this revision is published:

```sh
npx skills add Dest1n640/study-skills --agent codex \
  --skill study-hint study-guide study-review study-trace \
  --yes
```

These commands use the [Skills CLI](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#skills-add); `--yes` skips installer confirmation prompts. To install for Claude Code, replace `--agent codex` with `--agent claude-code`. To install a different single mode, replace `study-hint` with its name from the table above.

The interactive alternative is `npx skills add Dest1n640/study-skills`. Choose your agent and the available `study-*` skills you want to use. Explicit selection keeps the `openspec-*` development helpers out of the tutoring install.

Run the following from this checkout. To install into a different project, run the command there and replace `.` with the absolute path to this checkout.

```sh
npx skills add . --agent codex --skill study-hint
npx skills add . --agent codex --skill study-review
npx skills add . --agent codex --skill study-trace
npx skills add . --agent codex --skill study-hint study-guide study-review study-trace
```

See [evaluation results](evaluation/RESULTS.md) for local Codex installation and behavior checks. Remote installation of this revision remains unverified. Restart or refresh skill discovery as required by your agent.

## Use

When you start hint or guide, choose **Quick** or **Detailed** using the client’s choice control or a text menu. If you already ask for a pace, the skill starts immediately. Quick gives the next step with a short reason. Detailed explains the reasoning and uses an example when helpful. The pace stays active in the chat until you change it or switch skills.

Codex examples follow.

```text
$study-hint Help me understand why my sliding window fails on repeated characters.
$study-guide Keep it brief. Implement only the validation helper and explain the important decisions.
$study-review Review my parser changes and give me hints for addressing the findings.
$study-trace Follow the arguments A7 2 from the CLI through order submission.
```

Claude Code uses slash invocations, for example `/study-trace`. It has not been tested. Explicit-only selection is configured with `agents/openai.yaml` for Codex and `disable-model-invocation: true` for Claude Code. Other agents may interpret these extensions differently.

Choose another study skill explicitly to change mode, or say that you are ending study mode.

## Upgrade from the previous skill names

| Old skill | New skill | Pace |
| --- | --- | --- |
| `study-hint-normal` | `study-hint` | Detailed |
| `study-hint-fast` | `study-hint` | Quick |
| `study-guide-normal` | `study-guide` | Detailed |
| `study-guide-fast` | `study-guide` | Quick |

From your project directory, remove the old copies. This removes those four names for all agents in that project.

```sh
npx skills remove study-hint-normal study-hint-fast study-guide-normal study-guide-fast --yes
```

Then install `study-hint` and `study-guide` using the install commands above. For previously global installations, add `--global` to both the remove and install commands.

## Scope and status

The files use the open [Agent Skills format](https://agentskills.io/specification). Codex is the initial behavioral evaluation target; see [evaluation scenarios](evaluation/SCENARIOS.md) and [results](evaluation/RESULTS.md). Claude Code and other clients are not behaviorally tested or installation-certified.

These are instructions for an assistant, not a technical barrier. Passing program tests does not prove that the learner understands. No quizzes, learning profiles, XP, persistent progress tracking, or spaced-repetition scheduler are required. Original project materials are licensed under MIT.

## Inspiration

Independently written instructions informed by examining [TuTor](https://github.com/kevinnio/tutor), [programming-tutor](https://github.com/cdmorozov/claude-tutors), [Think Before Code](https://github.com/Far-200/think-before-code), and [ai-socratic-tutor](https://github.com/bstellato/ai-teaching-skills). Their implementations and licenses remain separate. No third-party tutoring skill text is bundled. OpenSpec development-helper notices are retained separately.

## License

[MIT](LICENSE), Copyright (c) 2026 Dest1n640. Each product skill includes its own LICENSE copy for independent installation. Upstream development-helper notices are retained in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md); external materials retain their own terms.
