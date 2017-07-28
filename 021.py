#!/usr/bin/env python3 -tt

import math

def proper_divisors(x):
    divs = []
    for i in range(1, ((x+1) // 2) + 1):
        if x % i == 0:
            divs.append(i)
    return divs

def d(n):
    return sum(proper_divisors(n))

def is_amicable_number(n):
    return n == d(d(n)) and n != d(n)

print(sum(x for x in range(1,10000) if is_amicable_number(x)))
