#!/usr/bin/env python3 -tt

num = 600851475143
divisor = 2

while num > 1:
    if num % divisor == 0:
        num /= divisor
    else:
        divisor += 1

print(divisor)
