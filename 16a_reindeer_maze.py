from sys import stdin
from collections import *
from itertools import *
from math import *
from bisect import *
from copy import * 
import heapq

matrix = []
ans = 0

for line in stdin:
    line = list(line.strip())
    matrix.append(line)

n, m = len(matrix), len(matrix[0])
r, c = 0, 0
endr, endc = 0, 0

direc = ((-1, 0), (0, 1), (1, 0), (0, -1))

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'S':
            r, c = i, j
        if matrix[i][j] == 'E':
            endr, endc = i, j

minheap = [(0, r, c, 1)] # cost, row, col, direction
seen = set()

while minheap:
    cost, r, c, d = heapq.heappop(minheap)
    
    if (r, c, d) in seen:
        continue
    seen.add((r, c, d))

    if (r, c) == (endr, endc):
        print(r, c, cost)
        break

    dr, dc = r + direc[d][0], c + direc[d][1]

    if matrix[dr][dc] != '#':
        heapq.heappush(minheap, (cost+1, dr, dc, d))
    heapq.heappush(minheap, (cost+1000, r, c, (d+1)%4))
    heapq.heappush(minheap, (cost+1000, r, c, (d-1)%4))
