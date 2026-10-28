"""Week 9 OOP supplement. Run with Python 3.10+; no packages required."""


class BankAccount:
    def __init__(self, owner, balance=0):
        if not isinstance(owner, str) or not owner.strip():
            raise ValueError("owner must be nonblank text")
        if type(balance) is not int or balance < 0:
            raise ValueError("balance must be a nonnegative integer")
        self.owner = owner.strip()
        self._balance = balance

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if type(amount) is not int or amount <= 0:
            return False
        self._balance += amount
        return True

    def withdraw(self, amount):
        if type(amount) is not int or amount <= 0 or amount > self._balance:
            return False
        self._balance -= amount
        return True

    def account_type(self):
        return "Standard"


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, bonus=100):
        super().__init__(owner, balance)
        if type(bonus) is not int or bonus <= 0:
            raise ValueError("bonus must be a positive integer")
        self.bonus = bonus

    def add_bonus(self):
        return self.deposit(self.bonus)

    def account_type(self):
        return "Savings"


class AccountBook:
    """Holds references to account objects; never copies their balances."""
    def __init__(self):
        self._accounts = []

    def add_account(self, account):
        # Contract: account supports get_balance() and account_type().
        # In this lesson it is a BankAccount or SavingsAccount.
        if account in self._accounts:
            return False
        self._accounts.append(account)
        return True

    def total_balance(self):
        total = 0
        for account in self._accounts:
            total += account.get_balance()
        return total

    def report(self):
        rows = []
        for account in self._accounts:
            rows.append((account.owner, account.account_type(), account.get_balance()))
        return rows
