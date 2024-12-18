emp_name = {'jabir': 50000, 'Hijas': 60000, 'nabeel': 80000, 'ramis': 30000}
print(type(emp_name))

print(emp_name['nabeel'])  # Here I fetch the data using key. O/P is 80000

emp_name["Shibu"] = 40000  # Adding a new element in dictionary

emp_name.__setitem__("abdu", 25000)  # It's also adding an element in dictionary using magic function
emp_name.__setitem__('abdu', 10000)  # If I add a key again the older value is updated with new one

print(emp_name)
