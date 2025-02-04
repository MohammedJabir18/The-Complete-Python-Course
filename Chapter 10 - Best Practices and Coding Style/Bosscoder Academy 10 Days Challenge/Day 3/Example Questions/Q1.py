"""
Q1. Write a program that checks if a given number is positive, negative, or zero.
"""

num = int(input("Enter a number: "))

if num > 0:
    print(f"{num} is a positive number")
elif num < 0:
    print(f"{num} is negative number")
else:
    print("Entered number is zero")
