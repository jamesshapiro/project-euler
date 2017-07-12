#!/usr/bin/env python3 -tt

import collections
import itertools
import math

digit_string = "0123456789"
anagramic_squares = []

def is_square(x):
    return math.sqrt(x) == math.ceil(math.sqrt(x))

def distinct_letters(word):
    return set(letter for letter in word)

def is_anagramic_square(word, anagrams):
    print(word)
    digits = itertools.combinations(digit_string, len(distinct_letters(word)))
    for digit_combo in digits:
        digit_perms = itertools.permutations(digit_combo, len(digit_combo))
        for digit_perm in digit_perms:
            if digit_perm[0] == "0":
                continue
            for anagram in anagrams:
                if anagram == word:
                    continue
                digit_word = word[:]
                digit_word2 = anagram[:]
                for (i, letter) in enumerate(distinct_letters(digit_word)):
                    digit_word = digit_word.replace(letter, digit_perm[i])
                    digit_word2 = digit_word2.replace(letter, digit_perm[i])
                if digit_word2[0] == "0" or digit_word[0] == "0":
                    continue
                if is_square(int(digit_word)) and is_square(int(digit_word2)):
                    anagramic_squares.append(int(digit_word))
                    anagramic_squares.append(int(digit_word2))
                    print(word, digit_word, anagram, digit_word2)
    

with open('/Users/jamesshapiro/Desktop/p098_words.txt', 'r') as f:
    lines = f.readlines()
line = lines[0]
line = line.replace('"','').replace("'","")
words = line.split(",")

anagram_dict = collections.defaultdict(lambda: set())
for word in words:
    sorted_word = "".join(sorted(word))
    anagram_dict[sorted_word].add(word)

for key in anagram_dict:
    for word in anagram_dict[key]:
        if len(anagram_dict[key]) > 1:
            is_anagramic_square(word, anagram_dict[key])

print(max(anagramic_squares))

