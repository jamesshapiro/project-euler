#!/usr/bin/env python3 -tt

import itertools

ab_candidates = list(range(1,1001))
combos = itertools.combinations(ab_candidates, 2)
for combo in combos:
    a = combo[0]
    b = combo[1]
    if a + b > 999:
        continue
    c = 1000 - a - b
    if a**2 + b**2 == c**2:
        print(a * b * c)
        break
