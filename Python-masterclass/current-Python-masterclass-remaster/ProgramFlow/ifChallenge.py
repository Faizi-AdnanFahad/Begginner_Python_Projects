name = input("Please enter your name: ")
age = int(input(f"Please enter you age {name}: "))

if 18 <= age <= 30:
    print(f"Since you are {age} years old, you can join the party {name}")
else:
    print("Sorry you are not allowed " + name)