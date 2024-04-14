import time
import random

result_list = []

# Trials
for i in range(1, 100, 1):

    # Generates a random number from 1 and 6
    no = random.randint(1, 6)

    result_list.append(no)


    if no == 1:
        print("┌─────────┐")
        print("│         │")
        print("│    ●    │")
        print("│         │")
        print("└─────────┘")
    if no == 2:
        print("┌─────────┐")
        print("│  ●      │")
        print("│         │")
        print("│      ●  │")
        print("└─────────┘")
    if no == 3:
        print("┌─────────┐")
        print("│  ●      │")
        print("│    ●    │")
        print("│      ●  │")
        print("└─────────┘")
    if no == 4:
        print("┌─────────┐")
        print("│  ●   ●  │")
        print("│         │")
        print("│  ●   ●  │")
        print("└─────────┘")
    if no == 5:
        print("┌─────────┐")
        print("│  ●   ●  │")
        print("│    ●    │")
        print("│  ●   ●  │")
        print("└─────────┘")
    if no == 6:
        print("┌─────────┐")
        print("│  ●   ●  │")
        print("│  ●   ●  │")
        print("│  ●   ●  │")
        print("└─────────┘")
        if result_list.count(6) == 5:
            break


    # Wait until the next trial
    time.sleep(0.25)
