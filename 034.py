#!/usr/bin/env python3 -tt

import math

def is_digit_factorial(x):
    return int(x) == sum(math.factorial(int(digit)) for digit in x)

print(sum(x for x in range(3,1000000) if is_digit_factorial(str(x))))
