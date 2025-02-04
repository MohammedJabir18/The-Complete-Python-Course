"""
9. Given a list of words, count the number of words with more than five characters.
"""

words = ["hello", "world", "python", "programming", "data", "science", "artificial", "intelligence"]

# Count the number of words with more than five characters using list comprehension
count = len([n for n in words if len(n) > 5])

print(f"{count} words are more than five characters.")
