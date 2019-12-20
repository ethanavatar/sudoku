#!/bin/python3

from pprint import pprint

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

def solve(board):
    point = ()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                point = (i, j)
    if not point:
        return True
    else: row, col = point
    
    for i in range(1, 10):
        if check(board, i, (row, col)):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False

def check(board, num, pos):
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