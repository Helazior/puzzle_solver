from config import DAY, MONTH
from piece import *
from grid import Grid


def solve(grid, pieces):
    num_piece = 0
    shift = 0
    downgrade = False
    is_placed = False

    while True:
        #print(grid)
        if not downgrade:
            is_placed = pieces[num_piece].place(grid)
        #print(num_piece, shift, pieces[num_piece].position, pieces[num_piece].rotation)
        if not is_placed or downgrade:
            if downgrade:
                downgrade = False
            if pieces[num_piece].rotate() == 0:
                if not pieces[num_piece].next_pos(grid):  # Impossible to find a place
                    num_piece -= 1
                    if num_piece < 0:
                        print("End")
                        return True
                    else:
                        pieces[num_piece].remove(grid)
                        #print(num_piece, shift, pieces[num_piece].position, pieces[num_piece].rotation)
                        #print(grid)
                        downgrade = True
        else:
            if num_piece == 1:
                download = pieces[0].position[0] / (grid.len_x * grid.len_x - 5) + pieces[0].position[1] / grid.len_y + pieces[0].rotation / (len(pieces[0].frame) * (grid.len_x * grid.len_x - 5))
                download += ((pieces[1].position[0] / (grid.len_x * grid.len_x - 5) + pieces[1].position[1] / grid.len_y + pieces[1].rotation / (len(pieces[0].frame) * (grid.len_x * grid.len_x - 5)))) / (grid.len_x * grid.len_x - 5)
                download = int(download * 1000 + 0.5) / 10
                print(f"\r{download}%\r", end='')
                #print(num_piece, shift, pieces[num_piece].position, pieces[num_piece].rotation)
                #print(grid)
                #input()

            num_piece += 1
            if num_piece >= len(pieces):
                print(grid)
                num_piece -= 1
                pieces[num_piece].remove(grid)
                downgrade = True


def main():
    grid = Grid(DAY, MONTH)
    #print(grid)

    pieces = [
        Piece(get_permutations(
            [[1, 1, 1],
             [1, 1, 1]]),
            0),
        Piece(get_permutations(
            [[1, 0, 0],
             [1, 0, 0],
             [1, 1, 1]]),
            1),
        Piece(get_permutations(
            [[1, 0, 1],
             [1, 1, 1]]),
            2),
        Piece(get_permutations(
            [[0, 0, 0, 1],
             [1, 1, 1, 1]]),
            3),
        Piece(get_permutations(
            [[1, 1, 1, 1],
             [0, 1, 0, 0]]),
            4),
        Piece(get_permutations(
            [[0, 1, 1],
             [1, 1, 1]]),
            5),
        Piece(get_permutations(
            [[0, 0, 1, 1],
             [1, 1, 1, 0]]),
            6),
        Piece(get_permutations(
            [[0, 1, 1],
             [0, 1, 0],
             [1, 1, 0]]),
            7),

    ]
    #piece[4].places(grid, 2, 2)
    #piece[1].rotate()
    #piece[1].places(grid)
    #print(grid)

    #pieces[0].rotation = 4
    #pieces[1].position = [2, 2]
    #pieces[1].rotation = 1
    #pieces[2].position = [1, 1]
    solve(grid, pieces)


if __name__ == "__main__":
    main()
