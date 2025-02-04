"""
9. Create a function to count the number of vowels in a given string.
"""

# Function to count the number of vowels in a string
def count_vowels(string: str):
    vowels = "aeiouAEIOU"
    count = 0

    for i in string:
        if i in vowels:
            count += 1

    return count

user_input = input("Enter a string: ")

print(f"The number of vowels in the {user_input} is {count_vowels(user_input)}")
