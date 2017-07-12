#!/usr/bin/env python3 -tt

import math

primes = [2]

i = 3
four_factors = 0

while four_factors < 4:
    i_copy = i
    i_primes = []
    for prime in primes:
        if prime > i // 2:
            break
        if i_copy % prime == 0:
            while i_copy % prime == 0:
                i_copy = i_copy // prime
            i_primes.append(prime)
        if i_copy == 1:
            break
    if len(i_primes) == 0:
        i_primes.append(i)
        primes.append(i)
    if len(i_primes) == 4:
        four_factors += 1
    else:
        four_factors = 0
    i += 1

print(i - 4)

