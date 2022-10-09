import random
import direction


def check_move(pos_x, pos_y, board_x, board_y, direct, sheep_move_dist):
    if direct == 0:  # up
        y = pos_y + sheep_move_dist
        if y > board_y:
            return False
    if direct == 1:  # down
        y = pos_y - sheep_move_dist
        if y < -board_y:
            return False
    if direct == 2:  # left
        x = pos_x - sheep_move_dist
        if x < -board_x:
            return False
    if direct == 3:  # right
        x = pos_x + sheep_move_dist
        if x > board_x:
            return False
    return True


class Sheep:
    def __init__(self, num, distance, board_x, board_y):
        self.pos_x = random.randint(-board_x, board_x)
        self.pos_y = random.randint(-board_y, board_y)
        self.sheep_id = num
        self.sheep_move_dist = distance
        self.board_x = board_x
        self.board_y = board_y
        self.alive = True

    def __str__(self):
        return "Sheep no." + str(self.sheep_id) + ": [" + "%.3f" % self.pos_x + " ; " + "%.3f" % self.pos_y + "]"

    def get_sheep_id(self):
        return self.sheep_id

    def set_alive(self, status):
        self.alive = status

    def is_alive(self):
        return self.alive

    def get_sheep_position(self):
        return self.pos_x, self.pos_y

    def move_sheep(self):
        while True:
            # --- if chosen direction is impossible to perform, sheep will pick other direction --- #
            direct = direction.get_direction()
            if check_move(self.pos_x, self.pos_y, self.board_x, self.board_y, direct, self.sheep_move_dist):
                break
        if direct == 0:  # up
            self.pos_y += self.sheep_move_dist
            return 0
        if direct == 1:  # down
            self.pos_y -= self.sheep_move_dist
            return 1
        if direct == 2:  # left
            self.pos_x -= self.sheep_move_dist
            return 2
        if direct == 3:  # right
            self.pos_x += self.sheep_move_dist
            return 3
