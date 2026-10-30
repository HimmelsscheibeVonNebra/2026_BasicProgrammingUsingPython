"""Study logger: log one study session, then show the weekly totals."""
from logic import make_record, weekly_totals
from report import format_totals
from storage import append_record, load_records

DATA = "data/study.csv"


def main():
    date = input("Date (YYYY-MM-DD): ")
    course = input("Course: ")
    minutes = input("Minutes: ")
    try:
        record = make_record(date, course, minutes)
    except ValueError as error:
        print("Not saved:", error)
    else:
        append_record(DATA, record)
        print("Saved.")
    totals = weekly_totals(load_records(DATA))
    for line in format_totals(totals):
        print(line)


if __name__ == "__main__":
    main()
