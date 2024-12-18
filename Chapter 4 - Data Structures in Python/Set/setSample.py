num_set = {7, 9, 76, 24, 22, 7, 31, 2, 93, 31}
print(num_set)
print(type(num_set))

num_set.add(70)  # Adding an element in set.
print(num_set)

num_set.remove(31)  # Removing an element in set. raises KeyError if not present.

num_set.discard(5)  # Removes element (5) from the set if present. Does nothing, no error raised
print(num_set)

num = num_set.copy()  # Copying the set into another variable.

num_set.clear()  # Clear the set. Now it's an empty set.
print(num_set)

# Removes and returns an arbitrary element from the set.
# An arbitrary element refers to an element chosen without any specific criteria or preference.
popped_element = num.pop()
print(popped_element)  # Output could be any element


