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
            is_placed = pieces[(num_piece + shift) % len(pieces)].place(grid)
        #print(num_piece, shift, pieces[(num_piece + shift) % len(pieces)].position, pieces[(num_piece + shift) % len(pieces)].rotation)
        if not is_placed or downgrade:
            if downgrade:
                downgrade = False
            if pieces[(num_piece + shift) % len(pieces)].rotate() == 0:
                if not pieces[(num_piece + shift) % len(pieces)].next_pos(grid): # Impossible to find a place
                    num_piece -= 1
                    if num_piece < 0:
                        num_piece = 0
                        shift += 1
                        if shift > len(pieces):
                            print("End")
                            return True
                    else:
                        pieces[(num_piece + shift) % len(pieces)].remove(grid)
                        downgrade = True


        else:
            num_piece += 1
            if num_piece <= 1:
                print(grid)
                print(num_piece, shift, pieces[(num_piece + shift) % len(pieces)].position, pieces[(num_piece + shift) % len(pieces)].rotation)
            if (num_piece + shift) % len(pieces) == len(pieces):
                print("---------------")
                print(grid)



def main():
    grid = Grid(DAY, MONTH)
    #print(grid)

    pieces = [
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
    #piece[4].places(grid, 2, 2)
    #piece[1].rotate()
    #piece[1].places(grid)
    #print(grid)

    solve(grid, pieces)





if __name__ == "__main__":
    main()
