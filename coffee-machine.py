money = 550
water = 400
milk = 540
beans = 120
cups = 9

def status():
    print("The coffee machine has:")
    print(water, "of water")
    print(milk, "of milk")
    print(beans, "of coffee beans")
    print(cups, "of disposable cups")
    print(money, "of money")

def buy():
    global money, water, milk, beans, cups
    order = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    
    if order == "back":
        return 0
    elif int(order) == 1 and water >= 250 and beans >= 15 and cups > 0:
        money += 4
        water -= 250
        beans -= 16
        cups -= 1
    elif int(order) == 2 and water >= 350 and beans >= 25 and milk >= 75 and cups > 0:
        money += 7
        water -= 350
        beans -= 20
        milk -= 75
        cups -= 1
    elif int(order) == 3 and water >= 200 and beans >= 12 and milk >= 100 and cups > 0:
        money += 6
        water -= 200
        beans -= 12
        milk -= 100
        cups -= 1
    else:
        print("Sorry, not enough resources!")

def fill():
    global water, milk, beans, cups
    more_water = int(input("Write how many ml of water do you want to add:"))
    more_milk = int(input("Write how many ml of milk do you want to add:"))
    more_beans = int(input("Write how many grams of coffee beans do you want to add:"))
    more_cups = int(input("Write how many disposable cups of coffee do you want:"))
    milk += more_milk
    water += more_water
    beans += more_beans
    cups += more_cups

def take():
    global money
    print("I gave you $" + str(money))
    money = 0

while True:
    mode = input("Write action (buy, fill, take):")
    if mode == "buy":
        buy()
    elif mode == "fill":
        fill()
    elif mode == "take":
        take()
    elif mode == "remaining":
        status()
    elif mode == "exit":
        break
