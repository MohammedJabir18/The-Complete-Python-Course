"""
2. Given a list of integers, find all the even numbers and store them in a new list.
"""

num_list = [34, 23, 87, 26, 13, 90, 33, 78]

# List to store the even numbers using list comprehension
new_list = [num for num in num_list if num % 2 == 0]

print("List of integers:", num_list)
print("New list:", new_list)
