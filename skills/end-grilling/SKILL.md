---
name: end-grilling
description: "End a grilling: write every decision the human made, in their own words, to the decision journal, kept outside the repo."
disable-model-invocation: true
---

The spec keeps what was decided. The **decision journal** also keeps how the human said it, what they rejected and why, and what they pushed out of scope. During `/ship`, the arbiter answers from it instead of asking again: a decision missing here is a question asked twice.

Run it at the end of the grilling session, after `/to-spec`.

## Steps

1. **Turns.** The source is this conversation. If the human points to a past session (a `.jsonl` under `~/.claude/projects/`), run [extract-turns.py](extract-turns.py) on it (`python3 -I extract-turns.py <session.jsonl> > <scratch>/turns.md`) and read that.

2. **Path.** The journal lives outside the repo: one file that every worktree reads and appends to, out of git's reach. Use the path the delivery rules name (`docs/agents/delivery.md`, Docs); else `~/.local/share/ship/<repo>/decisions/<slug>.md`, where `<repo>` is the main checkout's folder name, lowercased, and `<slug>` the spec's. If the journal exists, append; never rewrite entries.

3. **Decisions.** Walk the turns in order. A decision is an answer, a "yes" to a recommendation (record what it accepted), an unprompted want, a rejection, a deferral, a correction. One entry each, grouped by topic:

   ```markdown
   ### D<n>: <title>

   - **Asked**: <what the human was choosing between>
   - **Answer**: "<their words, verbatim; trim only filler>"
   - **Decision**: <what this commits the feature to>
   - **Spec**: <section, or `not in spec`>
   ```

   A later turn that overrides an earlier one: keep both, mark the earlier `superseded by D<m>`.

   Done when every user turn is accounted for: it produced entries, or it carried no decision.

4. **Gaps.** Show the human every `not in spec` entry and every contradiction with the spec, with the spec fix you'd make. Apply the ones they accept.

5. **Write** the journal, headed with the spec and the session date. If `docs/agents/delivery.md` exists and names no journal path, add this one under Docs.
