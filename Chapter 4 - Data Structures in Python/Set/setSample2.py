num_set1 = {1, 2, 3, 4}
num_set2 = {3, 8, 2, 6, 7, 5}

union_set = num_set1.union(num_set2)
print(f"Union of {num_set1} and {num_set2} = {union_set}\n")

inter_set = num_set1.intersection(num_set2)
print(f"Intersection of {num_set1} and {num_set2} = {inter_set}\n")

A_difference_B = num_set1.difference(num_set2)
print(f"Existing A. But not B = {A_difference_B}")

B_difference_A = num_set2.difference(num_set1)
print(f"Existing B. But not A = {B_difference_A}")
