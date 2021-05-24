# This program checks if a given year is a leap year or not

year = int(input("Which year do you want to check?\n"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            leap = True
        else:
            leap = False
    else:
        leap = True
else:
    leap = False

if leap:
    print(f"{year} is a leap year!")
else:
    print(f"{year} is not a leap year!")
