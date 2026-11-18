# Distribution and validation

## Purpose

Package the four skills for explicit use across supporting agents while accurately describing installation, compatibility, evaluation evidence, and publication status.

## Requirements

### Requirement: Keep skills independently installable
Each product skill SHALL contain its own English SKILL.md and SHALL remain usable without a custom installer, profile service, or another installed tutoring skill.

#### Scenario: Only one mode is installed
- **WHEN** a learner installs one product skill
- **THEN** its essential behavior and boundaries are available without a missing sibling dependency

### Requirement: Document languages and invocation
The project SHALL provide Russian and English public descriptions, learner-language conversation, and documented client-specific explicit invocation settings.

#### Scenario: Codex reads product metadata
- **WHEN** a supporting Codex client reads agents/openai.yaml
- **THEN** allow_implicit_invocation is false and examples use dollar-name invocation

#### Scenario: Claude Code reads product metadata
- **WHEN** a supporting Claude Code client reads skill frontmatter
- **THEN** disable-model-invocation is true and documentation distinguishes slash invocation without claiming a tested Claude session

### Requirement: Reuse an existing installation route
Installation documentation SHALL use the existing Skills CLI route and SHALL label unpublished repository placeholders and untested instructions accurately. The recommended product installation SHALL select only the four study skills, without installing repository-development helpers.

#### Scenario: The repository is unpublished
- **WHEN** documentation shows npx skills add OWNER/REPO
- **THEN** it identifies OWNER/REPO as a placeholder rather than a working published project address

#### Scenario: Development skills are present in the source repository
- **WHEN** a learner follows the recommended product installation for a selected client
- **THEN** the installed project skill set contains the four study modes and does not include openspec-* development helpers

### Requirement: Report only the evidence actually checked
Evaluation reports SHALL distinguish metadata validation, direct-instruction Codex smoke tests, native discovery, installation, other-client behavior, and learning effectiveness.

#### Scenario: The skill file is supplied directly
- **WHEN** Codex smoke tests succeed with a supplied SKILL.md
- **THEN** the report does not claim that native invocation, installation, or Claude Code behavior was verified

#### Scenario: Program checks pass
- **WHEN** code passes tests
- **THEN** the tutor and documentation do not infer learner understanding from that result

### Requirement: Keep compatibility claims conservative
The project SHALL prioritize Codex and Claude Code format support, limit initial behavioral testing to Codex, and describe other agents only at the level actually established.

#### Scenario: Another client supports the shared format
- **WHEN** the client has not been behaviorally tested
- **THEN** documentation does not promise identical vendor-metadata handling or guaranteed tutor behavior

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

### Requirement: Document permission-bound hint launch
The product SHALL document Codex hint sessions using read-only workspace permissions with approval escalation disabled. It SHALL explain that selecting a skill does not change client permissions and that workspace-write guide use requires resuming with suitable permissions and explicitly selecting guide. Chat-output boundaries SHALL remain described as instructions rather than technical enforcement.

#### Scenario: The learner launches protected hint
- **WHEN** the learner follows the documented Codex hint launch
- **THEN** the client uses read-only with approval policy never, and the hint skill does not claim it set these permissions

#### Scenario: The learner moves from protected hint to guide
- **WHEN** the learner wants guide to edit files
- **THEN** documentation directs them to resume the same chat with workspace-write and on-request approvals and then explicitly select guide

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
