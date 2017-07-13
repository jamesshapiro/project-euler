#!/usr/bin/env python3 -tt

import math

"""
Note: This solution is inefficient, but it does get the job
done in just under a minute. I may work on trying to improve
it further
"""

def is_prime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

primes = [x for x in range(1,1000001) if is_prime(x)]
largest_prime = primes[-1]
longest_range = 21
longest_range_prime = 953

for prime in primes:
    next_window = False
    for i in range(longest_range+2, 550, 2):
        for j in range(0, len(primes) - i):
            window = sum(primes[j:j+i])
            if window > prime:
                break
            elif window == prime:
                longest_range = i
                longest_range_prime = prime

print(longest_range_prime)

