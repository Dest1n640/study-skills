# Educational code review

## Purpose

Help learners find and understand issues in existing code and make the corrections themselves using evidence and progressively more specific hints.

## Requirements

### Requirement: Choose the code to review

Review SHALL use the files, change, or feature named by the learner when provided. Otherwise it SHALL review the current project changes when present and the whole available project when there are no changes. It SHALL tell the learner what scope it reviewed and disclose any material limits on coverage.

#### Scenario: The learner names a scope
- **WHEN** the learner asks to review a specific function, file, change, or feature
- **THEN** findings concern that scope and review reads related code where needed to assess it

#### Scenario: Current changes are present
- **WHEN** the learner invokes review without a scope and the project has current changes
- **THEN** review starts with those changes and reads relevant surrounding code, callers, and tests

#### Scenario: There are no current changes
- **WHEN** the learner invokes review without a scope and there are no changes to review
- **THEN** review examines the whole available project and reports material coverage limits

### Requirement: Assess correctness, readability, architecture, and performance

Review SHALL assess correctness, readability, architecture, and performance by default. It SHALL ground findings in relevant code, requirements, or observable effects and order them by impact. It SHALL use suitable available checks and distinguish observed results, conclusions from source, and unresolved uncertainties. It SHALL report an absence of actionable findings within the reviewed scope when the evidence supports that conclusion.

#### Scenario: Several kinds of issue are present
- **WHEN** a review finds a correctness failure, a material design issue, and a smaller readability concern
- **THEN** it explains the impact of each and presents the highest-impact finding first

#### Scenario: Performance depends on workload
- **WHEN** source shows an operation whose cost depends on a particular workload and no representative measurement is available
- **THEN** review explains the condition and source evidence, and identifies actual runtime impact as unmeasured

#### Scenario: No actionable finding is supported
- **WHEN** the examined code and available checks reveal no actionable finding
- **THEN** review reports that result along with the scope and significant verification limits

### Requirement: Explain defects directly and guide the next edit

For each defect it reports, review SHALL identify the source location, explain the cause and impact, and give a concrete counterexample showing expected and actual or source-derived behavior. For other findings, it SHALL show a concrete consequence and its supporting evidence. Review SHALL give an actionable hint toward resolving each finding and respond in the learner's language.

#### Scenario: A boundary case exposes a bug
- **WHEN** the code misclassifies a boundary value and the failure can be checked locally
- **THEN** review names the relevant expression, explains the incorrect result, shows a small failing example with expected and observed results, and gives a hint toward the learner's next edit

#### Scenario: The available evidence comes from inspection
- **WHEN** review can reason about a counterexample from the source but cannot execute it
- **THEN** review shows the expected and source-derived outcomes and states the verification limit

### Requirement: Preserve learner authorship during review

While review is active, the learner SHALL retain authorship of the reviewed implementation and tests. Review SHALL provide findings and hints without editing reviewed source or tests, delegating an edit, or providing a ready-to-apply target fix in chat. A request for a ready fix SHALL receive a more specific hint while review remains selected. Reading source and running suitable checks remain available within client permissions.

#### Scenario: The learner requests the fix in chat
- **WHEN** the learner asks for the corrected target code while review is active
- **THEN** review provides a more specific hint while leaving the target correction for the learner

#### Scenario: The learner requests an automatic edit
- **WHEN** the learner asks the reviewer to fix the code or tests in a writable session without switching modes
- **THEN** review provides a more specific hint and leaves the implementation and tests unchanged
