## ADDED Requirements

### Requirement: Document migration to the consolidated tutoring skills

The release SHALL replace the four pace-specific hint and guide skills with `study-hint` and `study-guide`. Both public READMEs SHALL map the four old names to the new skill and equivalent pace and explain how to replace previously installed copies at their installation scope.

#### Scenario: The learner upgrades an installed fast guide
- **WHEN** the learner has `study-guide-fast` installed
- **THEN** the migration instructions direct them to replace the old copy, invoke `study-guide`, and choose Quick or request it explicitly

#### Scenario: A learner installs the current product set
- **WHEN** a learner follows the current full installation instructions in a fresh project
- **THEN** the selected product set contains exactly `study-hint`, `study-guide`, `study-review`, and `study-trace`

## MODIFIED Requirements

### Requirement: Compare pace on matched tasks

Evaluation SHALL compare Quick and Detailed within each of `study-hint` and `study-guide` using the same underlying learner request and starting fixture in separate fresh contexts. It SHALL assess directness, explanation depth, useful reasoning, and unchanged authorship boundaries. Separate cases SHALL cover the menu, inline pace, and persistence across turns in the same conversation.

#### Scenario: A pace comparison is performed
- **WHEN** Quick and Detailed responses from the same skill are compared
- **THEN** the reviewer uses matched inputs differing only in pace choice and a behavioral rubric that considers reasoning and authorship as well as concision

#### Scenario: The learner chooses a pace through the opening menu
- **WHEN** evaluation exercises the menu, a follow-up, and an explicit skill switch in one conversation
- **THEN** it records the first menu, whether the original task resumes, whether the chosen pace persists, and how the new skill resolves its pace
