import random

WORDS = ("treehouse", "python", "learner",)


def prompt_for_words(challenge):
    guesses = set()
    print("What words can you find inside the word '{}'".format(challenge))
    print("Enter Q to quit.")
    while True:
        guess = input("{} words >    ".format(len(guesses))
        if guess.upper() == "Q":
            break
        guesses.add(guess.lower())
        return guesses

def output_results(results):
    for word in results:
        print("* " + word)

challenge_words = random.choice(WORDS)
player1_words = prompt_for_words(challenge_words)
player2_words = prompt_for_words(challenge_words)

print("Player 1 Results:")
player1_unique= player1_words - player2_words
print("{} guesses, {} unique").format(len(player1_words), len(player1_unique))
output_results(player1_unique)
print("-" * 10)

print("Player 2 Results:")
player2_unique= player2_words - player1_words
print("{} guesses, {} unique").format(len(player2_words), len(player2_unique))
output_results(player2_unique)

print("Shared Guesses:")
shared_words = player1_words & player2_words
output_results(shared_words)
