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
        # TODO: reject nonintegers, nonpositive values, and overdrafts.
        # A rejected withdrawal must leave the balance unchanged.
        raise NotImplementedError("Complete withdraw")

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
        # TODO: sum get_balance() across the stored account objects.
        raise NotImplementedError("Complete total_balance")

    def report(self):
        # TODO: return (owner, account_type(), get_balance()) tuples.
        raise NotImplementedError("Complete report")


def main():
    minsu = BankAccount("Minsu", 1000)
    jisu = SavingsAccount("Jisu", 500, 100)
    book = AccountBook()
    book.add_account(minsu)
    book.add_account(jisu)
    print("Withdraw:", minsu.withdraw(300), minsu.get_balance())
    print("Rejected:", minsu.withdraw(900), minsu.get_balance())
    print("Bonus:", jisu.add_bonus(), jisu.get_balance())
    for owner, kind, balance in book.report():
        print(owner, kind, balance)
    print("Total:", book.total_balance())


if __name__ == "__main__":
    main()
