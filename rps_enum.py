import sys
import random
from enum import Enum, auto

class Choice(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()

def get_user_choice():
    while True:
        try:
            user_input = input('Enter either\n1. Rock\n2. Paper\n3. Scissors\n\n').capitalize()
            return Choice[user_input.upper()]
        except KeyError:
            print("Invalid input. Enter 'Rock', 'Paper', or 'Scissors'.")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == Choice.ROCK and computer_choice == Choice.SCISSORS) or
        (user_choice == Choice.PAPER and computer_choice == Choice.ROCK) or
        (user_choice == Choice.SCISSORS and computer_choice == Choice.PAPER)
    ):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    user_choice = get_user_choice()
    computer_choice = random.choice(list(Choice))

    print(f"You choose {user_choice.name}.")
    print(f"Computer chooses {computer_choice.name}.")

    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()
