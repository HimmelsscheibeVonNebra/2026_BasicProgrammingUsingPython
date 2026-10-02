"""Lab 1 solution: a Friday-evening portfolio report."""
import pandas as pd

holdings = pd.DataFrame({
    "ticker": ["CODE", "TEA", "ROBO", "MLBK", "FIT"],
    "shares": [10, 40, 5, 30, 20],
    "buy": [10000, 5000, 40000, 2000, 3000],
    "close": [10800, 4800, 45000, 2500, 4200],
})

print("Shape:", holdings.shape)
holdings["value"] = holdings["shares"] * holdings["close"]
print("Value:", holdings["value"].tolist())
best = holdings["value"].idxmax()
print("Top holding:", holdings.loc[best, "ticker"])
print("Mean value:", round(holdings["value"].mean(), 1))
