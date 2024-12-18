num_list = []
num_limit = int(input("Enter the limit of list: "))
i = 0
while i < num_limit:
    num_list.append(int(input(f"Enter {i+1} element: ")))
    i = i + 1

mini = num_list[0]
i = 1
while i < num_limit:
    if mini > num_list[i]:
        mini = num_list[i]
    i += 1

print("Lowest value from the list =", mini)

