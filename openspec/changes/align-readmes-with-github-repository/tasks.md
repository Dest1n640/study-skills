## 1. Bilingual README update

- [x] 1.1 Update `README.md` and `README.ru.md` with the canonical repository link and the exact single-skill and four-skill installation commands in `proposal.md`, including `--agent codex` and `--yes`. State the Node.js prerequisite, run-from-project context, project-local default, and `claude-code` agent replacement; label the shorter alternative interactive. Remove local-only/unpublished-placeholder wording. Verify both languages have matching copyable commands, the correct four skill names, no `OWNER/REPO`, and retain local-checkout installation and explicit invocation examples without recommending `--all`. Check command syntax against the linked upstream reference; do not report this as a remote installation test.
- [x] 1.2 Delete the complete `Protected hint sessions in Codex` and `Защищённый hint в Codex` sections through the next heading. Verify neither README contains these sections, their launch/resume commands, or relocated copies, while license notices and general evidence/compatibility limits remain.

## 2. Current project context

- [x] 2.1 Update repository identity in `openspec/DECISIONS.md` and `openspec/config.yaml`; split the old combined GitHub-address/publication checklist item into the established source address and genuinely pending verification. Record this README-only removal without revoking the approved skill-permission rules. Verify the current context names `Dest1n640/study-skills`, does not claim tested remote installation or publication of all local revisions, and preserves dated historical records.

## 3. Documentation verification

- [x] 3.1 Check local Markdown links in both READMEs, compare translated installation/limitation claims, run `git diff --check` and `openspec validate align-readmes-with-github-repository --strict`, and inspect the complete diff. Verify only the four implementation targets and this change's planning artifacts changed; product skills, metadata, main specs, archived changes, research, and retained run evidence stay unchanged. Keep remote installation, other-client behavior, and interactive session switching explicitly unverified; these documentation edits require no new behavioral run or publication.

Planning note: `skip_specs: true` because no requirement changes. `design.md` is deliberately omitted under its conditional creation rule: this is a bounded documentation update with no new architecture, dependency, migration, or unresolved technical decision. The concrete scope and verification are in `proposal.md` and the tasks above.

Verification on 2026-11-18: six shell examples matched the planned arguments and passed `sh -n`; all 13 local README links resolved. Full diff review and an explicit changed-file check confirmed only the four implementation targets and this task list changed. Dated decision history was preserved verbatim. `git diff --check` and strict OpenSpec validation passed. Remote installation, other clients, and interactive session switching were not run.
