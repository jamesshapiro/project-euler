#!/usr/bin/env python3 -tt

import numpy as np

collatz_lengths = {}

def get_collatz_length(n_argument):
    num_steps = 1
    n = n_argument
    while (n != 1):
        if n in collatz_lengths:
            num_steps = num_steps + collatz_lengths[n]
            break
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3*n + 1
        num_steps = num_steps + 1
    collatz_lengths[n_argument] = num_steps
    return num_steps

def get_max_chain(n):
    collatz_chains = np.array(list(get_collatz_length(x) for x in range(1,n)))
    return np.argmax(collatz_chains) + 1

print(get_max_chain(1000000))

