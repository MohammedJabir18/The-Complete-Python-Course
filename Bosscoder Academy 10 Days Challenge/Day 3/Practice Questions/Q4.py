"""
4. Create a program that generates the Fibonacci sequence up to a given number of terms.
"""

num = int(input("Enter a number: "))

a, b = 0, 1

for _ in range(num):
    print(a)
    a, b = b, a + b
