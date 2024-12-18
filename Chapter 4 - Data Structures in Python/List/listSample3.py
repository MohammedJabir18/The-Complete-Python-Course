age_list = [18, 24, 64, 67, 42, 76, 68, 33]

age_list.pop(0)  # To remove an element. By default, (-1) remove the last element. This is removing using index number

age_list.pop()

pop_value = age_list.pop(4)  # Removed item can store in a variable
print(pop_value)  # Variable type is an integer

print(age_list)

emp_list = [54, 64, 78, 100, 43, 200, 65, 76, 200, 14]

emp_list.remove(100)  # To remove the value from the list. This is removing using value.

emp_list.remove(200)

print(emp_list)
