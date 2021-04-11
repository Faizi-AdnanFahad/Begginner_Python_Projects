# parrot = "Norwegian Blue"
#
# for character in parrot:
#     print(character)


# for i in range(0, len(parrot)):
#     print(parrot[i])

number = input("Please enter a series of numbers, using any separators you lke: ")
seperators = ""

# 1. first way of summing all the numbers
sumS = 0

for char in number:
    if not char.isnumeric():    #   isnumeric method checks if the char variable is numeric
        seperators += char
    else:
        sumS += int(char)


print(seperators)
print(sumS)

# values = "".join(char if char not in seperators else " " for char in number).split()
# print([int(val) for val in values])

# 2. Second of adding all numbers from the list using the built in function sum()
values = "".join(char if char not in seperators else " " for char in number).split()
print(sum([int(val) for val in values]))
