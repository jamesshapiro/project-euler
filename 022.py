#!/usr/bin/env python3 -tt

import json

with open('022-input.json') as json_data:
    names = json.load(json_data)

def name_value(name):
    return sum(ord(letter) - 64 for letter in name)

sorted_names = sorted(names)

print(sum((index + 1) * name_value(name)
          for (index, name) in enumerate(sorted_names)))

