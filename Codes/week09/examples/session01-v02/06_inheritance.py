"""Runnable lecture example / 강의용 실행 예제."""
from models import BankAccount, SavingsAccount

savings = SavingsAccount("Jisu", 500, 100)
savings.add_bonus()
savings.add_bonus()
print("Two fixed bonuses:", savings.get_balance())
accounts = [BankAccount("Minsu", 700), SavingsAccount("Jisu", 600, 100)]
for account in accounts:
    print(account.owner, account.account_type(), account.get_balance())
