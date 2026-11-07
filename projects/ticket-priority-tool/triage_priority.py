#!/usr/bin/env python3
"""Score an EHR support ticket and assign a priority.

Asks four questions (category, whether patient care is blocked, scope,
and whether a workaround exists) and prints a priority from P1 to P4
with a response target and first steps. Scoring rules are deliberately
simple and visible so any support team can audit or tune them.
"""

CATEGORY_SCORES = {
    "system": 3,
    "interface": 2,
    "data": 2,
    "workflow": 1,
    "access": 1,
}

SCOPE_SCORES = {"one": 0, "unit": 1, "facility": 2}

RESPONSE_TARGETS = {
    "P1": "15 minutes",
    "P2": "1 hour",
    "P3": "4 hours",
    "P4": "next business day",
}

FIRST_STEPS = {
    "P1": "page the on-call analyst, open the incident record, notify the house supervisor, start the downtime log if the outage will pass 30 minutes.",
    "P2": "assign to the EHR support queue, confirm the workaround with the unit, update the ticket every hour until resolved.",
    "P3": "work in queue order, confirm the fix with the reporting user before closing.",
    "P4": "schedule as a request: new account, new report, or build change. Confirm requirements before starting.",
}


def ask(prompt, valid):
    while True:
        answer = input(prompt).strip().lower()
        if answer in valid:
            return answer
        print(f"Please answer one of: {', '.join(sorted(valid))}")


def score_ticket():
    category = ask(
        "Category (access, workflow, data, interface, system): ", CATEGORY_SCORES
    )
    care_blocked = ask("Is patient care blocked right now? (y/n): ", {"y", "n"}) == "y"
    scope = ask("How many users are affected? (one, unit, facility): ", SCOPE_SCORES)
    workaround = ask("Is there a workaround? (y/n): ", {"y", "n"}) == "y"

    score = CATEGORY_SCORES[category]
    parts = [f"category {score}"]
    if care_blocked:
        score += 3
        parts.append("care blocked +3")
    if SCOPE_SCORES[scope]:
        score += SCOPE_SCORES[scope]
        parts.append(f"{scope} affected +{SCOPE_SCORES[scope]}")
    if not workaround:
        score += 1
        parts.append("no workaround +1")

    if score >= 7:
        priority = "P1"
    elif score >= 5:
        priority = "P2"
    elif score >= 3:
        priority = "P3"
    else:
        priority = "P4"
    return priority, score, ", ".join(parts)


def main():
    priority, score, breakdown = score_ticket()
    print()
    print(f"Priority: {priority}")
    print(f"Response target: {RESPONSE_TARGETS[priority]}")
    print(f"Score: {score} ({breakdown})")
    print(f"First steps: {FIRST_STEPS[priority]}")


if __name__ == "__main__":
    main()
