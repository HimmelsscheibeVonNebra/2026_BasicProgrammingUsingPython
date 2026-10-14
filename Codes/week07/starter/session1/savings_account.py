"""Optional lab: keep this beside your completed bank_account.py.

For Colab, paste the completed BankAccount class above this code and
remove the import line. Starting balance is a nonnegative integer and
bonus is a positive integer. Placeholder results are intentionally wrong.
"""

from bank_account import BankAccount


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance, bonus):
        # TODO: initialize the parent with owner and balance using super().
        # This placeholder keeps the starter runnable.
        super().__init__(owner, 0)
        # TODO: store the supplied bonus.
        self.bonus = 0

    def add_bonus(self):
        # TODO: call the inherited deposit method and return its result.
        return False


if __name__ == "__main__":
    savings = SavingsAccount("Minsu", 10000, 500)
    print(savings.add_bonus())      # Expected after completion: True
    print(savings.get_balance())    # Expected after completion: 10500
