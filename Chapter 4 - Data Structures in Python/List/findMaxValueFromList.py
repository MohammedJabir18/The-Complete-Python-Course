num_list = [15, 34, 55, 23, 54, 65, 33, 87, 52, 43, 51]
max_value = 0
i = 0
while i < len(num_list):
    if max_value < num_list[i]:
        max_value = num_list[i]
    i += 1
print("Highest value from the list is", max_value)
