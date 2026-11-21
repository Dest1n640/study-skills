## Why

Learners currently choose both who writes the code and how much explanation they want by picking one of four skill names. Put the pace choice inside each tutoring skill and make the explanations easier to follow by connecting decisions to the exercise's domain, requirements, and relevant code.

## What Changes

- **BREAKING** Replace `study-hint-normal`, `study-hint-fast`, `study-guide-normal`, and `study-guide-fast` with `study-hint` and `study-guide`. Keep `study-review` and `study-trace` available as independent skills.
- On activation, offer **Quick** and **Detailed** when the learner has not already stated a pace. Use a choice control when available and a text menu otherwise. When the learner gives a clear preference up front, continue at that pace immediately. Retain the selection in the current conversation until the learner changes it, switches skills, or ends tutoring.
- Keep the existing authorship boundaries. Hint leaves the assignment to the learner. Guide can implement concretely requested parts, starts broad requests with a plan, and offers comprehension checks on request.
- Ground explanations and advice in the relevant part of the task. Explain why important tools, algorithms, data structures, and design patterns fit. Compare viable approaches when the choice matters and show where each applies.
- Use a small example, pseudocode, or a flowchart when it helps the learner follow a difficult mechanism, branch, or data flow. Keep detailed hint pseudocode and diagrams limited to the current obstacle.
- Update installation and invocation examples and add a short migration table to both READMEs.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `study-modes` defines the new skill names, pace selection and persistence, and hint's scope for detailed diagrams as well as pseudocode.
- `learning-assistance` defines how tutoring uses domain requirements, explains choices, checks structures and patterns, and illustrates the relevant code.
- `distribution-validation` defines the new installable inventory, migration documentation, and matched pace checks within each skill.

## Impact

- Product files in `skills/`, their tracked local copies in `.agents/skills/`, and their entries in `skills-lock.json`.
- Both public READMEs, the OpenSpec index and context, and current evaluation procedures and cases. Preserve historical run evidence under its original skill names.
- The documentation checks in `list-all-study-skills-in-readmes` overlap with the inventory update. Run those checks against the new inventory and coordinate that separate change's status explicitly if needed.
- Learners who installed the old copies need migration instructions for replacing them at the scope where they were installed.
