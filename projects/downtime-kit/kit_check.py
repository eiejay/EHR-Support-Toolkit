#!/usr/bin/env python3
"""Downtime kit checker.

Usage:
    python3 kit_check.py kit_inventory.csv

Reads a unit's downtime kit inventory (item, required, on_hand,
last_checked) and reports what is missing or stale. A kit that is
short during an outage is worse than no kit, because the plan assumed
it was there. The weekly check this automates is the difference.

An item is flagged when on_hand is below required, or when its
last_checked date is more than 14 days old.
"""

import csv
import sys
from datetime import date, datetime, timedelta

STALE_AFTER_DAYS = 14


def parse_date(value):
    try:
        return datetime.strptime(value.strip(), "%Y-%m-%d").date()
    except (ValueError, AttributeError):
        return None


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 kit_check.py <kit_inventory.csv>")
        return 2
    today = date.today()
    problems = []
    total = 0
    with open(sys.argv[1], newline="") as handle:
        for row in csv.DictReader(handle):
            total += 1
            item = row.get("item", "?").strip()
            try:
                required = int(row.get("required", "0"))
                on_hand = int(row.get("on_hand", "0"))
            except ValueError:
                problems.append(f"{item}: required or on_hand is not a number")
                continue
            if on_hand < required:
                problems.append(f"{item}: SHORT, {on_hand} on hand of {required} required")
            checked = parse_date(row.get("last_checked", ""))
            if checked is None:
                problems.append(f"{item}: last_checked missing or not a date")
            elif today - checked > timedelta(days=STALE_AFTER_DAYS):
                problems.append(f"{item}: STALE, last checked {checked.isoformat()} (over {STALE_AFTER_DAYS} days ago)")
    print(f"Items reviewed: {total}")
    if problems:
        print(f"Problems: {len(problems)}")
        for problem in problems:
            print(f"  - {problem}")
        print("Verdict: kit is NOT ready. Restock and recheck before this unit relies on it.")
        return 1
    print("Problems: none")
    print("Verdict: kit is ready.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
