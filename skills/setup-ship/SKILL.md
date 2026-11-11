---
name: setup-ship
description: "Configure this repo for /ship and /end-grilling, or check that its configuration still holds: the delivery rules, and a tree free of specs, journals and vendored skills. Run before the first /ship, and again after a skills update."
disable-model-invocation: true
---

# Setup ship

Scaffold and check what `/ship` and `/end-grilling` assume of a repo:

- **Delivery rules** (`docs/agents/delivery.md`): the human's standing instructions for every delivery, so they never paste them again.
- **A clean tree**: specs live in the issue tracker, decision journals and ledgers in `~/.local/share/ship/`, skills at user level. None of them is committed.

A repo with no delivery rules and a repo whose rules have aged go through the same process: explore, check, present, confirm, write.

## Process

### 1. Explore

Look at the current repo to understand its starting state. Read whatever exists; don't assume:

- Is the checkout current? `git fetch`, then compare the default branch (`gh repo view --json defaultBranchRef`) with its remote. Behind means the rules may already be fixed upstream: stop and ask the human to pull.
- `docs/agents/issue-tracker.md`: its absence means `/setup-matt-pocock-skills` has not run. Stop and tell the human to run it first: `/ship` needs a tracker that holds a spec and its child tickets.
- The skills a delivery calls: `to-spec`, `to-tickets`, `end-grilling`, `ship`, `tdd`, `code-review`. Each is installed when `~/.claude/skills/<name>/SKILL.md` exists; a missing one is a finding, its fix an install.
- `docs/agents/delivery.md`: does this skill's prior output already exist?
- `CLAUDE.md` and `AGENTS.md` at the repo root: is there a `### Delivery` entry in an `## Agent skills` section?
- The tree (`git ls-files`; untracked files don't count): spec files, decision journals, vendored skills.

### 2. Check

Hold the existing delivery rules against the seed template, [delivery-template.md](./delivery-template.md), and against the repo. A repo with no delivery rules skips **Shape**, **Standing** and **True**.

- **Shape.** Every section and bullet of the template is there, and nothing survives from an older template: a journal or ledger path, a branch naming scheme, a place for specs. A bullet the project added for itself (where its worktrees live, how gentle its builds are) is fine.
- **Standing.** Every line holds for every delivery. What belongs to one delivery (its spec, its tickets, its branches, its journal) comes from `/ship <n>`, never from this file: flag a spec or ticket number given as the work to do, and a branch name. A number inside an example or a note of history stays.
- **True.** Each fact still holds. Existence is the bar: run a command only when the human asks, since a full verify can take minutes.
  - A path named exists (`test -e`, with `~` expanded, globs and paths relative to a subfolder resolved from the line's context). Probing an off-limits path for existence is not reading it. A path the line says is created on demand passes; one that is missing without saying so is a finding.
  - A command named is defined in the build scripts or installed on the machine (`command -v`). One the line itself announces as not existing yet passes.
  - A file of the repo named is tracked, or ignored on purpose (build output, dependencies).
  - The default branch is the one named.
- **Clean tree.** No spec file (`docs/spec-*`, `.scratch/`), decision journal (`*.decisions.md`, `docs/decisions/`) or vendored skill (`.agents/skills/`, `.claude/skills/`, `skills-lock.json`) is tracked. A skill written for this repo alone, absent from `skills-lock.json`, is not vendored: leave it and say so.
- **Pointer.** The `### Delivery` entry exists, names `docs/agents/delivery.md`, and its summary promises only what the rules still hold.

A **finding** is one line of the rules, or one group of files, that fails: the fix you propose, where it comes from, the checks it fails and why. A line that fails several checks is one finding. Done when every check has a verdict, pass or findings.

### 3. Present findings and ask

State what exists and what is missing, give each check its verdict, then list the findings, each led by its fix so the human can accept it in a word.

For a repo with no delivery rules, draft them from the template. Fill every section from the environment: build scripts and task runners (`package.json`, `justfile`, `Makefile`, `Cargo.toml`), CI, `docs/`. Then ask, in one round with your best guesses, only what no file tells you: usually the off-limits data, the paid services and the real usage.

### 4. Confirm and edit

Show the human the draft or the diff of `docs/agents/delivery.md`, and the `### Delivery` entry. Let them edit before writing.

A **Clean tree** finding is theirs to settle: name the files you would remove, and what else refers to them (a README link, a pointer), then wait. Removing a spec or a journal from the tree means moving it to where it belongs first, the tracker or `~/.local/share/ship/<repo>/`.

### 5. Write

Write `docs/agents/delivery.md`.

**Pick the file that holds the pointer:** `CLAUDE.md` if it exists, else `AGENTS.md`; if neither exists, ask the human which one to create. Edit the one already there, and update an existing `### Delivery` entry in place.

The entry, inside `## Agent skills`:

```markdown
### Delivery

Rules for `/ship` (checks, off-limits data and services, commits). See `docs/agents/delivery.md`.
```

Commit nothing: the human reviews the change.

### 6. Done

Tell the human what passed, what you fixed, and what is left to them. They can edit `docs/agents/delivery.md` directly later; re-running this skill is worth it after a skills update, or when the project's tooling moves.
