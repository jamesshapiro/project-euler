#!/usr/bin/env python3 -tt

import math

string = "123456789"

def is_pandigital(x):
    for i in range(1, math.ceil(math.sqrt(x)) + 1):
        if x % i == 0:
            if "".join(sorted(str(x//i) + str(i) + str(x))) == string:
                return True
    return False

print(sum(x for x in range(10000) if is_pandigital(x)))
