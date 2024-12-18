dict_sam = {"old-key-1": 123, "old-key-2": 456, "old-key-3": 789}

# First remove the (old-key-1) element and this value assign to the (new-key-1) key.
dict_sam["new-key-1"] = dict_sam.pop("old-key-1")
print(dict_sam)
