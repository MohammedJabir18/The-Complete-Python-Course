"""
3. Write a Python program to check if a given number is a prime number.
"""

num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, (num//2)+1):
        if num % i == 0:
            print(f"{num} is a non prime number")
            break
    else:
        print(f"{num} is prime number")
else:
    print("Enter a greater than 1")
