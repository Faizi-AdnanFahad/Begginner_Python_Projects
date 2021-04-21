a = b = c = d = e = f = 42
print(c)

x, y, z = 1, 2, 76
print(x)
print(y)
print(z)

print("Unpacking on tuple")
#   -------------------------------------------
data = 1, 2, 76  # data represents a tuple
x, y, z = data
print(x)
print(y)
print(z)
#   -------------------------------------------
print("Unpacking a list")
# Disadvantage of unpacking them compare to a tuple is that, if we change the list (e.g.,
# appending new element to the list, the unpacking will crash.)

data_list = [12, 13, 14]
p, q, r = data_list
print(p)
print(q)
print(r)
#   -------------------------------------------
print("Unpacking a string")

data_list = "WOW"
p, q, r = data_list
print(p)
print(q)
print(r)










