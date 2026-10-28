"""Runnable lecture example / 강의용 실행 예제."""
from models import BankAccount, AccountBook

a = BankAccount("Minsu", 1000)
book, other = AccountBook(), AccountBook()
print("First registration:", book.add_account(a))
print("Duplicate registration:", book.add_account(a))
snapshot = book.report()
a.withdraw(300)
print("Current total:", book.total_balance())
print("Old report values:", snapshot)
print("New report values:", book.report())
print("Independent empty book:", other.total_balance(), other.report())
