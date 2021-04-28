# 1
# time_table = [print(x, y) for x in range(5) for y in range(5)]

# 2
time_table = [str(x) + " " + str(x * y) for x in range(1, 11) for y in range(1, 11)]
for each in time_table:
    print(each)

