#!/usr/bin/env python3 -tt

# this bound is the first n such that n*(n+1) // 2 > 9999
upper_bound = 142

def is_four_digits(x):
    return 999 < x and x < 10000

def digits_overlap(xxoo, ooyy):
    # returns true if the 'oo' digits match. E.g. 55[67] matches [67]89
    #                                                ^^           ^^
    return str(xxoo)[2:] == str(ooyy)[:2]

formulas = [lambda n: n*(n+1) // 2, lambda n: n*n, lambda n: n*(3*n-1) // 2,
            lambda n: n*(2*n-1), lambda n: n*(5*n-3) // 2, lambda n: n*(3*n-2)]

number_lists = [[f(n) for n in range(1, upper_bound)] for f in formulas]
number_lists = [list(filter(is_four_digits, numbers)) for numbers in number_lists]
list_indices = set(range(len(number_lists)-1))

def find_cycle(curr, path, visited):
    for i in list_indices.difference(visited):
        overlapping = [next for next in number_lists[i] if digits_overlap(curr, next)]
        for next in overlapping:
            if next in path:
                continue
            if len(path) == len(number_lists) - 1:
                first = path[0]
                last = next
                if digits_overlap(last, first):
                    print(sum(path + [next]))
            else:
                find_cycle(next, path + [next], visited.union({i}))

for i in range(len(number_lists[-1])):
    start = number_lists[-1][i]
    find_cycle(start, [start], set())

