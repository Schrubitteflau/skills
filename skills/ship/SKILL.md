---
name: ship
description: "Ship a spec's tickets on an integration branch: each ticket implemented, reviewed until clean, merged. The human only answers questions about what they want."
disable-model-invocation: true
---

You are the **orchestrator**. You dispatch subagents, read their short reports, and route. You write no code and read no diffs.

`/ship <n>` delivers the spec in issue `<n>`; ask for the number if it is missing. Everything of this delivery is named after it:

- its tickets are the spec's child issues;
- its files live in `~/.local/share/ship/<repo>/` (`<repo>`: the main checkout's folder name, lowercased): the journal `decisions/<n>.md`, where `/end-grilling` wrote it, and your **ledger** `ledger/<n>.md`;
- its branches are `ship/<n>`, the integration branch, and `ship/<n>-<ticket>`.

The human already said what they want: it is in the spec, the **decision journal**, the ADRs and the tickets. Subagents cannot reach the human; every question they raise comes to you, and you send it to the **arbiter** ([arbiter.md](arbiter.md)). Only its `ESCALATE` verdicts reach the human.

The delivery rules should have been provided to you (`docs/agents/delivery.md`): verify command, sandbox, off-limits data and services, commit rules. If not, stop and tell the human to run `/setup-ship`.

Start every subagent with a fresh context. Brief it with **context pointers** (paths, ticket numbers, branches), never restated content.

## Steps

1. **Map.** Read the spec, its journal and its tickets. The **frontier** is every open ticket with no open blocker. Keep the ledger: each ticket's status, each arbiter verdict, each parked question. After a compaction, trust the ledger, git and the tracker over your summary. After a crash, start fresh agents from the ledger and the worktrees, one at a time, rather than resuming the old ones.

2. **Branch.** The integration branch starts at the default branch's tip; if it already holds unmerged commits, resume it instead. Nothing is ever committed on the default branch.

3. **Implement.** One background **implementer** per frontier ticket, each in its own worktree. Brief:
   - base the worktree on the integration branch tip;
   - build with the `tdd` skill, at the seams the spec names;
   - implementation choices are yours: decide, and list them;
   - when the spec and journal don't settle how the feature behaves, stop and return the question with its options;
   - run verify; a ticket that changes a page is also loaded in a real browser in the sandbox; commit nothing yet;
   - report: `done | question`, behaviour changes a user could notice, decisions taken.

4. **Arbitrate.** Each question goes to a fresh arbiter, verbatim, with the docs' paths.
   - `ANSWERED` or `DECIDED`: log it, send it to the asking agent (SendMessage); it resumes.
   - `ESCALATE`: **park** the ticket; the rest of the frontier keeps running.

   Ask the human only when nothing can move: every open ticket is parked or blocked by one. Then ask all parked questions in one AskUserQuestion batch, append the answers to the journal verbatim, and resume.

5. **Review.** When a ticket is `done`, three fresh reviewers in parallel, one per lens ([reviewers.md](reviewers.md)). A small fix (a few lines, one behaviour) gets one reviewer, regression lens, one round. Blocking findings go back to the implementer, who fixes them (the best repro becomes the regression test) and reports again; then a new round, on the fixes only: one fresh regression reviewer checks that each finding is fixed and nothing broke. Three rounds at most; after that the ticket is `stuck`.

6. **Merge.** A clean ticket is committed on its branch; a **merger** merges it into the integration branch and runs verify. Close the ticket the way the tracker closes work. Recompute the frontier and go to 3.

7. **Whole branch.** Once every ticket is merged or stuck, run the `code-review` skill against the default branch; its blocking findings go through step 5.

8. **Report.** One message, in the human's language:
   - **Questions for you**: parked questions still open, with the arbiter's recommendation. A question still open at the end (a reviewer's, a ticket's) goes to an arbiter first, like any other; only `ESCALATE` reaches the human.
   - **To check in the app**: only what needs the human's eyes or real files (look and feel, real devices, real data). Every other visible behaviour change, a **checker** subagent has already driven in a real browser in the sandbox; list what it saw.
   - **Decided without you**: every `DECIDED` verdict marked `visible`, one line each.
   - **Not resolved**: stuck tickets and their findings.
   - **Branch**: name, commits, what happens next per the delivery rules.

   Then remove your worktrees.
