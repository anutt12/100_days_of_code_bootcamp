print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ").strip().upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").strip().upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").strip().upper()

# My Solution

price = 0
valid_order = True

# Size selection
if size == "S":
    price += 15
elif size == "M":
    price += 20
elif size == "L":
    price += 25
else:
    print("You have chosen an invalid size.")
    valid_order = False

# Pepperoni selection
if pepperoni == "Y":
    if size == "S":
        price += 2
    elif size in ["M", "L"]:
        price += 3
    print("Pepperoni added.")
elif pepperoni == "N":
    print("Pepperoni not added.")
else:
    print("You have chosen an invalid pepperoni choice.")
    valid_order = False

# Extra cheese selection
if extra_cheese == "Y":
    price += 1
    print("Extra cheese added.")
elif extra_cheese == "N":
    print("Extra cheese not added.")
else:
    print("You have chosen an invalid extra cheese choice.")
    valid_order = False

# Final bill
if valid_order:
    print(f"Your final bill is: ${price}.")
else:
    print("Order cannot be completed due to invalid selections.")

# Course Solution
# bill = 0
# if size == "S":
#     bill += 15
# elif size == "M":
#     bill += 20
# elif size == "L":
#     bill += 25
# else:
#     print("You typed the wrong inputs.")
#
# if pepperoni == "Y":
#     if size == "S":
#         bill += 2
#     else:
#         bill += 3
#
# if extra_cheese == "Y":
#     bill += 1
#
# print(f"Your final bill is: ${bill}.")
