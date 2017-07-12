#!/usr/bin/env python3 -tt

def next_tph(tph, t, p, h):
    tph = [next(t), next(p), next(h)]
    while min(tph) != max(tph):
        min_index = tph.index(min(tph))
        if min_index == 0:
            tph[0] = next(t)
        elif min_index == 1:
            tph[1] = next(p)
        else:
            tph[2] = next(h)
    return tph

def triangle_generator():
    i = 1
    while True:
        yield int(i * (i + 1) * 0.5)
        i += 1

def pentagon_generator():
    i = 1
    while True:
        yield int(i * (3 * i - 1) * 0.5)
        i += 1

def hexagon_generator():
    i = 1
    while True:
        yield int(i * (2 * i - 1))
        i += 1

t = triangle_generator()
p = pentagon_generator()
h = hexagon_generator()

tph = []
for _ in range(3):
    tph = next_tph([], t, p, h)

print(tph[0])

