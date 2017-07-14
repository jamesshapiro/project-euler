#!/usr/bin/env python3 -tt

import math
import naive_prime_test as t

def generate_primes():
    n = 1
    while True:
        while not t.is_prime(n):
            n += 1
        yield n
        n += 1

def get_nth_prime(n):
    get_prime = generate_primes()
    for _ in range(n):
        next(get_prime)
    return next(get_prime)

print(get_nth_prime(10000))
