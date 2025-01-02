from collections import namedtuple

Color = namedtuple(
    'Color',
    ['RED', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN', 'ORANGE', 'PURPLE', 'RESET'])

Colors = Color(
    RED="\033[91m",
    GREEN="\033[92m",
    YELLOW="\033[93m",
    BLUE="\033[94m",
    MAGENTA="\033[95m",
    CYAN="\033[96m",
    ORANGE="\033[38;5;214m",  # Changed from BLACK to ORANGE
    PURPLE="\033[38;5;57m",
    RESET="\033[0m"
)


def get_permutations(matrix):
    def rotate_90(current_matrix):
        return [list(row) for row in zip(*current_matrix[::-1])]

    def reflect(current_matrix):
        return [row[::-1] for row in current_matrix]

    permutations = []
    current = matrix
    for _ in range(4):
        permutations.append(current)
        permutations.append(reflect(current))
        current = rotate_90(current)
    return remove_duplicate_frames(permutations)


def remove_duplicate_frames(matrices):
    unique_frames = []
    for frame in matrices:
        if frame not in unique_frames:
            unique_frames.append(frame)
    return unique_frames


class Piece:
    """Piece to place on the puzzle"""

    rotation = 0
    position = [0, 0]
    placed = False

    def __init__(self, frame, number):
        self.frame = frame
        self.number = number

    def check_collision_with_grid(self, grid):
        x, y = self.position
        len_piece_x = len(self.frame[self.rotation][0])
        len_piece_y = len(self.frame[self.rotation])

        if x + len_piece_x > grid.len_x or y + len_piece_y > grid.len_y:
            #print(f'Out of grid boundaries: {x + i}, {y + j}')
            return True  # Out of grid boundaries

        lock_up = False
        change_lock_up = True

        for j, row in enumerate(self.frame[self.rotation]):
            for i, cell in enumerate(row):
                if cell == 1:
                    if grid.matrix[y + j][x + i] != 0:
                        #print(f'Collision with another piece: {x + i}, {y + j}')
                        return True  # Collision with another piece
                else:
                    if grid.matrix[y + j][x + i] == 0:  # Empty cell in the grid
                        nb_wall = 0
                        for k in range(-1, 2, 2):
                            if 0 <= i + k < len_piece_x:  # Next cell is in the piece
                                nb_wall += 1
                            else:  # Next cell is out of the piece
                                if 0 <= x + i + k < grid.len_x:  # Next cell is in the grid
                                    if grid.matrix[y + j][x + i + k] != 0:  # Next cell is not free in the grid
                                        nb_wall += 1
                                else:  # Next cell is out of the grid
                                    nb_wall += 1

                        for l in range(-1, 2, 2):
                            if 0 <= j + l < len_piece_y:  # Next cell is in the piece
                                nb_wall += 1
                            else:  # Next cell is out of the piece
                                if 0 <= 0 <= y + j + l < grid.len_y:  # Next cell is in the grid
                                    if grid.matrix[y + j + l][x + i] != 0:  # Next cell is not free in the grid
                                        nb_wall += 1
                                else:  # Next cell is out of the grid
                                    nb_wall += 1

                        if change_lock_up:
                            if nb_wall == 4:
                                lock_up = True
                            else:
                                lock_up = False
                                change_lock_up = False
        if lock_up:
            return True
        return False

    def place(self, grid, x=-1, y=-1):
        if self.placed:
            print('Piece already placed')
            return False

        if x < 0:
            x, y = self.position
        else:
            self.position = [x, y]

        if self.check_collision_with_grid(grid):
            return False

        for j, row in enumerate(self.frame[self.rotation]):
            for i, cell in enumerate(row):
                if cell == 1:
                    grid.matrix[y + j][x + i] = self.number + 1
        self.placed = True
        return True

    def remove(self, grid):
        if not self.placed:
            return False
        x, y = self.position
        for j, row in enumerate(self.frame[self.rotation]):
            for i, cell in enumerate(row):
                if cell == 1:
                    if grid.matrix[y + j][x + i] != self.number + 1:
                        print(
                            f'Error removing piece: {x + i}, {y + j} : {grid.matrix[y + j][x + i]} and {self.number + 1}')
                        input()
                    grid.matrix[y + j][x + i] = 0

        self.placed = False
        #print('Piece removed')
        return True

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.frame)
        return self.rotation

    def next_pos(self, grid):
        x, y = self.position
        x += 1
        if x + len(self.frame[self.rotation][0]) > len(grid.matrix[0]):
            x = 0
            y += 1
        if y + len(self.frame[self.rotation]) > len(grid.matrix):
            self.position = [0, 0]
            return False
        self.position = [x, y]
        return True
