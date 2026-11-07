# Ticket Priority Tool

A small Python tool that scores an EHR support ticket and assigns a priority. It asks four questions and prints the priority, a response target, and the first steps to take.

## Why this exists

Priority arguments waste the first ten minutes of a real incident. A consistent scoring rule ends the argument: the same answers always produce the same priority, and the reasoning prints with the result so anyone can audit it.

## Run it

    python3 triage_priority.py

Answer the prompts. Example session:

    Category (access, workflow, data, interface, system): system
    Is patient care blocked right now? (y/n): y
    How many users are affected? (one, unit, facility): unit
    Is there a workaround? (y/n): n

    Priority: P1
    Response target: 15 minutes
    Score: 8 (category 3, care blocked +3, unit affected +1, no workaround +1)
    First steps: page the on-call analyst, open the incident record, notify the house supervisor, start the downtime log if the outage will pass 30 minutes.

## Scoring rules

- Category base: system 3, interface 2, data 2, workflow 1, access 1
- Patient care blocked: +3
- Scope: one user +0, a unit +1, the whole facility +2
- No workaround: +1

Totals: 7 or more is P1, 5 to 6 is P2, 3 to 4 is P3, below 3 is P4.

The rules live in one function at the top of the script so a support team can tune them to local policy.
