print("""
 _____________________
|  _________________  |
| | Arihant      0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
      )


def add(n1, n2):
    """Adds the 2 given numbers"""
    return n1 + n2


def subtract(n1, n2):
    """Subtracts the 2 given numbers"""
    return n1 - n2


def multiply(n1, n2):
    """Multiplies the 2 given numbers"""
    return n1 * n2


def divide(n1, n2):
    """Divides the 2 given numbers"""
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}

num1 = float(input("Enter the first number: "))

should_continue = 'y'

while should_continue == 'y':

    for symbol in operations:
        print(symbol)

    operation_symbol = input("Pick an operation from the above: ")

    num2 = float(input("Enter the second number: "))

    calculation_function = operations[operation_symbol]

    first_answer = calculation_function(num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {first_answer}")

    should_continue = input(
        f"\nType 'y' to continue calculating with {first_answer}, or type 'n' to exit: ").lower()

    num1 = first_answer

print("\nThank you for using my calculator!\n")
