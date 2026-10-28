"""Runnable lecture example / 강의용 실행 예제."""
from models import BankAccount

a = BankAccount("Minsu", 1000)
for action, amount in [("deposit", 200), ("withdraw", 500),
                       ("withdraw", 900), ("withdraw", -50),
                       ("withdraw", 700)]:
    result = getattr(a, action)(amount)
    print(action, amount, result, a.get_balance())

# Check both return and state. / 반환값과 상태를 함께 검사.
a = BankAccount("Minsu", 1000)
assert a.withdraw(1200) is False
assert a.get_balance() == 1000
assert a.withdraw(1000) is True
assert a.get_balance() == 0
print("State checks passed")
