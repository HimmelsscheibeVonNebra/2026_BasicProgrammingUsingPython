"""Step 5: keep balance rules in the account's methods.

Assumptions: starting balance is a nonnegative integer. Transaction
amounts are integers. A leading underscore is a convention, not a lock.
"""


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            return False
        self._balance = self._balance + amount
        return True

    def withdraw(self, amount):
        if amount <= 0 or amount > self._balance:
            return False
        self._balance = self._balance - amount
        return True


minsu = BankAccount("Minsu", 10000)
jisu = BankAccount("Jisu", 5000)
print("Start:", minsu.get_balance(), jisu.get_balance())
print("Deposit 3000:", minsu.deposit(3000), minsu.get_balance())
print("Withdraw 4000:", minsu.withdraw(4000), minsu.get_balance())
print("Withdraw 10000:", minsu.withdraw(10000), minsu.get_balance())
print("Deposit -1000:", minsu.deposit(-1000), minsu.get_balance())
print("Withdraw 0:", minsu.withdraw(0), minsu.get_balance())
print("Jisu withdraw 5000:", jisu.withdraw(5000), jisu.get_balance())
print("Final:", minsu.get_balance(), jisu.get_balance())
