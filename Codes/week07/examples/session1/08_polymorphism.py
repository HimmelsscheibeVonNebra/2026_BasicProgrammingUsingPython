"""Step 8: one method call, different implementations.

Assumptions: starting balance is a nonnegative integer. Transaction
amounts are integers; bonuses are positive integers.
A leading underscore is a convention, not a lock.
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

    def account_type(self):
        return "Standard"


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, bonus):
        super().__init__(owner, balance)
        self.bonus = bonus

    def add_bonus(self):
        return self.deposit(self.bonus)

    def account_type(self):
        return "Savings"


accounts = [BankAccount("Minsu", 10000),
            SavingsAccount("Jisu", 5000, 500)]
for account in accounts:
    print(account.owner, account.account_type(),
          account.get_balance())
