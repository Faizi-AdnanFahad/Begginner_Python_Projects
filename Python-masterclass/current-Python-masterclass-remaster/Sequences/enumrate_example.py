for index, character in enumerate("abcdefgh"):
    print(index, character)

# OR

for t in enumerate("abcdefgh"):
    index, character = t
    print(index, character)

# first iteration of the code in line 1-2 or 6-8 is equivalent to the following code:
index, character = (0, 'a')
print(index)
print(character)

# -------------------------------------------------

for t in enumerate("abcdefgh"):
    print(t)    # At each iteration, t is being assigned to another tuple

# #  extra Code for another usage of 'enumerate'
# ty = enumerate("HI")
# t, y = ty
# print(ty)
# print(t)
# print(y)

# ------------------------------------------------------

# The enumerator(#some sequence): will help us get the index and each item at that index in the following format:
#
# for index, character in enumerate("abcdefgh"):
#
#     print(index, character)
#
#
# OUTPUT:
#
# 0 a
#
# 1 b
#
# 2 c
#
# 3 d
#
# 4 e
#
# 5 f
#
# 6 g
#
# 7 h
