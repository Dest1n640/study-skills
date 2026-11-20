---
name: study-trace
description: Follow one concrete route through existing code, from input to outcome.
disable-model-invocation: true
license: MIT
---

# Study trace

## Choose a route

Read the relevant documentation, actual entry points, callers, and available tests or examples. Follow the learner's stated goal first. For an unscoped or whole-project request, show a compact map of the main parts and begin a clear principal route in the first answer. Pick a route that connects the program's purpose to a concrete outcome. Show where other major routes fit when the learner wants to understand the whole project.

If several routes fit equally well, ask one focused question naming the source-backed options. If the available evidence cannot establish a route, identify what's missing.

## Follow one input through the code

Use one request, input, object, or event throughout. Prefer a value the learner supplied or an existing example, or label an illustrative value. Show the significant transitions from entry to outcome or the last verifiable boundary. For each transition, name the file and symbol, link the line when available, and explain the call or branch, the relevant values before and after, and the next effect.

Use short source excerpts when they clarify a mechanism. Add a compact Mermaid flowchart or sequence diagram when calls, branches, or movement of data benefit from a picture. Keep the route navigable in the surrounding text. Answer in the learner's language. When asked to expand a step, keep the same route and explain the actual expression or call in more detail.

## Verify significant transitions

Start with source and use suitable available local checks for important or uncertain transitions. Distinguish what follows from source, what the specific check observed, and what still depends on runtime conditions. A test with a substitute dependency can confirm its assertions in that setup. Attribute intermediate steps it did not observe to source or an assumption. If a runtime choice cannot be resolved, show how the code makes the choice and where the verifiable path ends.

## Keep repairs within the learner's request

Preserve source and tests during explanation, even when the path exposes a problem. Apply a repair only when the learner directly requests it and the client permits writes. Use relevant callers and existing checks to scope the fix to the indicated problem and necessary related code. Verify with suitable local checks and explain the affected transition and outcome before and after. If writes are blocked, report the permission limit and explain what the existing evidence shows.

Explicit selection of study-trace replaces the previous study preference. Trace remains active until another study mode is explicitly selected or the learner ends study mode. A request to inspect code on its own leaves the existing mode active. A mode switch leaves the client's tool permissions in effect.
