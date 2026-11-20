## Why

The README shown by the user lists four learning modes, while the current checkout contains six. Readers should be able to find every study skill and choose a mode from one table.

## What Changes

- Use a two-column skill and behavior table at the top of each README, following the supplied example.
- Include one row for each current product skill: `study-hint-normal`, `study-hint-fast`, `study-guide-normal`, `study-guide-fast`, `study-review`, and `study-trace`.
- Give each skill a short description in the README's language. Make it clear that review gives evidence and hints for self-directed fixes and that trace follows one concrete input through existing code.
- Use `skills/*/SKILL.md` as the source for the list of product skills. Keep the introduction and full-set installation examples consistent with that list.

The user confirmed the full list and the two-column format. Both working-copy READMEs already contain candidate six-row tables as part of the earlier review and trace changes. Use those tables as the starting point for verification and correct any discrepancies in place.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

None. The existing distribution requirements already cover bilingual descriptions and full-set installation. This change documents the skills available in the current checkout.

## Impact

The implementation targets `README.md` and `README.ru.md`. It involves no skill behavior, installation tooling, or publication changes.
