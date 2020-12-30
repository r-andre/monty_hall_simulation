#!/usr/bin/env python

import random

def monty_hall(switch:bool) -> str:
    '''
    Playing the Monty Hall game.
    Input: whether the door should be switched or not.
    Output: whether the game was won or not.
    '''
    # Defining goats and prize:
    behind_doors = ['goat', 'goat', 'prize']
    # Randomly assigning goats and prize the doors A, B, or C:
    random.shuffle(behind_doors)
    door_a = behind_doors[0]
    door_b = behind_doors[1]
    door_c = behind_doors[2]

    # Giving the options of picking doors A, B, or C:
    options = [door_a, door_b, door_c]

    # Randomly choosing one of the three doors:
    choice = options.pop(random.randint(0,2))

    # Revealing one door with a goat and excluding it from the options:
    options.remove('goat')

    # If the choice was correct and the door is now switched, the game is lost:
    if switch and choice == 'prize':
        return False
    # If the choice was wrong and the door is now switched, the game is won:
    elif switch and choice == 'goat':
        return True
    # If the choice is correct and the door is not switched, the game is won:
    else:
        if choice == 'prize':
            return True
        elif choice == 'goat':
            return False

if __name__ == "__main__":

    print(
        'Playing the Monty Hall game 100,000 times each with switching doors ' +
        'and without switching doors...'
        )

    # Playing the Monty Hall game 100,000 times each with switching and without:
    instances = 100000
    results_switch = [monty_hall(True) for i in range(0, instances)]
    results_no_switch = [monty_hall(False) for i in range(0, instances)]

    # Printing the win percentage for switching doors:
    print(
        'Win percentage when switching doors: ' +
        str(
            round(
                results_switch.count(True) / len(results_switch) * 100, 1)
                ) +
        '%'
        )

    # Printing the win percentage for not switching doors:
    print(
        'Win percentage when not switching doors: ' +
        str(
            round(
                results_no_switch.count(True) / len(results_no_switch) * 100, 1)
                ) +
        '%'
    )
