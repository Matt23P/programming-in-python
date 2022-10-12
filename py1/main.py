import sheep
import wolf
import options
import json
from colorama import Fore, Style
import csv
import args


def check_alive(flock, size):
    alive = 0
    for h in range(size):
        if flock[h].is_alive():
            alive += 1
    return alive


def save_to_csv(round_num, am_of_sheep_alive):
    sur = [am_of_sheep_alive]
    rou = [round_num + 1]
    if round == 0:
        with open('output/alive.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(header_csv)
            writer.writerow(rou + sur)
    else:
        with open('output/alive.csv', 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(rou + sur)


def save_to_json(round_num, wolves_pos, sheep_pos):
    dictionary = {
        "round_no": round_num,
        "wolf_pos": wolves_pos,
        "sheep_pos": sheep_pos
    }
    json_dictionary = json.dumps(dictionary, indent=3)
    if round == 0:
        with open('output/pos.json', 'w', newline='') as json_file:
            json_file.write(json_dictionary)
    else:
        with open('output/pos.json', 'a', newline='') as json_file:
            json_file.write(json_dictionary)


if __name__ == '__main__':
    rounds, sheep_move_dist, flock_size, num_of_wolves, wolf_move_dist, board_a, board_b = options.menu()

    dead_sheep_cord = [None, None]
    header_csv = ["Round", "Sheep alive"]
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
        survivors = check_alive(flock_of_sheep, flock_size)
        # --- check if the whole flock aint dead --- #
        if check_alive(flock_of_sheep, flock_size) == 0:
            cause = "All sheep have been eaten"
            break

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
                print(">Sheep no." + str(flock_of_sheep[j].sheep_id) + " goes " + path + " by " + str(sheep_move_dist))
                # --- save sheep positions to the list --- #
                sheep_coordinates.append(flock_of_sheep[j].get_sheep_position())
                sheep_id.append(flock_of_sheep[j].get_sheep_id())
            else:
                sheep_coordinates.append(dead_sheep_cord)
                sheep_id.append(flock_of_sheep[j].get_sheep_id())

        # --- move wolves --- #
        for k in range(num_of_wolves):
            index, distance = wolves[k].move_wolf(sheep_coordinates, sheep_id, survivors)
            for g in range(flock_size):
                if flock_of_sheep[g].sheep_id == index:
                    targeted_sheep = flock_of_sheep[g].sheep_id
            if flock_of_sheep[targeted_sheep].is_alive():
                # --- eat the closest sheep if is in range of the wolf --- #
                if distance <= wolf_move_dist:
                    for g in range(flock_size):
                        if flock_of_sheep[g].sheep_id == index:
                            if flock_of_sheep[g].is_alive():
                                flock_of_sheep[g].set_alive(False)
                                wolves[k].eat(flock_of_sheep[g].sheep_id, survivors, sheep_id, sheep_coordinates)
                # --- if sheep is not in range of the wolf, move wolf towards it --- #
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

        # --- save to csv file -- #
        save_to_csv(round, survivors)
        # --- save to json file --- #
        save_to_json(round, wolves_coordinates, sheep_coordinates)

        # --- INFO --- #
        for info in range(flock_size):
            if flock_of_sheep[info].is_alive():
                print(Fore.GREEN + flock_of_sheep[info].__str__() + Style.RESET_ALL)
        for information in range(num_of_wolves):
            print(Fore.RED + wolves[information].__str__() + Style.RESET_ALL)

    print("=-=-=-=-= END OF SIMULATION =-=-=-=-=")
    print(cause + "!")
