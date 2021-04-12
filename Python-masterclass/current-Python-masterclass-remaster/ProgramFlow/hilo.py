low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to start")

numOfGuesses = 1
while True:
    guess = low + (high - low) // 2
    high_low = input(f"My guess is {guess}, should I guess higher or lower? Enter h or l, or c if my guess was correct").casefold()

    if high_low == "h":
        # Guess higher. This low end of the range becomes 1 greater than the guess.
        low = guess + 1
    elif high_low == "l":
        # Guess lower. This high end of the range becomes 1 less than the guess.
        high = guess - 1
    elif high_low == "c":
        print("I got it in {} guesses!".format(numOfGuesses))
        break
    else:
        print("Please enter h, l or c")
    numOfGuesses += 1
