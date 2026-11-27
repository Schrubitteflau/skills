---
name: ask-ship
description: "Ask where a delivery stands in the ship flow and which skill comes next."
disable-model-invocation: true
---

The human runs the ship flow by hand and asks you where a delivery stands. You are a **signpost**: you read the evidence, point at the next skill, and leave every run to the human.

The **flow**, one row per step. A step is done when its **artifact** exists; the skill that writes it says where (`~/.claude/skills/<name>/SKILL.md`), and `docs/agents/issue-tracker.md` says how to read the tracker. `<n>` is the spec's issue number.

| Step | Skill | Artifact |
| --- | --- | --- |
| 0 | `/setup-matt-pocock-skills`, then `/setup-ship`; once per repo | `docs/agents/issue-tracker.md`, `docs/agents/delivery.md` |
| 1 | `/grill-with-docs` | every decision the feature needs, taken by the human |
| 2 | `/to-spec` | the spec, issue `<n>` |
| 3 | `/end-grilling`, in the grilling's session | the decision journal of `<n>` |
| 4 | `/to-tickets` | the sub-issues of `<n>` |
| 5 | `/ship <n>` | the integration branch, every ticket merged or stuck |
| 6 | the human: review the branch, act on the report | the branch merged per the delivery rules |

A multi-ticket feature, grilled first, in a repo with a verify command and a sandbox, rides this flow. Anything else (a single ticket, a need still fuzzy, a cloud session) belongs to `/ask-matt`.

## Steps

1. **Locate.** Take `<n>` from the human's words or the conversation; ask for it only when the tracker holds several candidate specs. Check every row's artifact against the repo, the tracker and the skill's stated location. Done when each row is marked present or missing with the evidence you saw, or the delivery is placed off the flow.

2. **Point.** A few lines, in the human's language: the rows done, with their evidence; the first missing row's skill, as the exact command, and why it comes now; every row done out of order, with what it costs (tickets cut before the journal, the arbiter missing decisions). Done when the human has that command.
