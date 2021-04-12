

age = int(input("Please enter you age: "))
if 16 <= age <= 65:
    print("You can enter")
else:
    print("Sorry yor are either too old or too young to enter the bar")

#   another way of doing this code

if age in range(16, 66):
    print("You can enter")
else:
    print("Sorry yor are either too old or too young to enter the bar")