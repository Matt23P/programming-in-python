import os
import csv
import json

header_csv = ["Round", "Sheep alive"]


def save_to_csv(round_num, am_of_sheep_alive, dirr):
    sur = [am_of_sheep_alive]
    rou = [round_num + 1]
    path_to_file = str(dirr) + "/alive.csv"
    if os.path.exists(dirr):
        if round == 0:
            with open(path_to_file, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(header_csv)
                writer.writerow(rou + sur)
        else:
            with open(path_to_file, 'a', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(rou + sur)
    else:
        os.mkdir(dirr)
        with open(path_to_file, 'x', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(rou + sur)


def save_to_json(round_num, wolves_pos, sheep_pos, dirr):
    dictionary = {
        "round_no": round_num,
        "wolf_pos": wolves_pos,
        "sheep_pos": sheep_pos
    }
    json_dictionary = json.dumps(dictionary, indent=3)
    path_to_file = str(dirr) + "/pos.json"
    if os.path.exists(dirr):
        if round == 0:
            with open(path_to_file, 'w', newline='') as json_file:
                json_file.write(json_dictionary)
        else:
            with open(path_to_file, 'a', newline='') as json_file:
                json_file.write(json_dictionary)
    else:
        os.mkdir(dirr)
        with open(path_to_file, 'x', newline='') as json_file:
            json_file.write(json_dictionary)
