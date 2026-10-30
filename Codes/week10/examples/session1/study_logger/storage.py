"""Reading and writing study.csv. The only file that touches the disk."""
import csv
from pathlib import Path

FIELDS = ["date", "course", "minutes"]


def load_records(path):
    """Return every row of the CSV file as a record dict.

    minutes is converted to int. A missing file returns [].
    """
    path = Path(path)
    if not path.exists():
        return []
    with open(path, newline="", encoding="utf-8") as f:
        return [{"date": row["date"], "course": row["course"],
                 "minutes": int(row["minutes"])}
                for row in csv.DictReader(f)]


def append_record(path, record):
    """Append one record to the CSV file, writing the header if the file is new."""
    path = Path(path)
    is_new = not path.exists()
    with open(path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        if is_new:
            writer.writeheader()
        writer.writerow(record)
