"""
3.  Implement a program that checks if a given string is a palindrome.
"""

string = input("Enter a string: ")

# Checking Palindrome or not using the ternary operator.
has_palindrome = f"{string} is palindrome" if string[0] == string[::-1] else f"{string} is not palindrome"

print(has_palindrome)
