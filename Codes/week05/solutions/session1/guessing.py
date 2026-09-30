"""Lab 3 solution: number guessing game."""
import random

secret = random.randint(1, 100)
attempts = 0
while True:
    guess = int(input("Guess: "))
    attempts += 1
    if guess < secret:
        print("Higher")
    elif guess > secret:
        print("Lower")
    else:
        print("Correct! Attempts:", attempts)
        break
