"""
10. Calculate the sum of digits of a given number.
"""

num = int(input("Enter a number: "))  # 156
number = num
_sum = 0
while num >= 1:
    last_digit = num % 10  # 6, 5, 1
    reminder_digit = num // 10  # 15, 1
    num = reminder_digit
    _sum += last_digit

print(f"The sum of the digits of {number} is {_sum}")
