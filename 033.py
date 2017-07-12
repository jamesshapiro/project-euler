#!/usr/bin/env python3 -tt

import itertools
import functools

def gcd(a, b):
    while b % a > 0:
        (a, b) = (b % a, a)
    return a

def is_digit_cancelling(num, denom):
    for digit in num:
        if digit not in denom:
            continue
        num1 = num.replace(digit,"")
        denom1 = denom.replace(digit,"")
        if float(num) / float(denom) == float(num1) / float(denom1):
            return True
    return False

nums = list(range(12, 100))
unique_digits = list(filter(lambda x: x % 10 > 0 and x % 11 > 0, nums))
unique_digits = list(map(str, unique_digits))

nums = []
denoms = []

for i in range(len(unique_digits)-1):
    for j in range(i+1,len(unique_digits)):
        if is_digit_cancelling(unique_digits[i], unique_digits[j]):
            nums.append(int(unique_digits[i]))
            denoms.append(int(unique_digits[j]))

big_num = functools.reduce((lambda x, y: x * y), nums)
big_denom = functools.reduce((lambda x, y: x * y), denoms)
print(big_denom // gcd(big_num, big_denom))
