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

    def random_card():
        return random.choice(cards)

    def another_card():
        """Asks users if they want to draw one more card"""
        return input("Type 'y' to get another card, or type 'n' to pass: ").lower()

    def calculate_score():
        """Calculates player's score and displays it onscreen"""

        your_score = sum(your_cards)

        print(f"Your cards: {your_cards}, current score: {your_score}")

        print(f"Computer's first card: {CPU_cards[0]}")

        return your_score

    print(logo)

    your_cards = []
    CPU_cards = []
    CPU_score = 0

    # Adds 2 cards to your hand at first

    for i in range(2):
        your_cards.append(random_card())

    # Adds cards to CPU's hand

    while CPU_score < 17:
        CPU_cards.append(random_card())
        CPU_score = sum(CPU_cards)
    CPU_score = sum(CPU_cards)

    your_score = calculate_score()

    while another_card() == 'y':
        your_cards.append(random_card())
        print(your_cards)
        calculate_score()

        your_score = sum(your_cards)
        if your_score > 21:
            return ("You exceeded 21. You lose!")

    print(f"Your final hand: {your_cards}, final score: {your_score}")
    print(f"Computer's final hand: {CPU_cards}, final score: {CPU_score}")

    if your_score > CPU_score:
        return ("Congrats, you win!")
    elif CPU_score > 21:
        return("The computer exceeded 21. You win!")
    elif your_score == CPU_score:
        return ("It's a draw!")
    else:
        return ("You lose.")


should_continue = input(
    "Do you want to play a game of Arihant's Blackjack? Type 'yes' or 'no': ").lower()

while should_continue == 'yes':
    print(blackjack())
    should_continue = input(
        "\nDo you want to play again? Type 'yes' or 'no': ").lower()

    screen_clear()


print("Thank you for playing Arihant's Blackjack!")


############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
# Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
# user_cards = []
# computer_cards = []

# Hint 6: Create a function called calculate_score() that takes a List of cards as input
# and returns the score.
# Look up the sum() function to help you do this.

# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
