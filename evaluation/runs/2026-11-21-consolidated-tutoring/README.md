# Consolidated tutoring checks

The tests used Codex CLI 0.169.1 with `gpt-6.2-sol` and low reasoning effort in isolated workspaces. The supplied-file checks started with the tested skill text and the first learner request. Later requests resumed the same session. The native check used the installed packages. Hint sessions used read-only and approval policy never. Supplied guide implementation sessions used workspace-write and approval policy never.

[Observations](observations.json) contains the exact learner prompts, replies, starting fixture hashes, source diffs, command outputs, and judgments. The recorded reply links can point to temporary fixture locations. [Installation evidence](installation.json) records separate one-skill, full, and migration runs using Skills CLI 1.9.0.

| Check | Result |
| --- | --- |
| Matched hint pace | Quick explained why zero counted and pointed to the next edit. Detailed traced all three input values in a table. Both reproduced the expected failing test, preserved the fixture, and left the edit to the learner. |
| Matched guide pace | Quick gave the implementation decisions and checks concisely. Detailed unpacked the parsing steps and error cases. Both kept the parser and summarizer edits in the requested turns and passed the six-test suite after the second edit. The requested comprehension question came on turn 3. |
| Guide opening menu | Guide offered two choices and left the fixture byte-identical before selection. After “Быстро,” it implemented the pending parser request only and ran the parser checks. The unrequested summarizer still had its expected baseline failures. |
| Inline pace and broad requests | The deadline prompt went straight to a hint and a scoped algorithm comparison. Guide returned a plan without editing a file for both the multi-part analyzer and the one-function assignment. |
| Domain, alternatives, and flowcharts | Hint explained why a dictionary keyed by SKU would overwrite a distinct order, compared it with a list and grouped alternatives, and showed how factory lifetime affects the history. The separate report case produced a Mermaid flowchart covering missing IDs, negative totals, void status, and eligible rows. |
| Hint diagram boundary | The initial visual instruction yielded a complete filter flowchart during a request for the whole solution. After one clarification to the skill, the repeat gave a high-level overview plus a concrete lookup decision and left the missing flow to the learner. Both runs preserved the fixture. |
| Native Codex switching | Codex injected the installed hint on turn 1 and the installed guide on turn 5. Hint offered a text menu, resumed the original question, retained its pace on the next question, and accepted a change to Quick. Guide started immediately on the explicit Quick request, reported the read-only restriction, and preserved the code. The existing zero-quantity failure remained in the on-disk fixture. |
| Local installation | One-skill and full installs matched the documented selections. The migration removed all four legacy names and produced exactly the four current packages with matching content and lock entries. |

The button menu, interactive desktop discovery, Claude Code, and remote installation were not exercised. The consolidated revision was local at the time of testing. In the Detailed guide run, the parser checks passed before a Git diagnostic failed because the fixture was not a Git repository. The full suite passed on the following turn.
