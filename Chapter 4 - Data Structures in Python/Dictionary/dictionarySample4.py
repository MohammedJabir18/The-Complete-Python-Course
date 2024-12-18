employee = {}
name = ["Jabir", "Shuhaib", "Hijas", "Ramis", "Shibu"]
salary = [90000, 80000, 70000, 60000, 50000]

if len(name) == len(salary):  # Two lists combining to one list using the for loop.
    for i in range(len(name)):
        keys = name[i]
        values = salary[i]
        employee[keys] = values

print(employee, "\n")

emp_copy = dict(zip(name, salary))  # Two lists combining using the (zip()) function.
print(emp_copy, "\n")

# Here all name lists are converted to dictionary keys and (1) is the value for all elements.
emp_copy2 = dict.fromkeys(name, 1)
print(emp_copy2)

