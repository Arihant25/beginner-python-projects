TICKET_PRICE = 10
SERVICE_CHARGE = 2
tickets_remaining = 100

def calculate_price(number_of_tickets):
    return number_of_tickets * TICKET_PRICE + SERVICE_CHARGE

while tickets_remaining >= 1:
    print("There are {} tickets remaining.".format(tickets_remaining))
    name = input("What is your name?    ")
    try:
        num_tickets = int(input("How many tickets would you like, {}    ".format(name)))
        if num_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print("Oh no, we ran into an issue. {}. Please try again".format(err))
    else:
        amount_due = calculate_price(num_tickets)
        print("The total due is ${}".format(amount_due))
        should_proceed = input("Do you want to proceed? Type Y/N.    ")
        if should_proceed.lower() == "y":
            print("SOLD")
            tickets_remaining -= num_tickets
        else:
            print("Thank you anyways, {}!".format(name))
print("Sorry, all tickets are sold out!!!")
