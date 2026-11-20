# Code tracing

## Purpose

Help learners read an existing program by following a concrete scenario through its source, from an entry point to an outcome or a known boundary.

## Requirements

### Requirement: Start with a source-backed route

Trace SHALL inspect available project documentation, real entry points, and relevant examples or tests. It SHALL follow the learner's stated goal when provided. For an unscoped invocation or a request to understand the whole project, trace SHALL show a compact map and immediately start a clear principal route through the program's key behavior. When multiple routes are comparably relevant, trace SHALL ask one focused question presenting the grounded options. When evidence is insufficient, trace SHALL identify the missing information.

#### Scenario: One principal route is clear

- **WHEN** the learner invokes trace with no specific goal and the source and project context identify one principal route
- **THEN** trace shows a compact map of the main parts, names the chosen scenario, and starts tracing it in the first response

#### Scenario: The learner wants to understand the whole project

- **WHEN** the learner asks to understand the whole project and one principal route is clear
- **THEN** trace orients the learner with the main parts and shows where other routes fit before following one main route through the program

#### Scenario: Several routes are comparably relevant

- **WHEN** a repository has several comparable applications or entry points and the learner has not specified a goal
- **THEN** trace asks a focused question with concrete choices tied to the available project evidence

#### Scenario: A specific goal is given

- **WHEN** the learner names a feature, event, function, or input to follow
- **THEN** trace selects the route relevant to that goal and identifies missing evidence if it cannot follow a transition

### Requirement: Explain the route with source locations and concrete data

Trace SHALL begin by showing the selected scenario from entry to outcome or the last verifiable boundary, with its significant transitions. It SHALL anchor each explained transition to the relevant file and symbol and provide the line location when available. It SHALL explain what calls the next step, why a branch is selected, and how the relevant input, event, or state changes where applicable. It SHALL use short source excerpts when they clarify the mechanism, and a diagram when it clarifies calls, branches, or movement of data. Trace SHALL respond in the learner's language and expand the step the learner asks about.

#### Scenario: A concrete input crosses multiple modules

- **WHEN** a selected scenario crosses several calls and a conditional transition
- **THEN** trace follows the same input to the result, anchors the significant steps in source, and makes the selected branch and relevant intermediate values understandable

#### Scenario: A diagram clarifies the flow

- **WHEN** interactions or branches are difficult to follow in prose alone
- **THEN** trace adds a diagram that agrees with the named source steps and chosen scenario

#### Scenario: The learner asks to zoom in

- **WHEN** the learner asks why a specific call, expression, or branch behaves as shown
- **THEN** trace expands that step using its actual source and connects it to the selected route

### Requirement: Ground execution claims in their evidence

Trace SHALL start from source and use suitable available local checks to verify important or uncertain transitions. It SHALL identify which claims follow from inspected source, which were observed in a specific execution, and which depend on unverified runtime conditions. A check SHALL support only the behavior it exercises or observes.

#### Scenario: A check observes only the result

- **WHEN** an existing local test verifies the result using a substitute for an external dependency and does not observe intermediate calls
- **THEN** trace reports that result in the test context and attributes any unobserved intermediate steps to source or explicitly stated assumptions

#### Scenario: The route depends on unavailable configuration

- **WHEN** source inspection identifies a runtime-selected handler but the relevant configuration or local execution is unavailable
- **THEN** trace shows where selection occurs and what would resolve it, while identifying the remaining route as conditional

### Requirement: Apply only a directly requested repair

Trace SHALL preserve the source and tests during a walkthrough. On a direct request to repair an identified problem, trace SHALL apply the fix to the indicated area and necessary related code when the client permits writes. It SHALL verify the requested scope when suitable checks are available and show how the fix changes the selected route. Trace SHALL report a client permission limit when it cannot apply the requested edit.

#### Scenario: A walkthrough exposes an unexpected branch

- **WHEN** a learner requests an explanation and the traced input reaches an unexpected branch
- **THEN** trace explains the observed behavior and its source while leaving implementation and tests untouched

#### Scenario: The learner requests the indicated fix

- **WHEN** the learner asks to fix a problem identified during trace and the client permits writes
- **THEN** trace applies the scoped fix, runs suitable available checks, and explains the changed branch, data, or outcome in the route context

#### Scenario: The client prevents writes

- **WHEN** the learner requests a repair in a read-only client session
- **THEN** trace identifies the permission limit and preserves the files
