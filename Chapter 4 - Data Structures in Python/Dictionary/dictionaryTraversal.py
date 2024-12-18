emp_name = {"Jabir": 80000, "Shuhaib": 90000, "Muhsin": 70000, "Hijas": 50000}

for i in emp_name:
    print(i + ":", emp_name[i])  # Here (i) is keys printing and (emp_name[i]) values printing.
print()

for i in emp_name.items():  # Here (items()) function using to print both keys and values printing.
    print(i)
else:
    print(type(i))  # Here (i) storing variable type is tuple.
print()

# Here happening the tuple unpacking using (i) and (j) variable
# (items()) function using to print both keys and values printing.
for i, j in emp_name.items():
    print(f"{i}: {j}")

emp_salary = {}
for i in range(5):
    name, salary = input("Enter the name and salary: ").split()  # Two inputs assigning two variables using (split())
    # emp_salary[name] = int(salary)  # Method-1 Adding the keys and values in dictionary.
    emp_salary.__setitem__(name, int(salary))  # Method-2 Adding the keys and values in dictionary.
print(emp_salary)
