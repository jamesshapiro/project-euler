#!/usr/bin/env python3 -tt

import itertools

def is_palindrome(num):
    return str(num) == str(num)[::-1]

max_product = 0
three_digit_nums = range(100,1000)

palindromes = (x*y for (x,y) in itertools.product(three_digit_nums, repeat=2)
               if is_palindrome(x*y))

print(max(palindromes))
