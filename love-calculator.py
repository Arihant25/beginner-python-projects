# This program checks the compatibility between 2 people

print("Welcome to the Love Calculator!")

# Asks for the names

name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

# Combines the names into one string to make it easier to check

combined_name = (name1 + name2).lower()

# Counts the number of times the letters in 'True Love' appear in the names

true = combined_name.count("t") + combined_name.count("r") + \
    combined_name.count("u") + combined_name.count("e")

love = combined_name.count("l") + combined_name.count("o") + \
    combined_name.count("v") + combined_name.count("e")

# Forms the score

score = int(str(true) + str(love))

# Shows the result

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like Coke and Mentos.")

elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")

else:
    print(f"Your score is {score}.")
