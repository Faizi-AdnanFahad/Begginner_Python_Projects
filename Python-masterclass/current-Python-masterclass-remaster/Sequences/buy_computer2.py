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
        print(f"Adding {current_choice}")
        computer_parts.append(available_parts[current_choice - 1])
    else:
        for number, part in enumerate(available_parts):
            print(f"{number + 1}: {part}")
    current_choice = int(input())

print(computer_parts)