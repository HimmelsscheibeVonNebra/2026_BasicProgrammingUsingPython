"""Runnable lecture example / 강의용 실행 예제."""
from models import BankAccount, SavingsAccount, AccountBook


def main():
    minsu = BankAccount("Minsu", 1000)
    jisu = SavingsAccount("Jisu", 500, 100)
    book = AccountBook()
    book.add_account(minsu)
    book.add_account(jisu)
    print("Withdraw:", minsu.withdraw(300), minsu.get_balance())
    print("Rejected:", minsu.withdraw(900), minsu.get_balance())
    print("Bonus:", jisu.add_bonus(), jisu.get_balance())
    for owner, kind, balance in book.report():
        print(owner, kind, balance)
    print("Total:", book.total_balance())


if __name__ == "__main__":
    main()
