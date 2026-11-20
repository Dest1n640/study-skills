## 1. Skill and metadata

- [x] 1.1 Create `skills/study-trace/SKILL.md` in English with source-backed route selection, a project map, one concrete input, on-demand detail, conditional diagrams, evidence handling, and scoped repairs. Check the instructions against the [code-tracing delta](specs/code-tracing/spec.md), including permission-limited sessions.
- [x] 1.2 Add the MIT license and explicit-only metadata for Codex and Claude Code. Validate the skill name and description, parse both YAML settings, and compare the license copy with the root license.

## 2. Documentation and local installation

- [x] 2.1 Update `README.md` and `README.ru.md` with the trace use case, one grounded walkthrough example, invocation syntax, and individual and full installation selections. Check that both languages list the same available product skills and explain when trace can apply a repair.
- [x] 2.2 Exercise individual trace installation and full product installation from the local checkout in isolated Codex projects. Record the installed files and verify that individual selection needs no sibling skill and full selection excludes OpenSpec helpers.

## 3. Codex behavior and evidence

- [x] 3.1 Add repeatable trace prompts and minimal fixtures to the existing evaluation setup, reusing suitable cases. Check that the fixtures have a verifiable principal route, a comparable-routes case, and a runtime boundary or a test using a substitute dependency.
- [x] 3.2 Exercise unscoped invocation with a clear route, an explicit user goal, a comparable-routes choice, and a request to expand one step. Check the first response, source locations, selected branch and values, use of a helpful diagram, and scope of any execution claim. Retain the run evidence.
- [x] 3.3 Exercise a walkthrough that exposes a problem, a direct repair in writable Codex, and a blocked repair in read-only Codex. Compare file snapshots and executed checks, and verify that only the requested repair changes files and that the response explains the changed route.
- [x] 3.4 Check native explicit invocation, lack of implicit activation, and the effect of explicitly selecting trace from hint in a client that supports the sequence. Retain client evidence and list any sequence the test environment cannot establish as not run.
- [x] 3.5 Update the results with separate judgments for metadata, local installation, supplied-file behavior, and native behavior. Verify that evidence is linked and that remote installation, publication, and other-client testing retain their actual status.
