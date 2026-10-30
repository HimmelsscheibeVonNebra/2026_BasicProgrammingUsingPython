"""Practice 2: split one big function into functions with contracts.

The function all_in_one() below works, but it reads input, checks it,
adds it up and prints it in one block. You cannot test the adding-up
without typing at the keyboard.

Your task (10 minutes):
  1. Complete parse_amount, category_totals and format_report.
     Each docstring is the contract. Follow it exactly.
  2. Run this file. Every check should print PASS.

Do not use input() or print() inside the three functions.
"""


def all_in_one():
    """The original version. Read it; do not change it."""
    totals = {}
    while True:
        line = input("category,amount (blank to stop): ")
        if line == "":
            break
        category, amount = line.split(",")
        amount = int(amount)
        if amount <= 0:
            print("Skipped: amount must be positive")
            continue
        category = category.strip().lower()
        totals[category] = totals.get(category, 0) + amount
    for category in sorted(totals):
        print(f"{category}: {totals[category]} won")


def parse_amount(text):
    """Return text as a positive int amount in won.

    Raises ValueError if text is not a whole number or is not above 0.
    """
    # TODO 1: convert with int(), then reject 0 and negative numbers.
    return 0


def category_totals(expenses):
    """Return {category: total amount} for a list of (category, amount) pairs.

    Categories are compared in lower case without surrounding spaces.
    An empty list returns {}.
    """
    # TODO 2: build and return a dictionary of totals.
    return {}


def format_report(totals):
    """Return a list of lines "category: total won", sorted by category name."""
    # TODO 3: return one string per category.
    return []


def check(name, actual, expected):
    if actual == expected:
        print("PASS", name)
    else:
        print("FAIL", name, "-> got", repr(actual), "expected", repr(expected))


def rejects(text):
    try:
        parse_amount(text)
    except ValueError:
        return True
    return False


if __name__ == "__main__":
    check("parse_amount('4500')", parse_amount("4500"), 4500)
    check("parse_amount rejects '-200'", rejects("-200"), True)
    check("parse_amount rejects 'ten'", rejects("ten"), True)
    sample = [("Food", 4500), ("bus", 1500), (" food ", 8000)]
    check("category_totals(sample)", category_totals(sample), {"food": 12500, "bus": 1500})
    check("category_totals([])", category_totals([]), {})
    check("format_report", format_report({"food": 12500, "bus": 1500}),
          ["bus: 1500 won", "food: 12500 won"])
