userInput = input("Please enter three integers seperated by comma: ")
listInput = userInput.split(",")

result = int(listInput[0]) + int(listInput[1]) - int(listInput[2])
print(result)