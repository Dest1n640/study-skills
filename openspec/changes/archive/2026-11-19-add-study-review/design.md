## Context

Hint already gives learner-authored assistance and can inspect code and run existing checks. Review uses the same authorship principle for a different task. It looks for issues across a defined scope before explaining individual findings. The pending trace change follows concrete execution routes and handles requested repairs under its own contract. See the [proposal](proposal.md) and [review delta](specs/educational-code-review/spec.md).

## Goals / Non-Goals

**Goals**

- Make each finding usable as a starting point for an independent repair.
- Provide an honest account of review scope and evidence for a single change or a whole project.

**Non-Goals**

- Automated remediation, a persistent review dashboard, and automated grading belong outside this change.

## Decisions

### Keep one self-contained mode

Use the existing product layout with one English `SKILL.md`, explicit selection metadata, and the root MIT license copy. A single entry point can make later hints more specific within the conversation. Reuse the instruction pattern for learner authorship and tools in hint. Guide remains available when the learner wants a concrete implementation and explicitly selects it.

### Select scope from the request and worktree

Honor a named file, change, or feature. When no scope is supplied, inspect the worktree for staged and unstaged changes and relevant new project files. Read affected callers, requirements, and tests for context. When there are no current changes, inventory available source, tests, documentation, and entry points, then cover the project by its main modules and their interfaces. Report the inspected areas and any important gaps if the accessible material or available tools limit coverage.

### Explain the impact with evidence at the right depth

Check each dimension in the selected scope. For correctness, compare behavior with requirements, tests, and established contracts. For readability, identify a concrete way the code makes behavior hard to understand or change. For architecture, tie a finding to an affected boundary or maintenance scenario. For performance, name the operation and workload that matter, and give a representative measurement when one is available. Group repeated instances of a single cause where helpful. Lead with the greatest concrete impact.

Anchor each defect in a file and location, explain the cause, and show the expected and actual or source-derived result on a small counterexample. For example, the existing positive-count fixture has an input containing `0` whose result is one too high. The hint can direct the learner to compare the requirement's meaning of positive with how the boundary value enters the count. Existing checks can establish the result. Source inspection can locate the cause independently. [Existing fixture](../../../evaluation/fixtures/positive/test_exercise.py)

### Keep the correction with the learner

Use short excerpts of the existing code, concrete inputs, and hints about the relevant condition, invariant, dependency, or cost. On a request for a ready fix, give a more specific observation or direction while keeping the code and tests under learner authorship. Use the active client's permissions for checks. Selecting review leaves those permissions in effect, and the response describes the behavior actually observed in the session.

## Risks / Trade-offs

- **A whole-project review can imply broader coverage than was possible.** Record reviewed areas, checks run, and areas where important evidence was unavailable.
- **Style preferences can crowd out material findings.** Tie each issue to a consequence and available project conventions, then prioritize by impact.
- **A strong hint can become a ready correction.** Keep it at the level of the necessary condition, mechanism, or next inspection step. Evaluate both a request for corrected code and a request to edit files in a writable session.

## Migration Plan

Add the review entry and documentation for separate and full installation. The full selection should describe the skills available in that revision. Removing the review entry from that selection lets users keep the other skills installed if review is withdrawn.

The study-mode delta adds a distinct requirement, so it can coexist with the trace mode delta. The two changes both modify the full-installation requirement. Before syncing or archiving the second change, reconcile that shared requirement against the then-current baseline and keep both skill selections and their individual-install scenarios. Align count-based purpose text and installation examples with the available skills at that point.
