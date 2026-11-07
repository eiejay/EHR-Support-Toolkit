# EHR Support Toolkit

I spent my clinical years on PointClickCare and Epic, and my support instincts were built at the bedside, not in a classroom: when a system misbehaves at 2 AM, the nurse does not care whose queue it belongs to, she cares that the med pass is waiting. This repo is the toolkit I wish every EHR support analyst carried: a triage guide, downtime procedures that assume the worst hour, a go live checklist, and four small tools, including a machine learning model I trained to route tickets.

## The tools

- projects/ai-ticket-triage: a Naive Bayes classifier that reads a ticket's words and suggests its category (access, workflow, data, system). It earns an honest 62 percent on tickets it never saw, trained on 32 sample tickets, and the README explains exactly where it stumbles and why a person still files every ticket.
- projects/ticket-priority-tool: a scoring CLI that turns impact and urgency answers into a defensible P1 to P4, the same call two analysts should make the same way at 2 AM and 2 PM.
- projects/downtime-kit: the downtime log template, a fully worked example of a two hour outage, and a kit checker that verifies the paper fallback supplies are actually in the drawer before the night they are needed.
- projects/quickmar-support-notes: a symptom index for the QuickMAR medication administration side of PointClickCare: what the nurse sees, the first checks, the usual causes, and when to escalate.

## The documents

- ticket-triage-guide.md: how I sort access, workflow, data, and system problems, and the questions that separate a training issue from a defect.
- downtime-procedures.md: what happens on the unit when the system goes down, and the reconciliation that has to happen when it comes back.
- go-live-checklist.md: the list I would tape to the wall for cutover week.

## How I use this repo

WALKTHROUGH.md runs the tools against their sample data with real output. Nothing here contains patient or facility data; every example is fictional and labeled as such. If I cannot run it in front of you, I do not list it as a skill.

## License

MIT.
