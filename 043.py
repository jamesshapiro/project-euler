#!/usr/bin/env python3 -tt

import itertools

digits = "0123456789"
primes = [2, 3, 5, 7, 11, 13, 17]

def has_divisibility_property(base10):
    return all(int(base10[idx+1:idx+4]) % prime == 0 for (idx, prime) in enumerate(primes))

perms = map(lambda x: "".join(x), itertools.permutations(digits))
print(sum([int(x) for x in perms if has_divisibility_property(x)]))



