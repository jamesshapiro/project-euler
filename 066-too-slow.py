#!/usr/bin/env python3 -tt

import math

square_of = {x: x**2 for x in range(1,1000000)}
squares = {x**2 for x in range(1, 1000000)}
print("done")

def is_square(x):
    return x in squares

def get_minimal_diophantine(D):
    if is_square(D):
        return (0,0)
    x = 1
    while True:
        for y in range(1,x+1):
            if square_of[x] - (D * square_of[y]) == 1:
                return (x, y)
        x += 1

for i in range(2, 1001):
    print(get_minimal_diophantine(i))
