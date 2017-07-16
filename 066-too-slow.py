#!/usr/bin/env python3 -tt

import math

def is_square(x):
    return round(math.sqrt(x)) * round(math.sqrt(x)) == x

def get_minimal_diophantine(D):
    if is_square(D):
        return (0,0)
    x = 1
    while True:
        for y in range(1,x+1):
            if x**2 - (D * y**2) == 1:
                return (x, y)
        x += 1

for i in range(2, 1001):
    print(get_minimal_diophantine(i))
