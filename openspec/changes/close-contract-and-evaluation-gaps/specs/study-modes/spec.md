## MODIFIED Requirements

### Requirement: Provide four manually selected modes
The project SHALL provide study-hint-normal, study-hint-fast, study-guide-normal, and study-guide-fast as independent skills explicitly selected by the learner. The selected study preference SHALL continue until the learner explicitly selects another study mode or ends study mode.

#### Scenario: The learner selects another mode
- **WHEN** the learner explicitly selects another study skill
- **THEN** it replaces the previous study mode rather than combining contradictory authorship rules

#### Scenario: Time pressure occurs
- **WHEN** the learner is in a hurry without explicitly selecting another mode
- **THEN** time pressure does not silently expand implementation permissions

#### Scenario: The learner ends study mode
- **WHEN** the learner explicitly ends study mode
- **THEN** the selected tutoring preference no longer governs later requests and the assistant follows the remaining applicable instructions

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


### Requirement: Preserve learner authorship in hint
Hint modes SHALL leave assignment source code, submitted implementation, and tests to the learner and SHALL give guidance instead of patches or completed target-code fragments. An implementation request within an explicitly selected hint mode SHALL be interpreted as a request for guidance unless the learner explicitly selects guide or ends study mode. Other coding workflows SHALL preserve that authorship boundary.

#### Scenario: An automatic fix is requested
- **WHEN** the learner asks the hint tutor to edit or complete target code
- **THEN** the tutor offers useful guidance in ordinary teaching language without editing files, delegating the fix, or supplying replacement target code

#### Scenario: Another coding workflow recommends implementing a fix
- **WHEN** a debugging or refactoring workflow is used while hint remains selected
- **THEN** the tutor completes investigation and verification and explains the next learner action without applying the target fix
