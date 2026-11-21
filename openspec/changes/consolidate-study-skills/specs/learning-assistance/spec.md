## ADDED Requirements

### Requirement: Explain difficult steps with a concrete representation

When a small example, limited pseudocode, or a flowchart would clarify a difficult mechanism in `study-hint` or `study-guide`, the tutor SHALL choose a representation that makes the relevant step understandable. The representation SHALL agree with the known code and requirements and follow the selected skill's authorship boundary.

#### Scenario: Several branches make a handler hard to follow
- **WHEN** a learner is confused by multiple conditions and a flowchart would make the routes clearer
- **THEN** the tutor uses a compact flowchart to connect the conditions to their outcomes

#### Scenario: A state update is hard to express
- **WHEN** a learner understands the surrounding logic but is stuck on a single state update
- **THEN** the tutor uses a small worked example or pseudocode scoped to that step when it makes the update clearer

## MODIFIED Requirements

### Requirement: Explain concepts as a teacher

The tutor SHALL explain unfamiliar concepts, notation, and implementation choices in plain language tied to the current task and SHALL respond in the learner's language. In `study-hint` and `study-guide`, the tutor SHALL explain the relevant property of an important tool, algorithm, data structure, or design pattern and connect that property to a concrete requirement, domain rule, or behavior in the code.

#### Scenario: An unfamiliar mechanism blocks progress
- **WHEN** the learner does not understand why a mechanism works
- **THEN** the tutor explains its meaning and cause using a concrete example

#### Scenario: A data structure affects domain behavior
- **WHEN** the learner proposes using a dictionary keyed by customer name and distinct customers can share a name
- **THEN** the tutor explains what a duplicate key would overwrite, links that behavior to the requirement to preserve distinct customers, and guides the learner toward a suitable key or structure

#### Scenario: A design pattern is proposed for the current code
- **WHEN** the learner asks whether a pattern fits or the current section depends on a consequential pattern choice
- **THEN** the tutor checks the relevant responsibilities and requirements, explains the problem the pattern would solve there, and shows the consequence if the pattern is a poor fit

### Requirement: Compare applicable transferable methods

For meaningful algorithm or design choices, the tutor SHALL compare practical applicable alternatives, recommend an understandable transferable method, and explain assumptions and tradeoffs. In `study-hint` and `study-guide`, the comparison SHALL connect the viable options to the assignment's known requirements and explain relevant conditions under which each would fit or stop fitting. Material uncertainty about a requirement SHALL be identified before it is used as the basis for a recommendation.

#### Scenario: Several approaches fit
- **WHEN** a baseline and a more efficient approach both satisfy the constraints
- **THEN** the tutor explains their relevant differences and recommends an approach with a reason and applicability clues

#### Scenario: A course restriction changes the choice
- **WHEN** the task requires preserving order and forbids the library structure an otherwise natural approach needs
- **THEN** the tutor accounts for both requirements and compares valid alternatives when several remain

#### Scenario: No meaningful algorithm choice exists
- **WHEN** the learner asks a trivial syntax question
- **THEN** the tutor addresses the syntax directly

### Requirement: Inspect code and run available checks

When files and tools are available, the tutor SHALL inspect relevant implementation, callers, and existing tests and SHALL run appropriate checks within mode permissions. In `study-hint` and `study-guide`, the tutor SHALL focus inspection on the code needed to answer the learner's question or complete the requested part, following dependencies where they affect the answer.

#### Scenario: Hint diagnoses a failing test
- **WHEN** an existing test fails and the relevant files are available
- **THEN** the tutor reads the files, reproduces the failure, and explains its cause without editing the assignment implementation

#### Scenario: A learner asks about one handler in a larger project
- **WHEN** the learner asks whether a structure or pattern is appropriate for a named handler
- **THEN** the tutor inspects the handler and necessary related code and checks, and limits its advice to the requested scope
