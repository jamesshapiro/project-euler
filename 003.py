#!/usr/bin/env python3 -tt

def largest_divisor(x):
    divisor = 2
    while num > 1:
        if num % divisor == 0:
            num /= divisor
        else:
            divisor += 1
    return divisor

num = 600851475143

print(largest_divisor(num))
