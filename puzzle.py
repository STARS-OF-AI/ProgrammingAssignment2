"""
Christopher Mendez & Rupika Dikkala
Programming Assignment 2
15 Puzzle
CS 531 - AI
February 3, 2020
***********************************
This file contains the Solver class which
holds the path/time information for each
algorithm. Also contains the implementation
of the A* H1, A* H2, RBFS-H1, RBFS-H2 algorithms.
"""


import random
from datetime import datetime

class Solver:
  def __init__(self, path, front, end):
    self.path = path
    self.front = front
    self.end = end
    self.depth = 0
    self.expanded_nodes = 0
    self.Htime = 0
    self.Ttime = 0
    self.expanded = []


def actualRecursionH1(solver):
    h1 = []
    i = 0
    f_limit = 40
    
    if solver.front:
        solver.path = solver.front[i]
        h1.append(solver.path[0])
        solver.front = solver.front[:i] + solver.front[i+1:]
        endnode = solver.path[-1]
        if endnode == solver.end: return
        if endnode in solver.expanded: return
        for k in moves(endnode):
            if k in solver.expanded: continue
            star_time = datetime.now()
            if (heuristic_1(k)+ solver.depth) > f_limit:
                solver.Htime += millis(star_time)
                #print('flimit reached h1', solver.depth)
                solver.depth = 0
                continue
            star_time = datetime.now()
            newpath = [solver.path[0] + heuristic_1(k) - heuristic_1(endnode)] + solver.path[1:] + [k]
            solver.Htime += millis(star_time)
            solver.front.append(newpath)
            solver.expanded.append(endnode)
        solver.expanded_nodes += 1
        solver.depth+=1
        actualRecursionH1(solver)
    

def RBFS_H1(front, end, path):
    solver1 = Solver(path, front, end)
    stime = datetime.now()
    actualRecursionH1(solver1)
    solver1.Ttime += millis(stime)
    #print('solver', solver1)
    #path.pop(0)
    print("\nRBFS With H1")
    print("Number of expanded nodes:",solver1.expanded_nodes)
    y = 0
   # print("front ", solver1.path)
    for x in solver1.path:
        y += 1
    print("Solution length: ", y)
    print("Number of misplaced tiles (0 means completely solved) ", heuristic_1(x))
    print("Time on heuristic:", solver1.Htime)
    print("Total time in function: ", solver1.Ttime)

    # time, total time, num expanded nodes, soln length
    return solver1.Htime, solver1.Ttime, solver1.expanded_nodes, y, heuristic_1(x)

    
    
def actualRecursionH2(solver):
    h2 = []
    i = 0
    f_limit = 40
    
    if solver.front:
        solver.path = solver.front[i]
        h2.append(solver.path[0])
        solver.front = solver.front[:i] + solver.front[i+1:]
        endnode = solver.path[-1]
        if endnode == solver.end: return
        if endnode in solver.expanded: return
        for k in moves(endnode):
            if k in solver.expanded: continue
            star_time = datetime.now()
            if (heuristic_2(k)+ solver.depth) > f_limit:
                solver.Htime += millis(star_time)
                #print('flimit reached h1', solver.depth)
                solver.depth = 0
                continue
            star_time = datetime.now()
            newpath = [solver.path[0] + heuristic_2(k) - heuristic_2(endnode)] + solver.path[1:] + [k]
            solver.Htime += millis(star_time)
            solver.front.append(newpath)
            solver.expanded.append(endnode)
        solver.expanded_nodes += 1
        solver.depth+=1
        actualRecursionH2(solver)
    

def RBFS_H2(front, end, path):
    solver2 = Solver(path, front, end)
    stime = datetime.now()
    actualRecursionH2(solver2)
    solver2.Ttime += millis(stime)
    #print('solver', solver1)
    #path.pop(0)
    print("RBFS With H2")
    print("Number of expanded nodes:",solver2.expanded_nodes)
    y = 0
   # print("front ", solver1.path)
    for x in solver2.path:
        y += 1
    print("Solution length: ", y)
    print("Number of misplaced tiles (0 means completely solved) ", heuristic_1(x))
    print("Time on heuristic:", solver2.Htime)
    print("Total time in function: ", solver2.Ttime)
    
    # time, total time, num expanded nodes, soln length
    return solver2.Htime, solver2.Ttime, solver2.expanded_nodes, y, heuristic_1(x)


def iterative_deepening_astar_h1(start,end):
    #a*
    t = 0  # time spent on heuristic
    totalT = 0  # total time in function
    star_time = datetime.now()
    front = [[heuristic_1(start), start]]
    t += millis(star_time)
    expanded = []
    expanded_nodes=0
    stime = datetime.now()
    while front:
        i = 0
        for j in range(1, len(front)):
            if front[i][0] > front[j][0]:
                i = j
        path = front[i]
        front = front[:i] + front[i+1:]
        endnode = path[-1]
        if endnode == end:
            break
        if endnode in expanded: continue
        for k in moves(endnode):
            if k in expanded: continue
            star_time = datetime.now()
            newpath = [path[0] + heuristic_1(k) - heuristic_1(endnode)] + path[1:] + [k]
            t += millis(star_time)
            front.append(newpath)
            expanded.append(endnode)
        expanded_nodes += 1
        if expanded_nodes > 10000: break

    totalT += millis(stime)
    path.pop(0)
    print("A* algo using heuristic 1")
    print("Number of expanded nodes", expanded_nodes)
    y = 0
    for x in path:
        y += 1
    print("Solution length: ", y)
    print("Number of misplaced tiles (0 means completely solved) ", heuristic_1(x))
    print("Time on heuristic:", t)
    print("Total time in function: ", totalT)
    #print_path(path)

    # time, total time, num expanded nodes, soln length
    return t, totalT, expanded_nodes, y, heuristic_1(x)


def iterative_deepening_astar_h2(start,end):
    #a*
    t = 0
    totalT = 0
    star_time = datetime.now()
    front = [[heuristic_2(start), start]]
    t += millis(star_time)
    expanded = []
    expanded_nodes=0
    stime = datetime.now()
    while front:
        i = 0
        for j in range(1, len(front)):
            if front[i][0] > front[j][0]:
                i = j
        path = front[i]
        front = front[:i] + front[i+1:]
        endnode = path[-1]
        if endnode == end:
            break
        if endnode in expanded: continue
        for k in moves(endnode):
            if k in expanded: continue
            star_time = datetime.now()
            newpath = [path[0] + heuristic_2(k) - heuristic_2(endnode)] + path[1:] + [k]
            t += millis(star_time)
            front.append(newpath)
            expanded.append(endnode)
        expanded_nodes += 1
        if expanded_nodes > 10000: break

    totalT += millis(stime)
    print("A* algo using heuristic 2")
    print("Number of expanded nodes", expanded_nodes)
    y = 0
    for x in path:
        y += 1
    print("Solution length: ", y)
    print("Number of misplaced tiles (0 means completely solved) ", heuristic_1(x))
    print("Time on heuristic:", t)
    print("Total time in function: ", totalT)
    #print_path(path)

    # time, total time, num expanded nodes, soln length
    return t, totalT, expanded_nodes, y, heuristic_1(x)

def moves(mat):
    #returns all possible moves
    output = []

    m = eval(mat)   
    i = 0
    while 0 not in m[i]: i += 1
    j = m[i].index(0); #blank space (zero)

    if i > 0:
        m[i][j], m[i-1][j] = m[i-1][j], m[i][j];  #move up
        output.append(str(m))
        m[i][j], m[i-1][j] = m[i-1][j], m[i][j];

    if i < 3:
        m[i][j], m[i+1][j] = m[i+1][j], m[i][j]   #move down
        output.append(str(m))
        m[i][j], m[i+1][j] = m[i+1][j], m[i][j]

    if j > 0:
        m[i][j], m[i][j-1] = m[i][j-1], m[i][j]   #move left
        output.append(str(m))
        m[i][j], m[i][j-1] = m[i][j-1], m[i][j]

    if j < 3:
        m[i][j], m[i][j+1] = m[i][j+1], m[i][j]   #move right
        output.append(str(m))
        m[i][j], m[i][j+1] = m[i][j+1], m[i][j]

    return output

def heuristic_1(puzz):
    #   Counts the number of misplaced tiles
    misplaced = 0
    compare = 0
    m = eval(puzz)
    for i in range(4):
        for j in range(4):
            if m[i][j] != compare:
                misplaced += 1
            compare += 1
    return misplaced

def heuristic_2(puzz):
    #   Manhattan distance
    distance = 0
    m = eval(puzz)
    for i in range(4):
        for j in range(4):
            if m[i][j] == 0: continue
            distance += abs(i - (m[i][j]/4)) + abs(j -  (m[i][j]%4));
    return distance

def print_path(path):
    for i in path:
        print(i)

def millis(start_time):
   dt = datetime.now() - start_time
   ms = (dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0
   return ms
