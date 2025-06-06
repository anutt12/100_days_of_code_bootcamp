# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("What percentage tip would you like to give? 10 12 15 "))
# people = int(input("How many people to split the bill? "))
#
# percent = tip / 100
# total = bill + (bill * percent)
# bill_per_person = total / people
# final_amount = round(bill_per_person, 2)
#
# print(f"Each person should pay: ${final_amount:,.2f}")

print("Welcome to the tip calculator!")

# Get the bill amount with validation
while True:
    try:
        bill = float(input("What was the total bill? $"))
        if bill < 0:
            print("Bill amount can't be negative.")
        else:
            break
    except ValueError:
        print("Please enter a valid number.")

# Get the tip percentage with validation
while True:
    try:
        tip = float(input("What percentage tip would you like to give? (e.g., 10, 12, 15): "))
        if tip < 0:
            print("Tip percentage can't be negative.")
        else:
            break
    except ValueError:
        print("Please enter a valid percentage.")

# Get the number of people with validation
while True:
    try:
        people = int(input("How many people to split the bill? "))
        if people <= 0:
            print("There must be at least one person.")
        else:
            break
    except ValueError:
        print("Please enter a whole number.")

# Calculate the total and split
percent = tip / 100
total = bill + (bill * percent)
bill_per_person = total / people
final_amount = round(bill_per_person, 2)

# Display with commas and exactly 2 decimal places
print(f"Each person should pay: ${final_amount:,.2f}")
