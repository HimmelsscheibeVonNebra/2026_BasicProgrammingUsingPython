"""Lab 3 reference solution: one round of rock-paper-scissors."""

import random

options = ["rock", "paper", "scissors"]
player = input("Your choice: ").strip().lower()
computer = random.choice(options)

if player not in options:
    print("Invalid choice")
else:
    print(f"You: {player}, computer: {computer}")
    if player == computer:
        print("Tie")
    elif (
        (player == "rock" and computer == "scissors")
        or (player == "scissors" and computer == "paper")
        or (player == "paper" and computer == "rock")
    ):
        print("You win")
    else:
        print("You lose")

# Tests with computer temporarily fixed to "scissors":
# " ROCK " -> You win
# "paper" -> You lose
# "scissors" -> Tie
# "lizard" or "" -> Invalid choice
# Restore random.choice(options) after testing.
