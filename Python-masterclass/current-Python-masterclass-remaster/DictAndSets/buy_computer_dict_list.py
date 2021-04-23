available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "hdmi cable",
                   "6": "dvd drive",
                   }

current_choice = None
computer_parts = []
while current_choice != "0":
    if current_choice in available_parts:
        chose_part = available_parts[current_choice]
        if chose_part not in computer_parts:
            print(f"Adding {chose_part}")
            computer_parts.append(chose_part)
            print(f"Your current added items: {computer_parts}")
        else:
            print(f"Removing {chose_part}")
            computer_parts.remove(chose_part)
            print(f"Your current added items: {computer_parts}")
    else:
        print("Please add options from the list: ")
        for key, value in available_parts.items():
            print(key, value, sep=": ")
            # print(f"{key}: {value}")
        print("0: To exit")

    current_choice = input("> ")
