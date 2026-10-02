"""Lab 2: a week's trade journal.
Tests: Actions ['buy', 'sell'], Counts [6, 4],
Traded: 340000, and the four big buys.
"""
import pandas as pd

log = pd.DataFrame({
    "action": ["buy", "buy", "sell", "buy", "sell",
               "buy", "buy", "sell", "sell", "buy"],
    "amount": [50000, 20000, 30000, 40000, 30000,
               20000, 50000, 30000, 30000, 40000],
})
# TODO: count actions with value_counts, print
# action names and counts, the total traded,
# and the actions of trades >= 40000.
