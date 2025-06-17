from enum import Enum
import random
from typing import Optional, Tuple


class GameChoice(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2


# ASCII art representations stored as constants
ROCK_ART = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

PAPER_ART = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

SCISSORS_ART = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


def get_user_choice() -> Optional[GameChoice]:
    """
    Get and validate user input for their game choice.
    Returns GameChoice enum or None if input is invalid.
    """
    try:
        choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
        if 0 <= choice <= 2:
            return GameChoice(choice)
        print("Please enter a number between 0 and 2.")
        return None
    except ValueError:
        print("Please enter a valid number.")
        return None


def get_computer_choice() -> GameChoice:
    """Generate a random choice for the computer."""
    return GameChoice(random.randint(0, 2))


def get_choice_art(choice: GameChoice) -> str:
    """Return ASCII art for the given choice."""
    art_map = {
        GameChoice.ROCK: ROCK_ART,
        GameChoice.PAPER: PAPER_ART,
        GameChoice.SCISSORS: SCISSORS_ART
    }
    return art_map[choice]


def determine_winner(user_choice: GameChoice, computer_choice: GameChoice) -> str:
    """
    Determine the winner of the game.
    Returns a string indicating the result.
    """
    if user_choice == computer_choice:
        return "It's a draw!"

    winning_combinations = {
        GameChoice.ROCK: GameChoice.SCISSORS,
        GameChoice.PAPER: GameChoice.ROCK,
        GameChoice.SCISSORS: GameChoice.PAPER
    }

    if winning_combinations[user_choice] == computer_choice:
        return "You win!"
    return "Computer wins!"


def play_again() -> bool:
    """Ask if the user wants to play again."""
    while True:
        choice = input("\nDo you want to play again? (Y/N): ").strip().upper()
        if choice in ['Y', 'N']:
            return choice == 'Y'
        print("Please enter Y or N.")

def play_game():
    """Main game function."""
    print("Welcome to the Rock Paper Scissors Game!")
    
    while True:
        user_choice = get_user_choice()
        if user_choice is None:
            continue

        computer_choice = get_computer_choice()

        print(f"\nYou chose:\n{get_choice_art(user_choice)}")
        print(f"\nComputer chose:\n{get_choice_art(computer_choice)}")

        result = determine_winner(user_choice, computer_choice)
        print(f"\n{result}")

        if not play_again():
            print("\nThanks for playing!")
            break

if __name__ == "__main__":
    play_game()