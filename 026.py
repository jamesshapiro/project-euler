#!/usr/bin/env python3 -tt

import numpy as np

"""
This algorithm simulates the process of "long division"
that you would perform on a piece of paper, e.g. if you
were in grade school.

It terminates when either

(1.) We encounter a number that we have already divided 
by the divisor

(2.) The divisor cleanly divides the number

In case 1, we have a recurring cycle and we return the
length of the cycle which we have been keeping track of,
in case 2, we don't have a cycle (unless 000... counts)
"""

def recurring_cycle_length(x):
    num = 1
    fracs = {}
    i = 0
    while num < x:
        num *= 10
    fracs[num] = i
    while num % x > 0:
        num = num % x
        while num < x:
            num *= 10
            i += 1
        if num in fracs:
            break
        fracs[num] = i
    if num % x == 0:
        return 0
    return i - fracs[num]

cycle_lengths = list(recurring_cycle_length(x) for x in range(1, 1001))
cycle_lengths = np.array(cycle_lengths)
print(np.argmax(counts) + 1)

