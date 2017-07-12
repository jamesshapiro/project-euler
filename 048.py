#!/usr/bin/env python3 -tt

last_ten_digits = 0
for i in range(1,1001):
    j = 1
    for _ in range(i):
        j *= i
        j = j % 10000000000
    last_ten_digits += j
print(last_ten_digits % 10000000000)
