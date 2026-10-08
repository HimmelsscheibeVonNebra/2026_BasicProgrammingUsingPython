"""Practice 1: read the trade journal by hand.
Tests: buy 6 / sell 4. trades.csv sits beside
this file.
"""
buys = 0
sells = 0
with open("trades.csv") as f:
    f.readline()   # skip the header
    # TODO: loop over the remaining lines,
    # strip and split each one, and count
    # "buy" and "sell" actions. Then print
    # both counts exactly as shown above.
