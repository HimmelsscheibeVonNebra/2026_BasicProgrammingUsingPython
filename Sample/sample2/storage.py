"""CSV input and atomic HTML output; all file I/O lives here."""
import csv
from pathlib import Path
from logic import FIELDS, parse_row


def load_quotes(path):
    """Read UTF-8(-BOM) CSV; reject malformed header/rows with ValueError.

    Missing or unreadable files raise OSError. Header-only files return [].
    """
    with open(path, encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != FIELDS:
            raise ValueError("CSV header must be " + ",".join(FIELDS))
        quotes = []
        for number, row in enumerate(reader, start=2):
            try:
                quotes.append(parse_row(row))
            except ValueError as error:
                raise ValueError(f"CSV row {number}: {error}") from error
    return quotes

