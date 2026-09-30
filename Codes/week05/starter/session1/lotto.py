"""Lab 2: generate lotto games. Assume integer-formatted input.
Tests: 1 -> one line of 6 sorted unique numbers; 6 -> Invalid games.
"""
import random

games = int(input("Games (1-5): "))
if 1 <= games <= 5:
    for game in range(1, games + 1):
        # TODO: draw 6 different numbers from 1 to 45,
        # sort them, and print them on one line.
        pass
else:
    print("Invalid games")
