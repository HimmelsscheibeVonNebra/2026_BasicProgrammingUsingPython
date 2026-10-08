"""Lab 3 (take-home): chart the trade journal.
Tests: buy 6 / sell 4 / Traded: 340000 /
Saved journal.png. trades.csv sits beside this file.
"""
import pandas as pd
import matplotlib.pyplot as plt

log = pd.read_csv("trades.csv")
# TODO: count the actions with value_counts,
# chart the counts as a titled bar chart saved as
# journal.png, and print both counts, the total
# traded (shares * price) and the saved name.
