single_quote = 'Hello'
double_quote = "Hello"
triple_quote = """
Hello World  
"""  # Triple quotes can span multiple lines
print(triple_quote)

# Attempting to change a character will raise an error
# double_quote[0] = 'h' # This will cause a TypeError

# create a new string by using operations such as concatenation or slicing.
new_string = single_quote + " World"
print(new_string)

# (sep()) method is using for the separating with any delimiter between two strings
print("Hello", "World", sep="***")
