"""Lab 2 solution: generate lotto games."""
import random

games = int(input("Games (1-5): "))
if 1 <= games <= 5:
    for game in range(1, games + 1):
        numbers = random.sample(range(1, 46), 6)
        numbers.sort()
        print(*numbers)
else:
    print("Invalid games")
