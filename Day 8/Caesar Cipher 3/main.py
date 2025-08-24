# TODO-1: Import and print the logo from art.py when the program starts.
import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


# TODO-2: What happens if the user enters a number/symbol/space?


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    shift_amount = shift_amount % 26

    for letter in original_text:
        if letter.isalpha():
            position = alphabet.index(letter)
            if encode_or_decode == "decode":
                new_position = (position - shift_amount) % len(alphabet)
            else:
                new_position = (position + shift_amount) % len(alphabet)
            output_text += alphabet[new_position]
        else:
            output_text += letter
    print(f"Here is the {encode_or_decode}d result: {output_text}")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    while direction not in ["encode", "decode"]:
        direction = input("Please type only 'encode' or 'decode':\n").lower()

    while True:
        text = input("Type your message:\n").lower()
        if all(c.isalpha() or c.isspace() for c in text):
            break
        print("Please enter only letters and spaces in your message")

    while True:
        try:
            shift = int(input("Type the shift number:\n"))
            break
        except ValueError:
            print("Please enter a valid number for the shift")

    caesar(text, shift, direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result == 'no':
        should_continue = False
        print("Goodbye")
