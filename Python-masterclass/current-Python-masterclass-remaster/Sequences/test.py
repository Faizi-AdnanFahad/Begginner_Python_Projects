numbers = {
    1: 'one',
    3: 'three',
    5: 'five',
    7: 'seven',
    9: 'nine',
}

b = {
    4: "four",
    6: "six",
}

numbers.update(b)
print(numbers)  # -> {1: 'one', 3: 'three', 5: 'five', 7: 'seven', 9: 'nine', 4: 'four', 6: 'six'}

print(numbers.update(b))  # None

