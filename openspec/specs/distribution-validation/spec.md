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
Installation documentation SHALL use the existing Skills CLI route and SHALL label unpublished repository placeholders and untested instructions accurately.

#### Scenario: The repository is unpublished
- **WHEN** documentation shows npx skills add OWNER/REPO
- **THEN** it identifies OWNER/REPO as a placeholder rather than a working published project address

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

