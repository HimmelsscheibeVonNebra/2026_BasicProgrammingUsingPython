"""Step 7: use an account through its public operations.

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


# The caller uses the interface without managing _balance directly.
account = BankAccount("Minsu", 10000)
accepted = account.withdraw(4000)
print("Accepted:", accepted)
print("Balance:", account.get_balance())
