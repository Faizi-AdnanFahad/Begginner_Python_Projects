# Create a new Python file - I've called this one "fizzbuzz.py".
#
# Use the conditional expression from the previous video to produce
# a list comprehension that returns the fizzbuzz results.
#
# If a number's divisible by 3, the value should be "fizz".
# If it's divisible by 5, the value should be "buzz".
# If it's divisible by both 3 and 5, the value should be "fizz buzz"
# Finally, if none of those conditions apply, the value will be the number itself.
#
# The code from the end of the last video appears below, so you can check the result.
list_fizz_buzz = ['fizz buzz' if x % 15 == 0 else 'fizz' if x % 3 == 0 else 'buzz' if x % 5 == 0 else str(x) for x in
                  range(1, 31)]
print(list_fizz_buzz)

for buzz in list_fizz_buzz:
    print(buzz.center(100, "*"))

fizz_buzz_normal = []
for i in range(1, 31):
    if i % 15 == 0:
        fizz_buzz_normal.append('fizz buzz')
    elif i % 3 == 0:
        fizz_buzz_normal.append('fizz')
    elif i % 5 == 0:
        fizz_buzz_normal.append('buzz')
    else:
        fizz_buzz_normal.append(str(i))
print(fizz_buzz_normal)

for x in range(1, 31):
    fizzbuzz = "fizz buzz" if x % 15 == 0 else "fizz" if x % 3 == 0 else "buzz" if x % 5 == 0 else str(x)
    print(fizzbuzz)
