a = {1: "one", 2: "two", 3: "three"}

print(a.get(6, "not found"))
print(a)


print(a.setdefault(2))
print(a)

print(a.setdefault(7, "seven"))
print(a)
print(a.pop(99, "nO"))

keys = a.keys()
print(keys)

keys_tuple = tuple(keys)
print(keys_tuple)


what = [382, 324, 212,3]
