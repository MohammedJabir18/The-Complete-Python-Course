# A dictionary value is another collection item (dictionary).
student_dict = {"Jabir": {"Physics": 89, "Chemistry": 77, "Maths": 68, "English": 81},
                "Hijas": {"Physics": 69, "Chemistry": 58, "Maths": 73, "English": 77},
                "Shibu": {"Physics": 59, "Chemistry": 46, "Maths": 89, "English": 94},
                "Ramis": {"Physics": 63, "Chemistry": 76, "Maths": 59, "English": 82},
                "Nabeel": {"Physics": 67, "Chemistry": 91, "Maths": 83, "English": 89}}

# Method-1 for using nested loop.
# for name, subjects_n_scores in student_dict.items():
#     print(f"{name}: ", end="")
#     for subject, score in subjects_n_scores.items():
#         print(f"{subject} = {score}", end=" ")
#     print()

# Method-2 for using join() function.
for name, subjects_n_scores in student_dict.items():
    subjects_scores = ", ".join(f"{subject} = {score}" for subject, score in subjects_n_scores.items())
    print(f"{name}: {subjects_scores}")


