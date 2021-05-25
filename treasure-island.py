print("""
 ______   ______     ______     ______     ______     __  __     ______     ______           __     ______     __         ______     __   __     _____    
/\__  _\ /\  == \   /\  ___\   /\  __ \   /\  ___\   /\ \/\ \   /\  == \   /\  ___\         /\ \   /\  ___\   /\ \       /\  __ \   /\ "-.\ \   /\  __-.  
\/_/\ \/ \ \  __<   \ \  __\   \ \  __ \  \ \___  \  \ \ \_\ \  \ \  __<   \ \  __\         \ \ \  \ \___  \  \ \ \____  \ \  __ \  \ \ \-.  \  \ \ \/\ \ 
   \ \_\  \ \_\ \_\  \ \_____\  \ \_\ \_\  \/\_____\  \ \_____\  \ \_\ \_\  \ \_____\        \ \_\  \/\_____\  \ \_____\  \ \_\ \_\  \ \_\\"\_\  \ \____- 
    \/_/   \/_/ /_/   \/_____/   \/_/\/_/   \/_____/   \/_____/   \/_/ /_/   \/_____/         \/_/   \/_____/   \/_____/   \/_/\/_/   \/_/ \/_/   \/____/ 
                                                                                                                                                          
""")

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
''')


def wrongOption():
    print("You didn't choose one of the options correctly in time.")
    print("GAME OVER, YOU LOSE!")


# The game starts here

crossroad = (input(
    ('After travelling for weeks without food, you\'re at a cross road. Where do you want to go? Type "left" or "right. Choose quickly, before you die of hunger!"\n'))).lower()

if crossroad == "right":
    print('You think, "Right is always right, right?" and head towards the right. Wrong! You were so busy thinking of that tounge-twister that you didn\'t watch your step and fell into a hole and died.')
    print("GAME OVER, YOU LOSE!")

elif crossroad == "left":
    print("You get bad vibes from the right side, so you go towards the left.")
    lake = (input(('You come to a lake. There\'s an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n'))).lower()

    if lake == "wait":
        print("You arrive at the island unharmed.")
        door = (input(
            ("There is a house with 3 doors. One red, one yellow, and one blue. Which colour do you choose?\n"))).lower()

        if door == "red":
            print(
                "In your haste, you rush into the first room you see. Too bad it was full of fire.")
            print("GAME OVER, YOU LOSE!")

        elif door == "blue":
            print(
                "You enter a room full of hungry beasts. Don't feel bad, at least they said you were delicious!")
            print("GAME OVER, YOU LOSE!")

        elif door == "yellow":
            print('You found the treasure chest! You open it eagerly, only to find a messsage saying, "The real treasure was the friends you made along the way." Too bad you made the journey alone.')
            print("GAME OVER, YOU WIN...?")

        else:
            wrongOption()

    elif lake == "swim":
        print("You poor soul. Did no one tell you about the shark-infested waters? You were devoured before you even knew what was happening.")
        print("GAME OVER, YOU LOSE!")

    else:
        wrongOption()
else:
    wrongOption()
