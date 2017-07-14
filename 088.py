#!/usr/bin/env python3 -tt

# The exotic https://en.wikipedia.org/wiki/Twelvefold_way#case_sx
# This came up once in a combinatorics class I once took!

import naive_prime_test as t

def is_product_sum_number(n):
    return 1

primes = []

def get_prime_factorization_of_(n):
    prime_factors = []
    if t.is_prime(n):
        primes.append(n)
        prime_factors.append(n)
        return prime_factors
    n_copy = n
    for prime in primes:
        while n_copy % prime == 0:
            prime_factors.append(prime)
            n_copy //= prime
        if n_copy == 1:
            return prime_factors

all_prime_factors = [get_prime_factorization_of_(n) for n in range(2,12001)]

for (idx, list_of_prime_factors) in enumerate(all_prime_factors):
    if sum(list_of_prime_factors) == idx + 1:
        print(idx + 1, list_of_prime_factors)

print(all_prime_factors[-1])


"""
Hilariously naive approach: build up all possible non-empty 
additive subsets, then for each integer, see if any of its 
subsets has a product equal to the integer.

sx_array = [ [ ],
             [ ],
             [(1,1)],
             [(1,1,1), (1, 2)]
]

def fill_next_entry():
    n = len(sx_array)
    n_minus_one = sx_array[-1]
    new_set_of_sets = set()
    for partition in n_minus_one:
        for index in range(len(partition)):
            new_entry = list(partition)
            new_entry[index] += 1
            new_set_of_sets.add(tuple(sorted(new_entry)))
    new_set_of_sets.add(tuple([1 for x in range(n)]))
    sx_array.append(new_set_of_sets)
    return len(new_set_of_sets)
#    print(new_set_of_sets)

for i in range(12001):
    print(i, fill_next_entry())
"""
