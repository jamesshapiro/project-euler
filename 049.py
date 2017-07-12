#!/usr/bin/env python3 -tt

import math
import collections

primes = []
prime_perms = collections.defaultdict(lambda: list())

def is_prime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

for i in range(1000, 10000):
    if is_prime(i):
        prime_perms["".join(sorted(str(i)))].append(i)

for key in prime_perms:
    if len(prime_perms[key]) >= 3:
        srted = sorted(prime_perms[key])
        distances = []
        isFirst = True
        for i in range(len(srted) - 1):
            for j in range(i+1, len(srted)):
                distance = srted[j] - srted[i]
                if distance in distances and isFirst and distance == 3330:
                    print(prime_perms[key])
                    isFirst = False
                    break
                else:
                    distances.append(srted[j] - srted[i])
