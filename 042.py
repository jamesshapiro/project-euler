#!/usr/bin/env python3 -tt

triangle_numbers = {x*(x+1)/2 for x in range(1, 72)}
def is_triangle_word(word):
    total = sum(map(lambda x: ord(x) - ord('A') + 1, word))
    return total in triangle_numbers

with open('/Users/jamesshapiro/Desktop/p042_words.txt', 'r') as f:
    lines = f.readlines()

line = lines[0]
line = line.replace('"','').replace("'","")
words = line.split(",")

print(len(list(filter(is_triangle_word, words))))

