#!/usr/bin/env python3 -tt
import math

def has_odd_period(x):
    return get_period_of_sqrt(x) % 2 == 1

def get_whole_number_in_denom(num, denom_sqr, op):
    denom = (denom_sqr - op * op) // num
    num = (denom_sqr, -op)
    return (num, denom)

def get_next_num_denom(a_i, old_num, denom):
    new_num = (old_num[0], old_num[1] - a_i * denom)
    return (new_num, denom)

def get_period(num, denom_sqr, op, periods):
    num, denom = get_whole_number_in_denom(num, denom_sqr, op)
    a_i = math.floor((math.sqrt(num[0]) + num[1]) / denom)
    num, denom = get_next_num_denom(a_i, num, denom)
    if (a_i, num, denom) in periods:
        return len(periods)
    else:
        periods.append((a_i, num, denom))
    return get_period(denom, num[0], num[1], periods)

def get_period_of_sqrt(x):
    if round(math.sqrt(x)) * round(math.sqrt(x)) == x:
        return 0
    a_0 = math.floor(math.sqrt(x))
    num = 1
    denom_sqr = x
    minus_op = -a_0
    periods = []
    return get_period(num, denom_sqr, minus_op, periods)

print(len([i for i in range(10001) if has_odd_period(i)]))
