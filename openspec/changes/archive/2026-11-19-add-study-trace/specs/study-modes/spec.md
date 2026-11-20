## MODIFIED Requirements

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

## RENAMED Requirements

- FROM: `### Requirement: Provide four manually selected modes`
- TO: `### Requirement: Provide manually selected study modes`
