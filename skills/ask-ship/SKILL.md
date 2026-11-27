---
name: ask-ship
description: "Ask where you are in the ship flow and which skill comes next."
disable-model-invocation: true
---

The human runs the ship flow by hand and asks you where they stand. You locate the delivery on the **flow** below from what is on disk and in the tracker, then name the next skill. You run nothing: the human invokes every skill.

Before stating what a skill does, read its `SKILL.md` (`~/.claude/skills/<name>/SKILL.md`): the lines here are for orientation only.

## The flow

The spec's issue number `<n>` names everything of a delivery. `<repo>` is the main checkout's folder name, lowercased (first line of `git worktree list`).

| Step | Skill | Done when |
| --- | --- | --- |
| 0 | `/setup-matt-pocock-skills`, then `/setup-ship`, once per repo | `docs/agents/issue-tracker.md` and `docs/agents/delivery.md` exist |
| 1 | `/grill-with-docs` | the human has decided everything the feature needs |
| 2 | `/to-spec` | the spec is issue `<n>` |
| 3 | `/end-grilling`, in the grilling's session | `~/.local/share/ship/<repo>/decisions/<n>.md` exists |
| 4 | `/to-tickets` | issue `<n>` has sub-issues |
| 5 | `/ship <n>` | every sub-issue is closed or reported stuck; `ship/<n>` holds the work |
| 6 | the human reviews `ship/<n>` and acts on the report | `ship/<n>` is merged per the delivery rules |

Steps 1 to 4 share one context window: `/end-grilling` reads the grilling's turns, so a step 3 run elsewhere points it at that session's `.jsonl`. `/ship` resumes from its ledger, `~/.local/share/ship/<repo>/ledger/<n>.md`, and from the `ship/<n>` branches.

## Off the flow

`/ship` fits a multi-ticket feature, grilled first, in a repo with a verify command and a sandbox. A single ticket, a need still fuzzy, no grilling, or a cloud session: point to `/ask-matt`, which routes the rest.

## Steps

1. **Locate.** Get `<n>` from the human's words or the conversation; ask for it only when the tracker shows several candidate specs. Check each step's done-when, in order, against the repo, the delivery folder and the tracker. Done when you can name the first step whose done-when fails, or the delivery is off the flow.

2. **Answer.** A few lines, in the human's language: what is done, with the evidence you saw; the next skill, with the exact command and why it comes now; anything out of order, such as tickets cut before the journal was written. Then stop.
