"""Practice 2 solution: rank four positions by profit."""
import pandas as pd

positions = pd.DataFrame({
    "ticker": ["CODE", "TEA", "ROBO", "MLBK"],
    "shares": [10, 40, 5, 30],
    "buy": [10000, 5000, 40000, 2000],
    "close": [10800, 4800, 45000, 2500],
})

positions["profit"] = (positions["close"] - positions["buy"]) * positions["shares"]
ranked = positions.sort_values("profit", ascending=False)
print(ranked["ticker"].tolist())
print(ranked["profit"].tolist())
best = positions["profit"].idxmax()
print("Top:", positions.loc[best, "ticker"])
print("Winners:", (positions["profit"] > 0).sum())
