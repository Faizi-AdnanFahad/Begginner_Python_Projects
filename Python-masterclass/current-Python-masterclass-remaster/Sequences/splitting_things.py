panagram = """
The quick brown fox jumps\tover 
the lazy dog
"""

# Consider the difference
string_in_list = panagram.split()  # returns a list where each element is separated by the argument of split
print(string_in_list)

list_in_string = " ".join(string_in_list)
print(list_in_string)

numbers = "9,223,372,036,854,775,807"
print(numbers.split(","))

print()

generated_list = ['9', ' ',
                  '2', '2', '3', ' ',
                  '3', '7', '2', ' ',
                  '0', '3', '6', ' ',
                  '8', '5', '4', ' ',
                  '7', '7', '5', ' ',
                  '8', '0', '7'
                  ]
joined_values = "".join(generated_list)
print(joined_values)

splitted_Values = joined_values.split(" ")
print(splitted_Values)

# JOIN: list --> string
# SPLIT: string --> list

# splitted_Values = ['9', '223', '372', '036', '854', '775', '807']

# create a new list with the splitted_Values with int values instead of strings

#   1
intList = []
for num in splitted_Values:
    intList.append(int(num))
print(intList)

#   2
for index in range(len(splitted_Values)):
    splitted_Values[index] = int(splitted_Values[index])
print(splitted_Values)










