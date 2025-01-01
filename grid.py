from piece import Piece, Colors


class Grid:
    """Grid of the puzzle"""

    def __init__(self, day, month):
        self.matrix = [[0] * 7 for _ in range(7)]
        self.matrix[0][6] = -1
        self.matrix[1][6] = -1
        self.matrix[6][4] = -1
        self.matrix[6][5] = -1
        self.matrix[6][6] = -1

        self.matrix[6][3] = -2
        self.matrix[0][5] = -2

    def __str__(self):
        grid_str = f'⬛' * 9 + '\n'
        for row in self.matrix:
            grid_str += f'⬛'
            for cell in row:
                if cell == 0:
                    grid_str += f'  '
                elif cell == -1:
                    grid_str += f'⬛'
                elif cell == -2:
                    grid_str += f'X '
                elif cell > 0:
                    grid_str += f"{Colors[cell - 1]}⬛{Colors.RESET}"
            grid_str += '⬛\n'
        grid_str += f'⬛' * 9 + '\n'
        return grid_str

    def collision(self, x, y):
        """Test if the piece collides with another piece"""
        return self.matrix[y][x] != 0
