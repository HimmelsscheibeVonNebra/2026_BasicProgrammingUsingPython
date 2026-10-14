"""Step 2: one class, two objects, separate attributes.

pass is a placeholder that does nothing. Initialization comes next.
"""


class BankAccount:
    pass


minsu = BankAccount()
minsu.owner = "Minsu"
minsu.balance = 10000

jisu = BankAccount()
jisu.owner = "Jisu"
jisu.balance = 5000

minsu.balance = minsu.balance + 3000
print(minsu.owner, minsu.balance)
print(jisu.owner, jisu.balance)
print(minsu is jisu)  # Two constructor calls created two different objects.
