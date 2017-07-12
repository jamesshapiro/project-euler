#!/usr/bin/env python3 -tt

import math

def is_square(x):
    return math.sqrt(x) == int(math.sqrt(x))

def is_prime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    for i in range(2, math.ceil(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

primes = [2]
i = 1

while True:
    odd_num = 2*i + 1
    if is_prime(odd_num):
        primes.append(odd_num)
    else:
        sum_found = False
        for prime in primes:
            if is_square(int((odd_num - prime) * 0.5)):
                sum_found = True
                break
        if sum_found == False:
            break
    i += 1

print(2*i + 1)
