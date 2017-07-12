#!/usr/bin/env python3 -tt

numbers = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
           6: "six", 7: "seven", 8: "eight", 9: "nine",
          10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
           14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
          18: "eighteen", 19: "nineteen",
          20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
           60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety",
           1000: "one thousand"}

def get_description(n):
    if n < 20:
        return numbers[n]
    elif n < 100 and n % 10 == 0:
        return numbers[n]
    elif n < 100:
        return numbers[n - (n % 10)] + " " + numbers[n % 10]
    elif n < 1000 and n % 100 == 0:
        return numbers[n // 100] + " hundred"
    elif n < 1000:
        return numbers[n // 100] + " hundred and " + get_description(n % 100)
    else:
        return numbers[n]

print(sum([len(get_description(x).replace(" ","")) for x in range(1,1001)]))
