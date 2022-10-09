import random


def get_direction():
    # --- get the random integer from 0 to 3 --- #
    direction = random.randint(0, 3)
    return int(direction)
