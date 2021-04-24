# First way of opening a file
# jabber = open(
#     "C:/Users/Adnan Fahad Faizi/Desktop/Python Course/Python_Course_2021/Python-masterclass/Text_Files/sample.txt", 'r')
# # 'r' - read only
#
# print("-" * 40)
#
# for line in jabber:
#     if "he" in line.lower():
#         print(line, end="")  # end="" prevents from printing another line
#
# jabber.close()



# Second way of opening a file
# with open("C:/Users/Adnan Fahad Faizi/Desktop/Python Course/Python_Course_2021/Python-masterclass/Text_Files/sample.txt", 'r') as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end="")



# Third way of opening a file
# with open("C:/Users/Adnan Fahad Faizi/Desktop/Python Course/Python_Course_2021/Python-masterclass/Text_Files/sample.txt", 'r') as jabber:
#     line = jabber.readline()
#     print(line)
#     while line:
#         print(line, end="")
#         line = jabber.readline()



# # Forth way of opening a file
# with open("C:/Users/Adnan Fahad Faizi/Desktop/Python Course/Python_Course_2021/Python-masterclass/Text_Files/sample.txt", 'r') as jabber:
#     lines = jabber.readline()  # list
# print(lines)
#
# for line in lines:
#     print(line, end="")



# Fifth way of opening a file
# with open("C:/Users/Adnan Fahad Faizi/Desktop/Python Course/Python_Course_2021/Python-masterclass/Text_Files/sample.txt", 'r') as jabber:
#     lines = jabber.read()  # list
#
# for line in lines[::-1]:
#     print(line, end="")




