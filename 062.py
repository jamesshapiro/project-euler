#!/usr/bin/env python3 -tt

import itertools
import math
import collections

cube_bank = collections.defaultdict(lambda: list())

def num_digits(x):
    return len(str(x))

def is_cube(x):
    cube_root = math.pow(x, 1./3)
    return round(cube_root)**3 == x

candidates = []
i = 1
num_digits = 1000000
while not len(str(i**3)) > num_digits:
    print(i)
    cube = i**3
    cube_bank["".join(sorted(str(cube)))].append(cube)
    if len(cube_bank["".join(sorted(str(cube)))]) == 5:
        candidates.append("".join(sorted(str(cube))))
        num_digits = len(str(cube))
    i += 1

min_candidates = []
for candidate in candidates:
    if len(cube_bank[candidate]) == 5:
        min_candidates.append(min(cube_bank[candidate]))

if len(min_candidates) > 0:
    print(min(min_candidates))

