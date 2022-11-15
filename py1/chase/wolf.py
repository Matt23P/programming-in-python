import numpy
from colorama import Fore, Back, Style
import logging


class Wolf:
    def __init__(self, num, dist, board_a, board_b, x, y):
        self.pos_x = x
        self.pos_y = y
        self.sheep_eaten = 0
        self.wolf_id = num
        self.board_a = board_a
        self.board_b = board_b
        self.wolf_move_dist = dist

    def __str__(self):
        logging.debug("function wolf.__str__() ret: " + "Wolf" + str(
            self.wolf_id) + ": [" + "%.3f" % self.pos_x + " ; " + "%.3f" % self.pos_y + "] sheep eaten: " + str(
            self.sheep_eaten))
        return "Wolf" + str(
            self.wolf_id) + ": [" + "%.3f" % self.pos_x + " ; " + "%.3f" % self.pos_y + "] sheep eaten: " + str(
            self.sheep_eaten)

    def find_the_nearest(self, sheep_pos, sheep_id, sheep_amount):
        last_min = numpy.sqrt(self.board_a ** 2 + self.board_b ** 2)
        identity = 0
        for i in range(sheep_amount):
            sheep_x, sheep_y = sheep_pos[i]
            # --- wolf get the full list of sheep (with dead ones), we look for the nearest among alive only --- #
            if sheep_x is not None and sheep_y is not None:
                x = self.pos_x - sheep_x
                y = self.pos_y - sheep_y
                distance = numpy.sqrt(x ** 2 + y ** 2)
                if distance < last_min:
                    last_min = distance
                    identity = sheep_id[i]
        logging.debug("function wolf.find_the_nearest() ret: " + str(last_min) + ", " + str(identity))
        return last_min, identity

    def eat(self, victim_id, sheep_amount, sheep_id, sheep_pos):
        self.sheep_eaten += 1
        print(Fore.RED + Back.BLACK + "#Wolf" + str(self.wolf_id) + " EATS sheep no." + str(victim_id) + Style.RESET_ALL)
        logging.info('Wolf' + str(self.wolf_id) + ' EATS sheep no.' + str(victim_id))
        for i in range(sheep_amount):
            if sheep_id[i] == victim_id:
                self.pos_x, self.pos_y = sheep_pos[i]

    def get_wolf_position(self):
        logging.debug("function wolf.get_wolf_position() ret: " + str(self.pos_x) + ", " + str(self.pos_y))
        return self.pos_x, self.pos_y

    def move_wolf(self, sheep_pos, sheep_id, sheep_amount):
        logging.debug("call of function wolf.find_the_nearest(sheep_pos, sheep_id, sheep_amount)")
        distance, victim_id = Wolf.find_the_nearest(self, sheep_pos, sheep_id, sheep_amount)
        logging.debug("function wolf.move_wolf() ret: " + str(victim_id) + ", " + str(distance))
        return victim_id, distance
