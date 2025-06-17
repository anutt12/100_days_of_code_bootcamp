# Range Function with For Loop

sum_of_numbers = 0
for number in range(1, 101):
    sum_of_numbers += number
print(sum_of_numbers)

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)