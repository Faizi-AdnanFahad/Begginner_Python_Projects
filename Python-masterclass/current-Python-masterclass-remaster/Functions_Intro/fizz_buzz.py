def fizz_buzz(number: int) -> str:
    """
    This function should get a number and returns `fizz`, `buzz`, `fizz_buzz` or the number.

    :return:if the number is divisible by 3 returns `fizz`,
        if the number is divisible by 5 returns `buzz`, if the number is divisible by 3 and 5 returns `fizz_buzz`,
        and if the number is not divisible by 3 or 5 it returns the number back.
    """
    result = ""
    if number % 15 == 0:
        result = "fizz buzz"
    elif number % 3 == 0:
        result = "fizz"
    elif number % 5 == 0:
        result = "buzz"
    else:
        result = str(number)

    return result


# The next number computer will choose will be the number that its value should be calculated and
#   user should be asked to enter its value, if the input matches the value, then they should continue, else the game
#   should end when the loop terminates or the player's input doesn't match the expected value.

input("Play Fizz Buzz,   Press ENTER to start")
print()
next_number = 0
while next_number < 99:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    correct_answer = fizz_buzz(next_number)
    players_answer = input("Your go: ")
    if players_answer != correct_answer:
        print("You lose, the correct answer was {}".format(correct_answer))
        break
else:
    print("Well done, you reached {}".format(next_number))












# for num in range(1, 100):
#     print(num, fizz_buzz(num), sep=": ")
















