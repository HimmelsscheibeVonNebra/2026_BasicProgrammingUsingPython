"""Practice 1 solution: one stock, one week of closes."""
import pandas as pd

closes = pd.Series([10000, 10200, 9800, 10500, 10800],
                   index=["Mon", "Tue", "Wed", "Thu", "Fri"])

print("Mean:", round(closes.mean(), 1))
print("High:", closes.max())
print("Above buy (10000):", (closes > 10000).sum())
wins = closes[closes > 10000]
for day, close in wins.items():
    print(day, int(close))
