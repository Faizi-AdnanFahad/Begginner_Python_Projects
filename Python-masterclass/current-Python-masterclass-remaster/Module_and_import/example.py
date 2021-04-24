import shelve
# print(dir())

# print(dir(__builtins__))

# All the methods in builtin_function
# for m in dir(__builtins__):
#     print(m)

# print(dir(shelve))

for obj in dir(shelve):
    if obj[0] != "-":
        print(obj)

# Gives information about any function
help(shelve)

