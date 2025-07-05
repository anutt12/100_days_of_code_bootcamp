import random

# Refactored Solution

# Character sets as constants
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = LOWERCASE_LETTERS.upper()
NUMBERS = '0123456789'
SPECIAL_SYMBOLS = '!#$%&()*+'


def get_password_requirements() -> tuple[int, int, int]:
    """Get password requirements from user input."""
    print("Welcome to the PyPassword Generator!")
    letter_count = int(input("How many letters would you like in your password?\n"))
    symbol_count = int(input("How many symbols would you like?\n"))
    number_count = int(input("How many numbers would you like?\n"))
    return letter_count, symbol_count, number_count


def generate_password(letter_count: int, symbol_count: int, number_count: int) -> str:
    """Generate a random password based on the specified requirements."""
    # Create list of all characters using list comprehensions
    password_chars = (
            [random.choice(LOWERCASE_LETTERS + UPPERCASE_LETTERS) for _ in range(letter_count)] +
            [random.choice(SPECIAL_SYMBOLS) for _ in range(symbol_count)] +
            [random.choice(NUMBERS) for _ in range(number_count)]
    )

    # Shuffle the characters and join them into a string
    random.shuffle(password_chars)
    return ''.join(password_chars)


def main() -> None:
    """Main function to run the password generator."""
    letter_count, symbol_count, number_count = get_password_requirements()
    password = generate_password(letter_count, symbol_count, number_count)
    print(f"Your password is: {password}")


if __name__ == "__main__":
    main()

# Provided Solution

# import random
#
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
#            'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
#            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
#
# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
#
# Easy Level
# password = ""
#
# for char in range(0, nr_letters):
#     password += random.choice(letters)
#
# for char in range(0, nr_symbols):
#     password += random.choice(symbols)
#
# for char in range(0, nr_numbers):
#     password += random.choice(numbers)
#
# print(password)
#
# Hard Level
# password_list = []
#
# for char in range(0, nr_letters):
#     password_list.append(random.choice(letters))
#
# for char in range(0, nr_symbols):
#     password_list.append(random.choice(symbols))
#
# for char in range(0, nr_numbers):
#     password_list.append(random.choice(numbers))
#
# print(password_list)
# random.shuffle(password_list)
# print(password_list)
#
# password = ""
# for char in password_list:
#     password += char
# print(f"Your password is: {password}")
