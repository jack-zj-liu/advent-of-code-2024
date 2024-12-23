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
    matrix.append(list(line))

nwalls = deepcopy(matrix)

n, m = len(matrix), len(matrix[0])

dir = ((-1, 0), (1, 0), (0, -1), (0, 1))

for i in range(n):
    for j in range(m):
        walls = 0

        for dr, dc in dir:
            dr += i
            dc += j
            if dr < 0 or dr >= n or dc < 0 or dc >= m or matrix[dr][dc] != matrix[i][j]:
                walls += 1

        nwalls[i][j] = walls

def bfs(r, c):
    area, walls = 1, nwalls[r][c]
    letter = matrix[r][c]
    matrix[r][c] = '_'
    for dr, dc in dir:
        dr += r
        dc += c

        if 0 <= dr < n and 0 <= dc < m and matrix[dr][dc] == letter:
            na, nw = bfs(dr, dc)
            area += na
            walls += nw

    return area, walls

for i in range(n):
    for j in range(m):
        if matrix[i][j] != '_':
            area, walls = bfs(i, j)
            ans += area * walls

print(ans)