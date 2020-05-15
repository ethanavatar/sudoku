#!/bin/python3

from pprint import pprint

# TODO : Board generator. maybe as a class with the solver functions as children
board = [
    [7,8,0, 4,0,0, 1,2,0,],
    [6,0,0, 0,7,5, 0,0,9,],
    [0,0,0, 6,0,1, 0,7,8,],

    [0,0,7, 0,4,0, 2,6,0,],
    [0,0,1, 0,5,0, 9,3,0,],
    [9,0,4, 0,6,0, 0,0,5,],

    [0,7,0, 3,0,0, 0,1,2,],
    [1,2,0, 0,0,7, 4,0,0,],
    [0,4,9, 2,0,6, 0,0,7,],
]

def solve(board : list):

    # point : the current position to solve
    point = ()

    # iterate through each row and set `point` to the first unsolved position
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                point = (i, j)

    # if and unsolved position isnt found, the board is solved
    if not point:
        return True

    # if an unsolved position has been found, split up its coordinates
    else:
        row, col = point
    
    # check every number from 1 to 10 if its valid with the current board, else, set it back to 0
    for i in range(1, 10):
        if check(board, i, point):
            board[row][col] = i

            # I dont like recursion, but this is the only way i could figure it out
            if solve(board):
                return True

            board[row][col] = 0
    return False

def check(board : list, num : int, pos : tuple) -> bool:
    '''
    Takes an input list (`board`) and checks if an int (`num`) is a valid solution at the coordinates provided (`pos`)
    '''
    for i in range(len(board)):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    xbox = pos[1] // 3
    ybox = pos[0] // 3
    for i in range(ybox * 3, ybox * 3 + 3):
        for j in range(xbox * 3, xbox * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True
    
solve(board)
pprint(board)