#!/usr/bin/env python3 -tt

import math

def num_divisors(x):
    total = 0
    for i in range(1, ((x+1) // 2) + 1):
        if x % i == 0:
            total += 1
    total += 1
    return total

def tau(x):
    total = 1
    curr = 1
    i = 2
    while x > 1:
        while x % i == 0:
            curr += 1
            x /= i
        total *= curr
        curr = 1
        i += 1
    return total

def generate_triangles():
    n = 1
    t = 1
    while True:
        yield t
        n += 1
        t += n

g = generate_triangles()
triangle = next(g)
num_div = tau(triangle)
while num_div < 501:
    triangle = next(g)
    num_div = tau(triangle)
print(triangle)
