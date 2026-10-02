"""Lab 2 solution: a week's trade journal."""
import pandas as pd

log = pd.DataFrame({
    "action": ["buy", "buy", "sell", "buy", "sell",
               "buy", "buy", "sell", "sell", "buy"],
    "amount": [50000, 20000, 30000, 40000, 30000,
               20000, 50000, 30000, 30000, 40000],
})

counts = log["action"].value_counts()
print("Actions:", counts.index.tolist())
print("Counts:", counts.tolist())
print("Traded:", log["amount"].sum())
big = log[log["amount"] >= 40000]
print("Big trades:", big["action"].tolist())
