def square(x):
    return x * x


# f = square  # f does not the same job as the function, e.g, --> f(5) = square(5)
# print(f)
# print(square)
#
# print(f(5))

# Passing one function inside another function
def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result


squares = my_map(square, [1, 2, 3, 4, 5])
print(squares)


def cube(x):
    return x ** 3


cubes = my_map(cube, [1, 2, 3, 4, 5])
print(cubes)

print("--------------------------------------------------------")

# Returning Function form anther Function

def logger(msg):

    def log_message():
        print('Log', msg)

    return log_message  # Returning a function


log_Hi = logger('HI!')
log_Hi()

print("--------------------------------------------------------")


def html_tag(tag):

    def wrap_text(msg):
        print(f'<{tag}>{msg}</{tag}>')

    return wrap_text


print_h1 = html_tag('h1')
print_h1('Test Headline!')
print_h1('Another Headline!')


print_p = html_tag('p')
print_p('Test Paragraph')










