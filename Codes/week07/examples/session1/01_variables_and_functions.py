"""Step 1: manage account data with variables and a function.

Run: python3 7week/examples/session1/01_variables_and_functions.py
All amounts in this lesson are integers in won.
"""


def deposit(balance, amount):
    return balance + amount


minsu_owner = "Minsu"
minsu_balance = 10000
jisu_owner = "Jisu"
jisu_balance = 5000

# The caller chooses the balance and stores the returned value.
minsu_balance = deposit(minsu_balance, 3000)
print(minsu_owner, minsu_balance)
print(jisu_owner, jisu_balance)
