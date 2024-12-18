emp_salary = emp_name = {"Jabir": 85000, "Hijas": 60000, "Nabeel": 50000,
                         "Ramis": 40000, "Shibu": 35000, "Ummer": 70000}

print(emp_salary.values())  # To get the all values from the dictionary.

for i in emp_salary.values():  # Here the values act as list.
    print(i)

print(emp_salary.keys())  # To get the all keys from the dictionary.

for i in emp_salary.keys():  # Here the keys act as list.
    print(i)

print(emp_salary.get("Rafi", 3))  # Here get using not existing value given the program never be crashed or error.

# Updating the dictionary with new key-value pairs.
emp_salary.update({"Shabeer": 25000, "Salman": 30000, "Abdu": 15000})

print(emp_salary)
