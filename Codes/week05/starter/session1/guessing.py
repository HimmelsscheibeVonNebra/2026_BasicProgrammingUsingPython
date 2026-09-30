"""Lab 3: number guessing game. Assume integer-formatted input.
Test: a finished game ends with Correct! Attempts: N.
"""
import random

secret = random.randint(1, 100)
attempts = 0
while True:
    guess = int(input("Guess: "))
    attempts += 1
    # TODO: print Higher or Lower, or print
    # "Correct! Attempts:" with the count and stop the loop.
