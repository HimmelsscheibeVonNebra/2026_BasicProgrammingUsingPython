"""Reading and writing data/study.csv. The only module that touches the disk."""
import csv
from pathlib import Path

FIELDS = ["date", "course", "minutes"]


def load_records(path):
    """Return every row of the CSV file as a record dict.

    minutes is converted to int. A missing file returns [].
    """
    # TODO (next session, F2): implement with csv.DictReader.
    return []


def append_record(path, record):
    """Append one record to the CSV file, writing the header if the file is new."""
    path = Path(path)
    is_new = not path.exists()
    with open(path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        if is_new:
            writer.writeheader()
        writer.writerow(record)
