data = [104, 101, 4, 105, 308, 103, 5, 107, 100, 306, 102, 108]
    #    0    1   2   3    4    5   6   7    8    9    10   11
min_value = 100
max_value = 200

                                 # second comma is used to go till the last index and since we can't use 0 we should use any other number less than 0

#   GREAT WAY OF SOLVING THE OUTLINERS.PY FILE PROBLEM, by printing backward
# for index in range(len(data) - 1, -1, -1):
#     if data[index] < min_value or data[index] > max_value:
#         print(index)
#         del data[index]
#
# print(data)

# Second efficient
top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if value < min_value or value > max_value:
        del data[top_index - index]

print(data)





#   another way of iterating backward
# for index in range(len(data)):
#     print(len(data) - index - 1, data[len(data) - index - 1])
