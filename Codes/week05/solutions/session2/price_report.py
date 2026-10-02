"""Lab 3 solution: FIT's week in review."""
import pandas as pd

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
values = []
for day in days:
    values.append(int(input("Close " + day + ": ")))

closes = pd.Series(values, index=days)
print("Mean:", round(closes.mean(), 1))
print("High:", closes.max())
best = closes.idxmax()
print("Best day:", best, closes[best])
print("Above mean:", (closes > closes.mean()).sum())
