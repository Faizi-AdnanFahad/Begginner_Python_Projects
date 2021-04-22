numbers = (0, 1, 2, 3, 4, 5)

print(numbers)
print(*numbers)  # === print(0,1 2, 3, 4)

# print(numbers, sep=";")
# print(*numbers, sep=";")
# print(0, 1, 2, 3, 4, 5, sep=";")


# arbitrarily numbers of arguments passed in this function be unpacked in line 14
# in line 15, since there's no star before args, arbitrarily numbers of arguments passed in this function will be
# treated as tuples because they are tuples
def test_star(*args):
    print(args)
    for x in args:
        print(x)


test_star(0, 1, 2, 3, 4, 5, 6)

print()  # ()

test_star((1, 2, 3), (2, 6))
