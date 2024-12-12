"""
Read a number from user and check the number is prime or not

A prime number is a natural number greater than 1 that has exactly two distinct divisors: 1 and itself.
In other words, it can only be divided evenly (without leaving a remainder) by 1 and itself.
"""

num = int(input("Enter a number: "))

i = 2
if num > 1:
    while i <= num//2:
        if num % i == 0:
            print(f"{num} is not prime number")
            break
        i += 1
    else:
        print(f"{num} is a prime number")
else:
    print("Enter a valid number")
