#!/usr/bin/env python3 -tt

def list_digits(x):
    return "".join(sorted(str(x)))

def x_has_same_digits_as_2x_to_6x(x):
    return len(set(list_digits(i*x) for i in range(1,7))) == 1

x = 1
while not x_has_same_digits_as_2x_to_6x(x):
    x += 1
print(x)



# Solution in four lines of code:
# ===============================
"""
x = 1
while not len(set("".join(sorted(str(i*x))) for i in range(1,7))) == 1:
    x += 1
print(x)
"""

