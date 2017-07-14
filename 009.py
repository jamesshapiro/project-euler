#!/usr/bin/env python3 -tt

import itertools

def find_a_pythagorean_triplet_with_perimeter(n):
    leg_lengths = list(range(1, n+1))
    combos = itertools.combinations_with_replacement(leg_lengths, 2)
    for combo in combos:
        leg_1 = combo[0]
        leg_2 = combo[1]
        if leg_1 + leg_2 > n - 1:
            continue
        hypotenuse = 1000 - leg_1 - leg_2
        if leg_1**2 + leg_2**2 == hypotenuse**2:
            return leg_1 * leg_2 * hypotenuse

print(find_a_pythagorean_triplet_with_perimeter(1000))
