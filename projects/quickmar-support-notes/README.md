# QuickMAR and PointClickCare Support Notes

Floor-level support notes for medication administration workflows in long-term care, written from the support side of the med cart: what breaks during med pass, what it usually is, and how to get the nurse moving again without cutting corners on safety.

## Files

- issue_index.csv: this page as a table: symptom, first checks, likely causes, and the escalation line for each. Built to be searched, filtered, or loaded into a knowledge base.

## The med pass rule

Every fix during med pass is judged by one standard: the right resident, the right medication, the right dose, the right route, the right time, with the scan and the documentation to prove it. A workaround that skips verification is never the fix.

## First minute flowchart

When a nurse waves support over during a pass, the first minute runs the same way:

1. What exactly is blocked: scanning, finding the medication, signing off, or the count?
2. Is it this resident, this medication, this cart, or every cart? The scope names the layer.
3. Run the matching row in the issue index.
4. If the fix is not obvious in five minutes, escalate with the facts gathered, not with a shrug.

## Common issues and first responses

### Barcode will not scan

1. Check the wristband or med label for damage, glare, or a faded print. Reprint the label before blaming the scanner.
2. Clean the scanner window and check the battery. A dying scanner misses readably good barcodes.
3. Confirm the scanner is paired to the right workstation or cart. Cross-paired scanners scan perfectly, into the wrong session.
4. Test with a known good barcode. Scanner fine plus one bad label means a print problem, not a scanner problem.

### Medication does not appear on the eMAR

1. Confirm the order is active and verified, not sitting in a pending or unverified state.
2. Check the scheduled times on the order against the med pass window. An order timed outside the window will not present.
3. Confirm the resident's current location and status. A resident on leave or transferred will not show the pass where staff expect it.
4. Check for a held or discontinued duplicate. Duplicate therapy holds hide the live order more often than any system fault.

### Med cart or workstation is slow or frozen

1. Note exactly where it froze: before the scan, at the resident list, or at sign-off. The step names the likely layer.
2. Check the wireless signal where the cart physically is. Dead corners in older buildings are the most common cause of phantom system slowness.
3. Sign out and back in on a second workstation to separate a device problem from an account or system problem.
4. If every cart slows at the same minute, stop troubleshooting devices: it is the system or the network, and it is one ticket, not ten.

### The count is off at shift change

Controlled substance counts are a two-nurse process and are never a support shortcut. Support's role: confirm both nurses are documenting in the same record, check for a dose documented under the wrong resident or the wrong pass, and surface the audit trail. The count itself is resolved by nursing, not by editing records.

## Chart audit checks support can run

- Administrations documented well after the pass window, grouped by user or unit: a training or staffing signal, not automatically an error.
- PRN medications with no effectiveness note.
- Held doses with no hold reason.
- Orders verified long after entry, grouped by time of day.

Each pattern becomes a conversation with the unit, with the report attached. Audits support the floor; they are not a gotcha.

## Escalation line

Support fixes access, workflow, and system problems. Clinical judgment questions, order clarifications, and count discrepancies go to nursing leadership and pharmacy. Knowing which side of that line a problem sits on is most of the job.
