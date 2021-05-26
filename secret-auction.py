from os import system, name     # for clearing the screen


def clear():
    _ = system('cls')


print("Welcome to the Secret Auction!")
print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
''')


bids = {}

should_continue = 'yes'

while should_continue == 'yes':

    name = input("Please enter your name: ")
    amount = int(input("Enter the amount you would like to bid: "))

    bids[name] = amount

    clear()

    should_continue = input(
        "Are there more people? Type 'yes' or 'no': ").lower()

bid_list = []

for key in bids:
    bid_list.append(bids[key])

highest_bidder = list(bids.keys())[list(
    bids.values()).index(max(list(bids.values())))]

print(f"The highest bid was {max(bid_list)} by {highest_bidder}.")
