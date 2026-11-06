"""CSV input and atomic HTML output; all file I/O lives here."""
import csv
import os
from pathlib import Path
import tempfile
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


def write_html(path, html):
    """Replace output only after a complete UTF-8 write; raise OSError on failure."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8",
                                         dir=path.parent, delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(html)
        os.replace(temporary, path)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()
