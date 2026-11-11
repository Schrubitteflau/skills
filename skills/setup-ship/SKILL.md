---
name: setup-ship
description: "Set up a repo for /ship and /end-grilling, or audit that its setup still holds."
disable-model-invocation: true
---

`/ship` and `/end-grilling` assume a repo has **delivery rules** (`docs/agents/delivery.md`, the human's standing instructions for every delivery) and a **clean tree**. A repo without delivery rules gets them **scaffolded**; a repo that has them gets them **audited**. You write nothing to disk before the human has answered.

## Steps

1. **Gates.** Stop at the first that fails and tell the human what to do:
   - after a `git fetch`, the checkout holds the tip of the remote default branch; else they pull, since the rules may already be fixed upstream;
   - `docs/agents/issue-tracker.md` exists; else they run `/setup-matt-pocock-skills`.

2. **Audit.** When scaffolding, first draft the delivery rules from [delivery-template.md](delivery-template.md), in the template's language: every section filled from the environment (build scripts, CI, `docs/`, `git log`), every line written for its readers, the agents of `/ship` ([SKILL.md](../ship/SKILL.md), [reviewers.md](../ship/reviewers.md)). Then run every check of [checks.md](checks.md), on the rules or on your draft. Done when each check has a verdict: pass, or its **findings**.

3. **Present.** One message, in the human's language: each check's verdict; the findings, each led by its fix so they accept it in a word; when scaffolding, the draft; then your questions, each with your best guess, for what no file tells you: usually the off-limits data, the paid services, the real usage. They may edit anything. Done when every finding and every question has their answer.

4. **Write** what they confirmed, in the file's language: the fixes or the draft in `docs/agents/delivery.md`; and, when **Pointer** failed, this entry inside `## Agent skills` of `CLAUDE.md`, else `AGENTS.md` (neither: ask which to create), updated in place:

   ```markdown
   ### Delivery

   Rules for `/ship` (checks, off-limits data and services, commits). See `docs/agents/delivery.md`.
   ```

   Leave the change uncommitted for the human to review. Then rerun the checks: done when every check passes, or fails only on what they declined. Report what passed, what you fixed, what is left to them.
