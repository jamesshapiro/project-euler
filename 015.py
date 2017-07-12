#!/usr/bin/env python3 -tt
import itertools

import math

def n_choose_k(n, k):
    f = math.factorial
    return f(n) / (f(k) * f(n-k))

print(int(n_choose_k(40, 20)))

