num = int(input("Enter a number: "))
is_prime = True

for i in range(2, int(num ** 1 / 2) + 1):
    if num % i == 0:
        is_prime =  False
        break

if is_prime:
    print("Prime.")
else:
    print("Not prime.")
