#!/usr/bin/env python3 -tt

sum_of_squares = sum([x*x for x in range(101)])
square_of_sum = sum(range(101))**2
print(square_of_sum - sum_of_squares)

