exitChoice = "0"

while exitChoice != "exit" :
    table = int(input("Please enter a times table: "))
    for x in range(0, 11):
        print(x, "x", table, "=", x*table)
    exitChoice = input("Type exit if you want to stop, or press enter if you want to continue")
