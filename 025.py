#!/usr/bin/env python3 -tt

x, y = 1, 1
index = 2
while len(str(y)) < 1000:
    x, y = y, x+y
    index += 1

print(index)
