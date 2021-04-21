list = [1, 2]

listb = [9]

list.extend(listb)


list.reverse()
print(list)
print(list[::-1])

a = list.pop(1)
print(a)
print(list)