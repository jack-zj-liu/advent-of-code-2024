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

come_from = dict()
xs = defaultdict(list)

directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
dir = 0

def run(r, c, dir):
    seen = set()
    ok = False
    while 0 <= r < n and 0 <= c < m:
        if (r, c, dir) not in seen:
            seen.add((r, c, dir))
        else:
            ok = True
            break

        nr, nc = r + directions[dir][0], c + directions[dir][1]

        if 0 <= nr < n and 0 <= nc < m and matrix[nr][nc] == '#':
            dir = (dir+1)%4
        else:
            r, c = nr, nc

    return ok

while 0 <= r < n and 0 <= c < m:
    nr, nc = r + directions[dir][0], c + directions[dir][1]

    if matrix[r][c] == '.':
        matrix[r][c] = '#'
        ok = False
        if dir == 0:
            ok |= run(r+1, c, dir)
        elif dir == 1:
            ok |= run(r, c-1, dir)
        elif dir == 2:
            ok |= run(r-1, c, dir)
        else:
            ok |= run(r, c+1, dir)
        
        if ok:
            matrix[r][c] = 'O'
            ans += 1
        else:
            matrix[r][c] = '_'

    if 0 <= nr < n and 0 <= nc < m and matrix[nr][nc] == '#':
        dir = (dir+1)%4
    else:
        r, c = nr, nc

# print()
# for row in matrix: 
#     print(''.join(row))
print(ans)
    