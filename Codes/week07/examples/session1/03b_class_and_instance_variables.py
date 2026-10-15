"""Compare shared class data with each account's instance data."""


class BankAccount:
    bank_name = "Python Bank"  # class variable

    def __init__(self, owner, balance):
        self.owner = owner    # instance variable
        self.balance = balance


if __name__ == "__main__":
    minsu = BankAccount("Minsu", 10000)
    jisu = BankAccount("Jisu", 5000)
    print(minsu.bank_name, jisu.bank_name)
    print(minsu.balance, jisu.balance)

    # Updating the class changes the value both accounts read.
    BankAccount.bank_name = "Campus Bank"
    print(minsu.bank_name, jisu.bank_name)

    # Assignment on one instance creates its own attribute of this name.
    minsu.bank_name = "Minsu Bank"
    print(minsu.bank_name, jisu.bank_name)
    print(BankAccount.bank_name)

    # Each account also keeps its own balance.
    minsu.balance = 13000
    print(minsu.balance, jisu.balance)
