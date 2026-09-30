"""Practice 2 solution: weekday and countdown for a target date."""
from datetime import date, datetime

text = input("Date (YYYY-MM-DD): ")
target = datetime.strptime(text, "%Y-%m-%d").date()
print(target.strftime("%A"))
print("Days remaining:", (target - date.today()).days)
