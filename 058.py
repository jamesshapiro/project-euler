#!/usr/bin/env python3 -tt

import math
import naive_prime_test as t

first_five = [1, 3, 5, 7, 9]
last_prime = first_five[-1]
total_primes = len(list(filter(t.is_prime, first_five)))
total_diags = len([1,3,5,7,9])
i = 2
while total_primes / total_diags > 0.10:
    i += 2
    for _ in range(4):
        last_prime += i
        if t.is_prime(last_prime):
            total_primes += 1
    total_diags += 4
print(i+1)
