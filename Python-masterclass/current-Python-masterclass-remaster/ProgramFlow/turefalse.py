# day = "Friday"
# temperature = 9
# raining = False
#
# if (day == "Saturday" and temperature > 27) or not raining:
#     print("Go Swimming")
# else:
#     print("Learn Python")

# Automatic False Values: 0, empty sequences
if 0:
    print("True")
else:
    print("False")

name = input("Please enter your name: ")

# if name:
if name != "":
    print(f"Hello, {name}")
else:
    print("Are you the man with no name?")
