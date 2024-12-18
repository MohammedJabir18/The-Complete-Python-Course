# A dictionary value is another collection item (tuple).
student_dict = {"Jabir": (89, 77, 68, 81), "Hijas": (49, 58, 73, 77), "Shibu": (59, 46, 89, 94),
                "Ramis": (49, 76, 59, 82), "Nabeel": (67, 91, 83, 89)}
subjects = ["Physics", "Chemistry", "Maths", "English"]

for name, scores in student_dict.items():
    subject_scores = ", ".join(f"{subject} = {score}" for subject, score in zip(subjects, scores))
    print(f"{name}: {subject_scores}")

