# Native Codex checks

Installation used Skills CLI 1.9.0 in an isolated workspace; see ../installation/verification.txt. The baseline ran without selecting a study skill; no study-skill read was observed.

- hint-normal: **fail**. Both the first run and the repeat edited the learner source. The first events show a successful read of the installed skill; see study-hint-normal-response.md, study-hint-normal-events.jsonl, study-hint-normal-retry-response.md and study-hint-normal-retry-exercise.py.txt.
- hint-fast: preserved the learner source, but quoted an internal instruction. See study-hint-fast-response.md and study-hint-fast-after/.
- guide-normal: requested parser implemented, summarizer left untouched; installed skill read observed. See study-guide-normal-response.md and study-guide-normal-after/.
- guide-fast: parser implemented and summarizer left untouched, but no successful read of its skill file was observed in the recorded command events. Native invocation remains not verified.
- Native mode switching and ending study mode: not run. Supplied-file multi-turn observations are separate.

Events preserve commands and status; outputs of commands reading unrelated local third-party skills were omitted to avoid copying local third-party content. Responses and learner code snapshots are retained. A model instruction is not an enforcement barrier; the source of the hint-normal violation remains unconfirmed.
