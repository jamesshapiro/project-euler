#!/usr/bin/env python3 -tt

def iterate(x):
    my_x = x
    while True:
        x = x + int(str(x)[::-1])
        yield x

def is_palindromic(x):
    return str(x) == str(x)[::-1]

def is_pseudo_lychrel(x):
    """
    g = iterate(x)
    print([next(g) for _ in range(50)])
    g = iterate(x)
    print([is_palindromic(next(g)) for _ in range(50)])
    """
    g = iterate(x)
    return all(not is_palindromic(next(g)) for _ in range(50))

print(len([x for x in range(10000) if is_pseudo_lychrel(x)]))
