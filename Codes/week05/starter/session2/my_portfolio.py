"""Lab 1: a Friday-evening portfolio report.
Tests: Shape: (5, 4),
Value: [108000, 192000, 225000, 75000, 84000],
Top holding: ROBO, Mean value: 136800.0.
"""
import pandas as pd

holdings = pd.DataFrame({
    "ticker": ["CODE", "TEA", "ROBO", "MLBK", "FIT"],
    "shares": [10, 40, 5, 30, 20],
    "buy": [10000, 5000, 40000, 2000, 3000],
    "close": [10800, 4800, 45000, 2500, 4200],
})
# TODO: print the shape, add a value column
# (shares * close), print the value list,
# the top holding's ticker and the mean value
# rounded to 1.
