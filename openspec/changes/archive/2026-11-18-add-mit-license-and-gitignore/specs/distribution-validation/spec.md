## ADDED Requirements

### Requirement: Publish an explicit project license
Original project materials SHALL be distributed under MIT with a root license text and consistent product-skill metadata and README links. Existing third-party copyright and license notices SHALL be preserved without claiming to relicense external materials.

#### Scenario: A learner installs one product skill
- **WHEN** the learner reads its metadata
- **THEN** the license identifier is MIT and the repository provides the full applicable license text

#### Scenario: Generated third-party development helpers are retained
- **WHEN** the repository includes OpenSpec-generated helpers
- **THEN** it retains the upstream copyright and permission notice separately from the project's own copyright

### Requirement: Exclude local artifacts without hiding project evidence
The repository SHALL ignore common local environment, cache, secret and temporary files while keeping product skills, specifications, evaluation fixtures, retained run evidence and environment templates eligible for version control.

#### Scenario: A contributor creates local artifacts
- **WHEN** untracked environment secrets, Python caches, virtual environments or dependency directories are created
- **THEN** Git ignores them according to the repository rules

#### Scenario: A contributor adds a project artifact
- **WHEN** a skill, OpenSpec document, evaluation result or example environment template is added
- **THEN** repository ignore rules do not conceal it
