import os
from random import randint
from art import logo, vs
from data import data


def screen_clear():
    """Clears the terminal output and shows the game logo"""
    os.system('cls')
    print(logo)


should_continue = 'Y'

while should_continue == 'Y':

    screen_clear()

    score = 0

    random_index = randint(0, 49)
    second_random_index = randint(0, 49)
    if second_random_index == random_index:
        second_random_index = randint(0, 49)

    def format_account(account):
        """Gets account data and displays it in a readable format"""
        return f"{account['name']}, a {account['description']}, from {account['country']}"

    while True:

        # Gets A and B from the data

        a = data[random_index]
        b = data[second_random_index]

        print(
            f"Compare A: {format_account(a)}")

        print(vs)

        print(
            f"Against B: {format_account(b)}\n")

        answer = input(
            "Who has more followers on Instagram? Type 'A' or 'B': ").upper()

        # Finds the correct answer

        if a['follower_count'] > b['follower_count']:
            correct_answer = 'A'

        else:
            correct_answer = 'B'

        # Win/Lose Conditions

        if answer == correct_answer:

            score += 1

            screen_clear()

            print(f"You're right! Current score: {score}")

            # Reassigns A to B and B to a new account

            random_index = second_random_index
            second_random_index = randint(0, 49)

        else:
            print(f"\nWrong answer! Your final score was {score}.\n")
            break

    should_continue = input("Play again? Type 'Y' or 'N': ").upper()

print("\nThanks for playing The Higher Lower Game!\n")
