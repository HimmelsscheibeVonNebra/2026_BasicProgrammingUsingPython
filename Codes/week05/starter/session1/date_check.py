"""Practice 2: weekday and countdown for a target date.
Tests: today -> Days remaining: 0; a past date -> a negative count.
"""
from datetime import date, datetime

text = input("Date (YYYY-MM-DD): ")
target = datetime.strptime(text, "%Y-%m-%d").date()
# TODO: print the weekday name, e.g. Friday.
# TODO: print "Days remaining:" and the day count from date.today().
