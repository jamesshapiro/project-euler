#!/usr/bin/env python3 -tt

import math

def is_prime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

circular_primes = set()

def is_circular_prime(x):
    if x in circular_primes:
        return True
    cycle = []
    for i in range(len(x)):
        x = x[1:] + x[0]
        cycle.append(x)
    if all(is_prime(int(num)) for num in cycle):
        circular_primes.update(cycle)
        return True
    return False

for i in range(1,1000000):
    is_circular_prime(str(i))

print(len(circular_primes))
