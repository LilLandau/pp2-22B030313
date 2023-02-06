import math

def is_prime(number):
    if number == 1: return False

    for i in range(2, number):
        if number % i == 0:
            return False
        
    return True

def filter_prime(numbers):
    primes = []
    for num in numbers:
            if is_prime(num):
                primes.append(num)

    return primes

x = [1, 10, 9, 7, 4, 3, 5, 124, 41]
y = filter_prime(x)

for i in y:
    print(i)
