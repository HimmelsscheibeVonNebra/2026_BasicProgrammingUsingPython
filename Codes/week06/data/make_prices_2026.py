"""Generate prices_2026.csv - one trading year of the five story stocks.

Deterministic: random.seed(2026) makes every run produce the same
bytes, so the committed CSV can always be regenerated and checked.

Story anchor: the week of 2026-03-02..03-06 is pinned to the exact
closes used across the Week 5 materials (portfolio buys match the
Monday closes; Friday closes match portfolio.csv), so exercises can
cross-check files against each other.

Run from this data folder:  python3 make_prices_2026.py
"""
import random
from datetime import date, timedelta

random.seed(2026)

# ticker: Mon..Fri closes of the story week (2026-03-02..03-06)
ANCHORS = {
    "CODE": [10000, 10200, 9800, 10500, 10800],
    "TEA": [5000, 4950, 4900, 4850, 4800],
    "ROBO": [40000, 39800, 41200, 43500, 45000],
    "MLBK": [2000, 2100, 1900, 2300, 2500],
    "FIT": [3000, 2900, 3100, 3700, 4200],
}
YEAR_START = date(2026, 1, 2)
YEAR_END = date(2026, 12, 31)
WEEK_START = date(2026, 3, 2)
MAX_MOVE = 0.02  # daily change is uniform in -2%..+2%


def walk(first, days, last=None):
    """Return `days` closes as a random walk starting after `first`.

    With `last`, the walk is linearly drifted so its final close lands
    exactly on `last`; the anchor week then joins without a jump.
    """
    prices = [first]
    for _ in range(days):
        prices.append(prices[-1] * (1 + random.uniform(-MAX_MOVE, MAX_MOVE)))
    if last is not None and days:
        drift = (last - prices[-1]) / days
        prices = [p + drift * i for i, p in enumerate(prices)]
    return [max(100, round(p)) for p in prices[1:]]


def trading_days():
    days, day = [], YEAR_START
    while day <= YEAR_END:
        if day.weekday() < 5:
            days.append(day)
        day += timedelta(days=1)
    return days


days = trading_days()
pre = [d for d in days if d < WEEK_START]
post = [d for d in days if d > WEEK_START + timedelta(days=4)]

columns = {}
for ticker, closes in ANCHORS.items():
    week = dict(zip((WEEK_START + timedelta(days=i) for i in range(5)), closes))
    columns[ticker] = {**dict(zip(pre, walk(closes[0], len(pre), closes[0]))),
                       **week,
                       **dict(zip(post, walk(closes[-1], len(post))))}

with open("prices_2026.csv", "w") as f:
    f.write("date," + ",".join(ANCHORS) + "\n")
    for day in days:
        f.write(day.isoformat() + ","
                + ",".join(str(columns[t][day]) for t in ANCHORS) + "\n")

print(f"prices_2026.csv: {len(days)} trading days, {len(ANCHORS)} tickers")
