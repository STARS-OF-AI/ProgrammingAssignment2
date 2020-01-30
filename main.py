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
from pandas import DataFrame
from os import path


def main():
    shuffles = [10, 20, 30, 40, 50]
    final = str([[0,  1,  2,  3],
                 [4,  5,  6,  7],
                 [8,  9, 10, 11],
                 [12, 13, 14, 15]])

    # initializes the algs dictionary
    # with all the required values
    algs = [{} for i in range(4)]
    for alg in algs:
        a = {"Heuristic Time": [], "Total Time": [], "Expanded Nodes": [], "Solution Length": [], "Misplaced Squares": []}
        alg.update(a)

    for i in shuffles:
        # appends border for data
        append_border(i, algs)

        # main for loop with n=10 runs
        for j in range(0, 10):
            puzzle = scramble(i, final)
            front = [[p.heuristic_1(puzzle), puzzle]]
            r_path = front[0]

            # running the RBFS search
            rbfs_h1(front, final, r_path, algs[0])
            rbfs_h2(front, final, r_path, algs[1])

            # running the A* search
            astar_h1(puzzle, final, algs[2])
            astar_h2(puzzle, final, algs[-1])

        # appending to data frames
        r1 = DataFrame(algs[0], columns=['Heuristic Time', 'Total Time', 'Expanded Nodes', 'Solution Length', 'Misplaced Squares'])
        r2 = DataFrame(algs[1], columns=['Heuristic Time', 'Total Time', 'Expanded Nodes', 'Solution Length', 'Misplaced Squares'])
        a1 = DataFrame(algs[2], columns=['Heuristic Time', 'Total Time', 'Expanded Nodes', 'Solution Length', 'Misplaced Squares'])
        a2 = DataFrame(algs[-1], columns=['Heuristic Time', 'Total Time', 'Expanded Nodes', 'Solution Length', 'Misplaced Squares'])
        print('m of ', i)
    # function for writing to csv
    write_to_csv(r1, r2, a1, a2)

    print(r1)
    print(r2)
    print(a1)
    print(a2)


# run the RBFS search algorithm for heuristic 1
def rbfs_h1(front, final, r_path, rbfs1):
    # catch time, total time, num expanded nodes, soln length
    t, total_t, nodes, length, ms = p.RBFS_H1(front, final, r_path)

    # append the values to the dictionary
    rbfs1["Heuristic Time"].append(t)
    rbfs1["Total Time"].append(total_t)
    rbfs1["Expanded Nodes"].append(nodes)
    rbfs1["Solution Length"].append(length)
    rbfs1["Misplaced Squares"].append(ms)


# run the RBFS search algorithm for heuristic 2
def rbfs_h2(front, final, r_path, rbfs2):
    t, total_t, nodes, length, ms = p.RBFS_H2(front, final, r_path)

    # append the values to the dictionary
    rbfs2["Heuristic Time"].append(t)
    rbfs2["Total Time"].append(total_t)
    rbfs2["Expanded Nodes"].append(nodes)
    rbfs2["Solution Length"].append(length)
    rbfs2["Misplaced Squares"].append(ms)


# run the A* search algorithm for heuristic 1
def astar_h1(puzzle, final, astar1):
    t, total_t, nodes, length, ms = p.iterative_deepening_astar_h1(puzzle, final)

    # append the values to the dictionary
    astar1["Heuristic Time"].append(t)
    astar1["Total Time"].append(total_t)
    astar1["Expanded Nodes"].append(nodes)
    astar1["Solution Length"].append(length)
    astar1["Misplaced Squares"].append(ms)


# run the A* search algorithm for heuristic 2
def astar_h2(puzzle, final, astar2):
    t, total_t, nodes, length, ms = p.iterative_deepening_astar_h2(puzzle, final)

    # append the values to the dictionary
    astar2["Heuristic Time"].append(t)
    astar2["Total Time"].append(total_t)
    astar2["Expanded Nodes"].append(nodes)
    astar2["Solution Length"].append(length)
    astar2["Misplaced Squares"].append(ms)


# function for writing data to csv
def write_to_csv(r1, r2, a1, a2):
    alg = [r1, r2, a1, a2]
    names = ["rbfs_h1.csv", "rbsf_h2.csv", "astar_h1.csv", "astar_h2.csv"]

    for n in names:
        # get the element from alg
        a = alg[names.index(n)]

        # append to path
        if path.exists(n):
            a.to_csv(n, mode='a', header=False)
        # create a new file
        else:
            a.to_csv(n)


# add a border for data separation in csv
def append_border(i, algs):
    for a in algs:
        a["Heuristic Time"].append("M = {}".format(i))
        a["Total Time"].append("M = {}".format(i))
        a["Expanded Nodes"].append("M = {}".format(i))
        a["Solution Length"].append("M = {}".format(i))
        a["Misplaced Squares"].append("M = {}".format(i))

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

