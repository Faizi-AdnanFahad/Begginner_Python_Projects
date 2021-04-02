#
#         012345678901234
parrot = "Norwegian Blue"   # Len(parrot) = 14

print(parrot[0:6:2])    # Nre
print(parrot[0:6:3])    # Nw

number = "9,233;372:036 854,775;807"
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])














"""
print(parrot[-4:2]) # we can't print backward

print(parrot[0:6])  # Norweg
print(parrot[-14:6])
print(parrot[-14:-8])

print()

# we can slice from left to right(no matter if use positive, negative and a mixture of them) or  but not from right to left
print(parrot[-4:-2])    # Bl
print(parrot[-4:12])    # Bl
"""



""" # Slicing
print(parrot[0:6])  # Norweg
print(parrot[3:5])
print(parrot[0:9])
print(parrot[:9])
print(parrot[0:])

print(parrot[10:14])
print(parrot[10:])

print(parrot[:6])
print(parrot[6:])

print(parrot[0:6] + parrot[6:])
"""





#   posiive and negative indexing

"""
print(parrot[3])
print(parrot[4])
print()
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()

print(parrot[-11])
print(parrot[-1])
print()
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print()

# we can subtract the positive indexing - the String length to get the negative indexing of the strings
print(parrot[3 - 14])
print(parrot[4 - 14])
print()
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])
"""












