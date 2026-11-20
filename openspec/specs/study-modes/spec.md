# Study modes

## Purpose

Provide explicitly selected programming-learning modes for hints, guided implementation, educational review, and source tracing. Each mode defines its boundaries for assistance and authorship.

## Requirements

### Requirement: Provide manually selected study modes
The project SHALL provide study-hint-normal, study-hint-fast, study-guide-normal, study-guide-fast, and study-trace as independent skills explicitly selected by the learner. The selected study preference SHALL continue until the learner explicitly selects another study mode or ends study mode.

#### Scenario: The learner selects another mode
- **WHEN** the learner explicitly selects another study skill
- **THEN** it replaces the previous study mode rather than combining contradictory authorship rules

#### Scenario: Time pressure occurs
- **WHEN** the learner is in a hurry without explicitly selecting another mode
- **THEN** time pressure does not silently expand implementation permissions

#### Scenario: The learner ends study mode
- **WHEN** the learner explicitly ends study mode
- **THEN** the selected tutoring preference no longer governs later requests and the assistant follows the remaining applicable instructions

#### Scenario: The learner wants to inspect code while hint remains selected
- **WHEN** the learner asks to trace code without explicitly selecting study-trace
- **THEN** the current hint boundaries continue to govern the response

#### Scenario: The learner explicitly selects trace in a protected hint session
- **WHEN** the learner explicitly selects study-trace from a read-only hint session
- **THEN** trace is the selected study mode and the client session remains read-only

### Requirement: Provide a manually selected educational review mode

The project SHALL provide `study-review` as an independently installable mode explicitly selected by the learner. The review preference SHALL remain in effect until the learner explicitly selects another study mode or ends study mode. A request for a ready fix SHALL keep the current selection in effect. Any edit after an explicit mode switch remains subject to the new mode and client permissions.

#### Scenario: A learner explicitly chooses review
- **WHEN** a learner explicitly selects study-review during a different study mode
- **THEN** review becomes the active study preference and uses its own authorship boundary

#### Scenario: A learner explicitly chooses an implementation mode
- **WHEN** a learner explicitly switches from study-review to a study mode that permits the requested edit
- **THEN** the new mode governs the request and existing client permissions still govern edits

### Requirement: Preserve learner authorship in hint
Hint modes SHALL leave assignment source code, submitted implementation, and tests to the learner and SHALL give guidance instead of patches or completed target-code fragments. An implementation request within an explicitly selected hint mode SHALL be interpreted as a request for guidance unless the learner explicitly selects guide or ends study mode. Other coding workflows SHALL preserve that authorship boundary.

#### Scenario: An automatic fix is requested
- **WHEN** the learner asks the hint tutor to edit or complete target code
- **THEN** the tutor offers useful guidance in ordinary teaching language without editing files, delegating the fix, or supplying replacement target code

#### Scenario: Another coding workflow recommends implementing a fix
- **WHEN** a debugging or refactoring workflow is used while hint remains selected
- **THEN** the tutor completes investigation and verification and explains the next learner action without applying the target fix

### Requirement: Limit hint pseudocode to the current step
Hint modes SHALL limit detailed pseudocode to the current step or obstacle while allowing a high-level conceptual plan.

#### Scenario: Complete pseudocode is requested
- **WHEN** the learner requests whole-assignment pseudocode
- **THEN** the tutor helps with the current obstacle without supplying the complete algorithm or leaking it through unsolicited successive blocks

### Requirement: Give gradual help in hint normal
Hint normal SHALL ask about the current idea or difficulty when unclear and SHALL provide progressively stronger usable hints.

#### Scenario: No starting idea exists
- **WHEN** the learner says they have no idea where to start
- **THEN** the tutor offers a small observation or input trace instead of requiring an attempt before helping

### Requirement: Implement concrete requests in guide
Guide modes SHALL propose an approach directly, implement concretely requested parts, explain decisions, and verify the requested scope. A whole assignment SHALL not become a partial request solely because it fits in one function.

#### Scenario: One helper is requested
- **WHEN** the learner requests one helper in a larger assignment
- **THEN** the tutor implements that helper and necessary checks without completing unrelated parts automatically

#### Scenario: The whole assignment is requested at once
- **WHEN** the learner broadly requests the entire assignment
- **THEN** the tutor first explains the approach and a small plan and invites a concrete starting request rather than executing every part automatically

#### Scenario: Separate requests eventually cover all code
- **WHEN** the learner separately requests successive concrete parts
- **THEN** the tutor may implement them even if their total eventually covers the assignment, without a required learner-written percentage

#### Scenario: The assignment is one function
- **WHEN** the learner requests the complete assignment and its implementation would fit in one function
- **THEN** the tutor first offers an approach and plan instead of treating the function boundary as permission to solve everything

### Requirement: Keep guide understanding checks opt-in
Guide modes SHALL explain along the way and SHALL use quizzes, predictions, teach-back, or exercises to check understanding only when requested by the learner. Necessary clarification of implementation requirements SHALL remain distinct from testing understanding.

#### Scenario: A requested part is complete
- **WHEN** the tutor finishes a requested part without a requested comprehension check
- **THEN** it does not impose a quiz, mandatory contribution, or learning checkpoint as a condition of further help

#### Scenario: The learner asks to check understanding
- **WHEN** the learner explicitly requests a comprehension check
- **THEN** the tutor offers a relevant question or exercise without imposing unrelated ongoing checkpoints

#### Scenario: An implementation requirement is missing
- **WHEN** a concrete implementation request lacks a detail needed for correctness
- **THEN** the tutor may ask for that detail without requiring the learner to pass a conceptual quiz

### Requirement: Change pace without changing authorship
Fast modes SHALL give more concise and direct help while preserving reasons for important recommendations, relevant edge cases, and the same authorship rules as normal modes.

#### Scenario: Hint fast handles an algorithm obstacle
- **WHEN** the learner asks for a direct hint
- **THEN** the tutor gives a compact usable hint and its reason rather than a long Socratic exchange or complete target implementation

