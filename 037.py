#!/usr/bin/env python3 -tt

import math
import naive_prime_test as t

last_digit = [3, 7]
extender_digits = [1, 2, 3, 5, 7, 9]
first_digit = {2, 3, 5, 7}

def is_left_truncatably_prime(x):
    return all(t.is_prime(int(x[:len(x)-i])) for i in range(len(x)))

def is_right_truncatably_prime(x):
    return all(t.is_prime(int(x[i:])) for i in range(len(x)))

def is_truncatable_prime(x):
    return is_left_truncatably_prime(x) and is_right_truncatably_prime(x)

truncatable_primes = []

def left_extend(prefix, curr):
    num = int(prefix + curr)
    if not t.is_prime(num):
        return
    if is_truncatable_prime(str(num)):
        truncatable_primes.append(num)
    for digit in extender_digits:
        left_extend(str(digit), prefix + curr)

for digit in last_digit:
    for extender in extender_digits:
        left_extend(str(extender), str(digit))

print(sum(truncatable_primes))
