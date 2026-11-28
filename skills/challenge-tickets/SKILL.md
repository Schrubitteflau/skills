---
name: challenge-tickets
description: "Challenge a to-tickets draft with three independent reviewers on different models, down to the fewest tickets that still ship the spec."
disable-model-invocation: true
---

Run it while the `to-tickets` skill quizzes the human on its draft. The words after the command are the human's **constraints** (a ticket cap, what must be usable first); every brief carries them verbatim.

The **slicing rules** are those of the `to-tickets` skill: you and every reviewer read them in its skill file and apply them as they stand. This skill adds one reading and one cost:

- **Size.** The rules' size bound is measured against the agent that implements: a frontier coding agent, which carries a large slice in one context.
- **Ceremony.** Each ticket costs, under the `ship` skill, an implementer, three reviewers for up to three rounds, a merger, and merge conflicts with every ticket running beside it.

The target is the fewest tickets the slicing rules allow.

## Steps

1. **Draft.** Write the draft as `breakdown-v1.md` in your scratch space, in the format `to-tickets` quizzes with. Gather the paths the reviewers read: the spec, the decision journal where the `ship` skill keeps it (when it exists), `docs/adr/`, `docs/agents/delivery.md`, the code when there is some, and the installed skill files of `to-tickets` and `ship`. Done when the file and the path list exist.

2. **Review.** Three fresh subagents at once, read-only, each on its own model: three different models when the harness offers them, otherwise three reasoning efforts. Brief each with **context pointers**: the paths above, the constraints verbatim, this skill's size and ceremony lines, and its **lens**:

   | Lens | Reviewer | Reads the draft | Returns |
   |---|---|---|---|
   | **Blind** | a model unlike yours, high effort | no, so it starts unanchored | its own breakdown from the spec alone, fewest tickets; the ticket that gives the human a first real use |
   | **Coverage** | the strongest model, high effort | yes | every user story and implementation decision owned by exactly one ticket (orphans, doubles); every slicing rule checked ticket by ticket; anything against the journal or the ADRs |
   | **Delivery** | a faster model, high effort | yes, and the `ship` skill's files | what stalls an unattended `ship`: tickets editing the same files in parallel, steps only the human can do (accounts, paid calls, real data, another repo), criteria a reviewer cannot check by running something; questions the spec leaves open |

   On Claude Code: Blind on `fable`, Coverage on `opus`, Delivery on `sonnet`.

   Every lens also lists its **merges**: tickets that become one and still keep the slicing rules. Each report: English, under 600 words. Done when all three reports are in.

3. **Synthesis.** Start from the smallest credible proposal, often Blind's. Each ticket above that count names what it buys: the slicing rule that requires it, or a `ship` need (two tickets editing the same files in parallel, serialized; a spike whose outcome reshapes what follows). `ship` works every open sub-issue of the spec: a step only the human can do becomes the part an agent finishes plus what it names as left for the human, or it leaves this breakdown. Write `breakdown-v2.md`, the final numbered table: the one source the publish reads. Done when every finding is taken or rejected with a reason.

4. **Quiz.** Hand the result to the quiz of `to-tickets`: the count before and after, and each lens's count; what changed and which lens caught it; rejected findings, one line each; open questions in one batch, each with your recommendation; then the table. Append each answer to the journal in the entry format of the `end-grilling` skill, and update the table. When the human asks for another round, run the same lenses on the new table, each model on a lens it has not had, each reporting only what remains. Done when the human approves.

5. **Publish.** `to-tickets` publishes from the approved table. Done when the published issues match the table one to one.
