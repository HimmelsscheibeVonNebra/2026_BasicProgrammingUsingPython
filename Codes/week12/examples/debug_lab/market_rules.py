"""Student starter: three intentional defects. Edit this file in the lab.

Contract: positive integer prices (bool excluded); no rounding in calculations.
Empty summary: count=0 and mean=None. rank_changes returns a new list,
sorted by change_pct descending, then six-digit code ascending.
"""


def change_pct(previous_close, close):
    if type(previous_close) is not int or type(close) is not int:
        raise ValueError("prices must be positive integers")
    if previous_close <= 0 or close <= 0:
        raise ValueError("prices must be positive integers")
    return (close - previous_close) / close * 100


def summarize(changes):
    return {"count": len(changes), "mean": sum(changes) / len(changes)}


def rank_changes(rows):
    return sorted(rows, key=lambda row: row["change_pct"])
