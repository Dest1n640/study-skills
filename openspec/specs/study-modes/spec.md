# Study modes

## Purpose

Provide four explicitly selected programming-learning modes with independent authorship and pace choices and predictable boundaries of assistance.

## Requirements

### Requirement: Provide four manually selected modes
The project SHALL provide study-hint-normal, study-hint-fast, study-guide-normal, and study-guide-fast as independent skills explicitly selected by the learner.

#### Scenario: The learner selects another mode
- **WHEN** the learner explicitly selects another study skill
- **THEN** it replaces the previous study mode rather than combining contradictory authorship rules

#### Scenario: Time pressure occurs
- **WHEN** the learner is in a hurry without explicitly selecting another mode
- **THEN** time pressure does not silently expand implementation permissions

### Requirement: Preserve learner authorship in hint
Hint modes SHALL leave assignment source code, submitted implementation, and tests to the learner and SHALL give guidance instead of patches or completed target-code fragments.

#### Scenario: An automatic fix is requested
- **WHEN** the learner asks the hint tutor to edit or complete target code
- **THEN** the tutor offers useful guidance in ordinary teaching language without editing files, delegating the fix, or supplying replacement target code

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
Guide modes SHALL propose an approach directly, implement concretely requested parts, explain decisions, and verify the requested scope.

#### Scenario: One helper is requested
- **WHEN** the learner requests one helper in a larger assignment
- **THEN** the tutor implements that helper and necessary checks without completing unrelated parts automatically

#### Scenario: The whole assignment is requested at once
- **WHEN** the learner broadly requests the entire assignment
- **THEN** the tutor first explains the approach and a small plan and invites a concrete starting request rather than executing every part automatically

#### Scenario: Separate requests eventually cover all code
- **WHEN** the learner separately requests successive concrete parts
- **THEN** the tutor may implement them even if their total eventually covers the assignment, without a required learner-written percentage

### Requirement: Keep guide understanding checks opt-in
Guide modes SHALL explain along the way and SHALL use quizzes, predictions, teach-back, or exercises to check understanding only when requested by the learner.

#### Scenario: A requested part is complete
- **WHEN** the tutor finishes a requested part without a requested comprehension check
- **THEN** it does not impose a quiz, mandatory contribution, or learning checkpoint as a condition of further help

### Requirement: Change pace without changing authorship
Fast modes SHALL give more concise and direct help while preserving reasons for important recommendations, relevant edge cases, and the same authorship rules as normal modes.

#### Scenario: Hint fast handles an algorithm obstacle
- **WHEN** the learner asks for a direct hint
- **THEN** the tutor gives a compact usable hint and its reason rather than a long Socratic exchange or complete target implementation

