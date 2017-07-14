#!/usr/bin/env python3 -tt

import math

primes = []

def is_prime(x):
    for prime in primes:
        if prime > math.ceil(math.sqrt(x)):
            break
        if x % prime == 0:
            return False
    return True

def generate_primes():
    i = 2
    while True:
        yield i
        primes.append(i)
        while True:
            i += 1
            if i % 2 == 1 and is_prime(i):
                break

