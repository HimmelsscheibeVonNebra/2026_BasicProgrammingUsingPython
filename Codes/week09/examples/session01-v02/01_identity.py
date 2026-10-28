"""Runnable lecture example / 강의용 실행 예제."""
from models import BankAccount

a = BankAccount("Minsu", 1000)
b = BankAccount("Jisu", 500)
a.deposit(200)
print("Separate accounts:", a.get_balance(), b.get_balance())
alias = a
alias.withdraw(300)
print("Shared reference:", a.get_balance(), alias is a)

# Reset before the slide 8 prediction. / 슬라이드 8은 새 상태에서 시작.
a = BankAccount("Minsu", 1000)
b = BankAccount("Jisu", 500)
c = a
accounts = [a, b]
accounts[0].withdraw(200)
print("Slide 8:", c.get_balance(), b.get_balance())
accounts[0] = b
print("After replacing list element:", c.get_balance(), accounts[0] is b)
