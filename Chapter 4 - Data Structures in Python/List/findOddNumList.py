num_list = [24, 51, 62, 25, 34, 52, 21, 76, 44, 59, 10, 91]
i = 0
count = 0
while i < len(num_list):
    if num_list[i] % 2 != 0:
        print(num_list[i])
        count = count + 1
    i += 1
print("Total number of odd numbers:", count)
