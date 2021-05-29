MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

water = resources['water']
milk = resources['milk']
coffee = resources['coffee']
money = 0

print("Welcome to the Coffee Machine Lite!")

print('''
                      (
                        )     (
                 ___...(-------)-....___
             .-""       )    (          ""-.
       .-'``'|-._             )         _.-|
      /  .--.|   `""---...........---""`   |
     /  /    |                             |
     |  |    |                             |
      \  \   |                             |
       `\ `\ |                             |
         `\ `|                             |
         _/ /\                             /
        (__/  \                           /
     _..---""` \                         /`""---.._
  .-'           \                       /          '-.
 :               `-.__             __.-'              :
 :                  ) ""---...---"" (                 :
  '._               `"--...___...--"`              _.'
    \""--..__                              __..--""/
     '._     """----.....______.....----"""     _.'
        `""--..,,_____            _____,,..--""`
                      `"""----"""`
''')

while True:
    command = input(
        "What coffee would you like? (espresso/latte/cappuccino): ").lower()

    make_coffee = False

    # Switches off the machine
    if command == "off":
        break

    # Generates report
    elif command == "report":
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Money: ${money}")

    elif command == "espresso":
        water_required = MENU['espresso']['ingredients']['water']
        coffee_required = MENU['espresso']['ingredients']['coffee']
        milk_required = 0
        cost = MENU['espresso']['cost']
        make_coffee = True

    elif command == "latte":
        water_required = MENU['latte']['ingredients']['water']
        coffee_required = MENU['latte']['ingredients']['coffee']
        milk_required = MENU['latte']['ingredients']['milk']
        cost = MENU['latte']['cost']
        make_coffee = True

    elif command == "cappuccino":
        water_required = MENU['cappuccino']['ingredients']['water']
        coffee_required = MENU['cappuccino']['ingredients']['coffee']
        milk_required = MENU['cappuccino']['ingredients']['milk']
        cost = MENU['cappuccino']['cost']
        make_coffee = True

    else:
        print("Please enter a correct command.")

    # Checks if resources are sufficient
    if make_coffee:
        sufficient_resources = True
        if water_required > water:
            print("Sorry, there is not enough water.")
            sufficient_resources = False

        elif coffee_required > coffee:
            print("Sorry, there is not enough coffee.")
            sufficient_resources = False

        elif milk_required > milk:
            print("Sorry, there is not enough milk.")
            sufficient_resources = False

        # Asks for money
        if sufficient_resources:
            print("Please insert coins.")

            quarters = int(input("How many quarters?"))
            dimes = int(input("How many dimes?"))
            nickels = int(input("How many nickels?"))
            pennies = int(input("How many pennies?"))

            money_received = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01

            # Checks if money is sufficient
            if money_received == cost:
                print(f"Here is your {command} ☕️. Enjoy!")
                sufficient_money = True
                money += cost

            elif money_received > cost:
                change = round(money_received - cost, 2)
                print(f"Here is ${change} in change.")
                print(f"Here is your {command} ☕️. Enjoy!")
                sufficient_money = True
                money += cost

                # Reduces resources accordingly
                if sufficient_money:
                    water -= water_required
                    coffee -= coffee_required
                    milk -= milk_required

            else:
                print("Not enough money. Money refunded.")
                sufficient_money = False
