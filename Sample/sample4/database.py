"""SQLite connections are short-lived; imports commit as one transaction."""
import sqlite3
from pathlib import Path
from logic import FIELDS, analyze, parse_row


def import_snapshot(path, quotes):
    # Validate before deleting any existing rows, including calls outside Flask CLI.
    quotes = [parse_row({key: str(row[key]) for key in FIELDS}) for row in quotes]
    analyze(quotes, 'ALL')
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(path)
    try:
        with connection:
            connection.execute('''CREATE TABLE IF NOT EXISTS quotes (
                date TEXT NOT NULL, code TEXT PRIMARY KEY, name TEXT NOT NULL,
                market TEXT NOT NULL CHECK(market IN ('KOSPI','KOSDAQ')),
                previous_close INTEGER NOT NULL CHECK(previous_close > 0),
                close INTEGER NOT NULL CHECK(close > 0),
                volume INTEGER NOT NULL CHECK(volume >= 0))''')
            connection.execute('DELETE FROM quotes')
            connection.executemany(
                'INSERT INTO quotes VALUES (?, ?, ?, ?, ?, ?, ?)',
                [tuple(row[key] for key in FIELDS) for row in quotes])
    finally:
        connection.close()


def read_quotes(path):
    # mode=rw prevents an accidental empty database on a missing path.
    connection = sqlite3.connect(Path(path).resolve().as_uri() + '?mode=rw', uri=True)
    connection.row_factory = sqlite3.Row
    try:
        rows = connection.execute('SELECT * FROM quotes ORDER BY code').fetchall()
        return [parse_row({key: str(row[key]) for key in FIELDS}) for row in rows]
    finally:
        connection.close()


def read_quotes(path):
    # Read-only connection prevents a request from creating an empty DB by accident.
    connection = sqlite3.connect(Path(path).resolve().as_uri() + '?mode=ro', uri=True)
    try:
        connection.row_factory = sqlite3.Row
        rows = connection.execute('SELECT * FROM quotes ORDER BY code').fetchall()
        return [parse_row({key: str(row[key]) for key in FIELDS}) for row in rows]
    finally:
        connection.close()
