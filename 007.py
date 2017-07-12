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

def generate_primes():
    n = 1
    while True:
        while not is_prime(n):
            n += 1
        yield n
        n += 1

p = generate_primes()
for _ in range(10000):
    next(p)
print(next(p))
