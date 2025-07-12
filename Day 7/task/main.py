import random
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []
lives = 6

while not game_over:
    guess = input("Guess a letter: ").lower()

    display = ""
    was_correct = False

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
            was_correct = True
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if not was_correct:
        lives -= 1
        if lives == 0:
            print("You lose!")
            game_over = True

    print(display)
    print(stages[lives])

    if "_" not in display:
        print("You win!")
        game_over = True