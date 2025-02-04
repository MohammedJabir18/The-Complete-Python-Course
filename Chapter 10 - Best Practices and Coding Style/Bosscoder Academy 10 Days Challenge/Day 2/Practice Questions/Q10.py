"""
10. Write a program to check if a number is prime.
"""

num = int(input("Enter the number: "))

half_check = num // 2

# A prime number is greater than 1
if num > 1:
    for i in range(2, half_check+1):
        if num % i == 0:
            print(f"{num} is non prime number")
            break
    else:
        print(f"{num} is a prime number")
else:
    print("Invalid input")
