import random

print("""

 ██████╗ ██╗   ██╗███████╗███████╗███████╗    ████████╗██╗  ██╗███████╗    ███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗ ██╗
██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝    ╚══██╔══╝██║  ██║██╔════╝    ████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗██║
██║  ███╗██║   ██║█████╗  ███████╗███████╗       ██║   ███████║█████╗      ██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝██║
██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║       ██║   ██╔══██║██╔══╝      ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗╚═╝
╚██████╔╝╚██████╔╝███████╗███████║███████║       ██║   ██║  ██║███████╗    ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║██╗
 ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝       ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝

""")

print("Welcome to Guess The Number!")

print("I'm thinking of a number from 1 to 100.")

# Chooses a random number

number = random.randint(1, 100)

difficulty = input("Choose a difficulty: 'easy' or 'hard': ").lower()

if difficulty == 'easy':
    attempts = 10

elif difficulty == 'hard':
    attempts = 5

while attempts > -1:

    print(f"You have {str(attempts)} attempts remaining to guess the number.")

    guess = int(input("Make a guess: "))

    if guess == number:
        print(f"You got it! The answer was {number}.")
        break

    if guess > number:
        print("Too high.")

    if guess < number:
        print("Too low.")

    attempts -= 1

    if attempts == 0:
        print(
            f"You don't have any attempts remaining. The answer was {number}.")
        break

    print("Guess again.")
