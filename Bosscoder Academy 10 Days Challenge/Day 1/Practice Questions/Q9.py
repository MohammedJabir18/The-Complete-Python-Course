"""
9. Create a program that takes a sentence as input and counts the number of words in it.
"""

sentence = input("Enter the a sentence: ")

words = sentence.split()  # Split the sentence into words

print("The number words in the sentence is", len(words))
