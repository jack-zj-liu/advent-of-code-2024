from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import * 
import heapq

matrix = []
ans = 0

robots = []

for line in stdin:
    if line != '\n':
        line = list(line.strip())
        matrix.append(line)
    else:
        break

n, m = len(matrix), len(matrix[0])

for i in range(n):
    newline = []

    for j in range(m):
        if matrix[i][j] == '#':
            newline.extend(['#', '#'])
        elif matrix[i][j] == 'O':
            newline.extend(['[', ']'])
        elif matrix[i][j] == '.':
            newline.extend(['.', '.'])
        elif matrix[i][j] == '@':
            newline.extend(['@', '.'])

    matrix[i] = newline

moves = ''

for line in stdin:
    moves += line.strip()

direc = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}

n, m = len(matrix), len(matrix[0])

def detect(move, r, c):
    dr, dc = direc[move]
    dr += r
    dc += c

    if matrix[r][c] == '#':
        return False
    elif matrix[r][c] == '.':
        return True
    else:
        if move == '^' or move == 'v':
            if matrix[r][c] == '[':
                return detect(move, dr, dc) and detect(move, dr, dc+1)
            if matrix[r][c] == ']':
                return detect(move, dr, dc) and detect(move, dr, dc-1)

def go(move, r, c):
    dr, dc = direc[move]
    dr += r
    dc += c

    if matrix[r][c] == '#':
        return False
    elif matrix[r][c] == '.':
        return True
    else:
        if move == '^' or move == 'v':
            if matrix[r][c] == '[':
                if detect(move, r, c) and detect(move, r, c+1):
                    go(move, dr, dc)
                    go(move, dr, dc+1)
                    matrix[r][c], matrix[dr][dc] = matrix[dr][dc], matrix[r][c]
                    matrix[r][c+1], matrix[dr][dc+1] = matrix[dr][dc+1], matrix[r][c+1]
                    return True
            if matrix[r][c] == ']':
                if detect(move, r, c) and detect(move, r, c-1):
                    go(move, dr, dc)
                    go(move, dr, dc-1)
                    matrix[r][c], matrix[dr][dc] = matrix[dr][dc], matrix[r][c]
                    matrix[r][c-1], matrix[dr][dc-1] = matrix[dr][dc-1], matrix[r][c-1]
                    return True
        else:
            canmove = go(move, dr, dc)
            if canmove:
                matrix[r][c], matrix[dr][dc] = matrix[dr][dc], matrix[r][c]
                return True
            
r, c = 0, 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == '@':
            r, c = i, j

for move in moves:
    dr, dc = direc[move]
    dr += r
    dc += c

    if matrix[dr][dc] == '.':
        matrix[r][c], matrix[dr][dc] = matrix[dr][dc], matrix[r][c]
        r, c = dr, dc
    else:
        if go(move, dr, dc):
            matrix[r][c], matrix[dr][dc] = matrix[dr][dc], matrix[r][c]
            r, c = dr, dc

for i in range(n):
    for j in range(m):
        if matrix[i][j] == '[':
            ans += 100*i + j

print(ans)
