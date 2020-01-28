"""
Christopher Mendez & Rupika Dikkala
Programming Assignment 2
15 Puzzle
CS 531 - AI
February 3, 2020
***********************************
"""

import puzzle as p
import random as rand
from copy import deepcopy


def main():
    shuffles = [10, 20, 30, 40, 50]
    final = str([[0,  1,  2,  3],
                 [4,  5,  6,  7],
                 [8,  9, 10, 11],
                 [12, 13, 14, 15]])

    for i in range(0,1):
        
        #print("\nSHUFFLE COUNT: {}".format(i))
            for j in range(0, 10):
                puzzle = scramble(10, final)
                print(puzzle)

                p.recursive_best_first_h1(puzzle, final)
                p.recursive_best_first_h2(puzzle, final)
                p.iterative_deepening_astar_h1(puzzle, final)
                p.iterative_deepening_astar_h2(puzzle, final)


# function that randomly shuffles the
# puzzle board, param = # of shuffles
def scramble(shuffle, board):
    # coordinates of the blank space
    x, y = 0, 0
    moves = []

    # shuffles the board for param
    # number of times
    for m in range(0, shuffle):
        # if valid move, add to moves array
        if x > 0:
            moves.append("up")
        if x < 3:
            moves.append("down")
        if y > 0:
            moves.append("left")
        if y < 3:
            moves.append("right")

        # now pick a move to perform
        if len(moves) > 1:
            # pick random move from array
            move = rand.choice(moves)
            # catch shuffled board and new blank space coordinates
            board, x, y = deepcopy(parse_move(move, board, x, y))
        else:
            board, x, y = deepcopy(parse_move(moves[0], board, x, y))

        moves.clear()

    return board


# performs the move on the board
def parse_move(move, board, x, y):
    # parse the string into int
    current_board = eval(board)

    # translating the move on the board
    if move == "up":
        current_board[x][y], current_board[x - 1][y] = current_board[x - 1][y], current_board[x][y]  #move up
        x = x - 1
    if move == "down":
        current_board[x][y], current_board[x + 1][y] = current_board[x + 1][y], current_board[x][y]   #move down
        x = x + 1
    if move == "left":
        current_board[x][y], current_board[x][y - 1] = current_board[x][y - 1], current_board[x][y]   #move left
        y = y - 1
    if move == "right":
        current_board[x][y], current_board[x][y + 1] = current_board[x][y + 1], current_board[x][y]   #move right
        y = y + 1

    # return shuffled board and new coordinates of
    # the blank space
    return str(current_board), x, y


if __name__ == "__main__":
    main()

