a = 2
b = 3
print(f"a = {a}, b = {b}")

# Method 1 - Swapping variable values
a, b = b, a
print(f"a = {a}, b = {b}")

# Method 2 - Swapping variable values
temp = a
a = b
b = temp
print(f"a = {a}, b = {b}")