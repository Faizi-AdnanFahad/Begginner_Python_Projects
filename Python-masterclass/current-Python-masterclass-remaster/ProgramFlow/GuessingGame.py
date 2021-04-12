import random

highest = 10

answer = random.randint(1, highest)

print(f"Please guess the number between 1 and {highest}: ")
guess = int(input())    # TODO: Remove after testing

count = 2

if guess == answer:
    print("Wow you guessed it in your first attempt!")

while guess != answer and guess != 0:
    if guess > answer:
        print("Please guess lower: ")
        guess = int(input())
    else:
        print("Please guess higher: ")
        guess = int(input())

    if guess == answer:
        print(f"Well done! you guessed it in your {count} attempt")
        break

    if guess == 0:
        break
    count += 1



# if guess == answer:
#     print("You got it first time")
# else:
#     if guess < answer:
#         print("Please guess higher: ")
#     else:   # guess must be greater than answer
#         print("Please guess lower: ")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it ")
#     else:
#         print("Sorry, you have not guessed correctly")


# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:   # guess must be greater than answer
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it ")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")


# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guess correctly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guess correctly")
# else:
#     print("You got it first time")
