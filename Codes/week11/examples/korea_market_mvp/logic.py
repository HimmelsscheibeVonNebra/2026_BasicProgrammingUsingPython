"""Pure rules for a single-date classroom snapshot; prices are integer KRW."""
from datetime import date

FIELDS = ["date", "code", "name", "market", "previous_close", "close", "volume"]
MARKETS = ("ALL", "KOSPI", "KOSDAQ")


def parse_row(row):
    """Return a typed quote; raise ValueError for any invalid field. No I/O."""
    if set(row) != set(FIELDS) or any(not isinstance(v, str) for v in row.values()):
        raise ValueError("each row needs exactly seven fields")
    quote = {key: value.strip() for key, value in row.items()}
    day = quote["date"]
    if date.fromisoformat(day).isoformat() != day:
        raise ValueError("date must be YYYY-MM-DD")
    code = quote["code"]
    if len(code) != 6 or not code.isascii() or not code.isdigit():
        raise ValueError("code must be six ASCII digits")
    if not quote["name"] or quote["market"] not in MARKETS[1:]:
        raise ValueError("name and KOSPI/KOSDAQ market are required")
    for field in ("previous_close", "close", "volume"):
        text = quote[field]
        if not text.isascii() or not text.isdigit():
            raise ValueError(f"{field} must be a whole number")
        quote[field] = int(text)
        minimum = 0 if field == "volume" else 1
        if quote[field] < minimum:
            raise ValueError(f"{field} must be >= {minimum}")
    return quote


def change_pct(previous_close, close):
    """Return unrounded daily percent change; both prices must be positive."""
    if previous_close <= 0 or close <= 0:
        raise ValueError("prices must be positive")
    return (close - previous_close) / previous_close * 100


def analyze(quotes, market):
    """Validate snapshot identity; filter and sort by change desc, then code asc.

    Return fresh quote dicts with change_pct. Empty input/selection returns [].
    Mixed dates, duplicate codes or an unknown market raise ValueError.
    quotes must already contain typed, validated values from parse_row().
    """
    if market not in MARKETS:
        raise ValueError("market must be ALL, KOSPI or KOSDAQ")
    if len({q["date"] for q in quotes}) > 1:
        raise ValueError("snapshot must contain one date")
    codes = [q["code"] for q in quotes]
    if len(set(codes)) != len(codes):
        raise ValueError("duplicate code in snapshot")
    rows = [dict(q, change_pct=change_pct(q["previous_close"], q["close"]))
            for q in quotes if market == "ALL" or q["market"] == market]
    return sorted(rows, key=lambda q: (-q["change_pct"], q["code"]))


def summarize(rows):
    """Return sample count, up/down/flat counts and equal-weight mean (or None)."""
    count = len(rows)
    return {"count": count,
            "up": sum(q["change_pct"] > 0 for q in rows),
            "down": sum(q["change_pct"] < 0 for q in rows),
            "flat": sum(q["change_pct"] == 0 for q in rows),
            "mean": sum(q["change_pct"] for q in rows) / count if count else None}
