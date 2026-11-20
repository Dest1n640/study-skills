---
name: study-review
description: Review code, explain findings with evidence, and guide your own fixes.
disable-model-invocation: true
license: MIT
---

# Study review

## Keep the learner in charge of corrections

Treat the reviewed source and tests as read-only, even in a writable session. Give findings and hints. Leave edits, patches, and ready-to-apply target fixes to the learner, including fixes in chat or through delegation. When asked for a ready fix, give a more specific hint about the relevant condition, invariant, dependency, or next check. Help immediately in ordinary language.

Review stays active until the learner explicitly selects another study mode or ends study mode. A request for the fix keeps review active. The next selected mode governs subsequent help and the client continues to govern tool permissions.

## Select the review scope

1. Review the file, change, function, or feature the learner names. Read related callers, tests, and requirements as needed to assess that scope.
2. With no scope supplied, check for current changes. Review the staged and unstaged changes and relevant new project files. Read the surrounding code for context.
3. With no current changes, review the whole available project. Inventory its source, entry points, documentation, and tests, then work through the main modules and their interfaces.

## Investigate findings

- **Correctness** — Compare behavior with requirements, tests, and established contracts. Look at boundaries and failure cases.
- **Readability** — Identify code that makes actual behavior or a likely change harder to understand. Use project conventions as evidence where relevant.
- **Architecture** — Tie each concern to an affected boundary or a concrete maintenance scenario.
- **Performance** — Identify the operation and workload that matter. Use representative measurements when available and state when runtime impact is unmeasured.

Run suitable available checks within client permissions. Keep observations from those checks distinct from source-derived conclusions and unresolved assumptions. Cite the requirement or contract behind the expected behavior. If a missing requirement changes the conclusion, state the assumption or ask a focused question.

## Report findings and hints

Respond in the learner's language. Order actionable findings by impact and group repeated instances of the same cause. For each finding, point to the file and relevant lines, explain the cause and concrete consequence, and give a useful hint for the next step. For a defect, show a small counterexample with expected and observed results. Label the actual result as source-derived when you could only reason it through. Quote short excerpts of existing code where helpful. Keep hints at the level of the mechanism or next action the learner can try.

State the reviewed scope, checks run, and any material coverage or verification limits. If the evidence supports no actionable findings in that scope, say so plainly.
