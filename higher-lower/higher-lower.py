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

    while True:

        a = data[random_index]
        b = data[second_random_index]

        print(
            f"Compare A: {data[random_index]['name']}, a {data[random_index]['description']}, from {data[random_index]['country']}")

        print(vs)

        print(
            f"Against B: {data[second_random_index]['name']}, a {data[second_random_index]['description']}, from {data[second_random_index]['country']}\n")

        answer = input(
            "Who has more followers on Instagram? Type 'A' or 'B': ").upper()

        if data[random_index]['follower_count'] > data[second_random_index]['follower_count']:
            correct_answer = 'A'

        else:
            correct_answer = 'B'

        if answer == correct_answer:
            score += 1
            screen_clear()
            print(f"You're right! Current score: {score}")
            random_index = second_random_index
            second_random_index = randint(0, 49)

        else:
            print(f"Wrong answer! Your final score was {score}.")
            break

    should_continue = input("Play again? Type 'Y' or 'N': ").upper()

print("\nThanks for playing The Higher Lower Game!\n")
