"""Lab: complete BankAccount, then compare the output with slide 31.

Assume a nonnegative integer starting balance and integer amounts.
TODO methods intentionally return placeholder values. This starter runs,
but its results will be wrong until you complete all four methods.
"""


class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        # TODO: store balance in the instance attribute self._balance.
        self._balance = 0

    def get_balance(self):
        # TODO: return the current balance.
        return 0

    def deposit(self, amount):
        # TODO: reject zero/negative amounts without changing the balance.
        # Otherwise, increase the balance and return True.
        return False

    def withdraw(self, amount):
        # TODO: reject zero/negative amounts and amounts above the balance.
        # Otherwise, decrease the balance and return True.
        return False


if __name__ == "__main__":
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

    # Add two more checks: depositing zero and withdrawing a negative amount.
    # Explain why a rejected operation must leave the balance unchanged.
