"""
5. Create a Python function to check if a given string is a palindrome.
"""

def is_palindrome(string: str):
    # Check if the string is equal to its reverse
    if string == string[::-1]:
        print(f"{string} is a palindrome")
    else:
        print(f"{string} is not a palindrome")

user_input = input("Enter a string to check if it's a palindrome: ")

is_palindrome(user_input)
