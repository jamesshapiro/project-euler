#!/usr/bin/env python3 -tt

def inc_if_sunday(day, total):
    if day % 7 == 6:
        return total + 1
    return total

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def count_sundays_before(end_year):
    total = 0
    
    year = 1901
    day = 1
    month_idx = 0
    while year < end_year:
        for month_idx in range(12):
            total = inc_if_sunday(day, total)
            day += days_in_month[month_idx]
            if month_idx == 1 and year % 4 == 0:
                if year % 100 != 0 or year % 400 == 0:
                    day += 1
        year += 1
    return total

print(count_sundays_before(2001))
