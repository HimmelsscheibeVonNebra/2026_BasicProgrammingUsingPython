"""Practice 2: rank four positions by profit.
Tests: ['ROBO', 'MLBK', 'CODE', 'TEA'],
[25000, 15000, 8000, -8000], Top: ROBO,
Winners: 3.
"""
import pandas as pd

positions = pd.DataFrame({
    "ticker": ["CODE", "TEA", "ROBO", "MLBK"],
    "shares": [10, 40, 5, 30],
    "buy": [10000, 5000, 40000, 2000],
    "close": [10800, 4800, 45000, 2500],
})
# TODO: add profit = (close - buy) * shares,
# print tickers and profits sorted top first,
# the top ticker's name and the winner count.
