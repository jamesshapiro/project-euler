#!/usr/bin/env python3 -tt

# The exotic https://en.wikipedia.org/wiki/Twelvefold_way#case_sx
# This came up once in a combinatorics class I once took!

import naive_prime_test as t

upper_bound = 13001

def is_ps_number_for_k(k, n):
    factorizations = factorization_book[n]
    for factorization in factorizations:
        if len(factorization) == 1:
            continue
        if len(factorization) <= k and n - sum(factorization) == k - len(factorization):
            return True
    return False

def minimal_ps_number_for_k(k):
    n = k
    while not is_ps_number_for_k(k, n):
        n += 1
    return n

factorization_book = {}

primes = []

def get_prime_factorization_of_(n):
    prime_factors = []
    if t.is_prime(n):
        primes.append(n)
        prime_factors.append(n)
        return prime_factors
    n_copy = n
    for prime in primes:
        while n_copy % prime == 0:
            prime_factors.append(prime)
            n_copy //= prime
        if n_copy == 1:
            return prime_factors

all_prime_factors = [get_prime_factorization_of_(n) for n in range(2, upper_bound)]

for i in range(upper_bound-2):
    n = i + 2
    if t.is_prime(n):
        factorization_book[n] = {(n,)}
        continue
    factorizations = set()
    for pf in set(all_prime_factors[i]):
        factors_without_pf = n // pf
        factorizations_wo_pf = factorization_book[factors_without_pf]
        for factorization_wo_pf in factorizations_wo_pf:
            lst = sorted([pf] + list(factorization_wo_pf))
            factorizations.add(tuple(lst))
            fact_wo_pf_as_list = list(factorization_wo_pf)
            for index in range(len(fact_wo_pf_as_list)):
                lst = fact_wo_pf_as_list[:]
                lst[index] *= pf
                factorizations.add(tuple(sorted(lst)))
    factorization_book[n] = factorizations

min_nums = set()
for i in range(2, 12001):
    min_num = minimal_ps_number_for_k(i)
    print(i, min_num)
    min_nums.add(min_num)

print(sum(min_nums))

