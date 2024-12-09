"""
6. Implement a program that prints the multiplication table of a given number.
"""

num = int(input("Which multiplication table you want: "))

for i in range(1, 11):
    print(f"{i} x {num} = {i * num}")
