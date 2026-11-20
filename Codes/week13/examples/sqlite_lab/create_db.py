"""Create market.db from schema.sql and load prices.csv. Safe to run again."""
import csv
import sqlite3
from pathlib import Path

BASE = Path(__file__).resolve().parent
INSERT = """
    INSERT INTO quotes
    VALUES (?, ?, ?, ?, ?, ?, ?)
"""


def main():
    schema = (BASE / "schema.sql").read_text(encoding="utf-8")
    with open(BASE / "prices.csv", encoding="utf-8", newline="") as f:
        rows = [tuple(r.values()) for r in csv.DictReader(f)]
    con = sqlite3.connect(BASE / "market.db")
    con.executescript(schema)
    con.execute("DELETE FROM quotes")
    con.executemany(INSERT, rows)
    con.commit()
    count = con.execute("SELECT COUNT(*) FROM quotes").fetchone()[0]
    con.close()
    print(f"market.db ready: {count} rows")


if __name__ == "__main__":
    main()
