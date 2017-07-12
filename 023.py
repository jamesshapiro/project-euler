#!/usr/bin/env python3 -tt

def is_abundant_sum(x):
    for i in range(1, (x+1) // 2 + 1):
        if i in abundant_numbers and x - i in abundant_numbers:
            return True
    return False

def is_abundant(x):
    return sum(proper_divisors(x)) > x

def proper_divisors(x):
    divs = []
    for i in range(1, ((x+1) // 2) + 1):
        if x % i == 0:
            divs.append(i)
    return divs

abundant_numbers = {x for x in range(28124) if is_abundant(x)}
print(sum(x for x in range(28124) if not is_abundant_sum(x)))
