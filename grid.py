from piece import Piece, Colors


class Grid:
    """Grid of the puzzle"""

    def __init__(self, day, month):
        self.matrix = [[0] * 7 for _ in range(7)]
        self.matrix[0][6] = -1
        self.matrix[1][6] = -1
        self.matrix[6][3] = -1
        self.matrix[6][4] = -1
        self.matrix[6][5] = -1
        self.matrix[6][6] = -1
        # TODO faire avec les dates
        if not (0 <= month <= 12 and 0 <= day <= 31):
            print('Invalid date')
            exit(1)

        self.day = day
        self.month = month

        i = (month - 1) % 6
        j = (month - 1) // 6
        self.matrix[j][i] = -3
        i = (day - 1) % 7
        j = (day - 1) // 7
        self.matrix[j + 2][i] = -2
        #self.matrix[1][0] = -2
        #self.matrix[3][5] = -2

        self.len_x = len(self.matrix[0])
        self.len_y = len(self.matrix)

    def __str__(self):
        grid_str = f'░░' * 9 + '\n'
        for row in self.matrix:
            grid_str += f'░░'
            for cell in row:
                if cell == 0:
                    grid_str += f'  '
                elif cell == -1:
                    grid_str += f'░░'
                elif cell == -2:
                    grid_str += f'{self.day}' + ' ' * (2 - len(str(self.day)))
                elif cell == -3:
                    grid_str += f'{self.month}' + ' ' * (2 - len(str(self.month)))
                elif cell > 0:
                    grid_str += f"{Colors[cell - 1]}██{Colors.RESET}"
            grid_str += '░░\n'
        grid_str += f'░░' * 9 + '\n'
        return grid_str

    def collision(self, x, y):
        """Test if the piece collides with another piece"""
        return self.matrix[y][x] != 0
