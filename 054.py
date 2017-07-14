#!/usr/bin/env python3 -tt

from poker import Hand
from deck import Card

suits = {'S': '♠', 'C': '♣', 'D': '♦', 'H': '♥'}
ranks = {str(num): num for num in range(2,10)}
ranks.update({'T':10,'J':11,'Q':12,'K':13,'A':14})

def to_Card(txt_card):
    return Card(rank=int(ranks[txt_card[0]]), suit = suits[txt_card[1]])

def to_Hand(txt_hand):
    return Hand([to_Card(txt_card) for txt_card in txt_hand])

with open('/Users/jamesshapiro/Desktop/p054_poker.txt', 'r') as f:
    lines = f.readlines()

total = 0
for line in lines:
    cards = line.split()
    if to_Hand(cards[:5]) > to_Hand(cards[5:]):
        total += 1

print(total)
