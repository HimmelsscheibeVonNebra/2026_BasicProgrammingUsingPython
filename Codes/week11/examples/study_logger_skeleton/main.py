"""Entry point: python3 main.py

Week 10 skeleton: loads records and prints a placeholder summary.
"""
from report import format_totals
from storage import load_records

DATA = "data/study.csv"


def main():
    records = load_records(DATA)
    print(f"Loaded {len(records)} records")
    for line in format_totals({}):
        print(line)


if __name__ == "__main__":
    main()
