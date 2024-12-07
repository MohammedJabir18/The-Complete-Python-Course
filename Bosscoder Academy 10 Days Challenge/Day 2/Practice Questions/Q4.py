"""
 Create a function to reverse a given string.
"""

def reverse_string(string: str) -> str:
    reversed_string = string[::-1]  # Here reversing using the index
    return reversed_string

user_input = input("Enter a string: ")
print(reverse_string(user_input))
