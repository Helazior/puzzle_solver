from config import DAY, MONTH
from piece import *
from grid import Grid


def main():
    grid = Grid(DAY, MONTH)
    #print(grid)

    piece = [
        Piece(get_permutations(
            [[1, 1, 1, 1],
             [0, 1, 0, 0]]),
            0),
        Piece(get_permutations(
            [[1, 1, 1],
             [1, 1, 1]]),
            1),
        Piece(get_permutations(
            [[0, 1, 1],
             [1, 1, 1]]),
            2),
        Piece(get_permutations(
            [[0, 1, 1],
             [1, 1, 1]]),
            3),
        Piece(get_permutations(
            [[0, 0, 1, 1],
             [1, 1, 1, 0]]),
            4),
        Piece(get_permutations(
            [[1, 0, 1],
             [1, 1, 1]]),
            5),
        Piece(get_permutations(
            [[0, 0, 0, 1],
             [1, 1, 1, 1]]),
            6),
        Piece(get_permutations(
            [[0, 1, 1],
             [0, 1, 0],
             [1, 1, 0]]),
            7),
        Piece(get_permutations(
            [[1, 0, 0],
             [1, 0, 0],
             [1, 1, 1]]),
            8),
    ]
    piece[1].rotate()
    piece[1].place(grid)
    piece[4].place(grid, 2, 0)

    print(grid)


if __name__ == "__main__":
    main()
