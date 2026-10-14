"""Step 6: extend BankAccount with a fixed bonus.

Self-contained for copying into Colab. Same BankAccount as Step 5.
Starting balance is a nonnegative integer and bonus is a positive integer.
add_bonus adds the fixed amount each time it is called.
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


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, bonus):
        super().__init__(owner, balance)
        self.bonus = bonus

    def add_bonus(self):
        return self.deposit(self.bonus)


savings = SavingsAccount("Minsu", 10000, 500)
print("Start:", savings.get_balance())
print("Bonus:", savings.add_bonus(), savings.get_balance())
print("Deposit:", savings.deposit(1000), savings.get_balance())
print("Withdraw:", savings.withdraw(1500), savings.get_balance())
print("Rejected:", savings.withdraw(20000), savings.get_balance())
