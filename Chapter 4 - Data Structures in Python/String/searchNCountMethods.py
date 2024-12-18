word = "python world, hai python"

print(word.find("world"))  # Returns the index of the first occurrence of the substring.
print(word.find("Hello"))  # Returns -1 if not found.
print(word.rfind("python"))  # Returns the index of the last occurrence of the substring.

text = "python hello world"
print(f"Count of {text} =", word.count("o"))  # count(substring): Counts the occurrences of a substring.


