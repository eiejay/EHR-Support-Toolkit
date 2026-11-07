# Downtime Log, Worked Example

A completed example of the downtime log template, from a fictional two-hour outage during an evening med pass. Names and times are invented; the shape of the record is the point.

Incident number: INC-2041  Date: 2026-11-06
System down confirmed at: 18:07  Confirmed by: EHR support, after three units reported the same freeze
Units affected: All (facility wide)
Vendor or IT case number: VND-88123

## Running log

| Time | Event or action | By |
| --- | --- | --- |
| 18:07 | Downtime declared, units notified by phone tree | Support |
| 18:12 | Paper packets issued to all four units | Support and supervisors |
| 18:15 | Evening med pass proceeds on paper MAR | Unit nurses |
| 18:40 | Status update to house supervisor: vendor engaged, no ETA | Support |
| 19:05 | Vendor update: database failover in progress, ETA 30 minutes | Vendor |
| 19:38 | System reported restored by vendor | Vendor |
| 19:44 | Support verifies logins, eMAR loads, interface queue draining | Support |
| 19:50 | Units told to resume electronic charting; back entry begins | Support |
| 21:15 | Back entry complete on all units; reconciliation started | Unit nurses |

## Paper documentation issued

| Unit | MAR sheets | Order sheets | Admission packets | Returned complete? |
| --- | --- | --- | --- | --- |
| A | 22 | 3 | 0 | Yes |
| B | 19 | 1 | 1 | Yes |
| C | 24 | 2 | 0 | Yes |
| D | 17 | 0 | 0 | Yes |

## Critical events during downtime

- 18:52: critical potassium result for a Unit C resident phoned by the lab and read back by the charge nurse; entered first at recovery and verified by the nurse who took the call.
- No admissions arrived during the window beyond the single Unit B packet above.

## Closure

System stable at: 19:44  Declared by: EHR support
Reconciliation checklist completed and signed: yes
Log filed with incident record: yes

## What this example shows

- The log is boring on purpose. Times, actions, names. In the review meeting, boring is what trustworthy looks like.
- The critical result is called out by name in the log, which is why it was reconciled first.
- Closure is a verification, not a hope: system stable, back entry done, reconciliation signed, then the incident closes.
