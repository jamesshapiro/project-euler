#!/usr/bin/env python3 -tt

def is_palindrome(string):
    return string == string[::-1]

def is_double_base_palindrome(x):
    return is_palindrome(str(x)) and is_palindrome("{0:b}".format(x))

print(sum(x for x in range(1,1000000) if is_double_base_palindrome(x)))
