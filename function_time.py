from time import time


def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time()
        function()
        end_time = time()
        return end_time - start_time
    return wrapper_function


@speed_calc_decorator
def first_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def second_function():
    for i in range(10000001):
        i * i


first_time = first_function()
second_time = second_function()

print("First function took:", first_time, "seconds")
print("Second function took:", second_time, "seconds")

if first_time < second_time:
    print("First function is faster")
elif first_time > second_time:
    print("Second function is faster")
else:
    print("Both functions took the same amount of time!")
