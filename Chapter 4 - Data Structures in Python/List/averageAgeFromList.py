age_list = []
age_limit = int(input("How many ages do you want to store: "))
i = 0
add_list = 0
while i < age_limit:
    age = int(input(f"Enter {i+1} person age: "))
    age_list.append(age)
    add_list += age_list[i]
    i += 1

avg = add_list / i
print(age_list)
print("Average of age =", avg)
