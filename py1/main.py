import sheep
import wolf
from colorama import Fore, Style
import args
import logging
import save_operations


def check_alive(flock, size):
    alive = 0
    for h in range(size):
        if flock[h].is_alive():
            alive += 1
    logging.debug("function check_alive() ret: " + str(alive))
    return alive


def get_log_level(level):
    if level == 10:
        return logging.DEBUG
    elif level == 20:
        return logging.INFO
    elif level == 30:
        return logging.WARNING
    elif level == 40:
        return logging.ERROR
    else:
        return logging.CRITICAL


if __name__ == '__main__':
    wait, rounds, flock_size, num_of_wolves, directory, board_a, board_b, sheep_move_dist, wolf_move_dist, log_level = args.get_args()
    log = get_log_level(log_level)

    logging.basicConfig(filename="chase.log",
                        filemode='w',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=log)

    dead_sheep_cord = [None, None]
    flock_of_sheep = []
    wolves = []
    cause = ""
    path = ""
    x, y = 0.0, 0.0
    if rounds <= 1:
        cause = str(rounds) + "round has elapsed"
    else:
        cause = str(rounds) + "rounds have elapsed"

    # --- create the flock and wolves -- #
    logging.warning("SIMULATION HAS STARTED")
    for i in range(flock_size):
        flock_of_sheep.append(sheep.Sheep(i, sheep_move_dist, board_a, board_b))
    for j in range(num_of_wolves):
        wolves.append(wolf.Wolf(j, wolf_move_dist, board_a, board_b, x + j, y + j))

    print("---=== START POSITIONS OF ANIMALS ===---")
    for info in range(flock_size):
        logging.debug("call of function sheep.__str__()")
        print(flock_of_sheep[info].__str__())
    for information in range(num_of_wolves):
        logging.debug("call of functino wolf.__str__()")
        print(wolves[information].__str__())

    for round in range(rounds):
        logging.warning("Round" + str(round) + " has begun")
        sheep_coordinates = []
        sheep_id = []
        wolves_coordinates = []
        survivors = check_alive(flock_of_sheep, flock_size)
        # --- check if the whole flock aint dead --- #
        logging.debug("call of function check_alive(flock, size)")
        if check_alive(flock_of_sheep, flock_size) == 0:
            cause = "All sheep have been eaten"
            break

        # --- move flock --- #
        print("---=== ROUND " + str(round + 1) + " ===---")
        print("Sheep alive: " + str(survivors))
        for j in range(flock_size):
            logging.debug("call of function sheep.is_alive()")
            if flock_of_sheep[j].is_alive():
                direct = flock_of_sheep[j].move_sheep()
                logging.debug("call of function sheep.move_sheep()")
                if direct == 0:  # up
                    path = "up"
                elif direct == 1:  # down
                    path = "down"
                elif direct == 2:  # left
                    path = "left"
                elif direct == 3:  # right
                    path = "right"
                print(">Sheep no." + str(flock_of_sheep[j].sheep_id) + " goes " + path + " by " + str(sheep_move_dist))
                logging.info(
                    'Sheep no' + str(flock_of_sheep[j].sheep_id) + ' goes ' + str(path) + ' by ' + str(sheep_move_dist))
                # --- save sheep positions to the list --- #
                sheep_coordinates.append(flock_of_sheep[j].get_sheep_position())
                sheep_id.append(flock_of_sheep[j].get_sheep_id())
            else:
                sheep_coordinates.append(dead_sheep_cord)
                sheep_id.append(flock_of_sheep[j].get_sheep_id())

        # --- move wolves --- #
        for k in range(num_of_wolves):
            logging.debug("call of function wolf.move_wolf(sheep_pos, sheep_id, sheep_amount)")
            index, distance = wolves[k].move_wolf(sheep_coordinates, sheep_id, survivors)
            for g in range(flock_size):
                if flock_of_sheep[g].sheep_id == index:
                    targeted_sheep = flock_of_sheep[g].sheep_id
            logging.debug("call of function sheep.is_alive()")
            if flock_of_sheep[targeted_sheep].is_alive():
                # --- eat the closest sheep if is in range of the wolf --- #
                if distance <= wolf_move_dist:
                    for g in range(flock_size):
                        if flock_of_sheep[g].sheep_id == index:
                            logging.debug("call of function sheep.is_alive()")
                            if flock_of_sheep[g].is_alive():
                                logging.debug("call of function sheep.set_alive(status)")
                                flock_of_sheep[g].set_alive(False)
                                logging.debug("call of function wolf.eat(victim_id, sheep_amount, sheep_id, sheep_pos)")
                                wolves[k].eat(flock_of_sheep[g].sheep_id, survivors, sheep_id, sheep_coordinates)
                # --- if sheep is not in range of the wolf, move wolf towards it --- #
                else:
                    logging.info('Wolf' + str(wolves[k].wolf_id) + " CHASE sheep no." + str(index))
                    print("#Wolf" + str(wolves[k].wolf_id) + " CHASE sheep no." + str(index))
                    for i in range(survivors):
                        if sheep_id[i] == index:
                            sheep_x, sheep_y = sheep_coordinates[i]
                            vector_x = (wolves[k].pos_x - sheep_x) * -1
                            vector_y = (wolves[k].pos_y - sheep_y) * -1
                            if vector_x == 0:
                                if vector_y < 0:
                                    wolves[k].pos_y -= wolves[k].wolf_move_dist
                                elif vector_y > 0:
                                    wolves[k].pos_y += wolves[k].wolf_move_dist
                            elif vector_y == 0:
                                if vector_x > 0:
                                    wolves[k].pos_x -= wolves[k].wolf_move_dist
                                elif vector_x < 0:
                                    wolves[k].pos_x += wolves[k].wolf_move_dist
                            else:  # x != 0 i y != 0
                                if vector_x > 0:
                                    wolves[k].pos_x += wolves[k].wolf_move_dist
                                    if vector_y > 0:
                                        wolves[k].pos_y += wolves[k].wolf_move_dist
                                    else:
                                        wolves[k].pos_y -= wolves[k].wolf_move_dist
                                elif vector_x < 0:
                                    wolves[k].pos_x -= wolves[k].wolf_move_dist
                                    if vector_y > 0:
                                        wolves[k].pos_y += wolves[k].wolf_move_dist
                                    else:
                                        wolves[k].pos_y -= wolves[k].wolf_move_dist
            # --- save wolves positions to the list --- #
            wolves_coordinates.append(wolves[k].get_wolf_position())

        # --- save to csv file -- #
        logging.debug("call of function save_operations.save_to_csv(round_num, am_of_sheep_alive, dirr)")
        save_operations.save_to_csv(round, survivors, directory)
        # --- save to json file --- #
        logging.debug("call of function save_operations.save_to_json(round_num, wolves_pos, sheep_pos, dirr)")
        save_operations.save_to_json(round, wolves_coordinates, sheep_coordinates, directory)

        # --- INFO --- #
        for info in range(flock_size):
            logging.debug("call of function sheep.is_alive()")
            if flock_of_sheep[info].is_alive():
                print(Fore.GREEN + flock_of_sheep[info].__str__() + Style.RESET_ALL)
        for information in range(num_of_wolves):
            print(Fore.RED + wolves[information].__str__() + Style.RESET_ALL)
        if round != rounds - 1:
            if wait:
                logging.warning("SIMULATION PAUSED")
                input("PRESS ENTER TO CONTINUE\n")
    logging.warning("END OF SIMULATION: " + str(cause))
    print("=-=-=-=-= END OF SIMULATION =-=-=-=-=")
    print(cause + "!")
