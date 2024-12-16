from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import *
import heapq

ans = 0
matrix = []

r, c = 0, 0

for line in stdin:
    matrix.append(list(line.strip()))

n, m = len(matrix), len(matrix[0])

for i in range(n):
    for j in range(m):
        if matrix[i][j] == '^':
            r, c = i, j
            break

directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
dir = 0
while 0 <= r < n and 0 <= c < m:
    nr, nc = r + directions[dir][0], c + directions[dir][1]

    if 0 <= nr < n and 0 <= nc < m and matrix[nr][nc] == '#':
        dir = (dir+1)%4
    else:
        matrix[r][c] = 'X'
        r, c = nr, nc

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'X':
            ans += 1
print(ans)
    