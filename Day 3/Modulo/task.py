try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid integer number")

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
