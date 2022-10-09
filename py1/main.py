import time
import sheep
import wolf
import options
import json
from colorama import Fore, Back, Style


def check_alive(flock_of_sheep):
    survivors = 0
    for i in range(flock_size):
        if flock_of_sheep[i].is_alive():
            survivors += 1
    return survivors


if __name__ == '__main__':
    rounds, sheep_move_dist, flock_size, num_of_wolves, wolf_move_dist, board_a, board_b = options.menu()

    flock_of_sheep = []
    wolves = []
    cause = ""
    x, y = 0.0, 0.0

    for i in range(flock_size):
        flock_of_sheep.append(sheep.Sheep(i, sheep_move_dist, board_a, board_b))
    for j in range(num_of_wolves):
        wolves.append(wolf.Wolf(j, wolf_move_dist, board_a, board_b, x + j, y + j))

    print("---=== START POSITIONS OF ANIMALS ===---")
    for info in range(flock_size):
        print(flock_of_sheep[info].__str__())
    for information in range(num_of_wolves):
        print(wolves[information].__str__())

    for round in range(rounds):
        sheep_coordinates = []
        sheep_id = []
        wolves_coordinates = []
        survivors = check_alive(flock_of_sheep)
        if check_alive(flock_of_sheep) == 0:
            cause = "All sheep have been eaten"
            break
        if rounds <= 1:
            cause = str(rounds) + "round has elapsed"
        else:
            cause = str(rounds) + "rounds have elapsed"
        # --- move flock --- #
        print("---=== ROUND " + str(round + 1) + " ===---")
        print("Sheep alive: " + str(survivors))
        for j in range(flock_size):
            if flock_of_sheep[j].is_alive():
                direct = flock_of_sheep[j].move_sheep()
                if direct == 0:  # up
                    path = "up"
                elif direct == 1:  # down
                    path = "down"
                elif direct == 2:  # left
                    path = "left"
                elif direct == 3:  # right
                    path = "right"
                # time.sleep(1)
                print(">Sheep no." + str(flock_of_sheep[j].sheep_id) + " goes " + path + " by " + str(sheep_move_dist))
                # --- save sheep positions to the list --- #
                sheep_coordinates.append(flock_of_sheep[j].get_sheep_position())
                sheep_id.append(flock_of_sheep[j].get_sheep_id())
        # time.sleep(1)
        # --- move wolves --- #
        for k in range(num_of_wolves):
            index, distance = wolves[k].move_wolf(sheep_coordinates, sheep_id, survivors)
            for g in range(flock_size):
                if flock_of_sheep[g].sheep_id == index:
                    targeted_sheep = flock_of_sheep[g].sheep_id
            if flock_of_sheep[targeted_sheep].is_alive():
                if distance <= wolf_move_dist:
                    for g in range(flock_size):
                        if flock_of_sheep[g].sheep_id == index:
                            if flock_of_sheep[g].is_alive():
                                flock_of_sheep[g].set_alive(False)
                                wolves[k].eat(flock_of_sheep[g].sheep_id, survivors, sheep_id, sheep_coordinates)

                else:
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

        # --- INFO --- #
        for info in range(flock_size):
            if flock_of_sheep[info].is_alive():
                print(Fore.GREEN + flock_of_sheep[info].__str__() + Style.RESET_ALL)
        for information in range(num_of_wolves):
            print(Fore.RED + wolves[information].__str__() + Style.RESET_ALL)

    print("=-=-=-=-= END OF SIMULATION =-=-=-=-=")
    print(cause + "!")
