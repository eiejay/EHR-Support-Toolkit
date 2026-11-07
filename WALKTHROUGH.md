# Walkthrough

A guided tour of the projects in this repository: what to run, what you should see, and how each piece is used on a real support shift.

## Before you start

You need Python 3 (any recent version) for the two scripts. Everything else is documents and data files. No packages to install; both scripts use only the standard library.

    git clone https://github.com/eiejay/EHR-Support-Toolkit.git
    cd EHR-Support-Toolkit

## 1. Ticket Priority Tool

    cd projects/ticket-priority-tool
    python3 triage_priority.py

Answer the four questions. A worked example: the EHR is down for one unit during med pass.

    Category (access, workflow, data, interface, system): system
    Is patient care blocked right now? (y/n): y
    How many users are affected? (one, unit, facility): unit
    Is there a workaround? (y/n): n

    Priority: P1
    Response target: 15 minutes
    Score: 8 (category 3, care blocked +3, unit affected +1, no workaround +1)
    First steps: page the on-call analyst, open the incident record, notify the house supervisor, start the downtime log if the outage will pass 30 minutes.

Try a quiet one: category access, care not blocked, one user, workaround yes. It lands on P4 with next business day as the target, which is exactly where a single password problem belongs while a med pass is waiting elsewhere.

## 2. Downtime Kit checker

    cd ../downtime-kit
    python3 kit_check.py kit_inventory.csv

What you should see:

    Items reviewed: 8
    Problems: 4
      - Paper order sheets (pack of 25): SHORT, 1 on hand of 2 required
      - Downtime admission packets: STALE, last checked 2026-10-20 (over 14 days ago)
      - Pens and markers (box): SHORT, 0 on hand of 1 required
      - Flashlight with batteries: STALE, last checked 2026-09-28 (over 14 days ago)
    Verdict: kit is NOT ready. Restock and recheck before this unit relies on it.

The sample inventory is deliberately imperfect. Fix the CSV (raise the counts, set fresh check dates), run it again, and the verdict flips to ready. That loop is the weekly kit check a unit actually performs.

## 3. QuickMAR support notes and the issue index

These are used at the med cart, not at a desk:

- Symptom first: find the row in projects/quickmar-support-notes/issue_index.csv (open it in any spreadsheet program and filter the Symptom column).
- Run the first checks in order. They are sequenced cheapest and most likely first.
- Respect the escalation line in the last column. Two rows deserve a second read: the count discrepancy row (support never edits records to balance a count) and the wrong-resident row (anything saved goes to nursing leadership and the chart correction process).

## 4. When the system actually goes down

The order of operations, using the documents in this repository:

1. Declare downtime and start the downtime log (projects/downtime-kit/downtime-log-template.md).
2. Issue the paper kit; the worked example (example_downtime_log.md) shows what a filled log looks like two hours in.
3. At recovery, work the reconciliation checklist in its stated order: admissions, orders, MAR, results, then the rest.
4. File the log with the incident record. Same number, joined trail.

## The thread through all of it

Every document here exists because of one support truth: during an incident, people do not rise to the occasion, they fall to the level of their checklists. The toolkit is the checklists, plus two small tools that make the boring parts automatic so attention can go to the patient-facing parts.
