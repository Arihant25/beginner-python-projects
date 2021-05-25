# This program will select a random name from a list of names. The person selected will have to pay for everybody's food bill.

import random

print("Welcome to Banker's Roulette!")

# For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(', ')

result = random.randint(0, len(names) - 1)

print(f"{names[result]} is going to pay for the meal today!")
