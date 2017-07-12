#!/usr/bin/env python3 -tt

fifth_powers = {x: x**5 for x in range(10)}

def is_digit_fifth(x):
    return int(x) == sum(fifth_powers[int(i)] for i in x) and int(x) > 1

print(sum(i for i in range(1000000) if is_digit_fifth(str(i))))
        
