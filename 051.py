#!/usr/bin/env python3 -tt

import math
import itertools
import collections

"""
runs in 15 seconds on my laptop
"""

primes = [2,3,5,7]

def is_prime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def get_n_digit_primes(n):
    return [i for i in range(10 ** (n - 1), 10**n) if is_prime(i)]

def all_same_slot(x, indices):
    digits = [int(str(x)[i]) for i in indices]
    return max(digits) == min(digits)

def remove_indices(x, indices):
    digits = [str(x)[i] for i in range(len(str(x))) if i not in indices]
    return int("".join(digits))

def run():
    n = 1
    while True:
        n_digit_primes = get_n_digit_primes(n)
        for num_slots in range(1,n):
            combos = itertools.combinations(range(n),num_slots)
            for combo in combos:
                same_digit_in_indices = [x for x in n_digit_primes if all_same_slot(x, combo)]
                count_map = collections.defaultdict(lambda: list())
                for num in same_digit_in_indices:
                    count_map[remove_indices(num, combo)].append(num)
                for key in count_map:
                    if len(count_map[key]) == 8:
                        return min(count_map[key])
        n += 1

print(run())
