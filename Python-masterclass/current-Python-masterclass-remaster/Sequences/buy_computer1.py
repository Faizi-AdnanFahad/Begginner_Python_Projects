available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "hdmi",
                   "dvd drive"
                   ]

# valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]

valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)
current_choice = "-"
computer_parts = []     # create an empty list

while current_choice != "0":
    if current_choice in valid_choices:
        print(f"Adding {current_choice}")
        computer_parts.append(available_parts[int(current_choice) - 1])
    else:
        for number, part in enumerate(available_parts):
            print(f"{number + 1}: {part}")
    current_choice = input()

print(computer_parts)


# for i in range(len(available_parts)):
#     print(f"{i + 1}: {available_parts[i]}")