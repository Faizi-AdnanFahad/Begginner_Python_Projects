import random


def get_integer(prompt=""):
    """
    Get an integer from Standard Input (stdin).

    The function will continue looping, and prompting
    the user, util a valid `int` is entered.

    :param prompt: The String that the user will see, when
        they're prompted to enter the value.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(prompt)
        if temp.isnumeric():
            return int(temp)    # return will cause this loop to exit from the loop
        else:
            prompt = "please enter a number not a string: "

# Print the documentation of our function
#   1
# help(get_integer)

#   2
# print(input.__doc__ )
# print("*" * 80)
# print(get_integer.__doc__ )
# print("*" * 80)

highest = 1000
answer = random.randint(1, highest)

print(f"Please guess the number between 1 and {highest}: ")
guess = get_integer()   # TODO: Remove after testing

count = 2

if guess == answer:
    print("Wow you guessed it in your first attempt!")

while guess != answer and guess != 0:
    if guess > answer:
        print("Please guess lower: ")
        guess = get_integer()
    else:
        print("Please guess higher: ")
        guess = get_integer()

    if guess == answer:
        print(f"Well done! you guessed it in your {count} attempt")
        break

    if guess == 0:
        break
    count += 1