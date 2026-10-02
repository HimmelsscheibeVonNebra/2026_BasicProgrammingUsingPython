"""Lab 3 (take-home): FIT's week in review.
Tests: 4200, 4350, 4100, 4400, 4300 ->
Mean: 4270.0, High: 4400, Best day: Thu 4400,
Above mean: 3. Assume integer-formatted input.
"""
import pandas as pd

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
values = []
for day in days:
    values.append(int(input("Close " + day + ": ")))
# TODO: build a Series with days as the index,
# then print the mean rounded to 1, the high,
# the best day with its close, and the count of
# days above the mean.
