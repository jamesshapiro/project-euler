#!/usr/bin/env python3 -tt

import math

def proper_divisors(x):
    divs = []
    for i in range(1, ((x+1) // 2) + 1):
        if x % i == 0:
            divs.append(i)
    return divs

def dn(x):
    return sum(proper_divisors(x))

def is_amicable_number(x):
    return x == dn(dn(x)) and dn(x) != x

print(is_amicable_number(284))
print(is_amicable_number(220))
      
print(sum(x for x in range(1,10000) if is_amicable_number(x)))
