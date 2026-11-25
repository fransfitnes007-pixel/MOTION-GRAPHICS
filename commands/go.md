---
description: "Run the GO routine for one account: one finished vertical video per sub niche, built in parallel, checked and dropped"
argument-hint: "<account> [notes for this batch]"
---

Account and notes: $ARGUMENTS

Use the `multi-account-content` skill. Read `pipelines/multi-account-content/PLAYBOOK.md` and the account's
`pipelines/multi-account-content/accounts/<account>.md`. If its FORMAT LOCK is empty, do not batch: make one test video
and ask the owner to approve it first. Otherwise check the store listing (`tools/store_lookup.sh`), run every script through `tools/claim_check.py`, and
follow PLAYBOOK section 7 to the end and finish with what was dropped
where, what was not checked, and `Say "GO" for the next batch.`
