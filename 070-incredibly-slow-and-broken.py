#!/usr/bin/env python3 -tt

import naive_prime_test as t
import numpy as np

def list_digits(x):
    return "".join(sorted(str(x)))

def have_same_digits(x, y):
    return list_digits(x) == list_digits(y) and len(str(x)) == len(str(y))

primes = [x for x in range(1,10000000//3 + 1) if t.is_prime(x)]

def prime_divisors(n):
    results = []
    n_copy = n
    for prime in primes:
        if n % prime == 0:
            results.append(prime)
            n_copy = n_copy // prime
        if n_copy < prime:
            break
    return results

euler_totients = []

def euler_totient(n):
    totient = n
    for prime in prime_divisors(n):
        totient = totient // prime
        totient *= prime - 1
    if totient == n:
        totient = n - 1
    euler_totients.append((n, totient))
    return (n, totient)

for i in range(2,10000000):
    print(i)
    euler_totient(i)
    (x,y) = euler_totients[i-2]

for et in range(len(euler_totients)):
    (x,y) = euler_totients[et]
    if have_same_digits(x, y):
        print(x, y)
    
same_digs = [(x / y, x, y) for (x,y) in euler_totients if have_same_digits(x, y)]

same_digs_sorted = sorted(same_digs, key=lambda trip: trip[0])

print(same_digs_sorted[0])

#for i in range(100):
#    print(i, same_digs_sorted[i])

