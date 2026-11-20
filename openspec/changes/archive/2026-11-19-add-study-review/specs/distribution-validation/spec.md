## MODIFIED Requirements

### Requirement: Reuse an existing installation route

Installation documentation SHALL use the existing Skills CLI route and SHALL label unpublished repository placeholders and untested instructions accurately. It SHALL document individual product skill selection, including study-review. The recommended full product installation SHALL explicitly select the product study skills available in the documented revision, including study-review, and exclude repository-development helpers.

#### Scenario: The repository is unpublished
- **WHEN** documentation shows npx skills add OWNER/REPO
- **THEN** it identifies OWNER/REPO as a placeholder rather than a working published project address

#### Scenario: Development skills are present in the source repository
- **WHEN** a learner follows the recommended full product installation for a selected client
- **THEN** the installed set contains the product study skills available in that revision and excludes openspec-* development helpers

#### Scenario: A learner installs review on its own
- **WHEN** the learner uses the documented individual skill selection for study-review
- **THEN** the selection includes study-review without requiring another study skill
