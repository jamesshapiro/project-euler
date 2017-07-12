#!/usr/bin/env python3 -tt

def inc_if_sunday(day, total):
    if day % 7 == 6:
        return total + 1
    return total

def count_sundays_before(end_year):
    total = 0
    
    year = 1901
    day = 1
    while year < end_year:
        # January
        total = inc_if_sunday(day, total)
        day += 31
        total = inc_if_sunday(day, total)
        day += 28
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            day += 1
        total = inc_if_sunday(day, total)
        day += 31
        
        #April
        total = inc_if_sunday(day, total)
        day += 30
        total = inc_if_sunday(day, total)
        day += 31
        total = inc_if_sunday(day, total)
        day += 30
        
        # July
        total = inc_if_sunday(day, total)
        day += 31
        
        total = inc_if_sunday(day, total)
        day += 31
        
        total = inc_if_sunday(day, total)
        day += 30
        
        #October
        total = inc_if_sunday(day, total)
        day += 31
        
        total = inc_if_sunday(day, total)
        day += 30
        
        total = inc_if_sunday(day, total)
        day += 31

        year += 1
    return total

print(count_sundays_before(2001))
