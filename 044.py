#!/usr/bin/env python3 -tt

first_n = 10000
pentagons = [n*(3*n - 1) // 2 for n in range(1, first_n + 1)]
pent_set = {n*(3*n - 1) // 2 for n in range(1, first_n + 1)}

for i in range(first_n - 1):
    for j in range(i, first_n):
        if pentagons[i] + pentagons[j] in pent_set:
            if pentagons[j] - pentagons[i] in pent_set:
                print(pentagons[i], pentagons[j], pentagons[j] - pentagons[i])

