## Context

The four existing modes are self-contained Markdown skills. They use client-specific metadata for explicit selection and retain the selected preference across turns. Trace adds a route that may span files, may depend on runtime configuration, and can be revisited after a requested fix. See [proposal](proposal.md) and the [code-tracing delta](specs/code-tracing/spec.md).

## Goals / Non-Goals

**Goals**

- Make each trace usable for opening the source and continuing the investigation independently.
- Keep the skill usable with the reader's existing repository tools and session permissions.

**Non-Goals**

- A separate review workflow, persistent project maps, and a visualization or instrumentation runtime belong outside this change.

## Decisions

### Keep trace independently selectable

Use one English `SKILL.md`, `agents/openai.yaml` with explicit-only selection, and the existing MIT license pattern. One entry point fits the agreed overview and on-demand depth. The normal and fast variants in hint and guide address a separate choice about the pace of coding help.

Explicit selection follows the shared study-mode rule. An inspection request alone leaves an active hint mode in force. A new explicit selection changes the teaching preference while client permissions continue to govern tools. A read-only trace can explain the code and run permissible checks. A repair requires both a direct request and a writable session.

### Find the route from the program's purpose

Start with the user's stated interest. For open-ended requests, use documentation to identify the program's intended outcome, then inspect real entry points, their callers or configuration, and an existing integration example or test when present. Choose a route that reaches a result central to that purpose. For a backend it might be the request that carries out the main user action. For a CLI it might be the usual command that produces its primary output. A focused question resolves a genuine choice between equally plausible tasks or applications.

Use the compact map for orientation and pick one concrete input from the request, a test, or a clearly labeled illustrative example. Explain the same input throughout the route. The first pass links the main stages, then follow-ups reuse the route and expand the requested call or expression. The map points to other major routes for readers exploring the whole project in stages.

### Anchor the walkthrough in code and checks

Use file and symbol references, with line locations where available. For a significant transition, explain the relevant condition or call, the change in values or state, and the next step or effect. Short excerpts can make specific expressions easier to follow. Use a compact Mermaid sequence or flow diagram when branches, calls, or data movement benefit from a picture. A plain-text route conveys the same information in clients where diagrams do not render.

Check important or uncertain transitions with existing local tests or a suitable isolated run. Retain the input and what the check actually observed. A response assertion, a mock interaction, and a runtime trace each establish different facts. For a dynamically chosen handler, show the selection rule and available configuration. If selection cannot be resolved, state the condition and stop the factual trace at that boundary.

### Keep requested repairs connected to the route

Use the code and scenario already located by trace to scope a directly requested fix. Apply changes needed for that fix, verify with an appropriate available check, and revisit the affected transitions. Explain the previous and new branch, state change, or outcome with updated source references. If writes are blocked, report the client limit and continue the walkthrough with the available evidence.

## Risks / Trade-offs

- **A peripheral entry point can look like the main route.** Check how it leads to the documented purpose and confirm the connection in source or an existing scenario. Ask a focused question when there is a genuine choice.
- **An overview can obscure important details.** Name source locations and the concrete input in the overview, then let the learner choose which step to expand.
- **A successful test can be mistaken for proof of the full path.** Report the exact observation and derive remaining transitions from source with their conditions.
- **A skill instruction can be mistaken for a client permission change.** Preserve the client's sandbox in both explanation and repair flows, and check the read-only case separately in Codex.

## Migration Plan

Ship the skill as an additive selection. Update both READMEs' individual and full installation examples and verify the local selection in an isolated project. Existing users can install trace on its own or update their product selection. Rolling back removes the trace entry from the installation selection and the new skill directory. During spec sync or archive, update the existing Study modes and Distribution and validation purpose text to describe the expanded product set.
