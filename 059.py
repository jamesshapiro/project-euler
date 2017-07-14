#!/usr/bin/env python3 -tt

import itertools

lower = 'abcdefghijklmnopqrstuvwxyz'*3
passwords = ["".join(x) for x in set(itertools.permutations(lower, 3))]
with open('/Users/jamesshapiro/Desktop/p059_cipher.txt', 'r') as f:
    line = f.readlines()[0].strip()
chars = line.split(",")

total = 0
plaintexts = []

max_spaces_index = 0
max_spaces = 0
for i in range(len(passwords)):
    if passwords[i] != "god":
        continue
    mask = (passwords[i]*(len(chars) // 3)) + passwords[i][:len(chars) % 3]
    plaintext = "".join([chr(int(x) ^ ord(y)) for (x,y) in zip(chars, mask)])
    plaintexts.append(plaintext)
    num_spaces = len(list(filter(lambda z: z == "e", plaintext)))
    if num_spaces > max_spaces:
        max_spaces = num_spaces
        max_spaces_index = i
    if " the " in plaintext:
        #print(plaintext)
        print(sum(ord(x) for x in plaintext))


