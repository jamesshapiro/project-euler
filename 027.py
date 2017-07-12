#!/usr/bin/env python3 -tt

import math
import itertools

def get_run(a, b):
    i = 0
    while is_prime(i**2 + a*i + b):
        i += 1
    return i

def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

max_pair = ()
max_run = 0
pairs = itertools.combinations_with_replacement(range(-1000,1001), 2)
for pair in pairs:
    a = pair[0]
    b = pair[1]
    run = get_run(a, b)
    if run > max_run:
        max_run = run
        max_pair = (a, b)

print(max_pair[0] * max_pair[1])
