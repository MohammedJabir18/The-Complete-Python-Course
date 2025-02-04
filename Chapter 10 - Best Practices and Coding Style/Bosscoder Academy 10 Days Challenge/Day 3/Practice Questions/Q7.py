"""
7. Write a program that calculates the factorial of a given number.
"""

num = int(input("Enter a number: "))

fact = 1
for i in range(1, num+1):
    fact *= i

print(f"Factorial of {num} is {fact}")
