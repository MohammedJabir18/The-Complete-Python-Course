student_dict = {"Jabir": (89, 77, 68, 81), "Hijas": (49, 58, 73, 77), "Shibu": (59, 46, 89, 94),
                "Ramis": (49, 76, 59, 82), "Nabeel": (67, 91, 83, 89)}

for name, scores in student_dict.items():
    sum_values = 0
    count = 0
    for score in scores:
        count += 1
        sum_values += score
    print(f"Average mark of {name} is {sum_values/count}")

print()
student_dict2 = {"Jabir": {"Physics": 89, "Chemistry": 77, "Maths": 68, "English": 81},
                 "Hijas": {"Physics": 69, "Chemistry": 58, "Maths": 73, "English": 77},
                 "Shibu": {"Physics": 59, "Chemistry": 46, "Maths": 89, "English": 94},
                 "Ramis": {"Physics": 63, "Chemistry": 76, "Maths": 59, "English": 82},
                 "Nabeel": {"Physics": 67, "Chemistry": 91, "Maths": 83, "English": 89}}

for index, (name, mark_dict) in enumerate(student_dict2.items(), start=1):
    total = 0
    for marks in mark_dict.values():
        total += marks
    print(f"{index}. Average mark of {name} is {total/len(mark_dict)}")
