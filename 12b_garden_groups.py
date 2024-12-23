from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import *
from functools import cache
import heapq

matrix = []
ans = 0

for line in stdin:
    line = line.strip()
    matrix.append(['_'] + list(line) + ['_'])

n, m = len(matrix), len(matrix[0])
filler = ['_'] * m

matrix = [filler] + matrix + [filler]
n, m = len(matrix), len(matrix[0])
og = deepcopy(matrix)
sidescnt = deepcopy(matrix)

dir = ((-1, 0), (1, 0), (0, -1), (0, 1))

def bfs(r, c):
    area, sides = 1, 0
    letter = matrix[r][c]

    if letter != og[r-1][c] and letter != og[r][c-1]:
        sides += 1
    if letter != og[r][c+1] and letter != og[r+1][c]:
        sides += 1
    if letter != og[r-1][c] and letter != og[r][c+1]:
        sides += 1
    if letter != og[r+1][c] and letter != og[r][c-1]:
        sides += 1

    if letter == og[r+1][c] == og[r][c+1] and letter != og[r+1][c+1]:
        sides += 1
    if letter == og[r-1][c] == og[r][c-1] and letter != og[r-1][c-1]:
        sides += 1
    if letter == og[r+1][c] == og[r][c-1] and letter != og[r+1][c-1]:
        sides += 1
    if letter == og[r-1][c] == og[r][c+1] and letter != og[r-1][c+1]:
        sides += 1

    sidescnt[r][c] = sides

    matrix[r][c] = '_'
    for dr, dc in dir:
        dr += r
        dc += c

        if 0 <= dr < n and 0 <= dc < m and matrix[dr][dc] == letter:
            na, nw = bfs(dr, dc)
            area += na
            sides += nw

    return area, sides

for i in range(n):
    for j in range(m):
        if matrix[i][j] != '_':
            area, walls = bfs(i, j)
            ans += area * walls

print(ans)