"""Runnable lecture example / 강의용 실행 예제."""
class BadBook:
    accounts = []


class IndependentBook:
    def __init__(self):
        self.accounts = []


first, second = BadBook(), BadBook()
first.accounts.append("Minsu")
print("Shared class list:", second.accounts)
first, second = IndependentBook(), IndependentBook()
first.accounts.append("Minsu")
print("Independent instance list:", second.accounts)
