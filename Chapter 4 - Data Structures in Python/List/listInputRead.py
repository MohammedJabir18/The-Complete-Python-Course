num_list = []
num = int(input("How many numbers do you want to store a list: "))
i = 0
while i < num:
    age = int(input(f"Enter {i+1} number: "))
    num_list.append(age)
    i += 1

print(num_list)
