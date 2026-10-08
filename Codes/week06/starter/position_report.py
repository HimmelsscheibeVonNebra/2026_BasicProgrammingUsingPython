"""Practice 2: the portfolio as objects.
Tests: five profit lines / Saved
portfolio_report.txt.
"""

class Position:
    def __init__(self, ticker, shares, buy):
        self.ticker = ticker
        self.shares = shares
        self.buy = buy
    # TODO: add profit(self, close) that returns
    # (close - self.buy) * self.shares


rows = [("CODE", 10, 10000), ("TEA", 40, 5000),
        ("ROBO", 5, 40000), ("MLBK", 30, 2000),
        ("FIT", 20, 3000)]
closes = {"CODE": 10800, "TEA": 4800,
          "ROBO": 45000, "MLBK": 2500,
          "FIT": 4200}
# TODO: build a Position for each row, print
# "TICKER +N" (or "TICKER -N") for each, write
# the same lines to portfolio_report.txt, and
# print Saved portfolio_report.txt last.
