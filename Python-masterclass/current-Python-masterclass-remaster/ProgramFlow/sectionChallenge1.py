list_of_things_to_do = ["Learn Python", "Learn Java", "Go swimming", "Go hiking", "Play Soccer", "Play Cricket", "Quit"]

output = ""
for i in range(len(list_of_things_to_do)):
    if i < len(list_of_things_to_do) - 1:
        output += f"{str(i + 1)}. {list_of_things_to_do[i]}\n"
    else:
        output += f"0. {list_of_things_to_do[i]}"

condition = True
chosen_activity = -1

while condition:
    print(output)
    chosen_activity = int(input("Enter the number you want to learn: "))
    if 1 <= chosen_activity <= len(list_of_things_to_do):
        print(f"Great choice! to do {list_of_things_to_do[chosen_activity - 1]}")
    elif chosen_activity == 0:
        break
    else:
        condition = False
else:
    print(f"Your input {chosen_activity} is not valid")