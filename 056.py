#!/usr/bin/env python3 -tt

print(max([sum(map(int,str(x**y))) for x in range (1, 100) for y in range(1,100)]))
