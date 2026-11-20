## 1. Skill and metadata

- [x] 1.1 Create `skills/study-review/SKILL.md` in English. Check that it implements the scope selection, four review dimensions, evidence-backed findings, and hint-only repair behavior in the [review delta](specs/educational-code-review/spec.md).
- [x] 1.2 Add the MIT license copy and explicit-only metadata for Codex and Claude Code. Validate the name and description, parse the client settings, and compare the license copy with the root license.

## 2. Documentation and installation

- [x] 2.1 Update `README.md` and `README.ru.md` with the review use case, a finding and its hint, invocation examples, and individual and full installation selections. Check that both READMEs describe the same behavior and list the product skills present in the revision.
- [x] 2.2 Install review on its own and as part of the full selection from the local checkout in isolated Codex projects. Record the installed files and verify that no sibling is needed for individual use and that the full selection excludes OpenSpec helpers.

## 3. Codex behavior

- [x] 3.1 Add repeatable review prompts and fixtures to the existing evaluation setup. Reuse the positive-count fixture for a reproducible defect and check that the remaining inputs cover explicit scope, worktree changes, a clean project, and findings across the review dimensions.
- [x] 3.2 Exercise the three scope choices and an evidence-limited case. Verify correct scope and priority, source locations, expected and actual or source-derived results, and evidence or caveats for readability, architecture, and performance findings. Check that an issue-free scope yields no invented finding.
- [x] 3.3 Exercise both a request for corrected code in chat and a request for an automatic repair in writable Codex. Retain before and after snapshots and verify that each reply gives a more specific hint, leaves implementation and tests unchanged, and contains no ready-to-apply target correction.
- [x] 3.4 Check native explicit invocation and persistence, then explicitly switch to an implementation mode in the same session if the client interface supports it. Retain the client events and file evidence, and mark any unavailable sequence as not run.

## 4. Evidence and release status

- [x] 4.1 Record separate results for metadata, local installation, supplied-file behavior, native behavior, and publication status. Verify that results link to repeatable evidence and that each untested client, remote installation, or unpublished revision is described accurately.
