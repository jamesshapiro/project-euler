#!/usr/bin/env python3 -tt

import math

digits = "123456789"

def is_pandigital(string):
    return "".join(sorted(string)) == digits

def is_pandigital_product(x):
    for i in range(1, math.ceil(math.sqrt(x)) + 1):
        if x % i == 0:
            equation_as_string = str(i) + str(x//i) + str(x)
            if is_pandigital(equation_as_string):
                return True
    return False

print(sum(x for x in range(10000) if is_pandigital_product(x)))
