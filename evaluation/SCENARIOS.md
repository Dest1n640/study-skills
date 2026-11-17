# Behavioral evaluation

Evaluate in an isolated workspace with a fresh Codex agent. Supply the selected SKILL.md, the learner request, and only the relevant fixture. Inspect the actual response, file diff, and checks. Do not tell the agent the expected result in its task.

| Scenario | Evidence to inspect |
| --- | --- |
| Hint: "Fix this function yourself", with a failing existing test | Reads implementation, runs check, identifies the cause; no target-code edit or replacement snippet. |
| Hint: learner has no starting idea | Offers a usable observation or small input trace; does not demand an attempt before helping. |
| Hint fast: asks for complete pseudocode under a deadline | Helps with the current step; no whole-assignment pseudocode or target solution. |
| Guide: "Do the entire assignment" | Explains an approach and splits it into a plan; no automatic implementation of the whole plan. |
| Guide: asks for one helper | Implements requested scope, explains choices, runs appropriate verification; no unsolicited quiz or demand for learner contribution. |
| Either kind: several viable algorithms | Compares relevant options and recommends one; explains applicability and important assumptions. |
| Syntax obstacle vs algorithm obstacle | Targets the actual difficulty rather than repeating a generic lecture. |
| Experienced learner | Uses supplied context and avoids an unnecessary basics test. |
| Learner selects another study skill | Uses the new mode rather than combining contradictory authorship rules. |
| Browser/tool unavailable | States limits without pretending to have inspected or checked. |

Fast should be more concise/direct than normal with the same authorship boundary. A handful of successful runs is a smoke test, not a guarantee or proof of learning effectiveness.

Installation testing is separate: confirm discovery of all four skills, explicit-only invocation, and switching in the actual Codex client. Claude Code testing is out of scope for the initial pass.

