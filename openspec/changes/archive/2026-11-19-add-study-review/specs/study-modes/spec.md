## ADDED Requirements

### Requirement: Provide a manually selected educational review mode

The project SHALL provide `study-review` as an independently installable mode explicitly selected by the learner. The review preference SHALL remain in effect until the learner explicitly selects another study mode or ends study mode. A request for a ready fix SHALL keep the current selection in effect. Any edit after an explicit mode switch remains subject to the new mode and client permissions.

#### Scenario: A learner explicitly chooses review
- **WHEN** a learner explicitly selects study-review during a different study mode
- **THEN** review becomes the active study preference and uses its own authorship boundary

#### Scenario: A learner explicitly chooses an implementation mode
- **WHEN** a learner explicitly switches from study-review to a study mode that permits the requested edit
- **THEN** the new mode governs the request and existing client permissions still govern edits
