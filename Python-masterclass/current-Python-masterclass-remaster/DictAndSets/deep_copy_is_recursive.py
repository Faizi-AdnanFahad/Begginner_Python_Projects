from deep_copy_challenge import deep_copy_dict
import copy

original = {
    "Tim": ["Buchalka", ["Programmer", "Teacher"]],
    "J-P": ["Roberts", ["Programmer", "Teacher"]],
}


copy_1 = copy.deepcopy(original)
copy_2 = deep_copy_dict(original)

original["Tim"].append("Australia")
original["J-P"].append("UK")

original["Tim"][1].append("Cashier")
original["J-P"][1].append("Courier")

print(original)
print(copy_1)
print(copy_2)
