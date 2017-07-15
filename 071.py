#!/usr/bin/env python3 -tt

import math

max_num = 1000001

def gcd(a, b):
    while b % a > 0:
        (a, b) = (b % a, a)
    return a

lower_bound = 3 / 7
lb_multiplier = 1/ lower_bound
closest_frac_tuple = (1, 7)
ub_multiplier = closest_frac_tuple[1] / closest_frac_tuple[0]
min_delta = 3/7

for num in range(2, max_num - 1):
    for denom in range(math.floor(lb_multiplier * num), min(max_num, math.ceil(ub_multiplier * num) + 1)):
        if gcd(num, denom) == 1:
            delta = 3/7 - num/denom
            if delta < min_delta and delta > 0:
                min_delta = delta
                closest_frac_tuple = (num, denom)
                ub_multiplier = denom / num

print(closest_frac_tuple[0])
