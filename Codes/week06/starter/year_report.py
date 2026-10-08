"""Lab 2: the trading year in two charts.
Tests: Days: 260 / Best close: 12795 /
Best date: 2026-08-06 / two saved files.
prices_2026.csv sits beside this file.
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("prices_2026.csv")
code = df["CODE"]
# TODO: chart 1 - code's year as a titled line,
# saved as code_year.png. Then figure(), chart 2
# - a histogram of code's daily changes
# (diff().dropna()), saved as changes.png.
# Print the day count, the best close, its date
# and both saved file names.
