# for i in range(1, 13):
#     print(f"No. {i} squared is {i ** 2} and cubed is {i ** 3:.2f}")
#     print("*" * 80)

names = input("Please enter your name: ")
age = int(input(f"How old are you, {names}? "))
print(age)

# if age >= 18:
#     print("You are old enough to vote")
#     print("Please put an X in the box")
# else:
#     print(f"Please come back in {18 - age} years")

if age < 18:
    print(f"Please come back in {18 - age} years")
elif age == 900:
    print("Sorry, Yoda, you die in Return of the Jedi")
else:
    print("You are old enough to vote")
    print("Please put an X in the box")





