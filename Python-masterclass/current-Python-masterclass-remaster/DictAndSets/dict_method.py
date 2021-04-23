d = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    "iv": "four",
}

pantry_items = ['chicken', 'spam', 'egg', 'bread', 'lemon']

# ********************************************************************************
# The usage of `Dictionary values`
v = d.values()
print(v)

d[10] = "ten"
print(v)

print("four" in v)  # True
print("eleven" in v)  # False

# changing keys and values of dictionary ot lists
keys = list(d.keys())
values = list(v)
if "four" in values:
    index = values.index("four")
    key = keys[index]
    print(f"{d[key]} was found with the key {key}")

print()

for key, value in d.items():
    if value == "four":
        print(f"{value} was found with the key {key}")
# ********************************************************************************
# Updating the value of dictionary or adding if the item was not in the dictionary
# d2 = {
#     7: "Lucky seven",
#     10: "ten",
#     3: "this is the new three",
# }
#
# d.update(d2)
#
# for key, value in d.items():
#     print(key, value)
#
# # or
# d.update(enumerate(pantry_items))
# for key, value in d.items():
#     print(key, value)
# ********************************************************************************




# Code for the "the remaining `dict` methods" lecture.
# ***************************************************

# ********************************************************************************
# Creates a dictionary that will have the keys of the iterable type passed with same values (second argument) passed
# new_dict = dict.fromkeys(pantry_items, 0)
# print(new_dict)  # -> {'chicken': 0, 'spam': 0, 'egg': 0, 'bread': 0, 'lemon': 0}
# # ********************************************************************************
# keys = d.keys()
# print(keys)  # -> dict_keys([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# # ********************************************************************************
# # Using d.keys() instead of d
# for item in d.keys():  # d or d.keys()
#     print(item)
# ********************************************************************************
