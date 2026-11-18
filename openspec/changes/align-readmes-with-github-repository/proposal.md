## Why

The public repository is now https://github.com/Dest1n640/study-skills, but both READMEs still describe a local unpublished draft and use `OWNER/REPO`. The user also requested removal of the protected Codex hint-session section in both languages.

## What Changes

- Replace current installation placeholders with `Dest1n640/study-skills` in English and Russian, including the short interactive command; link the canonical repository and remove instructions to wait for publication or substitute an owner.
- Preserve the recommended explicit selection of the four product skills, local installation instructions, invocation examples, license notices, and accurate compatibility/evaluation limits.
- Delete `Protected hint sessions in Codex` and `Защищённый hint в Codex` in their entirety from the respective READMEs. Do not relocate or recreate these blocks in the README installation or usage sections.
- Update current repository identity and release-status context in `openspec/DECISIONS.md` and `openspec/config.yaml`, separating the established public source address from unverified remote installation and remaining release checks. Retain historical research, archived changes, and evaluation evidence as historical records.
- No tutoring behavior changes: all four skill texts and metadata retain their existing rules, including client-permission guidance. The learner-visible change is the repository-specific installation documentation and shorter READMEs.

Confirmed: the user supplied the repository and requested both section deletions. On 2026-11-18, GitHub repository and root-contents reads confirmed a public repository containing `skills/` and both READMEs; local `origin` already matches. Sources: [repository metadata](https://api.github.com/repos/Dest1n640/study-skills), [root contents](https://api.github.com/repos/Dest1n640/study-skills/contents). These reads do not establish successful remote installation, or that the latest local changes have been published.

Scope assumption: “adapt the implementation” covers current repository identity references; inspection found no owner-specific product code or installer to change. Removing the specified README sections does not revoke the earlier confirmed skill-permission instructions. No unresolved decision blocks this documentation update.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

None. This documentation-only change uses `skip_specs: true`. Existing `distribution-validation` requirements already permit concrete repository addresses, require truthful installation claims, and do not require permission guidance to be in the README; the self-contained skills retain that guidance.

## Impact

Implementation targets: `README.md`, `README.ru.md`, `openspec/DECISIONS.md`, and `openspec/config.yaml`. No dependency, custom installer, skill identifier, Git remote, branch, runtime setting, or main specification needs changing. No publication or push is part of this change.

Verification: compare both languages, check local Markdown links and exact installation commands, confirm complete removal of both named sections, and verify that product skills and historical evidence remain unchanged. Remote installation remains explicitly untested unless separately exercised; this change does not add behavioral claims.
