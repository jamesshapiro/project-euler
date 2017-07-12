#!/usr/bin/env python3 -tt

import numpy as np

def count_repeating(x):
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

counts = np.array(list(count_repeating(x) for x in range(1, 1001)))
print(np.argmax(counts) + 1)

