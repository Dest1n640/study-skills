## MODIFIED Requirements

### Requirement: Reuse an existing installation route
Installation documentation SHALL use the existing Skills CLI route and SHALL label unpublished repository placeholders and untested instructions accurately. The recommended product installation SHALL select only the four study skills, without installing repository-development helpers.

#### Scenario: The repository is unpublished
- **WHEN** documentation shows npx skills add OWNER/REPO
- **THEN** it identifies OWNER/REPO as a placeholder rather than a working published project address

#### Scenario: Development skills are present in the source repository
- **WHEN** a learner follows the recommended product installation for a selected client
- **THEN** the installed project skill set contains the four study modes and does not include openspec-* development helpers

## ADDED Requirements

### Requirement: Keep behavioral checks repeatable and attributable
New claimed behavioral evaluation results SHALL identify the evaluated skill content, exact learner requests, starting fixture when needed, relevant environment, observed response and file changes, executed checks, and pass, fail, or not-run judgment against stated criteria.

#### Scenario: A contributor repeats a file-based check
- **WHEN** the contributor follows a documented case in a fresh isolated workspace
- **THEN** the supplied prompt and fixture permit repeating the procedure without reconstructing missing inputs from a past chat

#### Scenario: A new evaluation result is published
- **WHEN** a report claims that a scenario passed
- **THEN** the report links the observations supporting that judgment and identifies the tested skill revision rather than relying only on a narrative summary

#### Scenario: Only historical narrative evidence exists
- **WHEN** an earlier result lacks retained prompts, fixtures, or run artifacts
- **THEN** it remains labelled as historical limited evidence and is not retroactively presented as a newly reproduced run

### Requirement: Compare pace on matched tasks
Evaluation of a normal and fast mode pair SHALL use the same learner request and starting fixture in separate fresh contexts and SHALL assess directness, explanation depth, useful reasoning, and unchanged authorship boundaries.

#### Scenario: A pace comparison is performed
- **WHEN** normal and fast responses are compared
- **THEN** the reviewer uses matched inputs and a behavioral rubric rather than different assignments or a word-count-only verdict

### Requirement: Separate native invocation from supplied-file checks
Claims about installed Codex behavior SHALL identify whether the skill was invoked through native discovery or supplied directly, and unperformed checks SHALL remain explicitly not run.

#### Scenario: Native discovery cannot be exercised
- **WHEN** files are installed but the actual Codex invocation path has not been checked
- **THEN** the result reports installation evidence separately and leaves native invocation pending

#### Scenario: A fresh Codex context has no study selection
- **WHEN** the installed study modes are present but the learner has not selected one
- **THEN** the evaluator checks that their explicit-only settings are respected before claiming verified native manual selection

