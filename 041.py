#!/usr/bin/env python3 -tt

import math
import itertools

digits = "123456789"

def is_prime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

pandigital_primes = []
subsets = [digits[:i+1] for i in range(len(digits))]
pandigital_subsets = [itertools.permutations(subset,len(subset)) for subset in subsets]
for subset in pandigital_subsets:
    numbers = map(lambda x: int("".join(x)), subset)
    pandigital_primes.extend(filter(is_prime, numbers))

print(max(pandigital_primes))

