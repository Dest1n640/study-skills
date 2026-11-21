## Context

See [proposal.md](proposal.md) for the motivation. The repository currently packages four independent hint and guide variants and tracks their project-local copies. Each pair shares an authorship contract and differs mainly in pace. The installed skill files and client metadata are the product surface. The existing evaluation distinguishes direct skill-file checks from native invocation and preserves the observed file changes.

## Goals / Non-Goals

Ship self-contained tutoring skills and keep pace in the conversation context. The scope is the two basic tutoring skills, their packaging, public documentation, and evaluation. Review and trace keep their own contracts. Client permissions remain the source of filesystem enforcement.

## Decisions

1. **Select the skill explicitly and resolve pace within it.** Keep the existing explicit-invocation metadata. On activation, check for a clear pace in the request before offering two choices. Use a choice tool if the active client exposes one. A numbered text prompt with the same labels is the portable fallback. Hold the original task in the conversation until the learner picks. Scope persistence to the current activation, including when the conversation moves to a new coding question. Use the new invocation's pace when the learner switches to another tutoring skill. Treat a one-off request such as “say this more simply” as an adjustment to that explanation. A request such as “go faster from now on” changes the ongoing pace.
2. **Put authorship and verification in the shared part of each skill's own instructions.** Define Quick and Detailed only for directness, clarification, and explanation depth. Quick foregrounds the usable next step and gives its main reason and material constraints. Detailed can show a concrete example and the reasoning that leads to the recommendation. Preserve read-only Codex launch guidance in hint and write-permission requirements in guide, following the current documentation decision about where those instructions live.
3. **Explain the choice through the immediate task.** Identify the relevant requirement and code, then explain one concrete consequence before naming or expanding on the underlying theory. Read callers, tests, or domain definitions when they affect the current question. For a meaningful design choice, compare a small set of valid options against the same constraints, including a simple baseline when useful. For a branch, use a compact flowchart showing the condition and outcomes. For a state update, use a concrete value or small pseudocode fragment. Keep the hint representation within its existing authorship contract. A text diagram is a portable fallback when diagram rendering is unavailable.
4. **Replace old names in the same release as the documentation update.** The two new packages have their own `SKILL.md`, `agents/openai.yaml`, and license, as the current packages do. The migration table maps `*-fast` to Quick and `*-normal` to Detailed in the corresponding new skill. Remove legacy packages from both source and the tracked local install. Refresh product entries in `skills-lock.json` with the repository's existing installer workflow. Keep the current development helpers and preserve archived specs and run records as historical evidence.

## Risks / Trade-offs

- An installed client may expose no choice tool or fail to render a diagram. Use the text forms and test the menu behavior separately from native discovery.
- A concise response can lose the reason that makes a hint reusable. Compare the same prompt in both paces and check the reason, assumptions, and edge cases alongside brevity.
- An overly detailed flowchart can reveal a complete solution. Test an explicit request for a whole-assignment flowchart in hint and inspect the actual diagram and surrounding answer.
- A prior installation may still expose old names after new skills are added. Document removal at the scope previously used, then check the documented replacement in an isolated install. Keep migration steps explicit about local versus published source and report what was exercised.

## Migration Plan

1. Create and validate `study-hint` and `study-guide` using the four existing files as the source of their contracts.
2. Replace the tracked packages and project-local installs in one change alongside bilingual documentation and the current evaluation references. Verify the complete current set and an individual skill install from the checkout.
3. An existing learner replaces their old installed copies at the same project or global scope, then invokes the new skill at the equivalent pace. To return to the old names, install from the previous revision and use that revision's instructions.
