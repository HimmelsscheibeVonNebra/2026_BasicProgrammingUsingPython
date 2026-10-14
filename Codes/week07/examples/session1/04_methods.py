"""Step 4: methods change the object and return a result.

Teaching version: assume positive amounts and sufficient funds.
Step 5 adds checks. Do not use this version for the final lab.
"""


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return True

    def withdraw(self, amount):
        self.balance = self.balance - amount
        return True


minsu = BankAccount("Minsu", 10000)
jisu = BankAccount("Jisu", 5000)
accepted = minsu.deposit(3000)
print("Deposit:", accepted, minsu.balance)
print("Withdraw:", minsu.withdraw(4000), minsu.balance)
print("Jisu:", jisu.balance)
