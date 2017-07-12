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

primes = [x for x in range(1,1000001) if is_prime(x)]
largest_prime = primes[-1]
longest_range = 6
print(largest_prime)
print(sum(primes[0:550]))
for i in range(6,550):
    print(i)
    for j in range(0, len(primes) - i):
        window = sum(primes[j:j+i])
        if window in primes:
            longest_range = i
            print(i, primes[j:j+i])
print(longest_range)
#999983
