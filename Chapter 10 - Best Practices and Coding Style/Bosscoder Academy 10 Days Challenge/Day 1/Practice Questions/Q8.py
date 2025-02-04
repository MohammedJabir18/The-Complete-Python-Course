"""
8. Given a list of integers, find the sum of all positive numbers.
"""

num_list = [39, -83, 27, 20, -98, 29, 9, -3, -4]

# Calculate the sum of all positive numbers
positive_sum = sum(num for num in num_list if num > 0)

print("Sum of the all positive numbers =", positive_sum)
