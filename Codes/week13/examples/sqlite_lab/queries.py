"""Week 13 Session 1 lab: answer five questions with SELECT.

Run create_db.py first, then: python3 queries.py
Q1 is done. Write Q2-Q5. Every value that comes from outside the
program goes through a ? placeholder, never into the SQL string.
"""
import sqlite3
from pathlib import Path

BASE = Path(__file__).resolve().parent


def show(title, rows):
    print(title)
    for row in rows:
        print("  ", tuple(row))


def main():
    con = sqlite3.connect(BASE / "market.db")

    # Q1 (example): name and close of every KOSPI stock, by code.
    q1 = """
        SELECT name, close FROM quotes
        WHERE market = ?
        ORDER BY code
    """
    show("Q1 KOSPI stocks", con.execute(q1, ("KOSPI",)))

    # Q2: name and volume of stocks with volume >= 300000,
    #     largest volume first.

    # Q3: the top 2 gainers: name and change_pct (percent).
    #     change_pct = (close - previous_close) * 100.0 / previous_close

    # Q4: how many stocks closed lower than the previous close?

    # Q5: ask for a stock code with input() and print that row,
    #     or "not found". Use a ? placeholder.

    con.close()


if __name__ == "__main__":
    main()
