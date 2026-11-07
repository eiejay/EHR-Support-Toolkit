#!/usr/bin/env python3
"""Ticket category suggester: Naive Bayes over the words in a ticket.

Usage:
    python3 ticket_classifier.py sample_tickets.csv
    python3 ticket_classifier.py sample_tickets.csv "nurse locked out of her account"

First line support burns minutes reading a ticket just to route it.
This model reads the text and suggests one of the toolkit categories
(access, workflow, data, system), so the human starts from a good
guess instead of a blank field. It suggests; it never files.
"""

import csv
import math
import re
import sys
from collections import Counter, defaultdict

TOKEN = re.compile(r"[a-z0-9']+")
CATEGORIES = ["access", "workflow", "data", "system"]


def tokenize(text):
    return TOKEN.findall(text.lower())


class TicketBayes:
    def __init__(self):
        self.class_counts = Counter()
        self.word_counts = defaultdict(Counter)
        self.vocab = set()

    def train(self, rows):
        for label, text in rows:
            self.class_counts[label] += 1
            for word in tokenize(text):
                self.word_counts[label][word] += 1
                self.vocab.add(word)

    def predict(self, text):
        words = tokenize(text)
        total_docs = sum(self.class_counts.values())
        scores = {}
        for label in self.class_counts:
            total_words = sum(self.word_counts[label].values())
            score = math.log(self.class_counts[label] / total_docs)
            for word in words:
                score += math.log((self.word_counts[label][word] + 1) / (total_words + len(self.vocab)))
            scores[label] = score
        ranked = sorted(scores.items(), key=lambda item: item[1], reverse=True)
        top, second = ranked[0], ranked[1]
        confidence = 1 / (1 + math.exp(-(top[1] - second[1])))
        return top[0], confidence, ranked


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 ticket_classifier.py <sample_tickets.csv> [ticket text]")
        return 2
    with open(sys.argv[1], newline="") as handle:
        rows = [(r["category"], r["text"]) for r in csv.DictReader(handle)]
    holdout = rows[::4]
    train = [row for i, row in enumerate(rows) if i % 4 != 0]
    probe = TicketBayes()
    probe.train(train)
    correct = sum(1 for label, text in holdout if probe.predict(text)[0] == label)
    print(f"Training tickets: {len(train)}  Held out: {len(holdout)}")
    print(f"Held-out accuracy: {correct}/{len(holdout)} = {correct / len(holdout):.0%}")
    model = TicketBayes()
    model.train(rows)
    demos = [
        "The system is down for the whole unit and nobody can see orders",
        "I forgot my password and the reset email never arrives so I cannot log in",
    ]
    targets = [sys.argv[2]] if len(sys.argv) > 2 else demos
    for text in targets:
        label, confidence, _ = model.predict(text)
        print(f"\nTicket: {text}")
        print(f"Suggested category: {label.upper()} (confidence {confidence:.0%})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
