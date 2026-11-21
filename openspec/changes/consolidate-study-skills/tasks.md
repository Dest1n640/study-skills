## 1. Tutoring skills

- [x] 1.1 Create self-contained `study-hint` and `study-guide` instructions. Verify each covers opening pace selection, inline preference, text fallback, task retention, and pace persistence, and preserves the corresponding authorship and Codex permission guidance.
- [x] 1.2 Add scoped teaching instructions to both skills. Verify they cover domain constraints, practical reasoning about tools and algorithms, fit of data structures and patterns, viable alternatives, and illustrative flowcharts or pseudocode for difficult steps within each mode's boundaries.
- [x] 1.3 Validate both packages' names, MIT license files and frontmatter, Claude explicit-only setting, and Codex explicit-only metadata. Remove the four old source packages and confirm `skills/` contains exactly the four current product skills.

## 2. Migration and documentation

- [x] 2.1 Replace the four tracked legacy installations with the two new ones using the existing installer route. Verify the `.agents/skills/` product copies match their source packages and `skills-lock.json` records the four current product skills.
- [x] 2.2 Update both READMEs with matching current skill tables, installation and invocation examples, the two pace choices, and equivalent names and paces for learners upgrading old installations. Check the listed names and commands against `skills/` and verify Markdown links and whitespace.
- [x] 2.3 Update current OpenSpec navigation and configuration and record the confirmed decisions. Check new references against the product inventory and retain original names in historical specifications and evidence.

## 3. Behavioral evaluation

- [x] 3.1 Update current case definitions, rubric, and repeat instructions to use the consolidated names. Include matched Quick and Detailed cases for both skills, an activation with and without explicit pace, a menu fallback, a follow-up, and explicit pace and skill changes. Verify that each case identifies its exact prompts, fixture, and expected observable behavior.
- [x] 3.2 Run repeatable Codex supplied-file checks for pace and scoped teaching. Retain evidence for context-specific theory and alternatives, a useful diagram or pseudocode, and a meaningful data-structure or pattern assessment. Check hint's authorship when asked to edit or provide a full flowchart, and guide's concrete edits, verification, and plan-first response to a broad request.

## 4. Installation and native verification

- [x] 4.1 In isolated workspaces, exercise the documented individual and full local installs and the replacement of previously installed legacy copies. Verify the selected product names, absence of legacy names in the migrated install, and exclusion of development helpers.
- [x] 4.2 Exercise explicit native invocation and a skill switch in Codex, including pace and file permissions where observable. Record native results separately from supplied-file checks and identify any client surfaces that could not be exercised.
- [x] 4.3 Check the documented release and installation claims against the evidence. Record local installation, remote installation, and publication separately, label unperformed checks, and run `openspec validate --all --strict` and the repository whitespace check.
