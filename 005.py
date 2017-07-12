#!/usr/bin/env python3 -tt

i = 2520 * 2 * 11 * 13 * 17 * 19
divisors = list(range(1,21))
while True:
    remainders = [(i % x == 0) for x in divisors]
    if not all(remainders):
        i = i + 1
    else:
        print(i)
        break
