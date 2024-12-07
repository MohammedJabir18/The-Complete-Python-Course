"""
Skip vowels in a string
"""

word = input("Enter the word: ").lower()
vowels = ("a", "e", "i", "o", "u")

print("After removing vowels letters")
for letter in word:
    if letter in vowels:
        continue
    print(letter)
