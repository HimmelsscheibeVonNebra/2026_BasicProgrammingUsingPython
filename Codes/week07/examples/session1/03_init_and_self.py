"""Step 3: initialize instance attributes with __init__ and self."""


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance


minsu = BankAccount("Minsu", 10000)
jisu = BankAccount("Jisu", 5000)
print(minsu.owner, minsu.balance)
print(jisu.owner, jisu.balance)

minsu.balance = minsu.balance + 3000
print("After changing Minsu:", minsu.balance, jisu.balance)
