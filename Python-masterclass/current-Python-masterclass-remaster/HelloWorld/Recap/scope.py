"""
LEGB
Local, Enclosing, Global, Built-in
"""

# x = "Global x"  # global variable
#
#
# def test():
#     global x
#     x = 'x value has been changed'  # because of the keyword global, the x variable will be changed
#     # x = 'local x'  # local x
#     y = "local y"  # local variable
#     print(y)
#     print(x)
#
#
# # print(y)  # Not possible
#
# test()
# print(x)


def test_1():
    a = "1"

    def test_2():
        nonlocal a
        a = "2"
        print(a)

    test_2()
    print(a)

test_1()





















