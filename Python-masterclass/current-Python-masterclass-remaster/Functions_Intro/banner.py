def banner_text(text: str = " ", width: int = 80) -> None:  # the second parameter uses a default value (meaning that if no argument has passed, the default values will be used)
    """ Print a string centred, with ** either side.

    :param text: The string to print.
        An asterisk (*) will result in a row of asterisks.
        The default will print a blank line, with a ** border at
        the left and right edges.
    :param screen_width: The overall width to print within
        (including the 4 spaces for the ** either side).
    :raises ValueError: if the supplied string is too long to fit (length of the text greater than width).
    """
    if len(text) > width - 4:
        raise ValueError(f"String {text} is larger than specified width {width}")

    if text == "*":
        print("*" * width)
    else:
        output_string = f"**{text.center(width - 4)}**"  # this will create a sequence of the len(width - 4) and place the text inside it
        print(output_string)


banner_text("*", 60)
banner_text("Always look on the bright side of life...", 60)
banner_text("If life seems jolly rotten,", 60)
banner_text("There's something you've forgotten!", 60)
banner_text("And that's to laugh and smile and dance and sing,", 60)
banner_text(width=60)  # if we want to use the second argument but still want to get the first arguemnt as the default value, therefore, we can just add the keyword for that argument and only pass that argument to the our function.
banner_text("When you're feeling in the dumps,", 60)
banner_text("Don't be silly chumps,", 60)
banner_text("Just purse your lips and whistle - that's the thing!", 100)
banner_text("And... always look on the bright side of life...", 60)
banner_text("*", 60)

# result = banner_text("Nothing is returned")
# print(result)

numbers = [4, 2, 7, 5, 8, 3, 9, 6, 1]
print(numbers.sort())