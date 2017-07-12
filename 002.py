#!/usr/bin/env python3 -tt

def fibn(n):
    num1 = 0
    num2 = 1
    while num2 < n:
        yield num2
        num1, num2 = num2, num1 + num2

even_terms = [x for x in fibn(4000000) if x % 2 == 0]
print(sum(even_terms))
