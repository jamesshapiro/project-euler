#!/usr/bin/env python3 -tt

# This wasn't really a programming problem so much as
# a pure math problem.
#
# 2520 is the smallest number divisible by n=1...10.
# Hence, any number divisble by n=1...20 must also
# be divisible by 2520. (TODO: provide a formal proof
# of this)
#
# The only new prime factors introduced by 11...20 are
# the primes [11, 13, 17, 19] and the fourth 2 introduced
# by n = 16 = 2^4.
i = 2520
new_prime_factors = [2, 11, 13, 17, 19]
for factor in new_prime_factors:
    i *= factor

divisors = list(range(1,21))
if all([(i % x == 0) for x in divisors]):
    print(i)
