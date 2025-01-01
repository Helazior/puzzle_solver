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

    def __init__(self, frame, number):
        self.frame = frame
        self.number = number

    def check_collision_with_grid(self, grid):
        x, y = self.position
        for j, row in enumerate(self.frame[self.rotation]):
            for i, cell in enumerate(row):
                if cell:
                    if x + i < 0 or x + i > len(grid.matrix[0]) or y + j < 0 or y + j > len(grid.matrix):
                        print(f'Out of grid boundaries: {x + i}, {y + j}')
                        return True  # Out of grid boundaries
                    print(f'Collision with grid: {x + i}, {y + j}')
                    if grid.matrix[y + j][x + i] != 0:
                        print(f'Collision with another piece: {x + i}, {y + j}')
                        return True  # Collision with another piece
        return False

    def place(self, grid, x=-1, y=-1):
        if x < 0:
            x, y = self.position
        else:
            self.position = [x, y]

        if self.check_collision_with_grid(grid):
            return False

        for j, row in enumerate(self.frame[self.rotation]):
            for i, cell in enumerate(row):
                if cell:
                    grid.matrix[y + j][x + i] = self.number + 1
        return True

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.frame)
