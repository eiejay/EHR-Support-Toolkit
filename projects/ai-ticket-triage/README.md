# Ticket Triage Assistant: Teaching a Model to Route Tickets

The first minutes of a support ticket are wasted on the dumbest step: reading it just to decide whose queue it belongs in. I built this to see how far a small model gets at that step. It reads the words in a ticket and suggests one of the four categories this toolkit already uses (access, workflow, data, system). It suggests. A person still files the ticket, because a model that is wrong confidently is worse than no model.

## Run it

    python3 ticket_classifier.py sample_tickets.csv
    python3 ticket_classifier.py sample_tickets.csv "your ticket text here"

## What I got

    Training tickets: 24  Held out: 8
    Held-out accuracy: 5/8 = 62%

    Ticket: The system is down for the whole unit and nobody can see orders
    Suggested category: SYSTEM (confidence 100%)

    Ticket: I forgot my password and the reset email never arrives so I cannot log in
    Suggested category: ACCESS (confidence 100%)

    Ticket: The wristband scan freezes the med pass screen every time
    Suggested category: WORKFLOW (confidence 100%)

## What surprised me

The model is Naive Bayes, the same math as the phishing classifier in my SOC repo, pointed at a different problem. It works because categories have accents: access tickets talk about passwords and logins, system tickets talk about everybody and down. Where it stumbles is where I stumble reading fast: a ticket about a login that fails only inside one workflow wears both accents, and with 32 training tickets the model has barely seen the difference. 62 percent on tickets it never saw is honest for this much data. Feed it a real ticket history, thousands of rows, and this is the part of the help desk that quietly gets faster.

## Where this fits in a real shop

- Auto suggest the category and let the analyst confirm or correct, and log the corrections: that log is tomorrow's training data.
- Route the obvious ones instantly (the full outage, the password reset) and spend human reading time on the ambiguous middle.
- Pair it with the priority tool in this repo: the classifier says what it is, the scorer says how bad it is. Neither files anything alone.

## The honest limit

A category is not a diagnosis. The model has never seen a chart, a unit, or a patient, and it shows in the misses. I would let it sort the mail. I would not let it close a ticket.
