available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "hdmi",
                   "dvd drive"
                   ]

current_choice = 20
computer_parts = []     # create an empty list

while current_choice != 0:
    if 1 <= int(current_choice) <= len(available_parts):
        chosen_part = current_choice - 1
        if available_parts[chosen_part] in computer_parts:
            # it's already in, so remove it
            print(f"Removing {current_choice}")
            computer_parts.remove(available_parts[chosen_part])
        else:
            print(f"Adding {current_choice}")
            computer_parts.append(available_parts[chosen_part])
        print("Your list now contains {}".format(computer_parts))
    else:
        print("Please add from the following options: ")
        for number, part in enumerate(available_parts):
            print(f"{number + 1}: {part}")
    current_choice = int(input())

print(computer_parts)
