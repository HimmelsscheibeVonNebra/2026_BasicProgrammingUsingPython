"""Generate a static page from Korean stock classroom data stored in SQLite."""
import argparse
from contextlib import closing
from pathlib import Path
import sqlite3
from logic import MARKETS, analyze, summarize
from storage import (connect, init_db, load_quotes, read_csv,
                     replace_quotes, write_html)
from report import render_html

BASE = Path(__file__).resolve().parent


def main(argv=None):
    """Return 0 after successful generation, 1 on data/file errors; CLI errors use 2.

    --import-csv validates a CSV and replaces the stored snapshot first.
    A failed import changes neither the database nor the old HTML.
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, default=BASE / "data/market.db")
    parser.add_argument("--import-csv", type=Path, metavar="CSV")
    parser.add_argument("--output", type=Path, default=BASE / "docs/index.html")
    parser.add_argument("--market", choices=MARKETS, default="ALL")
    args = parser.parse_args(argv)
    try:
        with closing(connect(args.db)) as con:
            init_db(con)
            if args.import_csv:
                replace_quotes(con, read_csv(args.import_csv))
            quotes = load_quotes(con)
        rows = analyze(quotes, args.market)
        summary = summarize(rows)
        day = quotes[0]["date"] if quotes else "데이터 없음"
        html = render_html(rows, summary, args.market, day)
        write_html(args.output, html)
    except (OSError, ValueError, UnicodeError, sqlite3.Error) as error:
        print(f"Report not generated: {error}")
        return 1
    print(f"Generated {args.output} ({len(rows)} stocks)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
