#!/usr/bin/env python3 -tt

import itertools

squares = ["01", "04", "09", "16", "25", "36", "49", "64", "81"]

def dice_can_form_all_squares(pair):
    all_nums = []
    die_1 = list(pair)[0]
    if len(list(pair)) == 1:
        die_2 = die_1
    else:
        die_2 = list(pair)[1]
    if 6 in die_1:
        die_1 = die_1 + (9,)
    elif 9 in die_1:
        die_1 = die_1 + (6,)
    if 6 in die_2:
        die_2 = die_2 + (9,)
    elif 9 in die_2:
        die_2 = die_2 + (6,)
        
#    print(die_1)
    all_nums.extend(str(i)+str(j) for i in die_1 for j in die_2)
    all_nums.extend(str(j)+str(i) for i in die_1 for j in die_2)
    if all(square in all_nums for square in squares):
#        print(pair)
        return True
    

digits = [0,1,2,3,4,5,6,7,8,9]
die_combos = itertools.combinations(digits, 6)

all_pairs = set(frozenset(pair) for pair in itertools.product(die_combos, repeat=2))

#for pair_of_die in all_pairs:
#    print(pair_of_die)

#print(len(all_pairs))

square_pairs = [pair for pair in all_pairs if dice_can_form_all_squares(pair)]
for i in range(len(square_pairs)-1):
    for j in range(i+1, len(square_pairs)):
        list1 = list(square_pairs[i])
        list2 = list(square_pairs[j])
        print(list1[1])
        if list1[0] == list2[0] and list1[1] == list2[1]:
            print(i,j)
        elif list1[1] == list2[0] and list1[0] == list2[1]:
            print(i,j)
print(len(square_pairs))
