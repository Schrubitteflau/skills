# Delivery rules

`docs/agents/delivery.md` holds the human's standing instructions for `/ship`, so they never paste them again.

To write it, fill every section from the environment (`CLAUDE.md`, build scripts, CI, `docs/`). Ask the human, in one round with your best guesses, only what no file tells you: usually the off-limits data and the paid services. Then add a pointer to it in `CLAUDE.md`'s agent-skills section.

Write only what holds for every spec. What belongs to one delivery (its spec, its tickets, its branches, its journal) comes from `/ship <n>`, never from this file.

```markdown
# Delivery

Read by `/ship` and its subagents.

## Checks

- Verify: `<command>`, on every ticket and on the integration branch.
- Manual check: `<sandbox command>`; <how to stop it, what it isolates>.
- Real browser: <how an agent loads a page headless and reads its console errors>.

## Off-limits

- Real data, never read or written: <paths>.
- Real actions, never performed: <actions>.
- Paid services, never called for real: <service, and what may run instead>.
- Shared resources: <e.g. the human's dev server>.

## Branches and commits

- Running `/ship` is the human's request to commit on its `ship/<n>` branches, never on the default branch.
- Commit messages: <language and style>.
- At the end: <push, PR, who merges>.

## Docs

- ADRs, glossary: <where>. Review standards: <file>.

## Real usage

<Who calls the code and with what: typical inputs, sizes, how many at once. Reviewers block only on these.>

## Project edge cases

<Failure modes this project has already met.>
```
