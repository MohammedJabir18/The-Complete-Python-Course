"""
1. Create a program that takes a year as input and checks if it is a leap year or not.
"""

year = int(input("Enter a year: "))

# The year is divisible by 4 and not divisible by 100, or if it is divisible by 400.
# This follows the rules for determining leap years.
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
