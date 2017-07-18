#!/usr/bin/env python3 -tt
import math

def get_whole_number_in_denom(num, denom_sqr, op):
    denom = (denom_sqr*denom_sqr - op * op) / num
    num = (denom_sqr, -op)
    return (num, denom)

def get_next_num_denom(a_i, old_num, denom):
    new_num = (old_num[0], old_num[1] - a_i * denom)
    return (new_num, denom)

def get_period(num, denom_sqr, op, periods, iterations):
    num, denom = get_whole_number_in_denom(num, denom_sqr, op)
    a_i = math.floor((math.sqrt(num[0]) + num[1]) / denom)
    num, denom = get_next_num_denom(a_i, num, denom)
    if len(periods) == iterations:
        return periods
    else:
        periods.append(a_i)
    return get_period(denom, num[0], num[1], periods, iterations)

def get_period_of_e(iterations):
    a_0 = math.floor(math.e)
    num = 1
    denom_sqr = math.e
    minus_op = -a_0
    periods = []
    return get_period(num, denom_sqr, minus_op, periods, iterations)

iterations = 100
print(get_period_of_e(iterations))
