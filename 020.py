#!/usr/bin/env python3 -tt

import math

one_hundred_f = math.factorial(100)
string = str(one_hundred_f)
print(sum(int(x) for x in string))
