"""Week 7 recap / 7주차 복습: init, state, class variables, four principles."""
from models import BankAccount, SavingsAccount


class SimpleAccount:
    """Minimal recap without validation / 검증을 생략한 기본 구조."""
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount


class LabelledAccount:
    bank_name = "Python Bank"

    def __init__(self, owner):
        self.owner = owner


a = SimpleAccount("Minsu", 1000)
b = SimpleAccount("Jisu", 500)
a.deposit(200)
print("Instance state:", a.owner, a.balance, b.owner, b.balance)
assert (a.balance, b.balance) == (1200, 500)

first, second = LabelledAccount("Minsu"), LabelledAccount("Jisu")
LabelledAccount.bank_name = "Campus Bank"
print("Class variable:", first.bank_name, second.bank_name)
first.bank_name = "Minsu's Bank"
print("Instance shadowing:", first.bank_name, second.bank_name)
assert second.bank_name == "Campus Bank"

# Existing models demonstrate the four principles. / 완성 모델로 네 원리 확인.
accounts = [BankAccount("Minsu", 1000), SavingsAccount("Jisu", 500, 100)]
for account in accounts:
    before = account.get_balance()
    accepted = account.withdraw(-50)
    assert accepted is False and account.get_balance() == before
    print("Shared interface:", account.owner, account.account_type(), before)
print("Week 7 recap checks passed")
