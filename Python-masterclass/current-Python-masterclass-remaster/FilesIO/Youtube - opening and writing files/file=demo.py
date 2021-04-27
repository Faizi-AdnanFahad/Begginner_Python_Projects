# File objects

# Method - Requires closing
# f = open('text.txt', 'r')
# print(f.name)
#
# f.close()

# READING FROM A FILE
# # Method 2
# with open('text.txt', 'r') as f:
#     # f_contents_all = f.read()  # Reads everything
#     # f_contents_list_of_lines = f.readlines()  # a list of lines
#     # f_contents_each_line = f.readline()  # each line at each call - first LIne
#     # print(f_contents_each_line)
#     #
#     # f_contents_each_line = f.readline()  # each line at each call - first LIne
#     # print(f_contents_each_line)
#
#     # iterating over each line in a file
#     # for line in f:
#     #     print(line, end='')
#
#     # size_to_read = 10
#     # f_contents_up_to_character = f.read(size_to_read)
#     # print(f.tell())  # Current position
#     # while len(f_contents_up_to_character) > 0:
#     #     print(f_contents_up_to_character, end='*')  # Prints the first 10 characters
#     #     f_contents_up_to_character = f.read(size_to_read)  # goes to the next 10 characters
#
#     print("--------------------------------------------------------------------------")
#     size_to_read = 10
#     print(f.read(size_to_read))  # Reads the first 10 characters
#
#     size_to_read = 10
#     print(f.read(size_to_read))  # Reads the second 10 characters
#
#     # if we want the time we call that to start reading from the first character again we use
#     f.seek(0)
#
#     size_to_read = 10
#     print(f.read(size_to_read))  # starts from the beginning


# WRITING TO A FILE
# with open("text2.txt", 'w') as f:
#     # f.write('Test')
#     # f.seek(0)  # starts writing back at 0
#     # f.write('Rest')


# USING READ AND WRITE TOGETHER
with open('text.txt', 'r') as rf:
    with open('text_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

















