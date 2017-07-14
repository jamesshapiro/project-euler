#!/usr/bin/env python3 -tt

import math
import naive_prime_test as t

# Find the sum of all the primes below two million.
print(sum([x for x in range(2000000) if t.is_prime(x)]))
