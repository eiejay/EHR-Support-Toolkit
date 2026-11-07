# Downtime Kit

The paper packet a nursing unit runs on when the EHR is unavailable, plus the reconciliation that closes the loop when the system returns, plus the checker that keeps the kit honest.

## Why this exists

Downtime is where EHR support earns its keep. Care does not pause for an outage, so the paper process has to be ready before it is needed: printed, stocked, and understood by the night shift, not designed during the incident.

## Contents

- [Downtime Log Template](downtime-log-template.md): the running record of the outage and everything done on paper during it.
- [Worked Example Log](example_downtime_log.md): the template completed for a fictional two-hour outage during an evening med pass.
- [Recovery Reconciliation Checklist](recovery-reconciliation-checklist.md): the ordered back-entry and verification process that proves nothing documented on paper was lost.
- kit_check.py and kit_inventory.csv: a small checker that reads a unit's kit inventory and flags items that are short or stale (not checked within 14 days). Run it:

      python3 kit_check.py kit_inventory.csv

  The sample inventory deliberately contains a short item, an empty item, and two stale checks, so the checker reports four problems and a NOT ready verdict. A ready kit is the only acceptable result.

## Kit rules

1. The kit lives in one known place per unit, checked weekly like the crash cart.
2. Every paper page carries the patient identifiers required by local policy, the date, and the page number of the total for that patient.
3. Nothing on paper is discarded after recovery until reconciliation is signed off.
4. The downtime log and the incident record share the same incident number, so the paper trail and the ticket trail stay joined.
