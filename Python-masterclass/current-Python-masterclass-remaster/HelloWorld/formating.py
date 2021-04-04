for i in range(1, 13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))

print()

for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i ** 2, i ** 3))

print()

print("pi is approximately {0:12}".format(22/7))    #   15 digits after the decimal points
print("pi is approximately {0:12f}".format(22/7))   #   6 digits after the decimal points
print("pi is approximately {0:2}".format(22/7))
print("pi is approximately {0:12.50f}".format(22/7))
print("pi is approximately {0:52.50f}".format(22/7))
print("pi is approximately {0:62.50f}".format(22/7))
print("pi is approximately {0:72.50f}".format(22/7))

for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3))

print()

print("This is an example I made {:.2f} ".format(13.123123123))    # Only 2 digits after the decimal point



