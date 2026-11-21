## ADDED Requirements

### Requirement: Select a tutoring pace on activation

When the learner activates `study-hint` or `study-guide`, the tutor SHALL honor a clear pace preference in the invocation. Otherwise the tutor SHALL offer **Quick** and **Detailed** in the learner's language and wait for the selection before addressing the assignment. It SHALL use the client's choice control when available and offer the same choices in text otherwise. The tutor SHALL retain the pending task while awaiting a choice. The selected pace SHALL remain active in the current conversation until the learner explicitly changes pace, selects another skill, or ends study mode.

#### Scenario: The learner selects guide with a task and no pace
- **WHEN** the learner invokes `study-guide` with a request to implement a concrete part and no pace preference
- **THEN** the tutor first offers the two pace choices without implementing the part and resumes the original request when the learner chooses

#### Scenario: The learner says they are in a hurry at activation
- **WHEN** the learner invokes `study-hint` and clearly requests brief help or says they are in a hurry
- **THEN** the tutor starts at Quick pace immediately and follows the hint authorship boundary

#### Scenario: The learner requests an in-depth explanation at activation
- **WHEN** the learner invokes either tutoring skill and clearly asks for a detailed walkthrough
- **THEN** the tutor starts at Detailed pace immediately

#### Scenario: The client lacks a choice control
- **WHEN** the tutor needs a pace selection and the client has no usable choice control
- **THEN** the tutor offers both choices in text and accepts a plain-language reply

#### Scenario: The learner continues in the selected pace
- **WHEN** the learner asks another question during the same skill activation
- **THEN** the tutor uses the current pace without showing the menu again

#### Scenario: The learner explicitly changes pace or skill
- **WHEN** the learner asks to change pace in the current tutoring skill or explicitly activates another tutoring skill
- **THEN** an explicit pace change applies immediately within the current authorship boundary, and a different skill activation resolves pace from its own invocation or menu

### Requirement: Limit detailed hint diagrams to the current step

Hint SHALL limit detailed diagrams of missing target logic to the current step or obstacle and SHALL allow a high-level conceptual overview. Hint SHALL avoid using diagrams or a sequence of visual explanations to give the learner a complete assignment solution.

#### Scenario: The learner asks for a complete solution as a flowchart
- **WHEN** the learner requests a flowchart that would specify all missing target logic
- **THEN** hint shows the current obstacle or gives a high-level overview that leaves the implementation to the learner

## MODIFIED Requirements

### Requirement: Provide manually selected study modes

The project SHALL provide `study-hint`, `study-guide`, `study-review`, and `study-trace` as independent skills explicitly selected by the learner. The selected study mode SHALL continue until the learner explicitly selects another study mode or ends study mode.

#### Scenario: The learner selects another mode
- **WHEN** the learner explicitly selects another study skill
- **THEN** the new study mode replaces the previous study mode and applies its own authorship rules

#### Scenario: Time pressure occurs
- **WHEN** the learner is in a hurry without explicitly selecting another mode
- **THEN** the current mode's implementation permissions continue to apply

#### Scenario: The learner ends study mode
- **WHEN** the learner explicitly ends study mode
- **THEN** the selected tutoring preference no longer governs later requests and the assistant follows the remaining applicable instructions

#### Scenario: The learner wants to inspect code while hint remains selected
- **WHEN** the learner asks to trace code without explicitly selecting study-trace
- **THEN** the current hint boundaries continue to govern the response

#### Scenario: The learner explicitly selects trace in a protected hint session
- **WHEN** the learner explicitly selects study-trace from a read-only hint session
- **THEN** trace is the selected study mode and the client session remains read-only

### Requirement: Change pace without changing authorship

Quick pace in `study-hint` and `study-guide` SHALL give direct, concise help and retain the reason for important recommendations and material edge cases. Detailed pace SHALL explain the reasoning in more depth and use a concrete example when it helps. Detailed hint SHALL ask about the current idea or difficulty if unclear and give progressively stronger hints. Both paces SHALL preserve the selected skill's authorship, clarification, and verification boundaries.

#### Scenario: Hint fast handles an algorithm obstacle
- **WHEN** the learner chooses Quick and asks for help with an algorithm step
- **THEN** the tutor gives a compact usable hint and its reason within the current obstacle

#### Scenario: The learner has no starting idea in Detailed hint
- **WHEN** the learner chooses Detailed and says they have no idea where to start
- **THEN** the tutor offers a small observation or input trace without requiring an attempt before helping

#### Scenario: Quick guide receives a broad implementation request
- **WHEN** the learner chooses Quick and asks guide to implement the whole assignment at once
- **THEN** guide gives a compact plan and a suggested starting part and waits for a concrete implementation request

## REMOVED Requirements

### Requirement: Give gradual help in hint normal

**Reason**: Gradual help is now a pace within `study-hint`. The updated pace requirement preserves the behavior.

**Migration**: Invoke `study-hint` and choose Detailed.
