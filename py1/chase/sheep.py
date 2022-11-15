import random
import logging


class Sheep:
    def get_direction(self):
        # --- get the random integer from 0 to 3 --- #
        direction = random.randint(0, 3)
        logging.debug('function get_direction() ret:' + str(direction))
        return int(direction)

    def check_move(self, pos_x, pos_y, board_x, board_y, direct, sheep_move_dist):
        if direct == 0:  # up
            y = pos_y + sheep_move_dist
            if y > board_y:
                logging.debug('function check_move() ret: False')
                return False
        if direct == 1:  # down
            y = pos_y - sheep_move_dist
            if y < -board_y:
                logging.debug('function check_move() ret: False')
                return False
        if direct == 2:  # left
            x = pos_x - sheep_move_dist
            if x < -board_x:
                logging.debug('function check_move() ret: False')
                return False
        if direct == 3:  # right
            x = pos_x + sheep_move_dist
            if x > board_x:
                logging.debug('function check_move() ret: False')
                return False
        logging.debug('function check_move() ret: True')
        return True

    def __init__(self, num, distance, board_x, board_y):
        self.pos_x = random.randint(-board_x, board_x)
        self.pos_y = random.randint(-board_y, board_y)
        self.sheep_id = num
        self.sheep_move_dist = distance
        self.board_x = board_x
        self.board_y = board_y
        self.alive = True

    def __str__(self):
        logging.debug("function sheep.__str__() ret: " + "Sheep no." + str(
            self.sheep_id) + ": [" + "%.3f" % self.pos_x + " ; " + "%.3f" % self.pos_y + "]")
        return "Sheep no." + str(self.sheep_id) + ": [" + "%.3f" % self.pos_x + " ; " + "%.3f" % self.pos_y + "]"

    def get_sheep_id(self):
        logging.debug("function sheep.get_sheep_id() ret: " + str(self.sheep_id))
        return self.sheep_id

    def set_alive(self, status):
        self.alive = status

    def is_alive(self):
        logging.debug("function sheep.is_alive() ret: " + str(self.alive))
        return self.alive

    def get_sheep_position(self):
        logging.debug("function sheep.get_sheep_position() ret: " + str(self.pos_x) + ", " + str(self.pos_y))
        return self.pos_x, self.pos_y

    def move_sheep(self):
        while True:
            # --- if chosen direction is impossible to perform, sheep will pick other direction --- #
            logging.debug("call of function get_direction()")
            direct = self.get_direction()
            if self.check_move(self.pos_x, self.pos_y, self.board_x, self.board_y, direct, self.sheep_move_dist):
                break
        if direct == 0:  # up
            self.pos_y += self.sheep_move_dist
            logging.debug("function sheep.move_sheep() ret: 0")
            return 0
        if direct == 1:  # down
            self.pos_y -= self.sheep_move_dist
            logging.debug("function sheep.move_sheep() ret: 1")
            return 1
        if direct == 2:  # left
            self.pos_x -= self.sheep_move_dist
            logging.debug("function sheep.move_sheep() ret: 2")
            return 2
        if direct == 3:  # right
            self.pos_x += self.sheep_move_dist
            logging.debug("function sheep.move_sheep() ret: 3")
            return 3
