# This program asks you for your age in years and tell you the number of days, weeks, and months you have left to be alive.

# Asks for the age and stores it as an integer
age = int(input("What is your current age (in years)?\n"))

# Calculates the result
years_left = 90 - age
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12

# Outputs the result
print(
    f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left to live. So make the most of it! 😃")
