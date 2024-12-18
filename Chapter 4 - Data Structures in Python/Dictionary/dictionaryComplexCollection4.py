emp_details = {
    "Id": 101,
    "Name": "Mohammed Jabir M",
    "Salary": 95000,
    "Academic_details": {'10th': 95, '12th': 80, 'degree': 75},
    "Department": "Development",
    "Address": ("Mayanthriyakath (H)", "Purangu", "Malappuram", 679584),
    "Project": {"Android": ["Flutter", "React Native"], "Python": ["Django", "Numpy", "Pandas"]}
}

for lang, modules in emp_details.get("Project").items():
    print(f"{lang}: {', '.join(i for i in modules)}")

print()
for details in emp_details.get("Address"):
    print(details)
