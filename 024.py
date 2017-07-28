#!/usr/bin/env python3 -tt

import itertools

digits = "0123456789"
permutations = list(itertools.permutations(digits))

print("".join(permutations[999999]))
