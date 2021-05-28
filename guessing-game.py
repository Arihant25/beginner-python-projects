import random

tries = 0
limit = int(input("Till what number do you want me to think of?"))
number = random.randint(1, limit)
guess = int(input("I'm thinking of a number from 1 to " +
                  str(limit) + ". What is it?"))

while guess != number:
    if guess < number:
        print("Your number was too low...")
        tries = tries + 1
    else:
        print("Your number was too high...")
        tries = tries + 1
    guess = int(input("Please try again..."))
print("Congratulations! It took you " +
      str(tries) + " tries to reach the answer!")
if tries > 1:
    print("You can do better!")
else:
    print("Your luck is shining today!")
