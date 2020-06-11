soda = ["Coca Cola", "Sprite", "Thumbs Up"]
chips = ["Lays", "Kurkure"]
candy = ["Dairy Milk", "Eclairs", "Bubblegum"]
while True:
    try:
        choice = input("Would you like a SODA, some CHIPS, or a CANDY? ").lower()
        if choice == "soda":
            snack = soda.pop()
        elif choice == "chips":
            snack = chips.pop()
        elif choice == "candy":
            snack = candy.pop()
        else:
            print("Sorry, I didn't understand that.")
            continue
    except IndexError:
        print("We're all out of {}!".format(choice))
    else:
        print("Here's your {}: {}".format(choice, snack))
