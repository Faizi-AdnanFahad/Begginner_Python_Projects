low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to start")

numOfGuesses = 1
while low != high:
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
    # numOfGuesses = numOfGuesses + 1
    numOfGuesses += 1
else:   # this else is part of the loop and WHENEVER the loop condition evaluates to false, this will get executed. Note that a while loop's body can be executed and when its false it will come back to else or at if the loop's condition is false at the first place it can also go to else.
    print("You thought of the number {}".format(low))   # it can only get be ignored if we step out of the loop with break in the while loop's body
    print(f"I got it in {numOfGuesses} number of guesses")
