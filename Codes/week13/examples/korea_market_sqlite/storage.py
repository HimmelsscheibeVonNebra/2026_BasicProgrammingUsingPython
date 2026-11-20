"""SQLite storage, CSV import and atomic HTML output; all I/O lives here."""
import csv
import os
from pathlib import Path
import sqlite3
import tempfile
from logic import FIELDS, parse_row

SCHEMA = Path(__file__).resolve().parent / "schema.sql"
INSERT = """
    INSERT INTO quotes
    VALUES (?, ?, ?, ?, ?, ?, ?)
"""


def connect(path):
    """Open the database (":memory:" in tests) with rows readable by name."""
    if str(path) != ":memory:":
        Path(path).parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(path)
    con.row_factory = sqlite3.Row
    return con


def init_db(con):
    """Create the quotes table if it is missing. Safe to call every run."""
    con.executescript(SCHEMA.read_text(encoding="utf-8"))


def replace_quotes(con, quotes):
    """Replace the whole snapshot in one transaction: all rows or none.

    quotes are typed dicts from parse_row(). A constraint failure raises
    sqlite3.IntegrityError and leaves the previous rows in place.
    """
    rows = [tuple(q[f] for f in FIELDS) for q in quotes]
    with con:
        con.execute("DELETE FROM quotes")
        con.executemany(INSERT, rows)


def load_quotes(con):
    """Return every stored quote as a dict, in code order. Empty table -> []."""
    query = "SELECT * FROM quotes ORDER BY code"
    return [dict(row) for row in con.execute(query)]


def read_csv(path):
    """Read UTF-8(-BOM) CSV; reject malformed header/rows with ValueError.

    Missing or unreadable files raise OSError. Header-only files return [].
    (This was load_quotes() in the week 11 MVP.)
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
