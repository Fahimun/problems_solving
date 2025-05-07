# Python Program to Print all Prime Numbers in an Interval
# (একটি ব্যবধানে সকল মৌলিক সংখ্যা প্রিন্ট করার জন্য পাইথন প্রোগ্রাম)

import math

def is_prime(num):

    if num <= 1:
        return False
    elif num <= 3:
        return True
    elif num % 2 == 0 or num % 3 == 0:
        return False
    else:
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i+2) == 0:
                return False

            i += 6
        else:
            return True

def find_primes_in_range(start, end):
    print(f"{start} from {end} all Prime Number:")

    for num in range(start, end + 1):
        if is_prime(num):
            print(num)

lower = 10
upper = 25

find_primes_in_range(lower, upper)