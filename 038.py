#!/usr/bin/env python3 -tt

digits = "123456789"

def is_pandigital(x):
    return "".join(sorted(x)) == digits

"""                  "192" "384" "576"
                  192*1   192*2   192*3
"""
largest_pandigital = 192384576

for i in range(1, 500000):
    digit_str = ""
    j = 1
    while(len(digit_str) < 9):
        digit_str += str(i * j)
        j += 1
    if is_pandigital(digit_str):
        largest_pandigital = max(largest_pandigital, int(digit_str))

print(largest_pandigital)
