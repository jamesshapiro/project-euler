#!/usr/bin/env python3 -tt

import math

"""
very ugly, will add a more verbose solution eventually
"""
print(len([x for x in range(1,101) for y in range(1,101) if y >= x and (math.factorial(y) / (math.factorial(x) * math.factorial(y-x))) > 1000000]))
