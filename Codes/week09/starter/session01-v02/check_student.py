"""Student checks / 학생용 검사. Run after completing the three TODOs."""
from accounts import BankAccount, SavingsAccount, AccountBook

for cls in [BankAccount, SavingsAccount]:
    account = cls("A", 100)
    for bad in [0, -1, 101, 1.5, "10", True]:
        assert account.withdraw(bad) is False, (cls.__name__, bad)
        assert account.get_balance() == 100
    assert account.withdraw(100) is True
    assert account.get_balance() == 0

empty = AccountBook()
assert empty.total_balance() == 0 and empty.report() == []
a, b = BankAccount("Minsu", 1000), SavingsAccount("Jisu", 500, 100)
book = AccountBook()
assert book.add_account(a) and book.add_account(b)
assert not book.add_account(a)
a.withdraw(300)
b.add_bonus()
assert book.total_balance() == 1300
assert book.report() == [("Minsu", "Standard", 700), ("Jisu", "Savings", 600)]
a.deposit(50)
assert book.total_balance() == 1350
assert empty.total_balance() == 0
print("All student checks passed / 학생용 검사 통과")
