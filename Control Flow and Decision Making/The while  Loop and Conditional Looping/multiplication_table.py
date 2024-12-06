"""
Code the multiplication table using while loop and read a number which multiplication table user wants.
"""

num = int(input("Which multiplication table you want: "))

i = 1
while i <= 10:
    print(f"{i} x {num} = {i*num}")
    i += 1
