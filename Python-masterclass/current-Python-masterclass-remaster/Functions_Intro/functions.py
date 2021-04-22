def multiply(x: float, y: float) -> float:
    """
    Multiply 2 numbers.

    Although this function is intended to multiply 2 numbers,
    you can also use it to multiply a sequence.  If you pass
    a string, for example, as the first argument, you'll get
    the string repeated `y` times as the returned value.

    :param x: The first number to multiply.
    :param y: The number to multiply `x` by.
    :return: The product of `x` and `y`.
    """
    result = x * y
    return result


def is_palindrome(string: str) -> bool:
    """
    Check if a string is a palindrome.

    A palindrome is a string that reads the same forwards as backwards.

    :param string: The string to check.
    :return: True if `string` is a palindrome, False otherwise.
    """
    # backwards = string[::-1]
    # return backwards == string
    return string[::-1].casefold() == string.casefold()


def is_palindrome_sentence(sentence: str) -> bool:
    """
    Check if a sentence is a palindrome.

    The function ignores whitespace, capitalisation and
    punctuation in the sentence.

    :param sentence: The sentence to check.
    :return: True if `sentence` is a palindrome, False otherwise.
    """
    new_sentence = ""
    for char in sentence:
        if char not in ",. !$?%":  # OR if char.isalnum():
            new_sentence += char

    # return new_sentence[::-1].casefold() == new_sentence.casefold()
    return is_palindrome(sentence)


def fibonacci(n: int) -> int:
    """Return the `n` th Fibonacci number, for positive `n`."""
    if 0 <= n <= 1:
        return n

    n_minus1, n_minus2 = 1, 0

    result = None
    for i in range(n - 1):
        result = n_minus1 + n_minus2
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))

# sentence = input("Please enter a sentence to check: ")
# if is_palindrome_sentence(sentence):
#     print(f"{sentence}: is a palindrome")
# else:
#     print(f"'{sentence}' is not a palindrome")

# word = input("Please enter a word to check: ")
# if is_palindrome(word):
#     print(f"{word} is a palindrome")
# else:
#     print(f"'{word}' is not a palindrome")


# answer = multiply(10.5, 4)  # 42.0
# print(answer)
#
# print(multiply(6, 7))  # 42
#
# for val in range(1, 5):
#     tow_times = multiply(2, val)
#     print(tow_times)

print(multiply(1, 2))