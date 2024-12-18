num_list = []
num_limit = int(input("Enter the limit of list: "))
i = 0
count = 0
even_list = []
while i < num_limit:
    nums = int(input(f"Enter {i+1} value: "))
    num_list.append(nums)
    if num_list[i] % 2 == 0:
        even_list.append(num_list[i])
        count = count + 1
    i += 1
print(even_list)
print("The total number of even numbers:", count)
