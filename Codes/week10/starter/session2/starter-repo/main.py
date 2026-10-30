"""Entry point: python3 main.py"""
from report import format_summary
from storage import load_records

DATA = "data/sample.csv"


def main():
    records = load_records(DATA)
    print(f"Loaded {len(records)} records")
    for line in format_summary({}):
        print(line)


if __name__ == "__main__":
    main()
