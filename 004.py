#!/usr/bin/env python3 -tt

max_product = 0
for i in range(100,1000):
    for j in range(100,1000):
        product = i*j
        stringified = str(product)
        if stringified == stringified[::-1] and product > max_product:
            max_product = product
print(max_product)
