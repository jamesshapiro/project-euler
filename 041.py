#!/usr/bin/env python3 -tt

import math
import itertools
import naive_prime_test as t

digits = "123456789"

pandigital_primes = []
prefixes = [digits[:i+1] for i in range(len(digits))]
pandigital_subsets = [itertools.permutations(subset) for subset in prefixes]
for subset in pandigital_subsets:
    numbers = map(lambda x: int("".join(x)), subset)
    pandigital_primes.extend(filter(t.is_prime, numbers))

print(max(pandigital_primes))

