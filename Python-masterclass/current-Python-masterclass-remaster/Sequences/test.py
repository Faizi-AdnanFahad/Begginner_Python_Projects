a = [1, 2, 3]
b = a.copy()
print(id(b))
print(id(a))

print()

c = {1: "a"}
b = c.copy()
print(id(c))
print(id(b))