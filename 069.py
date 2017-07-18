#!/usr/bin/env python3 -tt

import naive_prime_test as t
import numpy as np

primes = [x for x in range(1,1002) if t.is_prime(x)]

def prime_divisors(n):
    return [prime for prime in primes if n % prime == 0]

def euler_totient(n):
    print(n)
    totient = n
    for prime in prime_divisors(n):
        totient = totient // prime
        totient *= prime - 1
    return totient

print(np.argmax(np.array([n / euler_totient(n) for n in range(1, 1000000)])) + 1)
