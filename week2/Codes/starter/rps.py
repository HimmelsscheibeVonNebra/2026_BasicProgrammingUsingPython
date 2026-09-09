"""Lab 3: Complete one round of rock-paper-scissors."""

import random

options = ["rock", "paper", "scissors"]
player = input("Your choice: ").strip().lower()
computer = random.choice(options)

# TODO: Print Invalid choice if player is not in options.
# TODO: For valid input, print the player and computer choices.
# TODO: Check for a tie, the three winning combinations, then a loss.
# Print exactly Tie, You win or You lose for the outcome.

# Testing tip: temporarily set computer = "scissors" for predictable results.
# Restore random.choice(options) before submission.
# Add at least three test inputs and expected results here.
