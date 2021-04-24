def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def center_text(*args, sep=' ', end="\n", file=None, flush=False):
    text = ""
    for i in range(len(args)):
        if i < len(args) - 1:
            text += str(args[i]) + sep
        else:
            text += str(args[i])
    # for arg in args:
    #     if arg != args[-1]:
    #         text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text, end=end, file=file, flush=flush)


# printing them to a file
with open("centred", mode='w') as centred_file:
    # call the function
    center_text("Spam and eggs", file=centred_file)
    center_text("Spam, spam and eggs", file=centred_file)
    center_text(12, file=centred_file)
    center_text("Spam, spam, spam and eggs", file=centred_file)
    center_text("first", "second", 3, 5, "spam", sep="-", file=centred_file)
    center_text("Hi", "Bye", sep="-", end="    ", file=centred_file)
    center_text("wow", "second", sep="-", end=" ", file=centred_file)

