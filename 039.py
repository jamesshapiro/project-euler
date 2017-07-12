#!/usr/bin/env python3 -tt

import math
import itertools
import numpy as np

def is_solution(leg_1, leg_2, hypotenuse):
    return leg_1**2 + leg_2**2 == hypotenuse**2

num_solutions = [0, 0]

for perimeter in range(3, 1001):
    solutions = set()
    for hypotenuse in range(math.ceil(perimeter // 3), perimeter-1):
        for leg_1 in range((perimeter - hypotenuse) // 2, min(hypotenuse, perimeter - hypotenuse)):
            leg_2 = perimeter - hypotenuse - leg_1
            if leg_2 > leg_1:
                continue
            if is_solution(leg_1, leg_2, hypotenuse):
                solutions.add((leg_1, leg_2, hypotenuse))
    num_solutions.append(len(solutions))
    
arr = np.array(num_solutions)
print(np.argmax(arr) + 1)
