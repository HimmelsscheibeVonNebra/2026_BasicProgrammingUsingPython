"""Runnable lecture example / 강의용 실행 예제."""
from models import BankAccount

for owner, balance in [(" ", 0), ("Minsu", -100), ("Minsu", True)]:
    try:
        BankAccount(owner, balance)
    except ValueError as error:
        print("Rejected construction:", error)

account = BankAccount("Minsu", 1000)
for amount in [0, -10, 1.5, "10", True, 200]:
    before = account.get_balance()
    result = account.deposit(amount)
    print(repr(amount), result, before, account.get_balance())
print("bool is an int subclass:", isinstance(True, int))
print("bool is exactly int:", type(True) is int)
