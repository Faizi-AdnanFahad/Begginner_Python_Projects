import copy

animals = {
    "lion": "scary",
    "elephant": "big",
    "teddy": "cuddly",
}


# # Performing deep copy
# things = copy.deepcopy(animals)
# animals["teddy"] = "toy"
# print(things["teddy"])  # cuddly
# print(animals["teddy"])  # toy
#
# animals2 = {
#     "lion": ["scary", "big", "cat"],
#     "elephant": ["big", "grey", "wrinkled"],
#     "teddy": ["cuddly", "stuffed"],
# }
#
# things = copy.deepcopy(animals2)
#
# print(things["teddy"])  # ['cuddly', 'stuffed']
# print(animals2["teddy"])  # ['cuddly', 'stuffed']
#
# print()
#
# things["teddy"].append("toy")
# print(things["teddy"])  # ['cuddly', 'stuffed', 'toy']
# print(animals2["teddy"])  # ['cuddly', 'stuffed']

# -----------------------------------------------------------------------------
# # Performing a shallow copy
# things = animals.copy()
#
# animals["teddy"] = "toy"
# print(things["teddy"])  # toy
# print(animals["teddy"])  # toy
#
# animals["teddy"] = "toy"
# print(things["teddy"])  # cuddly
# print(animals["teddy"])  # toy
#
# animals2 = {
#     "lion": ["scary", "big", "cat"],
#     "elephant": ["big", "grey", "wrinkled"],
#     "teddy": ["cuddly", "stuffed"],
# }
#
# things = animals2.copy()
#
# print(things["teddy"])  # ['cuddly', 'stuffed']
# print(animals2["teddy"])  # ['cuddly', 'stuffed']
#
# print()
#
# things["teddy"].append("toy")
# print(things["teddy"])  # ['cuddly', 'stuffed', 'toy']
# print(animals2["teddy"])  # ['cuddly', 'stuffed', 'toy']
# -------------------------------------------------------------------------------------------












