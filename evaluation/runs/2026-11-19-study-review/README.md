# Study review evaluation on 19 November 2026

The tested [skill](skill.md) and [Codex policy](policy.yaml) match the installed files. The [installation record](installation.json) covers two isolated Codex projects using Skills CLI 1.9.0. Individual installation contained only `study-review`. Full installation contained the five product skills and excluded OpenSpec helpers. Installed skill, policy, and license hashes matched the checkout.

Codex CLI 0.169.1 ran the [review cases](../../cases.json) in separate synthetic workspaces. Each `run.json` records the starting files, exact prompts and command arguments, tool events, and before and after snapshots. Observer checks appear separately from the tutor's checks. For repeatable setup, see [REPEAT.md](../../REPEAT.md).

| Supplied-file case | Result | Evidence |
| --- | --- | --- |
| Explicit scope | Pass. Reviewed only `order_count`, ran its targeted test, and reported no findings. | [Response](review-explicit-scope/response-1.md) · [Run](review-explicit-scope/run.json) |
| Current changes | Pass. Read the diff, found the changed predicate, observed that `[0]` returns `1` instead of `0`, and gave a hint. | [Response](review-worktree/response-1.md) · [Run](review-worktree/run.json) |
| Whole clean project | Pass. Reviewed requirements, code, and tests. Led with the broken storage boundary and zero exclusion, then explained the repeated scan and identified runtime as unmeasured. | [Response](review-whole-project/response-1.md) · [Run](review-whole-project/run.json) |
| Readability | Pass. Showed why the compound negation hides the inclusion rule and used the zero case to illustrate its consequence. The hint asks the learner to express the inclusion rule in words. | [Response](review-readability/response-1.md) · [Run](review-readability/run.json) |
| Source-only evidence | Pass. Derived the `2` versus `1` counterexample from the source and stated that the program and tests were not run. | [Response](review-source-only/response-1.md) · [Run](review-source-only/run.json) |

All five supplied-file cases preserved the fixture and its initial Git status. The intentionally buggy fixtures produced the expected failures in cases where tests were run.

## Native Codex

- **Review alone passed.** The client injected `study-review` from an individual installation. The tutor ran the tests, explained the defect, and left the fixture untouched. [Response](native-one/response-1.md) · [Run and injection record](native-one/run.json)
- **Review and switch passed in one writable session.** The client injected the installed review skill on turn 1 and the installed guide skill on turn 4. Turns 2 and 3 gave more specific hints for requests to copy a ready fix and to edit the file. The source and tests were byte-identical during review, and neither reply supplied the corrected target line. The explicit guide switch changed only the comparison, and the tutor and observer suites both passed all three tests. [Finding](native/response-1.md) · [Chat request](native/response-2.md) · [Edit request](native/response-3.md) · [Switch](native/response-4.md) · [Run and injection record](native/run.json)

The native records identify the model from the client's session metadata and verify that each injected skill body matches its local installed file. The supplied-file command output does not identify the model. These are bounded smoke checks. Remote installation, publication of this revision, behavior in other clients, and learning outcomes remain unverified.
