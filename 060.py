#!/usr/bin/env python3 -tt

import naive_prime_test as t
import prime_generator as pg
import collections

prime_sets = collections.defaultdict(lambda: list())
get_prime = pg.generate_primes()

primes = set()

def is_prime(x):
    if x in primes:
        return True
    elif t.is_prime(x):
        return True
    return False

def is_concatenable(y, x):
    return is_prime(int(str(y) + str(x))) and is_prime(int(str(x) + str(y)))

def is_pairwise_concatenable(set_of_length_n, prime):
    return all(is_concatenable(prime, prime2) for prime2 in set_of_length_n)

size = 5
while len(prime_sets[size]) == 0:
    next_prime = next(get_prime)
    primes.add(next_prime)
    compatible_set = {x for x in primes if is_concatenable(x, next_prime)}
    compatible_set.add(next_prime)
    for n in range(1, size):
        for set_of_length_n in prime_sets[n]:
            if set_of_length_n <= compatible_set and next_prime not in set_of_length_n:
                new_set = set_of_length_n.union([next_prime])
                prime_sets[n+1].append(new_set)
    prime_sets[1].append(set([next_prime]))

smallest_set = prime_sets[size].pop()
print(sum(smallest_set))
