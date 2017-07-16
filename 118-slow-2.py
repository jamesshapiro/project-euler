#!/usr/bin/env python3 -tt

import itertools
import naive_prime_test as t
import time

start_time = time.time()

digits = "123456789"
unique = set()
unique_non_prime = set()

primes = []
nonprimes = []

def is_prime(x):
    if x in primes:
        return True
    elif x in nonprimes:
        return False
    elif t.is_prime(x):
        primes.append(x)
        return True
    else:
        nonprimes.append(x)
        return False

def add_all_pandigital_prime_sets(permutation):
    perm_partitions = get_all_partitions(permutation, 0)
    for partition in perm_partitions:
        candidate = frozenset(sorted(partition))
        if candidate in unique_non_prime or candidate in unique:
            continue
        if all(t.is_prime(int(x)) for x in partition):
            unique.add(candidate)
        else:
            unique_non_prime.add(candidate)



def get_all_partitions(string, start_index):
    all_partitions = []
    for i in range(start_index + 1, len(string) + 1):
        i_partitions = []
        first_subpartition = string[start_index:i]
        i_partitions.append(first_subpartition)
        if i == len(string):
            all_partitions.append(i_partitions)
            return all_partitions
        for group_of_partitions in get_all_partitions(string, i):
            i_partitions.extend(group_of_partitions)
            all_partitions.append(i_partitions)
            i_partitions = i_partitions[:1]
    return all_partitions

i = 0
for perm in itertools.permutations(digits, len(digits)):
    if i % 100000 == 0:
        print(i)
    add_all_pandigital_prime_sets("".join(perm))
    i += 1

print(len(unique))

print("--- %s seconds ---" % (time.time() - start_time))
