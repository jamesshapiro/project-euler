#!/usr/bin/env python3 -tt

coins = [1, 2, 5, 10, 20, 50, 100, 200]

def ways_to_make_change(n, coin_types):
    if n < 0:
        return 0
    if n == 0:
        return 1
    elif coin_types == 1:
        return 1
    return ways_to_make_change(n, coin_types - 1) + ways_to_make_change(n - coins[coin_types-1], coin_types)

print(ways_to_make_change(200, len(coins)))

