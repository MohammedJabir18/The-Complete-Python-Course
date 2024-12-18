"""
Given a sentence, write a function called reverse_and_capitalize(sentence) that does the following:

Reverses the order of words in the sentence.
Capitalizes the first letter of each word.
Excludes punctuation from the final output.
"""
import string


def reverse_and_capitalize(sentence):
    word_ = sentence.split()
    reversed_and_capitalized = [
        word.strip(string.punctuation).capitalize() for word in word_[::-1]
    ]
    result = " ".join(reversed_and_capitalized)
    print(result)


words = input("Enter anything: ")
reverse_and_capitalize(words)
