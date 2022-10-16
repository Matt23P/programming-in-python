import argparse
import configparser
import os


def get_args():
    parser = argparse.ArgumentParser(description="Programming in Python 2022/23 =-=-= WOLF & SHEEP",
                                     epilog="M. Przybyl 236630, F. Warchol 236682")
    parser.add_argument("-d", "--directory", default="output", type=str,
                        help="directory where output files will be placed (eg. DIRECTORY = ./dir/output)")
    parser.add_argument("-r", "--rounds", default=50, type=int, help="the number of rounds (ROUNDS > 0)")
    parser.add_argument("-s", "--sheep", default=15, type=int, help="the number of sheep in a flock (SHEEP > 0)")
    parser.add_argument("-wo", "--wolves", default=1, type=int, help="the number of wolves (WOLVES > 0)")
    parser.add_argument("-c", "--config", type=str,
                        help="indicates a configuration file (eg. CONFIG = ./dir/config.ini)")
    parser.add_argument("-w", "--wait", default=0, type=int,
                        help="simulation will be paused at the end of each round (WAIT = 0 - do not pause, WAIT = 1 - "
                             "pause)")
    parser.add_argument("-l", "--log", type=int,
                        help="turn on logging events (DEBUG-10, INFO-20, WARNING-30, ERROR-40, CRITICAL-50)", default=10)
    args = parser.parse_args()

    log_level = args.log
    level = 10
    while True:
        if log_level == level:
            break
        if level == 50:
            exit(-1)
        level += 10

    var = args.wait
    if var > 1 or var < 0:
        exit(-1)
    else:
        if var == 1:
            wait = True
        elif var == 0:
            wait = False

    rounds = args.rounds
    if rounds <= 0:
        exit(-1)

    flock_size = args.sheep
    if flock_size <= 0:
        exit(-1)

    num_of_wolves = args.wolves
    if num_of_wolves <= 0:
        exit(-1)

    directory = args.directory

    if args.config is None:
        sheep_move_dist = 0.5
        wolf_move_dist = 1
        board_a = 10
        board_b = 10
    else:
        config_file = args.config
        if os.path.exists(config_file):
            config = configparser.ConfigParser()
            config.sections()
            config.read(config_file)
            try:
                board_a = float(config['Terrain']['board_a'])
                if board_a <= 0:
                    exit(-1)
            except ValueError:
                exit(-1)

            try:
                board_b = float(config['Terrain']['board_b'])
                if board_b <= 0:
                    exit(-1)
            except ValueError:
                exit(-1)

            try:
                sheep_move_dist = float(config['Movement']['sheep_move_dist'])
                if sheep_move_dist <= 0:
                    exit(-1)
            except ValueError:
                exit(-1)

            try:
                wolf_move_dist = float(config['Movement']['wolf_move_dist'])
                if wolf_move_dist <= 0:
                    exit(-1)
            except ValueError:
                exit(-1)
        else:
            exit(-1)

    return wait, rounds, flock_size, num_of_wolves, directory, board_a, board_b, sheep_move_dist, wolf_move_dist, log_level
