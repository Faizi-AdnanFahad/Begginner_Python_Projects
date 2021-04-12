letters = "abcdefghijklmnopqrstuvwxyz"
        #  01234567890123456789012345
# backward = letters[25:-27:-1] same as backward = letters[25::-1]  it will print all the letters backward including the "a"
backward = letters[25::-1] # It will print backward OR ****letters[::-1] --> reverses the sequence****
# Note when a negative step is used the starting and ending index will be changed and it the sequence will be reversed
print(letters[25:0:-1])  #  Slicing ---> letters[startingIndex:endingIndex:Step]
print(backward)

#   For positive step values the ending index must be greater or equal to the starting index  e.g, letters[0:25:1], letters[3:5:2]
#   For negative step values the starting index must be greater or equal to the ending index. e.g, letters[25:0:-1], letters[2:1:-2]


# IMPORTANT NOTE
# If you want to print straight you have to provide the starting and ending index and use a + step size
# If you want to print backward you have to provide a starting and ending index and use a - step size


# Examples
# create a slice that produces the character qpo
print(letters[16:13:-1])    # qpo
print(letters[-10:-13:-1])  # qpo
print(letters[16 - 26:13 - 26:-1])  # qpo

print()

# slice the string to produce edcba
print(letters[4::-1]) # edcba
print(letters[-22::-1]) #edcba

print()

# slice the string to produce the last 8 characters, in reverse order
print(letters[-1:-9:-1]) #  last eight characters reversed
print(letters[25:17:-1]) #  last eight characters reversed


# ITDIOMS

print(letters[-4:]) #   last 4 characters
print(letters[-3:])
print(letters[-1:]) #   last item
print(letters[:1])  #   first item
print(letters[0])   #   first item # the downfall is that the code will crush if the sequence is empty

seq = ""
print(seq[:1])  # still prints the first index without causing to run into error










