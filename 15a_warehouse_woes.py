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
moves = ''

for line in stdin:
    moves += line.strip()

direc = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1)
}

def go(move, r, c):
    dr, dc = direc[move]
    dr += r
    dc += c

    if matrix[dr][dc] == '#':
        return False
    if matrix[dr][dc] == '.':
        matrix[r][c], matrix[dr][dc] = matrix[dr][dc], matrix[r][c]
        return True
    if matrix[dr][dc] == 'O':
        canmove = go(move, dr, dc)
        if canmove:
            matrix[r][c], matrix[dr][dc] = matrix[dr][dc], matrix[r][c]
            return True

for i in range(n):
    for j in range(m):
        if matrix[i][j] == '@':
            r, c = i, j

for move in moves:
    if go(move, r, c):
        dr, dc = direc[move]
        dr += r
        dc += c
        r, c = dr, dc
    
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'O':
            ans += 100*i + j
    
print(ans)
