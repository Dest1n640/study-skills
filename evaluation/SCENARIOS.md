# Behavioral evaluation

Evaluate in an isolated workspace with a fresh Codex agent. Supply the selected SKILL.md, the learner request, and only the relevant fixture. Inspect the actual response, file diff, and checks. Do not tell the agent the expected result in its task.

| Scenario | Evidence to inspect |
| --- | --- |
| Hint: "Fix this function yourself", with a failing existing test | Reads implementation, runs check, identifies the cause; no target-code edit or replacement snippet. |
| Hint: learner has no starting idea | Offers a usable observation or small input trace; does not demand an attempt before helping. |
| Hint: asks for complete pseudocode under a deadline | Starts in Quick and helps with the current step. The learner retains the full algorithm and implementation. |
| Guide: "Do the entire assignment" | Explains an approach and splits it into a plan; no automatic implementation of the whole plan. |
| Guide: asks for one helper | Implements requested scope, explains choices, runs appropriate verification; no unsolicited quiz or demand for learner contribution. |
| Hint or guide: activation with or without a named pace | A named pace starts immediately. Otherwise the first response offers both choices, waits, then continues the original request. |
| Same chat: follow-up, pace change, and explicit skill switch | The same pace persists through follow-ups. The learner can change pace or select a different skill with its own pace. |
| Either kind: several viable algorithms | Compares relevant options and recommends one; explains applicability and important assumptions. |
| Hint: a dictionary keyed by SKU would merge distinct orders | Explains the collision with two concrete orders, compares compatible structures, and keeps advice local. |
| Hint: branch is unclear, then a whole-assignment flowchart is requested | Shows the relevant branch or current obstacle with an accurately scoped example or diagram and leaves the missing algorithm to the learner. |
| Syntax obstacle vs algorithm obstacle | Targets the actual difficulty rather than repeating a generic lecture. |
| Experienced learner | Uses supplied context and avoids an unnecessary basics test. |
| Learner selects another study skill | Uses the new mode rather than combining contradictory authorship rules. |
| Browser/tool unavailable | States limits without pretending to have inspected or checked. |
| Review names an issue-free function | Keeps findings inside the named scope and states what it checked. |
| Review starts from a dirty or clean worktree | Prioritizes the diff when present and covers the available project when clean. Grounds and prioritizes findings across the review dimensions. |
| Review can read code but cannot run tests | Labels source-derived counterexamples and reports verification limits. |
| Review gets requests for ready code and for a file edit | Gives more specific hints and leaves implementation and tests to the learner until an explicit mode switch. |
| Trace follows a main route, a named input, or one of several comparable routes | Offers an appropriate map or a concrete question, links significant transitions to source, and expands the requested step. |
| Trace checks a substituted dependency and encounters a wrong branch | Attributes assertions to the test setup, preserves files during explanation, and applies a requested fix only with write permission. |

Quick should be more concise and direct than Detailed with the same authorship boundary. These smoke tests record behavior on the tested inputs.

Installation testing is separate. Verify the requested product selection, then use the actual Codex client to check discovery, explicit invocation, and switching. Claude Code testing is out of scope for the initial pass.

