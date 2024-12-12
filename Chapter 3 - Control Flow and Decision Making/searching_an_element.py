"""
 Searching for an Element
 -------------------------
Exit a loop when a specific element is found in a list and also print the position.
"""

search_list = [23, 2, 49, 5, 12, 89, 71, 29, 4, 87]
find_element = int(input("Which element you want to find: "))

for index, element in enumerate(search_list, start=1):  # enumerate() function is mainly used for finding index number
    if find_element == element:
        print(f"{element} is found at {index} position")
        break
else:
    print(f"{find_element} is not found in this list.")
