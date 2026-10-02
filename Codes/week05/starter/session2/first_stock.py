"""Practice 1: one stock, one week of closes.
You bought CODE at 10,000 on Monday.
Tests: Mean: 10260.0, High: 10800,
Above buy (10000): 3, winning days
Tue 10200, Thu 10500 and Fri 10800.
"""
import pandas as pd

closes = pd.Series([10000, 10200, 9800, 10500,
                    10800],
                   index=["Mon", "Tue", "Wed",
                          "Thu", "Fri"])
# TODO: print the mean rounded to 1, the high,
# the count of closes above the 10000 buy, and
# each winning day with its close.
