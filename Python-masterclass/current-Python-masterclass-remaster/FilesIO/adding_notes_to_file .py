# Write a program to append the times tables to our jabberwocky poem
# in sample.txt. We want the tables from 2 to 12 (similar to the output
# from the For loops part 2 lecture in section 6).
#
# The first column of numbers should be right justified. As an example,
# the 2 times table should look like this:
#   1 times 2 is 2
#   2 times 2 is 4
#   3 times 2 is 6
#   4 times 2 is 8
#   5 times 2 is 10
#   6 times 2 is 12
#   7 times 2 is 14
#   8 times 2 is 16
#   9 times 2 is 18
#  10 times 2 is 20
#  11 times 2 is 22
#  12 times 2 is 24
#  --------------------

with open("C:/Users/Adnan Fahad Faizi/Desktop/Python Course/Python_Course_2021/Python-masterclass/Text_Files/sample.txt", 'a') as data_file:
    print(file=data_file)   # creates a space, `file=data_file` is important because it will make sure that the code is
    # implemented in the text file not in the console
    for i in range(1, 13):
        for j in range(1, 13):
            print(f"{j:>2} times {i} is {i * j:>2}", file=data_file)
        print("-" * 40, file=data_file)



















