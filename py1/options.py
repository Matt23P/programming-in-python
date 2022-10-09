def get_wolf_move_dist():
    wolf_move_dist = input("Move distance of wolf: ")
    try:
        wolf_move_dist = float(wolf_move_dist)
    except ValueError:
        print("Input is not a float!")
        get_wolf_move_dist()
    if wolf_move_dist > 0:
        return wolf_move_dist
    else:
        print("Invalid range!")
        get_wolf_move_dist()


def get_board_size():
    board_a = input("Size of first side of board: ")
    board_b = input("Size of second side of board: ")
    try:
        board_a = int(board_a)
        board_b = int(board_b)
    except ValueError:
        print("Input is not an integer!")
        get_board_size()
    if board_a >= 1 and board_b >= 1:
        return board_a, board_b
    else:
        print("Invalid range!")
        get_board_size()


def get_num_of_wolves():
    num_of_wolves = input("Number of wolves: ")
    try:
        num_of_wolves = int(num_of_wolves)
    except ValueError:
        print("Input is not an integer!")
        get_num_of_wolves()
    if num_of_wolves >= 1:
        return num_of_wolves
    else:
        print("Invalid range!")
        get_num_of_wolves()


def get_flock_size():
    flock_size = input("Size of a flock of sheep: ")
    try:
        flock_size = int(flock_size)
    except ValueError:
        print("Input is not an integer!")
        get_flock_size()
    if flock_size >= 1:
        return flock_size
    else:
        print("Invalid range!")
        get_flock_size()


def get_sheep_move_dist():
    distance = input("Move distance of sheep: ")
    try:
        distance = float(distance)
    except ValueError:
        print("Input is not a float!")
        get_sheep_move_dist()
    if distance > 0:
        return distance
    else:
        print("Invalid range!")
        get_sheep_move_dist()


def get_rounds():
    rounds = input("Number of rounds: ")
    try:
        rounds = int(rounds)
    except ValueError:
        print("Input is not an integer!")
        get_rounds()
    if rounds >= 1:
        return rounds
    else:
        print("Invalid range!")
        get_rounds()


def choice():
    cho = input("Please choose the settings:\n"
                "1. Manual settings\n"
                "2. Static task settings\n"
                "> ")
    try:
        cho = int(cho)
    except ValueError:
        print("Input is not an integer!")
        menu()
    if cho < 1 or cho > 2:
        print("Please select settings 1 or 2.")
        print("------------------------------")
        menu()
    else:
        return cho


def menu():
    cho = choice()
    if cho == 1:
        rounds = get_rounds()
        sheep_move_dist = get_sheep_move_dist()
        flock_size = get_flock_size()
        num_of_wolves = get_num_of_wolves()
        wolf_move_dist = get_wolf_move_dist()
        board_a, board_b = get_board_size()
    else:
        rounds = 50
        sheep_move_dist = 0.5
        flock_size = 15
        num_of_wolves = 1
        wolf_move_dist = 1
        board_a = 10
        board_b = 10

    return rounds, sheep_move_dist, flock_size, num_of_wolves, wolf_move_dist, board_a, board_b
