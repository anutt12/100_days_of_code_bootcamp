from random_word import RandomWords


def ask_play_again():
    """
    Prompts the user to decide if they want to play again and validates input.

    This function repeatedly asks the user if they want to play again until valid input
    is provided.
    The valid inputs are 'yes', 'no', 'y', or 'n', and the function
    returns a boolean value indicating the user's choice.

    Returns:
        bool: True if the user chooses 'yes' or 'y', False if the user chooses 'no'
        or 'n'.
    """
    while True:
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again in ['yes', 'no', 'y', 'n']:
            return play_again.startswith('y')
        print("Please answer 'yes' or 'no'")


def get_player_guess(guessed_letters):
    """
    Prompts the player to guess a letter, validates the input, and ensures it has not been guessed before.

    Parameters:
        guessed_letters (list[str]): A list of letters already guessed by the player.

    Returns:
        str: A single valid letter that the player guesses.
    """
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Please enter a single letter!")
        elif not guess.isalpha():
            print("Please enter a letter from the alphabet!")
        elif guess in guessed_letters:
            print("You already guessed that letter. Try another one!")
        else:
            return guess


def process_guess(guess, word, word_letters, word_display, guessed_letters):
    """
    Processes a guessed letter for a word guessing game, checks its presence in the target word,
    and updates relevant states such as guessed letters, the displayed word, and correctness of
    the guess.

    Args:
        guess: The guessed letter to process.
        word: The target word to guess.
        word_letters: A set containing the unique letters in the target word.
        word_display: A list representing the displayed word with correct guesses revealed.
        guessed_letters: A set of letters already guessed by the player.

    Returns:
        True if the guessed letter is correct, False otherwise.
    """
    guessed_letters.add(guess)
    if guess in word_letters:
        print("\nCorrect!")
        for i, letter in enumerate(word):
            if letter == guess:
                word_display[i] = guess
        return True
    print("\nWrong!")
    return False


class HangmanGame:
    """
    Manages the logic for running a game of Hangman.

    The HangmanGame class allows players to play the traditional word-guessing Hangman game.
    In the game, the user must guess the letters of a randomly chosen word while attempting
    to avoid running out of lives.
    The class handles the game's state, user interactions,
    and scoring system.
    """
    MAX_LIVES = 6
    HANGMAN_STAGES = [  # Final state: head, torso, both arms, and both legs
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        # Head, torso, both arms, and one leg
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
           -
        """,
        # Head, torso, and both arms
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
           -
        """,
        # Head, torso, and one arm
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
           -
        """,
        # Head and torso
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |
           -
        """,
        # Head
        """
           --------
           |      |
           |      O
           |
           |
           |
           -
        """,
        # Initial empty state
        """
           --------
           |      |
           |
           |
           |
           |
           -
        """
    ]

    def __init__(self):
        self.score = 0
        self.random_words = RandomWords()

    def display_game_header(self):
        print("\n" * 2)
        print("=" * 20)
        print("  HANGMAN GAME")
        print(f"Current Score: {self.score}")
        print("=" * 20)

    def display_game_state(self, word_display, lives, guessed_letters):
        print(self.HANGMAN_STAGES[lives])
        print("\nWord:", " ".join(word_display))
        print(f"Lives remaining: {lives}")
        print("Guessed letters:", " ".join(sorted(guessed_letters)))

    def play_round(self):
        word = self.random_words.get_random_word()
        word_letters = set(word)
        guessed_letters = set()
        lives = self.MAX_LIVES
        word_display = ["_" for _ in word]

        self.display_game_header()

        while lives > 0 and len(word_letters - guessed_letters) > 0:
            self.display_game_state(word_display, lives, guessed_letters)
            guess = get_player_guess(guessed_letters)

            if not process_guess(guess, word, word_letters, word_display, guessed_letters):
                lives -= 1

            input("\nPress Enter to continue...")
            print("\n" * 2)

        self.handle_game_end(lives, word_display, word)

    def handle_game_end(self, lives, word_display, word):
        print(self.HANGMAN_STAGES[lives])
        print("\nWord:", " ".join(word_display))

        if lives > 0:
            print("\n🎉 Congratulations! You won! 🎉")
            self.score += 1
        else:
            print("\n💀 Game Over! You ran out of lives! 💀")
            print(f"The word was: {word}")
        print(f"Current Score: {self.score}")

    def play(self):
        while True:
            self.play_round()
            if not ask_play_again():
                print(f"\nThanks for playing! Final Score: {self.score}")
                break


if __name__ == "__main__":
    game = HangmanGame()
    game.play()
