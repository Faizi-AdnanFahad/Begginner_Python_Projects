# data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160,
#         170, 183, 185, 187, 188, 191, 350, 360]

# data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160,
#         170, 183, 185, 187, 188, 191]

# data = [104, 105, 110, 120, 130, 130, 150, 160,
#                 170, 183, 185, 187, 188, 191, 350, 360]

# data = [104, 105, 110, 120, 130, 130, 150, 160,
#         170, 183, 185, 187, 188, 191]

# data = [213, 234, 1235, 2343, 3124]
data = [1, 329, 9, 120, 788, 122, 40]

# del data[0:2]
# print(data)
#
# del data[-1:-3] # or data[-1:-3:-1]
# print(data)

min_valid = 100
max_valid = 200

# --------WONT WORK TRY IT---------
# for index, value in enumerate(data):
#     if (value < min_valid) or (value > max_valid):
#         data.remove(value)
#
# print(data)

# -------WORKING VERSION-----------
# i = 0
# condition = i < len(data)
#
# while condition:
#     if (data[i] > max_valid) or (data[i] < min_valid):
#         del data[i]
#         i = 0
#         condition = i < len(data)
#     else:
#         i += 1
#         condition = i < len(data)
# print(data)

# ------------------------------------------------------------
# Useful to know: Printing backward while using the enumerate
# for index, value in enumerate(data):
#     print(data[len(data) - index - 1])
# ------------------------------------------------------------
# The most efficient
# Process the low values in the list
# stop = 0
# for index, value in enumerate(data):
#     if value >= min_valid:
#         stop = index
#         break
#
# print(stop)  # for debugging
# del data[:stop]
# print(data)
#
# # Process the high values in the list
# start = 0
# for index in range(len(data) - 1, -1, -1):
#     if data[index] <= max_valid:
#         # we have the index of the last item to keep
#         # item to delete which is 1 after the 'index'
#         start = index + 1
#         break
#
# print(start)    # For debugging
# del data[start:]
# print(data)
