from math import sqrt

num = int(input("Enter a number: "))

for i in range(2, int(sqrt(num)) + 1):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")