# This program asks you for your bill amount and the tip percentage you want to give, and then splits it among the number of people you want.

print("Welcome to the Tip Calculator!")

# Asks for the bill amount and stores it as a float

bill = float(input("What was the total bill?\n"))

# Asks for the tip percentage and stores it as a float

tip = float(input("What percentage tip would you like to give?\n"))

# Asks for the number of people and stores it as int

people = int(input("How many people to split the bill among?\n"))

# Calculates the result

final_amount = bill + bill * tip/100
split_amount = final_amount / people

# Outputs the result

print("\nThe final amount is {:0.2f}.".format(final_amount))
print("Each person should pay {:0.2f}.\n".format(split_amount))

print("Thank you for using the Tip Calculator!\n")
