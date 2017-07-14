#!/usr/bin/env python3 -tt

def num_digits(x):
    return len(str(x))

def non_one_part():
    num = 1
    denom = 2
    while True:
        yield (num, denom)
        num, denom = denom, (2 * denom) + num

g = non_one_part()
i = 0

num_is_longer = []
for _ in range(1000):
    frac_part = next(g)
    num, denom = sum(frac_part), frac_part[1]
    if num_digits(num) > num_digits(denom):
        num_is_longer.append((num, denom))

print(len(num_is_longer))


