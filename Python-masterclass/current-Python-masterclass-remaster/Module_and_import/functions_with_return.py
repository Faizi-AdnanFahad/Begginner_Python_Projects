def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def center_text(*args, sep=' '):
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
    return " " * left_margin + text


# Calls for function

# Creating a new file
with open("menu", "w") as menu:
    s1 = center_text("Spam and eggs")
    print(s1, file=menu)
    print(center_text("Spam, spam and eggs"), file=menu)
    print(center_text(12), file=menu)
    print(center_text("Spam, spam, spam and eggs"), file=menu)
    print(center_text("first", "second", 3, 5, "spam"), file=menu)
    print(center_text("Hi", "Bye", sep="-"), file=menu)
    print(center_text("wow", "second", sep="-"), file=menu)












# # Printing in console
# s1 = print(center_text("Spam and eggs"))
# print(s1)
# print(center_text("Spam, spam and eggs"))
# print(center_text(12))
# print(print(center_text("Spam, spam, spam and eggs")))
# print(center_text("first", "second", 3, 5, "spam"))
# print(center_text("Hi", "Bye", sep="-"))
# print(center_text("wow", "second", sep="-"))
#
# print("=" + str(12 * 3))