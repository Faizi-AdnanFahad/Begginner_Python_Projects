a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 11, 12, 13]

# Deleting backward
# leng = len(a)
# for i in range(len(a)):
#     del a[leng - 1 - i]
#     print(a)

# OR

# for i in range(len(a)):
#     a.pop()
#     print(a)

leng = len(a)
for i in range(len(a)):
    del a[-leng + i]
    print(a)

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'g']