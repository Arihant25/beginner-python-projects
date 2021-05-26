def prime_checker(number):

    isPrime = True

    for i in range(2, number):

        if number % i != 0:
            isPrime = False

    if isPrime:
        print(f"{number} is a prime number.")

    else:
        print(f"{number} is a composite number.")


prime_checker(int(input("Enter a number: ")))
