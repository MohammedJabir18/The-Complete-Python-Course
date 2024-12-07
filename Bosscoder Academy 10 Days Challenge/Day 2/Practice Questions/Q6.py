"""
6. Write a Python program to check if a given string is a pangram (contains all letters of the alphabet).

sample inputs:
Pack my box with five dozen liquor jugs
Hello, world
Sphinx of black quartz, judge my vow
"""

import string

user_input = input("Enter a string: ").lower()

alphabets = set(string.ascii_lowercase)  # Create a set of all lowercase letters

input_set = set(user_input)  # Create a set of the characters in the string

# Check if all letters of the alphabet are in the input set
if alphabets.issubset(input_set):
    print(f"{user_input} is a pangram")
else:
    print(f"{user_input} is not a pangram")
