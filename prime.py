def is_prime(num):
    prime = False
    factors = 0
    if num > 1:
        for i in range(2, round(num)):
            if num % i == 0:
                factors += 1
        if factors < 1:
            prime = True

    return prime
