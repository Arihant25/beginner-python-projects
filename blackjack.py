import os
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

logo = '''

       db                   88 88                                                     88888888ba  88                       88        88                       88
      d88b                  "" 88                                  ,d                 88      "8b 88                       88        ""                       88
     d8'`8b                    88                                  88                 88      ,8P 88                       88                                 88
    d8'  `8b     8b,dPPYba, 88 88,dPPYba,  ,adPPYYba, 8b,dPPYba, MM88MMM ,adPPYba,    88aaaaaa8P' 88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8
   d8YaaaaY8b    88P'   "Y8 88 88P'    "8a ""     `Y8 88P'   `"8a  88    I8[    ""    88""""""8b, 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"
  d8""""""""8b   88         88 88       88 ,adPPPPP88 88       88  88     `"Y8ba,     88      `8b 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[
 d8'        `8b  88         88 88       88 88,    ,88 88       88  88,   aa    ]8I    88      a8P 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,
d8'          `8b 88         88 88       88 `"8bbdP"Y8 88       88  "Y888 `"YbbdP"'    88888888P"  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a
                                                                                                                                    ,88
                                                                                                                                  888P"

'''


def screen_clear():
    """Clears the terminal output"""
    os.system('cls')


def blackjack():

    your_cards = []
    CPU_cards = []
    CPU_score = 0

    def random_card():
        """Deals a random card"""
        return random.choice(cards)

    def another_card():
        """Asks users if they want to draw one more card"""
        return input("Type 'y' to get another card, or type 'n' to pass: ").lower()

    print(logo)

    # Adds 2 cards to everyone's hands at first

    for _ in range(2):
        your_cards.append(random_card())
        CPU_cards.append(random_card())

    def displayScore(your_cards, your_score, CPU_cards):
        """Displays everyone's scores onscreen"""

        print(f"Your cards: {your_cards}, current score: {your_score}")

        print(f"Computer's first card: {CPU_cards[0]}")

    def calculate_score(your_cards):
        """Calculates player's score"""

        your_score = sum(your_cards)

        # Converts Aces from 11 to 1

        if your_score > 21:
            while 11 in your_cards:
                your_cards.remove(11)
                your_cards.append(1)
                your_score = sum(your_cards)

        return your_score

    your_score = calculate_score(your_cards)
    displayScore(your_cards, your_score, CPU_cards)

    CPU_score = sum(CPU_cards)

    # Checks for Blackjacks

    if CPU_score == 21:
        return "The computer has a blackjack. You lose."

    elif your_score == 21:
        return "You have a blackjack. You win!"

    # Adds cards to CPU's hand

    while CPU_score < 17:
        CPU_cards.append(random_card())
        CPU_score = sum(CPU_cards)

    while another_card() == 'y':
        your_cards.append(random_card())
        your_score = calculate_score(your_cards)

        displayScore(your_cards, your_score, CPU_cards)

        # Checks for Blackjacks

        if CPU_score == 21:
            return "The computer has a blackjack. You lose."

        elif your_score == 21:
            return "You have a blackjack. You win!"

        if calculate_score(your_cards) > 21:
            return "You exceeded 21. You lose!"

    print(f"Your final hand: {your_cards}, final score: {your_score}")
    print(f"Computer's final hand: {CPU_cards}, final score: {CPU_score}")

    # Win/Lose Conditions

    if your_score > CPU_score:
        return "Congrats, you win!"
    elif CPU_score > 21:
        return "The computer exceeded 21. You win!"
    elif your_score == CPU_score:
        return "It's a draw!"
    else:
        return "You lose."


should_continue = input(
    "Do you want to play a game of Arihant's Blackjack? Type 'yes' or 'no': ").lower()

while should_continue == 'yes':
    print(blackjack())
    should_continue = input(
        "\nDo you want to play again? Type 'yes' or 'no': ").lower()

    screen_clear()


print("Thank you for playing Arihant's Blackjack!\n")

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.
