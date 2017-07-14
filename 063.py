#!/usr/bin/env python3 -tt

total = 0
for base in range(1,10):
    power = 1
    while len(str(base**power)) == power:
        total += 1
        power += 1

print(total)
