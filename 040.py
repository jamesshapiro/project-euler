#!/usr/bin/env python3 -tt

import functools
powers_of_ten = [10**x for x in range(7)]

def generate_champernowne_digit():
    i = 1
    while True:
        for digit in str(i):
            yield digit
        i += 1

g = generate_champernowne_digit()

digits = [int(next(g)) for i in range(10**7+1)]
powers_of_ten_digits = [digits[x - 1] for x in powers_of_ten]

print(functools.reduce((lambda x, y: x * y), powers_of_ten_digits))
