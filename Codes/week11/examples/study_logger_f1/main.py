"""Study logger, F1 slice: log one study session.

F2 (reload the file) and F3 (weekly totals) arrive in session 2.
"""
from logic import make_record
from storage import append_record

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


if __name__ == "__main__":
    main()
