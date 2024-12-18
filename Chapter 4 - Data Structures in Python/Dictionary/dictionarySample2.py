emp_name = {"Jabir": 85000, "Hijas": 60000, "Nabeel": 50000, "Ramis": 40000, "Shibu": 35000, "Ummer": 70000}
emp_name_dup = emp_name.copy()  # Copy the dictionary into another variable

emp_name.popitem()  # Removes last element from dictionary

pop_element = emp_name.popitem()  # Removed item can store in a variable.
print(pop_element)  # Removed item is stored as tuple type.

remove_item = emp_name.pop("Hijas")  # Here remove the specific element using key. But the variable store only a value.
print(remove_item)  # Removed item is integer type.

print(emp_name_dup)

emp_name.clear()  # To clear the dictionary
print(emp_name)
