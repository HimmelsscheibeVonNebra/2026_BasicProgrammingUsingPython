"""Generate a static page from a single-date Korean stock classroom snapshot."""
import argparse
from pathlib import Path
from logic import MARKETS, analyze, summarize
from storage import load_quotes, write_html
from report import render_html

BASE = Path(__file__).resolve().parent


def main(argv=None):
    """Return 0 after successful generation, 1 on data/file errors; CLI errors use 2."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=BASE / "data/prices.csv")
    parser.add_argument("--output", type=Path, default=BASE / "docs/index.html")
    parser.add_argument("--market", choices=MARKETS, default="ALL")
    args = parser.parse_args(argv)
    try:
        quotes = load_quotes(args.input)
        rows = analyze(quotes, args.market)
        summary = summarize(rows)
        day = quotes[0]["date"] if quotes else "데이터 없음"
        html = render_html(rows, summary, args.market, day)
        write_html(args.output, html)
    except (OSError, ValueError, UnicodeError) as error:
        print(f"Report not generated: {error}")
        return 1
    print(f"Generated {args.output} ({len(rows)} stocks)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
