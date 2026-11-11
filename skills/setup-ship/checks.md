# Checks

A **finding** is one thing that fails (a line of the delivery rules, a group of files, a missing entry or skill): its fix, where it is, the checks it fails and why. A line that fails several checks is one finding. A fix that hangs on a fact only the human knows carries its question and your best guess.

**Existence** is the bar: a command the rules name runs only when the human asks, since a full verify takes minutes.

## Skills

`to-spec`, `to-tickets`, `end-grilling`, `ship`, `tdd` and `code-review` are installed: `~/.claude/skills/<name>/SKILL.md` exists (a user-invoked skill is absent from your skill list). Fix: install it.

## Shape

Every section and bullet of [delivery-template.md](delivery-template.md) is there, judged by meaning, not wording; one with nothing to say stays and says so. Nothing survives from an older template: a journal or ledger path, a branch naming scheme other than `ship/<n>`, a place for specs. A bullet the project added for itself (where its worktrees live, how gentle its builds are) passes.

## Standing

Every line holds for every delivery. What belongs to one (its spec, tickets, branches, journal) comes from `/ship <n>`: flag a spec or ticket number given as the work to do, and the name of one delivery's branch. A number in an example or a note of history passes.

## True

Every fact a line states still holds. The common ones:

- a path exists, `~` expanded, globs read from the line's context, relative paths from the main checkout or the subfolder the line is about. Probing an off-limits path for existence is not reading it. Two absences pass: a path the line calls created on demand, and a path under a folder ignored on purpose (build output, dependencies);
- a file of the repo is tracked, or was just written by this skill;
- a command is defined in the build scripts or installed on the machine. One the line announces as yet to come passes;
- the default branch, where a line names it, is the right one.

## Clean tree

Among tracked files (`git ls-files`): no spec (`docs/spec-*`, `.scratch/`), no decision journal (`*.decisions.md`, `docs/decisions/`), no vendored skill (`.agents/skills/`, `.claude/skills/`, `skills-lock.json`). A skill written for this repo alone, absent from `skills-lock.json`, passes: say so.

The fix is the human's to settle: name the files and what refers to them (a README link, a pointer), and wait. A spec or a journal leaves the tree by moving to where it belongs: the tracker, or `~/.local/share/ship/<repo>/`.

## Pointer

`## Agent skills` holds a `### Delivery` entry that names `docs/agents/delivery.md` and promises only what the rules still hold.
